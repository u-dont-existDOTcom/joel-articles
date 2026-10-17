const want = {"d58439ffaa0ce4dd4bf04431f69f1e9d49f28963b99c1a8ae06a6910daafab66": "t65z20_fg1p1w7p1", "f89b9b22a0cd4745f5bc6abd6f3964254417e29b6bfc6aeadd15daa6b982bb6b": "t65z20_fg1p1w8p1", "ca1d33c6f918d957b77a8dbe1a69681bff4034c89aeff42a76bb5759b9089cf1": "t65z20_fg1p1w9p1", "a227f6cd738eac24526c2753d991f6011b7875d40a2c7d9616a0f273635e767a": "t65z20_fg1p3w8p1", "e4ba1ef0b24d5dd5e04421c33dba3caae659c24ffaf22fe2b74001399a6f44c7": "t65z20_fg1p3w9p1", "4e996c00b08617be217010c36f1c5eaa4731fbffd2ebce1bd5393b702115d1e6": "t65z20_st1p6w7p1", "2d2036090bd7352b8400a60ee58c02733cb8630b32d8fb9ed909a5d933ed3d23": "t65z20_st1p6w8p1", "af3f4eb7b2f6e86895c300244267a87e024dde9001be5d862daba1a5cd3e9d96": "t65z20_st1p6w9p1"};
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
