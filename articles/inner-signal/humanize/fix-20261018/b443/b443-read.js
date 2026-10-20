const want = {"ef7f13929461eba79f607db6e08bd40a958fa963599f08f7e923257f0326908d": "HG02+03-refix", "bd8e00fc57ebcd9c0f7e182889bd74e960a9cb5b418f0e9c4df04ce6bff99b07": "HG10-refix", "a0fbade1c58c2c07a169a0c4452e7c174b26add36b98947a00fbe42ed951b7bf": "HG11-refix", "f82b236267c00c0df345362fe27e8747244a71ed93a979136dcde2f09468aa6f": "HG13-refix", "59b333ac3b4252afed0545daa878b4cf6864f0ee0ff65d730bcc5a908997932a": "HG14-refix", "3ef779ed5ce66846a7e7047095194923190d5471a44381998825785fd7143080": "HG15-refix", "32c382ff3280a2f503683cf2570290d5bcf44ae1db3debbec4a4aa4821b078c8": "HG18-refix", "b0c1713226590c9f8559fb6374ca35c9e8a3a33a427b0badbca39250a8e7fbe9": "HG19-refix", "434932a959142fb113036d254379d541c346d8682a2fa60c011aaf09da3ed698": "HG20-refix", "7c3b16f1bf1f27a53db15ac8f80c184ea8c73c4cf77112f336af83d2e4b2b905": "HG21-refix", "920bb2f6fd301330b9daa8b470474789d869883b490b53a9737c10409e3f7c1f": "HG22-refix", "cc23f2d30c4a11754d4a8bc6472938242821b30977fe3ccd33f1a9b962fe5129": "HG23-refix", "7bdff950c7b3006d2bc0a7f4e76b9894c9dab0dea1070616fdc2f215dcd7085c": "HG25-refix", "e0e9e13cc3b93a4263e9a3d227a8df96f1630413bff8e834d419a24a9fd7382a": "HG26-refix", "b16a6135be404fddaf933247608146c136db185df2bfeee9ab531cd365bf757a": "HG27-refix", "80cb46deac3277bd5038a0b2f1847f6eb73f62b3d17f3167e37517b6b589e747": "HG28-refix", "b30eb5af40508b8219749a409bb00480d9362f56b2de524856f035628620ff5e": "HG33-refix", "53040ba4e2f6534501637d82ed68fd225e37e72d3ab88a499b115f2b8e5e7d1b": "HG34-refix", "1c9f0c712e92362d1ae6f19e693e119c9a6e563ef039911b5b7fa0d68301ec90": "HG35-refix", "f48ba94ac3350360bcb7229f31d184f5aa1bd48d10b837bdb2e5493988424ac8": "HG36-refix", "a42004fac5be11fb44b85eca2822ebd321f37a6eee690573d730b04c43c0d91e": "HG40-refix"};
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
