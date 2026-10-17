const want = {"472e43e240edef981b12babac90f36fff6080e58c95919f58f387bdfd1b9a26b": "t65d_p12f2", "3277303e9a97999ffacf546a8f01b2939cbd83cd8fd865df158e2c0156555688": "t65d_p12f4", "f0b05ab7467f0044e1f5aa34ed87fb75258970380db83b2bab299396cb97ad75": "t65d_p12f6", "6394267036a7adee337536d030b0a2f2e9a6f4a14b71e4ca4416dfeed192fad3": "t65d_p12f7", "46f41661cef2c2b5995db02ec2e3369819607092bd60e3de8e93ccb8fb285abb": "t65d_pairp12f2", "928af2d3b3199d808748fc24d960fe8fa016da765d860557426e40d5e1873544": "t65d_pairp12f4", "35716118bc5a3130d0d82bdeb044c7abfe4019e3a30e3755df206bab3ef75d87": "t65d_pairp12f6", "8406cf81d76bbe36c67fc898369311a9531527e2e63d189f9f4af7dbfd2f73ce": "t65d_pairp12f7", "182ceff1f7ffaa4c16cc3c6811389eae0e385851faf427c4013a3fec3cb95677": "t65d_secp12f2", "222a7569fe21f599a9dcd3e85b8733a86b5c9545772ecd20ae23579519ae7c0f": "t65d_secp12f4", "167d85b3a207f8d358a234107a1f0c0bee6af4fa9b08619657b937d5eb225ee6": "t65d_secp12f6", "933c99324a121b361178928a90626727b37ac3d227a6e0d6d1a9d2b6f5571073": "t65d_secp12f7"};
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
