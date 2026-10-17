const want = {"4ac2cacb78a4a059bfcd6dc36e8051e6f76a989b2a3f287098409df5b331e50c": "t65k_sp1p1a", "e86c8c22909ca4905862d2caf0ee109e8f445c0ee95b6bb32ab0739deaf20321": "t65k_sp1p1b", "a6b36bd2a98c99e7d0efb4f6f48caafebba7a0c491b129dca319a1c4eef3560f": "t65k_sp1p1d", "1b2f1b1d5d59504a196d733513c4923a61241fa370345bf025a1b40d606ea900": "t65k_sp1p1e", "7800af4a70e36e6401fc2abf4d8799ccaa83f198b2392febbb6252e1c9368fc7": "t65k_secsp1p1a", "20a7b16491bad188c5b2c946b2117d4504a1931accfe0bbacd5ab7b06eb5422b": "t65k_secsp1p1b", "0601ffea969ef54cc8fbbf3c827b5162b18d6a95eaeebb6b7fa687dd55c9a788": "t65k_secsp1p1d", "7efba2d2d1ac5d89b73021e72f5c94341e0b1e5ad3ecc93a6b8b32d4625761b5": "t65k_secsp1p1e", "33298b11c30774f573fc20e1d907689930f4a74fae5ce6ab98c8ad507b0a1469": "t65k_sec2sp1p1a", "6341a483618cba75657127c0f4d250f7931bb38aabbd3741a13dc34964e719ae": "t65k_sec2sp1p1b", "96915d55f61e10c0c9e48176ba6b1477c792e2d625072f0f31137cf04d06b8be": "t65k_sec2sp1p1d", "ecde20285c4eec69695232ddeda50c854c4a68d34932247161255012cd877bfb": "t65k_sec2sp1p1e"};
const sha = async t => Array.from(new Uint8Array(await crypto.subtle.digest('SHA-256', new TextEncoder().encode(t)))).map(b => b.toString(16).padStart(2, '0')).join('');
const out = {};
let url = 'https://web.pangram.com/api/history-list/?limit=20&offset=0';
for (let p = 0; url && p < 5 && Object.keys(out).length < Object.keys(want).length; p++) {
  const l = await fetch(url, {credentials: 'include'}).then(r => r.json());
  for (const it of l.results || []) {
    const d = await fetch('https://web.pangram.com/api/history/' + it.uuid + '/', {credentials: 'include'}).then(r => r.json());
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
