const want = {"632ce757b3b13ff7c1276328836f8c57b4d290db8e890d899a9852ab67171524": "t72e_bg2a", "568ac8f3fddf86da7804fcb4371bd11c587939862ad7f9bbdbe6902e52c0a18d": "t72e_bg2b", "20f934e86277b152fdef581aeef77b0a0b4e09d259e294cb64e7e6f894492b79": "t72e_bg2c", "323b6160ea2b5d9226bf5827a6ecf993c992df0e82258bb891c39040ab11542f": "t72e_yb5e", "cf994051952ad541157aa9ef7489829fe148b2e47165e23f2da4636846f4bed3": "t72e_yb5f", "5535cd97cff0bdaf15ac79979b739295894f6be43a5a4fd7fec372fcb3273286": "t72e_yb5g", "4383edf676eac861b7ddd993cd7d8385f92df4e4051e6632653715631b1b76c0": "t72e_yb6g", "11d1a1d33e81ebbbf7193b164682c6349aec440294f3cb2ed7a41b940f4e0f30": "t72e_yb6h", "1fb9408f308419e175772897da1b01ac0b08df0f264fd438891d9c6aac32fb95": "t72e_yb6i", "d6c8b855d132c0fbb06c7b3367e61f98183ae39635bab0c8694be61b76f41dc0": "t72e_alohona", "b48b2b97d5fc3738d180a75347a14826106563bb897b795e32532ffaebf6c047": "t72e_alohonc", "39970d2d425eff2473e1aca12eb5b27a3814cf98d3b64fd3c5ef5535418980bf": "t72e_wi5a", "a6e8237614e5abc2f0346487812af5942d28c1622881f1fd45b6821ef29da274": "t72e_h1bge1", "5fe59cd694ce04079ab8b6dc23c450e6112333437ee484b66b6b1eb4b23dbabf": "t72e_h1bge2", "5ae2c3795c6dda686c478c488052cc70b329bc8cbd82e4839450e7ad41272ed7": "t72e_h1bge3"};
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
