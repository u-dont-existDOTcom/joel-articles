const want = {"d13c2ad3aa9805643ceab5b45631beadc5b128700fbbb0ad44c4693eb7289e15": "APXv5-E18-19", "0368202204df83bdcac14e1fd9a955d559597e7ab530a7e7378f368bba21a1ba": "APXv5-E25", "15269d5452236f13df118707fb0592466d926854e5b0f6e494e9f5b985585722": "APXv5", "f5bc9bfc6f27d6b63a18c4a483e95ac1af1dd599e1ed400548cee9a81a063cdd": "APXv5x-E18-19", "c50e6d6935d0771b225d47dd318fdc17dec4edf68acfa114cbd548cd33ed3217": "APXv5x-E25", "e08c39ff805f4f64bc73640ecffe26befbf50463cd162a61a65882fdd5816921": "APXv5x"};
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
