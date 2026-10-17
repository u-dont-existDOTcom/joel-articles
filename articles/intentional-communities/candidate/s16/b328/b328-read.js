const want = {"690254d8f2d8a064784c6aea2f9ad2580d9009b6c261c0b3e954bc7a8873a460": "S16v4-H1-P1+P2", "6f2033673e6b6505bbc188facf75c2f3e3388af1513f97436b754b38faf4a6d9": "S16v4-H1-P2+P3", "ddb54a946ae7e04ddcbd2b28501a861cc103d8b94eec35f48096d91f25ac5b11": "S16v4-H1-P3", "4c34430a3d50cd088a8b4d5db652421890265fa2870724023867c398b431f75d": "S16v4-H2-P1", "1ca37adf90ce8e240f08eb6419eb1e4ee3f2e59c11227acef610f9e6ca63fea0": "S16v4-H2-P1+P2", "4542f9e2921748358cb82bbc4d54925350d393e0970d4219cd1368b68e268832": "S16v4-H2-P2+P3", "e07b227030760080e11d99633efaa1aa96bd303a943c6083605bb72b64176f42": "S16v4-H2-P3+P4", "9f6fc90d44b285abca1177c6fefd69a695e704e973216ff57e6ce0e15aa5488c": "S16v4-H2-P4+P5", "332e3ac6dd025835ac4c4606f99b68e95b8198f2f6e23b465b4b82fa9bd7f4cb": "S16v4-H2-P5", "0cab0a962ee3d49fb6976b2d938c98b1695bf6f63b54f1fa3dc43e9017a2831d": "S16v4-H2-P5+P6", "5d1150f2b7821f586a86ca5ec687762c583f8a10c37586b4994a9be0b5c7bff8": "S16v4-H3-P2+P3", "0dd828475519572cbbe2c6480fec3fc5adc02bc0e2a7749d95e9e22433b487e7": "S16v4-H3-P3+P4", "9144df460fae3ffc077c7e1961c1303b291dcbdcfae4496278440e6c02779ce2": "S16v4-H3-P4+P5", "b67608319a7041fd460ea7c8782c4f542b697f1d862cf8e35f7ee8467e029cb2": "S16v4-H3-P5+P6", "ffe54f9a39849b490c49794c9f99ee648cd8f55fde0781cde8376f9e5c265ec8": "S16v4-H3-P6+P7", "c3bfd6e20d3563d11008c845a860893342d5627a8327f6b393dabde8e03e08c2": "S16v4-H3-P7+P8", "a8e3759dd2505b2c8d70115adc7e719938533e4d4da3af279bb562f4b2dc5bbb": "S16v4-H3-P8+P9", "ec6e8ff07f66575c8ef7f39f7a8d446613fbbd974cc2df5f5b85667bef85d944": "S16v4-H3-P10+P11", "95c3484fa884e6024f9333d164b25c07ea64dae6d6404d81041345a9815b8c45": "S16v4-H1", "a54753d11438f2e4ab5557e039be79cf20971f41ee490217d7492e40d57a4a6b": "S16v4-H2", "b16ad31e4f5042cb8945b20361cf1f3a308a14cf1d08d9974726396f936e276b": "S16v4-H3", "2417fea5bc44dc9d8a048df966a5ed7c89251344705ca2ca863a9cbf1eacc8ba": "S16v4"};
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
