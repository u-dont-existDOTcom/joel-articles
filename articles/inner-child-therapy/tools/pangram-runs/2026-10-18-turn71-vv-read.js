const want = {"685dcf567b0e3ae7ce47aea004d5d8c573f32b06a1ccd5d114389e622f54dedc": "t71vv_ifs1s", "3129b1c1e958e68f9959280d8d1325609dd27c17356fd058bdec7e4c757ae066": "t71vv_ifs2t", "b85e3b246b2a282d8e2961d0e0cc7bbc52feb191ed3589c577fdd3ae658395e1": "t71vv_ifs3t", "b008382f602edf0230bfc91d5f03c2d3607811e1e1bca475f4448e12c43f6d11": "t71vv_ap56b", "5f0413223fece57e257e1cdc7217f32c5ee2127c098c545d6f1169d0ff05dce3": "t71vv_ifs5s", "e308db6947b00e92343c1cfa52ce2b165d311fddf74ab63d9ab2d193ab852cbc": "t71vv_ap9e", "7144361866a16344d07ad6cf182425a1db545da6fb728f17623397236406ffbf": "t71vv_secifss", "713d801942d225c0e6c6e00b2ee429179a28fcc0a86291f7a31d184e23eac64d": "t71vv_ifs12s", "ebe75e75d613f4344d92ed182a0a005cc8698cd03151fe5d24abf29b58d71359": "t71vv_ifs34s", "bd1fe91073fe419207d5592bafa2a5a4aa9558ad8fbc700d5e213db09eaea0d8": "t71vv_ifs56s"};
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
