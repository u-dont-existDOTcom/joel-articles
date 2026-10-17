const want = {"5d21cefa63847cef7b656bee5cebdfee0913d24484eb14dfbf4f4db6abe7c820": "t65j_p15d3", "a5af32353b9f2031fbc3499f4d2c48ef6b1e06e958f1c9d02d818da4b4624907": "t65j_p15d4", "82c2567733cff0f179615ffc40a7c8b1a11c73ab26b39236972c3fb0fce296e9": "t65j_p15d5", "221395f1610e2a355498f551971f9e622f49b598fe2f5501fa83b5430573968d": "t65j_p15d6", "6ad16e89dabbf1bfbd19c4d72e4b0ba048c1f024e731aceae05f3bbf36dadf12": "t65j_pairp15d3", "0dadef7ce277e0ac75161a2dbc75ff61ce86d7e549bb0140f3760913f5957262": "t65j_pairp15d4", "80c4269d3e10b61eb85d0038c48ce1cb9eddfee2b6ea1215d5ce8f42ff6aef69": "t65j_pairp15d5", "37da90311be1ad1c3b055c5ccb1c2f16dcd780ebcd99581df6e5bd706d549b61": "t65j_pairp15d6", "bcdcb36ae02c8b1c02bead13582848582a83d7d4b25b499dc8b7c59261e3f08d": "t65j_secp15d3", "f35559780a3da0044be750f4ec99975e4a492b2f01d70351c7641c550e165b18": "t65j_secp15d4", "248d7c3cf7d1a4e653b693013c041e11d2be17690783ff2b35ec189b348fbd11": "t65j_secp15d5", "8f5011889867d1b91c4c8f205c3d6e11d4090fc4e674af4d611ec287b1a66578": "t65j_secp15d6"};
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
