const want = {"4df928cc8cb4d9a46ef340bb24fab3f2b3efa7a16e74f1f671533ea940071e16": "t54_O2b", "f2abfadff5157a71c7cf4efc7fcbf7a70a12c1dff5a500a159c7fee824b24c2b": "t54_G1f", "d40849550af265249f4d679bb886b3cdbcbe8772f85f00bb059d14bf5dae9743": "t54_G2f", "16eb6c138c6dcdeb4e99160940b8e0528677e3ff049e64ed1335d5ad20f356af": "t54_SPf", "516debd7ce901db6fe7927a31005f9ec1d2aaa171c1be4cf8de9777c4bc107d2": "t54_open2", "ba46ff5b3b439d618ac8cfa6e48333b62674fa03d7cc05dbb02e9e4c1fdebf89": "t54_play_h2b", "1fdb0ddcc73fa848abe626b6bc49db93d7aee05af7982b71f7828fc09185ac30": "t54_spirit_h3b", "ac55315f407064d9c40acd23ae6f52de668319a5f8cc91730ed3c211f37e09ea": "t54_borrow_h2b"};
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
