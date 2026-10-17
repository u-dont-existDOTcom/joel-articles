const want = {"290f8ae2779785d4817546abf286bbf2ef3416948b26f052dbfa5219b501553e": "t65z13_st1p3w1p1", "e162984f04204ed0eea277a3bd2010935839d54bbfdf0aad83d81c1e97c786cf": "t65z13_st1p6w1p1", "7c0f9d7ef6e3e9e3da087adcf7fda7cf0f8a4b82cd8b08eb335006be4dcfcb83": "t65z13_st1p4w1p1", "4bd0c4a5248299513689499cd5708014f87f86e241e60305d6202c43fbf1c45a": "t65z13_st1p2w2p1", "d5d819c7e06fe7c8228e9890ae74c6f5663e0a18309535ba51e8d0a29f367735": "t65z13_st1p3w2p1", "5ce6ba81a63c789c58a2a98bb6e6aaef3c8d9b430291992de216a79a19b664af": "t65z13_st1p5w2p1", "aff93add57d00071de50b10258f80c439b7b1754ac8586fc76ffec0f88eb3451": "t65z13_st1p6w2p1", "3e45434970d75dd383f234b3827b419639e5c3a8034ec7f61429a385d07c6d5e": "t65z13_fg1p1w8p1", "82df872e2bfd9b767521a537d24ca3d0702e9548c87906328bbf621542bfe6ae": "t65z13_fg1p3w8p1", "195118d5c379b6b202814db58acb084c176db6969a2d1a8fd6acd9d989784bfb": "t65z13_fg1p4w8p1", "12b0a5824628b2d4f2b78bbaa71c84f783277da3baea979f1e94b58cdc877d6c": "t65z13_secfg1all8", "85cfbe4595f172189eda054b7d452e9abc193074ae233fb7fd587cc2ad91b0fd": "t65z13_secfg1all9"};
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
