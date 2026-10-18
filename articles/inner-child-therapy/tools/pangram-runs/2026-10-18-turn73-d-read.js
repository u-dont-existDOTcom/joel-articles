const want = {"64b9852244d1f3f5c1b876df5040e5856aacf018f55f2468f4bb8862c036ca3c": "t73d_yb4j", "ae024734f3f593e3c0d878f9c543ae068addfaa2a6618257f743a6fb3ed1bb7f": "t73d_yb4l", "a6ebce6691256cf9f462491f6571e0169216080808f5d5da6c0464b3204fb959": "t73d_h1d1", "6a34bbfc72ff817c9cbc1e2d40327b9f1ea06920ba5b2f00a3ed87a400de0907": "t73d_h1d2", "bf76279920307c32fc56e04f08a064b823e674db3a3da30146a963b1b405af0c": "t73d_h1d3", "af6f666abe0e7bd23dea2635054a43ef0b8fe940cffe9a9d71334cf792feeb9c": "t73d_h1d4"};
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
