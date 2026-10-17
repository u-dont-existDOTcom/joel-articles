const want = {"d42b97d6827e1465e630330ea9b729104ca75002f0128517cad791ac7cf20c97": "t67c_ks4g", "af71ae467f326d63802224905172fbce0a220cd4d2352c9fd457dadea3537438": "t67c_ks4k", "41507720c6509f397c3459cd873937197dc19bed09d32c1d55295cbfd724ac72": "t67c_ks4l", "c1e4869b010411f7bbaad92ac7d7f09785e7e980d6fe5155c6570ffff2e67722": "t67c_ks4be1", "eecb5cc0d56f3926e25883830e65fea1de791dd82163332031e3e5e3e6bc3d46": "t67c_ks5e1", "e6cba5886034397d2c6187f1996c19b5b3f90a1bc6abf63ac3c90b43879d6f01": "t67c_lm4p1j1", "001ec369a23e89caafeb662643cd6185aea0f2cb6dd7154f974fd614094c0a1e": "t67c_lm4p1j2", "c1db88a37a3d03c7e0d118fb7b88bd07ba00759fa5d6e94bf29e0120ed600a80": "t67c_le2h", "a74052626b466a98ad2500bb3027815ea5137f52bb8e3516f7ddd2d61ce97b9b": "t67c_le2i", "248dc57e17a62f5e65fd7844c04fd2bfc53f3481096b248a6b387074c5dd9846": "t67c_le3ag", "02562f386f975e4e763c0013f7eb87d201765667f719f27211ed40bd064defed": "t67c_le3ah", "de5fa356dcafc8943aebce1b023111951ffd101f3c1c7b2cf53ee2c5c761967d": "t67c_secksa2e", "dbbcd54d1c23022a5da5ee4ae63ae5bac182812c620faa2ecbc1772d994ec7ab": "t67c_secksge", "1d5f4e7ca1ae5e906335d96e15df038254d859fe076f6faceeeb5cb5d5209975": "t67c_seckske", "c83919ecef2df36293ab54a53db4b5625eaa59a31df190f6fcea8c094230648e": "t67c_secksle", "9be7ecb7fb86a2845d2ab1fdc67b8db613b0b4429fe9474f0ca8a9793f680873": "t67c_seclm4j1", "87d7ed7e5d8540dd2dd7fb01c4b1ff887a5f325e329c83545183ca8bcceaf427": "t67c_seclm4j2", "06217ede7050f9f00ab407547729c43d1c752a81b965a79482df02ff609123a8": "t67c_seclm4nop1"};
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
