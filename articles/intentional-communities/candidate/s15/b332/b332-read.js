const want = {"7f9893a35a0719f2d11144d5a3c63cdde4513cd06eb0fbbaa9c5cc18b3252483": "S15v10-H1-P4q", "29c59ca614233b97966d7f6573c82271c425947a98a94157956272bd480117cd": "S15v10q-H1", "809d1700d632a0d3e2d364761e9f81f2ed1205231bd706fec3e23ef77eba23b3": "S15v10-H3-P2", "feac674677359581c82a8b0541eb70a4506fd03df87fee65462c7658e16224a1": "S15v10-H3", "61b88095727e398ed29c58012cdebd00933140797cef2b920898a97817d04eb8": "S15v10q", "f763b2a5efeb0d1d8110f037f441bc25f5a596a66c00c4caeee71f5102792b4f": "S15v10-H1-P4u", "be56f911e31fc3b2c49273a92c4e6dfca4a2bfb52302d281573c9a10aa34ac1a": "S15v10u-H1", "4221be408fa112cb4209d6927dada2d9f9f031d5c7f4cd2b0b6d5a632fcfcc1e": "S15v10u", "034dcf6e43bd1e02dd4f8403514b1cfba8c9a206cf4dbb278ba57fb6e5fc1217": "S15v10-H1-P4v", "3f87889e8b259c02b75186292f33faf945e93757618f6326c523160399ee114a": "S15v10v-H1", "d7fb9e62378f21d4ce35cef98e76e9ae278ccbcfcd7efa25b5476f45e7cf6d08": "S15v10v"};
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
