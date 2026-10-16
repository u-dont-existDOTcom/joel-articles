const want = {"7f5a05e25ad280f877e7ef5247f896ffd58ba8ee5c5d7e982e3dc412325acf7c": "S13v27-1P3P4", "a35c461be54de92d7539cfcdbdc9d86fa605af67b868187cd9d5f8e411af0142": "S13v27-H1", "e23788c691fe95627703c7f185033607857f6fe5bb068e08a059f92455a92cac": "S13v27-2P2P3", "e80267b87f652930e301e9c1bc64b847b7869dd8b697492c2b508f1ea69e9bb1": "S13v27-2P3bP4", "3bf6bfb0b1bacbd7ee6e6295d1d555cfa7094d4112b12f92b91526239023580a": "S13v27-H2", "aafeff49c8f0f564dcd330aa7b9eb07e55e55a8670829226bd65df204e2f762b": "S13v27-J1", "76c99912faf176462493fbfc51bd10bb62dfc15e0f7bad8801969ab8dbd193e3": "S13v27-5P1P2", "2e5993b4b0de4f98b1216da5083f724a030d9bf746024e5c0458878cc9e253d1": "S13v27-5P3P4", "14118b9d49f26a55ced57b593109632b394d770c5f6ce09f983f974bc7d39675": "S13v27-H5", "9014339d2ba47d6bdff9f10292f893b54131783eb98c2439fbb1467f4cafed57": "S13v27-4P9h5P2", "434de0c4799e27ea8c8faf18d258fce0ed30a3d57d4cbad8981a6a0f3e21f365": "S13v27"};
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
