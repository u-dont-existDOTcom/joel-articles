const want = {"2cca3ed6f177e4959507c49495b6281e6f41467ca1b3ea622469100dedacce46": "S15v11-H1-P4h1", "5116a88ea7ce7eea019291051d85df49d10045f096ca818c7d2ff3913142f20c": "S15v11h1-H1", "2b9046a4d335124b492c69d258c01ee4defb90b1be00d744fae9b467b7b36526": "S15v11h1", "c473026da9170033fe5bc13fabea631de8a9f3ac5e3e10d44dad4df8480385eb": "S15v11-H1-P4h4", "f4e3d43c2beddc16924719079789fef0ff694ba3c625c857c7741639d8573a41": "S15v11h4-H1", "608224ad064b9dd449243fc8a29f06a719327fabcf5029829297fec7ae8e9014": "S15v11h4", "927821e8098a6c792ffc0d26fb6e3a70b3e2d45816454a562830ee10327e5a9f": "S15v11-H1-P4c2", "747e534ed5d7421000239d9dd8a976a5a0fdfcd88b2bbbb6f164cbd6c2eecf30": "S15v11c2-H1", "2612018909416a6967d642765350acb5c66b9bf6d256d832679cab773d919429": "S15v11c2"};
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
