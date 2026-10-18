const want = {"6b66b59fc5417a2be84cfbd8e9f2f94f058a97752f5bdcdeb861831e502ccdcf": "t71bb_jwl", "961edfdcd4c5d186139692bb06b83d485121e42e1044a3545cec341e4a86289d": "t71bb_oiq", "7ca56db582de4b3bb7a2fa90ad6315cb1639460d66f8ae3c216d7aa1b0f22de8": "t71bb_jl2l", "fa5dab12259d336ace5e1dbb6d35afa5d9a46346b978ecd8a4341574c7d8ce87": "t71bb_secjwl", "1cbb7577c21a94f008725d2b4003165b8073b6c0e64c7d55557911a9bb6ff63e": "t71bb_secoiq", "2737a030164cc429fe9b1473bba8c90761df46ea116b9e45de49985e514e5328": "t71bb_secjll"};
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
