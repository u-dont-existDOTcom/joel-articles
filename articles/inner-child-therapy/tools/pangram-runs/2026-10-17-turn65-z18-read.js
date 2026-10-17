const want = {"474fac74e3066d35dfd9452f83bced47ee31b88653137fb26496fe06f076a77b": "t65z18_fg1p3vw1p1", "df26d377ee31c2de6cd87a6702f3eac67e65e51f56c895fa06c6487c34add73d": "t65z18_fg1p3vw1p2", "675979771549aa0dc6378d31d6238f2cfcfe0736ca6b498a6e2d17a6d922cf09": "t65z18_fg1p3vw1p3", "66f326840c964ca46530a875109d5f311d35d93dae98bc2ec9e7325d62f7619d": "t65z18_fg1p3vw2p1", "6c795b4684191f78ace9b5c2ef30e4ec2eb29f7e1bfa4f3e435822575383be44": "t65z18_fg1p3vw2p2", "70ec9c4057b2efa57c7b6eb1e9f65b71fca3bfff8174a361b60a68f3de26bb18": "t65z18_fg1p3vw2p3", "09156e27472370be45cdd8f217d0c93b6dd5bf629b563e8cd108656f9ef3c798": "t65z18_fg1p3w7p1", "fc9d2f56b8b945d7ce0ba2812fbd9c3334fada8f3c137824e2a3184b38ec5ed6": "t65z18_fg1p1w6p1", "964ff996a5cddd387a00737f339841fdcfe593465a944257e5f02083b6fffe09": "t65z18_le1p2w5p1", "48dc230e7cc9de4ee307956400e9d06cf96170387b8ab3d7482ba2e431893753": "t65z18_st1p2w5p1", "06a39619c31df0b0aba391d38f98f33f1dfa62811156607f50372504bab010e9": "t65z18_st1p2w6p1", "245ee1dcae568ba57373896bada40470126b3322f5a2d9eaad581baf48b2c382": "t65z18_st1p2w7p1", "1c1bcc62dc3ac1c080416074c792676956c594ef157f0ccfb04de580ce2e9b7c": "t65z18_st1p1vw2p1", "b53b638966fe8d8304459d994ed883ca0e73efac3dd0d6780cea7df51bb57f97": "t65z18_st1p1vw2p2", "4ded4182ac7fe5dae5b211267246d92d239d90dc9be9c1fce22402052bb01e98": "t65z18_st1p1vw2p3", "fce74ba1efda07e7287f5ba977bdfb8b92c7e52e380d40a79d7e84b50fc272a4": "t65z18_st1p6vw2p1", "13b5630fd20c46e4a713feea2ce550e869c78a69b0fbfabc090fdae9b0e3e24a": "t65z18_st1p6vw2p2", "165da537ba622c4a04a0b499e91185e1c073d2c5629ad89506e6ddd5dd8a7d77": "t65z18_st1p6vw2p3", "a6ed4ab6110abb2fdcd116c4d3e7ab5087e10f0cd6d283945ef1e7804f3f031b": "t65z18_st1p2vw2p1", "e00a91bfaea40f5607878fb4976a87d0e00726c565dfd645c90c6a78d382d011": "t65z18_st1p2vw2p2", "9d9a0ea4f7368f2842370dd02c17adcc8606a10c3f2ab2f858a201d94a274da0": "t65z18_st1p2vw2p3"};
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
