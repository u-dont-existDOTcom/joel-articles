const want = {"ef202eaa691d87ccbfa0ddcbe949bdc33c65688ad779c00db1984c29bc912ce1": "HG15-f-p1", "aead61e5b27f763f4555cfe7c90ccd3f76cdb48d034c8b022ae0a228ef94b61e": "HG15-f-p2+prev", "07e2467b510388412aa52e78eb690e3a195244009680ee7d6f5b95125413bee1": "HG15-f-p3+run", "c264a598e112b8277166d222029b447d05328a5974130871b9aa13aeca5d1a0a": "HG15-f-p6+next", "08f7e9942390f8bf17e50951a266594b6b660e3547a18aa12e32111ef8ca5a73": "HG15-f-p9+next", "be8325f947b9370c5166852fbc18af8a3ef0c0e6b84d6c10e0f2fad0fdfff17d": "HG15-f-p10", "65dacca79b6562b60d3ae1d3dd38a29f2c83d8492d4d0e17b82dfcc55c873fec": "HG15-f-p11", "20ebca54552deb50359470d6f9b3ff27fc41f57c1c3683650821a43eb22f0364": "HG15-f-p12", "9a4e40890e368c705acc20644280deaf60eb5e6f106c523b21637a7645ecbe03": "HG15-f-p13+prev", "582ad7dbde0784315307ae4dbbe7180958796a8ab04b2f33607402130f4d290f": "HG15-f-p14+run", "a4674a587dd9b0ab4673e87448e5f928b1356dfc099093b396fd757fb98faa17": "HG15-f-p18+prev", "82756d12b867fbf1868c88b99516a8985ecaecbb9d5380f472574bc8cab11d68": "HG15-f-p19+prev", "2d6e1fc5b9e2d850dd49b1afe41fe5470735ce3f179b15f5364cb227dd1d44e2": "HG15-f-p20+prev", "10f4e3d86348fd1a5009840ec6cfc7dab0adf9961fc4beb25e2a34501a4bb09c": "HG15-f-p21+next", "099da81ee03c75ae9907a4c099dfe9baade176136a49e12db43ec1ee21b52085": "HG15-f-p22", "f50907813b18cfe960f12599603ab5dfc79010e1ec19bbb5be5fb8facd1a2d41": "HG15-f-p23", "878a19d7b4b51d74d62f2732c5d2c8d377ae78b4a827a39c6fecfb8ff6512861": "HG15-f-p24+prev", "18fffb6f9f05516d3924adfd16a1040994a2ca1e666a7367b8aff0a3a2ea311e": "HG15-f-p25+next", "30032ac44eed996db156cc2f7c33ee1254e8f5098f0d13cac04189daee313a40": "HG15-f-p28+next", "f4c1b30520726e31a8a939098cee5e209a7c5dfb95c52eecbaf9491b3bc82f9a": "HG15-f-p31+prev", "e1e5a5570a3ed1d6d69db794308c81c3809a50997b2dc0f26facfbc0299a8e7d": "HG34-f-p1", "8e2c6412d98253c06d0bbb96e10ee11a3d1363039d7bae24e424f3ff3392e34c": "HG34-f-p2+next", "e45ccfd59cc1812c5b69a27eeda07bccf51f5d7c03dad2dd23ed8e20c4c9a0dc": "HG34-f-p4+prev", "3e20a414c2ec3d1904bf4312d74c16b6e47b9009ca16c68bad8dbb1a0306fabc": "HG34-f-p5", "dd16d292800273b353339e1667902523017a01bdb9e1c98764999610ac00aedf": "HG34-f-p6+next", "d5774c3c2f15e969fc37626270e126f074a0f7b04f640dc1044942d4d8e5b90e": "HG34-f-p7", "b46f2a5aa51d88b0ccd11f1e72618630515639b18a748718c72ff1c328cb6a95": "HG16-rfix", "c22f58bb2a88bd44f5646535217c08f4d6700e11beee943dbf78ff6567b998fb": "HG38+39-rfix", "9c29cffa16611ded4bfd2684bfa17388c6a2a3579d93c659da522a2f799eb5ad": "HG20-rfix2", "608bb55320dee10f1e93294572b4a257937208ef83549824b39acc2e886bb114": "HG20-z-p8"};
const sha = async t => Array.from(new Uint8Array(await crypto.subtle.digest('SHA-256', new TextEncoder().encode(t)))).map(b => b.toString(16).padStart(2, '0')).join('');
const out = {};
let url = 'https://web.pangram.com/api/history-list/?limit=20&offset=0';
for (let p = 0; url && p < 5 && Object.keys(out).length < Object.keys(want).length; p++) {
  const l = await fetch(url, {credentials: 'include'}).then(r => r.json());
  // each page's details in parallel (2026-10-17: the History is shared with other lanes and fills fast)
  const ds = await Promise.all((l.results || []).map(it => fetch('https://web.pangram.com/api/history/' + it.uuid + '/', {credentials: 'include'}).then(r => r.json()).then(d => [it, d])));
  for (const [it, d] of ds) {
    const k = want[await sha(d.prompt || '')];
    if (!k || out[k]) continue;
    const o = d.response.overall;
    const n = (d.prompt || '').replace(/\n{2,}/g, '\n');  // window indexes count a blank line as one newline
    const words = w => { const s = n.slice(w.start_index, w.end_index).trim();
      return s.startsWith((w.text || '').trim().slice(0, 30)) ? s : (w.text || '').trim() + '…'; };
    out[k] = {history_id: Number(it.id), link: 'https://www.pangram.com/history/' + it.uuid,
              utc: new Date(it.timestamp).toISOString().replace(/\.\d+Z$/, 'Z'), words: o.word_count,
              avg_ai_likelihood: o.avg_ai_likelihood, headline: o.headline, version: o.version,
              windows: (o.windows || []).map(w => w.label + ', ' + w.confidence + ', ' + w.word_count),
              flagged: (o.windows || []).filter(w => w.label !== 'Human').map(w => w.label + ' (' + w.word_count + ' words): ' + words(w))};
  }
  url = l.next;
}
JSON.stringify(out)
