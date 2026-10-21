const want = {"dd981a50603636e4285947f97fec5bb35d10a2d167f5944a62e2b8f70c52e473": "HG12-p3c", "98d0a7990390b486f0fae36628c86b03a96122b6630017882fbc47897894a3c0": "HG12-p7e", "faadb6e364f9990dc7884e8ddbc7fbaf0a3b66f206b39ae693da7652af8eef9e": "HG15-p9e", "e3b01385f5a4626e49c45ba4a895cdb554457b6ececfdca3dd56cc23264df3f8": "HG15-p11t", "dc849e4fc570a1d4646bc040552fe764a83ba68769cf6c64bfe26d06282216ec": "HG33-buteyko-e", "fd731a46b244cddb05d28574d39f9bf888c7defbb802bf628edebceaec2b9191": "HG35-forgive-e2", "4ad4c679dfffda33aa258c55a6e0d96b48eaeaeda3955b70258cb27d741ae806": "HG12-w467", "2bdb6688329190366c11d39db369c909b8f41a35cd270ea370d84aee5791a93a": "HG15-w467", "4b4cbda87d8872b69dcdeb439a2647fe0027b8193d767d4161f81263039a1efd": "HG33-w467", "c71ba7b3e8caaa871ba8a4fad49ae0ff525965c996bfef476cfc60e57ecf2ff7": "HG35-w467"};
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
