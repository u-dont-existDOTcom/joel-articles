const want = {"05c517d03e9090ef7f45e94db6d1cb86c37f142d03ef54a44b0e8ab45df07957": "t69c_st1c", "d128422e5c6b56bc0a722863c324615469a9a72998a7de25d1dfaacf25e814d3": "t69c_st1d", "4c70b18e08b06652f0e6418239084750606b5ef4a07928605481fc0a5eb38721": "t69c_st2h", "5c8538a27a6618a5428fc421ca75f14281d0819210f50a2c888814a1f5a46ea7": "t69c_st2i", "d3b6e4e3937d518732e86c93207c3661d1865e186644cb8870e233ecd3a18252": "t69c_hwd", "d7b62db0a8930573e8d7056fcc761a9a965ee5e933f32ea709d0443c7e9b2b2a": "t69c_p4hwa", "62ddf7cb999c2858ec19504424eff241892a955b94c703b17eb2405da0865470": "t69c_st5d", "a5b74f949f83ef9033e88df3df2353fdbaee8f88b82e5b5d9c1b88aa6269ff39": "t69c_st5e", "9d6c7d057854d1de5e3aac7668f1207d5922841d83c33bed9071544c2a93b742": "t69c_st6ac", "06e3800d5ed7f387c8f625dff97fb58f45ad0c43c1d141603f15a9cfd810d78e": "t69c_st6ad"};
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
