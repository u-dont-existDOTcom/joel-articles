const want = {"c9f6b8bb18ed3c35acffb401f64d8461c681526694fba06beb3a1f5df8b3bc7c": "t71nn_jw2g", "247ce1bd43b1efdd259a14d5adae6626e1965bc4d2ca9bef76d8875f5e278a88": "t71nn_jw2h", "735608a422a69d32ee7f8fdfae24282159f7ee2f3c231a0edffa8eb958a5fdc4": "t71nn_jw2i", "2ade924a82f0eb5eec3ee9214575319b7f2115da4ff1a5950110267db41fd0c2": "t71nn_oix", "53fb600609ac4f89c8b12bc8a5f01ca3756975bcf4c67d5f4f1137763d9ae7d9": "t71nn_secjwsg", "5957b477cf3981d324a78b34aad9728e6bfc02681bf2fc8779be90ed02d395e3": "t71nn_secjwsh", "24a3f15fb63eaa66147942a8a8b52cd24e2df832d0bb4cf8a020c0763399306a": "t71nn_secjwsi", "b5da2e50aa544b13b72dbb985739de61b456e6f8ce7c51b7374ae1986de8fa66": "t71nn_secoix"};
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
