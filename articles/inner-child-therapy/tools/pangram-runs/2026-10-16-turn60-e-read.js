const want = {"5991cc00605e6430a567165219b06ba312a6968eced9c8b0be13e77877e7e6cb": "t60e_p5w1", "c0a543392ad9e90d0eb31c9a5ff553d17e29c1cbd8c24aff0fb106060efb8af7": "t60e_p5w3", "fd2c793e0c8f3c369f95257aa2911776094b134187302c0c9f08d7040decd882": "t60e_p5w4", "790d818c69540389e83ee8642d647cf38c798dbbd046613cf5153327afa1e9f3": "t60e_h1w1", "727aee8e5d268ff761d12199ecd28f6a7a3f709805b0b3010d905bb21e875502": "t60e_h1w3", "b35aa7228694ff2887da9e3a442920f9067f01b5227d81cddeb6ea152af94ef9": "t60e_h1w4"};
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
