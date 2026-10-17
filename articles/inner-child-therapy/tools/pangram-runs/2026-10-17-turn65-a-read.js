const want = {"870861a0dad15592c2cc17ac7f3e58939263957232936a670321b2cd67307c20": "t65a_p12a", "2353f61837a3fb1df070eb6bbe6422aaaae2c1e65964f4afb2d999b7e028dd56": "t65a_p12b", "8811e134050b4a90c749be0ec7f680e273779892b5acf18360adab9212ff9de8": "t65a_p12c", "fd71754882f75f1a1ae3131b7661bcacd73b236ea74e31c36d3cb7b2e6177e23": "t65a_p12d", "8f0865c0f03913b35a3963358362208b01bbd82f95572570aefa5b36552d0426": "t65a_pairp12a", "02c336e4d0d2ccf698ec4a5f2fd0ebe627006707a2e5e27cef4ad405d3c488b6": "t65a_pairp12b", "04a4387fa100e21071eff377cc860d610e5effa9d5eaa11fe949380731b73c96": "t65a_pairp12c", "21fcaa9afc496abe4fdbca1d12a34effb72cd77a1ab59569a4fd28672f6030fa": "t65a_pairp12d", "0566d5774bd3d71699dbb34b6de7b152b53abf2234875a264d4bbe729f16e51a": "t65a_secp12a", "350e224b6f5cf3b556e2cb543e554c8d43927c53ece465cf7af6d6b7dc204009": "t65a_secp12b", "8e708f87dc8072fe43623fb191f85586cd11438b6f3ebf5109256007c88966da": "t65a_secp12c", "de95126af8355801bfcdb93944ed2987f75d36b5f3e4db4898dd284de47f74cc": "t65a_secp12d"};
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
