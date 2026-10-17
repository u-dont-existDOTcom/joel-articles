const want = {"b19dd2763bd01439b96e5367261063dbd203826d21dc48e29261d307bcbfcc77": "S2v34-P2", "1665f42b591ab91ecfb2b8e3dd93a7ea7ed7d10e53b80e5c71b8484ddac9b277": "S2v34-A46", "85c085d0d9a3a521df06ca3169204b8b8646e0d95ff08d41fbc11c7b5f9171c3": "S2v34-A46+next", "a373fc60d2ae06840125b9027062d0d03e409f405bb1308991a948708fd14e03": "S8v31-rumspringa", "600b14812a17cea7dc23c818ad656eceb2c8178715abf60f817cc915e9b26948": "S8v31-skills", "5c75005e82296114921a67e9681478706cf2b7983d38d5719f44fbab7f49c03a": "S8v31-skills+next", "e627ed75ab7e27c1e66d8d7f7fb6061ceeae21eeb3af2fbe2f90ef324db4789b": "S15v15-H2P1+next", "945515d7b91ad7b5c56c98e05e7ef4ef3ad510dfaecc71439028fc3570c4502e": "S15v15-H2P2", "a5417f84385aca5687a455adb4c88f5650bbe78c20ffdb82e96b6c384f9f8dcc": "S16v30-H3P2+prev", "b015762abb47f7b5919141a33919fd0f60c35a961626b26689ad803f6952d8e0": "S16v30-H3P2+next", "b5a9561472bcb65d8f3bc6537150eeee87daa512b3bbf9cf335552b9311e838f": "S2v34", "75f39f12d0c2b4b5e81c80fc3b6e8824a64af355ec6b823c4a6aaf80d2aa5e36": "S8v31", "05dcf73ad03bf0d81c69ed17e15a5ffde0962e2b84556dd648cafd9b7d072cd6": "S12v16", "b3c6330eba0b01b9e9fd708fa5ac22e021246d6fc56c14b73e4a21ce4571aa1d": "S15v15", "e3a1eef890cd46571401a5525f1d11f50a00e256e60700c1a746f3e148838e25": "S16v30"};
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
