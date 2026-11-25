// same_post_links.js - turn a post's links to its own sections from the /i/ form, which loads the whole page again when
// a reader clicks it, into "#§<slug>", which only scrolls (lesson toc-2026-11-25c; Joel, 2026-11-25 11:18 UTC: "i notice
// that your anchor links are reloading the whole page, don't you need to fix them to be just # without the url before
// it?"). tools/humanization/section_links.py has the rule and what was tested.
//
// Run in the post's editor tab (/publish/post/<id>), in the desktop app's browser pane:
//   await window.__samePostLinks({dry: true})    -> the report, nothing changed
//   await window.__samePostLinks({dry: false})   -> dispatched; then Update -> "Update now" (no email) in the editor,
//                                                   with the post's date (gate E323)
// It refuses to change anything when the editor's text is not the published post's text (someone's unpublished edit is
// sitting in the draft, and Update would publish it), or when a link's slug has no heading in the post.
// After the update, on the public page:  await window.__samePostLinksCheck()   -> every "#§" link has its heading.
window.__slug = h => h.replace(/\s+/g, ' ').toLowerCase().replace(/&/g, ' and ').normalize('NFKD').replace(/[̀-ͯ]/g, '')
  .replace(/[^a-z0-9 -]/g, '').replace(/ /g, '-').replace(/-+/g, '-').replace(/^-|-$/g, '');
window.__samePostLinks = async (opt) => {
  const id = (location.pathname.match(/\/publish\/post\/(\d+)/) || [])[1];
  if (!id) return {error: 'open the post\'s editor first'};
  const ed = document.querySelector('.ProseMirror').editor, st = ed.state, tr = st.tr, S = st.schema;
  const rep = {post: id, errors: [], changed: []};
  const norm = t => t.replace(/\s+/g, '');
  const live = await fetch('/api/v1/posts/by-id/' + id, {credentials: 'include'}).then(r => r.json());
  const div = document.createElement('div'); div.innerHTML = (live.post || live).body_html || '';
  div.querySelectorAll('.header-anchor-parent, .image-link-expand, button, style, script').forEach(e => e.remove());
  const blocks = t => t.length;
  const liveText = norm([...div.children].filter(e => /^(P|H[1-6]|BLOCKQUOTE|UL|OL)$/.test(e.tagName) && !e.classList.contains('button-wrapper')).map(e => e.textContent).join(''));
  const edParts = []; st.doc.forEach(n => { if (['paragraph', 'heading', 'blockquote', 'bulletList', 'orderedList'].includes(n.type.name)) edParts.push(n.textContent); });
  const edText = norm(edParts.join(''));
  rep.text = {editor: edText.length, live: liveText.length, same: edText === liveText};
  if (!rep.text.same) {
    let k = 0; while (k < edText.length && edText[k] === liveText[k]) k++;
    rep.errors.push('the editor\'s text is not the published post\'s (first difference at character ' + k + ': editor "' + edText.slice(k, k + 60) + '", live "' + liveText.slice(k, k + 60) + '")');
  }
  const slugs = new Set(); st.doc.descendants(n => { if (n.type.name === 'heading') slugs.add(window.__slug(n.textContent)); return true; });
  const re = new RegExp('^https?://[^/]+/i/' + id + '/([a-z0-9-]+)/?$');
  st.doc.descendants((n, pos) => {
    if (!n.isText) return true;
    const m = n.marks.find(x => x.type.name === 'link');
    const hit = m && re.exec(m.attrs.href || '');
    if (!hit) return true;
    if (!slugs.has(hit[1])) { rep.errors.push('no heading for ' + m.attrs.href + ' ("' + n.text.slice(0, 40) + '")'); return true; }
    tr.removeMark(pos, pos + n.nodeSize, m);
    tr.addMark(pos, pos + n.nodeSize, S.marks.link.create(Object.assign({}, m.attrs, {href: '#§' + hit[1]})));
    rep.changed.push([n.text.slice(0, 40), hit[1]]);
    return true;
  });
  rep.n = rep.changed.length;
  if (rep.errors.length || opt.dry || !rep.n) return rep;
  ed.view.dispatch(tr);
  rep.dispatched = true;
  return rep;
};
window.__samePostLinksCheck = () => {
  const body = document.querySelector('.body.markup') || document.body;
  const all = [...body.querySelectorAll('a[href]')];
  const hash = all.filter(a => decodeURIComponent(a.getAttribute('href')).startsWith('#§'));
  const dead = hash.filter(a => !document.getElementById(decodeURIComponent(a.getAttribute('href')).slice(1))).map(a => [a.textContent.slice(0, 40), a.getAttribute('href')]);
  const id = ((document.querySelector('button[data-href*="/i/"]') || {}).getAttribute ? document.querySelector('button[data-href*="/i/"]').getAttribute('data-href').match(/\/i\/(\d+)\//) : null);
  const still = id ? all.filter(a => a.getAttribute('href').includes('/i/' + id[1] + '/')).map(a => a.getAttribute('href')) : [];
  return {post: id && id[1], same_post_links: hash.length, dead, still_reloading: still};
};
