const want = {"f510d500a6c22082210b71ae41f8c4897234d164da7fc98861a6d219015027ea": "t58d_p5d", "cfa0b282a354aa0ef2a2b59484a9e3c0cc835d92292b671e75b7f37a49c860be": "t58d_p5e", "92a4921db2e1e0af0f273e834d9a07b7062afd8a87652cc79ab3864773f29e40": "t58d_p6d", "dd565e26c459672870d6ec277987a13854589551db3455d7a51497a136fc637b": "t58d_p6e", "93281c24a739606b2889c27dc9467e95bf62bcc8b21b5b772817455b361f9fcc": "t58d_p7d", "e77893356ed90c285d6bbf63082dd408c61fc4170362f8e95c056b7857c6e3e9": "t58d_p7e"};
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
