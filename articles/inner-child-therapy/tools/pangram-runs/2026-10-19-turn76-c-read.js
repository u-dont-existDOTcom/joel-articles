const want = {"e4d472ef2e75499e17c54b7c9d9e74fbe6dc3b2b33d109ca74baee242b30a456": "t76c_ba3e", "bcc51e22c50eaf900e1d9e01b8e29eda125fda2af652a9d7c66c2a940c8dda66": "t76c_as4bf", "229536aa28b9ce5c92120b6a1b67538c76ce6084584fa3b78625d2b98c0dc647": "t76c_ue27b", "508eca8476a6019fce22f8513379b7312e2bd80420923ce0b13c444c5042d826": "t76c_ue29b", "a52df96eadc2118b23b31e90f23c7b868627f29cd06def4b479c1adb1bcbd222": "t76c_lomedf", "dd3114263637ba58f6512ffa2db90d6e1861d4c5d921af896e62583a3b291711": "t76c_losh1f", "ead1cceafaff51396a5ef6af694079ace50c95cf531ad1d5a47eb5b4f1ee6ebf": "t76c_losh2f", "95e4ca2ddbc0e0f61f1ba324edf05a7798205e8553203fcfd7a583ca7bbbc78d": "t76c_cs57e", "05a37a4da0ff787ac3476ba129850f630c6a8e26b52ecc96a5fee7d8896f64c2": "t76c_hero6d", "3d2e2da180d04d046e78b8f72f109086e841c3851ce3a99b4ef62d23ea7f7152": "t76c_h1ba", "4feed9a4214f57e8e9e12f070af9b1d707998795ed8d3df6c7fa2fe0cf100350": "t76c_h1as", "e74c001fc4dfa2b40692395ef5482650508fe4e1b57ebf31f1d4f0b6f6ca545e": "t76c_h1bo", "e2fda352537b7960b20e4751817041f4c41010eae5106b5e12daa698e7d460dd": "t76c_h1wa", "d36e07c5ab4bd94043572de820290a887ce54a52a811227bad12f366f585ff82": "t76c_h1ce", "1372677c3fb72f8216dd176840c52d4c92e5285a1be75cb9848ff5992cdf5f87": "t76c_h1bt", "d08df03c5a3bd4ba5221ab20bda20e2838b3896d9d2f7897408f9ca681a6d3d9": "t76c_h1by"};
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
