const want = {"3a054f53532623516b5effe0f28ec2fdab1abdaf02f1a7fcc8b5d6bf9d6b2719": "S16v29b-H1P3", "b1024966937adb4814f8b7122d3fc359e587ba56d1a636b8a65e7919b4496d1a": "S16v29b-H1P3+prev", "16653d4b9ae9b746e20e4e22ef3a205d8715005e5a782e979957fb3f55c86739": "S16v29b-H2P4+prev", "88a7b9fd1f0f463c178efd5c7d05959bd41a1e44cc6c1de56688a736a5b2e941": "S16v29b", "0c37774c8f9ed6f1d1318f2c0018a83bb172bcf5e77cf2fa05f1423fc1aed605": "S15v14b", "6b8c9473e795b33c1642d4cf137a411501e6beb08cf864ce22ac1dc25a75cc18": "S2-A46b"};
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
