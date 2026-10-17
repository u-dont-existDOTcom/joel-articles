const want = {"f299f205ef27144b5e13430df61ab53ba06d0b65cfa8b19c5c1635dce0bd69bd": "t66b_fg1p1w14p1", "a112c93d37e23dde37655a95d43d12d6232f5931aadab83362b190ebed7f48d3": "t66b_fg1p1w15p1", "67d98c3841478e2de3ed7d1eeba603a497f4d5ea761148fc08ee3aba08033aad": "t66b_fg1p1w16p1", "1d9eba786d777e219c7863a8c6a5076713f4c5d7a738a4f513c3300a330851f5": "t66b_secfgh1p1w14", "6bdd026b665f296cfe28cb788b5b1ccaafd60859299092d482242b900d4010c7": "t66b_secfgallw14", "602637b356f2f098e1bb6143fa919cf128f9d6d4e17893e19832218b45df11ae": "t66b_secfgh1p1w15", "51e5517d4c2711b1491b5ec381ce26aa1e3e55930e522fb67bed55e1e65c7c3c": "t66b_secfgallw15", "22f1600571b4d961572dc10b2313ec162255f175fda35f36f3ee0baf4f4b33de": "t66b_secfgh1p1w16", "3f9911b24fecc0d1bee1ad8066df306a87a8746d995e20d7cac44164f7cbf285": "t66b_secfgallw16"};
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
