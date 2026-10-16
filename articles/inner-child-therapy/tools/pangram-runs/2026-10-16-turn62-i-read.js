const want = {"958cabb306d00aa5677078e6c50aaba36e2b8d8b12aff25075e4ba53bcd722c3": "t62i_p8s", "0a2eabed1732a1fba955ac97f0ca0b87071c2abea87754dd1eea38da1596d143": "t62i_p8v", "b96712d170ef0e8c3322116403a41f64014e3c6c1c4569a65270f017f8c423ee": "t62i_p8w", "e08ebe2a568dfa3465e6dd97fe1be5b602403a3f5001c660ff7efc41723da9f8": "t62i_p8x", "cc18a3e9646d054278cb4dd550df5875d36a92cc01354b454046974466420f1c": "t62i_p89s", "c0f3b5db129f515d487703d084c3c64787b39584652f8de3ed4c081e1009d1b8": "t62i_p89v", "00951ec4f3ae976d853de676cba19baeadf682f22372db1bbb0a92afba96240a": "t62i_p89w", "77c1f85de49cf36407a5080df0475e6f40b2e56df962f4fd57ef90f8c8d26302": "t62i_p89x", "a17d38a54d1fe62ac78ca35830d25443317ae12daa3a7800c7534c9f4f20da7f": "t62i_p78s", "7fb7289f399a2cea66374338ef9e2e44d8c10669c11a0a37e08247d534b35cf2": "t62i_p78v", "f2e8fa34d93559e3a9c6bc700be232f22cb40a016b57ced8ab4f5f7705972afa": "t62i_p78w", "6160b2619ca63e57fafcc1385dfb7102d860374fb62557eb675f74c3a9a71ec2": "t62i_p78x", "c89ccc7e82970c312d2dae2a2ad54dc578731f9b1a09ca3fab538499a512e73f": "t62i_h1s", "8188fc4106b8f011c8d69610f85b7a571e12f30be74a3c37b3f84c5403276efe": "t62i_h1v", "0e5b972c8af634f91da3ea57bdf941dadde240aa39a04b3ff4dfc3758c4c8e82": "t62i_h1w", "a302677479bee4246ddd319b502da15083035cbb15721106b1203c85a0c5220e": "t62i_h1x"};
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
