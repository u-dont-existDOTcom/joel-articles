const want = {"d8d51a097e95e8fc98d9b10dcb6a7edcce96eea00c2e0bb62d72bb1d06b5a316": "t65g_p14b3", "591896dcc96e26ec9f6d9e2bf5b9bee1295b247297d91bd5003b64caa474abcb": "t65g_p14i", "b398fa532b195dc768cbd3df3725bc116dff430910ea17c6e040f122f98b34ee": "t65g_p14j", "4e6eb3191a1ae2c5743e3a9f2cb05181710ba95e3ffd8633453e66a56b1d4fc5": "t65g_p14k", "cd3941509a53e921ceab33aaca7847b08c5fdfd19cf866ff8e168228a139aefe": "t65g_pairp14b3", "eadf6abe37ed90b727b991155d48a9e8fdb4d574e4aa7002606fbcd4d39cf1f7": "t65g_pairp14i", "f63a9d1f57ddde11f320f99f60a234d5b63fc5b45030f712f463620c54f12fda": "t65g_pairp14j", "8531e133127b749f6bfb37ef5056bba002fd3df62167e28eb4f2628df354149e": "t65g_pairp14k", "a7d5d5fda9206892375a5da9f47657ae21eac3a93a39c8e0cc4b2eee425f2ba0": "t65g_secp14b3", "c8f94ebd3c4c739c40fdcbd7cf3ebb7e0d83f84ee1027115e9a0969b5f499813": "t65g_secp14i", "a215f4f66388c024493a26aee23d88a247dfd529fd4418f688e83e65fa82e772": "t65g_secp14j", "48b490908b415e8dacacc38b82b64dc2f7b197ab3fa08a9511b04d5654190cd2": "t65g_secp14k"};
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
