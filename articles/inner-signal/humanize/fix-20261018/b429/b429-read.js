const want = {"30fcda86b0c3dde4b19cf4a8e3ef9d516ddf36b36e49d23e9a67b34471733f53": "HG01", "2fa0c5537cd743aa65ec411bf32371ca13ebcd4e6fededc670026315e61bada5": "HG02+03", "accb52be18bdcf5d88df91c9c074dbe6177de25664a00a6f8c978bde6a7b6f50": "HG04", "47eef79adf9bf346363427da94f7b3826054c7f8c12353fa5eead4e005800725": "HG05", "0b142a5f03224ec2befdc2c66e47bff5544b1530dd9f5c32bedde137f1a58352": "HG06", "88a7019d943810fb85069db60db5ef907e0e87dbe1631a2646129db8166aa30b": "HG07", "af33fe83d0c2c85e9e937b32f9a4b08f7cbccc4c147a56b40df6c9e1d84c5811": "HG08", "6b7ac2bf26c0243094b277fa798a073e2586c31e9dab1114b9af72331fc3e7d7": "HG09", "1b7462ca5d735500e4af7d1821238df68a7266c8aadd28e0e41059b55ef86e63": "HG10", "593dc68daedd4fcf310fce2ae8e9058350c6dfd061b8ef7920fda3c3ef41f58b": "HG11", "3dfe22147d25c0accb13653bc636980ce06d78f6107881c35642beb164d71056": "HG12", "092445330a35e56a64f2801b8c9e0f60465e065c9ad9ed6dba7e8c29fdf0140b": "HG13", "c11c40983d8268ee757e219694c9fec63b4334ec9eb9b9634e3b0d6a5f535964": "HG14", "970ba8e6b277b37dfc9054bb2a7074afd33a3f17be45a4373402b5db9ee88382": "HG15", "6fb5403bc56d03f10a7a97e59944a09691ac74163b05c0733cd3f99629779ad6": "HG16", "e81475bb1141cf08f3e7d00f8733f2cd5c3c2b82115ffd3127bff747d942bbe6": "HG17", "29f2dd149799af700e8dd60a3947118d8f87ba0770c23884864678eb624a7a8c": "HG18", "cc62657ee46a1d7ee8b61dd2e1066c7e3c23f4abd5cff69f42a162cd9831c657": "HG19", "65468e7b6aca6e059707581ca9eb868332fcdd52da69f3422e74b2c4346c91ff": "HG20", "ebdda3ed851fa9e841ef2d593fbfff5a26c51c79231a0b2c2af5b41fb5a1ef2a": "HG21", "cde5fab9d639c83da878c1983d57303e9d0e0087f45a5b0b8cff25cecf78ad25": "HG22", "e30364bf9aacf02af02640a6475ee87af9253887811a738aed4d2d904fe53ecf": "HG23", "c1910795fed523f874f288955ae8f7caed7fa9a8b4158a2e66f63d8a2d7c5570": "HG24", "74f31607f8026fad56501d82cef22b74f51f9d26444023191c03c00c39ebb6ea": "HG25", "05336eb189cf188a59f362da4f046f7152f828d1f0c5264693dd5884b5f03e28": "HG26", "a97813e22c9e9b3b59efc145306bb3cfd01b01cdf78a502cf6a2240a312f2321": "HG27", "485ebb543deb4a2279aadff693267dad301c6109825bfc4bcc619c1166cdcdfd": "HG28", "5f602615c896455fbbce7fb60d9f6c0cbc9f7bfee2499c87afef9cb8906b631a": "HG29+30", "b558346b2487bc6723d043d85d7d23b2626d6b4352a60f4fba7d0de6ce63e827": "HG31", "261525de5db38b82a4b42db37a4a03c62203d131cbcb80220084e1d1cb1c16b3": "HG32", "c88f4858487b2b65e59d78649ec25b10e4ae7913b1dd4016261a43855af8f843": "HG33", "1d6d18c70d667206695575e8b650480c7fa44734ec82870fecf8f696979846dd": "HG34", "dfc07549a89cead9902c303356d3f0189d8c42520b421d1d6947bf87481eb240": "HG35", "cad956e71b2cbfca4cfc6dfec1a22370415ac29610a5ed77e66bcca048e31a16": "HG36", "ee9e4413efafe41641f4e0c60d172439635481c173bd7d758a47dd5bdf40712d": "HG37", "52b50cb5adbe713b08eb539a721a868f57594d4b724a05fd68934488f8466e97": "HG38+39", "edaf23387730af13704b555e7c7f756345b29d4b5cf9dde2fb8044b2624bcd5f": "HG40"};
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
