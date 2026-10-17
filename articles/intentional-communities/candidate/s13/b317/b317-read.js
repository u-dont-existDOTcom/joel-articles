const want = {"810e17783ca46d2594658290909e102df81ebf2994122d7515a8e7cc9bd6c392": "S13v34-H2-P2", "1a246ee2aa1e76365079df57a8178aa5aad434f7b1f9bf44d976a932b6901e62": "S13v34-H2-P3", "89fe8b5294a909769ae8a94e67102e444146e9fbbb64f2142ef36ad449a37918": "S13v34-H2-P3b+P4", "8608514bb17b3f7652487f8270cd2209388e6bcb016bcf0b63ab3b1b1b72ac94": "S13v34-H2-P4", "97d8e2bea5ef0d2b639a2231b3d7859e7e285cf9daa6caff409db9bdc497f851": "S13v34-H2-P2-P4", "5b1013fa871d488dfbaec350a1b8e9bf463fead62a32438c38054983de0766f1": "S13v34-H2", "16144e8243caca5b903c185fc8710af9e2ef9319718941e6b22af40dd5c111f7": "S13v34-H3-P4", "fce8f720e257f58dcfb95c7b3638c129686b9eb4e4116bc09259953f52b50aea": "S13v34-H4-P8", "3fe3b0320bbf8e49a797c3d17b8252e5d75b1ce3968ca907d7c1a9e9b721ff5c": "S13v34"};
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
