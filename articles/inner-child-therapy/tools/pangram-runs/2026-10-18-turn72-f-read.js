const want = {"0514bf0a1cf290b5ac0d4a407211ad35835469867a8cdceb3372062011926e33": "t72f_ifsguidec", "e47bb169362e4ab06b40a3c02bfb90bae8feeb52f7cc94e6abcc7f342969112c": "t72f_h1bgf1", "30d6e6db18e6098d65cdb9e067adc2ea628d26ea743b6a002c0868df577e8ce5": "t72f_h1bgf2", "622e3538f5c4ee628cabbaa48fff29fa0ae838e881b811aa51f42f8f4c0e27e3": "t72f_h1bgf3", "cc2829edb3b1cbf66b619987ff8443f5ef19ca8bf7f8606b2fc9fa59fd425594": "t72f_h1bgf4", "0c56389feb091e49b4bccaa43c2e1171de06cce7f144df0573772654bad189b8": "t72f_h1appf5"};
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
