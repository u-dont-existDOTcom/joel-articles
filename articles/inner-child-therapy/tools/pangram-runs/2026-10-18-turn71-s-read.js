const want = {"a7db1d86a7ff57d08f8b44809f9f5b56fb7416193088730b278ef31c8cd0833e": "t71s_cs1d", "340d022a443969dfa6527b00fadad978c932a6cdd081cd3d67a961a096e91f06": "t71s_ap14b", "489a8bdaeaead517d070dbb0c6c6e5acac545347e873ab32a6235f5e6d7769bd": "t71s_as4l", "d16f3b2be626a1ddd0b7eb6abb7b1cc03ca24b4e64bf9c01705782782b56c0d5": "t71s_as5l", "a54e5eff7888202509ad83607aa91f3dbe9073700cf692e92308b45de27a15f1": "t71s_jlone", "1837c0d78da50f292ecfa8011690540b962b8c8e55a523d014214c06d6692afc": "t71s_oione", "04fcd4bde28dc1d3ba1932f02dbd7279f4088a4a7c8b50c7aeaf89e78b749c22": "t71s_seccsd", "33a250e15ba9bd5af19dc7c15400afcc875956f34c18b2651cbe7adb0eb6dca4": "t71s_secteab", "7eea184d1622d3617085d2fd9b780cedc295088387497c6f145a31b759b6a411": "t71s_astril", "b719ff67f6f8ae3a08d3d9672a98ee441309a8d2c68a55da11ea8ac3e00fbcf4": "t71s_secas3k", "d8782d63d660f623d427d6f470979b51b93e14f8a9f80437b86cb309183bbdc7": "t71s_secasl", "4c394d359fd01ecc2f1c1d4ae18deac179502382d365e61656625a628c46f219": "t71s_secjlone", "4bec2b83fa097d4396f7b277e26fae174c0c47532a158e379a02c63924db32ea": "t71s_secoione"};
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
