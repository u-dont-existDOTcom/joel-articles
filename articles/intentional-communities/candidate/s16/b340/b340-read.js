const want = {"cc9f3ef01e74d556f40b0a534e5bc664079e1f14e98e62b147de2bafae123f74": "S16v8n-H1-P1+P2", "12fba84be82473d546631b878545fa504c8db6fbb162ba158967090103d9181d": "S16v8ny-H1-P2+P3", "7970caa963fe7184e86175e974a0be472ef678682078b599412f03c117d2f645": "S16v8ny-H1", "44fc1e609bc9724656ef5330aa33b30cd352c9d4e96c142b89adc0d85ee5b06d": "S16v8-H2-P4+P5", "469cce6530f0a4fa474c063cead497a70af7d1242e51e373506f7aba0e0c2e60": "S16v8-H2-P5", "9e90103a5169ceb044cd7bb7e454b1d285442b3da1efccd550997049b4b14339": "S16v8-H2-P5+P6", "4bee17b7c5c4b0866d2fa5f99c5f12618cdb0aed0590e8542db2971372b60cc5": "S16v8-H2", "0e87b2bfa2a942c48c59ad2e7cf4616974f0fb3b196d08f1921c061a181d111a": "S16v8-H3-P3+P4", "640956f6653171885fe4b8ab1718fe3ab9576ffb29c3450ebe6647e177dcaf8a": "S16v8-H3-P4+P5", "4484c6cdb62dcc7f7a286e1d8dde0bcd824ed5c32e63fa61d1b14425f7933b84": "S16v8-H3-P5+P6", "d6f4a6ddfc68e18abbe499472fec050806594e11e5313bd8e6a5b56f230de7dd": "S16v8-H3-P6+P7", "4f35be40d7c2ced966517919021cbdaa594c03a9f283106bfc58924de4063bc5": "S16v8-H3", "b4b3c92519ea9b925796e1060de63828a05c95fa13b98ecbfdf55ee3ad25aa5d": "S16v8nv-H1-P2+P3", "18478f37a3534e89e164ee67769ff8a776d05e102bd14c582125a7bc508c0c9b": "S16v8nv-H1", "e4f679e836a89a84e46d6c57a75b2239afeac43cafafdbb13715b1d99c83cb0a": "S16v8e-H1-P1+P2", "e8d61aba601d6a795ec242c2098ffb8f506c964b3368408f133217d665b261ab": "S16v8ey-H1-P2+P3", "b88bc3a87394480555256aae28c08d24caa9cf15ffd164b4f4231b49f8a467c4": "S16v8ey-H1", "e0c71982f1b2e2332c8a235014268a9c17d242670ddfe5f03b2ae95a75114e71": "S16v8ev-H1-P2+P3", "25e3b2284e571090a6c8ce49407fb3ab8d2914bee90d7bd1af833e9720532eaf": "S16v8ev-H1"};
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
