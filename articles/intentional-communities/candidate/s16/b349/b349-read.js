const want = {"ab9f2d34dbf5b3b29d24acc74f7dbbe5c8baa997e358dff80f7ea601382439d1": "S16v13M-H2-P1-P3", "120b498e169b3a6fa2eb7a233c32a6c5c2ad7bdcefafa665a59d56b08b54c967": "S16v13M-H2-P2-P4", "d1cb43bf81e5d706e4bda992546b58f7f3a83360f9aa1c3a63d3885b803b232f": "S16v13M-H2-P3-P5", "2110acdbf8849864a80fc76d15ceb3fd14a02c1a3a00806c4826b43badea7740": "S16v13M-H2-P4-P6", "3afd148533e14ab52b789475379197dd3b67b5d224c8e230f5b414ea8bb6f173": "S16v13M-H2-P5-H3-P2", "c36295db5439f16525632e206300e1be9b625bb8fd0592993e83537c4faefbc3": "S16v13M-H2-P6-H3-P3", "e1a8724c2da577a6fb4ad2a87630bef7f1349df0100a7ce0b0feb999c98b0bc6": "S16v13M-H3-P2-P4", "9b009b855c93bb6903b376200469b2c6d39754cbc14e19b3095896e75fc73f5b": "S16v13M-H3-P3-P5", "07129e3831f0f445a417877af7cfe6584e89bcd27b12084c76df9fd6ddd999b4": "S16v13M-H3-P4-P6", "37d0205fd2a46efe6079590de816c50830855936fdddac8413926694497d87e0": "S16v13M-H2-P2+P3", "8283d45f6979013094d88bcbd9ef1810e2e837bef93d3cd1e80d5290e5577803": "S16v13M-H2-P3+P4", "bc8faa67767ee1337ce5269ab6fed7a66467538f30633cd6c310a2b274b37fca": "S16v13M-H2-P4+P5", "23b9702cac6ef3e996298068db2523d44e3c2d87aff124ff5ea0edf939c7fcba": "S16v13M-H3-P2+P3", "ccba73fd510408c901b6e626b5bd2454dc7a76bfc600d257c649951a5e249f9e": "S16v13M-H3-P3", "73fafcbef05d363be003138ef00e4bf96582ec4d1cf375d68fbb5dcfbedc81fd": "S16v13M-H3-P3+P4", "cd55837e84dcdf8e2ccae7739000c3c8c37825cf5c54ba2e6c3f3bef52717b45": "S16v13M-H3-P4", "a03b62f069332b8df171f6aa26ee88f5e4d4ba2e93b09ee8e5a4d2d494d445f5": "S16v13M-H3-P4+P5"};
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
