const want = {"30e5a354b86bfdcbef5e439c084f53799d44603ee6eaca4bcf16e5b154fa7726": "J4-P11d", "fdbc2097f93078c6b4a79a949b6b8dc5f19ea4e3f3ba1a01184080ba7f2f40eb": "J4-P11dP12d", "908fe4de90f0f18001be3ad76ec0bdf39898860febe8e6da0b2b31d7d02b6422": "S4v113", "c204a8116689149aed20507a8836562f3fc9d3d3622311e69ee3d98ce9b152f2": "S13v5-1P1P2", "5c466496c9197ec7a90e35864868367bfb2a58090dc68c1e2fdec2668861152b": "S13v5-1P2", "f1a627804335be9f3730a3e018c48542ad11f7e5228a051e4fa9c7a85e19f9e9": "S13v5-1P3", "b9e7d2960b81ebb8fbcecd2aa4273737a317a384bbeaa80ca1a9487d2dc7f95e": "S13v5-3P2", "3c7d5586dd18ed543b2a072caf92c2367be0f97bb5f6e5abd256bff615858943": "S13v5-3P3", "2b4943330a8dd47da1c075583cd0fde0d93fb86ad24d03e761bd34603cfe535a": "S13v5-3P4", "bc98a8b7d38040588b1d6220d4d116c11f3bf676089c1edc1036f01557f147ed": "S13v5-4P6P7", "a1c5e0ebd8b2755bc006fa66e26907db2b3248dd788d49e33095387ac8e2e6a7": "S13v5-4P7", "a79b5df784acd0f62e0b982f3618bb35f7903f59ddd8a683878e03b008cab7c9": "S13v5-4P8", "af72d8f5e5ddc62d99be64aecb0b6d76062cf3ca8293c99ba717ccf3861697ec": "S13v5-5P3"};
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
