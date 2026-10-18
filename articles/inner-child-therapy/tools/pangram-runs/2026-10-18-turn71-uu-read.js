const want = {"ff442312d44da18c1da73cc0df9242750cf84c66be7cb45dff04652606038411": "t71uu_oi2u", "76fe3f1aae08339a755c1a93cbdc409aeb6549213604a4a061fe9cfe4922401a": "t71uu_oi2v", "e6619cf37a90c6ad49b28200e3b8ffe25160381cb5f69b4a9ee74af0c5b977dc": "t71uu_secoiddu", "751ae980d47eb015270be5ec92b1d79a9c7d8ef6576cbbf083df44ad4eb38852": "t71uu_secoiddv", "70831f3751d03afbc1799a04c93dd7af838a19f9833c2c85a96df349d3460bc5": "t71uu_secspa", "4a91a026daf713b9f7a9b61615dcf0c74a46c3b2cc45b3eb749a2e51fb0656f3": "t71uu_secspb"};
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
