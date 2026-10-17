const want = {"92805442b56b69d36ea18f2cbe01ad076c0cedb6c4eaf1f14d0d188f5388ef78": "S13v37-p1+next", "a59a7ba8c94d2660d3833f56393a2fbad0f31a7bd73399dd0dd29c6397b42f81": "S13v37-p2", "c0e5a63c10e8a2c987f396082c0a7855953d7ff7957059ca2ddac6558e0a8982": "S13v37-p2+next", "697ead7eb71dbf73141fbb97d3b9548fa6017fb57cc901b1493b774270617b6d": "S13v37-p14+prev", "8938b1eecd6ac61ca19a663ceec431e2e5546cae077f8c69e56c306e42a1b60e": "S13v37-p23", "1259b6a2796b9391fd5bfb22d103d1d7356721f52a296ac57cf634e9207e166a": "S13v37-p24", "0ffc6b45d000a320854e9a6fd84592affc5c98c7afd139a885c655637e482de7": "S13v37", "77f873eead7e05cabde79a4e4f9aad3f3941c27690888379541f0c0e43d20052": "S13v37a", "b495945d4e605875a88aafcdea8da0f7bde440aac362249ed453970a17a4b13b": "S13v37b", "274645a14542252a157ebd44361872906f07a984095dea650b216babf74cfcb5": "S15v17-p20", "8b2430d482d0ded2020622493a7d8b24315635c2f989577645d417a7d515a64a": "S15v17"};
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
