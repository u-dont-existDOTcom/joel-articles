const want = {"d9688f79447f3157d0ddd9b293b5039426a30c1593fea0dad3dc0b5fe2d0c669": "t65z17_fg1p1w5p1", "33d409863788ecb29b5fe3fbe3b0b70c692029a6001f75cb04992ccb740902d3": "t65z17_fg1p3w6p1", "ecf2c7444fb9067207caf6d39cc1c5ac2c11f05d3f04a438bc52f889cd684845": "t65z17_st1p5vw2p1", "7a939e92d70ee7ac2247337d5a9dec70e4ac313c35a483055a70d2d52914de1a": "t65z17_st1p5vw2p2", "bdddc06f69421adc00766102af10f0a273d6c73cdc252d5e3e757ae864af6ceb": "t65z17_st1p5vw2p3", "f035b241992e6a7334a4c1b37461fa46ed65ecbf9156e73091472d1226c9cb17": "t65z17_le1p2vw1p1", "8b689f41a23676b3ceb59edc96dae5e3926e90a25819babeea3bbb57e3d34478": "t65z17_le1p2vw1p2", "cdb5fff1793775b768678b4644813632f1fa9f2cb702a73dfa0257a4e6684555": "t65z17_le1p2vw1p3", "0bbbaef55128dc61b14f47f35811eaa05b9b1f3405da02f4b8c432a5a09a8314": "t65z17_le1p2vw2p1", "ad167b1cc2d97d5cf38f9e1c294c794feb2e2686e9e7deea968d591a250cd2fc": "t65z17_le1p2vw2p2", "58f2c80175ce1c1d747c5cdd1f28ebe4e653fe5d3df00235891237171c5f9057": "t65z17_le1p2vw2p3", "46c082dce8734cd3f8641ba50ed848ad3c1204017bb08dfa5d7183c4536f6dcf": "t65z17_le1p3vw1p1", "4cf2988c28a1f756690e767e96cd492a2c0901204182dfe237a4d4c4c9f13799": "t65z17_le1p3vw1p2", "4399569445f901627939d060c6151a281a2fd4f189b38db4aa07deed09d1d683": "t65z17_le1p3vw1p3", "a777029796ecb8f790ddc2478f4358e401ab04e2c072956b969520abf6f15ebb": "t65z17_le1p3vw2p1", "4369c07f8874c59ce169a76241a92558ccd15ad52d2c58e2792c9d83151e90d5": "t65z17_le1p3vw2p2", "d6c33b620bec5d142eb8250ac3c4bdb81323d33b9d7956d0556cb0b5064d00fe": "t65z17_le1p3vw2p3", "7cc1f47f59d78a6c6fadd6cf5b63d31336cd3f04857cc88af0262c08473bffc8": "t65z17_st1p2vw1p1", "bb80f4bc5b3da2ea0daaca57b34b8d0a3d44347d89600ca385a29324a5a78841": "t65z17_st1p2vw1p2", "6a731a42eab8d1aff51ee1da7d042bcdacb69066386399feb97afa3560223c4e": "t65z17_st1p2vw1p3", "c37430dad20a50c72f595aade87b37939b3f8a16b294e0b4a090b4b00de6c991": "t65z17_fg1p1vw1p1", "258a5fe40103ca73517bbeda89d0a39f985025ae4dbfeb73fe2d3e4e93731341": "t65z17_fg1p1vw1p2", "316b07a983eb5fd6890f406c1babfd0d09a3c035d20f265ccea4c44ba5d226ff": "t65z17_fg1p1vw1p3", "f51f5bbb467395de96ffe57a25b7f930ca5a95c7a5f9d411c79b651e62a825ad": "t65z17_fg1p1vw2p1", "7b544d283d51ad508a0e6ada10b4af79e5d5155475ac57a7403283043a93e638": "t65z17_fg1p1vw2p2", "c8c0a60176d8d5f80d6c4f0dfc7625eb96bb96ab695a48da85dafb6d10d982ae": "t65z17_fg1p1vw2p3", "36dedbe6b17977ef04e9da9b6578cef2c1deeb819f2cd674740855c759bb595e": "t65z17_st1p1vw1p1", "4c8b6992110a06036566f15e49b207ca9ac5cf4da8139e6bc4077a592b1b6416": "t65z17_st1p1vw1p2", "b0b422622a662f38d9755a783f14c8f53ff8fbd934b1686b9f5d20239cc5b8e8": "t65z17_st1p1vw1p3", "c5014db7da6b1b743b8b2784fcda1a274226b9d104c0973dbe3a3f3d23c10afa": "t65z17_st1p6vw1p1", "24c6a3f8727cf1671e1fad77eae0a9ca1ee293ccaec9f3c022e077a0470f9342": "t65z17_st1p6vw1p2", "f62e7b88680fa599f729509fd1b73bf2a5db9f67ab1acda26106e3842a64c682": "t65z17_st1p6vw1p3"};
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
