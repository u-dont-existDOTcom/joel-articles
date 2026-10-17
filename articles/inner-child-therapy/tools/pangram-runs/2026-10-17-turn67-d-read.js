const want = {"d92aa4f18b0b26f3780d272ae266f4e078788fed1c537eab107489a28d6f4cac": "t67d_ks4m", "1627fb6ef2ab3f19712b3ea952604eedafdefa325f12e756ccae155c71582d85": "t67d_ks4n", "93f702f3a15c2321feaa7e23cb9c567426ad7117e91f9bf4f345ea5df255a619": "t67d_ks4o", "4f1beb4d0e73f43c6f649b579be8b4531b915d5ac5bfa18c17041458403b93c1": "t67d_ks4p", "cc9cea045daeae907c19a2270fc119ed457f45987e495b01ca771d8f286c7ed0": "t67d_lm4p1j3", "7ad74403b7890a7e23ea6cb098511546fa2c34326720c7fccd73ce3252d6277f": "t67d_lm4p1j4", "e52cfff643c9337cb584629e3e8b37c525cd6254acce2ae0a083deedccc1b5be": "t67d_le2f1c", "45c70b45933c921970f6d556cbf82b4e96b6e4f4c023a58d7ed94583ff509d1e": "t67d_le2f2c", "1ad309a32e58c08326b0aeab4d678e4f2a266d3166afce03ccf1b8fce471efe8": "t67d_le2f2d", "06e94fb6db9a7186ca0875fc64b3e91bc531b37ff98378c695266086dee9aba2": "t67d_le3aj", "fc509f840b0a5fcd5b730802bcb679dc216836f927fa57f4291adf01d70d22e8": "t67d_secksme", "42df926bbac8928a0659dbf8f775fa54847cbca7e7427ea583785ca639c8b04f": "t67d_secksne", "d0831b66c8e79c03116a8d2f886ccabbd3c9ab480cbd665435044322975876cf": "t67d_secksoe", "3ce41fdbc35ea79e0ba41257f91450e6368dd4d029c6f9438f8e0cae1d489dbe": "t67d_seckspe", "bf9aeff5e966067de123f3404afe3647c2a82620350ead091616b86ae470e01e": "t67d_seclm4j3", "362c3938abb2f0dd6cc316034c24db3331f2df315ccee01445d57f16ad9e0d41": "t67d_seclm4j4", "d3039b6dcdd78c40aa5115ab323f8fdcfe89b34d0055cd77dc05d12758bf7043": "t67d_seclovej3", "83837ca023306d20594f57381278b1237cae4b8b27f1f90d48ded6e24fcaa58b": "t67d_seclovej4"};
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
