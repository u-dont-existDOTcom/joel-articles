const want = {"eaea891b579c3783efd7b44acf1166dc5b77f0fefbdd4ba1bf883fcd17432897": "S16-A", "16d485391508a736e4d01d1b7d43237ca526e9ca6acb382c9860e375d418edb7": "S16-B", "22b2a027e2594485d9cb054793bd16e27104ef24e1fdd5d982f5f21f22e93054": "S16-C", "03274455f1743e69f159a164746170f8eb06faf6d000970e29057f89aebf3662": "S16-D", "def736e7f1b64daec7f8a7aa93de641894eab37cde567e42886ebd86157bb310": "S16-E", "c27504af4bfc69a1dbd5ad264688b41c76945d7b0fad471fae7401fd4515e251": "S16-F", "f7dd076a46196ae639277c356ab1e9b8996f27c510ee14bcc7e05598db001fcd": "S16-G", "787448f4ac9b902be0d26982d8c2a82b9f149fefce02c6869e71f41e95f8b3f9": "S16-H", "fb235423e87bb491624cb19edb8e2fd167ba28b297d8b1a21f64cded58ff2473": "S16-I", "2914a4ed19365e83fb31327c0fced6596cc70f58af5f11f7d93204a9125b6c17": "S16-J", "5cb6c919c706cb135634763241fbfa5fe61883fcefd831cb8771b8b12a2fda98": "S16-K", "253650ff6cedbe0a7059e341921480919ada10a80b524cccdd9e6c01c584eb7e": "S16-L", "bb34f12cb635fe08423a6e956d0cfb06c0c805c136c0272409bccda34f814ae6": "S16v0"};
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
