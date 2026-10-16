const want = {"4e4a8074237d6d26436cc274ebbdfe636b431c931f3e5c37d13890d9defdad2f": "S14v2-1P12", "5819348b479f1d5740c637ee03d19ff957bb35443925aaba921ab45a4023d516": "S14v2-P2", "182daeaa4026176f652af0a90914107fff3a6a8e5b3309ba2a3034f012272cc7": "S14v2-P34", "003e2714f7f320c2fec8e10b43df97d71bd8e8b0d096c1c8bd725a29fc6b1db4": "S14v2-P5", "db2cc1a39bab12abe2bbf5cb7ff01f797855d850c113aec803e4ee1833651e17": "S14v2-P67", "5229d803c6fb5307db05738d78e915b5f299ba8c53c668b5b52f1f17c197e66a": "S14v2"};
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
