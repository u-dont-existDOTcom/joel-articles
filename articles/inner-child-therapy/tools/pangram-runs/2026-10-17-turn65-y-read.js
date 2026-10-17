const want = {"db0030a57bd35a00275e28cff3da13f87ecd5f56a4988727f378f3e1830cdf87": "t65y_le1p2d", "f60f54c220d4a6cd485f51f5b5192485824caf7ed5d263c67b00aadb24ab48fa": "t65y_le1p2e", "b42678e5cb236afc0eef0859659d81a086d29f807172eafd8280665c51d3b24f": "t65y_le1p3d", "b7a1a5b3004d41f596ed69a09aa20aeb62f8151f832c245248741be9dd9109c3": "t65y_le1p4f", "afedd49773ed8031c5e1b4ab208ef34768a982a35ae1102311595c9d1db58106": "t65y_ks1p1d", "02410984cd76f00658e612d62170d495236659604528da805572d7c91f32f4a2": "t65y_ks1p1e", "ee90a7cc6e01247f9afc2e14bb73ddfaad8078131c35d8782adff5cece5bb47f": "t65y_ks1p2d", "652a2647ebd7437788a1260a8c836734675de63d3faa6399435a569239f0d854": "t65y_ks1p2e", "bb32c51179e8846fcff26bfdf1760aceb186d342b0505808bb06358eadb7aac9": "t65y_ks1p4c", "70f3d76ae122af70c28049916beda7352835219472398f2cfa9156fe1d84499b": "t65y_ks1p4d", "20b36aa59cebe777cf5132f6715acc389a259929ac0f652568a7d2f2c9095b11": "t65y_ks1p6c", "6294f9523ecc77320989406bfd780b9112058d261ff752d18c50966cdea95797": "t65y_ks1p6d", "06298336ae78b623336f515c35aec962433735529f7b4fca77c3df385c6c06c0": "t65y_fg1p2e", "6e28d93314ad2675cb827593aa5a021b1773a06ce35ab977c71de7f1a180f83e": "t65y_fg1p3ad", "335780a1818076717c9b7b3f20a6c748242296aed7e0fd05b3311f5df2515808": "t65y_fg1p4d", "7b051b040ccf94a4af7ea28b13d75ca9c58cc80c8791f4139a5d8a0b6be0fa1b": "t65y_ba1p1d", "c050213af4d9e031c840df39eb044c9ecde4cdbf69327295ba4228d1982d32b0": "t65y_ba1p2d", "76693632509a31e5615c966f6f57981a3a686055add36dd8843461b34ab44565": "t65y_sh1d", "e1aa7daf1c144c83ce65d26521dfb1b74cb5835ecd99bb74fd220a3cccf0b788": "t65y_secle1p2d", "77b322cca39f335112e5178ec0608e45208344d7afc40eca32fbadc7222df868": "t65y_secle1p2e", "e76249a1ef9fd9a8f9f2bfc5433bc96943924e05f0e51ce2bbe0ef4e8151ef6e": "t65y_secks1p1d", "2143a93a92ad102982ebd29ca5c2a2814d174764fb99b8803d92516161138c55": "t65y_secks1p1e", "d8f4b3c4a2c3e4e79334719d8b8376d4c61e6b162e400a9637a199b237a5cf15": "t65y_secba1p1d", "3379be18aa9c83e1e971f759b6175010dd4e01be036f3b436a0b44225c3bdba8": "t65y_secsh1d"};
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
