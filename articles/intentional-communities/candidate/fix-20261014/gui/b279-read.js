const want = {"9b43c12db96b0ee31fd455c8cc9f50050e4090c129867f76eafcc6f5dcea1ab0": "E-S10P9fA", "1d6a2c2f2da905d76d7603cbd3983e451f4363046fa7f025af7704fd841cac74": "S10v3A", "2076ced4405ec5fdd468b229c8ac45316173564b515d914b73b4836c6e844184": "C-S11P12", "aa3f51d942928c1cda1bc81d6f29b9c9572982122907e6fb302130480ad0bf01": "E-S11P2f-b", "55fe1b4c7064fc8e2ecfba264ffdf0412f69c9c506c46387f8515cc33cf70bf7": "C-S11P23", "8970a7dbe6f3854e120b7a515b5d577003349787df69c97576fc3eddde5a9148": "E-S11P6f-b", "1ebc903642f54453c1da427292b101f7229183bf218620be407a50ddbd1c9829": "C-S11P8"};
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
