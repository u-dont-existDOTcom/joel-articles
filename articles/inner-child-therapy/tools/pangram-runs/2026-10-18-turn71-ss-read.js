const want = {"b714236fa85dbb69b5e3f4813abb5efc61befc42f7617f609d4ac5fc0ed12717": "t71ss_oi2i", "11f1bca0642cd4cf9c970d7685e16d9fbf997d4337d7c295fba0bb6910db4eb9": "t71ss_oi2k", "d69bd993c0252487c6737f42b68450e14eb7c395c1dad07b6ff2cde2f379bbfe": "t71ss_oi2m", "37de0eee4a1ae3983a4fbd84bf962c86f103ffd442835271e9cdf628ef244a7b": "t71ss_oi2o", "6554ea1e954634b282e5a7f0a894c2eb8e5bf79657dcff1ebe7a84f46462ba34": "t71ss_secoiddi", "7d6904153b61ee947761c2ef0f34b6f96c2ed90dc5ee0f524224dade9d6d354b": "t71ss_secoiddk", "5cde92ba1b9be5fc4933718dfabc56a0313844b1ec4ba5878a87149ec219d91a": "t71ss_secoiddm", "27058e9199bb2daf91fe08a6c3b985d569b8a2033e7e4a284535ba4b8f6d6246": "t71ss_secoiddo"};
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
