// update.js: run in post 176569317's editor (https://ibogaqueen.substack.com/publish/post/176569317), with
// window.__planGut = {url, sha256}: UPDATE-PLAN.json (make_plan.py) at a pushed commit on raw.githubusercontent.com, and
// window.__srcGut = the article HTML's URL at the same commit. Both are checked by SHA-256 before use. Builds one
// transaction and checks it; dispatching is a separate step (dispatch.js), only if every check passed.
await (async () => {
  const hexOf = async (s) => [...new Uint8Array(await crypto.subtle.digest('SHA-256', new TextEncoder().encode(s)))]
    .map((x) => x.toString(16).padStart(2, '0')).join('');
  const ptxt = await (await fetch(window.__planGut.url, {cache: 'no-store'})).text();
  if (await hexOf(ptxt) !== window.__planGut.sha256) return {ok: false, why: 'UPDATE-PLAN.json SHA-256'};
  const plan = JSON.parse(ptxt);
  const src = await (await fetch(window.__srcGut, {cache: 'no-store'})).text();
  if (await hexOf(src) !== plan.source.sha256) return {ok: false, why: 'source SHA-256 ' + (await hexOf(src))};
  const NAT = ['captionedImage', 'youtube2', 'paywall'];
  const PW = '@@PAYWALL@@';
  const blocks = (doc) => {
    const a = [];
    doc.descendants((n) => {
      const t = n.type.name;
      if (t === 'paywall') { a.push('<paywall>'); return false; }
      if (t === 'captionedImage') { a.push('<captionedImage>'); return false; }
      if (t === 'youtube2') { a.push('<youtube2:' + (n.attrs.videoId || '') + '>'); return false; }
      if (t === 'horizontalRule') { a.push('<horizontalRule>'); return false; }
      if (n.isTextblock) {
        const s = n.textContent.replace(/\s+/g, '');
        if (s === PW) a.push('<paywall>'); else if (s) a.push(s);
        return false;
      }
      return true;
    });
    return a;
  };
  const diff = (a, b) => { const d = []; for (let i = 0; i < Math.max(a.length, b.length) && d.length < 8; i++) if (a[i] !== b[i]) d.push([i, (a[i] || '').slice(0, 80), (b[i] || '').slice(0, 80)]); return d; };
  const els = document.querySelectorAll('.ProseMirror');
  if (els.length !== 1 || !els[0].editor) return {ok: false, why: 'not one editor'};
  const ed = els[0].editor;
  const state = ed.state;
  const doc = state.doc;
  const out = {ok: false};
  const now = blocks(doc);
  out.base = diff(now, plan.base);
  if (out.base.length) return Object.assign(out, {why: 'the editor differs from the master (his changes since 3 November?)'});
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
  out.parsed = diff(blocks(parsed), plan.after);
  if (out.parsed.length) return Object.assign(out, {why: 'the parsed source differs from the plan'});
  // the post's own native blocks, in order, from the editor as it is now
  const olds = [];
  doc.descendants((n) => { if (NAT.includes(n.type.name)) { olds.push(n); return false; } return true; });
  const tr = state.tr.replaceWith(0, doc.content.size, parsed.content);
  const spots = [];
  tr.doc.descendants((n, pos) => {
    if (NAT.includes(n.type.name)) { spots.push([pos, n]); return false; }
    if (n.isTextblock && n.textContent.trim() === PW) { spots.push([pos, n, 'paywall']); return false; }
    return true;
  });
  const kind = (n, k) => k || n.type.name;
  out.natives = spots.map(([, n, k]) => kind(n, k));
  if (spots.length !== olds.length || spots.some(([, n, k], i) => kind(n, k) !== olds[i].type.name)) return Object.assign(out, {why: 'native blocks: ' + out.natives + ' vs ' + olds.map((n) => n.type.name)});
  for (let i = 0; i < olds.length; i++) {
    if (olds[i].type.name === 'youtube2' && olds[i].attrs.videoId !== spots[i][1].attrs.videoId) return Object.assign(out, {why: 'video ' + i + ' is not the same'});
  }
  for (let i = spots.length - 1; i >= 0; i--) { const [pos, n] = spots[i]; tr.replaceWith(pos, pos + n.nodeSize, olds[i]); }
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
  if (JSON.stringify(got) !== JSON.stringify(srcLinks)) return Object.assign(out, {why: 'links differ', firstLinkDiff: diff(got, srcLinks)});
  out.blocks = plan.after.length;
  out.steps = tr.steps.length;
  out.textBefore = doc.textContent.length;
  out.textAfter = tr.doc.textContent.length;
  window.__updGut = {tr, base: doc, ed};
  return Object.assign(out, {ok: true});
})()
