const want = {"7465d06979fe371e705e5650556ad02cf154c03708a772423cc42ecc789db178": "t64a_p11a", "4739d6366dd7f0b428a91961ef833a34560b6e7996e946687aa27241da45a919": "t64a_p11b", "9e61acacfadf22f21b13d041478da03c8d4e46fa0d80a2156225d1ab3ea83dfc": "t64a_p11c", "fa838d65af65ab374fbd39055f6edfcbb0a8e9f3a83f296d2efdaa18ca051ef9": "t64a_p11d", "cf65717c5cb3477cc51b75418e87081b2cc876bd2a8706b4bdd95a7126ba22df": "t64a_pairp11a", "89bb866cdc7042c1712031cb886633a83dbc81b64885be4004bd30d08f87d9a3": "t64a_pairp11b", "ec075c72d18a65314e415e8cddb4688e66c62065e0f02e6c28e6f564e638d7f3": "t64a_pairp11c", "c7ac4da5f702ad701240b42d3593f4d770c4065415439fa1f7d35a4f8d994bea": "t64a_pairp11d", "92d65cc12587cfb279d5b8f662ac4cbf8f49d23e053bc5a2b0866c434676d606": "t64a_secp11a", "791e5538624e83a7efaed4b1acda0989a5cb425c44e0d55234622c24eef950d5": "t64a_secp11b", "57f7b1c689cca4d20e83834b94cd68025d725fd45d7aec5bc04b0a666b681b45": "t64a_secp11c", "bf269180a576896c3d88aaa1416db609334cdec014cade8ec0ef74e3e98063f0": "t64a_secp11d"};
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
