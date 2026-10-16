const want = {"8313914a196ea4fb3d9a41c79244131d1e15b752f9534d51e906721408653312": "S13v26-1hP1P2", "4b3c4254bc67787439347c1341e966ec4a0b2fc92fc12696870caec0bc0b0b19": "S13v26-1P3P4", "95172e59f91b005c20b1b434f7ee855a4bf6cc94137ef4c06bac12e83d0412f6": "S13v26-2P1P2", "0fa7d9affea7130aa9062d7c80b0b8682068c56f804fd8d218a09de4e0b9a2ec": "S13v26-3P1P2", "cc753f80e4150e88a1283c5131e52d1b5dab7777e93f29e7a439c7d568477e95": "S13v26-3P3", "6d4cae5c620f99fe685eca9ebff1aee48868e3089d22f39cabd6d2b76d415d2f": "S13v26-3P4P5", "665484478150d9761d2d682e577717827a27987f4631fc2beb74ddd2eb351029": "S13v26-H3", "0f6e2819859ea86c2c64effd44dc738730b007824bec74deb6b9a87e93aec559": "S13v26-4P1P2", "acfccc70378a315662282478e089beb751b5c32e691978217ab0921d84612a1a": "S13v26-4P6P7", "783801134b7abcbde04bf6254438b6e0bb208b51ea73b7a3e77a12aa013c5529": "S13v26-H4", "a03754abf03d0c788807c6860f9f3118eea11bc1b9aaa4bcdcfa3181aaf719a5": "S13v26-4P9h5P2", "59814cfc1d977f24261b8ad4f275f61244294d2b12b905a69cc8507d4cd15e46": "S13v26b-4P9h5P2", "ec4995542c272250be898f22a57a64c5f37253a084e1c4c5e5f4c092d87d4050": "S13v26-H5", "b05ea26c16950782cb42cce84c2ecb9f3bc86148526e5838a5d51a91940094e6": "S13v26b-H5"};
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
