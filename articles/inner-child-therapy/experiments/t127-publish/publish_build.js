// publish_build.js: run in his post's editor (https://ibogaqueen.substack.com/publish/post/189761959) with
// window.__plan127 = {url, sha256}: PUBLISH-PLAN.json (make_publish.py) at a pushed commit on raw.githubusercontent.com,
// checked by its SHA-256 before use. Builds the one transaction that makes the post's body the plan's, and checks it
// node by node; dispatching is a separate step (publish_dispatch.js), only if every check passed. Nothing here changes
// the editor: the parser is built with ed.can(), which never dispatches, and the document is compared before and after.
await (async () => {
  const src = window.__plan127;
  const txt = await (await fetch(src.url, {cache: 'no-store'})).text();
  const sha = async (s) => [...new Uint8Array(await crypto.subtle.digest('SHA-256', new TextEncoder().encode(s)))]
    .map((x) => x.toString(16).padStart(2, '0')).join('');
  if ((await sha(txt)) !== src.sha256) return {ok: false, why: 'PUBLISH-PLAN.json SHA-256 is not the one given'};
  const plan = JSON.parse(txt);
  const WS = new Set([0x20, 0x09, 0x0a, 0x0d, 0x0c, 0x0b, 0x85, 0xa0, 0x1680, 0x2028, 0x2029, 0x202f, 0x205f, 0x3000, 0xfeff,
    0x1c, 0x1d, 0x1e, 0x1f, 0x2000, 0x2001, 0x2002, 0x2003, 0x2004, 0x2005, 0x2006, 0x2007, 0x2008, 0x2009, 0x200a]);
  const strip = (s) => [...s].filter((c) => !WS.has(c.codePointAt(0))).join('');
  const NATIVE = ['captionedImage', 'video', 'audio', 'youtube2', 'digestPostEmbed'];
  const els = document.querySelectorAll('.ProseMirror');
  if (els.length !== 1 || !els[0].editor) return {ok: false, why: 'not one editor'};
  const ed = els[0].editor;
  const S = ed.schema;
  const state = ed.state;
  const doc = state.doc;
  const out = {ok: false, nodesBefore: doc.childCount};
  if (doc.childCount !== plan.base.nodes) return Object.assign(out, {why: 'the editor has ' + doc.childCount + ' nodes, not ' + plan.base.nodes});
  if ((await sha(JSON.stringify(doc.toJSON()))) !== plan.base.doc_json_sha256) return Object.assign(out, {why: 'the editor document is not the one the plan was made from'});
  let parser = S.cached && S.cached.domParser;
  if (!parser) {
    ed.can().setContent('<p>x</p>');   // no dispatch: only builds (and caches) the schema's DOM parser
    parser = S.cached.domParser;
  }
  if (!parser || ed.state.doc !== doc) return Object.assign(out, {why: 'no parser, or the doc changed'});
  const parse = (h) => parser.parse(new window.DOMParser().parseFromString('<!doctype html><body>' + h + '</body>', 'text/html').body).content;
  const old = [];
  doc.forEach((n) => old.push(n));
  const used = new Set();
  const find = (pred, what) => {
    const m = old.filter(pred);
    if (m.length !== 1) throw new Error(what + ': ' + m.length + ' matches in the post');
    if (used.has(m[0])) throw new Error(what + ': used twice');
    used.add(m[0]);
    return m[0];
  };
  const nodes = [];
  try {
    for (const it of plan.items) {
      if (it.k === 'html') {
        const f = parse(it.html);
        if (f.childCount !== it.n) throw new Error('a chunk parsed to ' + f.childCount + ' nodes, not ' + it.n);
        f.forEach((n) => nodes.push(n));
      } else if (it.k === 'pullquote') {
        const f = parse(it.html);
        if (f.childCount !== 1 || f.firstChild.type.name !== 'paragraph') throw new Error('the pull quote is not one paragraph');
        nodes.push(S.nodes.pullquote.create(null, f));
      } else if (it.k === 'divider') {
        nodes.push(S.nodes.horizontalRule.create());
      } else if (it.k === 'new_youtube') {
        nodes.push(S.nodes.youtube2.create({videoId: it.videoId, startTime: it.startTime, endTime: null}));
      } else if (it.k === 'new_image') {
        nodes.push(S.nodes.captionedImage.create(null, [S.nodes.image2.create({src: it.src, width: it.width, height: it.height, bytes: it.bytes, type: it.type})]));
      } else if (it.k === 'carry') {
        let n;
        if (it.type === 'captionedImage') n = find((x) => x.type.name === 'captionedImage' && x.firstChild && x.firstChild.attrs.src === it.src, it.src);
        else if (it.type === 'video' || it.type === 'audio') n = find((x) => x.type.name === it.type && x.attrs.mediaUploadId === it.mediaUploadId, it.type + ' ' + it.mediaUploadId);
        else if (it.type === 'youtube2') n = find((x) => x.type.name === 'youtube2' && x.attrs.videoId === it.videoId, 'YouTube ' + it.videoId);
        else if (it.type === 'digestPostEmbed') n = find((x) => x.type.name === 'digestPostEmbed' && x.attrs.canonical_url === it.canonical_url, it.canonical_url);
        else throw new Error('an unknown native ' + it.type);
        if (it.caption !== undefined && n.textContent !== it.caption) throw new Error('the caption is "' + n.textContent + '"');
        if (it.type === 'youtube2' && it.startTime && n.attrs.startTime !== it.startTime) n = n.type.create(Object.assign({}, n.attrs, {startTime: it.startTime}));
        nodes.push(n);
      } else throw new Error('an unknown item ' + it.k);
    }
  } catch (e) {
    return Object.assign(out, {why: String(e)});
  }
  const oldNatives = old.filter((n) => NATIVE.includes(n.type.name));
  if (used.size !== plan.carried || oldNatives.some((n) => !used.has(n))) return Object.assign(out, {why: 'not every native block of the post is carried over once'});
  const tr = state.tr.replaceWith(0, doc.content.size, doc.content.constructor.from(nodes));
  const after = [];
  tr.doc.forEach((n) => after.push(n));
  out.nodesAfter = after.length;
  if (after.length !== plan.after.length) return Object.assign(out, {why: after.length + ' nodes after, not ' + plan.after.length});
  const miss = [];
  for (let i = 0; i < after.length; i++) {
    const n = after[i];
    const s = NATIVE.includes(n.type.name) ? 't:' + n.type.name : (await sha(strip(n.textContent))).slice(0, 6);
    if (s !== plan.after[i]) miss.push([i, n.type.name, plan.after[i], s, n.textContent.slice(0, 80)]);
  }
  out.mismatches = miss.slice(0, 12);
  if (miss.length) return Object.assign(out, {why: miss.length + ' nodes differ from the plan'});
  const links = [];
  let bold = 0;
  let italic = 0;
  const levels = {};
  tr.doc.descendants((n) => {
    if (n.type.name === 'heading') levels[n.attrs.level] = (levels[n.attrs.level] || 0) + 1;
    if (n.isTextblock) {
      let prev = null;
      n.forEach((c) => {
        const l = c.marks.find((m) => m.type.name === 'link');
        const href = l ? l.attrs.href : null;
        if (c.isText) {
          if (href && href !== prev) links.push(href);
          if (c.marks.some((m) => m.type.name === 'bold')) bold += c.text.length;
          if (c.marks.some((m) => m.type.name === 'italic')) italic += c.text.length;
        }
        prev = c.isText ? href : prev;
      });
      return false;
    }
    return true;
  });
  const linkMiss = links.length !== plan.links.length || links.some((h, i) => h !== plan.links[i]);
  out.counts = {links: links.length, bold, italic, levels};
  if (linkMiss) return Object.assign(out, {why: 'the links differ from the plan', firstLinkDiff: links.findIndex((h, i) => h !== plan.links[i])});
  const want = plan.counts;
  if (bold !== want.bold || italic !== want.italic || JSON.stringify(levels) !== JSON.stringify(Object.fromEntries(Object.entries(want.headings).map(([k, v]) => [Number(k), v])))) {
    return Object.assign(out, {why: 'the emphasis or headings differ', want});
  }
  const fullSha = await sha(strip(tr.doc.textContent));
  if (fullSha !== plan.text_sha256_no_whitespace) return Object.assign(out, {why: 'the whole text is not round 11\'s'});
  out.natives = after.filter((n) => NATIVE.includes(n.type.name)).map((n) => n.type.name);
  out.steps = tr.steps.length;
  out.textBefore = doc.textContent.length;
  out.textAfter = tr.doc.textContent.length;
  window.__pub127 = {tr, base: doc, ed};
  return Object.assign(out, {ok: true});
})()
