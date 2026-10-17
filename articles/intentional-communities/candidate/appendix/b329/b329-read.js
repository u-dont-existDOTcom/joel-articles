const want = {"8bea27343442110809367a620e6fe85ea63794862aaa773f441f26377ab3d8ce": "APX-A", "a44cbdaccf7356a2a67012c0163f4019535c2560c58a86a68d5800d1dab46659": "APX-B", "b12ba235cc70722cf9fe5ad91e11a01b383f026593f3c7de280b10ac55f2956c": "APX-C", "38eb5cb59785629888205cb6f312ce48f95a2d03f359823971bc51df2b19c2df": "APX-D", "dd2bf002e4ed654fb7a5fefc7ac5552fd768d9a9f68d9586d0094452472565d7": "APX-E", "fba3451eb6fcdeced0171317b7606800314a16b20c0c57aa8fb136b4e8e3c8ea": "APX-F", "8dd4cb660c8bc92ba4fbfeab1b7463864787ae58f680941c1a03ef4c96f65a95": "APX-G", "b070278841924bea2a49f8de060786a1750589e0dd263bfee37f4d3caa680d46": "APXv0"};
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
