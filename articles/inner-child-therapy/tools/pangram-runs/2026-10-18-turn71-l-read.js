const want = {"1b90c18660b09073b11c67128b7cb0e7c697cadfffd237a0cb9edea7f3898a0b": "t71l_w2as3b", "ee56843ed0b2f7ee0e3fce9f107314695f29a8f587294d3389289d9af8092520": "t71l_w2as4", "cc4b13868e216440ac07fa9a35ef60ce6c7ebd5acb903c68a15f9c55c8ca3755": "t71l_w2as45", "b589920b0b0bf7b1aa22e3694203ab631d0ec72a6efced8dec49aadc595aac0e": "t71l_secasw2", "589e51886f6a56bda9852036a94a2d12ec1bdd87bfafe14b1ae16474b652e9a4": "t71l_cs1d", "c94a3f168582a8ee90f7fcaf44921572f68dc9fd500ec76f0a74e65fc6c0d05c": "t71l_cs1e", "9f23a4253bfa306f0b87adf1ac8c6e63bd5db17712af3ade4ccc7343a98722e6": "t71l_secsc4", "a864ba5b36fe04597b8cd12b162a3d024602406cc2d441683e9bb114b592b515": "t71l_secsc5"};
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
