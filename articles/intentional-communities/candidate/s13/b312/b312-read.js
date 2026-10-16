const want = {"319cf69d13ed629b8aa854ef8137d7f04da3c249d7800b65aba157d3cd342272": "S13v31-H1-P1", "5b6f6abf22be40966a0b82f56491cea0ae9f20a1e6ca66ad6404a627638f9af8": "S13v31-H1-P2", "a20bf0776a6d966d41b37c13e20578665f7ff1cc1722ad26b32707eb2aa16a90": "S13v31-H1-P3", "88d3efedcd79083a276e16c1bcbdd5d6296f67c3ab147b8b06103f77c1447199": "S13v31-H1-P4", "8caec3660709ee9478d1aecaa536ba00acc603e2ad5888a5497e69efc3495dac": "S13v31-H2-P1", "98e49cc8eda11764532436d8bb92bce382a1c6a012edd497769f2958fa2783e7": "S13v31-H2-P2", "02603fbabc811dd6a02728df1ed8788d848454dae7c14ae7605a80842e08e13b": "S13v31-H2-P3", "4f95da94da99433a53f361dbe0ea7bd510d0041a27eacb3286a4c153aa95b6f7": "S13v31-H2-P3b", "565e3401ff08b2367683f2ae0d49aea665738e2d7bd8c12c249acc590a01fe4b": "S13v31-H2-P4", "68cba9d5b217ce3c3521b9cbebc65c54fc7511405203b30f06c0e446c590900c": "S13v31-H3-P1", "88eeb42e3063f367e0dce00314fe52ceba03e7f1bc3632032b202e7cc6f825ed": "S13v31-H3-P2", "cc753f80e4150e88a1283c5131e52d1b5dab7777e93f29e7a439c7d568477e95": "S13v31-H3-P3", "dafb42296af3cd2251e755d22c5cb0adf34d06ba42cf64fb8261dfcf770eaf47": "S13v31-H3-P4", "5978019551ad64b643efaba3a2066ae0d9b3b72c146ecadc675e1ca793d19e48": "S13v31-H3-P4+P5", "18f9f783bda4cd8f05cf85b6cc99d37d5c7f518151b1de250b9c8bb474940e26": "S13v31-H4-P1", "6fdfa27fc0f73e364209f1cc57a98076c51a271da8a3c21666fd1d4e4abc1c72": "S13v31-H4-P2", "6e8197aa70652ad693a8076ab54ff04346af3d7a2008e47729a81f988d59aa84": "S13v31-H4-P2+P3", "53d8cd3f25109bd01587d48a1a35b726b25f5d1bd31b24d448bccd7f96004f6f": "S13v31-H4-P4", "f694abb8ca0bd17df9c56d5d4e5f6e4784e4cc40711879435c102efbf9e7f746": "S13v31-H4-P5", "2678e3c8ccf3d06a6265d1badcff57df936eb6dc755a90d92f2ae33b382f6801": "S13v31-H4-P6", "aedcd2e7b44ee26b33851bc21f7ba9dcee04915a3103fc9bcf82a4c9b30bb0f7": "S13v31-H4-P7", "6c47fb37461760eff77215a716295b3b3c01d99d96bfc37693dc978256517f02": "S13v31-H4-P8", "011f26989ebfa99eff2c416a360fb3ea129c51908879799b1fd1c2097542bd85": "S13v31-H4-P9", "98a02664761dfb989b12c7de8f9f3775ab96ba2744efcc059a566eb340a4eeaa": "S13v31-H5-P1", "df1ec12b367467c6da4ce2e13de678d1d679e75ef0dde8e21219e58cacd2d5ad": "S13v31-H5-P2", "b1051388bd326cc04d7d422bef64da73ceca22b10bfe1fcdab357cb3fc021ce4": "S13v31-H5-P3", "d462935f405ad4797de6b084c5a232bdce0200f219d6a3d8d154f913918a6ce5": "S13v31-H5-P4", "ed90ae6c429c2c31f1e3d78a4222c5f1673105fd14646c91d8b099e105aac2af": "S13v31-open", "d5b96222c06b7f56f6443f9c015d730ea400b676b0b37a11d8a89e999ae4bb66": "S13v31q"};
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
