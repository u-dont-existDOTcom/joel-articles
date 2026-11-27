window.__readIdx = async (items, maxPages) => {
  const want = {}; for (const [k, t, h] of items) want[h] = k;
  const sha = async t => Array.from(new Uint8Array(await crypto.subtle.digest('SHA-256', new TextEncoder().encode(t)))).map(b => b.toString(16).padStart(2, '0')).join('');
  const out = {};
  let url = 'https://web.pangram.com/api/history-list/?limit=20&offset=0';
  for (let p = 0; url && p < (maxPages || 4) && Object.keys(out).length < Object.keys(want).length; p++) {
    const l = await fetch(url, {credentials: 'include'}).then(r => r.json());
    const ds = await Promise.all((l.results || []).map(it => fetch('https://web.pangram.com/api/history/' + it.uuid + '/', {credentials: 'include'}).then(r => r.json()).then(d => [it, d])));
    for (const [it, d] of ds) {
      const k = want[await sha(d.prompt || '')];
      if (!k || out[k]) continue;
      const o = d.response.overall;
      out[k] = {uuid: it.uuid, at: new Date(it.timestamp).toISOString().slice(0, 19) + 'Z', headline: o.headline, ai: o.avg_ai_likelihood, words: o.word_count,
                windows: (o.windows || []).map(w => [w.label, w.confidence, w.word_count, w.start_index, w.end_index])};
    }
    url = l.next;
  }
  return out;
};
'readIdx defined';
