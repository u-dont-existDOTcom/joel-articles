const want = {"442f1bfce1dd4a6e0f7e32925be3cdb9fccd3ac2546f297bbf23a10864be1800": "t73b_c552b", "e3b895fe17e40271a0504fdec991205a9a02eee6d2932b2e1ea43cc2bf2806f2": "t73b_h1b1", "626c541f3234d5b24c484a36db96b4fe391913602709c5c4f5d8882ba22fa608": "t73b_h1b2", "dca8df2b779e3afb0c943bf21ecdf26a0d61a7c2ef7c5a684807bde3b1314599": "t73b_h1b3", "bf833bfe32cc25f99996a95ce310692c495df84b5e744d24fa712ac3f3f8e167": "t73b_h1b4", "2b29716a01896acdbc3297efcbbc69d04ef801652643f49fbc428c3282aceb31": "t73b_h1b5", "48829a97f1d61c46c0418930cd1b25a03af24dc4c2d347571d449d326afdec03": "t73b_h1b6", "3c06cb087d5c1dc98650a5aeb345369bd210262439c6c0249ca79a1aec3fb651": "t73b_h1b7", "c04bce0ef36f07490c686ec2250c64672ea6112a06a34e85e98c7f1da7ee2eed": "t73b_h1b8", "7ac93b0c5087640c4b9cf33286ff7b231f45c0c39a75c7711e9381974d057693": "t73b_h1b9", "144129a3acff21bb4093d334563a2b65334b37ef83aa7f43ee1fffddde5e64ba": "t73b_h1b10"};
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
