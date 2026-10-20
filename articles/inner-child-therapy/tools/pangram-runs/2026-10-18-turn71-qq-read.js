const want = {"ffc12daca6c5a9a8ce2d08c41fd54c33a7e89c9d919c4f3916f577488f2251aa": "t71qq_oicc", "e51cde7229db86f841c77a4ee196a1bf3c72dd15cffc2d247903a8ffa9c9411e": "t71qq_oidd", "9a2abc1bdb735ef07c524d9b42757dacc623443a6852605f2e5b275fa43c96c9": "t71qq_oi2b", "e962a850ae95799aaae1790736310d5b3cc6250dfe23b51a13049dc57cfb4d76": "t71qq_oi2c", "b463a39c903372c31d3718a2f4d1836b0030654bc3f0783030a2a7efa87c9c0e": "t71qq_oi3c", "b98593a36308cbd40e4b0f73b2f35fa75fc4076581cbabb12f83b439528bd573": "t71qq_oi3d", "803a052f18b574a8a14a2b3b2232aee7b6f4bb5b8d6c1567412d19fa5c9b8847": "t71qq_secoicc", "88c4716e3414d288d584727a7fcb033c3634232560ead35a03bc1a1110c9b6a1": "t71qq_secoicc2", "00e16ab3829a6ad5cbd3ef7db6a52e5d9d9aabfb761fb1e0f9d6cae1891b4484": "t71qq_secoidd", "eab1e693057670ff5429c8a05d7586ae63ecb60dcc1977492c65ccafa7f90a35": "t71qq_secoidd2"};
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
