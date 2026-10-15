const want = {"161adef9404631a1bb8e9bef9e1348efff5fcecacf463ca866c574f9d0ecf51b": "S13v10-2P1P2", "d45803cc1e94f4b1347f17badaa842202c63b7273a9480bdb4ed694e202fc09b": "S13v10-2P3", "7fc406a85b5d178635b735e07630adbe61ab2b62d397c6659549088e429b0205": "S13v10-2P3P3b", "5db887b41ea032add643e0c309bc01a38412a2127c51974f3f1463d6c4859946": "S13v10-2P4", "7b49e4bc481076df8411ee7e097e1f4926051a74c13b6034075a990309caa486": "S13v10-2P3bP4", "7df52a7e3ab6f3be187fe23eb372167ebbac16a0fd81b5997543a80f01c8cec6": "S13v10-5P2", "6dc7b835dc8c07c811524869875dc7629a0e5e584dbd30cc39aae35b78ad915a": "S13v10-5P4"};
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
