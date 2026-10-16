const want = {"ed77a8b30c95f2da6530f796fa85704418fc241bfe14f054e025e633d52ae7c2": "S13v21-1P3P4", "161adef9404631a1bb8e9bef9e1348efff5fcecacf463ca866c574f9d0ecf51b": "S13v21-2P1P2", "46a5d45484686aa3ad608bce6f23d6bfaefc6ce2cca40529b1b43bf6936f6760": "S13v21-2P3P3b", "13a732fb5e29b8b2b94eac173b92ff55984c79f960257d2e0d3cdf1496000824": "S13v21-2P4h3P1", "9c1c8917497548ed4c90175ad13dd1c5de97703ee035368f54d4d2b60780a778": "S13v21-3P2P3", "2ed9b0ac7d058603eed919d6ea88676f579f648827b0542180e8d0495f00b241": "S13v21-H3", "66f01071d29b16417eece767db54176c3263b1a7138f986a196b53dc29a006ed": "S13v21-H4", "4afda6968849598613975d255cd78fb9b7a541d36ccc517e1042f190d9bd3189": "S13v21-4P9h5P2", "1059a27dec258e95c61dab2c2d0b2df6732366ed7c47d29094edbe3b6fbf9b69": "S13v21-H5"};
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
