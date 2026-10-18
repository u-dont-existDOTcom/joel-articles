const want = {"0de5c2a239034b2ce92d06d6e490e873446c65e30f0b4bcd1013cf238ed2a955": "t71zz_ifs3y", "26d271101a479397fb3ac3c8855f0020fab46d25a324db7edb0c7c00584e0574": "t71zz_ap56d", "ecf6a94ede9a66786e03c8604607d097567b683b5f5e72958e7d89cd6b8cfc68": "t71zz_ifs5z", "1520c5084f38e790af01df4b03872d9d52c3a86524b7f83004fb9c78129cc197": "t71zz_secifsz", "89ab5ec87e1e7d77b2d1abf2b216bf22b07c9f64a2b45d2b55fea1cf399adf5c": "t71zz_secifsz2", "9b347ea19517c2dbb76097c8a0374e1cb0f3187b9112f6e3cd5939b08a9f1012": "t71zz_ifs45z"};
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
