const want = {"4327e6df295044ade01d98ad650fa6fd6704d6d75d06957a48676834eb101a69": "t76a_ba3", "a8eade86027f3f8833744d161c8c409deb87a27a63823fedf99f63451e1a0e4b": "t76a_h1ba", "3def36f4a3b08fe2871ff45808099a0a27b7d0ed8cf6d6782f9d6a0f9d21c78c": "t76a_as4b", "a3fadc9dd2df814fc00c1f4edc01cc26c31334e2e6918592f4c4fb1116efa3eb": "t76a_h1as", "99c57ecc3ff55f3b8506135fd0900ea5c37b2e3801e7053af018e6366e33ab26": "t76a_h1bo", "b3eb240f745d41220924b3b7f160aad49612cfda0bea14366f43ed8705345079": "t76a_ue2", "e61e0c39d05b1418255c9ae62d4c4fe71b43b45c9415c19d9ceca85e1e865f57": "t76a_h1wa", "fed89a237d1c49d89277c235c0fc4ee6e9a6cb68eef7b4a26ef16d61a1e24347": "t76a_lomed", "e2c070bb9c5bd465be8ea5630b0eae678a73547885d7f24c7fec1238c00c8c5a": "t76a_losh1", "dec0431bae912a6ee0cfe62c7e0845c2e6eba83043ea01a74894552ca9fdaa48": "t76a_losh2", "6afa90d9f74d0b9ec8db942ee0ddf79f67a9a8eb245466a7456b83e503b0937b": "t76a_h1by", "70ece6655aeb161f9893d31cf4da3fe2b8fbe64a3b5083db4f6d474a760e29f6": "t76a_cs57", "c93d406ad39db59d797dd5a1629425488094f1fc966c4ee5dba56dc03084a025": "t76a_h1ce", "50b6bb7d673d0957478b6f882e62e7352eb1ddad3f0f300a6d45849f0a6ad974": "t76a_hero6", "58b35095b1f525253b45d10f2b6739beba093c49b00e79bb8078d6765e48ce85": "t76a_h1bt"};
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
