const want = {"0677a9340d49b7038572501a5bbeaa5fbe349c538c318f60296d72019f6ae54f": "t65z4_lm4w3p1", "1b9fdb8a06a853f0276f046913ebc4b116a9d3ce1511a6e3a1a2eb979080afba": "t65z4_lm4w3p2", "42dd945d6c584bd7a7b88be1d509768bbea81e6087103457b428db3fe013c3c3": "t65z4_lm1p2w3p1", "d68c262542b8d735b2a3cd40e06d1c0a55c95d9d50b7fc11028405fe0d5b1111": "t65z4_ks2w6p1", "12929d70ad857aecc0c367765c064b702ab71affe7323d2c73a7ea1d7632bfa4": "t65z4_ks2w5p1", "0378b292b6d33e9c2f5e8a11da999d5eea28dc6b23bbcc4f3d93e3084529c9ef": "t65z4_seclm4m3", "16139587e03a6e5e2babef317e5ecd24c5f6a04390cdfb871585d73613714cff": "t65z4_seclm1m3", "088b5839784fe6c70b1782827c61a96e370baae8b9d257d3142b9198cff4632f": "t65z4_seclmh1", "ba20d70e1545ae3c6aa05f19818e7d3d0cfcaf997fed163d9b1bf151884161b0": "t65z4_secksp4b"};
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
