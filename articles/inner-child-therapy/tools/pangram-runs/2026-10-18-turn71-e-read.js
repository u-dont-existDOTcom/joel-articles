const want = {"f60a45ebf2696e7445ff41d4428de9fdfc4020e6d36f6201af6bb5d9f602988b": "t71e_as2c", "eff6e34398f2949070b563346a6c5b2417c88f38785fbee4825e756dcd9e1e3c": "t71e_as3d", "07de9c003d96dc4ccdf0ed61a9f0dd31d645a3f3361ad0c7c620866123aa7e75": "t71e_as5c", "9b226b036fd935eb0f3cf80b13a54645bae0f7500a811d9e70165bb4d6feb321": "t71e_ap12c", "855b73ca9ed4b524fa92883fa224c48214bab3a550a3b7aff7ec09cb52301a1b": "t71e_ap34c", "461f07ace00dc21f3a2de4cb31630fc4ca0d039acfb6ade6e865b9cbc7ad3ae4": "t71e_ap7b", "5818a4395ddb35fa467df2091e7953abc5e1e1736fbab65c5a0794e81b561eea": "t71e_ap8c", "d2b012593a0408f0150dfe7f21fc11ba126c3f6f7dccaecd658e2674ca559b6a": "t71e_ap9c", "6ba812d8cbe2ed2f6714e626bcd9ebeeb3bbf949b7f724a25c32a59fa53c7925": "t71e_ap11b", "2996ed3f152708319c1a5e153d2433111b8048124960829a03f71094c3db452a": "t71e_cs1c", "9f411137ce2bbf938f7f9389b821a34bca88bc05cb796f801bc123b9175f39f4": "t71e_jl2d", "c91b8afa1c0c04770277cc3d8b476717c4e28b88a1bbba94472e3ca6a75e5af3": "t71e_oij", "504bb64fe4c818b378289fede4ed7ba50f944331396368781f06d8bfeed434c7": "t71e_oii", "74a0eadc73c28cf202d430ac81df9ed3f043c6c52fc4633402272a4b3513018a": "t71e_jwf", "a1add19208d952e5656ed7544575e4487ccf743a2ae3b18ed1758423ef426a3d": "t71e_secas3", "a6db1d4e760db38c08c6e41416727d7dc2165f2634843d7f02830b7f466126af": "t71e_secifs2", "e2b912bce4210696885673e9ccdc292ae8fb6127fcc28da35138c774c023ed27": "t71e_sectea2", "eb8792c0a1acde6d82fcff876c6f8371aecd1fa4ed7848b3447576b420cc5d22": "t71e_secsc2", "adb08cb08f3d964d41f683d9619e19f7e6309f70d56bc7d9ab5408ab1459ecfc": "t71e_secjl2", "15101419105130f54b744489e6b833004ca426c2d3f9ac8ec2bc0d708fa3664b": "t71e_secoi", "8129140f8c4c91e7b0112093bafdbbc2980d6ba044dd5ff4c99d251b4cbdc80e": "t71e_secjw"};
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
