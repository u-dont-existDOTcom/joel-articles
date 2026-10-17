const want = {"46cf692e1d316931181e94b64d60e1759f599d2d530c90d2cce7cdd5f3538efb": "t65i_p15a", "319a3aed24581dd53e84d56ad11b0e275981dbb576ae48123ffbf3aa966cf234": "t65i_p15c", "dc7e8c28a02e824abebbf3e6140a1b30c6fdb96d409177912ac101586c22ebab": "t65i_p15d", "6a8597d5aee4d9d6244de5b8071a39ae359c9992785afd8f3d755585927a1817": "t65i_pairp15a", "e0a47feb04129186bb63961c21c4b1ee48b000a473f5110b83210af42a0e1814": "t65i_pairp15c", "3a80d7df49c61bebf8c8787bc221caf4d582baff3e3f7e48ce8e6de66febde31": "t65i_pairp15d", "d1db3766303d90d5740853e2b23d9c34f9f690c8b394ac296b75c54b6d64222b": "t65i_secp15a", "43332aa14e0f23867adc8776709efd44b9ce09423a8d2b135a9c91b1a02b04a0": "t65i_secp15c", "ce61d5730424f8f7c6d75a229ce4bb80d22c9c6d2166d30b9074964ba6a259cd": "t65i_secp15d"};
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
