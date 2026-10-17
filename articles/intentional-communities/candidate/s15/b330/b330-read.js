const want = {"0a386d3cd020c5935b8b017b334758cd902a3d8d66d63e7ae79ad4b0d6bce3ea": "S15v8-H1-P4g", "98800b617c44805907176c05e5e88838eaf7c227b5dc630670d56e4e8c617b5e": "S15v8g-H1", "0e3e52d6861280c2fbf0b21d45b650ecf871a8becd97006867324c4130e528e1": "S15v8-H2-P1+P2", "7e5a8fda915e867995f156d0e8e498548074dbe58dd49b8993314723de38d767": "S15v8-H2", "a8024b17ba362f90f6e4659c6aa48d6d6cf706969713780bcfc2dbde895ba279": "S15v8-H3-P2", "c1ef0a495e179b5d006ec3cc11d6f9a75a277d92d1e6f848a5d55ab130fbf339": "S15v8-H3", "783063a2b752dccbbc7ea67b52c24ff334e0ffc6427f285ae90890eaff90865c": "S15v8g", "5896fc15f3153c34c82536c8ab9e861d0be6441c82d2a7f68d3a2a05401c99fa": "S15v8-H1-P4m", "e97bba74d28379008b3a004678371131dae80a88f190e8f65c6210c38de45878": "S15v8m-H1", "b8145bcc8ddc2fb262ced530f69362f7565e15cdba143eab30691483248c8929": "S15v8m"};
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
