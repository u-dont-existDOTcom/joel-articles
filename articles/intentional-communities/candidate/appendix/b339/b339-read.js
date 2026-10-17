const want = {"f60a05eb7cdd6ad1588f0cd66cd1818e55e1571a61c448ec9ed4df88c25826cd": "APXv7-E12-13", "556db2e9e0f84ba6bbc9d79a9688c2a780545c6c9162cc6ea7f415690653976c": "APXv7-E11-12", "efe2ebfd8dcccb891190ce454c782a4d1a89c591bc0ea5cceb5a84ac18aba35b": "APXv7-E25", "8947449d94ec0c33adde94b95416f4c75da8219b3ba16f482ac001a8703bfd36": "APXv7", "f3c3aa72b8d004f1a580ecd1ae410e93c284eb7fc01602bffa0ac92efed72878": "APXv7x-E25", "28bd2b543563ee0bbfd79e5d1340f383c639bb220f4871694e799d72c44904d7": "APXv7x"};
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
