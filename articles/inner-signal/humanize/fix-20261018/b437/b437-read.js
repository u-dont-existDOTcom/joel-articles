const want = {"938759581c8873b727496b0243df27b2c648ab36a2b31483e59565c0a0f35019": "HG04-emuH", "ed0057b75a4dac7571c74fc39a0fa704551e9aa3ab681b950d5077de3e9998c3": "HG16-emuH", "08038e5bcd3098de1ac3481c4a1b46dc3b202d4ce53c3c74c8d8e436fc3ed55f": "HG29+30-emuH", "7eae822e98b5741cab91f0f64bebbc7b9b7d21a14e1479689f01bdddb16f9993": "HG17-emuH", "371ed720046a2e107c7874af76bb8bb6a3b044b4925fe2fcb400d5950de8afa8": "HG37-emuH", "a126917ab1a6f56a437198e8964210980c906df23331e58afefad8570797843d": "HG38+39-emuH", "6d14a3d028be4521167acb201ba9c34e0b0dca92b70c47755f4ee4d5426a99e4": "HG31-emuH", "99b54ff450fedbd27c66254f265232459a335f1ae3c804cb62825c5df6acefd8": "HG24-emuH"};
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
