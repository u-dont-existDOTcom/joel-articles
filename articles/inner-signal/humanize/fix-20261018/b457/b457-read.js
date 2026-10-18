const want = {"431035adfa427ec9132c51ccebfa310f5ffab3a346ca995fd3fc1bff5125bd33": "HG36-smc", "329523682c0bf1616a679e7b776b66012f5d811fd3bd1aef28cd56ec47dbc773": "HG36-c-p9+prev", "29649b1776fc19e85f2dc72e551ba5b940263da25e8c71fc9f9c68bf8f248221": "HG36-c-p10+prev", "f526e4686d27d4b2ff2fa76e74d0969f8b7ec51f1369e622a6580a339a29829f": "HG36-smd", "307d2a0362a32afeb56fe814e724b1f10511d55b341c8c26eaadf30935d7b9f8": "HG36-d-p9+prev", "080f4ccd32bebf32d9b4209aa2581168c826b33bb39b5d6f567e2c7e62c34f7d": "HG36-d-p10+prev", "03371906a6c6c089df4f13194b96bbf11324c789cf6f244f6ada167408deb099": "HG31-dg1", "e8d4d517bba591c353c91f29e1531daacdf60528b7c43b62c6181a01d0fea788": "HG31-dg2", "da8cae9a2f89f79258f18434b56cad63940aa2c13b7654f1e3c080d24eae6477": "HG24-dg1", "5a1fde80ccc8390af9cf820fd8289105d78190066335e93c0d27db4b0421ed62": "HG17-dg1", "509704645d7a55298d60d60c9ad0a92d6d9ffb9f747ce3e2668bbabd65b64d34": "HG17-dg2"};
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
