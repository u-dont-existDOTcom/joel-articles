// Pangram web-app page helpers (2026-10-18). Paste into the dashboard tab (https://www.pangram.com/dashboard) after any
// reload or navigation, which clears them. window.__run(name, items) types each item's text into the check box, checks its
// SHA-256, clicks "Check for AI" and logs to window[name]; window.__readC(items, maxPages) reads the results back from the
// history by SHA-256 in the compact form the lane's fill_preds.py takes:
//   [headline, ai likelihood (2 decimals), words, "label, confidence, words; ...", "HH:MM:SS" UTC, "/uuid", [flagged windows]]
// items: [[key, text, sha256], ...]. __run is the source the page held on 2026-10-17 (read back from the page); __readC is
// rebuilt from bNNN-read.js and checked against batch 427g's saved results.
window.__run = async function(name, items) {
  window[name] = [];
  const log = m => window[name].push(m);
  const setter = Object.getOwnPropertyDescriptor(HTMLTextAreaElement.prototype, 'value').set;
  const sha = async t => Array.from(new Uint8Array(await crypto.subtle.digest('SHA-256', new TextEncoder().encode(t)))).map(b => b.toString(16).padStart(2, '0')).join('');
  const button = () => [...document.querySelectorAll('button[type=submit]')].find(b => /check for ai/i.test(b.innerText));
  const wait = ms => new Promise(r => setTimeout(r, ms));
  for (const [k, T, want] of items) {
    for (let j = 0; j < 20 && !(button() && document.querySelector('textarea')); j++) await wait(500);
    const ta = document.querySelector('textarea');
    if (!ta) { log(k + ': no textarea'); break; }
    setter.call(ta, T); ta.dispatchEvent(new Event('input', {bubbles: true}));
    let b = null;
    for (let j = 0; j < 30; j++) { await wait(500); b = button(); if (b && !b.disabled) break; }
    const h = await sha(ta.value);
    if (h !== want) { log(k + ': hash mismatch ' + h); break; }
    if (!b || b.disabled) { log(k + ': button not ready'); break; }
    try { sessionStorage.setItem(k, T); } catch (e) {}
    b.click(); log(k + ': clicked');
    await wait(10000);
  }
  log('end');
};
window.__readC = async (items, maxPages) => {
  const want = {}; for (const [k, t, h] of items) want[h] = k;
  const sha = async t => Array.from(new Uint8Array(await crypto.subtle.digest('SHA-256', new TextEncoder().encode(t)))).map(b => b.toString(16).padStart(2, '0')).join('');
  const out = {};
  let url = 'https://web.pangram.com/api/history-list/?limit=20&offset=0';
  for (let p = 0; url && p < (maxPages || 8) && Object.keys(out).length < Object.keys(want).length; p++) {
    const l = await fetch(url, {credentials: 'include'}).then(r => r.json());
    const ds = await Promise.all((l.results || []).map(it => fetch('https://web.pangram.com/api/history/' + it.uuid + '/', {credentials: 'include'}).then(r => r.json()).then(d => [it, d])));
    for (const [it, d] of ds) {
      const k = want[await sha(d.prompt || '')];
      if (!k || out[k]) continue;
      const o = d.response.overall;
      const n = (d.prompt || '').replace(/\n{2,}/g, '\n');  // window indexes count a blank line as one newline
      const words = w => { const s = n.slice(w.start_index, w.end_index).trim(); return s.startsWith((w.text || '').trim().slice(0, 30)) ? s : (w.text || '').trim() + '…'; };
      out[k] = [o.headline, Math.round(o.avg_ai_likelihood * 100) / 100, o.word_count,
                (o.windows || []).map(w => w.label + ', ' + w.confidence + ', ' + w.word_count).join('; '),
                new Date(it.timestamp).toISOString().slice(11, 19), '/' + it.uuid,
                (o.windows || []).filter(w => w.label !== 'Human').map(w => w.label + ' (' + w.word_count + ' words): ' + words(w))];
    }
    url = l.next;
  }
  return out;
};
'helpers defined';

window.__items_his = [["bt-r07-his-warn", "Some people get a warning before a seizure takes hold, which is called an aura. That's when the things people report can still stop it, depending on what sets their seizures off. If it's flashing or flickering light, cover one eye with a hand and turn away from the light, because closing the eyes doesn't block enough of it. Some people stop a seizure at the warning stage with a strong smell like jasmine, and some train themselves to link one smell with feeling calm and then sniff it when a seizure threatens. When overstimulation is what sets it off, a cool, quiet, dark and comfortable space can help. I'd also try sniffing humic/fulvic acid powder, although that's just a hunch based on the effects I notice so far.", "1e837bcf746923c75fd7ce5f1bf18d38525c99f88a6b58f67684dd5b277be02e"], ["bt-r07-his-canna1", "As for CBD/cannabis, people do smoke or vape it at the start of an aura, while they're still awake enough to do it on purpose. There are also people who find THC and/or CBD works as a nasal spray or sublingually, and there's even a medical THC nasal spray marketed for seizure interruption in Brazil by a company called ABRACE. They testified in Congress that in 30 tests they did with children having seizures, the nasal spray ended those seizures within 30 seconds. You can see it being used on a child in this vid: https://www.youtube.com/watch?v=bgVi5o_2v_w", "e805fe3116f7882c3d2380c1881f28274e35cc51204ffed197d3c8042dc6c74b"], ["bt-r07-his-canna2", "I also read on forums some swear it stops the seizure from going any further, and there was one woman whose EEG showed fewer seizure discharges on the days she smoked. But other people say THC vapes and concentrates brought their seizures on, and in rats that get the brief staring seizures called absence seizures, high-THC smoke made them worse while injected CBD cut them about in half. So the THC may be what makes it go either way.", "9deb3d2eb265c115904e38fad9eece9500a0238653ab6b804411e4edb1a7325c"], ["bt-r07-his-cbd2", "As for topical CBD, it hasn't been well-studied. There was a short 12-week trial done, where they used a CBD skin gel, and although absorption was good, it didn't work any better than placebo to prevent seizures. The study authors suggested the dosing may have been too low, or it works better for generalized rather than focal seizures. Generalized are the type people usually have with MDMA & psychedelic overdoses.", "2cf02d32a67178e907f990413d8acd2099dd887ae3b705fcb072c03d7e555d45"]];
window.__run('r07his', window.__items_his); 'started ' + window.__items_his.length;