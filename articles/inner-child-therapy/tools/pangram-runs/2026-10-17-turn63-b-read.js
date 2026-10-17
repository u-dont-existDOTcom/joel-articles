const want = {"e914f42570c8c06929540164c586b1a9526a02ad6d31de55e41cc61b51de1ae3": "t63b_p10f", "0d52445fc655d908fe5bd95c22370a31c0d84d52806d7606a1764dc25af584fd": "t63b_p10g", "99f84dc35d10caa22f3e45f4fbc7e993629d7ed7005430361b1a6107828d1d55": "t63b_p10h", "163fe445cb8fe5aee23d5139889abd8fec113be21d9379c697d1665beb05c597": "t63b_p10i", "57b38d173694d12f8cc02320500ad1560e0b6f05f45a5b5656fd1c4e429e1b80": "t63b_p910f", "47f605dba5f071c352cd22bcb77fe845f11a6ba51b200b60655f1cc329573934": "t63b_p910g", "e43a93617c42b75661d20bd977e21ea53d4e40187d91a857c7ada5f900b367ec": "t63b_p910h", "0f00677954e13e1014a69d1b2d0a9eec16e3488919b802f858c5bc0d55111311": "t63b_p910i", "2f1580df31f4dd2504b892b8c88f10ca7496324662c61587636c087e93144e6d": "t63b_h1f", "42032f7d2f06399de979ae1dcad21cadd249092ae575dcd63984af570105f882": "t63b_h1g", "7168401ce820e40782bb4eff7c58694f630f2fbbdc945a9218ee00f42d6cd72e": "t63b_h1h", "607adee996e605bbc880cc1cdaac42ebd4e7f452a4625a2ff3d3a90443377558": "t63b_h1i"};
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
