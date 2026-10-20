const want = {"abcc32c14c1d9cda162f418c7793ca7378e09a61b37966dd10c40ee47bdf1c29": "HG16-refix", "07f3a5ddc2f8fc45819f47f8670ebb440cc87d2d9678edbeed5df6614ebcc54d": "HG17-refix", "3cb872616579d421de92aba23f2cd41be0ad2c6fbfee372a55454c91625c6ea3": "HG31-refix", "bc775f2c7dfc8738f7b9def43504167903752a90b562aa63ea3e4bc19bbe0730": "HG37-refix", "944079758a7e8455f7b0ed7f37e2d234f67c9f43575455b54215084dd6a0c63a": "HG38+39-refix", "d61937aaeeaa615e443d9daf6158515ec1b50f715e5875504f8183b54d98fe52": "HG10-r-p1", "de02a4ea54ea73a3f2459d293d3c9b2de32f7da899ea71f774a22353e43db78b": "HG10-r-p2+next", "fde7e905996921130629590181da7cb2c191b06a1ed84e12da6aa38218950b76": "HG10-r-p4+prev", "e11e580b747dbd4dd2a576c991849ea816156aff66640862e2d15bcf61895cde": "HG10-r-p5+next"};
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
