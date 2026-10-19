const want = {"2b01605ef8709652e132ff544436d3ebe8dec7c1c5da0142c5b8685f2da2d0e7": "t74a_jchk3", "98c2fdf95d30fe5f4e05605093cb2eb55a264dc757780b086b5588adfe937179": "t74a_fat2", "693a98fb7fdaba8282400b891c6501900db3470b6b3f9739c674592c32b3db1d": "t74a_fat3", "ca2d0ffe87993c704780851929f9aca93730bb2d0a73a12c48cfb59ae8b36b41": "t74a_fat4", "b126a5bcd90ece3fb8168720352d64cf58a618469179399dca0baff36f19b3f6": "t74a_fat5", "a4121e8848c720808bf3a5d30854089773f4220ac9151e20ab5cfa282438eed3": "t74a_h1bg", "cd8c551a21f3e05346688652dab609747226645591c241edb034afa33bd53f98": "t74a_h1fat", "e159b306c3ab308fbbbba39f76af4ff852e89515331818648c1de846e6695e50": "t74a_h1app"};
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
