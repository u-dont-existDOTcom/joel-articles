const want = {"002cc467ea4f4fc225eeec9faa953ef33da9f814558285823a4dcbcadfd4d2ac": "t71rr_oi2d", "446218ef3aa807a570b4adfffb8fcddd87ab489a7ccaf511ecf4e1f03f7c7b95": "t71rr_oi2e", "137558b21143b5fb51d6c5be356821ad3af4771a63157e4d024db2f23862ae9b": "t71rr_oi2f", "1255cd0e4d2ddf750ae374734317838df05996c257cb9c5be7279efc7413e084": "t71rr_oi2g", "9466b66641bffd7a42c33a22ae6a24958686374162cb6140ef31f25536a73746": "t71rr_secoiddd", "9eb2b4bb76f22dfb70fb1db9f6c79387b39ee28efa041b4b1e7db145a8787ca9": "t71rr_secoidde", "dcbafb620652a1eaefaeb493ee31d80114542267b6625d4c94c258917131f05b": "t71rr_secoiddf", "97418bc34ce2936c493b03b2e57eec0a0bebacda48667705be23f89676ab26f9": "t71rr_secoiddg"};
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
