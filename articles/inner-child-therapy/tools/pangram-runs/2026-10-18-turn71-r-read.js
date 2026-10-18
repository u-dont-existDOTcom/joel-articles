const want = {"78ae93b80f747b0ec4117cfa5b66448a4d2f822c0c7fcd9b7c5ccfd5920cf757": "t71r_jl2h", "f5209a636044622da3cb81b079c022e14fd6fd8e09a71252b7afe1e619c54068": "t71r_jl2j", "4a2e96d120dfd0250fc6bbabf8edd15e28b54ddf3eb0a51350c80baa7e3b969c": "t71r_jl2k", "cb266f09951579cfe635e3002ff830b275f52deaa8739b0dc7927f3a4e5a05f1": "t71r_oio", "19fa71862c105754af5e55edcc1ad971a3b26e42b9fdb1c0ede96683ad68346a": "t71r_oip", "ef5a62534901ceb4f2f43df26ca75c8d8c23bc99fa51355b82db3d838d846ba3": "t71r_jwj", "f234d123054d9b06a79b5665aedb1d4d4292c6a875d56f538b88f12da706ba1a": "t71r_jwk", "852bca3393e0e3d962a1af321b4672968b97e7929c2ff5c86bcca136bbfa4b9f": "t71r_as3k", "0d0aea1128191048593a382482a17ca3ec57d6f692a1db429f252728e3b2fd73": "t71r_as4k", "af8bcf5bb2c92498059813c337813b9b4e2debd1498784440a0ec8fd64447f57": "t71r_as5k", "377353c2d308dd62fe213d2e3f54a430e4d5560566365d66245067d34f896f2d": "t71r_secjl6", "12abc17e3f2816222e5a43a49fe4510925ee18be7b4f4f03136ee02d40e8b3ca": "t71r_secjl7", "cce05b65bd321d1b889677395b1b504b609c48447c1657f7d1e0cccd69d9083f": "t71r_secjl8", "f26b38b613303c6d021970f11184d9bd595e43d1fe7e4b9eae9ea49e04575e64": "t71r_secoi4", "666c1bc8ac08b33844bf6d677a37f5e4e3ec71934bf37ebbf5e99e7da766fa00": "t71r_secoi5", "f30fbb273745f353d7916ee54538a8c5c6fb6e4775c178be41108175db99ff23": "t71r_secjw4", "724602a315a313cff50de6d688656f5770ea790544ee9a88aa8ae3067e07ed15": "t71r_secjw5", "d4b3840134361111b4b05507ac14ee66934390b68385fee53cb6a2ceb036a265": "t71r_astrik", "34ab04ba65ad4e4c43d5cab1492394e609ae398152af5a42e2deed7dd3fab324": "t71r_secask"};
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
