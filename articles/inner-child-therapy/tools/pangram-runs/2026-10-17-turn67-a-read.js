const want = {"e0ced6eb0d5b6a8c2f833fdfa8fd04c706d88d2f1b8f1979a43bb2673620f11c": "t67a_ks4a", "18192aad2dfabc7b0d705ffe54929b3ad1271d15f62c31f66286db36a9d461ce": "t67a_ks4b", "df3f66c4382041069f58a62d2b8401ac1b3e5492e505a36765b1b2eb9281c918": "t67a_ks4c", "7ec364b31fbb87b9cb1287bce61282cbae26ffbf53cacdd77a1330c69795eca7": "t67a_ks4d", "e90d46352ddce361552eb272f628f87a63ca23a49b225a019ea4e061f79a0e0c": "t67a_ks4e", "de4abf3e9a34978b40b273c29f5b5105fc9d1b75f7db53ad1e0077d988e7ce69": "t67a_le2a2", "f89bed12d9b2928bd7519fc728a3a4183602543c37ae79de4c13eec9e7c9cfab": "t67a_le2b", "7ce28fc006114055556b25f20fcaf5c75741952836894ca703f7234d6e380682": "t67a_le2c", "d9e1b6e312cf16fd67481087aed80c427d95becc03b8c28c8c68a462d0e36d08": "t67a_le2d2", "7f68b07796f24b93396ce6a20b2ae80a47eff6d9ccada78bad1252ec754b53f7": "t67a_le3a", "db372acef23aaab293ac9cd0ff34da5215c9d21068b8cec827841f6a500c17d5": "t67a_le3aa", "0815509b079eb130554dfb5b43b2e7cb227a5261f8b3dcd4485a04a75d8ce794": "t67a_le3ba", "bcff7eb61cad9bbf46c4519029361404e2cdcf170b56ab068cfa209a1e0a0a13": "t67a_le3ab2", "66292337505f11100462257504f6d94fd3f6bb45130e72465e351d85d9a9c4a7": "t67a_le3bb", "1c6cd4f325797bcfb66112c54a1fa86ddfff506bfa4463aa20e4f19115cd669e": "t67a_secba9", "f1c458169b853a475c14d6189e8d9711271561f46d816d8cf54359bfb9b45373": "t67a_secba8", "ca021186c8787f99bed4a9c46a08f4a65d56650019c2c421c082ec2e428811d6": "t67a_seclm4", "b17a739b8082997c8c67476c061ba7bd3d1504bdd9a8642284ce20f2221c8c56": "t67a_seclove", "6c08e477b96be9503dadbc79e358c1abb0219a32e156dbc3fe4c04676fe44052": "t67a_sectiming", "d94c6399aa0145aba4c2851a1ca41dec2150e16eeb7769b0792446bc0d3bed9b": "t67a_secguide", "3d239ad892b753c3b374238093bbf777c20b17bd01aa49c5716562e4bc7b9831": "t67a_photop2", "dde6491d41dbbd2462a62e958863056550ce4cd18c2e9f6f328e555d61169b29": "t67a_secphotos", "900052e6f7afdc87f086f145760c13f33d683b04cd02d88226f29e45ab72755d": "t67a_secsp"};
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
