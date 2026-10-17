const want = {"082cb99494a703176fa49a7b7c8969eb7b769b563ca3df3af15bf3616243fbbd": "t67b_ks4a2", "b0b094cccc4957792f2b78da4a1b2fe7b5dc7f90ab005ec1d513c0822e68c533": "t67b_ks4a3", "4efc454df0cd588971f3926957f86ed1263c5f591bcc7670d352eed70a54b7e0": "t67b_ks4a4", "b3ce7a1a143e886f58b5d875d06f5897410460369c9d9acc003e80ad6cd6fe38": "t67b_ks4a5", "9e9ed52ef42b87713326b739ab591708012f87cf8a3598d6cd85b95dd446687d": "t67b_le2e", "e16b8a36ae12b5b0a64bf2ba4d30eecaedf3287239ea073b6692a4d6f32b3fd1": "t67b_le2f1", "c921312fc9d6439cc83e811a8e5e1c071b120465986716a217dac46ed242c054": "t67b_le2f2", "18e41dd4635615eace6cfd9f22850d5d037b5b58cf27c1d9ed8612425aeb7bae": "t67b_le2g", "a256d4448747a5cc7aad441d5def5742cfa7acb46681d46d4340173878b9c239": "t67b_le3ad", "3b45a4d899b5ed274a7aa4380eb2b196ab9c4115bd3a14875750170f19605865": "t67b_le3ae", "88d1e221e4baec763f1cf6972ea5ee5d70c7e2922087c84b111f1cea5204370c": "t67b_le3af", "404382e84b86ce34ca9d24b5acb2af410ffb3c8fd86eab3d93ef2375790040e2": "t67b_lm4p2j1", "a96be00829ef1c201f707a719774eca7225694138c125b95e61548e3136cd2e8": "t67b_lm4p2j2", "8085ee1179fad61394398a91c341476eb977209d7ad3fe259cea88cba4278145": "t67b_lm4p2j3", "f46d4ce3d750545b3178fa8029a391b0189df98989a9d380afc7b0c364b9c0df": "t67b_lm4p3j1", "794580ab8138989f02af894831ccf9e02673ccd3a2c56c7f66dcf80d18b7e026": "t67b_lm4p3j2", "30a869118f42dcb2e721cfff9ff501ed081562b6084098f6f1045ea1dd9a1b31": "t67b_secksa2", "96456b40f6e2ed6e76389a54334abe99be6acf40e358929d5d5db4b47825f586": "t67b_secksa3", "04f024c5432aa4abd36406dc012b75d2172d620551a33661aa031e0f1bdc252e": "t67b_secksa4", "875e6a75032dea4411ba58422b6d0376f13f68b85fd5afa15f6f92961e04cb4f": "t67b_secksa5", "8f94b878fb7b1e985f667801c70bf518a04a8e790cef5845368384822a9d3b33": "t67b_secksa2b", "0722799b7f711b04ffc4fb7c685136e0faf07bff391709bc6802de21ae33a461": "t67b_seclm4j1j1", "4e2825284a333948cf0097e40fb162f5bf25b4362171d1e89bce635ca81882db": "t67b_seclm4j2j2", "138f89fe8a40a0912293a56f18c9504e281dde2dcd2b37c57968b583e01bdf6b": "t67b_seclm4j3j2", "50e54cc8b28d158dbdfedcbeac48f1705e71f71f247a24ae5227d7e24a0d73c7": "t67b_seclm4j1w2"};
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
