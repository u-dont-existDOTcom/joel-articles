const want = {"b5aa8e96f78f1d3a956852b2ec76133116c6a3febc061913cc28edb796fc9d16": "S13v36-c1", "acdc30fabcffa1ec88cf77d612992a1326ceb50a7b1286355b434a910985df5c": "S13v36-c1+prev", "4b802369e8d1a513b1bcd5c8b2e811ce1e2e69fd351831b2ef59a788dd1deeb1": "S13v36-c1+next", "7d7ebbf2f213e34f6fcf0f9bcdb8c4951cda98e58fa7628342246dad0b127746": "S13v36-c2", "1352e907d4217f6f530acee6f5d024521ddd33dff9b048118eefe3b63e2ae941": "S13v36-c3", "43c8f1477c7084b0cec82d8a1cc9b01182501eaaed64602e06b79fd21fc4c867": "S13v36-c4", "c96e054951b31348e3b022b806cca7befeb53c547567803a190088a9de337a63": "S15v16-c5", "9521cda09e6b6ba87875363d7c6d56e12e7e99558a5fe8940aa39ef94bd6fea6": "S16v31-c6", "edd7486a56a1407aeeffa37e21eca57f02b2ecda023b099ff5b8567cbb73dca1": "S16v31-c6+prev", "caf62a484eca49515486df5a952931e5fadeede20ef47d91e59be320a4d23f10": "S13v36", "22ef104c330f055fdd4b2290a79a30a3184f0c6466fd6597d9593a39c23cff9a": "S15v16", "3e96e68dee2998dc9174ca4e5169862c8bd615e50906357b12f39b7ef8977086": "S16v31", "4f6f16f82ea4a05177c12f03d28477632dc8456a922792b4676c434c49d908d6": "S2v34a-P2+next", "421ccdb8fc4c2c8f4c8d81b8630fa090ec1690e8237f831b78e4d2b6d0f50bb8": "S2v34a", "91440e601563277b1b178cb0d2e03d1879549fd95c8b94d3c401aae874a5927a": "S2v34b"};
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
