const want = {"6a5b3d30967e9a4af8a909a1e22720769612a86802a9a33d8da59448d0d1782d": "t71j_as34g", "1773f87d0f99ae0b0c2da81ce8b715f332426c4768e562bc3bc519ea269b3d0f": "t71j_as5g", "053f0f47824cf52c3db6f032e55011da9322f5f04da5a65cc3ff8eb5ff616d20": "t71j_wifs1", "18e067003a2d15f70f39c6a3e3abc495cc34d8daa6c1c95d636b9acae4cb6eee": "t71j_wifs2b", "a2bb9c299ea32bef63268beebc62ba2dacf1a848018546f961d94f59999e2e2c": "t71j_wifs4", "54261608f814fe714340dc17183406a123313a9a0ea4b54f840848b645e2c643": "t71j_wifs5", "7d40ae9708c42e89f8b1e0a6a7443b9e6d2592cfd6671039494210b4260c29bf": "t71j_secasg", "2fb2b8ac978538662719def8b9085c418727707c67837a1e3bb2fcfa56fbca36": "t71j_secifsw"};
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
