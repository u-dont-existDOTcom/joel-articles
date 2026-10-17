const want = {"5fcb21ce351e54368417dbc152eefd9010131b537dbe16d773f39cb78f31d0e5": "t70d_thl", "317010e1b34e48a77e90fc7c2ea780bcc71d28fa13050ca0dd676d8c9e53f5fb": "t70d_secks3", "918aaf8cef16e9b300ccb995fcb57274626b09508e893ea037f4822dca6b9ced": "t70d_sp5p2y1", "075f07a0bf20518faad6e86e2ec0c4663c0a9166bc6784d52ceaa6e23bfb0a0f": "t70d_sp5p2y2", "0da4894d02eac03bd1b2956ab26483b74df797b2a76db8f3a9150852af079730": "t70d_secsp5y1", "885a246847cafbd48d8ad64a04af3f773d3ee638f20e2430866fe4b8020a9c89": "t70d_secsp5y2"};
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
