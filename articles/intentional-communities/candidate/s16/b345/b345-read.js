const want = {"f08d2001a366bf016c53143eb6392115f178a733257cdc98ab3f913e8c7793ce": "S16v11-H2-P1+P2", "db0960ddc2f603d9cbbc01b39075d4de10225dfdef590ffbd54f48514a025263": "S16v11-H2-P2+P3", "2ee758ae8a92ee278ac2d86918da37a190ee4698a5f75e083203dbd8f565b281": "S16v11-H2-P3+P4", "3743e827503a1a85233f45b82a745ee0e2c314c9ea17c946f24ebe9adb96cb5a": "S16v11-H2-P4+P5", "30c9b167a5510ee31cc3d8e26725a1c0988cad4d2306374fcc34edc469c36f56": "S16v11-H3-P4", "682178e33bdf63c99095ffe1dfc4ea03757c57b132e71f1959fe82cbfb6c83db": "S16v11-H3-P3+P4", "f27f01e351754762875553813019ed7d2f91c32e94838fe9b3a01c095f9e3166": "S16v11-H3-P4+P5", "297b59fcae2fd0487634f45f1150e49d94d1dbafc592d1a7f29e82604dc1a724": "S16v11-H3-P5+P6", "f166c836dcd2d0b4223edf19bbe33beba17bae8d4cf241df771bccfe5d7cb7d0": "S16v11-H3-P6+P7", "5c62db3d119e2b135046024968a1b538b7fa6029fda137c419e53a8af55b8d46": "S16v11a-H2", "1863a59024ca1ee628a7d4e75d4e330b35a39620676e53e5556c16ffd21f44d3": "S16v11a-H3", "764bde17696f6ad0b9558e71bf1c5d7abd3b1b0f95f8300816f0c900b0858b9d": "S16v11aa", "a48f2bd6ca8e55bcdae5baf6be8a28855fd8b4f79655a3b19258ef14e1ce7afb": "S16v11ak", "b0ff3ec05e0da27c0146cefac37b27635c7020f60a2f60d99ec8ab39bfbbbf52": "S16v11ka"};
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
