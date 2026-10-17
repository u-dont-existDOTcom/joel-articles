const want = {"6ff3578ea8faf95acc77a72bae8b26772ca2c3b7023adfa8400ebf4c1cd2f166": "S16v5-H1-P1a+P2", "d6d2f99538152f0572a4fbfc0b6ace9e473fe1398e5451c29c31f757a8a49c93": "S16v5a-H1", "14b4e6ba7945fdfdadacb404a473e8491e7634c5af70fb7659c7390b4f0bd325": "S16v5-H2-P2+P3a", "f47c150661bd4bcbc6b3c2bcd4204b658b38627efd5198c1e00e0ce69277645a": "S16v5-H2-P3a+P4", "ced50d45df5261d4ccaef7b13787a94e7849f307cdaaa04c7fc53c58de5427e7": "S16v5a-H2", "d6253d1a993447679fdd7a6cfbca728aff67b69a0b7ffba3ee296caa69951c07": "S16v5-H2-P5+P6", "afad3638f618558eb7d9f351f661337d08c4e2a7de952f779af70c769e286449": "S16v5-H3-P3+P4", "6e1783678548391ae1f6c9f67a52e51fb61e8c83ef198b0e2ce6b5415d07c632": "S16v5-H3-P4+P5", "b2ff020b1d9b43de2357e7d4bcf85d594e137aaaf3df00a117568750d9a672a9": "S16v5-H3-P5+P6", "edeb790fe7af383f664f57ddf90295161140feea3b184005aa868b4ef6ec0b99": "S16v5-H3-P6+P7", "156750ade2aedcd2ba139ff467fee7f9e2be88d84f1c03591efe21b3f13ca59f": "S16v5-H3", "51fa08325c2eff8cde7ae2d38c64263e92c2b3133e9f29b7f1111c651c17733c": "S16v5a", "e325dd5660f91938ad4ffdb45770838f00d8066588942467c0a80afd525feec5": "S16v5-H1-P1b+P2", "f3c6ad874a001c20fb55edf34daef426579d4c505d89766135760f22b2f77f1b": "S16v5b-H1", "c73913179b21eaccac6332f31c1d6cc91d5769427253c8e58d5e75826951645b": "S16v5b"};
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
