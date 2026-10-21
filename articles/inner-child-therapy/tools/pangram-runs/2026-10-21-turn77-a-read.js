const want = {"80f171cbc9e47e2c2232aac32aaa80746a1f25ce36c1a5f0414333936465cc2a": "t77a_j00", "d8a0b1d71b4fe49521ca07460d111a4cb19eb74fa4c37ca0e9b98c0e6231da23": "t77a_j01", "ae6fd94d75996d614c852d7608455a0a78db79a2dc96342dd8ed5f461550bcc0": "t77a_j03", "4df6c7ce03547175103e6a2770aa13a6217f9d77f83c8339a9a4a3aeaff0e3b1": "t77a_j04", "b7e6dfcea2002809dccea607c0c8c881829aa546d04f868ad93eacb973e17580": "t77a_j05", "e2826637804dc8b1e2015fa49eea12dd91f4b13ce57ac5a4ed37ec6a7e3d23b8": "t77a_j06", "b41c42bac8221c9de978d09068096bfc82c2abe6f81b29266581cc953634ebed": "t77a_j07", "789b91dcd3f4f7444f797ba71036572e643523015cddd9ac9f2e0f5286dfe89a": "t77a_j08", "f05a1ccf6ce56c781296db5d5329804edc811e6b9acbe55e733cd7711c655d88": "t77a_j09", "35619771578481cc6209db9e4e4d84cf963ec93dc1f9e12e2b63001623fa74b9": "t77a_j10", "bd40aabcf7209fbbbb797e07a0b8bceb374e67e28aee861ebd9cceee2c78a73d": "t77a_j11", "b830b262a8dc4d90e20b2435ca59ea9ca4d003ec2bc0b72d35868ddc5ffab589": "t77a_j12", "d345fc0e7b60fd1f3fa1c5c6c1e1a5459facc87819edbc59fa7a7a04eb852ab6": "t77a_j13", "3cf4f3eae3af629f1589c2e8d7e50de01f3b1da9e800132c7c09a4a00dfe2b59": "t77a_j14", "ea6e9344fd6e16f7f552f956d2418bf0ce3c90031ea03b1695c323616e707d77": "t77a_j15", "2c9ff76e5596cee6fc51b42e1a626929d33c1ffef7736c5e986ff0d886d94139": "t77a_j16", "4c753751651167ce76754754f6a437cf8ac63bde4f2a38444201249783f8c579": "t77a_j17", "b01049ad29547e81a42a40b24d2b214e8896c2572d72e19e7bc17e5a678c6619": "t77a_j18", "71e3dca2036625bf2432b0f123cd87aa02caa31552ebb15e005293866e56f4d6": "t77a_j19", "c72da6b26ea96afeccf5efae4e610da950862b674fd8a056e587e403961ba8f5": "t77a_j20", "5581a59be11d3ea54005fbc5eba35362322793a90a2d07674b2345da01b24614": "t77a_j21", "3cc4ddbc55ca28b2abf92500c205ec06edf59a82cf241d287b80955454c65a53": "t77a_j23", "68f86fe962c304c480affa1e969ac5a259c3a05d4d72259822147c2234adea17": "t77a_j24", "0acb2546c54738ab23a954a78c211629cd5397d54c2b0a8ca2dd927040b9aadb": "t77a_j25", "a42ade50e9658b94542cad11849e16ee22bfb9b3e037a24c2349e66fdef7d92b": "t77a_j26", "1b9971d0c09419f2301eba2f414e131d5ecfda9de998ec6e2730b374969a9697": "t77a_j28", "6c1eed4c98f8556bab66167cea0cc0ef2f23643bae2e754293dbed4bfeb63290": "t77a_j30", "f7789e9f257c283d1efe18327b59190bc15d0f9df49018fe9fb871816cbd9314": "t77a_j31"};
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
