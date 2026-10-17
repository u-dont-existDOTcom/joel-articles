const want = {"4c19520389c101e41ca6604afd3ed028a700be57d25bc8991c71a890c8c52fde": "t65z6_sh1w8p1", "e72754ed075545d3b2c19aaa33a5323a78b7a11105f12bc6e1c22f5fc1c562c6": "t65z6_ba1w9p1", "e6b473fb91ea540100643a9c0fb416b2ad523192e600bb2aa7fdf737a4e830cd": "t65z6_ba1w9p2", "b69127c53e336c7826249350c457177be570be93bfa02f8404a66ec953d1c90c": "t65z6_secba1w9", "cb2533fa9a1234b1ca70c5ba69dc170c4c1bc95ca41a5ccb1ffd286b6e35ce5d": "t65z6_secsh1w8", "368315e7103e62bc6f9c0e9841dc7f78248afd4e90347721cb8e263b2e1faba0": "t65z6_secsomh2v8"};
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
