const want = {"feb2f00474b0f1d9e6ff802ef5e4d22eaeee0348119107875083a532b202a780": "t65z12_le1p3w1p1", "5367ce1fd94d3e156fe18cf0c634d6f85864a3d62a051a5e74370ae9bacdf4bf": "t65z12_fg1p1w2p1", "527a22738f7ad30183545df4c575c5f31a82531a71fa6eb006a2651a3301def4": "t65z12_fg1p2w8p1", "3b73dfa54c02381e6af3db56083d0f8bd0becc4f9430213bca7ef2cfb7496399": "t65z12_fg1p2w9p1", "d6a23e4f30c5aa40e0dedd3436d55ecb96e6a9bbcf9c22c0291e183c94d93a86": "t65z12_fg1p3w2p1", "61e538c4d35f654ec0132d9675f9ecd4c690e3458bf73c6378c7f6ab9485416c": "t65z12_st1p5w1p1", "555ae60405a86dcc225ed5c0f7721c8f540a421ed295c5947e49814c3592ce36": "t65z12_st1p2w1p1"};
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
