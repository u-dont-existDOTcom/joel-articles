const want = {"b51c919c7cfe26dfca5c5263931ba6c53b1d6a1357455b521e3c98c47eb53022": "S13v29", "61e91b98927753f47e656ad2a089b7e98dafa0647e948b1d0657fb848697013a": "S13v29a", "6165e8b6446172b697e1b8daf9b14d9ded7018915343a73bb7184f139525cb6f": "S13v29b", "086a8e8e4d471237fb06210b616342b0db08554b0bfec8885c5c66f2222d111d": "S13v29c", "952d988274057d390cdf80f84d2c49aeab965dd7fb3ed8157a9dff8559e0e417": "S13v29-H1", "1bf844562cca6fd637170a9686e43d685bcd7c0554768153872898677f716cad": "S13v29-H2", "b30daec3bf3727de801f41aea858b5a4273f238f7e06e8c3b56cb68a6574e2e9": "S13v29-H3", "2b86075e590cba27020952a3eff3846d6b994890507aa3709f407986046ead77": "S13v29-J1"};
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
