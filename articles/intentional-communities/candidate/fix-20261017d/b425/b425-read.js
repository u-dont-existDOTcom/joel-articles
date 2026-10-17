const want = {"e27a2d8e4c9806104f0dd74493cafc192445843ee8f7e720d055107147d0f2bb": "S2v35-P1+next", "01158374af2602d95c15c2053533a459f1c0135c44545e00bcf94b082a50fd93": "S2v35-P2", "c5466f39bce0263d28d10b1b0fbd7613c3bdd6b231fc4daf17d6a065c67fa01e": "S2v35-P2+next", "77fac3e249990b87d5046d560442a5eaf095b332d9d53c8bdccd20aefca1048e": "S2v35", "e75b269de24d6246da6acd8e233913180643cf3c4937b8c5f0485c8153cd2f1e": "S2v35b", "1a5478c166e0896b2b92bdd907b8da8f3c468d2cd8d40a0f3159a26b0e7b56c3": "S2v35c"};
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
