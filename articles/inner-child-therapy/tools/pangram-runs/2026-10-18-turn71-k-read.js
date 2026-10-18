const want = {"73d34f813639eae6c4dd30cf6eb0361335ca63ed75783563b3c3bd80f04d465b": "t71k_oik", "76a9d8c5996fc1ae2a1b08e408d6db40906e581217c65295f0179e05c64976a1": "t71k_jwg", "3939eb12d07e7f87efb3e0fd75b40ff5eb5f6e81128d1270cdfc083359804e8b": "t71k_cspa", "e57631de66aca2318c0e3f0e75318a6c3ca0416cd6d48b155735f0eed9a29a85": "t71k_cspb", "56963778dd49b28a558a175e1fb58de414017c041cf3e316a0d083dbd002ded1": "t71k_cspc", "619b4c663436c2700a4325f81a552643d42410ae4b2f16987fdf92f039ef991b": "t71k_jlpb", "c9104dd38ba752ed2a69df40274002f300e92245759ddfac6557e5a7c875d7cc": "t71k_jlpc"};
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
