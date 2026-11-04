// dispatch.js: apply the transaction update.js built and checked, only if the editor still holds the document it was built on.
(() => {
  const u = window.__updGut;
  if (!u) return {ok: false, why: 'no checked transaction'};
  if (u.ed.state.doc !== u.base) return {ok: false, why: 'the editor changed since the check'};
  u.ed.view.dispatch(u.tr);
  let n = 0;
  u.ed.state.doc.forEach(() => n++);
  return {ok: true, nodes: n, text: u.ed.state.doc.textContent.length};
})()
