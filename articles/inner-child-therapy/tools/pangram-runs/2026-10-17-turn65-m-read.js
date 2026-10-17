const want = {"322452af39a868f844496be0aa77d241d61d40734c2256d525c52a0e40b21bd6": "t65m_sp2a", "fb502738beb52314f2a571f75a503e7d5f02a514fc1b146fab603801cf42b639": "t65m_sp2c", "64082688d455e738fe32d8839731bdd4d6b46fdc121f13286819c64330b404a9": "t65m_sp2d", "2c30f9a70b2e938c74930a4e84fd66fcf2427b89be43a185bde97bb1647467b4": "t65m_sp2e", "7723048077edf07efb7beaf6f1f5807b5cb684f484cb6fa7aec61a13d4f27fc9": "t65m_secsp2a", "d28884c14023db8964dde4d0d4d58dfc18bc3b87b1d48ab95381678b283b53fe": "t65m_secsp2c", "503098fa0cb21e2806631fa8fb37e0924313149491245683b086f6b21859f49e": "t65m_secsp2d", "a90e18e250463ec08c0ef54079cc94894d579c5a1aac2a60f5735949b9bed90e": "t65m_secsp2e", "158366d544eee23b42f03a28550f7864881617e1ac8b4d21104910e5df94d6ed": "t65m_sec2sp2a", "1458cde9e271784811ebc87176b3a492f39b00504891d46195559aabc42c5b2b": "t65m_sec2sp2c", "cc1dd728c59ac1431931b608d8c14fa6b62ad42540815e54bf62f81e8da6e0bb": "t65m_sec2sp2d", "605f99a12d7d4e96207c97306e2743995aee8bd2f0c317fb54b323eb86e86da3": "t65m_sec2sp2e"};
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
