const want = {"23fdc539c0f7d92164ae6a6081e24942b31d2fb799e5ebb00cf72f6768f41531": "t72c_bgoutd", "a799d8bf8b63c18870fde40d41d99c30ecf3c11774d7d12c2452501ffe72b765": "t72c_bgoute", "8331736a43a99d9712045abb36b5de499c0683220132d86361b3806a625f0581": "t72c_bgoutf", "b7a0eb08c1fa4ba7cd66b13be60dfc8d326d97a1737932554084e516baf1da0a": "t72c_yb5d", "c0411a13be86e10bae9dc80006ba933fdc78eda04530acbbb980e3b0207fc8fb": "t72c_yb6d", "c3b7c5aaf58efcd67d07146c40f5b75bdfb2853c060b354b265ab9a3a6eba3d3": "t72c_yb6e", "31878e931f2fbdbc040e232cb6a74a4824c855a5b28aeb0714282d8f25e36f7f": "t72c_sth", "91e432325b49c88fb8955ce6cbbaba46dec62075f1e6b933d8676f6c698bcd2b": "t72c_ifs6b", "f30133dea1c4d2ee05e81c669bec24769e54fd59b55ee8d6623518566d03ada9": "t72c_h1wavf", "906630c97d7ebc45ff64f01adfa11730f58cfabf28c1e84a76789e0e0ccf926f": "t72c_h1bgp", "9929a7583743f96f8122b558e3ae7da624a449ea5557d7d6cbae335fff3b2132": "t72c_h1appa", "ef6d9419a4fb6168a83d12fbc2d04760f19a559ef099d9fab087d0797a12b0e6": "t72c_h1appb"};
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
