const want = {"38b828f0a711b8d1b881f24d5492f0f36ef6693d75199d19a022d8fa7ba05c2a": "b470-guard-first-read", "1218539f30cd78a0b14cdbfbaf3e4b7a2ea1018c865cbd2cf260b152fa4c3d63": "b470-three-jobs-named", "528ea216fa79582afdcc30abb2d25d2f5b22ece819be42ae421348e9d28521f4": "b470-guide-label", "294bddcc986d8effb091357bff0eae96c5c34dc0360afbb589d4d9138214a707": "b470-guide-work", "ed137ba17d1883e7dc3f336be7dbfa32a59655cd9d6db5eb505025cc0511b5dd": "b470-protector-parts-label", "5a2050b23a130cbc30c4fd35d09aaaf6cbee76c5b06cb063ed7a8621528d9616": "b470-guard-defined", "06c22a1e1379aa2d3ce20951c851323c4376fafb606b43ec1fc528bd0fc8ac5e": "b470-parent-script", "09f4472d5ed642ffc6640691e0598d428f72bab382de3798a5c871e7f9f76df5": "b470-to-the-part", "8ec49b119ef85526e39fb9a32a9c413e04c2e825f4c59355b028ffb47df43be5": "b470-talk-to-part", "69678a958bc8441f9811d78e8258bb0197dadbaf598eecfe92c5124b2ece4129": "b470-part-wants", "865d8348d2d585169f4179edd196382fb7203c3ca7caf0fa4c1acb4f7aa37029": "b470-script-humiliating", "946bdc0ae288a1a185fab2e6580ed1931299bc51ca4192b1c51d8c4d4b630cde": "b470-chemicals", "d7ac34b3d201f1a1276a126ab9f7ade84c13c150c87291ade5256584af40fd1a": "b470-guide-care", "57dfe1c2ba37211e71a4c300ab58401f8f24ec9855877d9befcebb149edbca31": "b470-script-fake", "c0427394a88f002d973b331992d8d78c132a7b9073004ea920fda7965465ed29": "b470-anxious-parts", "f8be44b21fa1f0e50b5f40178e91dd84dc478c3855787ea98c07145c3a6b2881": "b470-guide-stuck", "bb01eede78b3fb3801111ef0c0f1e3e28da8f92f0eb0e4d054e919e7adc95949": "b470-guide-proportion", "cb6c927fa60b29f34bdafcc322573986f400eeae55d670f6f93497e25f4332ee": "b470-synchronicity", "fe0e2cad8079b7021eaac735b3d7e1242bbe691f593cf803c0959c2e1adc39fb": "b470-guide-cue", "44e8772b580ee27e01793ebfb734c6f7986534a53fc7e36479b933b22e2fcef1": "b470-guide-reframe", "3f89d143d4e1a25e550932392c5f0ff2f7e12523f2be62567615d1813912db88": "b470-guide-nlp", "55a9cbea6c19fb33a2530166a172e25a26a67b3a0c7d474be690c7b15a03db06": "b470-anxiety-part", "57236bf62060e41d4fa1ea6a7bdadf0fbd32adcb2eab0479bab099c0fd553016": "b470-altered-part"};
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
