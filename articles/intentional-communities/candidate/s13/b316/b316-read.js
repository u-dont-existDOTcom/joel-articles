const want = {"0437422a28a964f8e390fb11f4e1dd95134c08a90db0501a0a591f2f6fdb853d": "S13v33-H1-P3+P4", "980bea4a87190037baf67a573f9bb3d4810a8e472ce0ae25e8e9a2a56c100b77": "S13v33-H4-P8", "884ef2e68c9273c3efef2afb253f9673782f2bce86fb143f4987e158fc3fa5e2": "S13v33-H1", "cb7ba9c8b26326b564d035bd637daf140c0853057366f21cdc76e0fabc72addb": "S13v33-H4", "4050fd94d9b0891b8db8b23d403030030b7bad3f32e4ba93f08ba66c293320d5": "S13v33-H2-P4", "b35b334851024232d20d16c2642f4b41c04e619f29b0afd4645e6b4caa4a5632": "S13v33-H2-P3b+P4", "d83550ce952f7d8ff2effe1d72f84ede71bd06a1c08715fad1879658d2ec43a3": "S13v33-H2", "359efaf978ceee0e454ddc36ce580e24e2601c59f90986e09cc80aa3e5acfe92": "S13v33", "7d86938f816a1ab38ad7558e7da6330a8f955dc19714c3ba3fe3a9630e3e7a89": "S14v8"};
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
