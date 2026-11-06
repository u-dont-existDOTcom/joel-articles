// The neuro de-armoring lane's copy of the Inner Child lane's paste helper (articles/inner-child-therapy/experiments/
// t88-substack/paste_payload_lane.js, copied on 2026-11-04 and not changed there), with this lane's one temporary draft
// title, which has no detector's name in it (E205). That helper's reasons hold here: the body must be empty first (clear it
// with real keystrokes, ctrl+a then Delete, after checking the title), and after the paste the editor's words, with curly
// quotes made straight, must hash to words_sha256 (PAYLOADS.json, from make_payload.py).
// Set window.__paste = {url: <the payload's raw.githubusercontent.com address at a commit>, sha256: <PAYLOAD-A.html's
// SHA-256>, title: <the draft's exact title>, words_sha256: <PAYLOADS.json's>}, then run this in the draft's editor tab.
// It never clicks anything: Preview, Share and the rest are done by hand in the page, and Publish never.
(async () => {
  const LANE_TITLES = ['Neuro de-armoring, draft A (temp, delete after)'];
  const want = window.__paste || {};
  if (!want.url || !want.sha256 || !want.title || !want.words_sha256) return 'set window.__paste = {url, sha256, title, words_sha256} first';
  const hex = async s => Array.from(new Uint8Array(await crypto.subtle.digest('SHA-256', new TextEncoder().encode(s))))
    .map(b => b.toString(16).padStart(2, '0')).join('');
  const html = await fetch(want.url, {cache: 'no-store'}).then(r => r.ok ? r.text() : Promise.reject('HTTP ' + r.status));
  const got = await hex(html);
  if (got !== want.sha256) return 'refused: the payload\'s SHA-256 is ' + got + ', not ' + want.sha256;
  const title = (document.querySelector('textarea[placeholder="Title"], input[placeholder="Title"]') || {}).value || '';
  if (!LANE_TITLES.includes(want.title) || title !== want.title)
    return 'refused: this draft\'s title is ' + JSON.stringify(title) + ', not one of this lane\'s temporary drafts named in title';
  const eds = Array.from(document.querySelectorAll('.ProseMirror[contenteditable="true"]'));
  if (!eds.length) return 'no editor on this page';
  const ed = eds.sort((a, b) => b.getBoundingClientRect().height - a.getBoundingClientRect().height)[0];
  if (ed.innerText.trim().length > 0)
    return 'refused: the body is not empty (' + ed.innerText.trim().length + ' characters); clear it with ctrl+a, Delete in the editor first';
  ed.focus();
  const tmp = document.createElement('div');
  tmp.innerHTML = html;
  const dt = new DataTransfer();
  dt.setData('text/html', html);
  dt.setData('text/plain', tmp.innerText);
  const ev = new ClipboardEvent('paste', {clipboardData: dt, bubbles: true, cancelable: true});
  ed.dispatchEvent(ev);
  await new Promise(r => setTimeout(r, 2000));
  const words = ed.innerText.replace(/[“”]/g, '"').replace(/[‘’]/g, '\'').split(/\s+/).filter(Boolean);
  const wsha = await hex(words.join(' '));
  return JSON.stringify({pasted_sha256: got, editor_words: words.length, words_sha256: wsha, words_match: wsha === want.words_sha256,
                         handled: ev.defaultPrevented});
})()
