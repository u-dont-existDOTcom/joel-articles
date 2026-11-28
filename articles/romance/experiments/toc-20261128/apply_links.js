// The section links of LINK-PLAN.json into his post's Substack editor, as one ProseMirror transaction, and the title's
// date. Run in the post's editor tab (/publish/post/197034035), in the desktop app's browser pane:
//   window.__linksRomance(PLAN, TITLE, {dry: true})   -> the report, nothing changed
//   window.__linksRomance(PLAN, TITLE, {dry: false})  -> dispatched, the title set; then __updateNow() (no email)
// Each link's "find" must occur once in the editor's text blocks and hold its "words" once; the words get a plain link
// (no new tab), "#§<slug>", which scrolls on the page (lesson toc-2026-11-25c). Nothing else changes: the report
// compares every block's text before and after, and the headings.
window.__linksRomance = (PLAN, TITLE, opt) => {
  const ed = document.querySelector('.ProseMirror').editor;
  const st = ed.state, S = st.schema, tr = st.tr, rep = {errors: [], links: []};
  const blocks = [];
  st.doc.descendants((n, pos) => { if (n.isTextblock) { blocks.push([pos, n]); return false; } return true; });
  const locate = (find) => {
    const hits = [];
    for (const [pos, n] of blocks) {
      let text = ''; const map = [];
      n.forEach((c, off) => {
        if (c.isText) { for (let k = 0; k < c.text.length; k++) map.push(pos + 1 + off + k); text += c.text; }
        else { map.push(pos + 1 + off); text += '￼'; }
      });
      let i = text.indexOf(find);
      while (i >= 0) { hits.push({i, map, node: n}); i = text.indexOf(find, i + 1); }
    }
    return hits;
  };
  const marks = [];
  for (const l of PLAN.links) {
    const h = locate(l.find);
    if (h.length !== 1) { rep.errors.push('"' + l.find + '": ' + h.length + ' matches'); continue; }
    const k = l.find.indexOf(l.words);
    const from = h[0].map[h[0].i + k], to = h[0].map[h[0].i + k + l.words.length - 1] + 1;
    let linked = false;
    st.doc.nodesBetween(from, to, (n) => { if (n.isText && n.marks.some((m) => m.type.name === 'link')) linked = true; });
    if (linked) { rep.errors.push('"' + l.words + '" already has a link'); continue; }
    marks.push({from, to, href: l.href, words: l.words});
  }
  for (const m of marks) {
    tr.addMark(m.from, m.to, S.marks.link.create({href: m.href, target: null, rel: null, class: null}));
    rep.links.push([m.words, tr.doc.textBetween(m.from, m.to), m.href]);
  }
  const texts = (d) => { const out = []; d.forEach((n) => out.push(n.type.name + ':' + n.textContent)); return out; };
  rep.same_text = JSON.stringify(texts(st.doc)) === JSON.stringify(texts(tr.doc));
  const titleEl = document.querySelector('textarea[placeholder="Title"], input[placeholder="Title"]');
  rep.title = titleEl ? [titleEl.value, TITLE.from, TITLE.to] : 'no title field';
  if (!titleEl || titleEl.value !== TITLE.from) rep.errors.push('the title is not the one the plan was made from');
  if (rep.errors.length || !rep.same_text || opt.dry) return rep;
  ed.view.dispatch(tr);
  const setter = Object.getOwnPropertyDescriptor(Object.getPrototypeOf(titleEl), 'value').set;
  setter.call(titleEl, TITLE.to);
  titleEl.dispatchEvent(new Event('input', {bubbles: true}));
  rep.dispatched = true;
  return rep;
};
