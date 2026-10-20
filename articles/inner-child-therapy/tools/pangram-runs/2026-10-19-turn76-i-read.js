const want = {"c1160353c72072e41a7599658b1a625ddf27e7f7956d4a125bf15aefb0793e0a": "t76i_ue27h", "7270d1022ce77d17797b0e58e0d5618154b23f20b5e58cbcf77a10f092f338f5": "t76i_ue29c", "521e6fb733e389fd2b7b171b698354636bf618a8855d09a0e449dcfe60aab8ae": "t76i_as4bg", "b8a436e3ccb0861b15cc66380e7b556ce71254ee9511c87b76fbbe01b7af2297": "t76i_ba3f", "c78907d25d89bf1ae31e51cd407a46a610840122fe776e257e2bb622f07ddb3c": "t76i_h1wa", "e135d686f8e2b06d887ece2d5407889ca3d1d167dea4e5d127e8cea39dee74a4": "t76i_h1as", "2032d3d03d8813cb632e3cd361e71a2763ba2bbae572a172bff495c41d4132e6": "t76i_h1ba", "09d31d5bad957b019909f749853f90c4eec15b9d32f4b1d1e0f2433bf78b6ce1": "t76i_h1bt", "eaa894327521195327fc9779dceaf0b8fae607847d558781cfbcff9449719227": "t76i_h2he"};
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
