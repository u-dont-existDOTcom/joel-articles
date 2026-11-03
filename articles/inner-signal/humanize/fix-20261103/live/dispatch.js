// dispatch.js: after update.js passed, apply its one transaction, if the editor's document is still the one it was built on.
await (async () => {
  const u = window.__upd1103;
  if (!u) return {ok: false, why: 'no transaction built'};
  if (u.ed.state.doc !== u.base) return {ok: false, why: 'the document changed since the transaction was built'};
  u.ed.view.dispatch(u.tr);
  const now = u.ed.state.doc;
  return {ok: now.eq(u.tr.doc), nodes: now.childCount, textLength: now.textContent.length};
})()
