const want = {"2a9a9dbb505fc5af9944b6ea15873e2a62cd31a8670b8b90e292591f768771da": "HG17-refix2", "41723ba3adaa335c5023e3ac8101fbb3c1b2ca64aac92fd889c8fb068fbc5c18": "HG31-refix2", "b836a7b777f100d59837f26695dc0c363d8da3278fad7d434422f847f156a4ed": "HG37-refix2", "5327c257a77d37f4ca23b8a0f70a0e09bd517ac4cc7e2eaf94ab6ccb169af867": "HG13-rfix", "799dad8dd8ee8df070bd843c9629fde8af6b474b8a9ccb693369003d880cc590": "HG19-rfix", "6a23a6b3331bf6e4eb422400f36d6a31e31a86461a51d337b462a11089fb1390": "HG20-rfix", "0079974ba6ecb011c547678362a072235bd7157160c3a6866e47e146ea1cf113": "HG22-rfix", "ecf9cdefd7e679ddb8519165711240ea5e06a08514f99f9659df7abb16a49736": "HG25-rfix", "ea65bda234e04fff15bb0b3fcc2c30030f8e095ba7d271d92e4632330c533154": "HG26-rfix", "7752c24dc0242d1fb3deb5327dc3506bba58f2cb201f35b7ae82773c20318f81": "HG40-rfix", "82767c02714b8106c4db95848d6b203493b6dbf1cf8871edf5ae80b1bac09d3a": "HG29+30-rfix", "bf4062b1d18ad2949daf033b7d64007150e93005d35d7537a6d3b413bf752622": "HG36-rfix"};
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
