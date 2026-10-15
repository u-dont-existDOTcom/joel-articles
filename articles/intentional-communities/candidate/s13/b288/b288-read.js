const want = {"f740a793114a874b80e333f08dec87b0f6675f9233769e3d01f500284d3018e2": "S13v6-1P4", "1621f7b52163a97e8b54755d759a55fd2b2c9ba06f02d0b2671a32fa6ddb75d7": "S13v6-2P1", "739c505b6077c872543cf7eca9b237eb6764e09ac7085dbe5613d4ee46dd2705": "S13v6-2P1h", "185737c4d5eaa2de7872b41f4a6cd8cab0fa9f9669aba6027ccf4eae2c0c7ddc": "S13v6-2P1P2", "635caae88b2237b16e356708f9cf829887f5c27005b83c016bfa1e8de846c71d": "S13v6-2P3", "c4bd0b90be05e2a634648706096ab3b025029c8a36a3b003777393ca322e7ec6": "S13v6-2P4", "18f9f783bda4cd8f05cf85b6cc99d37d5c7f518151b1de250b9c8bb474940e26": "S13v6-4P1", "256cbbc01b4a96b0c6afccd68808197534d195cfd17d5d886911b766b4216102": "S13v6-4P1h"};
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
