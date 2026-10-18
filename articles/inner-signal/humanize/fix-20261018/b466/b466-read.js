const want = {"0f73a2c9e720f8a83c283ce92e6202d98258b987f1725cf549fa795cbbc0cc5b": "HG18-smp1", "a3ee49f8a0fe18d9ded5a47cf8e5857b95c82d305c2e1882c21518a872ee93e0": "HG18-q1-p2", "1bb1890fcfaae9e15ab62afd82e9ae57cc491dedb06ea778a214ebfbadb3472c": "HG18-q2-p4", "6a845b102e6f72005b6fb5b8467c81becf6cc27c70d027d3ad4a93fc46c18a88": "HG18-smp2", "116609763d833fe5bb5541a1476febbe35650e6df75472d84e999aa64f77743e": "HG18-q3-p2", "7bfd41b486ffab13eeac54b032b4188e51853a2d1406efef3067434924315820": "HG18-smp3", "e90382f7ab990c2820594148f710d6fdcaf76ad83183d4002ad3eb649d4fed45": "HG18-smp4", "bca5df6365c84dc3fb4cf1dbec56ffb79bfa172c8b55e46dd44cbd00296039c8": "HG18-q4-p2"};
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
