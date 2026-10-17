const want = {"ea120a0d4149b02df6b0561693a1baefd9750ed9153532441671e66dbc4b8ff4": "t65z3_sp8p1w8p1", "bb51157906f0642ead561959576798918c7a0457a774579e2c382bd942829528": "t65z3_sp8p1w9p1", "43c7e7b41db8084366aafa5041b06ee770a3284cf7c1d4109a4273eee5801a62": "t65z3_lm4p4w1p1", "873c1311a0964362a895f239ecba3765f6edeee0358cf9e65b0af6152ad691eb": "t65z3_sp6p1w1p1", "7212d1ba4154a4ea816318cb92ed6fea72594d96fc0ff74b57a6e63504854597": "t65z3_ks2w7p1", "cf524222a825e0aa4ff33fce3f7a3a72d3f3dfaa9c9e34aabe2b3e89e2866b72": "t65z3_ks2w8p1", "3760e8b52dffcf41020b8ded3c503e4ba189ea915e374ae37981bfe9d6274532": "t65z3_ks2w9p1", "5efef83c9b34f1f06859273274222e3f70ad3ac671554ab432d01d62b7cc75e0": "t65z3_ks4bw8p1", "c11f64b64cb42da88c3fa4e7288a09cd956101a804aacb188c76a60b90b2b00b": "t65z3_ks4bw9p1", "0d9517e0652c8ace9125d146801eb3493d1d7c5a5fd8308bde4d6ea49bbd1ae6": "t65z3_lm1p2w1p1", "709ea443d59f3bca50860d882ab7748edf05b2d9a3905cced8dcf94cbd98d591": "t65z3_secsp6mix1", "3dc7f2d24d795f2232d8c28738c895e78ca003d30ff8ab05a6b2a8daf4139b09": "t65z3_secsp6mix2", "b948251d716e3afd0b574ae1108c5de7883b334c7d2a1f73fca2443a65ded115": "t65z3_seclm4m1", "ed70b6b4463588dc59f82720eb9613bf93adc49a503d65017b8865bab3e4e300": "t65z3_secsp8m8", "6adec6c8d1d945ad2b1a99de4c64278ffb161fd3104f34bf22ad759df46a38d5": "t65z3_secsp8m9", "fd0f314f214fb6448a3eecd64c1a1c95859fa299ec44dce0f67d9de57eb32b17": "t65z3_secsp8m3", "cacb3e5ebdf83eb571b5200c04860eccb2e02af8fa10068ee19440ef0ea03064": "t65z3_seclm1m1", "d43dc7cebf36f56d5ddf4effdf0fde4e0296d45244604f362cc261cd0811f32b": "t65z3_seclm1m1b", "abb07d300439f5a8bf9e0eac3f01b5371db9fe8a06653e485cfd66ca21f423d0": "t65z3_seclm1gap", "2aa3ddd3dbf9b3cfe46c413bb6fd01471c058a47f4dd695949269d77a80ce8de": "t65z3_secksgap"};
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
