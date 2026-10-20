const want = {"333ab347c90b8ebedfc6d7548e3dfe11353338bc969b32398ce690e15d9a414c": "HG14-emuC", "414f409d954d3a01f24c2f55353c3a5ea4e3c1716401c534f14f18ad4cceb28e": "HG17-emuC", "5b6b5b0d3ebbb926e8fd5e555ed92d4edd46b611f0514844335509ce5e950472": "HG20-emuC", "3b5582aeecd5fdcacfac3313eb0818ccb74ddc76fb2ef2e5f820a2e8dcd34208": "HG24-emuC", "50a01c1e825c084e7059633b86e627f61807e669c8c244ff8debd591c7b4f78f": "HG31-emuC", "55e937b75fe376aca1148bdbd037b2a59cd45dc2cbdec6f8785c49776c9c5d21": "HG35-emuC", "c64571caf9d578fcdfad64b10377898cca1309c6f3fd2001adbefd5c4be41c6f": "HG37-emuC", "c40d045b6840dbd011d48169d9238f981d2dce43d5ec7e3f062091d7722b43d6": "HG38+39-emuC", "a986a61514ec22162a3e0870d4af9602c47e21fe5cc693dbd2c1458bfb4bf27a": "HG04-emuC", "59f5c02882b4c6ab864b11085166cf9aceb65d27e2afc77c8e42f9f6df06dfa3": "HG16-emuC", "fede0a7f3dfdd06d1e88944e8202ba6991ca06a1eea08a0c436832a1260bf461": "HG29+30-emuC"};
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
