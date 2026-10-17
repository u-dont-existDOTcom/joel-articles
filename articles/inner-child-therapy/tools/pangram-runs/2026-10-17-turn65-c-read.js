const want = {"9bf57e37397e6c116c88aa1320759202465e805984bc8fd8fa09dd3129663ff8": "t65c_p13a", "cb5aa88a2cdf13dfd579be242d46a27c432cdefc17556855e298eb2d5f9141d4": "t65c_p13b", "55017cab15ad7984792f4b5c07ed648ec395c680ef9d3382892e68528d4f686f": "t65c_p13c", "7d53afab89bb19fca91f011a810fb9d2742a042d59a1dc6d92fc7841a404d2b8": "t65c_p13d", "e291a1ac7aba9ba11073742234f32a9d5f0dee9f6dbdbeda2b49bf479981e213": "t65c_pairp13a", "7a37f2d58e0c617ae29357bee4681e9e422ae50f9916e8ab41b3a89dafa2a736": "t65c_pairp13b", "48b93599a89a52e4a04527179ae461a3dedfe52166b8efe43b76ac0e929d8481": "t65c_pairp13c", "9cdf57bdccca3eb571dd4c4bc00e1b6585d908dcdf49afcc833b526014ba97b3": "t65c_pairp13d", "633551c9757b653436ba22e247b40eee6fc2e2dc2a26561f09a2cfd34f1a6910": "t65c_secp13a", "de03b2350e9353364180dcf38282f691b881c16c43fa352b820b6b1b28381a5e": "t65c_secp13b", "2ee79daeff294f42ec6fc0c73233dddd1b5ad6037e053406bbd316ab98080d42": "t65c_secp13c", "f879b242acd5aa74689173ce483e6b7ce1115a664676e93a14be93c631c90541": "t65c_secp13d"};
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
