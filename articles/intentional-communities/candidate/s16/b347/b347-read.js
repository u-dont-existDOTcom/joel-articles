const want = {"d36ff7700c129f42a4e4fcc6f498b66afca1a2c487df83708ede0bf8036d1c03": "S16v10-cap+H2-P2-P4", "0882748f98ab32cd5abc6e9dab65e22cb2616642a09dc8c22d05f636d0930432": "S16v10-H2-P3-P5", "75b6a6ec9f29db91428165c7140e910398c77c7a4ccc36ad36214e3a19fb76cb": "S16v10-H3-P4-P6", "ee8f3495bd1f1ef5b6e806b57de28254aecbc4451acae1593eeeb304e327b2fc": "S16v10-H3-P5-P7", "0ccaa01d33bc37e4e1920fab1bef5441f1c7140a61c017011bf80fb68bd0220c": "S16v11-cap+H2-P2-P4", "9c9d0db6238bc26ab4327d2c1db7817dc5ed3489739903a864c243efea9b77ab": "S16v11-H2-P3-P5", "ad33ebb089b5b27240bf6fd6f8ae4c5265c0d4c3d6d252ac745c7daf80625977": "S16v11-H3-P5-P7"};
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
