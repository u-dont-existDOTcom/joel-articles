const want = {"dafb3ee8b49bf3f2b7333ccf1640f70b20ca5599fa9629266951d1ee502ecc18": "S15v4a-H2h-P1+P2", "93020395c7690391e199c903fb35aef3c3f4df8fa218a408a10b20aab34fdbef": "S15v4a-H2", "91418b749e95c46baf379eaee5c57eacc55662a11e9f89af5a5a8abe85f879b9": "S15v4b-H2h-P1+P2", "8c38b9a35f780eb5758c35c9b590b6fbc2ed1734e392f91a5a700a11d5279ce6": "S15v4b-H2", "aa15f343acb2fc9b3c5888a46385a6815177274158b92d6d511ad5cea1ec4f74": "S15v4c-H2h-P1+P2", "78a98aa67544ac358594918342ceef5244956a95956e40e672693d3136e4d433": "S15v4c-H2"};
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
