const want = {"49c9efa138a6521079f2d697c793120fa668fe05fc5e2794b8d2f3f815ebac21": "t71n_as34h", "43c4c32c08d8443056aa008cf6061d84b447209e28fd76653a6bcc8c13fcb252": "t71n_as5h", "87988e9fe55919134ec9fc0df2ff5f6ec30db622fd93e5c2bc9b8e2492d60558": "t71n_secash", "e76b97607b697663f67c9c9b0c8620ce43d62890d5bcfc84aa49804ecab076db": "t71n_cs2n", "5a52276d93dc232055581eb0f3f00e42497a655334cdee07efe59fdbba3d0a5c": "t71n_secsc6", "bfad8e3dfd99fac5288335913a61ece518b3384e729866d3f0f3c75bf6a4db95": "t71n_jl2f", "682913bb9f3beb31e1f088bcd32f0d44b952aadff2aa79a0c572d6b3336b93e2": "t71n_secjl4", "bb0f45e7ed9e5d2b7199c8b2f8b753b016a2681a95a1908bacc1c2c86cc58ed2": "t71n_oim", "0ee09b76084eccd1864eae41f919987a25bfa87ec3f50bd7623bda2dafc612e5": "t71n_secoi2", "e2d9aa2fe6c6e7341dcdf97dec4de85e95815ee01a61f5a9ec58423be080db76": "t71n_jwh", "35545a6d351708b3f5b35a24dc605620884f00375e55d48123c7b0549fad3327": "t71n_secjw2"};
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
