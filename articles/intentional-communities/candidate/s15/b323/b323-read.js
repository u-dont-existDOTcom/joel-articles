const want = {"7d2cdc39d1049efd776727b95db0bbe950610915b2511574af37b108b30577ef": "S15v3-H1-P4", "c60423ce279d1cd8a6faaa3224aac8686ceb44b696f9cf22561c952cf84c1e50": "S15v3-H2-P1+P2", "33cd041cb294d1b645bc5b75e5c0c0ccf05acc6eb0af56b2b4fd7d2e4c139b45": "S15v3-H2-P2", "c8523260e533422bf2a16235701f38aa422f3af7b8b675f9f2e825eb95c79df8": "S15v3-H2-P3", "258f7175236acf32bf4de37a3385d8c1b461949481eea23cdede04143af82f83": "S15v3-H2-P3+P4", "babb392deb0fa8eecad9ed141da4ba54d2bb7c305ee6dacee5fc01e11e235b66": "S15v3-H2-P4+P5", "2feb48c3181e335c6c6f4733339030887e7aa94ee8d4c5e8c7c8e2eea211bee0": "S15v3-H2-P5+P6", "01b9dd9d00a20893afe5b4781103399e530304dca04d4901255cb8d2746cedd7": "S15v3-H2-P6+P7", "1e014577ab7cdefe0c704f3ac3ae728e2ef79932cf43ab75d57c7e3f952f5844": "S15v3-H2-P7", "7edca962ad64d85ccc43057d6b333abbbe9634659f376781cd1ff773e639e4ec": "S15v3-H3-P1", "c461186e2c37a1a836f251d03cde8b93aba4c3976c403693816a0088eaf826ac": "S15v3-H3-P2", "9d660f031b91688e0558c73f90413d873bc97648fcffb02473d63474a4026384": "S15v3-H3-P3", "75e85d8c26312e8a6d9d029c1daa0e1082932cc1d6fad404ef77640d32dc2111": "S15v3-H3-P4", "d77bce5f6ed2c96961432b3404077ab5a8dad17270938ac5ad7fe331ea59c850": "S15v3-H3-P5", "727819edd459dc970283036f95e1329f0cd98e6f795398a5d2e7e87ae5c66c33": "S15v3-H3-P7", "34aba40755f668e58782b6759c29260efbdd10e0fc6202256f325077b6beb813": "S15v3-H1-P4x", "a83666260eac1012a45a14551cbf5fda3a4cbfbeb4571069c39d75541bcbd168": "S15v3-H1", "8a1c8cd4bd02362449f65cb6f36e6fa1d6cc70c1f7b7672d341c0acbe98d3840": "S15v3-H2", "d6b110b8fdf4634f91c31519c0efc0bc0cfc27dca3073776cf5f132305f598b8": "S15v3-H3", "8bde67e56acd49ad3380bdbeac1198d39f3d10d25722a6239f1844ff796c5710": "S15v3x-H1", "fa1dbc7e8ef3daad98b6d0028d5342e8600f7963356ae3f59d6732aa369a27e6": "S15v3"};
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
