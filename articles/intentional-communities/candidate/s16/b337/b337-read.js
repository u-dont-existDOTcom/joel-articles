const want = {"4dab83818e91c0ea661eeb5a59ff2dadb4cdad07852839987d93699171f25ae1": "S16v6-H1-P1+P2", "189670a1cee2fe3c74d9c4673cf2b6bebe30a8af3bfbe539d4b00f9d00f93c7a": "S16v6-H1-P2+P3", "cfe94c5d5f961592b2def3eaf2cf98a40ec3075dd083344d583cf508b6921141": "S16v6-H1", "aa756b34a13bd80b12a232d02c0f4d516b8f2236b6fe7c0dc5f4ccffa30af98c": "S16v6-H2-P4+P5", "e91bd6a18d747f5821a3a3cca33ea1b765773e47f1677aab88c50cd5123c32d9": "S16v6-H2-P5", "242a49fee1ab2061e0262a733f32721adf419ec32fcf4837bedb740dbb66de69": "S16v6-H2-P5+P6", "e4804932a8fed876d5b23f692836c583ca601edf72800b9a461ab3d26ec6c0a8": "S16v6-H2", "d417ba6eda163812bb2dd498558f8cc5d3ae0a5003158357dbc160d86ab80281": "S16v6-H3-P3+P4", "c3cc832b4f1db71b96249628abe952ddbb87ff6298d0dda965a6391f7d66f5fe": "S16v6-H3-P4+P5", "3cff2b1dc8201a0762da291b3eb92f7621bace49dc2c0078a6ffcb900e909865": "S16v6-H3-P5+P6", "470ded8bf0367cfa6b5c8b62dd57ef8d7400a9e17fdc2aeeea3dd3f8efdf4918": "S16v6-H3", "6fab49c22222bdfb301ea76650e9c5854c55514e2f7f5c44a89e86bdfedd54d4": "S16v6"};
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
