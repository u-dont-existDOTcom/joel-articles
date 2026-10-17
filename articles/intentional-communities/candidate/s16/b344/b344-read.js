const want = {"0a7a0dc7cba60d6b15957ad136f024d040d1a30a3ba4c6ce12833d817cdb33d2": "S16v10dd-H1-P1+P2", "b4241b785794ebc2b8bb7f7978a3fbceab2b972a2d083bf99fa19d0f669b1861": "S16v10dd-H1-P2+P3", "34baf9c496d526f082aff2a745f8e34965ba272246cf957618b97431653ab344": "S16v10-H1-P3", "60cacf8d82d31b6c9c4d032877285eb081cdfb724d2d62e3099d23396a91c43b": "S16v10dd-H1", "1dc5b51844a0fde4556575a4d925fed93113e4dfccf6628badbebf1be8bfe915": "S16v10dd", "5204a0060e02b3ccab3b8f7de76c905fbed7c5e1e60c20f41a33e5a4e7a0b1d4": "S16v10db-H1-P1+P2", "2fa2672610ea52c8773cd6c3cd4e0ef62dab3ab6bf533f4943b87e92ded771fd": "S16v10db-H1-P2+P3", "bc6b1a084f79eb51d4a18ca733a2a3b7fdfa0d796cbf3062955e829e0a9d05a6": "S16v10db-H1", "5e0454bf7f6a907ccc15c613c25dc7cd4c966a44a5d1c9a9d6d7e82d116f5ff2": "S16v10db", "c34de8da244767b6b5df9e99b1004a2104db2c40c7aadc0a53544ad7eb629a62": "S16v10ed-H1-P1+P2", "2c265bc8ddfa9ce449b6db048a8a9f813b3c0d3456c35d189d4f419e82359366": "S16v10ed-H1", "7ac7fe1c705d9beb93a89dc7907bf46c190ad27ceab319b075eaa7862d568943": "S16v10ed"};
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
