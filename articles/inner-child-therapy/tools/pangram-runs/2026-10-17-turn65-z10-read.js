const want = {"526e25fe0c5e067c7e96d1e2a1ae296379f2d4241d976f9f91b6ebc4fe85b35f": "t65z10_sp8p1w4p1", "f32183a9b069bdd08a3916d5eb51635a5660bc4c838e604f273bc51804ddf808": "t65z10_p14w7p1", "900669d6af1ad48d3d7978df38fa7de959b2e45eb6d36e9712796d176b2a07dd": "t65z10_p14w6p1", "5c8476c1f120ff08a91dc6431c5d922638b64e8c03b5902ac3af0248f619f79c": "t65z10_ba1p2w2p1", "cb20299ec66a9971b7cc3e240b73f6e4f05c8488387e24bd83f98b871a71330f": "t65z10_secba1p8q2", "bb73efb2dacd94a9725a31abdbd9ab602295c46ad9c10c6a97d51c7c58bc066d": "t65z10_secba1p9q2", "7bcab8ae24d18a27b211c862c5ab9673cca5e59f9b7e995be2c13718303a8aff": "t65z10_secsp8m4", "c55d84428a9ebfcd2fe7ccff650a39925ae5300840f915fa0602e26a34d4f67e": "t65z10_secp14h1w7", "5a7da70fbd7951d6e77dac7bb7b65a667565ad77c9791aa5bbac4829739d41c8": "t65z10_secp14h1w6", "57962b96f8b370f54561dcc9624e578ce554b2495956ccafc24215369608dc70": "t65z10_secp14h2w7", "0723c9bb40de2736808a04221c05e51718eb227346b57624fdceaa83dc4e8f40": "t65z10_secp14h2w6"};
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
