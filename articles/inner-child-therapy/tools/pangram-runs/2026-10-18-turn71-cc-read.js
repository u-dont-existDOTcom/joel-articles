const want = {"f9d8c91f5b78fccb52c6f8387d3a196682ade6349cc7a7f5412cb304568e847b": "t71cc_jwm", "0e5b0ab5e93d3c83808a81c2bb49a1db4372b505b2bcd47144e08efc8bb5f20d": "t71cc_jwn", "0496819c0ffa2f1aeac8f3347a6713de3d5c027d349abc59f89e9e1ddb5b0b11": "t71cc_oir", "52b01c2ad21dbbe7d705384adf87d6e3d5fb4cc9caed67e001f183b1b0fb110e": "t71cc_ois", "756732119506695439ee6119c1978ddc5bfa3559167a667f2a9e7d976813ae88": "t71cc_secjwm", "3d19f0aeb340819886a9887fbac5cee0255118ff45b116be9826efa47df71adb": "t71cc_secjwn", "78e4f0ff36fec7b02d49c0aa8461ecd805f5fc52b032953229c3c9e5ac32f8c7": "t71cc_secoir", "03ebe0b6a14e571e208097a4db3b520c27ddaf68fc1d5274b70478e7584d802e": "t71cc_secois", "33c6df38cc3b59e9f00d7ebcb8582d7c6b84d3d8abb50871f66951f789ac6545": "t71cc_secspjl"};
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
