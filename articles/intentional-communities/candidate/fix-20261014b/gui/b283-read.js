const want = {"175c25eeaaa7a6dd5c00ed79516ae2242959f48766d7ee1a817e4d4b4d109c17": "J11-P2P3", "568ed595fc2a3797720bcb0524ae50c3bbfd6f057d05e201d340404b5dfbecee": "J11-P3", "ddeca3c0c2a19d7b3c862db3795594a46966a3d9e8d1411959d975b721721552": "J11-P4", "43fbdd19cfb55152de829b3229cd24fd2c4c9dc48dd158f8c01e27f6c1b69aa3": "J11-R15", "baa6bd60bb14870dc4bd78bac35c0165c774d7f00819e0328c5eddc804fd4b3a": "J10-P5", "a6707c8563a0439f12829697d3bac3915dfc24d136c1c4e1b097110e7e0e3247": "J4-P1pair", "cd3ba625e2abb4bd4eb62545de63ebd3e8e190ebd85d7e136978367c91590f65": "J4-P10pair", "921a40f4f4fc29aa55062e5a6e1f135a0be43c1bbdc829c897b0c656bfb3ce71": "J9-P14"};
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
