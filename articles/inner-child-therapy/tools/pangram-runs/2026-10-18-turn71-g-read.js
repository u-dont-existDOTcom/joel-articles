const want = {"e4fff161e5375ec87a90fc930d6b2300f8d635ac704588898f0653137977e8a1": "t71g_ap10c", "371d0184903c67c64cfd9fd18b0ba5c06e9a50628588982ed95b034b49b2b76c": "t71g_ap11c", "61373190406189b1b89ebc565e2066cb1a5d2d2bec54e45877aa332f9fe4f22c": "t71g_cs2m", "1155101ee5c8063ba5e8054a9394e6242be82c8a0c50107b1fcffb5145f03a72": "t71g_jl2e", "268eaaaec80138a15baed34da1e231f3bb8b132f73f471504f5f4d47f7bfd710": "t71g_sectea4", "c6b69c68eca1e9a4fa314b22ccd6f5ef6cc857de9d218b5abd6b52854ac9293a": "t71g_secsc3", "1c39a497f71c2c76705c5f19e935495d09d59e808039d508f8726334591106ed": "t71g_secjl3"};
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
