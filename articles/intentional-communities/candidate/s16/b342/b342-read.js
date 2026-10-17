const want = {"56cf329a4e2341fc6c78d1ddda01790a6f626870a898deb72bab224b0348fb9e": "S16v9L-H1", "64cfc804712c7f6180cfb945e08a0a3ecc67054da44420cdb68fb6e321e6d432": "S16v9a-H3-P5+P6", "df5280bd08011768fb269dc1348dda61973c4ae2667fbfd7808f28d580b39a9a": "S16v9a-H3-P6+P7", "d3df728ff674d7f855f4914408854a3b7bca0b3ac4e7d97bcec4268124b22988": "S16v9a-H3", "f366f884f845bb8d25ada208e48768f91de3c54438b8d1bffacc1f01596095ff": "S16v9La", "4ead5435b0d7045c199f107b83f480d9bab44334e17f51e4c0a7c41b93e53d05": "S16v9q-H1-P3", "20fdde28a6c982911dfc9e5cd2a69fac3544c9bc4abb420ec2a38b4f91cd4957": "S16v9q-H1-P2+P3", "99b356d5c5cb2f69832a29bc0cf6c9abc2a6c1ebebd2d96ea4f745730f9fbec7": "S16v9q-H1", "a78c1ce41fd41558bc8e07621389c139da3f67424a381bd96ba4a4f717608169": "S16v9qa"};
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
