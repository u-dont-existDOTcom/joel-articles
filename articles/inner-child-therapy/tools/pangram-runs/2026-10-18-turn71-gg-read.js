const want = {"dba914bf92490c91ed6263f8d4b5e19f4201dbf6458ddd8b867c189924b79ce1": "t71gg_as4u", "6622e99192054a0e2692570f1202d62f0939ea88a6da3358326fb56ce66e6b3b": "t71gg_as4v", "f5bcf0df20d46631b7acb68367d0fdd36c455a05113936a6d4b568b0a7ae6e13": "t71gg_jwo", "b6d8b150a858efd24b7da1ae14a533cc3201168bbc3bdabf6eef9e2d846f0264": "t71gg_oit", "63fc72c4b857fb7952f94d1ecda10ca35f6ada4860ea8fd4386a4713a38b6ec8": "t71gg_secas4u", "e109529bc6c679566e05df7aa44514da64547393128b46a74a95fee0edcaa6ce": "t71gg_secas4v", "d392f300ee06e8e1eb088d8e2f99b491f817a84b4319862ef69d7837612814ca": "t71gg_secjwo", "64e32fc0255aeb6d166fa97a35d79f04bf42af7f2e3d1e32999adcfc7d39aad7": "t71gg_secoit"};
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
