const want = {"b7c946116b69c9a2037181e5f6f6dda2912b91daa83146cf2700c512d089529b": "S16v28-H1P3", "fde22f65106a2e8378d32fa47cb16e7833bc9d071f580d73316282bacef093e6": "S16v28-H1P3+prev", "c42149a03f20deed0b030b69e640549efa9bb8ac63ae0aaf238d1a585fc9f8a1": "S16v28-H3P7+prev", "c90e03dfd59c8fe84a7ea7494a63d350b541ef9364a3a89b3e7e068ed444070b": "S16v28-H3P7+next", "61c2ad90bca2ebb58ebb077d4fa9e20c537eba416002d45664f36ade69cc192b": "S15v13-H1P3", "d9fa7f642ed9edc9244aa9970107d60de35ef39cb7c51fb6cd2b0513eeac6d63": "S15v13-H1P3+prev", "e6fa0dba0d9469f28f15434d2620c5a5ab8935ae44189799e4ac8bd4112f9f45": "S15v13-H2P2", "3d89c1019f3974ff08809135ec0c03cf6b6c7e684da2e22ad0c217f6f9350d9c": "S15v13-H2P2+prev", "eded4637c0caafac0e4b8cb19e3c9b3ccda0027ffc2952c1b3bf1de44a1da1c8": "S15v13-H3P3", "c902d57306e1e8aea4ad4e6b4d4988d612680476da546c19d3e7e857146ea717": "S15v13-H3P5", "f07842492a525db9eaa099c24fccc1c821b27168ef7608ab3dbdf5b798593f27": "S4v114-container+prev", "6b90f4c309772f33c74b96e80f59c7e467630b5a36ec1555942768eeb1e8d3d0": "S4v114-container+next", "eba6eebf46baba4541ff8cb8e59257b07f6715946b8fb74634a116ee7e07178e": "S1sw-EastWind", "e90e71d7a922d26ade7bbc2cfdd4135a1f9be51fcdc8d6b1bcc7e9c4886d4af2": "S1sw-EastWind+prev", "c11f1e10dcc523ace1f8080c712f7387e8a2509b2f98c8a684ebada777748256": "S8v30-safeguards+prev", "f4464221ee16b31a4327129eb4b47103adcb919c460f86af94f64be9ec7e01fb": "S8v30-safeguards+next", "b42dddb3b30380eb19fc96344b6eaa5822e9413a3820076a7053b79dd4a9bdbf": "Q40-c-plus-often", "19e2cc248d1840ee45e2da94bc451c054d1fbbf4997e3a8a414085588fafc76d": "Q40-g-minus-often"};
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
