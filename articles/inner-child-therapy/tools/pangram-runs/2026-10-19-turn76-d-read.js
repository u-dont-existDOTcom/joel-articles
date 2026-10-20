const want = {"4c460ae21fdb6f9867190dca5250a95a7d2e531c5a3890355ced9ef78655f975": "t76d_ue27c", "09a837880806fb0f529fda8c6961118b4752aae1758018af85791d4d3f64d09d": "t76d_lomedg", "40ab118d27e3f5fa7ef863bc481b164dd770b4a48c4d7085c146c65012276a50": "t76d_losh1h", "7fc369cd2b00e7059180275f4885e911cae7f8f2cbb3dee34d2fdd7eadb2054c": "t76d_losh2g", "636ec52cc4fd0051c8ffd38c0a875046983a3907f05fc023163a45de015e7c2d": "t76d_h1wa", "f6ae115c3796a09e8dd0fffe181c3f67b6d1d285caf2910b0c6c40443f9d8f32": "t76d_h1ce", "b12e143cd5d849c10ae64127ac1c9242495ddc8777c616cb45ef630e2c35422f": "t76d_h1bt", "945c55f0ff505f570cab95a48afe07c36b57d1dfdc65ef232ab8acae18dd9b7a": "t76d_h2he", "0e02946c268046f9924352f0ba926da0eb69ee3eae779922354afc8eb422a751": "t76d_h1by", "c0bdf63bd4d706b658457cb09718119c14e32560559584144944e09ba1215c4b": "t76d_h3lo"};
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
