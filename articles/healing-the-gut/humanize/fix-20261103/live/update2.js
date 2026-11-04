// update2.js: the second update of post 176569317 (gate E332): run in its editor with window.__planGut = {url, sha256}
// (UPDATE-PLAN-2.json, whose base is the HTML last put in) and window.__srcGut (the new HTML), both from a pushed commit
// and checked by SHA-256. Checks the editor against what was last put in, then replaces only the top-level nodes whose
// text changed, with the post's own native blocks carried as the same nodes; every unchanged node stays the same object.
// Dispatching is a separate step (dispatch.js), only if every check passed.
await (async () => {
  const hexOf = async (s) => [...new Uint8Array(await crypto.subtle.digest('SHA-256', new TextEncoder().encode(s)))]
    .map((x) => x.toString(16).padStart(2, '0')).join('');
  const ptxt = await (await fetch(window.__planGut.url, {cache: 'no-store'})).text();
  if (await hexOf(ptxt) !== window.__planGut.sha256) return {ok: false, why: 'plan SHA-256'};
  const plan = JSON.parse(ptxt);
  const src = await (await fetch(window.__srcGut, {cache: 'no-store'})).text();
  if (await hexOf(src) !== plan.source.sha256) return {ok: false, why: 'source SHA-256'};
  const NAT = ['captionedImage', 'youtube2', 'paywall'];
  const PW = '@@PAYWALL@@';
  const blocks = (node) => {
    const a = [];
    node.descendants((n) => {
      const t = n.type.name;
      if (t === 'paywall') { a.push('<paywall>'); return false; }
      if (t === 'captionedImage') { a.push('<captionedImage>'); return false; }
      if (t === 'youtube2') { a.push('<youtube2:' + (n.attrs.videoId || '') + '>'); return false; }
      if (t === 'horizontalRule') { a.push('<horizontalRule>'); return false; }
      if (n.isTextblock) { const s = n.textContent.replace(/\s+/g, ''); if (s === PW) a.push('<paywall>'); else if (s) a.push(s); return false; }
      return true;
    });
    return a;
  };
  // a top-level node's signature: its own text if it is a paragraph or heading, else every block inside it (a list's items)
  const sigOf = (n) => n.type.name + '|' + (n.isTextblock ? n.textContent.replace(/\s+/g, '') : JSON.stringify(blocks(n)));
  const diff = (a, b) => { const d = []; for (let i = 0; i < Math.max(a.length, b.length) && d.length < 8; i++) if (a[i] !== b[i]) d.push([i, (a[i] || '').slice(0, 80), (b[i] || '').slice(0, 80)]); return d; };
  const els = document.querySelectorAll('.ProseMirror');
  if (els.length !== 1 || !els[0].editor) return {ok: false, why: 'not one editor'};
  const ed = els[0].editor;
  const state = ed.state;
  const doc = state.doc;
  const out = {ok: false};
  out.base = diff(blocks(doc), plan.base);
  if (out.base.length) return Object.assign(out, {why: 'the editor differs from what was last put in (his changes since?)'});
  let parser = ed.schema.cached && ed.schema.cached.domParser;
  if (!parser) { ed.can().setContent('<p>x</p>'); parser = ed.schema.cached.domParser; }
  if (!parser || ed.state.doc !== doc) return Object.assign(out, {why: 'no parser, or the doc changed'});
  const body = new window.DOMParser().parseFromString('<!doctype html><body>' + src + '</body>', 'text/html').body;
  body.querySelectorAll('br.ProseMirror-trailingBreak').forEach((b) => b.remove());
  const pws = body.querySelectorAll('.paywall-editor');
  if (pws.length !== 1) return Object.assign(out, {why: pws.length + ' paywalls in the source'});
  const ph = document.createElement('p'); ph.textContent = PW; pws[0].replaceWith(ph);
  const root = body.querySelector('.ProseMirror') || body;
  const parsed = parser.parse(root);
  // the new document, built aside (never dispatched), with the editor's own native nodes in place of the parsed ones
  const olds = [];
  doc.descendants((n) => { if (NAT.includes(n.type.name)) { olds.push(n); return false; } return true; });
  const scratch = state.tr.replaceWith(0, doc.content.size, parsed.content);
  const spots = [];
  scratch.doc.descendants((n, pos) => {
    if (NAT.includes(n.type.name)) { spots.push([pos, n, n.type.name]); return false; }
    if (n.isTextblock && n.textContent.trim() === PW) { spots.push([pos, n, 'paywall']); return false; }
    return true;
  });
  if (spots.length !== olds.length || spots.some((s, i) => s[2] !== olds[i].type.name)) return Object.assign(out, {why: 'native blocks do not line up'});
  for (let i = 0; i < olds.length; i++) if (olds[i].type.name === 'youtube2' && olds[i].attrs.videoId !== spots[i][1].attrs.videoId) return Object.assign(out, {why: 'video ' + i});
  for (let i = spots.length - 1; i >= 0; i--) { const [pos, n] = spots[i]; scratch.replaceWith(pos, pos + n.nodeSize, olds[i]); }
  const nd = scratch.doc;
  // Substack puts an empty paragraph above a picture that opens the post when the editor loads (seen 2026-11-04 after
  // the first update): keep such leading empty paragraphs and line the rest up
  let off = doc.childCount - nd.childCount;
  out.leadingEmpty = off;
  if (off < 0 || [...Array(off).keys()].some((i) => doc.child(i).type.name !== 'paragraph' || doc.child(i).content.size)) return Object.assign(out, {why: 'top-level nodes ' + nd.childCount + ' vs ' + doc.childCount});
  // only the top-level nodes whose text changed
  const changed = [];
  for (let i = 0; i < nd.childCount; i++) if (sigOf(doc.child(i + off)) !== sigOf(nd.child(i))) changed.push(i + off);
  const pos = [0];
  for (let i = 0; i < doc.childCount; i++) pos.push(pos[i] + doc.child(i).nodeSize);
  const tr = state.tr;
  for (let k = changed.length - 1; k >= 0; k--) { const i = changed[k]; tr.replaceWith(pos[i], pos[i + 1], nd.child(i - off)); }
  out.changedTop = changed;
  const unchangedSame = [];
  for (let i = 0; i < doc.childCount; i++) if (!changed.includes(i)) unchangedSame.push(tr.doc.child(i) === doc.child(i));
  out.unchangedKept = unchangedSame.every(Boolean);
  if (!out.unchangedKept) return Object.assign(out, {why: 'an unchanged node was not kept'});
  const after = [];
  tr.doc.descendants((n) => { if (NAT.includes(n.type.name)) { after.push(n); return false; } return true; });
  out.carried = after.length === olds.length && after.every((n, i) => n === olds[i]);
  if (!out.carried) return Object.assign(out, {why: 'the native blocks are not the same nodes'});
  out.after = diff(blocks(tr.doc), plan.after);
  if (out.after.length) return Object.assign(out, {why: 'the result differs from the plan'});
  const links = (d) => { const a = []; d.descendants((n) => { if (n.isText) n.marks.forEach((m) => { if (m.type.name === 'link') a.push(m.attrs.href); }); }); return a; };
  const srcLinks = [...root.querySelectorAll('a[href]')].filter((a) => !a.closest('.captioned-image-container, .youtube-wrap')).map((a) => a.getAttribute('href'));
  const got = links(tr.doc).filter((h, i, arr) => i === 0 || h !== arr[i - 1]);
  out.links = [got.length, srcLinks.length];
  if (JSON.stringify(got) !== JSON.stringify(srcLinks)) return Object.assign(out, {why: 'links differ'});
  out.steps = tr.steps.length;
  window.__updGut = {tr, base: doc, ed};
  return Object.assign(out, {ok: true});
})()
