const want = {"1f8f1b072dfe8118219b4da70dd8bdc7775d954c575f3d8cac9bf507fdd5cd29": "t67e_ks5e2", "d0587fc0df2257908cadefa621f2ba34faffbc4138439a155e490167baffe271": "t67e_ks4be2", "c0070e303804bb5d397d7d62329f20ddd3d6e22ca930dd279e1b6f1311f1d591": "t67e_lm4p1j5", "e45a191cc6070fa2e7c821f3f4b623af38970b185619b8c19530c296a46b2248": "t67e_lm4p1j6", "26b9257f94d0cc2a0de1c74c94112ed8872982c8469dc80145cc58756f8aacb4": "t67e_le2f2e", "05c5882abca2a9f9e3c9743266b8070169f11d1ee0ba4aaa69f897bdf580ca21": "t67e_le2f2f", "b6449440957c22bb9d90870d50beeb499443553bd24f8196180ccf958152ffee": "t67e_le3al", "934328be5df6c57fa272cd1f23221811800ddd2ee2539f4c8388b2dc350f8a79": "t67e_secksp12", "6a1dc4012613488f5bddd6d11014529cad97adfd4c3c1464ca77bdc84d392e60": "t67e_secksp21", "da0a0e648f126f3a9e3eafa5a95782f5e98d2085d2644228ca940d350ecffc0d": "t67e_secksp22", "0391a04c293c0f6850b58b6ed58ab4b09fe3fc1040577cfb85be325b0afbddc2": "t67e_seckso12", "96fc5e247deaf5ffb10bcb3c0269a55ff0ac52ac9b173249ab7739131b367423": "t67e_seclm4j5", "1dd2da6a300b4bd5617772f433dc90237e7bedfc3bae1eafeb4e6351a13d0f8e": "t67e_seclovej5", "1b78f14e0f3edb868c8ee3e7df2d4e1ba95f114b1b59c8af77d5642e9611a6e9": "t67e_seclm4j6", "27d57958c182b44bddd891e855e2d05ce0ec9f5a755a14c0cd4e0c693bc6e67b": "t67e_seclovej6"};
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
