const want = {"ca654caffa411bffb11feb5b21fa76c0921db577f1a24d2ff4d4a60117d23ab2": "t69a_rwb1", "fd8fc90178f6ec12ad35d13cb9fb695ecba87e88dedada8e41ad903a0a9dcbcd": "t69a_rwb2", "229dabbf62204ccee354c5e442c287e525dbf1ae2c01b25c8186db10f9973556": "t69a_rwb3", "aa98a3a09d7b66f0f8d1c881617faab7e14166c5f0df15184d8f1da4b98834d5": "t69a_ks0joel", "0ae8a9d98ac6391cdd127f680076b01a0baf34dfb8ccbd7d6b457cc2eadea447": "t69a_secsp", "f7a69064aef20c73905aa52c5102b5544d4a2475a9abda591a2c2d75f14e86e7": "t69a_secks"};
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
