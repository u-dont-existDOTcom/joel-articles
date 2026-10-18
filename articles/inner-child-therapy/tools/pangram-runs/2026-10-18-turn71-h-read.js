const want = {"429cdad213d6573837389d74c48b1c4c52265acdf95147abe8b5979556eb0463": "t71h_y1b", "020ccf528e3d4c8cdd41c153f8356b6c7a5644da15e56fd766a3410cfd3ccadd": "t71h_x3c2", "cede74566198900ea0aba5e6669261ea678b03d0b876980506c951ac36a302d6": "t71h_as1c", "42524a0390d6a5f7ed2c972215314ec65ec4853e9eb06f4ba7e52eaa9f3c6d09": "t71h_artrb", "aa30fd1ed4237bf8d83e6e00236dcdf74204c6fe9e750e521d277a741349649b": "t71h_ar7b", "40a940ecc0bfabdac39310113f8d3f9cfeb9570da424a1a464dcb405cef83249": "t71h_ar8b", "f84bb25dceed63ef1625886aa6501996b88416e27326d85ad0783011bc06bd76": "t71h_secsp5b", "251664368e69b618bfbeb7919daee400ab0b4aa07c2261e900015251a811ce40": "t71h_secar2", "53f32a1ee8e05387c13ddc091706b8cb110311e51ce79e9d0bc74798109d0237": "t71h_secascore2"};
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
