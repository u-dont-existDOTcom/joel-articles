const want = {"dfb3378a8bb9f1f471f7e31152f7cd24bbed767c1f473cd4062663e10cde3240": "t59e_p8k1", "25c10428c119a6f583f129420b13083cc746c7a462d337a6df1971228c7c6396": "t59e_p8k3", "dd189df3963d7343e662e9f9e0b0e043e8b210e24a77bd83f68249bfb5307d5f": "t59e_p8k5", "0e74ee8d6e2c3672358a029fc25d4ea015a5294da10dab1b1808d4359682a1d8": "t59e_p8k1_g456", "be66986ce359aa728b2830e278b87c1ef7fe9b481f122dfd76ce99c59c539c4d": "t59e_p8k3_g456", "9102398edae41e164393aa3c9bd1f9014f7c71b639ba6cb3849e67bb86ea9240": "t59e_p8k5_g456"};
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
