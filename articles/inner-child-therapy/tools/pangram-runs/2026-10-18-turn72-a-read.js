const want = {"cb949804389b3d6c0eaafc8e8db0cab1b0aba26848a381e234f000d60e0b3557": "t72a_par", "1eb1992d60de3ba6d25792f83f3865852f225d067d13603448e23451a84b8d9b": "t72a_tr", "3baf330fa747783a1290adf5faef05c6efc329687aa9709547ea165577991e27": "t72a_yb5", "48311a9aa4b963b696091847ebc7a279cac044a9a1332633b9d1d146536773fb": "t72a_bgout", "b3ccaf7ad9402e6298417e21dc55a702786e081a799690c427d130198dc3cf92": "t72a_bg3", "9c6ab26829530ff97b43c4f2af84a85c61430f4348b824c27c10dc8ebe5ab8bc": "t72a_dgchk", "69d81e8ac5aa19daed83c176327340a33d19a1dbee9058ec2501b098b0086f0e": "t72a_chkbeh", "3bdf398208572348aad2cd49419d817f13c7201a204af76a9bc1fcce07f56f49": "t72a_alodate", "3aa71f96e79520283e98c51378d441bae5b0fe35eb72db2b704c72f39105b43f": "t72a_ifshs", "78fbc6779c964182304381ad0253e2481b71e16fb938106a27f2b35ca9c7697e": "t72a_ifsguide", "3e7d758675bb8ed012e8431914df5753a0c7f37a19816a21a33b343fa33da3c1": "t72a_st", "8e5ddc7c32b5d1393cd679b8c4b38fc9d41b66e66555fccb10d1d953a38e99a3": "t72a_stb", "355a26224f52427e259179a0f3cf586b417d371cff23544aff5b98dbe4c249c5": "t72a_h1bg", "e959f0235d16d1c00609608f428f6b70bea7efc4ff0de557ebbe8456e3d34582": "t72a_h1wavf", "8e58a774c6ad38fb62fbe828882f0ba94dc28d3ffb641cff2f5c8556560ab120": "t72a_h1as", "fed821edb8cfbd24794ecb3e55bb30c0751b1d5fd304e26c48d1851ddb3a5f22": "t72a_h1app", "20466cec28d02ac1ddec1e461bcc9ed86fc4097782ce907cdd8f086870905616": "t72a_h1sp", "af8b4bce3bc8e0efec73d44884791c46a9e4d64c2ef433268b653ed8402f1393": "t72a_h1mj", "a9025a8cb5a5a025eb9b2d975548fc9e436dd63124ec0461c45d225815d4b458": "t72a_h1ce", "42f92e8a8cbb38e01e2247f5709e7a1d09d5daa370eae8e97cd85e039350b99c": "t72a_h1st"};
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
