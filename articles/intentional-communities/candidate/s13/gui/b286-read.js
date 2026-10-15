const want = {"c42228943514f7592f47848bc49808521f20c52ca64bb6031d5424ce8162c128": "S13-A", "d17418bb69a39e4701285f51fb6745621b0a2929faf4078368499b79836336eb": "S13-B", "16a8ad64d6767620c133b2b6bcd2bc8d0110485916865411e377c410a40ebfeb": "S13-C", "05c1041d623df6cf5f4dc518c4eed8e666e8a6080765633307db20407e33d640": "S13-D", "50d70a1f97d6bc6b64bdbb09427b7fbbf1f3dc2a6630386d45099bc577437051": "S13-E", "70a35f54aa10e25abcd8ecd609c8df0348b9e4f542fa5c08a9752db66d3e2fd1": "S13-F", "549337631f6899f35a9732672c001ab06be7b7817e1afbc055af39529fa28cd9": "S13-G", "1de76c7f429bf6946e0e04e32a5ea6bbc92699866e1e967d6e3d967f175126a7": "S13-H", "5b459a7434f71ca66bdb18c1c2817e003fec583673008a1979caf6b0ac8195e1": "S13-I", "4abe2f3519e7b8c111a005d2dc73c4d554865b0e30183c1600fda2e2a41beab8": "S13-J", "f3917a7cdcf800d4a88f8e55ba86cec1806e7cb5723378929142a32fec7b9b19": "S13-K", "749cef92a421f718ba794a499391936aee1378f29a52ead5a5a4daa828c20005": "S13-L", "e7b54dfb44dbfa5d4729f18efea62fa9d96de2806300a709800ddc2a991e20e9": "S13-M", "5deb38d3e80cba6735d5133f9aad48c1017561a304d6d6400b1c22174b914afb": "S13-N", "3a8c1c30cec5bf2b03455b821c43fdaf0b38924aa790e9e643671058673e1baa": "S13-O", "dda1783f25c4bfe5a69fbb8245bbcdc9816f0868efd878c8650f2f8552ca1ce5": "S13-P", "32893d70748bf8311083194f9d07b0586fb0b7b6393eeb9666f104aacb4b9a6e": "S13-Q", "2a92d57efc6028a8a208013367b94fc755c73ae866e47226794a248b00b35147": "S13v0"};
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
