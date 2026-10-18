const want = {"299f70595757ad5bd62e1bc059680b8981d83be958ec2cd90964c95d06de2493": "S13v35-OpeningP3+prev", "ded6d95706833cd79af314f5d440b8422797b1213462b9df07e7c22aa4600996": "S13v35-OpeningP3+next", "5d47599f13a434533b5c5d07f68a59b3a3a306916ba227ac763b5b4eef4c984d": "S13v35-OpeningP4", "0d06b9fe74a9ae0b8ac9c2641bb7a71c4989c96a635098d3d62572ea77ea15c1": "S13v35-ValuesP2", "5e27829ef9d32f2d6f06dbf6d3c3544003d0627b923ee79c9d71aa48e4601b52": "S13v35-ValuesP4+prev", "3b1cf9c32f203b3cf6f688a8c4201c13fc23c3538f45dd02d5690f751aa56e99": "S13v35-ValuesP4+next", "5983db65a3681cb11ee092d3fcf29f1bd7b7d55e52d8bc418ec111f997a04e62": "S13v35-ValuesP5", "df67b48d73867b7b699ead09e3d311d49303e1425fc9f661b04700c5cdb263d9": "S13v35-ResourcesP3", "f3af2fea933d6e0a5d7ad222f3197218a09f871ec7305fe91b0bd5b885dc782d": "S13v35-ResourcesP4", "5e5524557005c044587558831f0c12757f66275c6a43b973804470c642093b0d": "S13v35-ResourcesP4+next", "d187e3005e9956f1b93820aee83a523435849094ad9c51c5608c1957779cb89c": "S13v35-VisitortoMemberP2", "aba80af2f389ac798ab300c45d164ed8450bdcd3a5280741fd71710ef227c25a": "S13v35-VisitortoMemberP2+next", "68ea0dbf96ca03f1dc46a7b4d764d4039b9e89c224389ae6dda54b6e4edb7f3f": "S13v35-VisitortoMemberP3+next", "b3a94f1ab992dc102f71915ddef810ed034a51c3786eb24791a0090825920c00": "S13v35-VisitortoMemberP4", "15ea0f22e4864a245b0797c6a7cb1c12424b8fdee6dd855fd4f9f54cbd8c7f0d": "S13v35-VisitortoMemberP7", "a8af4de0cedebf18bbfe9067512c73d596d659645f540d653eb1d47b9f0e11b9": "S13v35-VisitortoMemberP8", "7445ffd80b2dd6cdeba1ef7b6eae33f8bb7449e99cf9e2fab030da0b44177de6": "S13v35-VisitortoMemberP9", "b80c36ac1f10dff8999ab2c1381b157c325dd4a7795352b21c22daa83d19c9da": "S13v35-WhenSomebodyHastoGoP3", "b5e99bab595402c9fba7f7158d308edd233b11db4c7f9284516a735b96c1e795": "S13v35"};
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
