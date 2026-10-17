const want = {"5ec8e840cbb36240d2851a3fa664b285accddef37572a2b924ddfc6516eb52a9": "t70b_secst", "24c255bd64e3e381cdba1ff0c61ca2b49dba2f9c7a8d304d79a8008eb3c2adfc": "t70b_shb", "cb91ff618f73be002c6973f02df5f41d65a4e9e44ae37fa80fb4e10a2dae9ed2": "t70b_she", "b2c2614065c5845ff86d6a865d08006334475f18e24c26c3ea73b5e0d59a6c73": "t70b_secshb", "96749043edc9300bdd252012932a85fa5616a430154f5f42916ce3bbcea5384c": "t70b_fg2c", "9b762f0d3db18a0df0e79a02b20a2a94a5e6208ea05d97257f253a288d64b087": "t70b_fg2e", "cada283e11f1d362d1b4d36ed9a815265f90ad76562da9a9b01c809bb96e80d4": "t70b_secfgc"};
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
