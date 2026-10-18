const want = {"351ab6bfc4b05bba15db61b0932b5fc8a963c3ac4d9c1875e23f8780b65c6877": "t71u_as4n", "4914dcace2e1caec9fa4d4672818b32a53f9cb6ddc51c0755dc04b9c0259cb2e": "t71u_as4o", "c7286eecc639582d83fdca3f51b8aa23e5e6601929e04d796cd297915e1f4778": "t71u_as5n", "f270d435a425edf058c285229e4a7586bd66fe07ba10af20f74d7267050c9d40": "t71u_as5o", "aa60123a9eedbafc840925e7f7e7d4513217ec0d7e1595c00ebf93e2c41d6469": "t71u_secasn", "94e178321b61eace0e9338f937e23cd05ce01b58e0170d85e4a0af54e8876379": "t71u_secaso", "91bea7f1db84c2fad28b317e96ae1a445c5d571e5ab496c8a24bbc8cd0dcb699": "t71u_secas5n", "b212f0fdf5f305cd12c4f3d8ae12e22d6743e5b50235358e13ffbe6183a55855": "t71u_secas5o", "ec06074122e59919f959ea6f4516c3d81a700d73a193ad3d954a8d482dacdc9b": "t71u_secas4o"};
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
