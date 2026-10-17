const want = {"ff16740fb0197f0459871cd8d7fdd51240c57921624fa17abfbcaf81275658e6": "t63a_p10a", "0c4a7f8f7446a147a83ce48f1ef1f876543d54853ec9f5e3ef5f0a62f15c3eb9": "t63a_p10c", "cab0a00454eb40cddaf460b0675bfd918135df6c0b39066fcdb7c0321b770e1f": "t63a_p10d", "9c7787cf37fd83f59b7633da89aa3c87165ca237fc0965dae91e6af538dd3f47": "t63a_p10e", "c9d657296ec89e3a15604260a1e76b7483179224a7fddb7e30527c3f43d6e28d": "t63a_p910a", "10d5b737df44eb2688c8cf08502a2e9d2c404a1b3482d466f8728b7e0d46b8e2": "t63a_p910c", "791530d4057a627d8cf1dad099eb544b2b7d13f37d437e4b134ea613af6a24db": "t63a_p910d", "e1d4a9bc05ae835fda113625d0f5415523cadfb740895b5c0c5c657464221edc": "t63a_p910e", "b83605f2de6d03aa67c79bb093b9a28d25ee70283b6a8e75ad1704f5040a8fb5": "t63a_h1a", "c4b7c618b351564574c9cafedddf8d977a3271e1b875fd8269a189d08f481d4e": "t63a_h1c", "94cc6f388437e008a45fe467bf3abe2b481cb7aae34c27f74bb68f7c901be4d6": "t63a_h1d", "d2fd66ab7fbd8cae6e87f28688c4c99750387331ed8b9470aba13eda9daf336d": "t63a_h1e"};
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
