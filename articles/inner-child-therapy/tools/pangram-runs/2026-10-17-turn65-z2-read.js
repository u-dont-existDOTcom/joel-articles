const want = {"5cfab1a8ea9469d354027353ef77fdc3368598f9e6b41513c4fe87d2bc83fe98": "t65z2_st1bw1p1", "5f10f8a873b38fabad6aa580b997fa60540589cb541ce29913881834246900c7": "t65z2_st1bw1p2", "05d04b25c4fd60ea76394d5f2e360b53ee241c11046f318ae3e382daa49cc142": "t65z2_st1bw1p3", "d7e3c302d0047412ee4b7b4f03f57bf66f3afb33b7fdd7927c880913a39c52e3": "t65z2_sp8p4bw3p1", "dc0d6b38fc4338f95e3711cb7eec00fde6d8ee62b47c6a07909e1bf02aea1e63": "t65z2_sh1w3p1", "ea0b4d5abb1a2cf47033b151896e7838c86caea37c2b27000bf0c85c1aed02f4": "t65z2_fg1w1p1", "3fbb990f93e7654f74cab75e2900753f962e6032657fdce3fb0f1779b1f5530b": "t65z2_fg1w1p2", "7a8c7d34b1da9fdd01473b53fef51c2e7e2073f17997217336116ba00bf95822": "t65z2_fg1w1p3", "21f443f9d93cd78538c240f64bcaf44bd6a349d423b8cc40b3882a93bc70f2ac": "t65z2_fg1w1p4", "4895833ceb0d041c3550a1dd2b40169d29b3a407fadb8581b4878d4e31536946": "t65z2_sp9w3p1", "367c3693e78518602f62ce7b5245aaa4dd2e05a4831267f5f8f9c0d64a82a3d6": "t65z2_st1aw1p1", "27a6fbf7541ca79161e87a63b2a608d22c10872d49f6ce1822714c1b792b1510": "t65z2_st1aw1p2", "435cd82609f4afa3f766d46dcd8290c9540baef6f3cb01d9d74eb6e9332f5a59": "t65z2_st1aw1p3", "5516954819a0e84b4510669af6518c2a7f367ea99894c5222fec084b54d7d514": "t65z2_ba1w3p1", "15456c0c2bb2c477e6e0b99f2aeba93249fb8f8dd25616267ef7820524e21a8e": "t65z2_ba1w3p2", "25b74254e8e57fbe4ef687fed0701d2e95c7f04e0121fdc3596de38be52944b6": "t65z2_sp8p1w3p1", "511659188e2df59e2163c0ba5eb862a1a76572f314fdf993909e319b462cbe9a": "t65z2_wl1w3p1", "b3b8321cce3a07cf40bc5fe90fcdb4735498ec9e343d56c8b39f1b9c399f68e9": "t65z2_lm1p2w9p1", "8c8ca944de31ffc1dc630042c726fd883b7977556a52e5c28560f93131778eb4": "t65z2_lm1p2w8p1", "1edc7092f807dff685ab9981e4522c008495984197fb2f7bd701c1d1218985af": "t65z2_lm4p4w9p1", "1a5842c7f996767b189ec0496190c240b42f007e61e499a71ec85fd683dec11f": "t65z2_sh1w9p1", "45e18ed9ae5325bbc4e88bf22ed4e0d55442eb754415c5d6a6054b0158f22cbb": "t65z2_ks12w8p1", "6e61b54020cfe6cdca823c1ab4f65e5786f5fb6a8ce537a3b0856e0e3aac70fd": "t65z2_ks12w8p2", "f8891123b07ba127ed49c784c8f77a8f2acdfb6d705f20f1c35fa82e8febe30c": "t65z2_secba1w3", "991d5bf16aa8b8270f45c9d53d08e860de234682594a1e9007a38c85dc1b606e": "t65z2_secfg1w1", "c8d02b99c4b84d608e76382a4f713fd75a26d66e157953d1e713155a93fb2bd8": "t65z2_secsh1w3", "29a9484682c48cee8bb0927a901b31893b8fd5ea1a853f3d9b2f9ace5d60ff97": "t65z2_secsh1w9", "69da026f949e46a5f813fdab015018c1f880eb0f06eca4c207a85ca720e31d6e": "t65z2_secsp9w3", "0bc47f87f8f9feb77512fb458b867e6be207d0a88a919263d0abffe3dfb9571b": "t65z2_secst1aw1", "2035f1d4dd3f713ab81932c1d207d7eb98e3fd5c3e84f86c3ee2f7b16121121a": "t65z2_secwl1w3", "a7decf08aed918d96ff2f2204f89664ae1d3d285ba662177800c58d91c8d8f2e": "t65z2_secwl1w1", "f78fdcfab74c35e7e7192a548d2efce7355ec577c4269c5e39df257d3003c354": "t65z2_secsp4mix", "c4101f20128b507ac1fa17585735fa551dd7dda19516797bbdafddd7c5ffaa9c": "t65z2_seclm1m9", "dc25babf8dcdf4e6311dfd16a0045e783829f147df8f0d7d4ab7799ceaac6ba8": "t65z2_seclm1m8", "c61feba8063d1c0622fbd57bf145c2b5fbd4c04d415dbeb44b475613dd028aeb": "t65z2_seclm4m9"};
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
