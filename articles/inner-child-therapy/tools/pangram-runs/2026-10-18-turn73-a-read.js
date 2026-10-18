const want = {"9fd2d19efd721821a52c9332774c26656945a24fbaafc7d75acd89f7fd454a37": "t73a_c552", "f19ec2db8d018a8fc910ba5af71d110e1433682a9508f0312badd8ea249c7096": "t73a_c554", "82b515420256113798f82094e29ecb9cc4b2d9725b91f7ec9ec297cf41e73461": "t73a_c559a", "a2c5df4a42007dd23d2713f93eb09dfd987ffcaf75c84ee1e67037ba40067359": "t73a_c559b", "edd19dcdfceae98599fe2a7cdb5ef081c7ca00bd767230db87101c241e744658": "t73a_c5512", "32f50f6202915f12cd9bc03152905c10a7d6f7ce60e05bd0fb6add19b76b0b8a": "t73a_c5513", "09aa7af7d50fec5882e590e4801ed483b088d30452b3c3b20dfa46b7de4a6a7f": "t73a_c5514", "635a04c97fe9b3dfe37da564f5b2d6396eac954e936fefa8acd4228b9e0a1956": "t73a_c5517", "118b4aa9b67e0480900ee22d35c13bc90883ebfbd1e38c6d6115fbf58f85cfc9": "t73a_c571", "921082f3c0dff0647467f89c56ccb17a1f510ab8b279a5210f74d39d2149dff4": "t73a_st2a", "3ce38961d44e70efa3c61c8f8d439db99d06b5ebad02c8999689f96424114dbe": "t73a_st2b", "07496a67a64fc8df5a26106d1c37baa28debdd817832d1f2d4c1dc30eb48db40": "t73a_st2c", "897c12009b6dc5a771e3c3c7fc1fc6f57eae72a5c6652811804dcd73fcb4ad83": "t73a_st3a", "95b4902a3dc57c7906b72aaebe877d59b404f93ba7058a187d3694ae87ebe8c6": "t73a_st3b", "5a0fa6f82b0268c1c3dfe344780c7e441eb50dac0e8c2579defdca544d595048": "t73a_st3c", "f90b5bbee2a54f9b5fe04cfff6b281cf478612b4426214056e33d3166b5cf17b": "t73a_h1bga", "defb7c6fab79ed35151942559a483df43bd5cdfc155661a1cfcf1c347be9a5b3": "t73a_h1bta", "f02c33be4aec0baa28e65e655e2444fbde41091c2785434d8754bfecd5c2f4f4": "t73a_h1btb", "ba6c3691d98ac5ef6ce673bf5239e106f8e3f12579b8bcc3f459aa13b426fd82": "t73a_h1sna", "1a283bf87a1ea78a77511a91d2d6905e64539a21a87ef43e00d75498484e8b43": "t73a_h1spa", "0edd7b567a251020497f7103bcecd2a202d6e1d6b5718f325bc1bb97c0708c36": "t73a_h1fga", "d11bcd4ae305e7e69b77bcfd051839ec07ac03d39ec1d46ffb0497ab9177d31b": "t73a_h1sta", "4a9d2b6a6f8dd842b82eb1a3a45b83ddfa05b33e6c13e51cc0fad9f7c841f614": "t73a_h1apa", "41a9b39e04ae2e2de5d36b1cfe4c50885273a3681c85aa42acbd7fc86f622b27": "t73a_h1apb", "4a1c8b38dc480cb978b34557c826806f1d8c486d26aaa897e5f4d1c1b3248200": "t73a_h1apc", "b6a2ba71eaf2b7e94c37f7c846a4d8bfdf53ed108604ba0f5b21b4a51a128e33": "t73a_h1apd"};
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
