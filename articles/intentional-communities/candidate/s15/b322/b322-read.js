const want = {"cd4d6c23023888d450c5e680c3a34e3b797062a766625112ce33627e7e720fd9": "S15v2-H1-P1+P2", "57c273ca50195dc5236ee1aa984dc235de43a3c1b763d3983333f58479eabbf6": "S15v2-H1-P3", "5c84c5ab3c86a452eab983db86d543f599b3184a7d533c0bae1def873cc23b1c": "S15v2-H1-P4", "8ed1956a8ef3067c8f476fa2a5c2cab14e963fb3b43bd78b78ff28d2b8a27dfb": "S15v2-H1-P5", "10b413197906beebadbea1946c8b2a8fa32f900370cec318aa94837da7c22e68": "S15v2-H2-P1+P2", "6a7e4ddcc130850f0716b10b38b64298ef162c930489574032d1bf558a335071": "S15v2-H2-P2", "68c42058b950cb46d701e8dc8b358e042a2c0f056b85ffcd836ec95081d2f4ae": "S15v2-H2-P3+P4", "962de06b4c5dd5afeea23775743e16a3775f45d737972a00d3e14cb44cc919a6": "S15v2-H2-P5+P6", "28f812569f674b30ae4dffb131daa623d4f850f4d5cc9c64a3babbb74c0f41b6": "S15v2-H2-P7", "39fda8ca25684220c09b56f3d05891e756108eae3c0aa57068c713d0c30915ae": "S15v2-H3-P1", "91c67658c8f8690bc4c6e49a6b0898da545937cfbbbf4d9bd11065e4f6e89fa2": "S15v2-H3-P2", "5b58239ada9d572a110e116a25dff09716cd3a2fc45b284e694c4bc1dd507017": "S15v2-H3-P3", "678bb9f01524440ef1f69f78f0e6dae3e7a47ed04c0a79f79ec6f76dbddca674": "S15v2-H3-P4", "aefdc9154f4c0c9ff533dd3253e78036f0ba2a613a7cfcd97a9650b11d617740": "S15v2-H3-P5", "d02394969b4d44a60e338de2350878781df13f2e2dcb7249ce74a16d2bc28858": "S15v2-H3-P6", "85860b6f2af8378eaee39bf14f473d1da5fac72e23c4f6bdc29715e5de7b50b6": "S15v2-H3-P7", "cd716be45fa1a4aee37c945df0d33c247c241e5b2ab6457cabb15fc2f2a6748a": "S15v2-H3-P8", "1f0d5b7e09f414b13a038a1ccc362344a43383c146369f1c683aaf9b08eed4b0": "S15v2-H1", "3499ea2b297599cd420989235be8907b891d158af4aca47bdd17f05fb460d3d1": "S15v2-H2", "6a7d45aace8670330de2f07e857c1f56745e6020ff4d4a18fd2b36b208d6e2b7": "S15v2-H3", "54a5ef406b5f84350abc213be82a1a4167a7ba50649d18e55aa269fc7710174f": "S15v2"};
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
