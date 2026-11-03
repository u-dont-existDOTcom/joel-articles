// update.js: run in the post's editor, with window.__plan1103 = {url, sha256}: UPDATE-PLAN.json (make_update.py) at a pushed
// commit on raw.githubusercontent.com, checked by its SHA-256 before use. Builds the one transaction and checks it;
// dispatching is a separate step (dispatch.js), only if every check passed.
await (async () => {
  const src = window.__plan1103;
  const txt = await (await fetch(src.url, {cache: 'no-store'})).text();
  const got = [...new Uint8Array(await crypto.subtle.digest('SHA-256', new TextEncoder().encode(txt)))]
    .map((x) => x.toString(16).padStart(2, '0')).join('');
  if (got !== src.sha256) return {ok: false, why: 'UPDATE-PLAN.json SHA-256 ' + got};
  const plan = JSON.parse(txt);
  const WS = /[ \t\n\r\f\v   -     　﻿\x85\x1c-\x1f]+/g;
  const hex = async (s) => [...new Uint8Array(await crypto.subtle.digest('SHA-256', new TextEncoder().encode(s.replace(WS, ''))))]
    .map((x) => x.toString(16).padStart(2, '0')).join('').slice(0, 6);
  const sig = async (node, exp) => (exp.startsWith('t:') ? 't:' + node.type.name : await hex(node.textContent));
  const els = document.querySelectorAll('.ProseMirror');
  if (els.length !== 1 || !els[0].editor) return {ok: false, why: 'not one editor'};
  const ed = els[0].editor;
  const state = ed.state;
  const doc = state.doc;
  const kids = [];
  doc.forEach((n) => kids.push(n));
  const out = {ok: false, nodes: kids.length};
  if (kids.length !== plan.base.length) return Object.assign(out, {why: 'node count ' + kids.length + ' != ' + plan.base.length});
  const baseMiss = [];
  for (let i = 0; i < kids.length; i++) {
    const s = await sig(kids[i], plan.base[i]);
    if (s !== plan.base[i]) baseMiss.push([i, kids[i].type.name, plan.base[i], s, kids[i].textContent.slice(0, 80)]);
  }
  out.baseMismatches = baseMiss.slice(0, 20);
  if (baseMiss.length) return Object.assign(out, {why: baseMiss.length + ' nodes differ from 2 November'});
  let parser = ed.schema.cached && ed.schema.cached.domParser;
  out.parserWasCached = !!parser;
  if (!parser) {
    ed.can().setContent('<p>x</p>');   // no dispatch: only builds (and caches) the schema's DOM parser
    parser = ed.schema.cached.domParser;
  }
  if (!parser || ed.state.doc !== doc) return Object.assign(out, {why: 'no parser, or the doc changed'});
  const pos = [0];
  for (const k of kids) pos.push(pos[pos.length - 1] + k.nodeSize);
  const tr = state.tr;
  const counts = [];
  for (const op of [...plan.ops].sort((a, b) => b.e1 - a.e1)) {
    if (op.n === 0) { tr.delete(pos[op.e1], pos[op.e2]); counts.push([op.e1, 0]); continue; }
    const body = new window.DOMParser().parseFromString('<!doctype html><body>' + op.html + '</body>', 'text/html').body;
    const frag = parser.parse(body).content;
    counts.push([op.e1, frag.childCount, op.n]);
    if (frag.childCount !== op.n) return Object.assign(out, {why: 'range at ' + op.e1 + ' parsed to ' + frag.childCount + ' nodes, not ' + op.n});
    if (op.e1 === op.e2) tr.insert(pos[op.e1], frag); else tr.replaceWith(pos[op.e1], pos[op.e2], frag);
  }
  const after = [];
  tr.doc.forEach((n) => after.push(n));
  out.after = after.length;
  if (after.length !== plan.after.length) return Object.assign(out, {why: 'after: ' + after.length + ' nodes, not ' + plan.after.length});
  const afterMiss = [];
  for (let i = 0; i < after.length; i++) {
    const s = await sig(after[i], plan.after[i]);
    if (s !== plan.after[i]) afterMiss.push([i, after[i].type.name, plan.after[i], s, after[i].textContent.slice(0, 80)]);
  }
  out.afterMismatches = afterMiss.slice(0, 20);
  if (afterMiss.length) return Object.assign(out, {why: afterMiss.length + ' nodes differ from today\'s blocks'});
  const natives = ['button', 'youtube2', 'captionedImage', 'digestPostEmbed'];
  const nb = kids.filter((n) => natives.includes(n.type.name));
  const na = after.filter((n) => natives.includes(n.type.name));
  out.natives = na.map((n) => n.type.name);
  if (nb.length !== 6 || na.length !== 6 || nb.some((n, i) => n !== na[i])) return Object.assign(out, {why: 'the six native blocks are not carried over as they are'});
  out.steps = tr.steps.length;
  out.textBefore = doc.textContent.length;
  out.textAfter = tr.doc.textContent.length;
  window.__upd1103 = {tr, base: doc, ed};
  return Object.assign(out, {ok: true});
})()
