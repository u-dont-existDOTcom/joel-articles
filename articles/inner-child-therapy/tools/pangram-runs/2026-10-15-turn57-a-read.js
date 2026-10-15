const want = {"62147a33c669fe2f2025d4e2111ed2a412b31d0f9c3f5e650b63424616ec8b25": "t57a_p2w1", "3851105b9ed56448ae5c8d284034a079c66d381e123d3bdfa68da003a3381552": "t57a_p2w2", "09f535e53b6c6f0c307a80cdd3dd31a65d5c20224db16853abe37bf295ee56f3": "t57a_p2w3", "a107331639d012222bb1da64fa262f2244c1b059613142375e9fd9a3379c69ec": "t57a_p3w1", "3852c5fc40cf330430dc63173ebd71f6894a9257575c768a6cb199207d04dbdc": "t57a_p3w2", "9a7ae63f0001faa2e0163050b39821ecebe79bac9d5877ea63d1b7b9da013e2e": "t57a_p3w3", "e5a2dce3597353b2c658dbe2d43a3400f02234d3586419e40479b7f7750bee0c": "t57a_p4w2", "03024c7ae900526f5081fcf958f9e72c5569c78d58e0a79878342912c37d01df": "t57a_p4w3"};
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
