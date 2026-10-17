const want = {"9950f686fe5444dc2bd9379e2abb36968cfce0c46559290182e2617510856ff3": "S13v32-H1-P4", "c599d01d0b5f9005f9862ecbf5717e0f703983f5df3aff7a321baa16fb5b4391": "S13v32-H3-P3", "53fa40c56b74dc8d447f64439a75fcac644c28c6f655d2e959d166e4b225b5ff": "S13v32-H3-P4", "f4912683eb46a76e32878e5690bd4264a081d9722ee521cd6ec95973c3c6121a": "S13v32-H3-P4+P5", "348d6c93ba0ec9f22710f960a9c522aba64294d6af4f288b48bca5745693945e": "S13v32-H4-P1", "c7f310cbfc8b9dcd874fdd6bfc972c5edfc229a78b9c95eff4a58e2487bca288": "S13v32-H4-P2+P3", "ddfabf2c433d06e97d445ad58e21f3b259422212b8be48666caf61f61e65ecfe": "S13v32-H4-P3+P4", "18c547e82360b96dfb4bd7cf8c64e918a7b0480a45fb1dccdbb9a5f36265d2ce": "S13v32-H4-P4", "2165b097ffbb1ac0b0708f67856cad494f409e6367cb4ee7d69ee8450abdd3b4": "S13v32-H1", "180d9dfeebe828184f4011edc4dd06452830795abc465d6501a2ce9e20b4a350": "S13v32-H3", "b03c06c8e71e5ce6f9cf3ed98ef766bab824aea80beded03d833be2375494e10": "S13v32-H4", "e32fa1225cdb0b64aaa4bf441cd8bec4bf1662a89e98360e0362cfa8bbb0e321": "S13v32"};
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
