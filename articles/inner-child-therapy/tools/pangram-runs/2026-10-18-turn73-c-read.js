const want = {"a752a72f5006eda118974bfac7d34cd2b805b9bf62ddc8808400404c9ee06134": "t73c_yb4a", "3296553c0e26ef7303d2a670fbd09130cb01be2332e03631ab84f7003f4aa2a9": "t73c_yb4c", "9d72b34b2ea98dc010c3ff47762dae255141abae8b602437c04e957a106f806d": "t73c_ifs5b", "8da66ce5f8668ba315d37a15b60bc31fb3d7a2983e143447bfec05e810840d6c": "t73c_ifs5c", "a466b9f99c3664f0353a4940ddd219e75d5360612b2cd8c30b1cf045c1f23cc0": "t73c_chkm2", "a2d89d60a172532a7b0cf1a5a95488e29981376045a8cfafa291ac0ba00f98fe": "t73c_h1c1", "e2d9117f317cf2c27258cbabd6e1c7120442a51f78403b7657543fa4dad1fd6e": "t73c_h1c3", "e588bba9b605a50b6adb538fae5b312e2777bda0d734941e976fc073e399af14": "t73c_h1c4", "0e9aaeaf9f9a2947906781c4f1b5b4e9a203d5b5ebbd5ea9953662a2095ce24c": "t73c_h1c5", "3dac419a546f90d1bc3507cc4e342f4298a05a1e782b46e4aaac3bc9b04ab42a": "t73c_h1c6", "92ef3970c9d8a1f54cfc49f0c93e7c27e006aaf058f7e8df7133f5c5b5f74d36": "t73c_h1c7", "e50cce53995e551221be229b51e05ac8e84c3f03e35d0d4f50a9c02ef19370bd": "t73c_h1c8"};
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
