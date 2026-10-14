const want = {"c7daf4ae525620e92a52dc8440985d8ee0a250d41b6a7583bc5f43bad089d2ef": "t55_ag_good", "735e6d31f3c3d1051524710b837055a7724a872043594412af1e5377eef452ef": "t55_ag_g1", "cd26f7b50df33f1647dba3577ece3115dd77a075ff7f528276872652499b89a1": "t55_ag_g2", "23568789ba0415996d933a43dcacebe52a15841c808cae255fdd765313cb203b": "t55_ag_g3", "eb71cab16d8b47cb8cb87a994a2695594e7462229c1503b98f49d135b28ef7f0": "t55_ag_g4", "277ffd09e2b6dfc8ae8de670bd51db8dc415596e45db39966e4213ce14758cc1": "t55_unt_p3", "c76c364619dc3c8aebda0bfc0490d7f8a4bff835607a41fb2b65cb9be2d97afc": "t55_heal_p", "7e5aa10847e47e481614297945bf8010bc19621cc61bfc42d376ea6275163bfd": "t55_boc_p1", "89b502312beb950e6e831614fc6e8e92785e705e958d067d7f31177911f81a12": "t55_boc_p3", "eaa3faf5e07354e237659ff7a5814c0e60e11f89faf5f1ca9d50e20c5efffcd9": "t55_ag_h3", "e02e997b2c0e21a3e9f3d8cdfb2c97e446f710b43d93c07f843723970f9a2d86": "t55_borrow_h2", "87b788cc1880ba47b30c6c3a963d74e93e4e9cfd227f204016463fb632fae159": "t55_boc_h2", "483856877cf44be810bb6e85232606de41c0ce0f4bd44fb2f5fd4be683c0627d": "t55_borrow_h1", "26bd798b29cf8428a1e3193061383d1b3c01d92b1a96a4b0f4cc1b671243fd16": "t55_unt_h2", "1cd9021ac0d005f75eb66bab873d01e2713d7f96143370fcf7304ac8fda3296c": "t55_play_h2", "fb1b706898d146edebef57463c794d03fee62e1d4c51f74e59d53af85b3b328f": "t55_some_h1", "1bd59e8e47275b6cdbbf47748693866bf297e64635ebe7ca1628ce8ff69d45d6": "t55_heal_h3", "363fa7469f623568169beedb8f9b08801b570ad9c0d46b90aa7a16a48db427dd": "t55_body_h2", "6517490914f1ea44d16497c0201c62fe6d9dfeb3559c20bb7124cf4b63a3a3fd": "t55_before_h1"};
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
