const want = {"d85ae65e9d466b8af792b0a44b5d33f2c0f17c7396d37115e211f150598c5eba": "S14v3-1P12", "1a5c5fe1140ddf305fba0aae959edf43c20e05f3601c9bac95f26d132d8e5572": "S14v3-P2", "70eac0dbc90eac696898b3da43071289a6ee5b4ba438cad20d9065e0dc57ff0b": "S14v3-P5", "cb55cced2415527bf032dc1566a683d89b4dfc274130c1756659f649226ee75c": "S14v3W1-P67", "e2a212618ba87e291122db628f7f7a3dc086142bebf2738edd4184b42fd62b6a": "S14v3W1-P567", "992cb94445039ffea8b9db596177284f6527ccde11dc6c62d3f3534fdcfa737d": "S14v3W1", "e47e36c18f5adcbd757e1bc03f7f38a40176f28e2cc453ab73943dd7b63d4866": "S14v3W2-P67", "efc932a23e6d2030374a48756556821ab0a69305993aa577e7541caad585e42c": "S14v3W2-P567", "3c9dbae916decc80c2af3945faab5dae92ad3f04257a880b7d404d79d0d6cf60": "S14v3W2", "1381c9634791b29ffb0fd6c540ad8b039deb4b9a469a6761a093fcf5ced5ab17": "S14v3W3-P67", "8258bea83a9dd0c2490496303903fd4aded2c9576b2e672f39b946e5297ad239": "S14v3W3-P567", "d5938e8de5b83d04ef846c0f5b6890655a994c0451c0e9d8e261da5235efaa11": "S14v3W3", "695bbff272404cc5b153e3965462e57195afdc804bc8320555a0975cc10b3d5e": "S14v3W5-P67", "e846d4eaae2fa833c0afd60715a9b5150d3b94c7e722f5701cb6c8e41c125f19": "S14v3W5-P567", "bc11b4e54320db99796ae622edd870c46bec96c622308e83e72229cab8e79452": "S14v3W5"};
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
