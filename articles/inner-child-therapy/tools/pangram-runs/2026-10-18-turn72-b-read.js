const want = {"fa3ca73426af5b62d62331f95c59e564fba31e7b105e529a4c4bf546211fce26": "t72b_bgout", "33221a272e24b669975cb1d561b824da2e6bd7ad8be44ea323fbf1fac9e31c97": "t72b_yb5", "24e8b16c44110d86207d30242f62e882696cac2a8871a09aa35ce8db7a28aa2c": "t72b_yb6", "98b06b82fb51b4a1628d258028d3bcc15d3d990fc51bc69e68d96aa6e93148ff": "t72b_st", "b1f576c8070eb899dbe5b145e8fbb0c1f267b83d78c53df08fdb02ba2ce090a0": "t72b_stb", "eb35370f6a7db2a579fb701f68204ea3711039a0c28da23d2590b3df7fea5554": "t72b_ifs6", "ae43781959157232381fd6a75e329000e0462cae97db6d5618d680ff9dfd4e03": "t72b_jl1", "b2c784ea1cb8590e6be1511ffb36ddc04bda0c9def4c51952300a6e2473f49f9": "t72b_jl2", "010bbefc68b186d610378588b108788b7d2f9b530cb315c93fcde5f1a3c16d71": "t72b_som", "5ce833c55d72174805408a07cf599431083c535bd679911033ff392fc209080c": "t72b_cs5", "e4b0f322850935cc8e1c76d07d04e2bb5b2a30a2f58db7246cda25d23f160d61": "t72b_tf11", "e36efb5aafb659058ec1426b33ffe9e39b75a03fa6019748b93a8771102197f1": "t72b_h1bg", "9e486902e1e2e1e96ba66ff60edc6266225c7dda60206bc75aa335db97c868a4": "t72b_h1bgm", "5727062f500147d3c0f549ef95cef4185d120f828e2ed7f400dd2636410d65d9": "t72b_h1app", "3c9be5dc9315805e16d548fe91fea9645950c8ce93f2103c794ad52417c765c2": "t72b_h1wavf", "07dd9d1d5d6668c9da387f0cb32b76e253a1e15db9ebad782f9ac0135428eaec": "t72b_h1sp", "bc244e93d722d2e659ce888e07109cc6b5a8f1a14967e06c75f6d69032db6491": "t72b_h1lsm"};
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
