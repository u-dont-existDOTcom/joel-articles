// The hypnosis lane's paste helper since 2026-10-22, replacing fix-20261020/substack41r/paste_payload.js. It is the Inner
// Child lane's paste_payload_lane.js (articles/inner-child-therapy/experiments/t88-substack/, turn 88) with this lane's
// draft titles; that lane's note (NOTE-FROM-INNER-CHILD-LANE-20261022.md, part 1) gave the reasons:
// 1. No "Pangram" in a temporary draft's title (E205, Joel 2026-10-21 18:06 UTC). The old helper replaced a body only under a
//    title starting "TEMP Pangram", which is how this lane's drafts got that word back; this one accepts only the exact
//    titles below.
// 2. No replace path. Selecting the body through the DOM and pasting at once can put the payload above the old text, because
//    the editor hasn't taken the selection yet (the Inner Child lane's draft A held both versions). So the body must be
//    empty: clear it first with real keystrokes in the editor (ctrl+a, then Delete), after checking the title. Clearing that
//    way can make Substack write to Joel's clipboard.
// 3. A check after the paste: the editor's words, with curly quotes made straight (Substack's editor curls every straight
//    quote and apostrophe on paste), must hash to words_sha256, computed the same way from the payload (make_screen.py's
//    WORDS-S.json, or the recheck's builder for drafts A and B).
// Set window.__paste = {url: <the payload's raw.githubusercontent.com address at a commit>, sha256: <the payload file's
// SHA-256>, title: <the draft's exact title>, words_sha256: <as above>}, then run this in the draft's editor tab.
// It never clicks anything: Preview, Share and the rest are done by hand in the page, and Publish never.
(async () => {
  const LANE_TITLES = ['TEMP recheck A (hypnosis guide) - do not publish',
                       'TEMP recheck B (hypnosis guide appendices) - do not publish',
                       'TEMP screen (hypnosis guide samples) - do not publish'];
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
  await new Promise(r => setTimeout(r, 2500));
  const words = ed.innerText.replace(/[“”]/g, '"').replace(/[‘’]/g, '\'').split(/\s+/).filter(Boolean);
  const wsha = await hex(words.join(' '));
  return JSON.stringify({pasted_sha256: got, editor_words: words.length, words_sha256: wsha, words_match: wsha === want.words_sha256,
                         handled: ev.defaultPrevented});
})()
