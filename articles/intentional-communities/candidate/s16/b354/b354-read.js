const want = {"6776ff8702d20b9edf51182c3753f3ae4d5d6b54ef465cfa990543911acf94ce": "S16v16kkkk-H2-P6-H3-P3", "e9c7eb3b30f445acb14d8f61f37ec73e46faca6bcf615733c0535dd727045f05": "S16v16kkkk-H3-P2-P4", "7852b5bcb1025cda0fbf9dfd487dbe06e33c3635b208569c04a4f1c4498f22b0": "S16v16kkkk-H3-P3-P5", "bf0df089b7857a993f480a079c903660da28a0d54e2188421649df68dbda88b4": "S16v16kkkk-H3-P4-P6", "a1c6c00bbc28a85243b4ebedca1c06cd76edf9286b059157a81c64021a8c7337": "S16v16kkkk-H3-P5-P7", "4e8e5a57f0c34f7be66a55f080764af378f1fdd42a7812a5830714c81398b31a": "S16v16kkkk-H3-P6-P8", "94254c632a1a14f96f0402568d3ebc74ee73491e61913d6914de2f192c0c011f": "S16v16kkkk-H3-P7-P9", "e872547855a5e5c866355fd9bf008982282f6b5ccde58c44afb57ed0f0832839": "S16v16kkkk"};
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
