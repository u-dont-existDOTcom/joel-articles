const want = {"92c6fd548ac44de86a790a45a32ce87227717c25c056a33416fbc599ca48ed17": "t65z9_sp4p1w8p1", "0cbd704f3bdc987b9a59adfb591dd716b6bf9003692b756101ea625de8174bc8": "t65z9_sp4p1w9p1", "6403501a4585702f325a64c0ff2785e65462d3614350b080143e47db923bb786": "t65z9_p14w8p1", "b5db238db802bbc49da4ee07b07b6e6c76037c27360aee1506efdcf8846c2ff6": "t65z9_p14w9p1", "f5f98e51efe1b6d8de4746a16a09bee5ba66a626785fced29a0a0e0a4f5e647b": "t65z9_sh1w5p1", "2c78f9fdb2ee8cf74c8aad2bfd89b61672807630297eab3a373839af4e95fc16": "t65z9_secsh1w5", "34c6acba351c4bd96d7381e15ff9a6e20aacfde3f155f447c4f0fbd50fea883c": "t65z9_secsp4h2w8", "3ba1ac1dd810324938a16640b41f0933edb56e3752d57fefc622bfe35ffe9f5f": "t65z9_secsp4h2w9", "4f11fe6e6eb91d8e5740d510face9d350e8d4cfcbf0d30971cf9b86d08fc5e23": "t65z9_secp14h2w8", "2e9c7ad99a5ef1e2ac4637e4cbc4ea97f842baac65f1cf5ddef0cf658ef49356": "t65z9_secp14h2w9", "9e6ccc048e3c8ec13b8add3b99a57ee63d6407bde42a0efea36a6666cc3f3e5e": "t65z9_secp14h1w8", "f774109e9bdb942b22a5889d71105c98b6539c56a496462afe7aad566405b2d6": "t65z9_secp14h1w9"};
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
