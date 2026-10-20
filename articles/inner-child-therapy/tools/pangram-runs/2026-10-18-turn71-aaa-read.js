const want = {"0ca6a2103efd6263f8deb5f25f2c09925ae718456566e6f72e2093018d7fc388": "t71aaa_ifs1w", "b59803cf50a437c959712d41c829e6815c71ecfdc6a669806189e06fb56ac6f7": "t71aaa_ifs1x", "536260ac9c56e40b1814cecf54ccd99a3270a9bdd865b074fb2f12215c72c862": "t71aaa_ap56e", "63a248cf22731980c642fba11aee7b6485e5a39ba0fb4ee9660046a30068641f": "t71aaa_ifs5bb", "a9a9fbd134f518ff00060cd1b05e3acc6b35376d9b80226c1e80cad300b9fe9a": "t71aaa_ifs5cc", "e7769e1cbbb90aef74e171a5dba2402f118efd975febe3b969525fbce2c3b323": "t71aaa_secifsbb", "de9f959fde782bfa2a6984c49cc6dfe293e27e5732b75aebad2c6c70e5508cd7": "t71aaa_secifscc"};
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
