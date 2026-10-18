const want = {"6a26e6306b13257b502df331d2cd52830906020fbf0d5c442f22ec2a839553a5": "t71ww_ifs1u", "2f57881846d5735843b56c0bd2a58e5535d3597228acae521f29a1c08194c7ea": "t71ww_ifs2u", "f611b373654ae42d883cb385226c6ae47ba1cbb25a31bdbb91cb21c10430ed5d": "t71ww_ifs3u", "7b43921534b8027a37e37e5c0968d2aee039f8960b12c260bb43ea2febf27c94": "t71ww_ifs5t", "564a2c60cbaa7902fca7e17c4d2236621db49f7adb8c4c469c1ad9602fb70a0f": "t71ww_secifsu", "677e791e5d3320d518079c755c90625cc68db1b6cb8b9007753a8f86332572c4": "t71ww_ifs12u", "584f5159cd20014ad4da91e51ef8d19f39b3b6c2302687f9238fc6b777897021": "t71ww_ifs34u", "afafcc5003d08e386b709cfa08a15cb3e2fdb7faa52ffd533272018ceffe5bd3": "t71ww_ifs56u"};
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
