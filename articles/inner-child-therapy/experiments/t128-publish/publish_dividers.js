// publish_dividers.js: turn 128, in his post's editor (https://ibogaqueen.substack.com/publish/post/189761959), with
// window.__plan128 = the contents of PLAN-2.json. A divider (horizontalRule) before every h1 heading but the first, and
// the four paragraphs whose whitespace-free text hashes are the plan's made pull quote blocks; one transaction, built and
// checked here (the whole text the same before and after, the counts the plan's), kept in window.__pub128 for
// publish_dispatch128 (the same check as publish_dispatch.js: dispatch only if the document is still the one it was built on).
await (async () => {
  const plan = window.__plan128;
  if (!plan) return {ok: false, why: 'no plan'};
  const sha = async (s) => [...new Uint8Array(await crypto.subtle.digest('SHA-256', new TextEncoder().encode(s)))].map((x) => x.toString(16).padStart(2, '0')).join('');
  const WS = new Set([0x20, 0x09, 0x0a, 0x0d, 0x0c, 0x0b, 0x85, 0xa0, 0x1680, 0x2028, 0x2029, 0x202f, 0x205f, 0x3000, 0xfeff, 0x1c, 0x1d, 0x1e, 0x1f, 0x2000, 0x2001, 0x2002, 0x2003, 0x2004, 0x2005, 0x2006, 0x2007, 0x2008, 0x2009, 0x200a]);
  const strip = (s) => [...s].filter((c) => !WS.has(c.codePointAt(0))).join('');
  const els = document.querySelectorAll('.ProseMirror');
  if (els.length !== 1 || !els[0].editor) return {ok: false, why: 'not one editor'};
  const ed = els[0].editor;
  const S = ed.schema;
  const doc = ed.state.doc;
  if (doc.childCount !== plan.base.nodes) return {ok: false, why: 'the editor has ' + doc.childCount + ' nodes'};
  const want = new Map(plan.pullquotes.map((p) => [p.sig, p]));
  const found = new Set();
  const nodes = [];
  let h1 = 0;
  for (let i = 0; i < doc.childCount; i++) {
    const n = doc.child(i);
    if (n.type.name === 'heading' && n.attrs.level === 1) {
      h1++;
      if (h1 > 1) nodes.push(S.nodes.horizontalRule.create());
    }
    if (n.type.name === 'paragraph') {
      const s = (await sha(strip(n.textContent))).slice(0, 12);
      if (want.has(s)) {
        if (found.has(s)) return {ok: false, why: 'a pull quote paragraph twice'};
        found.add(s);
        nodes.push(S.nodes.pullquote.create(null, [n]));
        continue;
      }
    }
    nodes.push(n);
  }
  if (found.size !== plan.pullquotes.length) return {ok: false, why: 'found ' + found.size + ' of the pull quote paragraphs'};
  const tr = ed.state.tr.replaceWith(0, doc.content.size, doc.content.constructor.from(nodes));
  const count = (t) => { let c = 0; tr.doc.forEach((n) => { if (n.type.name === t) c++; }); return c; };
  const out = {nodesBefore: doc.childCount, nodesAfter: tr.doc.childCount, horizontalRule: count('horizontalRule'), pullquote: count('pullquote'),
    sameText: (await sha(strip(doc.textContent))) === (await sha(strip(tr.doc.textContent))), h1};
  out.ok = out.nodesAfter === plan.after.nodes && out.horizontalRule === plan.after.horizontalRule && out.pullquote === plan.after.pullquote && out.sameText;
  const kids = [];
  tr.doc.forEach((n) => kids.push(n));
  out.rulesBefore = kids.map((n, i) => (n.type.name === 'horizontalRule' ? kids[i + 1].textContent.slice(0, 40) : null)).filter(Boolean);
  out.quotes = kids.filter((n) => n.type.name === 'pullquote').map((n) => n.textContent.slice(0, 50));
  if (out.ok) window.__pub128 = {tr, base: doc, ed};
  return out;
})()
