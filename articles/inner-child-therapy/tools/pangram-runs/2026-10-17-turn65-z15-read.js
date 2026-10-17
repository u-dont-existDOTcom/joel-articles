const want = {"42aa6196995b778fea5fd82349f2567713b1cf8ce2a39010c37081d3757fcf0b": "t65z15_st1p1w5p1", "e31629d6229bf88cf049f55257c14c8b5b944ad80894073b8fafb345287fc15c": "t65z15_st1p1w6p1", "2fad53072ee01c28b15afc4f30208e0f9b5d4a91faa180747eafff25d00fab3b": "t65z15_fg1p3w5p1", "7644b38a2d2ed5a4f700d0d344c4eb024ba8c12e72f4d5231a17e0af6c97076b": "t65z15_le1p2bw1p1", "3402654c24b51aa5822589312d73b33a14754fc301b19150754b495fa954b316": "t65z15_le1p2bw2p1", "f3a8c99cb6914293f99fe7a6b48657b0e4b8c5c8efec1edf9176030d1af3a5ae": "t65z15_st1p5bw1p1", "274f771f85f50449343117f58a46a0ce6e17303935b6fad6ec65cc8e66ecc8db": "t65z15_st1p5bw2p1", "24d913a5b473c29fb5a3387c928d1396e53218a6599106780e0c91c07dc429f9": "t65z15_fg1p4bw2p1", "f293fa727fdc817ee7127e069a4ce9d14315fb431e3311ce2ee13497a005aa71": "t65z15_st1p2bw1p1", "1d8c308b688bf49a6d454da21bb1ae46e6ddf2630222ab44ca1bd437010e3286": "t65z15_st1p6bw2p1", "ba4bcbce1358ce91cdfa7247f8b5fa2dddb7bc8815ab06b8281756bcc04d2d4d": "t65z15_le1p3bw1p1", "000a13fc567d0f88594c243c10861cc79b38e915775cb901dc4ae3a8d1802651": "t65z15_le1p3bw2p1", "e53788bd98d3181eead8c9ac77d99f83306ef98ff107a8b15cbcb89a0c6c82c5": "t65z15_lm4p4bw1p1", "548ba8648f37a7ca77bd7cccb01761d5b9ee557f058812d508a766fece156b23": "t65z15_fg1p1bw2p1", "7389465a61ace2e26a26b19ff99f0d20596648547655ae226d8723bdb5a00b74": "t65z15_fg1p1bw1p1", "fb0a8924bbc4d8540f299098aa40de325924686f99ad2378fb62c0946161a443": "t65z15_st1p6bw1p1", "208a0dd773597ef1a7038fdfe68a306e6011e5f933ff24474af885e1f40099bc": "t65z15_fg1p4bw1p1", "05d5465a662193dd0b330918977da4addf1c730484e7dfd71e73851805778f81": "t65z15_fg1p3bw1p1", "f0032bc2dbb58cb1219e4716f8230e3445d130bd573ceeaa7773f73f4f130c62": "t65z15_st1p2bw2p1", "b9f24c47725cc3af78e8d82a976bde7baad5c7226a72a2f0869121f17164fc43": "t65z15_secst34a", "9ad25bda94d6a99e10ba80778dba7e3608e603263ae55be0ba670d7bbb9abb35": "t65z15_secst34b"};
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
