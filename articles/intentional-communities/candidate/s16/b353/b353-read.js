const want = {"b18567dd0e6e2d80348f706af5178c7c497d3e1546f6816a8fb33161e2405a0c": "S16v15w-H2-P5-H3-P2", "fd54b7ca8fc4e958843aba0032139dfc885be0d6236e95ee9db7403ff7f073fb": "S16v15w-H2-P6-H3-P3", "96e078c73acc25fb9873364d042bb52f100e4e6cf14edd0c87852d982a7eac2c": "S16v15w-H3-P2-P4", "d8a44e17b9521dfa9e7ea3ff79bcc2d1bcf77e3edaeb0956defcec7ddca09ce9": "S16v15w-H3-P3-P5", "3b694c9c53d53802feeb9ed743183d8544c3ea6f3c1b1b8d896300bfcc1277db": "S16v15w-H3-P4-P6", "9725d77d387b277f93a5914b9f409d16b46313970169e10cf45b062fb8cd2a58": "S16v15w-H3-P2+P3", "ccba73fd510408c901b6e626b5bd2454dc7a76bfc600d257c649951a5e249f9e": "S16v15w-H3-P3", "59863f434bdd15f5cb24c8a8a2ec1a2ec92e4f109d6500f3e6a236b88e212499": "S16v15w-H3-P3+P4", "30c9b167a5510ee31cc3d8e26725a1c0988cad4d2306374fcc34edc469c36f56": "S16v15w-H3-P4", "f27f01e351754762875553813019ed7d2f91c32e94838fe9b3a01c095f9e3166": "S16v15w-H3-P4+P5", "a37a85a9f31b5d1bd69dc49b632d42cfd639f41c5d897af2ac756b100e52cb57": "S16v15w"};
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
