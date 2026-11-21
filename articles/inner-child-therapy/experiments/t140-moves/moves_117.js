// moves_117.js: turn 140, in his post's editor (https://ibogaqueen.substack.com/publish/post/189761959), the desktop
// app's browser pane, 2026-11-21 13:33 UTC, with his OK of 13:31 ("retry it now i'm here i can approve"). Question 117,
// A: Healing Old Patterns goes (its h1, the divider above it and the empty paragraph under it); Re-do Trauma Memories (h2
// -> h3) with Discipline Done Right? (h3 -> h4) moves to just before Healthy Mind, Not Perfect, after You Did It Well
// Before; Answer the Disciplinarian (h2 -> h3) moves to just before Earning trust, day to day, after Reframe the Critic.
// No words change. Step 1 builds and checks one transaction (kept in window.__t140); step 2 dispatches it only if the
// document is still the one it was built on. The editor then saves the draft; the live post changes with "Update now".

// Step 1
await (async () => {
  const ed = document.querySelector('.ProseMirror').editor;
  const doc = ed.state.doc;
  const H = (i, lvl, txt) => { const n = doc.child(i); return n.type.name === 'heading' && n.attrs.level === lvl && n.textContent === txt; };
  const checks = {
    hr400: doc.child(400).type.name === 'horizontalRule', hop: H(401, 1, 'Healing Old Patterns'), p402empty: doc.child(402).type.name === 'paragraph' && doc.child(402).textContent === '',
    redo: H(403, 2, 'Re-do Trauma Memories'), disc: H(410, 3, 'Discipline Done Right?'), ans: H(417, 2, 'Answer the Disciplinarian'),
    hr420: doc.child(420).type.name === 'horizontalRule', wpgh: H(421, 1, 'When Practice Gets Hard'),
    earning: H(174, 3, 'Earning trust, day to day'), healthy: H(259, 3, 'Healthy Mind, Not Perfect'), reframe: H(169, 4, 'Reframe the Critic'), welldone: H(255, 4, 'You Did It Well Before'),
    nodes738: doc.childCount === 738,
  };
  if (!Object.values(checks).every(Boolean)) return {ok: false, checks};
  const R = [], D = [];
  for (let i = 403; i <= 416; i++) R.push(i);
  for (let i = 417; i <= 419; i++) D.push(i);
  const relevel = (i, lvl) => { const n = doc.child(i); return n.type.create({...n.attrs, level: lvl}, n.content, n.marks); };
  const newLevel = {403: 3, 410: 4, 417: 3};
  const node = (i) => newLevel[i] ? relevel(i, newLevel[i]) : doc.child(i);
  const skip = new Set([400, 401, 402, ...R, ...D]);
  const nodes = [];
  for (let i = 0; i < doc.childCount; i++) {
    if (i === 174) D.forEach(j => nodes.push(node(j)));
    if (i === 259) R.forEach(j => nodes.push(node(j)));
    if (!skip.has(i)) nodes.push(doc.child(i));
  }
  const tr = ed.state.tr.replaceWith(0, doc.content.size, doc.content.constructor.from(nodes));
  const sig = (n) => n.type.name + '|' + n.textContent;
  const count = (d) => { const m = new Map(); d.forEach(n => m.set(sig(n), (m.get(sig(n)) || 0) + 1)); return m; };
  const exp = count(doc), aft = count(tr.doc);
  for (const k of ['horizontalRule|', 'heading|Healing Old Patterns', 'paragraph|']) exp.set(k, exp.get(k) - 1);
  if (exp.get('heading|Healing Old Patterns') === 0) exp.delete('heading|Healing Old Patterns');
  let sameMultiset = exp.size === aft.size;
  for (const [k, v] of exp) if (aft.get(k) !== v) sameMultiset = false;
  const ok = tr.doc.childCount === 735 && sameMultiset;
  if (ok) window.__t140 = {tr, base: doc, ed};
  return {ok, nodesAfter: tr.doc.childCount, sameMultiset};
})();

// Step 2
await (async () => {
  const u = window.__t140;
  if (!u) return {ok: false, why: 'no transaction built'};
  if (u.ed.state.doc !== u.base) return {ok: false, why: 'the document changed since the transaction was built'};
  u.ed.view.dispatch(u.tr);
  return {ok: u.ed.state.doc.eq(u.tr.doc), nodes: u.ed.state.doc.childCount};
})();
