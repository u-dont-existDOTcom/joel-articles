const want = {"58b4b65617dcc9f355dcf6a3a7fd987274be5ccbdcc6b404e5e7086c7a3ca8a7": "t65z8_ba1p1w8p1", "e9470cac4436f80db0c559b78479c966482e23c2e602f7baff0cb7cc658f84c5": "t65z8_ba1p1w9p1", "2c57d41df5f5c2ecdcb0abfab286ae43cccbd020fa600951fe7699ce3911802d": "t65z8_ba1p2w8p1", "9d5f4f7c3b83d34ef9c38204dc0023403a8c43f313e03545c3dc788ef1893cac": "t65z8_ba1p2w9p1", "0880a846f9ee0f1d53c78722e4ec7cbd6e98d4c9c85a230177630dfedde64a75": "t65z8_secba1p8p8", "45130183c9a3f0274d1ca26f1df3153a2e90cdabea768a9ebcab224a2c7d547a": "t65z8_secba1p8p9", "0d2909a22a7514f2a39350a617209bd79fa8ec5158743a9a4371464e2c65fb8b": "t65z8_secba1p9p8", "a4aa2702dda8689164ec6cecd359d807e9aea33a5f408490bf776d1ca7e0838f": "t65z8_secba1p9p9"};
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
