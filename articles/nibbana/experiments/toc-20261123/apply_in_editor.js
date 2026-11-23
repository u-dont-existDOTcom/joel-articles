// Joel's contents picks of 2026-11-23 (answers/JOEL-20261123-1724.json) into his post's Substack editor, as one
// ProseMirror transaction, from EDITOR-OPS.json (written by apply_plan.py from PLAN.json). Run in the post's editor tab:
//   window.__applyNibbana(ops, {dry: true})   -> the report, nothing changed
//   window.__applyNibbana(ops, {dry: false})  -> dispatched; then Update -> "Update now" (no email) in the editor
// The report lists the headings after the change against ops.expected_headings, and every paragraph whose text changed,
// so nothing but the planned changes goes in: 46 headings renamed (two also to ##), two headings removed, one section
// moved, two of his lines added at a section's top, one sentence's referent fixed, 13 section links added. Section links
// are plain links (no new tab), as the Inner Child post's are.
window.__applyNibbana = (OPS, opt) => {
  const ed = document.querySelector('.ProseMirror').editor;
  const st = ed.state, S = st.schema, tr = st.tr, rep = {errors: [], inline: []};
  const blocks = [];
  st.doc.descendants((n, pos) => { if (n.isTextblock) { blocks.push([pos, n]); return false; } return true; });
  const locate = find => {
    const hits = [];
    for (const [pos, n] of blocks) {
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
  const span = (hit, start, len) => [hit.map[hit.i + start], hit.map[hit.i + start + len - 1] + 1];
  const edits = [];
  for (const e of OPS.edit) {
    const h = locate(e.from);
    if (h.length !== 1) { rep.errors.push('edit ' + e.id + ': ' + h.length + ' matches'); continue; }
    const [from, to] = span(h[0], 0, e.from.length);
    edits.push({from, to, kind: 'text', text: e.to, what: e.id});
  }
  for (const l of OPS.links) {
    const h = locate(l.find);
    if (h.length !== 1) { rep.errors.push('link "' + l.find + '": ' + h.length + ' matches'); continue; }
    const k = l.find.indexOf(l.words);
    const [from, to] = span(h[0], k, l.words.length);
    edits.push({from, to, kind: 'link', href: l.href, what: l.words});
  }
  edits.sort((a, b) => b.from - a.from);
  for (const x of edits) {
    if (x.kind === 'text') tr.insertText(x.text, x.from, x.to);
    else tr.addMark(x.from, x.to, S.marks.link.create({href: x.href, target: null, rel: null, class: null}));
    rep.inline.push([x.kind, x.what, tr.doc.textBetween(x.from, x.kind === 'text' ? x.from + x.text.length : x.to)]);
  }
  const nodes = []; tr.doc.forEach(n => nodes.push(n));
  const hIndex = (text, level) => {
    const ix = nodes.map((n, i) => [n, i]).filter(([n]) => n.type.name === 'heading' && n.textContent === text && (level == null || n.attrs.level === level)).map(([, i]) => i);
    return ix.length === 1 ? ix[0] : -1 - ix.length;
  };
  for (const r of OPS.rename) {
    const i = hIndex(r.from, r.from_level);
    if (i < 0) { rep.errors.push('rename ' + r.id + ': ' + (-1 - i) + ' matches'); continue; }
    nodes[i] = S.nodes.heading.create(Object.assign({}, nodes[i].attrs, {level: r.to_level}), S.text(r.to));
  }
  for (const a of OPS.insert) {
    const i = hIndex(a.heading);
    if (i < 0) { rep.errors.push('insert ' + a.id + ': ' + (-1 - i) + ' matches'); continue; }
    nodes.splice(i + 1, 0, S.nodes.paragraph.create(null, S.text(a.text)));
  }
  for (const d of OPS.drop) {
    const i = hIndex(d.text, d.level);
    if (i < 0) { rep.errors.push('drop ' + d.id + ': ' + (-1 - i) + ' matches'); continue; }
    nodes.splice(i, 1);
  }
  for (const m of OPS.move) {
    const s = hIndex(m.heading);
    if (s < 0) { rep.errors.push('move ' + m.id + ': start not found'); continue; }
    let e = s + 1;
    while (e < nodes.length && nodes[e].type.name !== 'heading') e++;
    if (e === nodes.length && nodes[e - 1].type.name === 'paragraph' && !nodes[e - 1].textContent) e--;  // the doc's trailing empty line stays last
    const block = nodes.splice(s, e - s);
    const t = hIndex(m.before);
    if (t < 0) { rep.errors.push('move ' + m.id + ': target not found'); nodes.splice(s, 0, ...block); continue; }
    nodes.splice(t, 0, ...block);
    rep.moved = [m.id, block.length + ' blocks', 'before ' + m.before];
  }
  const after = nodes.filter(n => n.type.name === 'heading').map(n => [n.attrs.level, n.textContent]);
  rep.headings = after.length;
  rep.heading_diffs = OPS.expected_headings.map((x, i) => (after[i] && after[i][0] === x[0] && after[i][1] === x[1]) ? null : [i, x, after[i]]).filter(Boolean);
  const paras = d => { const out = []; d.forEach(n => { if (n.type.name !== 'heading') out.push(n.textContent); }); return out; };
  const before = paras(st.doc), now = paras({forEach: f => nodes.forEach(f)});
  const count = arr => arr.reduce((m, t) => (m.set(t, (m.get(t) || 0) + 1), m), new Map());
  const cb = count(before), cn = count(now);
  rep.text_gone = [...cb].filter(([t, c]) => (cn.get(t) || 0) < c).map(([t]) => t.slice(0, 100));
  rep.text_new = [...cn].filter(([t, c]) => (cb.get(t) || 0) < c).map(([t]) => t.slice(0, 100));
  rep.blocks = [st.doc.childCount, nodes.length];
  if (rep.errors.length || rep.heading_diffs.length || opt.dry) return rep;
  const doc2 = st.doc.type.create(st.doc.attrs, nodes);
  tr.replaceWith(0, tr.doc.content.size, doc2.content);
  ed.view.dispatch(tr);
  rep.dispatched = true;
  return rep;
};
