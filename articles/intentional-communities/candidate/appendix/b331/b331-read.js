const want = {"f9034d976eaf155bb0796ad735e344d7c4b69fe6ed136455e4ffd8911c93f039": "APXv4-E01-03", "3736566c9afce51349b7f2f81a278607c651c702e464914a7642bb42ed04cf69": "APXv4-E04-06", "3bdde910dccfa0da6b238f7f9e5f19be5116c42fcfeda3b6a160ed646b327409": "APXv4-E07-09", "e93ae8437ad61ddd19eca522009f228b69c842e28df245a5a65727aa92886bc6": "APXv4-E10-11", "06f5a929390779ceb5bbc48d6fe12f2ca82e4e787e75ba06e22c3c923c9157e0": "APXv4-E13-15", "721d3b7c49fc6087e3db97685430d72016ea73bf51bc39f0b2a4e129847eacbe": "APXv4-E14-17", "0067d11b696b406602eb6f5efa0096d10e5ab69817a4cacfe95695daa3f7db43": "APXv4-E20-22", "f7a95d69344e65672465507e225ccbec425f006082d5ef589a01106c77fde182": "APXv4-E11-12", "82b642bc299bc6e9fa80d5e52a56935be428e8daeff3b5f8b09955eec69ec4a5": "APXv4-E18-19", "e456d67d90cc14d49911a479b6a0130adf55741a40148162db0a7dec35b23135": "APXv4-E19-20", "bccfece54f4f5c4a8976b2acbe1d306d35d64c0a19a315388f950e536d12f805": "APXv4-E23-24", "46879a6213fabaf8f7bdcbce74133e9c01c036ae31b71a4c3723b6326305f82a": "APXv4-E25", "745fd8454b04df53c6e0aaca90010094e70fe8cb170864fc4d563ac74772de50": "APXv4"};
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
