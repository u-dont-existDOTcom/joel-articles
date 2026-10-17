const want = {"a3305aeef4a0e2b57a474824135e981023f8abfc29da27d5e32711708f4803e1": "t61c_p8c", "f67ea7385b2aa24b2ffe34681ffae2462065e14236564519b65e4d7778168723": "t61c_p8e", "fec938ae1f2d02b9781a7f0298f31e1f2b02bde21b8fe263a137b4b6acfb583c": "t61c_p9c", "5da0bd0712c733fe73c36c6c71bbf927021c37bd27361a591d22d4c54454d1d8": "t61c_p9e", "11a3258e1c33457cb3d7c695c4fcc57cb59a8dc8083aec8e2a33dd6bc2ce22a5": "t61c_h1ee", "d372054899ad5cf7b8ffa0c080df5a33c99b375a09c867d1ffe4a1f077ad30a0": "t61c_h1ce"};
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
