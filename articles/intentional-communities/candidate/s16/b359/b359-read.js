const want = {"b338b0a7c5eabfddf9e16e3d20b29f64ea4abc863754f891f0ac136ef0ddd976": "S16v17hq-H2-P6-H3-P3", "403cc056caf38d6cd227bcb81a6e3814e5c56d00316aab0d9e1d18ce6d8e2118": "S16v17hq-H3-P2-P4", "d1617fae2bc1c6bc3c78dffd9c06f0a1c3c94f6af939184c1c314327e90828fa": "S16v17hq-H3-P3-P5", "2e416bd03b21d34c69eff61385d7debb6e13730ae2404f351cde5907656da38a": "S16v17hq-H2-P5-H3-P3", "80e438ac1f8e0c2de2ac6105e36c2fe9bbe48e955c13fbc0a101c4390fb10105": "S16v17hq-H3-P5-P11", "ce59e4d87e7f78947b305bbc5dd0687d378c67fb3299ba65f391fcb500684602": "S16v17hq-H3-P7-P11", "043b888cc9e48f0d4bcab127675a7fb4f550680394022a1406733b51da6cec9e": "S16v17hq-H3", "73db6aba84bbcaea7e6f5ef4f273d6cf135ec90b780b8bf8b7095273d81b0ead": "S16v17hq"};
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
