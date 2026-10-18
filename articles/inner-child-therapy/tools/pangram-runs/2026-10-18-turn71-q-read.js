const want = {"4580bef29ea8bc2d102d435770263b518e534e420004e460fe90df6ba4c1d5c3": "t71q_as3j", "e097bd4b4209608276b8ca3249836c93ab8e32ce2e30ed41cf373298f26e97e4": "t71q_as5j", "b0e848a5e877dfbb6506436af69c1be31ac6c49785f01281ccfb554c81660fec": "t71q_secasj", "d59c6d291b4e3af165243c54f5c855353c1eafb1ddd38d3e6b4378aecb8b5ac5": "t71q_ifs1q", "8a42428dd823c1788039d07efca4d4524717184c97a6c98dcb06711b5846c9bd": "t71q_ifs2q", "aa72f19e3b757f835568e707430991dc2864e947144554256200ce01a27261fe": "t71q_ifs4q", "5e4e362691260a606da7df92b5247ddd35c09c250694fc90e80bf492079692a1": "t71q_secifsq"};
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
