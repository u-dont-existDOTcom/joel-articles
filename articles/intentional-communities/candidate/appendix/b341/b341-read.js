const want = {"80f7a634bd62580958ca7514f263fa399570223af7a82cbeef3f58f4fe4caec7": "APXv8-E13-15", "5ab2f4d540e45792d1cd830daf84f711dd1541f5fe3c778fa8eb9d954546b1a5": "APXv8-E11-12", "9f9e30e68fa6e63d3a6af6afdcbef75fecac1a175a161b9503af1e5b3fab86b3": "APXv8", "43948c344792a760ef8ccbf9312fd33d2d06df227506b1390a058c209f189745": "APXv8x-E12-13", "58187ff73d2109082861e13deb92cff77c44294125f0991a1b1e9fe62e318a5e": "APXv8x-E11-12", "73fb422e6ce759d961cd23e4df49d1760c11e1168c46114b9328e6bab5bf2e83": "APXv8x"};
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
