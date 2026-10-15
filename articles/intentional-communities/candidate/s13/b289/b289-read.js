const want = {"7776830f0b1ececb9af1be65635d2de362709225869006f45e17f2e6f37d6f26": "S13v9-1P2", "8caec3660709ee9478d1aecaa536ba00acc603e2ad5888a5497e69efc3495dac": "S13v9-2P1", "66ce0519db13be26e0c9d1f01f060bdc30d95e29cb7206bbba51fccdafd8953f": "S13v9-2P1h", "056f80fd0681f1f9c95655668b9d279d6d63fb94c43a543d876aa73aba5fc7a8": "S13v9-3P4", "c9bce0f046d3b4d6b1173e90f47d452b60d61427b82c146d9a869f9c0b5ac769": "S13v9-3P4P5", "53d8cd3f25109bd01587d48a1a35b726b25f5d1bd31b24d448bccd7f96004f6f": "S13v9-4P4", "e7f89847cf2a20c795a72063e830699d802c79f63a484827ab2f652eabdad97f": "S13v9-4P6"};
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
