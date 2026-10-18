const want = {"2eb0b5093be933f5e30e4b29bb3c4c4a0ff8d85d35d18e078c7bef3a4d523005": "HG18-wa", "e6a441695f2ea38579345731fcd0c6bdc42fb840bedb89ce1765e77225ddb874": "HG18-wa-p1", "e0266c3141320e8ff9b0b59b7582524d6eda3c7c9da6740ead8c3f4d596efc24": "HG18-wa-p2", "ffbacafa2769576b9180d381fd8310bf3f91b3488c03abeb95e094d3c3e23165": "HG18-wa-p3", "96af5729eed4b1c6fadfc77adc80fd63a23df4b4d89695b3377743239266a847": "HG18-wa-p4", "c8d9cb660d392f706b67aa018e07b2d3cf64b60850f6c28aaf33083b7e180d2c": "HG18-wa-p5", "a0f8fe6fae12d20b9244ac654b11198925bf988d722c93cfccfa51062ca0af02": "HG18-wa-p6", "1980a3a85c27de4122d39ac0f02ab731e5eb356821c55967f294239eea8dd352": "HG18-wb", "3d0dffd604461d75687a0471d0aeb7e062340d018dd3617f4d9d7cb2617ca86c": "HG18-wb-p1", "9e964baee32ebf82ad5b96d8927eedc69f7b9379d69e8e144d6486f0dcac1bee": "HG18-wb-p2", "a5b1e551adaaa1ab1348069b5d62f34ca8363b2015061f902b6918eccb5951c7": "HG18-wb-p3", "d135c475418c61773a13853a22eb9275c1fea5f2b07b0d7193ca6585344c32f8": "HG18-wb-p4", "35744145f87e4174c9e1324010983c4fffa94d090450521c9a26b89c0ae93052": "HG18-wb-p5+next", "3218ad46e2fa01a2bbd9db49a99d7eed24c81d63a4a671891e3bf1ea8cbdb0a5": "HG18-wb-p6", "141f9494f78c9b9220e8d9313344288a42ba844392bc3558010b18dc3f91bfe9": "HG18-wc", "ba1ca0575c6a92ccc3606f2fe0efd2467179fe157e5562b17f944349565a32bb": "HG18-wc-p1", "9f295eb00b4cadb0cd8d56e6884b7a0bb1c5f84dd689b0156ebe98c8c54c29e6": "HG18-wc-p2", "a8602e6bf4caeddca3c92777ca17594d64d05de16370c506cbd215a6dc5a2697": "HG18-wc-p3", "69a2e0b8bb8a12d4e55b0077248eae497b9f416a32c0d325a7837dcbfb0bd966": "HG18-wc-p4", "3e9ccc5e37cd6bc17825f6dbdcdd9ff414f139891c078db3414d61b902b31172": "HG18-wc-p5", "aea887366b1cd50d8c716f68649d6d198ae9711d8906a3dd50c86aa8f62eeac8": "HG18-wc-p6"};
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
