const want = {"bc6b1a084f79eb51d4a18ca733a2a3b7fdfa0d796cbf3062955e829e0a9d05a6": "S16v11aa-H1-P1-P3", "74b7e1d3a7e0a1fdeee3605518be4a11cd2becc86c51e45209c91ea85259b2ba": "S16v11aa-H1-P2-H2-P1", "4f30d2b5cd94e8edd4ee7de9ab7c0c5e66239d4a70496dc9aa170dc3f3f2977e": "S16v11aa-H1-P3-H2-P2", "b74d4ed0584a2199426c6b6513643457f1dfb42e58bccbc47a136cff6fbd5619": "S16v11aa-H2-P1-P3", "0ccaa01d33bc37e4e1920fab1bef5441f1c7140a61c017011bf80fb68bd0220c": "S16v11aa-H2-P2-P4", "9c9d0db6238bc26ab4327d2c1db7817dc5ed3489739903a864c243efea9b77ab": "S16v11aa-H2-P3-P5", "0a2fb0de6efa5c0743d439c7e6be4a2df6fe0050d9f898e81fd7e6db5185c6fb": "S16v11aa-H2-P4-P6", "c18be7c4cc0d9f7cb59c919d5d54ce1d00c9c2b8551346ea67b1f657a9c8595f": "S16v11aa-H2-P5-H3-P2", "46c097474ff74c8ae214e3b410252d0bf4fadbb3ab61df53fce59352c7cbe1ac": "S16v11aa-H2-P6-H3-P3", "8f0a15c5842777df531beb188cb76e1793f0512c10f3202e246210b51478f884": "S16v11aa-H3-P2-P4", "67b4c3d8acfc0e935174e85171ed6806de7fda15c61b0749684a2d6a4a532ae5": "S16v11aa-H3-P3-P5", "3b694c9c53d53802feeb9ed743183d8544c3ea6f3c1b1b8d896300bfcc1277db": "S16v11aa-H3-P4-P6", "ad33ebb089b5b27240bf6fd6f8ae4c5265c0d4c3d6d252ac745c7daf80625977": "S16v11aa-H3-P5-P7", "1614fd8053b39ec4b1b103e271404032dacc37753039a24dd4e29ef69387a54f": "S16v11aa-H3-P6-P8", "b361b3f0c9afd1b17616c09d7508e80b405d07c6447e1572a0179c249c8935d5": "S16v11aa-H3-P7-P9", "079d4dcd6fdda96759f323e4001417e859ca906f6b1bda718d2bc8881f6f2aaa": "S16v11aa-H3-P8-P10", "e2195ad765bdd0f999de2c5f32e91168c3b30b1bacd9032fd173d24467cc46b6": "S16v11aa-H3-P9-P11"};
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
