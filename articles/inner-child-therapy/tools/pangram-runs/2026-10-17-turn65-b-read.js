const want = {"ca66d2cfd0579bf4d049b1148f94abe1af4da415484ba94faef1c30d6b65c712": "t65b_p12e", "b9f094e3e5104e4d3f16e116bad149314a1b5939dd791f3249a096319d792c5a": "t65b_p12f", "5b0d8945145c7b89bc087b4d5424b9b476ecba12d2d63dfcfddd2766a9591a82": "t65b_p12g", "19ec6ac5f3914d61754724a393d7873cb424a6f2d9eec0714d26d1e22792cde8": "t65b_p12h", "7ffd18717ad7f6ffcd8eeba315cc074b1aae1376a21a30f534521c4b58c3192c": "t65b_pairp12e", "5bb029b7b910f9e5b9701e415313e88ff81149b252fa52bb629c740334126726": "t65b_pairp12f", "2d5bccdb0393e1b62bccd4611e7430b68d0303cfc158b2815f3f9cdeb05a159b": "t65b_pairp12g", "35c528647d6762bd2bed0e76ec89e37c527cae43306a3bda0be1f4262926bed7": "t65b_pairp12h", "bf8b61d5a5a0b280459069bdd029cab8ee1e3d9b6b17a52210f083d521292786": "t65b_secp12e", "b3671713981a7340683e8895d82ccfe8523c3fdd36821433e2b3cc21c10e779f": "t65b_secp12f", "d21279c3e67b8a1bce0d1f3b8d546cb36b6f10df46d7ec9fa3a3b2dfebe6a539": "t65b_secp12g", "84c9dc3ebd9b99da805c17589b77594dde100ee6476c130186586e303121be41": "t65b_secp12h"};
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
