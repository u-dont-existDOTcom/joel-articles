const want = {"8193caa8625699555ec65b597d196d45508234c9820d5fbf1d4e5071161949a9": "t63d_p910k", "2cf9648656e1111a575ecdc3712f5acb3925a39043999d4ef631e358134f4a61": "t63d_p910l", "9bd91f16e82239c8e23407da8744b2b9bdfd25f8855f0f7e3dd8169d05d0c65c": "t63d_p910o", "606df32ec67eff6a7b9cedbdcea5a634b625e022d46bef0334a15f913ff602f3": "t63d_p910p", "fefc882caf819630a89666c5d03ae265f73467f9db4c715471dc9c6f3808a99b": "t63d_h1k", "2dfc2b9f10b060fe599bfc2f9a7d30d8a6f154065081b7dabaaa18a66f847c26": "t63d_h1l", "dc998500e285166570dd66e474a60f83e8b02a8b436e54bbfb936865eea097ea": "t63d_h1o", "261623d445af90bb7d6f6345aa2343cd14ed78c025d150e061f27a81ef8a1f70": "t63d_h1p"};
const sha = async t => Array.from(new Uint8Array(await crypto.subtle.digest('SHA-256', new TextEncoder().encode(t)))).map(b => b.toString(16).padStart(2, '0')).join('');
const out = {};
let url = 'https://web.pangram.com/api/history-list/?limit=20&offset=0';
for (let p = 0; url && p < 5 && Object.keys(out).length < Object.keys(want).length; p++) {
  const l = await fetch(url, {credentials: 'include'}).then(r => r.json());
  for (const it of l.results || []) {
    const d = await fetch('https://web.pangram.com/api/history/' + it.uuid + '/', {credentials: 'include'}).then(r => r.json());
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
