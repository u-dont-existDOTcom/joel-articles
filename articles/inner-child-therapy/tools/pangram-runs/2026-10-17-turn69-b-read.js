const want = {"948c16cf086d5791c847b530f4a162f5d29030b1e357e65892838ebb52ed6a10": "t69b_st1a", "6d433d832354b9c82271b9ebfabe62793362b46b535360735e623f8e844a3e13": "t69b_st1b", "d4c6d32c74a4374ce7789cfd25f2d8fb4bc7de8d0435c22b70559007638a4f84": "t69b_st2f", "7f6d78c15f27684a4ae6e47ea50706d8af4e4434d04dbdf906c78d53660a56a5": "t69b_st2g", "abda071f500f5dea73a6fb17d90a1e05c8881d21f5e0b1a107e0ba81b1d1f2ff": "t69b_hwa", "fe96d53e19bc1b5fbfc7c4c47d29d9222915dd563f17b71abcfe6a0ee0fdd1b2": "t69b_hwc", "8c74adb1a1b90bafacf72dc9d3125d020dce11ee2d27939c5fe3762c8a08aac3": "t69b_st5a", "fc4b07329d0c138026d122cbb8e63777c26eddd0abda4cb3dff6f104a68b127f": "t69b_st5c", "eb34e8073cce362a7d3bf0304ea43eb3e5afa60a0568ec15c474311980260d3d": "t69b_st6ab", "a146dc78fc7650a696065ae0c25e5e1a3cd73acb63f9565105e05f9e5964261d": "t69b_st6ba", "f8038803d7ffeeb26e5a422a8713ab559f01ac12de800e28f5e9c2c61e13309f": "t69b_st6bb"};
const sha = async t => Array.from(new Uint8Array(await crypto.subtle.digest('SHA-256', new TextEncoder().encode(t)))).map(b => b.toString(16).padStart(2, '0')).join('');
const out = {};
let url = 'https://web.pangram.com/api/history-list/?limit=20&offset=0';
for (let p = 0; url && p < 5 && Object.keys(out).length < Object.keys(want).length; p++) {
  const l = await fetch(url, {credentials: 'include'}).then(r => r.json());
  // each page's details in parallel (2026-10-17: the History is shared with other lanes and fills fast)
  const ds = await Promise.all((l.results || []).map(it => fetch('https://web.pangram.com/api/history/' + it.uuid + '/', {credentials: 'include'}).then(r => r.json()).then(d => [it, d])));
  for (const [it, d] of ds) {
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
