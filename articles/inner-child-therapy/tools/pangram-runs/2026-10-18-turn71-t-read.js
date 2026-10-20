const want = {"3d2dfb96fb1c580a2403b20ebd0a71bde53051e8c28cd07c18cbaa55359ed137": "t71t_cs1e", "c547937995bc37e84f823feabe6b00c3c59a088c28cc6fd45f27c36e172b907c": "t71t_cs1f", "af78824b101be9c1269c260b5d2025448621fc1c3416508d289ed39c711b8363": "t71t_as4m", "30d0efbd9471aaac8b020369a9bebace26dd7f5d28de79ddd1be89ac1dbb3a6c": "t71t_as5m", "7b42e842bd01995d9bea69f0d41b2097547b9092845ffb6fefd12b6c02e0b567": "t71t_seccse", "f671533ff54a3701720284f6b478b44bebbf226a11be797c4798722fb4a4f5d0": "t71t_seccsf", "a0e1babd19a593f02ef96fa1399a433b0441b79ddfeda083be4d202dae7b5b97": "t71t_secasm", "94b10dd94fb1d4286d0db582f74f4a692e4686d144e54e89001912d2fd3e880b": "t71t_secas4m", "96b18e0aa196d43b0e5f024c508740926e110a736456175f57f38556825733c6": "t71t_secas5m"};
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
