const want = {"0989a10ef2adec51d1c474a20c1253017e22f0885a6219c5f82556e335bd0dba": "t65z5_lm3vw7p1", "b3430dd333100c7a6603c37bcbea3e1a319aa597ec33ab277ba3a933ae874316": "t65z5_lm3vw8p1", "82801c492a82df57ebf7d167d794cd24fe0ff444af47e3aa26ed1aea662b7d7b": "t65z5_lm3w3p1", "39fa3cffc61d96d9d937929ae49a9d03df24e39920c77d5185ffb1f0e6ca6143": "t65z5_seclm3w3", "1d70f8feecbd5282f62771b421bb4e112a397c21310bc399f0a51b576ca46534": "t65z5_seclmh1v7", "8a1f8ac2c3dc83a82630f6a8a1b6459a39dae20dee8d5c3e90fee39ba389e32e": "t65z5_seclmh1v8", "d7c62a883bc60d1d828f30d239a508333c0befc0162212b48c4e82df07218398": "t65z5_seclmh1w3"};
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
