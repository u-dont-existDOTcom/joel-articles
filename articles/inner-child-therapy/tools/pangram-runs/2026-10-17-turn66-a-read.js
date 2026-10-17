const want = {"5ee7ec59ee563156e4f43c35839ca262c182c6cf93f1b4f1af93e11f1f509378": "t66a_fg1p3w10p1", "19f1534ca6d143dd794fdecbaf6b2c3acfcc8e42c03fcf2d98c7e036c9302fdd": "t66a_fg1p3w11p1", "db22528f53fac3ec069775c53b2cc6dfbca0d1f9a0623c64fb38247ad2912857": "t66a_fg1p3w12p1", "c1374798bc49a52bc3ddde725d69de3c3bd1abc2edf093f2052abbd980150230": "t66a_fg1p1w10p1", "f1b27247c139a1d3a24a94f48d49d835d6fd1c1ec36d01664981bccf880292fc": "t66a_fg1p1w11p1", "57ede33821ac53fb11f190b092424aaca25008675351b9be2c30b306a1745125": "t66a_fg1p1w12p1", "045059da98614f0303615d997dc4e4ea6894ee3295894d1873dd110fa21fec3f": "t66a_fg1p1w13p1", "d34b7cc8e8ff852b6159f7ac2162dd6de11fc7d1f929ea2fab17083c91320b84": "t66a_secfgh1p1w10", "cf63b1060f420829f706e652acc5a5f5c60012a14afc84455edb12a7de046e6b": "t66a_secfgh1p1w11", "51d97779de33b256629ec36e38cd5497500035291b039d0f735efeb6829b5ae6": "t66a_secfgh1p1w12", "8e7f8b0192fa2a5dd7260d0c5ebe4d2363d35acf8fe584870903a07ee723c736": "t66a_secfgh1p1w13", "3c0425e9d16785d988b3ba523af13c19a6aeb975c7db3a0bf240c0dc463a57ef": "t66a_secfgp2p3w10", "1db7fc695c7b57b57ba6a4c9ef5e9240e905c2f360d86195eccc469263106675": "t66a_secfgp2p3w11", "c731b01d646fe04b6880db662259771ea0c3d3298ea39e332a7563d0b92424d5": "t66a_secfgp2p3w12"};
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
