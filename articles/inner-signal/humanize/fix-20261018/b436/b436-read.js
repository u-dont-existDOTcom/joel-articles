const want = {"d669a1c8a30d36f83b26a1b5f473a887a442b6a37b178f5bb4cff062e0940c56": "HG04-emuG", "a70eeb075210bf0eeab7610cdc9b3b5bd6ca9ca4f5fbde6df3e8486977fcd3bc": "HG16-emuG", "3a00ef7e6a4580beb23c6eb9cf9a6b927541c571eb4e7787abc4130492bcfcb2": "HG29+30-emuG", "cd9deae7e9b8a260870e14dd1761202baf7bcc8313522f6a03997b6ab4a7f87f": "HG17-emuG", "8859ed53f8c7d10c15a2590094db3defc6813a3b1a0fed876f3df5efd58286c5": "HG37-emuG", "d88dcf71b21548eb65482fe9e4a02c41d24895e95f8f0df7f12fd7446aeb0c70": "HG38+39-emuG", "30e70038040276a4e5aafb7242584e823567ddb70842d6125267f1d59919776b": "HG31-emuG"};
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
