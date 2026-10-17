const want = {"946a163296f6d5c36c4cc47c1039b6bd86c179518ebd3a09bc1fc40a65e92e85": "t65z14_st1p4w2p1", "fdd42d7c627e902111421410226db22dad8702427dd8eeb1c92be8334ba652c5": "t65z14_st1p1w2p1", "323d15e1a5845ed986d1ced9c66a58f52fe5b0f6aaff3b957d1f2ab757256b9b": "t65z14_st1p4w8p1", "c74c0e27f253f07e0d33afbbda68e17f547f213ef6cb9bb961ba8dadb52ecf76": "t65z14_st1p1w1p1", "03095d3c15a224b205312432287476de5818541245384975812b883091bc0f90": "t65z14_ba1p2w7p1", "23934f58e357bfbf909e5cfac1da9a280ccb1a71205ff79e7d95d6938d73552b": "t65z14_ba1p2w6p1", "a661fa5408e7db12779941d44e104e70f74b5c0552cbf06c7a83ebc46583db0e": "t65z14_ba1w2p1", "66792c0d8783ce308ffee37b119bc31b64383c46d198b15191e294c2bc56932d": "t65z14_ba1w2p2", "52bd68c85c1a7ac34840f9aee711b65ce3898980e16d09cceceb28ede1f6e790": "t65z14_le1w2p1", "fbdc2676b153584cbd235ee78c3a522fed0f5679329d3dba733154e92cb00556": "t65z14_le1w2p2", "1690183488450dd8f4952ccfa89d35c51dfc58974cbb6bf16bb1cbc6e560b833": "t65z14_sp6p1w2p1", "b0e3a7d0b2a460d1c9a87ca6768cb8308d4f93b4ac5dc4bf1865fa47368b7e39": "t65z14_lm4p4w3p1", "e515d4139a62afe6a45f0db22861553a0bb28c5227afb455409019f3aebdffff": "t65z14_fg1w2p1", "140ea0483d0afba8184568bb2d052aae7163e265f4d8145af6d3639ea0787b12": "t65z14_fg1w2p3", "d36414ac5c659fb400e394608dc66d49da35348782358660c40748fa95098f65": "t65z14_fg1w2p4", "d9f0e6f38f4f1c30ad139254bc34222f47a82222493b9421999fcadf40909432": "t65z14_fg1p3w1p1", "55391d76d812855db94c40fb0fd487442318b46fa93343f3a45c002ac9be51e7": "t65z14_sp7w3p1", "5699323fac543ea35adf1b8b6d9baa07e30efeeb17f54abc08e9a67e3825575a": "t65z14_secba1w2", "398ab9cd93352cd70e2f834d07e0d39333fe5126e813b3afd94ba2d29f7a35e1": "t65z14_secle1w2", "e3c7ef7363845b8ca1d2a4b27ea37fa7cf64ba706ac97ad44e9a936a8324e8c1": "t65z14_secsp7w3"};
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
