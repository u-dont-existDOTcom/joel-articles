const want = {"003c18a61b411a89e81fe7786d676c62faf9dd5379641ba457c1a5e455b1e032": "t71xx_ifs3w", "8023454bf6ceb62281e64b021214045b94754bc2933ee50d79ff639ebd9cb0ba": "t71xx_ap56c", "596fe3b4f844bb13346ea0f641882cf17f86a5f224a374d66760d90baf04e496": "t71xx_ifs5w", "2195072c552b8216fceb6de565315add2799f4bda9095375075217212892fbdd": "t71xx_secifsv", "abb8afeaf3908582a01bbd68535717e85a022cac1e99d6447e63afb7fb6d3282": "t71xx_ifs34v", "dcf46bcaf7b2063f31849804f0ecd6d121caab613d37625634ccf266edcd5bcb": "t71xx_ifs45v", "e6f875055a5bf1a7f58520060a7617026dfa44c0d879f1369588b7ad1df91d86": "t71xx_ifs56v"};
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
