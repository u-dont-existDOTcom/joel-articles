// dispatch.js: after update.js passed, apply its one transaction, if the editor's document is still the one it was built
// on, and set the title's date. The editor then saves the post's draft itself; the live post changes only with Update
// (tools/humanization/substack_update.js, which refuses while any box in the dialog, email included, is ticked).
await (async () => {
  const u = window.__updRomance;
  const T = window.__titleRomance;
  if (!u || !T) return {ok: false, why: 'no transaction built, or no title change set'};
  if (u.ed.state.doc !== u.base) return {ok: false, why: 'the document changed since the transaction was built'};
  const titleEl = document.querySelector('textarea[placeholder="Title"], input[placeholder="Title"]');
  if (!titleEl || titleEl.value !== T.from) return {ok: false, why: 'the title is not the one the plan was made from'};
  u.ed.view.dispatch(u.tr);
  const setter = Object.getOwnPropertyDescriptor(Object.getPrototypeOf(titleEl), 'value').set;
  setter.call(titleEl, T.to);
  titleEl.dispatchEvent(new Event('input', {bubbles: true}));
  await new Promise((r) => setTimeout(r, 1500));
  const now = u.ed.state.doc;
  return {ok: now.eq(u.tr.doc), title: titleEl.value, textLength: now.textContent.length};
})()
