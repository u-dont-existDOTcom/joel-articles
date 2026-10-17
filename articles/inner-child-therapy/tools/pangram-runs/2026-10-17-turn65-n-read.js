const want = {"5b789433d9105b82364eac607fe76079f99d627bdb8e15117e3aaed917b0d935": "t65n_sp3p1a", "de825784d255df7ed63ab687101b79e10305cd1e4793a74409da32c9ef645a56": "t65n_sp3p1b", "6c77d99c2090a302fb65eb10ae1f41b501359371aebc5d5fa2fe168099301b60": "t65n_sp3p1c", "5c4e05082bbdf4a6535fb176f3320bc924c15ad24279556284b5292077e9f8d9": "t65n_secsp3p1a", "29a9bcdfe2e7be27303123fb783c6973dedce4e906a17309f08e2d2cd688d01a": "t65n_secsp3p1b", "c66c226eb6b3a06707125b48057df78d1b50052f3ffe4866bb5735dad4f0e801": "t65n_secsp3p1c", "7e948b31f02aa55e5127e77d5d7591e2a35023842b99290a8e112c8ed1478c14": "t65n_sec2sp3p1a", "0f53a67ab66cc82984746f2db440eae51807ace430fa58625e309e7d9a9ebefa": "t65n_sec2sp3p1b", "7bbe5eb9bf06141948a2318c883012c63d26cbc858b7279ecdc440f457819cad": "t65n_sec2sp3p1c"};
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
