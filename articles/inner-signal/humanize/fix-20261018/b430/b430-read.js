const want = {"107d53a4415d723c26d34a22ed765d02fcaae13407d1fda851adf3ea709d9a2d": "HG06-emuA", "55f20080bd51e33904572ce5fbc511a1d14a969cc6b3b23b7a66f0f75bdae235": "HG07-emuA", "b4ec3b498a427ee6b6e97ba1843b09a443f8fdb726b1b97c822e352add86aee7": "HG10-emuA", "020e45682597caab09bfaa1f7188457b8d921474b916f0e2172ced516a5faa95": "HG11-emuA", "76fe70ec073b1a81c1c5087fd584147b5405d4fd80a2347d222bce4f3b4b23cd": "HG22-emuA", "6e8ac8c86f1b0924bbcd4b41fb478fad9e6a65b1cd7f0ddc25f6ff9a4e4e0582": "HG27-emuA"};
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
