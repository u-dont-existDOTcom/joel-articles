// build132.js: turn 132, in his post's editor, after probe132.js (which sets window.P132 and window.__plan132).
// Builds ONE transaction: his heading picks (text and level), the added heading, four small text fixes and the
// section links; checks it against the plan; keeps it in window.__pub132 for dispatch132.js. Changes nothing here.
await (async () => {
  const P = window.P132, plan = window.__plan132;
  if (!P || !plan) return {ok: false, why: 'run probe132.js first'};
  const ed = document.querySelector('.ProseMirror').editor, S = ed.schema, base = ed.state.doc;
  const tr = ed.state.tr;
  const ws = (s) => s.replace(/\s+/g, ' ').trim();
  const fail = (why, extra) => ({ok: false, why, ...(extra || {})});
  // 1. headings, last to first
  const want = plan.headings.filter((h) => h.from !== null);
  const H0 = P.headings(tr.doc);
  if (H0.length !== want.length) return fail('heading count', {editor: H0.length, plan: want.length});
  for (let k = want.length - 1; k >= 0; k--) {
    const h = P.headings(tr.doc)[k], w = want[k];
    if (h.level !== w.from_level || ws(h.text) !== ws(w.from)) return fail('heading ' + k + ' is not the planned one', {editor: h.text, plan: w.from});
    if (h.level !== w.level) tr.setNodeMarkup(h.pos, undefined, {...h.node.attrs, level: w.level});
    if (ws(h.text) !== ws(w.to)) {
      const n = tr.doc.nodeAt(h.pos);
      if (w.to) tr.replaceWith(h.pos + 1, h.pos + 1 + n.content.size, S.text(w.to));
      else tr.delete(h.pos + 1, h.pos + 1 + n.content.size);
    }
  }
  // 2. the added heading, before the paragraph that starts "Forced adulthood can get into your head too"
  const add = plan.headings.find((h) => h.from === null);
  const f = P.findAll(tr.doc, 'Forced adulthood can get into your head too');
  if (f.length !== 1) return fail('Forced adulthood paragraph found ' + f.length + ' times');
  if (tr.doc.resolve(f[0].pos).depth !== 0) return fail('that paragraph is not top level');
  tr.insert(f[0].pos, S.nodes.heading.create({level: add.level}, S.text(add.to)));
  // 3. text fixes: replace only the part that differs
  for (const e of plan.edits) {
    const m = P.findAll(tr.doc, e.from);
    if (m.length !== 1) return fail('edit ' + e.in + ' found ' + m.length + ' times');
    let a = 0; while (a < e.from.length && a < e.to.length && e.from[a] === e.to[a]) a++;
    let b = 0; while (b < e.from.length - a && b < e.to.length - a && e.from[e.from.length - 1 - b] === e.to[e.to.length - 1 - b]) b++;
    const from = m[0].from + a, to = m[0].to - b, mid = e.to.slice(a, e.to.length - b);
    if (mid) tr.insertText(mid, from, to); else tr.delete(from, to);
  }
  // 4. links, with the same attributes as the section link he made himself
  const attrs0 = {class: null, rel: 'noopener noreferrer nofollow', target: '_blank'};
  for (const l of plan.links) {
    const c = P.findAll(tr.doc, l.context);
    if (c.length !== 1) return fail('link context ' + l.in + ' found ' + c.length + ' times', {context: l.context});
    const t = P.findAll(tr.doc, l.text).filter((x) => x.from >= c[0].from && x.to <= c[0].to);
    if (t.length !== 1) return fail('link text ' + l.in + ' found ' + t.length + ' times in its context', {text: l.text});
    let linked = false; tr.doc.nodesBetween(t[0].from, t[0].to, (n) => { if (n.isText && n.marks.some((m) => m.type.name === 'link')) linked = true; });
    if (linked) return fail('already a link at ' + l.in, {text: l.text});
    tr.addMark(t[0].from, t[0].to, S.marks.link.create({...attrs0, href: l.href}));
  }
  // checks
  const out = {nodesBefore: base.childCount, nodesAfter: tr.doc.childCount};
  const H1 = P.headings(tr.doc);
  const wantAll = plan.headings;
  out.headingsAfter = H1.length;
  out.headingMismatch = [];
  for (let k = 0; k < Math.max(H1.length, wantAll.length); k++) {
    const a = H1[k], w = wantAll[k];
    if (!a || !w || a.level !== w.level || ws(a.text) !== ws(w.to)) out.headingMismatch.push({k, editor: a && [a.level, a.text], plan: w && [w.level, w.to]});
  }
  // every other top-level node is unchanged; the edited and linked paragraphs differ only as planned
  const hrefs = new Set(plan.links.map((l) => l.href));
  const canon = (node, drop) => {
    const out = [];
    const walk = (n) => {
      if (n.isTextblock) {
        out.push('<' + n.type.name + JSON.stringify(n.attrs) + '>');
        let cur = null;
        n.forEach((c) => {
          if (c.isText) {
            const k = c.marks.filter((m) => !(drop && m.type.name === 'link' && drop.has(m.attrs.href))).map((m) => m.type.name + JSON.stringify(m.attrs)).sort().join('|');
            if (cur && cur.k === k) cur.t += c.text; else { if (cur) out.push(cur.k + '::' + cur.t); cur = {k, t: c.text}; }
          } else { if (cur) { out.push(cur.k + '::' + cur.t); cur = null; } out.push(JSON.stringify(c.toJSON())); }
        });
        if (cur) out.push(cur.k + '::' + cur.t);
        out.push('</' + n.type.name + '>');
      } else if (n.isLeaf) {
        out.push(JSON.stringify(n.toJSON()));
      } else {
        out.push('<' + n.type.name + JSON.stringify(n.attrs) + '>');
        n.forEach(walk);
        out.push('</' + n.type.name + '>');
      }
    };
    walk(node);
    return out.join('\n');
  };
  const a = [], b = [];
  base.forEach((n) => a.push(n)); tr.doc.forEach((n) => b.push(n));
  const isAdded = (n) => n.type.name === 'heading' && n.textContent === add.to && n.attrs.level === add.level;
  const bb = b.filter((n) => !isAdded(n));
  if (bb.length !== a.length) return fail('node count after removing the added heading', {a: a.length, bb: bb.length});
  let changed = 0, editedSeen = 0; const bad = [];
  for (let i = 0; i < a.length; i++) {
    const x = a[i], y = bb[i];
    if (x.type.name === 'heading') { if (y.type.name !== 'heading' || JSON.stringify({...x.attrs, level: 0}) !== JSON.stringify({...y.attrs, level: 0})) bad.push({i, why: 'heading attrs'}); continue; }
    const cx = canon(x);
    if (cx === canon(y)) continue;
    changed++;
    let cy = canon(y, hrefs), edited = false;
    for (const e of plan.edits) { if (cy.includes(e.to) && cx.includes(e.from)) { cy = cy.split(e.to).join(e.from); edited = true; } }
    if (edited) editedSeen++;
    if (cy !== cx) bad.push({i, why: 'more than the planned change', now: y.textContent.slice(0, 90)});
  }
  const ranges = []; tr.doc.descendants((n) => { if (n.isTextblock) { let cur = null; n.forEach((c) => { const m = c.isText && c.marks.find((mm) => mm.type.name === 'link'); if (m && cur && cur.href === m.attrs.href) cur.text += c.text; else { if (cur) ranges.push(cur); cur = m ? {href: m.attrs.href, text: c.text} : null; } }); if (cur) ranges.push(cur); return false; } return true; });
  const got = plan.links.map((l) => ranges.filter((r) => r.href === l.href && r.text === l.text).length);
  out.paragraphsChanged = changed; out.editedSeen = editedSeen; out.bad = bad.slice(0, 5); out.badCount = bad.length;
  out.linksFound = got.filter((g) => g >= 1).length; out.linksPlanned = plan.links.length;
  out.sectionLinksAfter = ranges.filter((r) => r.href.includes('/i/189761959/')).length;
  out.ok = out.nodesAfter === out.nodesBefore + 1 && out.headingMismatch.length === 0 && out.badCount === 0 && out.editedSeen === plan.edits.length && out.linksFound === plan.links.length;
  if (out.ok) window.__pub132 = {tr, base, ed};
  out.headingMismatch = out.headingMismatch.slice(0, 5);
  return out;
})()
