const want = {"e7eff54f7f096d532f04965541983191d998339ff9b25cb77ce269e75520db3d": "t71d_as2b", "5ecdbcf68f19ccbe212c45d19cc284022e08c40c47aa9e169178f27bb48f93dc": "t71d_as3c", "2e384cc492b1b7588ea75467f520c594277ec4473a0db26792b342671e1a290a": "t71d_as5b", "ed773cb3aea917a2de68159bfc7db9bcbf9b50e2fc667d963b591d99aeb1dd03": "t71d_ap12a", "02a24a0e8d981f7726bb1bf25f4f6ca2db67cf68a8865153e01c40d671541a36": "t71d_ap34a", "5039aeda80223fa37393185aaada6c1afbd726d2cb608f6d9e967a281fc4babc": "t71d_ap56a", "941a6e9bbab3bf876b059cefe7eca859f0e93c5364d84166970f54b55c2968a3": "t71d_ap7a", "038315fa5d9210226f5f54b0dd79dcb56376f7ebb15c6501a1bde41fc99271af": "t71d_ap8b", "2059781151914f4df8b55e44848f2f364b735ec0c17a8d499120936004391563": "t71d_ap9a", "056c585ebe09bdc74320ede2e4c495a202b8d4cb74e07afd2816a4042ecc9f7f": "t71d_ap10a", "1aac5b8eb3d397182287b165c0f9888e405a2134550c484cfec29ee2124fb3a8": "t71d_ap11a", "d3f20751cccbc914cdb1eb1fdb59c08d20e0275d689138c051354cbcc2250119": "t71d_secas2", "78a16bcd3546d1171b20845c0bfc961dc08dd163c91078f091edf9a8ae36d07f": "t71d_secifs", "3f3046dfee374ba1837c3c2b62dc6ea9101ff405055ce0554725743764aa3911": "t71d_secrcw", "c66bbba95dce65fedd56d3eb20cd0a7290387e1bfe1354ffc4c38a3c34c9229e": "t71d_sectea", "880951791d18838d80c8caf8abbb5e0fb23c61d2000f01d705ab125fff9d5d46": "t71d_secapp"};
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
