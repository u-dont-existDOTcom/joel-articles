const want = {"688d55b991d9b56807afeeee722fed8cbceac44f8e2f032eb61e5b09236988e8": "t58c_p5a", "0440e7b735bc3bc968a094722ec86e074fe2883c51dd18bde6415ba2790236eb": "t58c_p5b", "7a4b72f3e2fc243ba4f3ff6056458323676787dee12e036fd986ebd00484ce19": "t58c_p5c", "c460e2828b9f8de551e10a2c3b9b86bd6d23c4244b18b39d27f609c01ecccdf3": "t58c_p6a", "f04734dd12973837f0ea2dd4d28237190dd5ed195073db8e9a7074349b41380a": "t58c_p6b", "59a34f541b4ac01ca8d23188a335a05c3674bfa461e046ce46b6d3636cb065c4": "t58c_p6c", "61897d92ca7cf736c64fbf05cb1a17f3bfd2ee9ae1d55f4f2b47afb5f23824f1": "t58c_p7a", "d5c3605f84fa79f4fb81843b91135a3a2185053a3112c9b3794c2645fe176307": "t58c_p7b", "18bfb9ea86081e273c27e1d9f79dbf93f2b69934784e58449ee26c39877da850": "t58c_p7c"};
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
