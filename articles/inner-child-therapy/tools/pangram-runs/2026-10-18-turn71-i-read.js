const want = {"438f14eabd765ec4824caf676b730eb964a588840521c6d03d156ad59193df4b": "t71i_w1as3", "7b2ae6caa876ec291d373d7f767346c16b0f77d65f57415441449fe833897b6b": "t71i_w1as4", "cf4ff9abac3ec887646e54eeaa0bc938006b822c9e86ea52b31602bfb889be98": "t71i_w1as5", "52167da643009056690d8e46326685fbe6ca7a9d2522604b0e171895b079002f": "t71i_x3c3", "23654ac16a5664d0e848e0a81949a5036bcf46c88517f0741ebb2fe04db81145": "t71i_secasw1", "2c8f3bd02ef7ef745aa196dd6ad670e8f50d56a952920f40a7b5cf8f3e61594b": "t71i_secsp5c", "87c3f6884e486a46bd31645399f71ac974e8306e3f748c2b0aa35f0e0bac67eb": "t71i_secsp5d"};
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
