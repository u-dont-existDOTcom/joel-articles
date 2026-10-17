const want = {"344a7261f4aed1bee116607397042e9f47111e52d0f0c459b9972928927c8442": "APX-A", "6e72a29a5178f2f82e198fc55c3bbb31abcb82ff5e68b18546903bb26bd1d8e0": "APX-B", "6acc3ee1709611284be80c45b2a625245d6ced13232498de7ebca7abc2caf251": "APX-C", "b9e4221f0f665573b6a9639f91cfa737ee2d3c607a124653fec967f76fab605a": "APX-D", "62ddbea4b0999faac92126d1636b93aba08236c3b037b6d83e2a69d57a6e037b": "APX-E", "dc9e1669d37bf11288ab4d762c4799a4f45c2edcad7fb0f986f1c658bde46f61": "APX-F", "7f2f3a50a83257151ebc9c8fc176073c8a76dc25cef43e9ce4a876b2cb4c7ee4": "APX-G", "b070278841924bea2a49f8de060786a1750589e0dd263bfee37f4d3caa680d46": "APXv0"};
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
