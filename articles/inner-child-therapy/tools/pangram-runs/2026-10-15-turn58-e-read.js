const want = {"b0947c59c7679b7be0e14dba11e80929c3052d60e5c8810289ddbb09ca3a5829": "t58e_p5f", "3b530e3340aae7219bfe864bf931cc3072a645c931836fcc66010ba71b6fba2f": "t58e_p5g", "30f8e01244247d87be77e6aa5b544f791c10b3ce585a580830bcf43203bcf318": "t58e_p5h", "70ff8d86b2b8632650a673e0fb39a3e64229af86fbef97d10d729401442368f3": "t58e_p7f", "d3ef027c4c72dd68ce5faa047c91d60559a2f03561e9e3ad41823578ff95db3e": "t58e_p7g", "4083fdae993d8b8105f67bc465cff4769236015b455ace03f18cb813276d5ad5": "t58e_p7h", "ece7a8197091b3119d41568e9d1834efc1dfcef86eaac0f9474aa8042847516e": "t58e_p7i"};
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
