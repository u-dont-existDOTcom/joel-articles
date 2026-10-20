const want = {"f601c27cb183fabd39b4857f7aea1748be2c11aeca9c7adbda3dacced30865f1": "t71b_secsc", "fc6f08af3254d436ae5cb88646728b5e73d3d7c89dc46f3a671eab93479688c7": "t71b_secjl", "54b432160133ece83f78c64c3c5b9a273d48117b62da9525853f329ed84f34ab": "t71b_x3a", "0b0edd286efb683fc81c5f66bdb73dfb91090afd25500f36de523a095a88f8c5": "t71b_x3b", "84bc5bbcf7b95593ce2c9263d0631f8eb774809eb73d189c9ea4c1d8feb54c8f": "t71b_x3c", "5bd12542047ba12c439df152a0563523b41683074f68937833d531465a5d5941": "t71b_jwc", "d6f88fea423b57f4678f2b58ab374976df570b7e425d1f4517de5accfc8f3094": "t71b_jwe", "5df1c495b44f07f4e8b3de4e99b19a4ae089c8e85a80a6a1425537cdee01cdc6": "t71b_oic", "f07b9338fd226d6a348a400b2f41b63fb37d532cd6b6b8ecf61ca54f1d8f861b": "t71b_oih"};
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
