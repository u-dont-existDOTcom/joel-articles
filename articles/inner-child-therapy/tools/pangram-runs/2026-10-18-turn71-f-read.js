const want = {"2e62b1f8ccfe7b3dc5877cf65f0041c53096a3a59c214c17b78163bd73a80faf": "t71f_as1b", "76ce3925179b686a3c8b6d32161451f1224f6ea32991fb49fdb0f7fc72da4017": "t71f_as3e", "6e16f2319171b42fe322932dd12d15773ca5422178c4321b3409af6d78ad238c": "t71f_as5e", "f496362b6c3014597f9b201c27e60164adf19a0091f02f71ebb749fe871a2b22": "t71f_as45f", "fcf72a0b7c3ce3a9829602bf195675bc5d56ebce488e6caceef6ab16da3112f8": "t71f_ap10b", "df0e8d186886b053b0b903ef753f5b4022ef43570f99f66da9097163b205a89b": "t71f_ap12d", "bfa9b4e90eb4497177ea5c7320040d45fadc65407f5760b5b38f2735fc675bf0": "t71f_ap34d", "08673c09a15f62e08a911fd63f12b8679e13388dbf9dd2cd93a1699db18ce549": "t71f_ap7c", "b34b0ca4ad505c3ac77a171f6bcaa27bc5bac86d0b62b8df20e06ca1f203c376": "t71f_ap8d", "668cdb50968928df2a4fe57752fe493f343974a3f3f0497507cd530ced1db113": "t71f_ap9d", "cfb17e410cd9736dd0e978ec6f1ba2abf09f9b9764dc87ea0704cc8611fbe43c": "t71f_secascore", "28de92d2112254cad2992c9a5754a75d2330bfa8051679ddfee57a6e6f362b4d": "t71f_secas6", "b0557655c6be88f250f4fecaca78e9d3d941a9875f43f1737aebc1e3a3054d62": "t71f_secas7", "bb1ff7457715ad8b59eca9af587b9e9ef035372e706e948f33049c4ed39d907e": "t71f_sectea3", "e5798e82726fb9e6530f5c135a5c48736622b35eb0e04f8b8b2b49bf63ec0115": "t71f_secifs3"};
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
