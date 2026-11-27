// update.js: run in post 197034035's editor (https://ibogaqueen.substack.com/publish/post/197034035), in the desktop
// app's browser pane, with window.__planRomance = {url, sha256}: r51/UPDATE-PLAN.json (make_update.py) at a pushed commit
// on raw.githubusercontent.com, checked by its SHA-256 before use. It builds one transaction and checks it; nothing here
// changes the editor (the parser is built with ed.can(), which never dispatches). Dispatching is dispatch.js, only after
// every check passed; the live post changes only with Update (tools/humanization/substack_update.js, no email).
//
// What the transaction does (make_update.py has the why): the editor's paragraph list (the post page's: p, li, h2 to h4,
// in order; a button's text as a paragraph, the Subscribe button at the end left out) is checked against the plan's
// fingerprints first; each changed paragraph takes its new paragraphs, parsed with the editor's own schema (an empty
// list removes it, and only a paragraph at the top level may be removed or split); the reel and the video go in as new
// blocks; then every text in the post gets the typography swap (swap_text of tools/humanization/typography_swap.py,
// ported below, each mark kept on its own characters). The result's paragraph list must equal the plan's, and its
// native blocks must be the plan's count.
await (async () => {
  const hexOf = async (s) => [...new Uint8Array(await crypto.subtle.digest('SHA-256', new TextEncoder().encode(s)))]
    .map((x) => x.toString(16).padStart(2, '0')).join('');
  const P = window.__planRomance || {};
  const ptxt = await (await fetch(P.url, {cache: 'no-store'})).text();
  if (await hexOf(ptxt) !== P.sha256) return {ok: false, why: 'UPDATE-PLAN.json SHA-256'};
  const plan = JSON.parse(ptxt);
  const ed = [...document.querySelectorAll('.ProseMirror')].map((e) => e.editor).find(Boolean);
  if (!ed) return {ok: false, why: 'no editor'};
  if (!location.pathname.endsWith('/' + plan.post)) return {ok: false, why: 'not post ' + plan.post + "'s editor"};
  const S = ed.schema;
  const state = ed.state;
  const doc = state.doc;
  const Fragment = doc.content.constructor;
  const norm = (s) => s.replace(/\s+/g, ' ').trim();
  const strip = (s) => s.replace(/\s+/g, '');
  const textOf = (n) => n.textBetween(0, n.content.size, '', '\n');
  const NAT = ['captionedImage', 'youtube2', 'instagram', 'button', 'horizontalRule'];
  // the paragraph list, as the post page has it
  const list = (d) => {
    const out = [];
    d.descendants((n, pos) => {
      const t = n.type.name;
      if (t === 'heading') { if (n.attrs.level >= 2 && n.attrs.level <= 4) out.push({tag: 'H' + n.attrs.level, text: textOf(n), pos, node: n}); return false; }
      if (t === 'button') { out.push({tag: 'P', text: n.attrs.text || '', pos, node: n, button: true}); return false; }
      if (t === 'listItem') { out.push({tag: 'LI', text: textOf(n), pos, node: n}); return true; }
      if (t === 'paragraph') { const tx = textOf(n); if (norm(tx)) out.push({tag: 'P', text: tx, pos, node: n}); return false; }
      if (NAT.includes(t) || t === 'image2') return false;
      return true;
    });
    return out;
  };
  const out = {ok: false};
  const before = list(doc);
  while (before.length > plan.index.length && before[before.length - 1].button) before.pop();
  if (before.length !== plan.index.length) return Object.assign(out, {why: 'the editor has ' + before.length + ' paragraphs, the index ' + plan.index.length});
  const bad = [];
  for (let i = 0; i < before.length; i++) {
    if (before[i].tag !== plan.index[i][1]) bad.push(i + ' tag ' + before[i].tag);
    else if ((await hexOf(norm(before[i].text))).slice(0, 12) !== plan.index[i][2]) bad.push(i);
  }
  if (bad.length) return Object.assign(out, {why: bad.length + ' paragraphs differ from the index (his changes since the index?)', bad: bad.slice(0, 12)});
  let parser = S.cached && S.cached.domParser;
  if (!parser) { ed.can().setContent('<p>x</p>'); parser = S.cached.domParser; }
  if (!parser || ed.state.doc !== doc) return Object.assign(out, {why: 'no parser, or the document changed'});
  const parsePs = (htmls) => {
    const body = new window.DOMParser().parseFromString('<!doctype html><body>' + htmls.map((h) => '<p>' + h + '</p>').join('') + '</body>', 'text/html').body;
    return parser.parse(body).content;
  };
  const jobs = [];
  for (const o of plan.ops) {
    let target = before[o.n];
    if (o.tag === 'LI') {
      target = before[o.n + 1];
      if (!target || target.tag !== 'P' || o.html.length !== 1) return Object.assign(out, {why: 'list item ' + o.n + ': not one paragraph after its LI'});
    }
    if (!target || target.button || target.node.type.name !== 'paragraph') return Object.assign(out, {why: 'paragraph ' + o.n + ' is not a paragraph'});
    const parent = doc.resolve(target.pos).parent.type.name;
    if (o.html.length !== 1 && parent !== 'doc') return Object.assign(out, {why: 'paragraph ' + o.n + ' (in a ' + parent + ') is removed or split'});
    const frag = parsePs(o.html);
    if (frag.childCount !== o.html.length || [...Array(frag.childCount).keys()].some((k) => frag.child(k).type.name !== 'paragraph')) return Object.assign(out, {why: 'paragraph ' + o.n + ' parsed to ' + frag.childCount + ' blocks'});
    jobs.push({n: o.n, pos: target.pos, node: target.node, frag, parent});
  }
  for (const e of plan.embeds) {
    const j = jobs.find((x) => x.n === e.after);
    if (!j || j.parent !== 'doc') return Object.assign(out, {why: 'the block after ' + e.after + ' has no top-level paragraph to follow'});
    j.frag = j.frag.addToEnd(S.nodes[e.type].create(e.attrs));
  }
  jobs.sort((a, b) => b.pos - a.pos);
  const tr = state.tr;
  for (const j of jobs) {
    if (j.frag.childCount) tr.replaceWith(j.pos, j.pos + j.node.nodeSize, j.frag);
    else tr.delete(j.pos, j.pos + j.node.nodeSize);
  }
  // the typography swap, every text block, each line (a run between line breaks) on its own, as swap_text does
  const QUOTE = {'‘': "'", '’': "'", '“': '"', '”': '"'};
  const DASH = /[  ]*—[  ]*|[  ]+–[  ]*|–[  ]+/g;
  const swapLine = (nodes) => {
    const ch = [], seg = [];
    nodes.forEach((t, i) => { for (let k = 0; k < t.text.length; k++) { ch.push(QUOTE[t.text[k]] || t.text[k]); seg.push(i); } });
    for (let k = 1; k + 1 < ch.length; k++) if (ch[k] === '—' && /\d/.test(ch[k - 1]) && /\d/.test(ch[k + 1])) ch[k] = '–';
    const src = ch.join('');
    const oc = [], os = [];
    let last = 0;
    for (const m of src.matchAll(DASH)) {
      for (let k = last; k < m.index; k++) { oc.push(ch[k]); os.push(seg[k]); }
      const end = m.index + m[0].length;
      const dashAt = m.index + m[0].search(/[–—]/);
      let r;
      if (m[0].includes('–') && /\d[A-Za-z%°]{0,3}$/.test(src.slice(0, m.index)) && /^\d/.test(src.slice(end))) r = null;
      else {
        const b = m.index ? src[m.index - 1] : '\n';
        const a = end < src.length ? src[end] : '\n';
        r = b === '\n' ? '-- ' : a === '\n' ? ' --' : '--';
      }
      if (r === null) { for (let k = m.index; k < end; k++) { oc.push(ch[k]); os.push(seg[k]); } }
      else for (const c of r) { oc.push(c); os.push(seg[dashAt]); }
      last = end;
    }
    for (let k = last; k < ch.length; k++) { oc.push(ch[k]); os.push(seg[k]); }
    const before = nodes.map((t) => t.text).join('');
    if (oc.join('') === before) return {changed: false, nodes};
    const res = [];
    let k = 0;
    while (k < oc.length) {
      let e = k;
      while (e < oc.length && os[e] === os[k]) e++;
      res.push(S.text(oc.slice(k, e).join(''), nodes[os[k]].marks));
      k = e;
    }
    return {changed: true, nodes: res};
  };
  const blocks = [];
  tr.doc.descendants((n, pos) => { if (n.isTextblock) { blocks.push([pos, n]); return false; } return true; });
  let swapped = 0;
  for (let i = blocks.length - 1; i >= 0; i--) {
    const [pos, n] = blocks[i];
    const items = [];
    n.forEach((c) => items.push(c));
    const res = [];
    let line = [], changed = false;
    const flush = () => { if (line.length) { const r = swapLine(line); changed = changed || r.changed; res.push(...r.nodes); line = []; } };
    for (const c of items) { if (c.isText) line.push(c); else { flush(); res.push(c); } }
    flush();
    if (changed) { tr.replaceWith(pos + 1, pos + 1 + n.content.size, Fragment.from(res)); swapped++; }
  }
  // the checks
  const after = list(tr.doc);
  while (after.length > plan.expected_after.length && after[after.length - 1].button) after.pop();
  const got = after.map((x) => strip(x.text));
  const diff = [];
  for (let i = 0; i < Math.max(got.length, plan.expected_after.length) && diff.length < 8; i++) {
    if (got[i] !== plan.expected_after[i]) diff.push([i, (got[i] || '').slice(0, 90), (plan.expected_after[i] || '').slice(0, 90)]);
  }
  out.paragraphs = [got.length, plan.expected_after.length];
  if (diff.length) return Object.assign(out, {why: 'the result differs from the plan', diff});
  const count = (d) => { const c = {}; d.descendants((n) => { if (NAT.includes(n.type.name)) { c[n.type.name] = (c[n.type.name] || 0) + 1; return false; } return true; }); return c; };
  out.natives = count(tr.doc);
  for (const [k, v] of Object.entries(plan.natives_after)) if (out.natives[k] !== v) return Object.assign(out, {why: 'native blocks ' + JSON.stringify(out.natives)});
  const links = (d) => { const a = []; d.descendants((n) => { if (n.isText) n.marks.forEach((m) => { if (m.type.name === 'link') a.push(m.attrs.href); }); }); return a; };
  out.links = [links(doc).length, links(tr.doc).length];
  out.curly_left = (tr.doc.textContent.match(/[‘’“”]/g) || []).length;
  out.emdash_left = (tr.doc.textContent.match(/—/g) || []).length;
  out.swapped_blocks = swapped;
  out.steps = tr.steps.length;
  out.text = [doc.textContent.length, tr.doc.textContent.length];
  window.__updRomance = {tr, base: doc, ed};
  return Object.assign(out, {ok: true});
})()
