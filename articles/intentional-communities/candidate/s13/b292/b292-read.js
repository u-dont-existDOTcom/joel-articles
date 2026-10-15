const want = {"dfd377d76e2c98fbd8499449cc99317bf08f836648f94847c64996eafc085ea8": "S13v12-1hP1P2", "7d533e71df00d15d75c8f64c382c6d35d3fd70903739c90eafbd07cec4c944e8": "S13v12-1P1P2", "7894ac41b904fb51a67165ffb287a2e3174724a43577564d97f343bc51f11a15": "S13v12-1P2", "facab2fb633c36495367f24d97bdc9ad35e7ea287b6f663a44cfcda6cca550ac": "S13v12-3P1", "1fd87d9cae26e53a9d9d47ac204c3a6e7ba39398c5aeb01f01f430c1b5f90d51": "S13v12-3hP1", "0e145a8074a21ca022dc2b5a23dc60a0d7ef31f117bffab156f418b4390b78c9": "S13v12-4P7", "44a01fc4a5780b085a51f70a4fec18e47dfdc34ad5cfb568473cfa1711545d45": "S13v12-5P1", "5137de67bb93f5de882f6d17e102e319fe5ef3693f32495a1e90c7598873ee57": "S13v12-5hP1"};
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
