const want = {"8777aa6c9fb41ab411d1c1496236f548d1ae12910254b80ea3c0fd0a0f5ea893": "t65l_sp1p2a", "9ea3e2b2fda4463f59a527f6c976520d3a49f14730fe75f42fe5c2024bfe4504": "t65l_sp1p2c", "5890312355236dc3565b3b8fab35f7e1aeb7c546e2bd7154b8dfec0a94b92092": "t65l_sp1p2d", "83ca3ff0883a71353964234b1cc8e98edeee9914de43c659f715a3214dfc7040": "t65l_sp1p2e", "ef51bef579eadc1e90b10eec01584d44312d2d28aec8a464db85dc0e66854de6": "t65l_pairsp1p2a", "2dc9e2e9d73beaa90daec9a895be750f6cf073aeb3facf483a59cca24e55e68a": "t65l_pairsp1p2c", "d7a50f70996a6526216df4e5704344cc441ce9655e234d0fc8e2936d0163c7e0": "t65l_pairsp1p2d", "980154ce5437a3f07da951a0be00461f0b8fe81644485b0148411d01b4e16766": "t65l_pairsp1p2e", "00cca2454c6c87b442d9937ddd33ef492deda901e9ce24df0f60b1c0e8fc06ac": "t65l_secsp1p2a", "2c4348a9839a4273aaa90246d210c96a5fe25f21a20d2cefe86a2ba6d1ebeb97": "t65l_secsp1p2c", "dc192425a7816b8312325417acf00f19c6b7311c2ad27357967dbcbc6522adc7": "t65l_secsp1p2d", "fd511c38f5a84997e690f94d8c1aee3b7b88180e8a6744aaf9e39a0db50d550d": "t65l_secsp1p2e", "a7483240510dcbb5a79c77c26b91deea5b2e4e3e86f9d51651d05612039b43bb": "t65l_sec2sp1p2a", "d6ebb11b41f5cc1345aab25a3438e0675c10c8abdb1cc498decf01a6c8ad0bb4": "t65l_sec2sp1p2c", "69ee93f9c9ecd0d6616d946f3f53a4437f552031975aa360be437623ab6c54bf": "t65l_sec2sp1p2d", "9f36acf5e1f2619864f070f613398b90eec12961490b3a5909c853e48e83904e": "t65l_sec2sp1p2e"};
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
