const want = {"d4269d35568bbbd9f36e249c97d88c700670ddcc5b63804485773aadc5d4e888": "t53_ag_p1find", "ae50c38562621c8763ed09397482ab82a93c64cd9c14d5c556cad977e448c399": "t53_ag_g1", "f2afd5ec375e436c744fc484df2c54c03d71b1b73b34f29729f4b66c255375bd": "t53_ag_g2", "e043b57ee5521a0b170a04e11ed22adfd2e2ccb0f71a221c416c99e2b515389e": "t53_ag_g3", "05ee9c48c159a2afc7f7817a2492bc90f79c5e1a56705cf7930ae794eb697a6a": "t53_ag_g4", "35bb4d4256e76fdbbf33ae4000a971db3a96e0bc2bfc7f8a1651da56ac76f13d": "t53_ag_g5", "980feb4cdaf93cffd153f8be6ccb0a8127c5ef2b8e18ca41f5182a4671920379": "t53_ag_g6", "84ba71566757e024e34be35acf381227bc3b22fa8c744b0240bba6e93a0023fa": "t53_ag_g6g7"};
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
