const want = {"a3e8930cba3101e6d2e83feef10333de655d685aa3c4adc51a0a8def689e3a6f": "t54_O1", "9f2f135dae7ee3696f262dafbe897038ed8744c00ed71fa8e9bf997f0cfba8ce": "t54_O2", "ecce0e57664d484371495867cebb6018dc16ba6d33bc289b60e9ad11375c881a": "t54_S2", "d96c9b334b0f8567fde585187f68834befe4372be4e8a622ff11a62854651a07": "t54_S3S4", "9fd0e4926c1051e7a07beb00c59b018229e821efa821ca7ba6b01ce3281f62dd": "t54_S56", "5153f8323b63539c684ab5eb44c5979cfa3246425a603032c2a7a6b506741c70": "t54_G1", "0db7096cfed29211c54e8ac4399c1c44895d11a0d663bf07ecce8f3d4e7bcb42": "t54_G2", "f0934e90aedfa860f552798fb4069bdc14429233eaa81c7de41b9a3200d98d06": "t54_G3", "6de7afda4b5e6a57c21d452d60de35f6fc64d18871bb4136f7421c2c017f26d5": "t54_open", "e1e02b2b17e34aaaf633a92caade89bc8c2d178cfcb2c3139d2482ed9ed321ac": "t54_fs_h2", "a6ff9cc0cf6d620395dd535636af1e975ceb59c1214f77ed65ad4ce8d82e0f9f": "t54_play_h2", "cd03d72454091238717bd008f23066ab5c052370a82c16bfba413b466d35f172": "t54_spirit_h3"};
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
