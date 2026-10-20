const want = {"b2817eefbf95664755f286d6fc76f254dadd777f4e4f809125f260619e49fca8": "HG18-refix3", "48d3c5c4497ccd3208e3a09eb2d7668786f0ef8a8a15920894336d4757d5267e": "HG24-refix2", "cefb49e4467a140f5a76b94a56a5de5eb721f71dc71cc3b5d05bfa058b3a14d6": "HG06-refix2", "d1ac6e16a34b66f28b7d8520a46d2c6b145dca76b8f4486487307cd4075f1a5a": "HG06-u-p3+prev", "62c95cc6dc626dbdfffe2cc2ba23634db92592da2519c0394050956e0b9f56a5": "HG06-u-p4+next", "935be1517d779ed47719d9ecd87823a7c7ec48f4394dd79727a8e4b2584667ca": "HG11-r-p1", "38c82e7454011035c3d17587f4242b0c2c5894897ae25e8ecff0171bcbfca221": "HG11-r-p2+prev", "b3eccf01446549f692e2895c9967267bf89b25dbdc28ea9aa6e55973bb077bbd": "HG11-r-p3", "55e6bd46bcf991e4bd56e0904ceaec46f5a6d0a141a4c9c1930d49fee04b683c": "HG11-r-p4+next"};
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
