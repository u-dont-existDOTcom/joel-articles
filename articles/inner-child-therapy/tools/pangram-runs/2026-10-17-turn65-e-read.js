const want = {"1df7bd3428615fa750e659bc1f7b3745ef764d282450da3a90fc92c6841b308d": "t65e_p14a", "c9252400a64d931af44e282660d2eb197a6419e8eaa6829ba01903fcda6f769e": "t65e_p14b", "adcb97a93451140de4f585526819cf83d9c1f172b8b7e677738fcfaaceb9b14f": "t65e_p14c", "fa612c32272c91d8a4293ce8d217796aa65cceec66d12bc793aafb80c2d4677f": "t65e_p14d", "e4136e47055b20a3d7da6e20bb9d344ede30061f6c7e086c5782f986b9d659fc": "t65e_pairp14a", "85e511b102d5d73e427391a5dd688a08d222652089d9d3ea6e156ab8037e3d13": "t65e_pairp14b", "324a0b0b4fc7c5a329f7a99b64637d09cb1d9df4ec8c93cf679842aabd47e0a5": "t65e_pairp14c", "e4fb372928c0848ed95ec10189218e0f648ca582996b9cf0eeeb01445376fbf6": "t65e_pairp14d", "97300df4c7e27f5ad6b6076cb188d78bea09b4b807db89c8eeb4f93c671f7bb6": "t65e_secp14a", "e38ed42d546bc5db8effca868034b190f5bd40272064a0034aaf732a4f2b0878": "t65e_secp14b", "ee001445dd063800c3b0275191cb345f5cea1dda2eb0f52dfb0995b013694e18": "t65e_secp14c", "45f3241744bb1e8a87348c518ee1c947481a849d4afa91f1d59e6cfc31ca8966": "t65e_secp14d"};
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
