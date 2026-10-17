const want = {"6c3fe960e63a33acec33ee7118b392ef274cdfc581003d1451d2be550ee8eac2": "S15-A", "867cfc4d0336722b9b2374f6dd48954ef39dce350398a1185b3ad09da0718188": "S15-B", "12fa6f36b3de213fe39d9c5c740866a79a9b660c29348569ed06c9ea38f2940b": "S15-C", "e199c819ef5b885278cacb9dce758f932504e31b9c858fc29f073efbb129fa9b": "S15-D", "71290a0c2e5c4fe7304c32efffb0fe8a99d5dfa794226af4a5271b4f8d38bd5a": "S15-E", "faa799a1fb34b735c266ff5a2d9972f76b2a690b8bf84015d4c58399b75319f0": "S15-F", "099647a894bc2bf0ee125921b078f7626e97285ba3d052700be4942158ee6eae": "S15-G", "55f757beb098eb852781d7708f021179223b029f06760a9b59c034d7fcca3290": "S15-H", "fd56cc5c8f688e02f0f12203a1d684794ea51ad8b47fbe2727c389094d837f87": "S15-I", "17a786fc570103ae88f00e055981b4291b63a2e944e36442236f4109d81f7402": "S15-J", "9155268880bec0e45ab9311ed3bd8a1c66f07ffc118a7fa03841f61f661e70e1": "S15-K", "b8c4516408410872e19494f1a4e4003dec81513b46f7266d9bd022cab672e3ba": "S15-L", "5c7ca8272942edc8787496afb3cb390496a2f549aa51464eed3e97f4a3679984": "S15-M", "532226dd83cf65489403d70f4ce37992b45639408f5822336e8f0016521789fe": "S15-N", "74389354eb9590dfb3480853ac48d98bf3ad5e9f9b6e23a9abab20c4deda6c4a": "S15v0"};
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
