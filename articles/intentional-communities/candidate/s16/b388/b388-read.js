const want = {"259e9da9f9f01e9d68b4f90f093b290941065e7ebd88dd648e2efdfed6073974": "S16v24-H3-P2+P3", "96d2b2b53b20e07327f5bcdd09c6035b7d633528cdbb2d60dd5682e1ad82c2ef": "S16v24-H3-P3", "80fbe15c75c6a6657261d32b60d6e6643507fcc485a6879c34695b4f9d7b2479": "S16v24-H3-P3+P4", "a7065471c9afcf599a6858fe05664fd82687eba4fb15df0375840f8353fd8c02": "S16v24-H3-P4+P5", "790d7033f0bb3bab3521221006ff936283c4aaebfd36665ea45e65a4e7e4bf48": "S16v24-H3-P5+P6", "97713f5b05d7652bcaa5d3b35b945620f8946b540ec43f30270b3dcaefe6c21c": "S16v24-H3-P6", "41101074ed79e51fc0a203ecb430388855b572426ec5c6b32701ec7bd04e9ee8": "S16v24-H3-P6+P7", "8ab8cae3076ce3e1295d0dd20e9ec983a74d24f4b2b3df41c35d6f615b615e32": "S16v24-H3-P7+P8", "e3923d66e61e0590789f800cfbdc0e66ec6b21b13a8f7dfebebdb62cc79b99b7": "S16v24-H3-P8", "1f3f543de38ad00ebc59adb2184f82863f14641b711045837ab9d010b591f09a": "S16v24-H3-P8+P9", "b14fba35a092db1e9777279d61dcc6fff914fe090dfc95c3053888a4fe0e087a": "S16v24-H3-P9+P10", "1792c9fe39971ffd67373239e5554ebe90f85f94a69e9e4d0851682ef3ec4e60": "S16v24-H3-P10+P11"};
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
