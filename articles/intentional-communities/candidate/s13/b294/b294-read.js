const want = {"5b6f6abf22be40966a0b82f56491cea0ae9f20a1e6ca66ad6404a627638f9af8": "S13v17-1P2", "d1e22ed8757cdd18678e15e138cb92242a5c86dfeacec6b809d9ecdef9949f9b": "S13v17-1P1P2", "eaa3ffe654437dda3a447463f2847080d5c5f893d12d92c034c9173679b921f3": "S13v17-1hP1P2", "e08ee777db1a9039f81e27287f3e2ab1a2f79534624a0e3a374f451f2c7bb5e2": "S13v17-3P1", "c410e998b3b3e68e56a53613a9e937ecb097fa2953164567534db52d6a79ba1d": "S13v17-3hP1", "7fe17290f374433ba5eef3a927bf9052a7eb8dae014a9341b64bf56f9dfa7204": "S13v17b-3P1", "19c83da3a48bbd72c92fb82fe30ef970597fef527752bd74ab8b2341118e0611": "S13v17b-3hP1", "23a6839a36b4608faf61c6bc250001c4117ad812466afd6c38fd1b4e45a2f1be": "S13v17c-3P1", "cd974826ba79f9d122c83340de3cf09b50963202f46e78c964defc197e10213e": "S13v17c-3hP1", "349c137949c0200a40f1ba3253cbcbc72e10e63cadeafb8ac2b1a688a47ff5e5": "S13v17-4P5"};
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
