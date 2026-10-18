const want = {"86d4ba0c4c3257e208404bf7dd660a4b45a2680256e516f01b455167fcf51b77": "t71tt_oi2p", "adc38de65a187ce65361286818626c6bd2d81e2dcb7bae63f8c4b414f7020598": "t71tt_oi2q", "4f3d7cf82b8374f5ab8e775f8d80ae9b5b28501af9264cdff0ebeff12cb86065": "t71tt_oi2r", "ed03e8d1836b64ed729e2b8d8906986f072ef8506ba221fa7be33abfcdf0832f": "t71tt_secoiddp", "30e14757c540b4100b39b104b6e6b4774ba59e4e535d71cb4e3895b17ce24415": "t71tt_secoiddq", "5a9c2be907630bfb3417c01a253a9c0d9089c7be3cbcc275af731829602478d3": "t71tt_secoiddr"};
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
