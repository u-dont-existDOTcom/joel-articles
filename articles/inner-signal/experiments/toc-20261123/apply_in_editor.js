// The Self-Hypnosis guide's final contents into the post's Substack editor, as one ProseMirror transaction, from
// EDITOR-OPS.json (written by apply_plan.py). After the Nirvāna run's apply_in_editor.js; this one works by block, so a
// section that moves takes its lists, quotes and pictures with it. Run in the post's editor tab:
//   window.__applyContents(ops, {dry: true})   -> the report, nothing changed
//   window.__applyContents(ops, {dry: false})  -> dispatched; then Update -> "Update now" (no email) in the editor
// It refuses to dispatch unless the editor's blocks are the live post's blocks (count, and each text block's hash), every
// edit and link is found exactly once, and the headings after the change are ops.expected_headings in order. The report
// lists the text that goes and the text that is new, so nothing but the planned changes goes in.
// The second edit of 2026-11-25 (apply_plan2.py, EDITOR-OPS2.json) uses the same function; it adds one heading that the
// post didn't have, which the order gives as {h: [level, text]} with no block number.
window.__applyContents = (OPS, opt) => {
  const ed = document.querySelector('.ProseMirror').editor;
  const st = ed.state, S = st.schema, tr = st.tr, rep = {errors: [], inline: []};
  const fnv = t => { let h = 0x811c9dc5; t = t.replace(/\s+/g, ''); for (let i = 0; i < t.length; i++) { h ^= t.charCodeAt(i); h = Math.imul(h, 0x01000193) >>> 0; } return h >>> 0; };
  // 1. the editor holds the post the plan was made from
  const top = []; st.doc.forEach(n => top.push(n));
  rep.blocks = [top.length, OPS.blocks];
  if (top.length !== OPS.blocks) rep.errors.push('blocks: the editor has ' + top.length + ', the plan ' + OPS.blocks);
  else {
    const bad = OPS.fingerprint.filter(([i, h]) => fnv(top[i].textContent) !== h).map(([i]) => [i, top[i].type.name, top[i].textContent.slice(0, 50)]);
    if (bad.length) rep.errors.push('text differs from the plan in ' + bad.length + ' blocks: ' + JSON.stringify(bad.slice(0, 12)));
  }
  // 2. inline edits, then links (found in the text as edited)
  const textblocks = doc => { const out = []; doc.descendants((n, pos) => { if (n.isTextblock) { out.push([pos, n]); return false; } return true; }); return out; };
  const locate = (doc, find) => {
    const hits = [];
    for (const [pos, n] of textblocks(doc)) {
      let text = ''; const map = [];
      n.forEach((c, off) => {
        if (c.isText) { for (let k = 0; k < c.text.length; k++) map.push(pos + 1 + off + k); text += c.text; }
        else { map.push(pos + 1 + off); text += '￼'; }
      });
      let i = text.indexOf(find);
      while (i >= 0) { hits.push({i, map}); i = text.indexOf(find, i + 1); }
    }
    return hits;
  };
  const edits = [];
  for (const e of OPS.edits) {
    const h = locate(st.doc, e.from);
    if (h.length !== 1) { rep.errors.push('edit ' + e.id + ': ' + h.length + ' matches'); continue; }
    edits.push({from: h[0].map[h[0].i], to: h[0].map[h[0].i + e.from.length - 1] + 1, text: e.to, id: e.id});
  }
  edits.sort((a, b) => b.from - a.from);
  for (const x of edits) { if (x.text) tr.insertText(x.text, x.from, x.to); else tr.delete(x.from, x.to); rep.inline.push(['edit', x.id]); }
  const linkMark = href => S.marks.link.create({href, target: null, rel: null, class: null});
  for (const l of OPS.links) {
    const h = locate(tr.doc, l.find);
    if (h.length !== 1) { rep.errors.push('link "' + l.words + '": ' + h.length + ' matches of its sentence'); continue; }
    const k = l.find.indexOf(l.words);
    tr.addMark(h[0].map[h[0].i + k], h[0].map[h[0].i + k + l.words.length - 1] + 1, linkMark(l.href));
    rep.inline.push(['link', l.words]);
  }
  // 3. the blocks in their new order, with the new headings and paragraphs
  const cur = []; tr.doc.forEach(n => cur.push(n));
  const nodes = OPS.order.map(x => {
    if (x.p) return S.nodes.paragraph.create(null, x.p.filter(([t]) => t).map(([t, href]) => href ? S.text(t, [linkMark(href)]) : S.text(t)));
    // a heading that is new to the post (no block of its own): {h: [level, text]}, with the schema's defaults for the rest
    if (x.i === undefined && x.h) return S.nodes.heading.create({level: x.h[0]}, S.text(x.h[1]));
    const n = cur[x.i];
    if (!x.h) return n;
    if (n.type.name !== 'heading') { rep.errors.push('block ' + x.i + ' is not a heading'); return n; }
    return S.nodes.heading.create(Object.assign({}, n.attrs, {level: x.h[0]}), S.text(x.h[1]));
  });
  const after = nodes.filter(n => n.type.name === 'heading').map(n => [n.attrs.level, n.textContent]);
  rep.headings = after.length;
  rep.heading_diffs = OPS.expected_headings.map((x, i) => (after[i] && after[i][0] === x[0] && after[i][1] === x[1]) ? null : [i, x, after[i]]).filter(Boolean).slice(0, 12);
  if (after.length !== OPS.expected_headings.length) rep.errors.push('headings: ' + after.length + ', expected ' + OPS.expected_headings.length);
  const paras = arr => arr.filter(n => n.type.name !== 'heading').map(n => n.textContent);
  const count = arr => arr.reduce((m, t) => (m.set(t, (m.get(t) || 0) + 1), m), new Map());
  const cb = count(paras(top)), cn = count(paras(nodes));
  rep.text_gone = [...cb].filter(([t, c]) => (cn.get(t) || 0) < c).map(([t]) => t.slice(0, 90));
  rep.text_new = [...cn].filter(([t, c]) => (cb.get(t) || 0) < c).map(([t]) => t.slice(0, 90));
  rep.blocks_after = nodes.length;
  if (rep.errors.length || rep.heading_diffs.length || opt.dry) return rep;
  tr.replaceWith(0, tr.doc.content.size, nodes);
  ed.view.dispatch(tr);
  rep.dispatched = true;
  return rep;
};
