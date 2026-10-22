// This lane's copy of the hypnosis lane's paste_payload.js (articles/inner-signal/humanize/fix-20261020/substack41r/), for
// this lane's two temporary drafts, whose titles have no "Pangram" in them (E205, Joel 2026-10-21 18:06 UTC).
// Two changes from the original, both from 2026-10-22 (turn 88):
// 1. No replace path. Selecting the body through the DOM and pasting at once inserted the payload above the old text instead of
//    replacing it (draft A held both versions, 30,526 words), because the editor hadn't taken the selection yet. So the body
//    must be empty: clear it first with real keystrokes in the editor (ctrl+a, then Delete), after checking the title.
// 2. A check after the paste: the editor's words, with curly quotes made straight (Substack's editor curls every straight quote
//    and apostrophe on paste, as a published post does), must hash to words_sha256, computed the same way from TEXT-<X>.txt.
// Set window.__paste = {url: <the payload's raw.githubusercontent.com address at a commit>, sha256: <the payload file's SHA-256>,
// title: <the draft's exact title>, words_sha256: <SHA-256 of TEXT-<X>.txt's words, quotes straightened, joined by one space>}.
// It never clicks anything: Preview, Share and the rest are done by hand in the page, and Publish never.
(async () => {
  const LANE_TITLES = ['Inner Child, draft A (temp, delete after)', 'Inner Child, draft B (temp, delete after)'];
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
