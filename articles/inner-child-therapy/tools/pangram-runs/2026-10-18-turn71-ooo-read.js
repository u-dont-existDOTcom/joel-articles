const want = {"81c9d8d31bcc8972a6e7a199777f7451538a3e5602492637275e797ca81f3ff8": "t71ooo_tf11j", "553d394cef39543ba1aeae090756e88de08e33cb8615a20091b8c96fd0b1d4c2": "t71ooo_tf89d", "abc2f931d9db0e7a94852d33b3ccc543b881e34b2d588817fdc3ff79b117a691": "t71ooo_u10e", "8429c951a03cabd182cd31a4f56bd074b4ee35f5a526709533f71a2f9bb3f0e4": "t71ooo_u10f", "bebddc5ef88559d43b5dd5bcd8be9c8647ccd64b1d838a2eba48d5fe902f453f": "t71ooo_h1ooo", "f0016c21a759ff4687513851095ab0cd0c0d76b372cf80fc0b8910353e46d331": "t71ooo_h1ooot"};
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
