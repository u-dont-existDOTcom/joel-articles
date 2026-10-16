const want = {"fb0dd3b5889caaa1b99f49d5b7847a96bda8f0d4d0384f7cadd8e1dea1828d17": "t62a_p8f", "548c6647b45512e1f8c393e7614be0963bc2b9a9665a119b820584e75547fad1": "t62a_p8h", "3efe967e538a0231aafb4bd7e666d3ea02ef742c152aa880f6d6db4664cff462": "t62a_p8i", "efcac7cf0f1dab33ae2038f0124e740cf79215559b401fbca7c86b14f741c089": "t62a_p9f", "2643b59914f6a6668c48ef3143d084763c6534f8c05c307891002aa9de07ec3b": "t62a_p9h", "d8ef290935dae594bb232a0ecf04cbcd42f41481557608b5abb7de32e1f143cf": "t62a_p89a"};
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
