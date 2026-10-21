// Paste one recheck payload (PAYLOAD-A.html or PAYLOAD-B.html, make_recheck.py) into a new Substack draft's body, as the
// copy page's Copy button and a paste would (2026-10-21; Joel, 23:54 UTC: "you can automate this method yourself ... go to:
// https://ibogaqueen.substack.com/publish/post then paste in the substack html"). Run in the draft's editor tab after
// setting window.__paste = {url: <the payload's raw.githubusercontent.com address at a commit>, sha256: <its SHA-256>}.
// It fetches the payload, refuses it unless the SHA-256 matches, and dispatches a paste event carrying it as text/html
// (and its text as text/plain) on the body editor, the way the browser hands a real paste to Substack's editor.
// It never clicks anything: Preview, Share and the rest are done by hand in the page, and Publish never.
// A recheck after more fixes reuses the lane's own temporary draft (2026-10-21, after Joel's answers of 17:56 UTC), so his
// drafts list doesn't fill with copies: with window.__paste.replace_title set to the draft's exact title, which must start
// "TEMP Pangram", the paste replaces the body instead of refusing a non-empty editor. Any other draft is refused.
(async () => {
  const want = window.__paste || {};
  if (!want.url || !want.sha256) return 'set window.__paste = {url, sha256} first';
  const html = await fetch(want.url, {cache: 'no-store'}).then(r => r.ok ? r.text() : Promise.reject('HTTP ' + r.status));
  const buf = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(html));
  const got = Array.from(new Uint8Array(buf)).map(b => b.toString(16).padStart(2, '0')).join('');
  if (got !== want.sha256) return 'refused: the payload\'s SHA-256 is ' + got + ', not ' + want.sha256;
  const eds = Array.from(document.querySelectorAll('.ProseMirror[contenteditable="true"]'));
  if (!eds.length) return 'no editor on this page';
  const ed = eds.sort((a, b) => b.getBoundingClientRect().height - a.getBoundingClientRect().height)[0];
  const title = (document.querySelector('textarea[placeholder="Title"], input[placeholder="Title"]') || {}).value || '';
  const replace = want.replace_title && want.replace_title.startsWith('TEMP Pangram') && title === want.replace_title;
  if (ed.innerText.trim().length > 0 && !replace)
    return 'refused: the editor is not empty (' + ed.innerText.trim().length + ' characters) and the title (' + JSON.stringify(title) +
           ') is not the lane\'s temporary draft named in replace_title';
  ed.focus();
  const sel = window.getSelection();
  sel.selectAllChildren(ed);
  if (!replace) sel.collapseToStart();
  const tmp = document.createElement('div');
  tmp.innerHTML = html;
  const dt = new DataTransfer();
  dt.setData('text/html', html);
  dt.setData('text/plain', tmp.innerText);
  const ev = new ClipboardEvent('paste', {clipboardData: dt, bubbles: true, cancelable: true});
  ed.dispatchEvent(ev);
  await new Promise(r => setTimeout(r, 1500));
  return JSON.stringify({pasted_sha256: got, replaced: replace, payload_chars: html.length, editor_chars: ed.innerText.length,
                         editor_words: ed.innerText.split(/\s+/).filter(Boolean).length, handled: ev.defaultPrevented});
})()
