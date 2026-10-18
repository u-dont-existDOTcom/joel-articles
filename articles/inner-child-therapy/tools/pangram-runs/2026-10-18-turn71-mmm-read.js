const want = {"7bbd049cfa22a86e1c6826224929c34ef32feca3f81e6b6ccdfe1d0b3cced6db": "t71mmm_tf11h", "83f3eca147bb44d4fe9153ae25c2a251b72d1a53d9887aed1eb44b33a37b3694": "t71mmm_h1tf11h", "a35ada9fedc1de97ce8263740a66864a1340ca28b630bbc998d503fdd45c7ac0": "t71mmm_wlu3", "81436ff334284eacfb0a7067301a51f3b4bda733dbc6ae2d51231dcf2e474df8": "t71mmm_h1wl3", "8aefa97701006ceccb3c24e1ac347d18f915e109f6494b9c8a3ba8c57d69844e": "t71mmm_wlu4", "6a16a5e016da9814cdc9d097922b4818071919a042e7abae03fe9c63dde15cfe": "t71mmm_h1wl4a", "98fadbf5bbda93cb63fe8098fb77d03217219660207b1dcd34989449b7ae2390": "t71mmm_h1wl1a"};
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
