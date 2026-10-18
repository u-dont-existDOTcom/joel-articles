const want = {"ae1e88a46783776e25b1fdc3444d3adfb74c93c833af2c57b8a6d555dec5f081": "HG01-emuA", "72334fc772ed9edd7070382c119421be95b28048a1fcc43fae785f4416b93d26": "HG02+03-emuA", "a3ec2ece064d3e4b849e39b2e9630f0ab052abd6a905768a0d6ce3395d1b0ea1": "HG04-emuA", "e79735e6f1099a56193d32346772c6a1a408819c1e102dccc20ca45b1a3ac41f": "HG12-emuA", "d9096fde09041400057e37a06cd7573836b2ba465ba7c54e28b00a07e2e16d74": "HG15-emuA", "82cd185dd48ca5256601982dd818a6c3f87fadf6864c7c93147ef17d140f6793": "HG16-emuA", "438ff24ae4847173d175b0720f1f47a86217e9ab87a2e969b7d248e7ee794120": "HG18-emuA", "7394ccbe547a5fbb3197ba1cdba739300bc56b91d31248534891d9d8c1dbc443": "HG19-emuA", "01744ef1a094b5994176e0cbfaf146a0fe3f7cb5fe7a5d2f1dce8cb0e2b28894": "HG21-emuA", "88d7e909ef534796c74d73130e2b5d7de9d001013b50a122c2c98a4902fb7608": "HG23-emuA", "5a36267dcc18c13a6fc2d3732fd9fbcb31359d854710e2392706343f4cb3129b": "HG25-emuA", "807ba137e108c44f14c4c3025013cb87d8e2e6aed176d18edd682086651f4469": "HG26-emuA", "82598d00ffbd65ef510b8081d80ad680f23e115e05a94a277f8278fd81b9c426": "HG28-emuA", "db3ea4e4ab398d6fadc2a1504830b3b897e2dae78cd7d2ee9e8e79219587ee4d": "HG29+30-emuA", "33de580a8b3bfbc37353eaa1e77db1e31efb13c53fcea4ad68cac089a72ccfae": "HG34-emuA", "77ff190e013b4078432795378d242065f1e7edfac39b4cf901338be7d86fbc3e": "HG36-emuA"};
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
