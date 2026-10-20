const want = {"c4e65bbd2aba76af86b0be8dd8a813cc80952e3650e7ba2c4ebdd78f6e4f4a09": "HG06-p1+next", "30dcfecf953ddd660cd3febb9240f538d5d4f2f39802a3e0936db3352c56b6d5": "HG06-p2", "67107c7f44a679ba57d38e49b1a7ed506bd673631eea45b0589e1ab6f05cb845": "HG06-p3+prev", "b1a308c3b0994d5a19c282e189a2aa6537a767d263b1e6f7dd7e1cfe33120bd8": "HG06-p4+run", "e5b7c04565b8a3a699ba2bf20d0763d392983086d77f998aaa9b52f0c632c5d2": "HG06-p5+next", "182ea7090844eab5850d4e9ba61db9d02554b3348a8906cfd3024d5d9d10b9ec": "HG06-p6", "cf1da13feec90434668a5beb9b1604977b672aa6ccd0f214ddc8f9bb5eb22b08": "HG07-p1+next", "00a95e1e1cdfe286a646feeac2d95e46814382ae50d9a0ac40d85467c2e4e69c": "HG07-p2", "3364bc9c391d428f24147f1822c9eaaedcaa9513a7b8cd26ac21cd928c84c322": "HG07-p3+prev", "af6d5b93dac1595e0478dabb97796bf5749d68f423bebee22a54d593319085b0": "HG01-p2", "f2b84adfff5c5cbb63303166042287fa1751c6949952e68f1718dd0826f821a1": "HG12-p1", "dfbda80eba40284e214e34281d17624868396012c31e6608b530b2ec585ea71e": "HG12-p2", "8c6c6ae9c3cac700aa172b53de2a6318bed215598a592f584a7abb5197bda235": "HG12-p3", "becd2d388ca7c7d40163844a66a04a84af10b392b39a5e4ff8da6b80b9bea428": "HG12-p4+next", "c9c10e2039ef7c218892851647c6040af5544ec778beac52182d82ea32bd8891": "HG12-p6", "b9ed352e5724d748e1efa7c78fadca2b4e003803298e55ac2f79f2c185ba57ab": "HG12-p7", "814f15ae2f4208ea2a50d87443ab21f476ebfa2021f211d823f6861fc8ec46eb": "HG12-p8+prev", "3b8e33412af7a7264b257b5b0d2bb8da70fbc6b03270cfd778abb1db8aaf3981": "HG04-p1+next", "b3b8e3991caab3357fa7f1927a757554eed2c50996a6cfcc4ac55a2867b18de1": "HG04-p2", "ba35a5fd0f170fe818b7a89282851411208cf52deaa6687117d8c75bd1970a45": "HG04-p3+next", "4871e701511865620d98fa5c1cce08b73e28e9775cf23392b8b1e5180a27641d": "HG04-p5", "af69e765847ecc19bcd64d25215d819d1dad6c53729f2ba4f8dbffa53367761d": "HG04-p6+prev", "7727885eeed2bed895e6bdd9dbf6f6a5b0f75f84f5a42fdc69a807df071becc0": "HG04-p7"};
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
