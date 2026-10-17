const want = {"9407bca7eb83cddba24ef04cda2e024d5988244e56a0068563abc81b911f6a3a": "t68a_le2bjoel", "1f602c03abe526bd495a24578da8f80a58133f76e36afef5266087466a6085d7": "t68a_rwa", "0aafd4c917106f9d3bd59d426ce92abcb6ed554035c84e7679fee7fb39ce8754": "t68a_hc1k", "e1d2a9d174a7e0f410f2119d07b95ad6a06ebe4bddafac3f06684aa30b9a00e0": "t68a_hc2n", "a646e0eda204e1cf290760413b262a250275304bc3fb4bc789cb6d3a9baefd6b": "t68a_ks1s", "42fb02ac160d3628c7d500223a09b3721258a4cecc8ff910a6347e3e9d24c1e5": "t68a_ks7f", "26415f915a64cfd087b958d55d068eea7677551cb479898aa35fe28fdf60a920": "t68a_secle", "ce89f382d7ddd145f9a61a326feb89735ac10da279ed3b7d7cbb5db201f89fd6": "t68a_secrememberwh", "84bbd3a0394afc2dee315350a66925a12d05c1a666faf555e88a7dee1780ebd2": "t68a_secahearttoch", "20e829f5351a69cb2b0871489452623ef314d93c54f22c92229f0eca32f76e90": "t68a_secsimpleprac", "5e7896381b4df58659a53de0724b76d777fb32a91267aa754546062f5e62fb3b": "t68a_secifyouwantt"};
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
