const want = {"153355e0ee49a2f5b45ad09c6f530dae243370828daf70798a9eb6dff5df5f56": "S13v30", "5db651768ee6aa3375bb17eab1a23ee001d3ac9033b8ed930dbd25ed241a4360": "S13v30-H1", "75bedb3892b089b0ae408483b5a2180dfb34515f764c55d61666b376af495c13": "S13v30-H2", "f6bc402571d08470e8e67246c78df5d2bdb5f979a43f87b5a5df26ade87b678a": "S13v30-H3", "c9a1abfe4c6c2527a554e8d67ff390a0a60b7ef82b5b6c23af1be906df929de0": "S13v30-H5", "59b67d8b3b3633561e755602669d77a200ff4d0448ce7aacbe62e6a0c4a04bc2": "S13v30-J1"};
const sha = async t => Array.from(new Uint8Array(await crypto.subtle.digest('SHA-256', new TextEncoder().encode(t)))).map(b => b.toString(16).padStart(2, '0')).join('');
const out = {};
let url = 'https://web.pangram.com/api/history-list/?limit=20&offset=0';
for (let p = 0; url && p < 5 && Object.keys(out).length < Object.keys(want).length; p++) {
  const l = await fetch(url, {credentials: 'include'}).then(r => r.json());
  for (const it of l.results || []) {
    const d = await fetch('https://web.pangram.com/api/history/' + it.uuid + '/', {credentials: 'include'}).then(r => r.json());
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
