const want = {"46cf692e1d316931181e94b64d60e1759f599d2d530c90d2cce7cdd5f3538efb": "t65h_p15a", "604c22861f43565f7f5f9899384e1a657dc6d4851486120daab4f3251b46a7cf": "t65h_p15b", "319a3aed24581dd53e84d56ad11b0e275981dbb576ae48123ffbf3aa966cf234": "t65h_p15c", "dc7e8c28a02e824abebbf3e6140a1b30c6fdb96d409177912ac101586c22ebab": "t65h_p15d", "d866abdd38afeb325e5f4c5a60d69d2628fdc5f440cadec3ba71af02776b1704": "t65h_pairp15a", "fdec60b830f2e8e9ace66270817a6b080fe92f989b184d105d847ae247b7e7cf": "t65h_pairp15b", "aba36ef54a0cd6b21c694df753834163f24f268328dde00f909ebb26cb01c332": "t65h_pairp15c", "d00634120a212ad8afc90bfb9ddd391e57ea5e91a3e93d6e3345b7a5af14f780": "t65h_pairp15d", "c62d33257aa3f803753cccf5725b91bd5592b36c8224662207b670b200410dd7": "t65h_secp15a", "8f2d1fd29d9464b13310a8f70dab9875026f1b98baa546c9e115e9ec8758fd6c": "t65h_secp15b", "ffb463b8a106f2d4c0ffc22cad1b90334b366ad1c7354f10dcf59f4f2e677d72": "t65h_secp15c", "f1ac92185574905cbd73d700ffe013c6ec3e26c269bd1f13c7ae7bfd0e660902": "t65h_secp15d"};
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
