const want = {"91210fd3861349a0f8c6f46e94e7ec192af174e917748d8385a1fdf96c0c7fba": "t76e_losh1i", "543a811dbf1ff5a3368441349949e77d14ceefe5cb30582dacacd522e6f60f1c": "t76e_losh2h", "ca8c3745f78fa56643ef91db98549152ad8ea745c0e6a250a51811043e4029c0": "t76e_ue27d", "0a206f90a2cf71d2395c215b7c12f85253f2cae4b598a034108663a9f4398462": "t76e_h1by", "5fab7a87aaba415cf5e2380f5eb375bc34a9a533664abcc37c6e7a0f77f08f18": "t76e_h1by30", "cf479bf7cabb30e0d4304da22cbaceae3770ab06342787c8c37d7eb12789442a": "t76e_h3lo30", "ecc9296061f3effa61eee731d7a5d9d130ef0a85819ceff866cc1be7ecade0bc": "t76e_h1wa"};
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
