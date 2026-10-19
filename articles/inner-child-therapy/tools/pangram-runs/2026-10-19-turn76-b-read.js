const want = {"8d9f1374588e2b146e4caffce98e4f54ee217d85d5d5cd540286e56047a44b1b": "t76b_ba3c", "9721fb9f25512a3fc50cc1ca52c5cea82333f656698890a242ea1e11ac62de42": "t76b_ba3d", "87c3a7993b2397f3e73236504d1e4986c85107a0f15312a47b0f8ce790ed32fe": "t76b_ue2b", "894279224e24710a28afaae52faa1db52b6c1b53af12d4ed31c9c05fa8cab35d": "t76b_lomedc", "c3e1f21b6622cb7893bdc976e47d7f98f344a2cd61fa2af4867ae76c2f7f81f8": "t76b_lomedd", "196fcdddd5da1fdae71de1f6738f68cc772caab5526fb0bc1dc513ef617730ec": "t76b_losh1e", "36022566b745745bbf5c100c17a03adc3c5c079f7c997cb3bc55948f1641ad81": "t76b_losh2e", "d807ef01d25062084b75dd36b4f3d92299167ae6f185a54b85f437d3e6c35c5f": "t76b_cs57d", "eb76e1fd24f7279e35276f7dd768370d0b853a78033b60b60556c7b586eaab7e": "t76b_hero6b", "d75f75681ce1e403d7493b15b21308c5f80b47efdc3b706c2a858eb35f972484": "t76b_hero6c", "2a3f6e899f1f4a21c0e3a132699b5e7c8f4ef2f87d2472ca7fcb4f2baa7e4f28": "t76b_h1ba1", "f5c962011ccfb35870298ba66e97fde008a78814afffb38c03fb548831309dc5": "t76b_h1ba2", "407c9799c1c26244e17a924e7c559ff66eff2fd48cd80463792a9332790a2006": "t76b_h1wa1", "f6b59ea8089ff30ad7b81ce5cc3fb6e948976d98c49ade1e36b00ba702c54bfa": "t76b_h1by1", "3bb9097b76b3adfb0f084fd43a09cfb37fde4bc011dc59c37e72178d9449c1df": "t76b_h1by2", "5908d0bbe3e10076f365e6267a0ee0f33b10ae67db204f5557bfe318d0fcf522": "t76b_h1ce1", "3c92d9fa4c72b8e5c98eb7a596f3b5f43e19322fbbf315ec4a52847375c261d3": "t76b_h1bt1", "d41bfc03c3da194567917b445d943c2f7e3780f1f401544524881fac56c87b2e": "t76b_h1bt2"};
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
