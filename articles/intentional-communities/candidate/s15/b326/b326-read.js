const want = {"441a769b19793f175779cfbaa518bf74126a37ec28cf448959f585daf3b7fa27": "S15v5-H1-P1+P2", "312e6bd466e5f1be3a480ffebbca44927f2f943cc1bf561ae85c808f5b8af537": "S15v5-H1-P4", "54bf6859a4bc8de824b2eb181b917ced8302aca01b9a35e4fe7fc69989200c15": "S15v5-H1-P5", "edf8224948b50162928f82a6a02956a1a641af3014b7f52c3793193c83ed5061": "S15v5-H2-P2", "7f24a661fa5c7ca460da8cf35ab01b0e844012dbe2cae932137d071e0b01f02f": "S15v5-H2-P3", "43b7635e5cf3fab6a371e5a983230880661c157657559c888a4724cad8776958": "S15v5-H2-P3+P4", "8c2ab780b2de06777ee23154e7527321c1324a03c850ee5811e233595c6304af": "S15v5-H2-P4+P5", "92d56c71aec1f1e2a8ee8309be56bcc2c670e7857d02c3fa95966b13d580b345": "S15v5-H2-P7", "4ab2a4d8eca50171b8c32bdf04421b9e2f8192b888a246a54c9ce452ef80b824": "S15v5-H3-P1", "c601ef9cc07c61f6014a6c40506df6ffe0d967bb5ed2bdbd8ae093b64dfe9244": "S15v5-H3-P2", "ea6d4b652e1d1f7b9052cf2119b11f333186071260bc56427c1d69858a1e4ee7": "S15v5-H3-P3", "11278db400e01015e1e18acbe306b1ca660d7f60e8d9b3ab1415ad12620276de": "S15v5-H3-P4", "8c50bc32b5370290b00975bd223c29fad28d022883f96dd81b0023aceae98ffc": "S15v5-H3-P5", "2e8d14706fa94f6ac9833a2e087b01061f96139db3e4aa6f616f7d3d3be528bb": "S15v5-H3-P7", "eebe7b57cee137b661d43ed7919b6e02343375f0fba399f9f4d46aea131efd85": "S15v5-H3-P8", "0e789a94e9149c673cb19cb5ea5c29c76ad5d929074dee8eeaa79562e21ee005": "S15v5-H2-P1+P2", "9844d9dd922a0e4c60b2e9dea2d5087f1fe4b81aaf98ac3e1dd3e898344cf7b5": "S15v5-H1-P4s", "7f2e79309f38e367a8557df92b57f97b6177facd8063a9816de70bd209e9eb2e": "S15v5-H1", "12fb057648be1ea4e9ba2dc6afb077bcbf92d5836da3afd891a97b1551700e19": "S15v5-H2", "810366510b448aee0b16af3eb22dd022a7670f6a22a17d67f4a0b5656947c454": "S15v5-H3", "0f1d9438af5fdcb059f5415fc1254537cc4fbcefbb6ed81e5ebb94640c4a9ee1": "S15v5s-H1", "60072e0397f51a226b940caeb8150cad05517605b75b408daa023868d7ffa435": "S15v5"};
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
