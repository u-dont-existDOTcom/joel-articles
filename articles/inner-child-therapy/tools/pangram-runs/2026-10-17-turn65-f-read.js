const want = {"63a80540a98972e805f81a7a32b9ec3433cd730928e673181458930beba57aee": "t65f_p14e", "35ee9513591a376a34ab352298617d5a3628ed315a4f2eac1a3f8b9d70c60c6e": "t65f_p14f", "3fc3ec4262577d44cd66499da6c3dd69693956e8f763aaa0692190340ac4092c": "t65f_p14g", "0087cd67ff09197232d5c9f2565c8128129290d5e4b5d9b9cfefa87f48e7732a": "t65f_p14h", "83b80dd6fc6d80bfb54e8437d9f80aa4dbc1063da09f497b449ba5b85f23c024": "t65f_pairp14e", "758851daba291c2a22fda93fb195104e286f12d1b480c884569e6601f56ca252": "t65f_pairp14f", "9094ae79542ad35e70dcf73b404402d0f292cee0839fa0518865a3f659a8c8ae": "t65f_pairp14g", "6b2f5673db871ad091bd526ddfd38f4cd2847f0b02a4074d02ab216c2182ed73": "t65f_pairp14h", "c84a2b698e863fb1d2b3cb5c2163f907b3965d23f273fb5d18ac21d8926d6425": "t65f_secp14e", "d3027e4902623d055f455b2fcc9a0b623027e7a0851fde19ed35c1a7f7eecd30": "t65f_secp14f", "70f7070e36160dad044386d2fb43fdd01909cf422afb4e8361a0b1f8f73f6a27": "t65f_secp14g", "b472774d043ecc7d9a53cc61cabdf2af631d3bb1b71257927704ab0fbdde4cc6": "t65f_secp14h"};
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
