const want = {"66f72278c9eee188df4db047efdfc13e8e26a813e91885302405a07ead0a98dd": "S14v4-1P12", "123b04f429ce47afb9964c1921b05c076ef366495084bc135492faee9544343f": "S14v4-P2", "5b874f6059615aa401a7ded49f18da69699141d68227bb6a97dd6282a85cba8d": "S14v4-P34", "70eac0dbc90eac696898b3da43071289a6ee5b4ba438cad20d9065e0dc57ff0b": "S14v4-P5", "e47e36c18f5adcbd757e1bc03f7f38a40176f28e2cc453ab73943dd7b63d4866": "S14v4-P67", "efc932a23e6d2030374a48756556821ab0a69305993aa577e7541caad585e42c": "S14v4-P567", "cfc3f8e533745fdb80137708b7e4bde47d974359b5d4b51c8589f5c1de153c3a": "S14v4"};
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
