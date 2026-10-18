const want = {"3f2eabe7202aae7f6ce452ea1952b8db23b444ee8f79a72e021d27d705f35f94": "t71yy_ifs1v", "790a13b7c9c5cd833ecd88f45d36bf75b572d7a5235aab6493ea5bc1f3a7c75c": "t71yy_ifs3x", "de0197bc33a4261914f59e335bb24d62228c3a03ad6bd50d9a988cfb7b53f5b1": "t71yy_ifs5x", "83bd2bd94e7659d287ed877fe4d965fa556510d5f03160983b7c5d0466a16f47": "t71yy_ifs5y", "7d3e50d9d95dca181c0d51cf09ca35e497d226c51ed06da38058b3d61ba2a0c8": "t71yy_secifsx", "82704f6739f4808c5826478d0070b2522a61ec1a2440c45ba4dd3be04b5ba785": "t71yy_secifsy", "9a584609c9cd0f5085cbe7d2d9ea1650ba6c459babcf27084c2133ab9904aec8": "t71yy_ifs34x", "02aa510b7fa62b30b04de8df4d5b18b1c69e0441f83302306e2a58b495c16e5b": "t71yy_ifs45y", "afc99d8b856049d46aded08caa4974556342fd595febdb33bff65bbad442ed47": "t71yy_ifs56y"};
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
