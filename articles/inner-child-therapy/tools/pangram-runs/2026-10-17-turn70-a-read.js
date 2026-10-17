const want = {"5ec8e840cbb36240d2851a3fa664b285accddef37572a2b924ddfc6516eb52a9": "t70a_secst", "c1aed729c8233dd87767dd6d84d1f484980a1e49c55c5c4b3dbbc7af144690c9": "t70a_bha", "3b82d0ae48e960ec7a8861ecb49833823f982666aa9cac435cef5bc52d9fa4f3": "t70a_secsp", "a8660f8e764dd6c130ed7ddc794409a03e95b97712a7d2aba273c2c7b72ae1e8": "t70a_lma", "4131f4ac3388b5c1fce4be8f65832e4d55541aa6f612f2eded9d277fab3f9b97": "t70a_seclm", "67bc388bce85a7fae681e8c7e568152a42e8d7f4fc12e543a1859c8c539e8d7c": "t70a_sha", "ea0b5ba093b960e165a07aa06fe91a3b042de2892c1f79a3d3aeb23631ac9e10": "t70a_secsh", "bc35c8f484b739bb6574087547e53d05723b0f1b9db5ef868236415e8f5fa3d6": "t70a_fg2a", "867bee48e48e8d1e676949b8244bc001620a4e36fee481d8bcfc9e3130198186": "t70a_fg2b", "23a1d444323f047d8e1209cfe17eede49f2e59557212c1743f6e93d804e2d6ed": "t70a_fg3a", "04e7ce6227a51f5686a6b235d05815bd0c75e405991f91a3747f6aae5afef3c9": "t70a_secfg"};
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
