// read_history.js - window.__readI(items, maxPages): this folder's Pangram results read back from his History by SHA-256, in
// the form ingest.py takes ({key: [headline, ai likelihood, words, uuid, timestamp, [[label, confidence, words, start, end,
// first 24 characters], ...]]}). Paste into a pangram.com tab after tools/humanization/pangram_page_helpers.js (which defines
// window.__run). items: [[key, text, sha256], ...].
window.__readI = async (items, maxPages) => {
  const want = {}; for (const [k, t, h] of items) want[h] = k;
  const sha = async t => Array.from(new Uint8Array(await crypto.subtle.digest('SHA-256', new TextEncoder().encode(t)))).map(b => b.toString(16).padStart(2, '0')).join('');
  const out = {};
  let url = 'https://web.pangram.com/api/history-list/?limit=20&offset=0';
  for (let p = 0; url && p < (maxPages || 4) && Object.keys(out).length < Object.keys(want).length; p++) {
    const l = await fetch(url, {credentials: 'include'}).then(r => r.json());
    const ds = await Promise.all((l.results || []).map(it => fetch('https://web.pangram.com/api/history/' + it.uuid + '/', {credentials: 'include'}).then(r => r.json()).then(d => [it, d])));
    for (const [it, d] of ds) {
      const k = want[await sha(d.prompt || '')];
      if (!k || out[k] || !d.response || !d.response.overall) continue;
      const o = d.response.overall;
      out[k] = [o.headline, Math.round(o.avg_ai_likelihood * 1000) / 1000, o.word_count, it.uuid, it.timestamp,
                (o.windows || []).map(w => [w.label, w.confidence, w.word_count, w.start_index, w.end_index, (w.text || '').trim().slice(0, 24)])];
    }
    url = l.next;
  }
  return out;
};
'readI defined';
