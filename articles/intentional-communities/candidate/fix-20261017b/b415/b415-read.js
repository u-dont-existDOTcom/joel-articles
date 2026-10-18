const want = {"ac6ce306ce5747be544df17b578f43bebae9099f87d14bee81533b465bbc7cac": "S12v15-P2cap", "d198a2eb027f183914c0a042133b22a36fd695694f0e8c8d1cedd44b1a9d0154": "S12v15", "9ed4e820c93c13483c482e56eef2f7683d758532aca35494a9af20291c616f31": "S2v33-P2", "81563b4aa62fcac6c9db6ae6844739278eec77b46039e3ded5b9df5d916bbf81": "S2v33-P2+next", "7f4da3f6cd551724030cc002695c9b9c5551e397ee0617e68a50bc8ab0e5f594": "S9v17-evid", "5b438fa680b208d763ebe0629a40353b1fcdf71aff99ebc31ca00ad998fd8ca3": "S15v14-H2P3", "e2a24fd815edd95b8f965a8b182024a6e12542c7acdd51aaa7325d1243665857": "S15v14-H2P3+next", "84eb40e5e7db9ca4b2203b6b4bf2da8fa1d649ef95fd5dfc2425c8a223c87f43": "S15v14-H3P1", "2f9dc432e7de681a7d76a1283c8ca30773e027ef6fe5d92e08f0440f203761a2": "S16v29-H2P4+prev", "b19e1c0b9aab25fdc5fd72c1a471dad563c721e165243aec3a4d72e670a559a3": "S16v29-H2P4+next", "cb6b341e95dc5d6ed664debda8d39f751fcaf2941677d0b9e376bdfd771d8853": "S15v14-H2P1+next", "1d385ec4d5f45873918bd58e203451c47210512c16ec7114cb94ca8a3adff7e3": "S15v14-H1P2+prev", "233cb11ee237182ce282519b3b5c39d76f3f69724886da797ea26eee68a6d7e3": "S15v14-H1P2+next", "93505431c3cd7f0fe342c0483e30dde3f1b3cacce75237dd5daa9b9f4cad12f1": "S15v14-H1P5", "542b0d3f0b358c826f6df5dbae604aa5e058f0afb847909a23d4a90ca686757b": "S15v14-H2P6+prev", "dcb2671d00ba129b268f28f9e8458318580088f2b355d40304a4e481e400c74e": "S15v14-H2P6+next", "4cd6cf1e30f2ac633214185b2bae111d3f933f04e3030e8de47f6fbde0920956": "S15v14-H3P4", "a01a65f57dcb390cd5e1f8f3f9073b5d921424eaa1f3f3cc4a1a318c13da6080": "S15v14-H3P8", "6c3749fad576ba7cbab61ac19505b389cfc25d43b0d4fffdfe0cd83a6421a6cf": "S16v29-H1P2+prev", "8f06db4a87e3489197882f4c0f3e7db159b581552772c65df9a4e8abb5fe3fd5": "S16v29-H1P2+next", "fcad187004958c5348fc0e7e31e4e98e6df031e752857123862887d83893d5ba": "S16v29-H1P3", "d7b4555358456c716cc89e8b69c68300a336344075602db1bdd4a58e45be48f3": "S16v29-H2P3+prev", "11fa1a106f2cd4ec7e686f7dbcdd9bb907d6d151b13c7515c1f6ac3c11d3141a": "S16v29-H2P5", "1e96383568bbcbd1bd6bb2803ea087b1a8d6464d2cb9c58e379bd1dbee78e084": "S16v29-H2P5+next", "082ffaa649e87f4c11f1f4efca34b64151168a868a64806c25ca551ac4acdadf": "S16v29-H3P1+next", "dbf0e36c204a38d6a5f2bfb45e0412d1af91b35daa069229447c20d7ec0742d1": "S2v33", "5af2c65ce9b8dd67b31b3eb7c6d84b3046bef05d33fd623263a00fb539320871": "S9v17", "b77dcc6d0dd7b8499510e44709b2587965fe803060fc0d3927e404e2e51ebf9a": "S15v14", "6a60177a283196c625d5d04e188b7e104b971a3d415e6d3776803c047794f98c": "S16v29", "1665f42b591ab91ecfb2b8e3dd93a7ea7ed7d10e53b80e5c71b8484ddac9b277": "A46", "85c085d0d9a3a521df06ca3169204b8b8646e0d95ff08d41fbc11c7b5f9171c3": "A46+next", "d11e00747b9d41009312da6448087911475b65fc507a8bfe83ef0f3145bf6687": "S2-A46"};
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
