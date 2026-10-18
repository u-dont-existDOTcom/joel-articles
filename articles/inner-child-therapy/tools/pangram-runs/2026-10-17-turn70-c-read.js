const want = {"1379f7b3c65f8783d88e0ba57897e1b85e16dd95d9c7614b45e2a5685023d163": "t70c_p4a", "dbd81f6afa645e9344015fb93d9def34bca3c816871d6d067d946d19cc0abf62": "t70c_p4c", "687c8a3250e39d68a0c4afe2553f1b3995587d7bc86fbf36a50ecd3afdb08426": "t70c_secst2", "a9f808edb5925f6256a8379a679b873287d2a04c10ce4bd9181599974571515b": "t70c_secshe", "63f803fa6234b1f42f25b8cfdddd96af3644415fcfd05e37698f3acc1f7b3b55": "t70c_fg2f", "279ee6df44e88cdcf6b40c3edb8883fefe5abc35106a0a3166b1d6fc5ee44bce": "t70c_secfgf"};
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
