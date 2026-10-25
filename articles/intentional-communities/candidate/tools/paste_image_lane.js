// Paste one image file into the community lane's temporary draft, so that Substack uploads it and writes its own image
// block (2026-10-24, Joel's answer 65.21: "after the "preferences and social change" i want to add this image:
// /home/joel/Documents/community article/kibbutz harms.png"). The block is then read back from the editor, because only
// Substack's own HTML may stand for a native object (docs/SUBSTACK-HELPER-DELIVERY-GATE.md).
// Set window.__img = {url: <the file's raw.githubusercontent.com address at a commit> (or b64: its bytes in base64),
// sha256: <the file's SHA-256>, name: <file name>, type: 'image/png', title: <the draft's exact title>} and run this in the
// draft's editor tab. It checks the bytes, the title and an empty body, pastes the file and never clicks anything.
(async () => {
  const LANE_TITLES = ['TEMP recheck (community article) - do not publish'];
  const want = window.__img || {};
  if (!(want.url || want.b64) || !want.sha256 || !want.name || !want.type || !want.title)
    return 'set window.__img = {url or b64, sha256, name, type, title} first';
  let bytes;
  if (want.url) {
    bytes = new Uint8Array(await fetch(want.url, {cache: 'no-store'}).then(r => r.ok ? r.arrayBuffer() : Promise.reject('HTTP ' + r.status)));
  } else {
    const bin = atob(want.b64);
    bytes = new Uint8Array(bin.length);
    for (let i = 0; i < bin.length; i++) bytes[i] = bin.charCodeAt(i);
  }
  const got = Array.from(new Uint8Array(await crypto.subtle.digest('SHA-256', bytes))).map(b => b.toString(16).padStart(2, '0')).join('');
  if (got !== want.sha256) return 'refused: the file\'s SHA-256 is ' + got + ', not ' + want.sha256;
  const title = (document.querySelector('textarea[placeholder="Title"], input[placeholder="Title"]') || {}).value || '';
  if (!LANE_TITLES.includes(want.title) || title !== want.title)
    return 'refused: this draft\'s title is ' + JSON.stringify(title) + ', not this lane\'s temporary draft named in title';
  const eds = Array.from(document.querySelectorAll('.ProseMirror[contenteditable="true"]'));
  if (!eds.length) return 'no editor on this page';
  const ed = eds.sort((a, b) => b.getBoundingClientRect().height - a.getBoundingClientRect().height)[0];
  if (ed.innerText.trim().length > 0 || ed.querySelector('img'))
    return 'refused: the body is not empty; clear it with ctrl+a, Delete in the editor first';
  ed.focus();
  const dt = new DataTransfer();
  dt.items.add(new File([bytes], want.name, {type: want.type}));
  const ev = new ClipboardEvent('paste', {clipboardData: dt, bubbles: true, cancelable: true});
  ed.dispatchEvent(ev);
  return JSON.stringify({file_sha256: got, bytes: bytes.length, handled: ev.defaultPrevented});
})()
