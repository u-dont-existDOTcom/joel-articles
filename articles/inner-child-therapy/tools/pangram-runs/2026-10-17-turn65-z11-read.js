const want = {"33c94f5897f9d9a9605f30c64cd3edf2fd2101489ce36c3d5b9a5db192736153": "t65z11_fg1p2w1p1", "a08eac209c0513aff6dd3669c0a0d97834cc59b63ad87906a2bd613ba4b8f99a": "t65z11_fg1p4w1p1", "d3d5e37af744d9616d722e414d082bec0d1e76cc878d8b2c8e80083da5a79797": "t65z11_fg1p4w2p1", "254bc62b558744f0b7f5f8071edb71f0a2f2a08380e9c13a337e38e847d6b6f1": "t65z11_le1p2w1p1", "fe193314813fab56b352d72d476a01ca8fda4e976816063f247b092e6058c80f": "t65z11_le1p2w2p1", "abbcd80f50e801bcadc0a2eb6792d2fdcedb624acca1687039863e5fd102ea52": "t65z11_ba1p2w1p1", "bc3c5cdb0cbdc5c5b76d04c7d81b5a36fa403dddb66991045a0220dcd9deb397": "t65z11_fg1p2w2p1", "d4adf3057c37528b4073d768c74a9a0164287a71776ba9ec339284ef0bf8c0b5": "t65z11_lm4p4w2p1", "c437ae90fc56ac90c985dd0e5d592784d75ae75aa0694fba368bf23cdff9f74b": "t65z11_fg1p1w1p1", "5da04e899f206d74ed1ee1ee4a1f39e111c941be33f80e6a5b684ba3b58d11d7": "t65z11_le1p3w2p1", "b6f527d49983e56439f748eb5461295ebee1ae8c5b24c0921067a255ff58d57e": "t65z11_seclm4m42", "ae8083cf0744df47deb6cb1fe791f7c03d5b4f82355e6428e0f59a8d80b9cd19": "t65z11_secba1p8r1"};
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
