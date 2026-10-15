const want = {"6385ee68a3d06cd2110ed566d680e553a0490d83657f7f799d81dac238cbcee3": "S13v9-1P4", "554be6fb23d959f1bf53a90cea82ef2861d7d6dc27cf8557af61c3c76d10fc2d": "S13v9-4P2", "74836e667339f0508bedcae82f3c9c93dc13f8fe12ca1434fa441f7258db73ee": "S13v9-4P1P2", "b49d27d42f4be907a474d6172e4683a014a0c725e67b18aa997722c8d033b8b0": "S13v9-4P3P4", "d83c7921bb03475e04b65deb6785f9ee94b29b5802b8d686d6fc0108755ebde0": "S13v9-4P5", "272b3b02f4cfa4856023629651189844f04e5d67fb2cee02073ecc9beba479b0": "S13v9-4P9"};
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
