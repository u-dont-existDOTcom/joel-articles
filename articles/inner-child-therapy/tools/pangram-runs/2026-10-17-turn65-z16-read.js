const want = {"ade116a54181b37eabd32bc1cf0f4f2c308e74337aac41c43daa18434fabf11a": "t65z16_fg1p4w5p1", "45876ff1fcea2908fe47613596530f1eb206c37fa6b57f5ca79b799177e8561d": "t65z16_fg1p4w6p1", "d99bc3bfcf8604c077b3ff03cfc198c4b6929c0facdf7f6cd5a5b455c519de75": "t65z16_st1p1xw2p1", "aa8532a955af4d2d0fb89925b9178c7b4bfdac276dbaf870ef08cf2074f63a53": "t65z16_st1p1xw1p1", "400b0d75f6cd924fee4e27961131c63429fbfc615893b43336c3524d4b86bc9f": "t65z16_sp8p1xw1p1", "c1ffb26681a7cb90d58f055798df00cdae7e4b4bf3cf7e43a49099dd93ab898b": "t65z16_sp9xw1p1", "86e5b67af5bc1d901824ea9e6ade7d57279be897cb14e7912934b7d9bc069305": "t65z16_secphotos1x", "1db1f6978d10471d8e61aa2ad9776adfddcaa1737f8d5a9d99fa91bef256928d": "t65z16_secclose9x"};
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
