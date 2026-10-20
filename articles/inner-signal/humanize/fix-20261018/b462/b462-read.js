const want = {"d012e9053ae91e724bd882753d04fcc78bd69bbcc0317448d46be0eaf4c2071a": "HG36-fix", "9c4c72054de41b03eeb89e767e0669c1ae78c018feb3bdc61d31e719e566a643": "HG36-y-p1+next", "7142f934519f4e2fad6a916a82da07922b2ee7544ca4d4391d9057bf408161b2": "HG36-y-p3", "e449f628d6288c834440e26974ed804a2d054ef7284afe6da673c60ba692ec2b": "HG36-y-p4+next", "477923be13006ae24645cefa0d90691567835be939f5ce21634386eb82e13f2a": "HG36-y-p6", "346a6624b4c079c53d629ef24a1bafab67e3a3506dfcb52b2634312501c7255b": "HG36-y-p7", "778b6c62cb1eb54a2776570f9cac8b68f31d4978b42769a79cd634a7df5b8f43": "HG36-y-p9", "3ef3419921cdb8465c7bc9eab4bb8d45548847450ffced321818002ebd99f42b": "HG36-y-p10+prev", "36b8dcb05e18c76e5c068909194fff2363a08846940bac93e44deb0b7fe62c16": "HG36-y-p11+prev"};
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
