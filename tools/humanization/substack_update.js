// substack_update.js - press Update on a published Substack post without sending an email, and wait until it has gone.
//
// Run in the post's editor tab (/publish/post/<id>), in the desktop app's browser pane, after the change is in the
// editor and the editor says "Saved":
//   await window.__updateNow({dry: true})   -> what the dialog has (its boxes), then Cancel; nothing is published
//   await window.__updateNow()              -> {clicked: true, ...}; the tab then moves to the post's share page
// Lesson toc-2026-11-25g. Two things went wrong by hand on 2026-11-25, and this guards both:
//   1. The dialog is not the same for every post. On one post the top button says "Update" and the dialog has no
//      delivery choice; on another it says "Continue" and the dialog has a box "Send via email and the Substack app".
//      This refuses to press "Update now" unless every checkbox in the dialog is unticked (no email, no scheduling).
//   2. Pressing the button is not the update. Leaving the page right after the click lost one update. This waits in
//      the page until the address is the share page (.../share-center?alreadyPublished=true); the caller's script is cut
//      off by that move, which is the sign it went. The proof is then the live post: fetch /api/v1/posts/by-id/<id> and
//      read updated_at and the body, never the click.
window.__updateNow = async (opt) => {
  opt = opt || {};
  const wait = ms => new Promise(r => setTimeout(r, ms));
  const saved = [...document.querySelectorAll('button')].map(b => b.innerText.trim()).find(t => /^(Saved|Saving|Unsaved)/.test(t));
  if (saved !== 'Saved') return {clicked: false, why: 'the editor does not say "Saved" (' + saved + ')'};
  const open = document.querySelector('[data-testid="publish-button"]');
  if (!open) return {clicked: false, why: 'no Update or Continue button'};
  const label = open.innerText.trim();
  open.click();
  let dlg = null, go = null;
  for (let k = 0; k < 20 && !go; k++) {
    await wait(500);
    dlg = [...document.querySelectorAll('[role=dialog], .modal, [class*=modal]')].find(d => /Update now/.test(d.innerText));
    go = dlg && [...dlg.querySelectorAll('button')].find(b => b.innerText.trim() === 'Update now');
  }
  if (!go) return {clicked: false, why: 'no "Update now" in the dialog: is the post published?', label};
  const boxes = [...dlg.querySelectorAll('input[type=checkbox]')].map(i => [(i.closest('label') || i.parentElement).innerText.trim().slice(0, 60), i.checked]);
  if (boxes.some(b => b[1])) return {clicked: false, why: 'a box in the dialog is ticked; untick it by hand or ask him', boxes, label};
  if (opt.dry) {   // look only: say what the dialog has, then Cancel
    const cancel = [...dlg.querySelectorAll('button')].find(b => b.innerText.trim() === 'Cancel');
    if (cancel) cancel.click();
    return {clicked: false, dry: true, label, boxes, would_click: !go.disabled, cancelled: !!cancel};
  }
  if (go.disabled) return {clicked: false, why: '"Update now" is greyed out', boxes, label};
  go.click();
  for (let k = 0; k < 60; k++) { await wait(500); if (/share-center/.test(location.href)) break; }
  return {clicked: true, label, boxes, at: location.href};
};
