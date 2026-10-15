const want = {"7e932d7285bc60fff10c640c347b23ff75882931642f7fd58b541b936b51b2ea": "E-S6P8f", "4fae7d8a2ae5961b8afec99f1ff0e11ada60fda884305c27b4540f6e7f966542": "S6v22", "d8ac465679e89d04a70d3914c217a63f2be36def39dd3587f434d1896180b9e2": "E-S8P10f", "81faca0765a5cd84684a59cf9a78188892ad1fa5df4dbac5e333cd7be2d1b310": "E-S8P12f", "ee5ac53867b9ec00e66726ef2270eda0b86ff66a70ba70d57a5c259292237021": "E-S8P20f", "d3666cf800d971fbd6d482b6a1f11828d1368cbd1d754928c69fdfe0f5da4253": "E-S8P23f", "51736e648988228539710a3d99b15bed5bf7d331f9287d5040fa4a4fdc8155a7": "E-S8F10", "3da284018ede65526759fb7c658d0116af3d5bfc81a09ccfdebbfb501b022144": "E-S8P26f", "08d545414aa0d3eedf96148d02c7b2ee47b27b66584f0e8e7ea779f8606a2ba0": "S8v29", "629f44a103fbe1b20c13a26bf90a40fa769a4ec8ac47868bf328013696ea67ee": "E-S11P2f", "5c4b9f49bf79380d4643476870f9d83684514cea368a6e63bb4b3d508ecbabf0": "E-S11P4f", "4fc29b403b38f21427e343765d3d56d3330093c441c6c9be367938f6c363fa15": "E-S11P6f", "6faa9b89c58abbea2adf3106c28841e9bf62b13f039a446beadf712a752173ab": "E-S11P9f", "7f17eba5ec88c21bb243050eb4ae124fd83da86bb360c0c9cb890c1fc3272195": "E-S11P10f", "301e0948bd08e2d891e6089fb2436de00d68d049b7b4d4133a85a8a6032e46d7": "S11v14"};
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
