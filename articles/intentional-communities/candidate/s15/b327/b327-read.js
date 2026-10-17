const want = {"6cd5e34e1425a3f6ec287259b73343a5728f375478269954bd4c9d6964b4897e": "S15v6-H1-P4a", "836ab9eed45240092472d9553c9364ac1e8e469bafb4bffa0d5a418b1a8f2ef1": "S15v6a-H1", "2e3fe3cb8a1724c14be131bc3b2cf7a4cda607771b516e9d1663923402b933e6": "S15v6-H1-P4c", "3befaaa4b95ae2dab57c0403cb999cbaf0afd183ca53fc0487c22ff11ce33161": "S15v6c-H1", "7279cfe2ce88374db983251778917f09a404d925562b7964fc69e23f552a472c": "S15v6-H3-P2plain", "0bb5ddd78925c7183ee783e79776c058b296d44f899d60491a7e6bd6c6275c2c": "S15v6plain-H3", "9e6738c87a9b3fe4bc1620466ad8e3ecba451c5bfc6e30448d8ab8464bee6dca": "S15v6-H3-P2l", "5fb5c693bd22f4b0bd19ec27c4af2d22a458abac054809075918f57c8a84f877": "S15v6l-H3", "96b7fe156545f14f2605b10f81eea1e2a7052e1f7f148fc05b141e987586138e": "S15v6", "570f10ce85903594bc6a917d575d733b35258fd463e019dbef53a5b5f170fc37": "S15v6x"};
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
