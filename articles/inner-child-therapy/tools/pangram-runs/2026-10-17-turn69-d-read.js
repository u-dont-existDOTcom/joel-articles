const want = {"3e94cc34d9d0b017c0c80ae1eed75d49bb44fc8d6046ada1c91eb221980c8c6d": "t69d_st1g", "6ddc55e6ca4e33b536f0d84c4e31dc386bdc621702f7e107f68ddfe86662cadd": "t69d_st1h", "43c7d7eb8cba466fe358cd78b566a345fe5c242723f471020ddf57329ecf8452": "t69d_st2m", "f8923ee7352538454ba3d5f6bca79f8c69a8ef9d0307af99566b6bbf4005492d": "t69d_st2n", "2022feafc4e704c2e792c368ba323310fcfd7cabccace8a8821f996d50714fbb": "t69d_st5f", "75b13dc43716cd553bf2205e47508ea48f1a80a7d0b4ee9fe6b2a903e4d9e3cf": "t69d_st5h", "738b39c99ec22cac6fbecbfbb284457667d8a0cb308497f46968c42dee6b034c": "t69d_secstpart"};
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
