const want = {"4bbc86626f750e9e434faf960ecd9c541222496bb0dc19c431c9cb5d5ab30973": "t71a_sp5p2z1", "badb8075d4a5e0040a936647518071cf1bbcfc47044b9e357a031a2e42736e7e": "t71a_jwa", "813f74f2462461e71d8367c15302edf79d1957831d4a7790b46eecc39cfd9552": "t71a_jwb", "93668b2780b1e0c464fc216633dd1a6b83bba36eb5210315001a67c4a090df13": "t71a_jw2a", "52b652248bb2f4adc36ee25f7064f822689dc2c20bba8a4f7b6287341a255211": "t71a_jw2b", "db92c3df8802f3f23154c95f147a0e1c2c47a3124e5fba967fc188d2c89e8389": "t71a_oia", "18c7fbde672dd2575f48468bf48ac5253303212c55266f92d8c234f24f783ba3": "t71a_oib", "63bc0c68ace035ded7ca965c4f6349ced721004ff9692e2a0fbf57109b08b453": "t71a_jl2a", "755957ab6576d8f303599b023d424e63c6d2de31ecdcd40cfe4e1ed6f3b4927b": "t71a_jl2b", "b015ed361221320813d1946a1cd56a612c5a41166b110771e1ea102f0e0ed7fd": "t71a_cs1a", "fc9f9a4a5e0527ccd2c32e4c8ac74a8bac3fa2e275e4ab53521345b41f7819b7": "t71a_cs1b", "a923eb4cb192979e05639bebefce10d135c79b1c8031476d7e860daef98f630f": "t71a_secsp5p12", "5bcc4acbed86e860532c6e7d9b093bec329f1ddd5943cce09899144708fe0b1c": "t71a_secsp5p23", "9e62d42c8e487de08b0b13fde554641f1347628d5ad2184a44a6f64ac017d10c": "t71a_secsp5z"};
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
