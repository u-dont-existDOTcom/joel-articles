const want = {"472bfdf72745d76a8545e3c9992c95065eacd8cca01a16b29a9d2e0f2422ef76": "S13v28", "b3829938da6130c1c471086dc0e87094907b3adadb8b8822523e2bb31888e0bd": "S13v28-H1", "5b5d98c375ec242e1a06e1de5a6789c00867f1b8788ccf7d49c80c671c248146": "S13v28-J1", "b25e9b753f87ee813e7378b45273dd38d87686565eefb37dcb9d20090795cdb8": "S13v28-H2", "6b0ef58d2658b1acc59276a4f280b22bab9a6d39025f86f6f2b08c586e6e11c3": "S13v28-5P3P4", "e9a066bf36f98cea6443b381d3fd8ba96b0a141e1731d0a0f25b5e209d3a56d1": "S13v28-H5"};
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
