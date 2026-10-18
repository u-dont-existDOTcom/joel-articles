const want = {"34c8c36dd3d95177b644e08beca73f3d11d9c8cf4a2fb2a5ee75c080ae139505": "S2v36-P1", "8038701925c314c21070c81b2edc2fec25fb4b3d5ad4bc705406aa8e1c569c4e": "S2v36-P1+head", "00d132ce55bf69df475adc22a7f1c45fa2e1a9ac5f351e748bbb74b03f36365e": "S2v36-P2", "b54fa96a0a35ea249e907bae8cc6665fbf6c5f6aefcf3e52ecd72ea4f552dcdc": "S2v36-P2+next", "ad617518d97f8298aa79bf245efa97b7b35bd94f47fb4700047c8a9ef4b943d9": "S2v36", "c37157b1be05dbbbbbe6d82ae277e7969af2bc18feae74198904c7affbbde892": "S2v36b", "3a781c9c648cb92105d514548c4ee442b0b62c0c2fa27f374f8b7d884b7a4430": "S2v36c"};
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
