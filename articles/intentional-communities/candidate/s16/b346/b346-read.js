const want = {"f9c3d693c8fc51a40eea1463808f3e15b4df6368675349682b4f61c363013fe4": "S16v12-H2-P3", "5a2adeafb495c54a621abda179fd7e95f561e1a00b04be5d9558f0f3696fca73": "S16v12-H2-P2+P3", "c344dbd44b55e65b32518b6e4dc9f061861d8707c49039d9c17d2d55ebd78043": "S16v12-H2-P3+P4", "d89c672fc6a7949bad2617d293777e0e305f82887bb7d170dc670cde5814b8d4": "S16v12-H2-P4+P5", "f56fe57ca6546f53a4f9cbd14c20aef64bacfca0e3aab5cfc9b01694b87e17d0": "S16v12-H3-P4+P5", "1d55704a9b0a0c0085afe5e2a9c00cca0e840b0a58db047b557e487569347a31": "S16v12-H3-P5+P6", "ac0abf3f8df507fb2a4a5a797a6a426eacbccc9d67436f8c5e7ccbcd7e90cfff": "S16v12-H3-P6", "acfa61a5cea72bbe601a51f9159363f20a5c1072b322b74c37fb0ff0e4797f1a": "S16v12-H3-P6+P7", "fc115c69a4b3fc85267bdc43c91dc5881239dcd975373559b8fda8137e13e497": "S16v12-H3-P7+P8", "a624cf9badc46f489f2e25bc53742a9af0566da4b7d452319ea09a719f83aa89": "S16v12-H3-P8", "0fa05e894479219b93ae1262ded2bfae6becebd4b887fe2889b2aacf97b676d6": "S16v12-H3-P8+P9", "0f45e81d476aa867f22998b97749af3e3b40e535c66afd30d6451cdaf4563131": "S16v12-H2", "eba54c4bc8998dff20bf02d246a352c9c4aca338abb184ac0be64c242d1fdd5f": "S16v12-H3", "32767ac37951c9d988f65be2f5aa4a1c9baa71ae2139cc334bff8126f6bd0e66": "S16v12"};
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
