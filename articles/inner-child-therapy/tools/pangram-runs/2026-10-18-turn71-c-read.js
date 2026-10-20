const want = {"9cb1508801e4523eee84fb8d4d54aa36f70cd26d14891cfa417436118062d2b0": "t71c_as1a", "c34d9424c7f568b61a1cd6eaf6c88057a02b13b6e97e49e9cf6043e59dfe0db8": "t71c_as2a", "99731f6af9416244a3ad28fb35943fd28bcb721a641d8e9db8501ecdce95276b": "t71c_as3b", "044db296cc01aec13b2a726dbaa25182b80fbc07a6058773ca23aa1e79518a74": "t71c_as4a", "16ce042398c6dab11975f22be9c00593c38badb422186cf08a094dc0171f8394": "t71c_as5a", "8265406f8b69da5ffebe617f43ac34c48bd6c0b4235f68c54fc02fe006f81a81": "t71c_ar1j", "e44ae6f4f28a36d204f063ed17328ed30caa296c2a7d21fad395840331daa3cc": "t71c_ar2j", "3b850cb1790d1a903078f7b1cf562050be3c177cc3ab7db2193a12fde975aecd": "t71c_ar3j", "139d145e58d41d786314d5772a3d5ce126355a6a5f5dc8bd44a97c45ea959b99": "t71c_artra", "8bf9ec7cc9a1da7a5b27d066be538e1599f26844c21e199119a809dd70f51d98": "t71c_ar4j", "7ee62bd0f74d4954f6aea3c1719ccef07f248e7f8f2bca0e7819227d9bb99a67": "t71c_ar5j", "51653ad146a5c59a1aab94fb28ce1b7a59df62a4f531f16b9450a10d3fc7f1ca": "t71c_ar6g", "522f089149c6bc88c781ac4ff12b24ce293bdfa64da169c4d1de894d8c8a8cab": "t71c_ar7a", "e1ca09e8465bef1ff04ee6ff0df9b5a74fa656c24ba79e168b3169ba5a6f90c5": "t71c_ar8a", "2e7490d1e7b039b03fe346b6a42691e516bd1baeccc56f60d19b1bff8c3fdf23": "t71c_ar9a", "5c125c77375d02ee562bd8a8658c7781eb23a63110d7c76d4962fde0c156dd6f": "t71c_an1g", "87d7727a4f8234cc25f07b52eec0cdcb200a2265f1c231959a947c387bb0afae": "t71c_secan", "d7020fab8a3f44daa1948d2a6711d149ec3d9566e8fdd9f25de3fc6925685a36": "t71c_secar", "b1e6589414e0027619d4ad3da23027e8a4f2bf33a34f4e2c306869d596533c7d": "t71c_secas", "074dbab366eb5773e9b433a27415fbd0b9d9ab473a58e56a781b02383107a409": "t71c_secsp5x3c"};
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
