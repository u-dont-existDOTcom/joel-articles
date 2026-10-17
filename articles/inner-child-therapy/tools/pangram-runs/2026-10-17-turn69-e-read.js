const want = {"5e1b05fe3e99f4238ba0a28d37bdb22323b6e68bfd30b2b65d696aab449508b6": "t69e_st1i", "bbc8d193f0b6ccebb180f7b566cb250d83fad0de139beb3b38dae12260271500": "t69e_st1j", "366519e5494d726a613428a0914daf961d20d0d7aa5c5e5fb0a902c343af3f35": "t69e_st2o", "9f4bd41bc3ca2924eecb2113944839daf38af97dbbe60228ec54ad56e7b684d0": "t69e_st2p", "efdef0c45cf4adfd412050b7d1d7fc2a537f890c5f76243653dea078b202dae2": "t69e_st5i", "d70ac284bced3da9e58ac61b12d4e739fd0053ed6ce5a3bc7c9d80b67cea211d": "t69e_st5j"};
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
