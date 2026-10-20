const want = {"16af01202b93f7f3b960bdedca251cc3c2e2bd6b4856e3f9dc717241ee2977fb": "HG06-fix", "15a25ec13fe287b2b33a96734fa9ecb92c41dc82d11b8cf5f12005e5895228b1": "HG07-fix", "2c329331ed0097c8ecd48f39283a8b442edfb4db5a00f581f8758b8992efed6e": "HG10-fix", "043d4962ace179b7c31bbae009198ff9ee8a2a591993b25a293056c6e5781d72": "HG11-fix", "701ae7a8e3b8c77ab4f61d96517d07e6f832874e7a39394c59cf4c733323c6ae": "HG22-fix", "18cf1cfdaf8b9c990c8e222e6957d4f012af06d3386bc34fd1e7ad8a91970f1c": "HG01-fix", "9d5e953576988a60a536a0ffbfdca058175be75417242eac921d70ce7b52e26c": "HG12-fix", "dff430fa4cbe8a3c6ffa5df5ba4807e579d1584cb8f0729809ab693d67f4239d": "HG15-fix", "05af934a6598f3ead60de0b1e9b90dfb6dae17d27c997f60f28eb4a92b6291ce": "HG18-fix", "82116b151a95179a436acff5213cffd892076380a1ff3b14036074eba6e47f05": "HG19-fix", "ac4159db6a91a20f44eb074e44be97ae92d53e9f5a16492c52ab8420c4f41e9f": "HG21-fix", "81b3eb7ad8ef1446766dba371cbc6d48272c6ba9637c5f06d7a65721e5b51f20": "HG23-fix", "36cb0643c0898f83c94b6a3dad796c3b411c569b10ea7276b4fcea8893da7bda": "HG25-fix", "598d2c8243cc6ec37fc31f966ba638dab68f5d128bff8a2df35e19777e2b9d6f": "HG26-fix", "3fd9886a526ac9f7b4a7e2ffd364b07531575687539ec4c3736afb3f5efb546d": "HG28-fix", "af667d3ef55b4856f411edde61412a27c544b6277b395b5c06e51a47e49cb12c": "HG34-fix", "06c53918f4a131a0f31c8ad911672117a3b126758699b3c7a2090f7364236178": "HG36-fix", "3d7f5d786570f48e397f89fa80f61835ea06cb2713155294a47a08bbdf8529f7": "HG13-fix", "9a1fcf518ae290c097f063f1b156b3d5b816d65fcc05ac60c18cc27817c2a5a2": "HG40-fix", "c42f92fc09dcfc0db424f41fe1e1cc6df397dad87550acf0fb1ad68680ba990c": "HG14-fix", "607ee1fe8340185db39fba96693bdcecfe0dc3b60d7ddad4267a7a9b8dfb4b7d": "HG20-fix", "8157498b12c9d319830cdeece42863b09e06df045c95c119ff9c9683afe23fb2": "HG35-fix", "f8ecfe692bd20901a124e13b6b880829b3c7ada3897e16b56f8e5e17fc03d1ea": "HG02+03-fix", "f0208511bb92bad12244cb910e0037e1ac64ce7db8d0bcb07a45c9758c5cd502": "HG27-fix", "addbe260ef359af15887e6aa87c82b55ab971c54fdaa2df7ba7125624b2dbef7": "HG33-fix"};
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
