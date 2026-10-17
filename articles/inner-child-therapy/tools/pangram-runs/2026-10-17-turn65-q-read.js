const want = {"043ee508e6a3fc7a0e6df3a5f195ced9e4b642d402e3aa913d67d276025fa87a": "t65q_sp1p2e3", "d8ddf337465053353448671d47d279b9fedf910cfed1b711dd3e4f417ac3606d": "t65q_sp1p2e7", "8dcecc7d1d75ada7e880b7216f5d03d2d2675c10c32a0486a8c9549fde825b0e": "t65q_sp1p2e8", "fdcc0658cbb7d7c104f69baaf0331312e211f6600339c4ef3d634541f100f94a": "t65q_secsp1p2e3", "91db85dcd36ae861bd6433027342eb95aded39d9f19ba47e5a0fe5d409bf68ff": "t65q_secsp1p2e7", "0716d94a0f23726e3342bfc7227271681867ccc7b9832e12c294420a9fbde7a4": "t65q_secsp1p2e8", "d7380c68b719640919b3e830c7d18b9041f27f56cab0073d59d323d24ada8cae": "t65q_sp2f", "640165ce0e0107fb3aad02a803fe2199a8c5abe8def77687c0cde831de8f5b63": "t65q_sp2h", "02b7a41099ee4ac4ecb831dd80483f27b766c204c0483c814ef6e02e245d6cf4": "t65q_secsp2f", "5c444a7a278449f94e10d75e18e0beaa5ae6b6b440f0b691091c7937a9b4c369": "t65q_secsp2h", "ef20cac10903eef985f2fba87a6726389244d7a257b3c4dda992292a946ba06d": "t65q_sp3p2a2", "b6812972a7f4db1401903a058599804d2d4a8ea02f059e1e976d2371f67621d3": "t65q_sp3p2d", "5b7747f4c536fd1223687ec479b5c8eed60d3ae92cd66ec71ae0a986682bbb1f": "t65q_sp3p2e", "e00198cab1d9664fc77728a225a7d6ec9aaf1110a3e3c8838efd2ef5bca4b0a0": "t65q_secsp3p2a2", "0836fc544857827b08ecdca606b3fd106ce446de6218cf3bc35608a7b2029324": "t65q_secsp3p2d", "f9884ae6106a28f8f85263b2e8128b55cade9c2bb4139be21d3b44cf2d0c1769": "t65q_secsp3p2e"};
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
