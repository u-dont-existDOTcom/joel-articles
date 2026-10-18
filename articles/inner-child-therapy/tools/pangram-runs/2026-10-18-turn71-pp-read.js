const want = {"378f76e67bf6ec6f380886ef4bb754bf78c5e14ee6ed35826e7636edf5424a75": "t71pp_oiaa", "bfb31481b1866462f395a479c2993169c8979e6606518b27ccd4caef4699e9cb": "t71pp_oibb", "d601ca7e4f6201ddafa42a2432ff0911881aff406ed651aadaa81c8113325e82": "t71pp_oi2a", "031116d5440839ffb7c9bc99a13af2a7c7ea0019d451d11c746bc14af61bd1d8": "t71pp_secoiaa", "1c2a9258e7698e191009493bb6009a0fb1b921bd6277f601fe81bc6dd1434012": "t71pp_secoibb", "c079c12f15e08c3f11a735bef9f1db51b3cb411fe039ed7b3b46473cdae5890b": "t71pp_secoiaa2", "cb69c7b35afcf3f78d3dbb9a6b2b7333e3815c7111d88d18b2f1f614a0c779be": "t71pp_secoibb2"};
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
