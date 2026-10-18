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
