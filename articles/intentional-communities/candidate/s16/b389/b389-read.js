const want = {"f35fbfee679a6326b0632b2f5a1c798f074b2b771c57b307f561fa599b8c3009": "S16v25-H3-P2+P3", "fd27104612b7fd195aae5bc2b6f6b48bbf6c11c31604a4e33e67727c40572d33": "S16v25-H3-P3+P4", "bfdee0440f8a843519c1001ea3532f92ee0407f4c07fd6020a77065fb770629f": "S16v25-H3-P4+P5", "d919313bd1e93c2e12f9b57d7b1a2851a05bb98da081c464ba3b9d1e940f876e": "S16v25-H3-P5+P6", "b13e5bc13a1896f0c1bd5aa8b5fd186bf65483c5052dd2996671ae03765538fc": "S16v25-H3-P6", "d54c96a3cf8b65f60ccdeb357fd7aa274017687cbfb91c0e6bb60ec0323d10fe": "S16v25-H3-P6+P7", "d18a2203dcdfd586feba2ba537cd501cf3c6f066e0a50c9f991b51615813b2ae": "S16v25-H3-P7+P8", "d67a6652489f5693fb6e226ba56bc6628e83d27d79613bb5bf27648223c041aa": "S16v25-H3-P8", "ad0c8be481bbdd0ad715dd792e466bd4ee9e5c40cd4a9c098711894cd0aa60b8": "S16v25-H3-P8+P9", "f0094c527c959fbd9108ddf37a6e67ff0a13341994634625de77082f83371ade": "S16v25"};
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
