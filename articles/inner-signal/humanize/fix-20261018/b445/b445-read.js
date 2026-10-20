const want = {"f6306fd000768579bba773db1cac2bb63f511d1575ba050b33139b381057646b": "HG18-refix2", "a98811b89f765c29417326756800438f106cf22cca284b6ffc2f3076a5b44bdd": "HG23-refix2", "9c0160be85d1d026ba1d802664d1c0023478e340ca043227c2138337fa83feb7": "HG36-refix2", "8b89b50351b73000d702c2407fb81e01788eee6ac7282e6841398ac326c7fa49": "HG24-refix", "cf20e58bef185081a077425d8ee3b0cca3434a41fb95d316880d28976bcbdd00": "HG29+30-refix", "7582d276ad904961e13da497e27646d7505157439838175365c3380e3d9da731": "HG04-refix", "9abc074b14615cea08be5bbcf0bdbdaa56685a9350d8bdacad8c51d578f7ce6a": "HG04-s-p1+next", "34321fc16be7e1ed0fb81e71c612ebd164f62c02b45e0687677cc5ab4a283fb7": "HG04-s-p2", "2b1c9a589a2fbb87373b2406e1b1282e72e15d981088104f3f60b82c881e960d": "HG06-refix", "39b6531caf7f8e1218a01d0589983838abb2d4cbc4a2712838fdf917ed88aea4": "HG06-s-p3+prev", "40c713e35192e2aca07514123c00f26300c924b9dfd6b49f025a0c6a2325d36b": "HG06-s-p4+run", "b570ac31ce1140a442ca327124d3169310ab5151c26f64b7bdfe7e2b5e3369f2": "HG06-s-p5+next", "cb97eb547355a02b6f7c31fc7449f239489fd6776596ed6de14e7be248fee8dd": "HG06-s-p6"};
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
