const want = {"a476d703238bbb5d978a23d8e0d91b3a35fd9a1deacc138f46731b4dbba28bd3": "S16v14-H2-P3-P5", "1cecc41856510a31bd73cebf746dcbd7d6c7269a682322f43b311861a321b98e": "S16v14-H2-P4-P6", "f3551645629265fde923e080ac3c2a03f8d5fb3fb2cb6268ccfed29a0942d48e": "S16v14-H2-P5-H3-P2", "435c152d37ec4bf8e40351e99ebce582483ee2fa95e8f9820ac7116bf5a6ab28": "S16v14-H2-P6-H3-P3", "4d98919d494c01a883fee8409a33852efb5a54f0860d7b20a0ec12159f3563da": "S16v14-H3-P2-P4", "75b8181970445df08ded2eae7ec03c632593e6a5451bcc4ddaede36088d95a25": "S16v14-H3-P3-P5", "958352a92d3fa4fb4df4e39ea4fb370d02e19bd2ba5b7c6f0fc0b293426dbc05": "S16v14-H3-P4-P6", "935a328d05109207505c1011bcbfb75e375270ebf31a22294fe2619d1aaa67e7": "S16v14-H2-P5", "b069bdbecfcefec167e14f988c84285909a78f8c93936233dcf9926b95715844": "S16v14-H2-P4+P5", "80eeffe8e136e59cff57eb62df3f04782eb7c922d6bb4ea8c09f6510025f75c3": "S16v14-H2-P5+P6", "3f124c61494f041cbd794e1b852200f1aa86c21fab880872dd549e4dd0c56559": "S16v14-H3-P2+P3", "3d3fbecb3da499d3ef5fa6520b95198a3d9a3902d11a801ca30661136a4a1024": "S16v14-H3-P3", "d694f889100986337e5721cf5b11d66707d9834cd230b4012f2a706664a1f295": "S16v14-H3-P3+P4", "ca32c279359554d0bc981b2638fa8c6a365fe51da65f13a694e401e56410bf89": "S16v14-H3-P4+P5", "ee0eca64cbaa983022db305dfc0528b89376f028ab974e9346f946f6dd6c5033": "S16v14"};
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
