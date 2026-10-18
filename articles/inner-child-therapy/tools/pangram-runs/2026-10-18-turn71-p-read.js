const want = {"0b46da1063aef577cf640a7576e2b7eab89d8d21bef6ee914b5d14583f9166a0": "t71p_cs2p", "c9a5e3b3e63bc705b3e1ab519db445f6a8c58b20b51e52f4a7d549a0dac6b14f": "t71p_secsc8", "780c4906a85db031b9bd66800224143684205029ca4c49d2c8e068e1c3321417": "t71p_jl2g", "6edd3bf0a26baef3f2a9be05ac25ae7b863396b41bc536badea3fde87c1b8601": "t71p_secjl5", "d18a74db5868f43149cc8cf81839b10085116d7f9c706ee49492f2893c5e7ac2": "t71p_oin", "4d3072d9a70b6a9ebd4dd231e11afc9e759d793d95143e5e2892e46371d815b8": "t71p_secoi3", "95947783a343849d54c67b6f6e623afb97eaa39927b0109729b427e28e9bbd1c": "t71p_jwi", "4fad1ca825aa658e43cf68642623e646788be6aa3ee28948d3ffda3a6db3ef58": "t71p_secjw3", "f363b268acc5279de3c61f8812f86be391be54e6a70454a6864b9b7f363a971b": "t71p_secsp2"};
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
