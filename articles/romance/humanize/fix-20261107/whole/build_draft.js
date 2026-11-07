// build_draft.js - build one part of the fixed romance post (2026-11-07) for its temporary Substack draft, and paste it.
//
// Run in the app's built-in browser, in a new draft's editor tab on ibogaqueen.substack.com (/publish/post), after setting
//   window.__part = {part: 'A' | 'B', commit: '<a commit of joel-articles with whole/REPLACEMENTS.json and LIVE-INDEX.txt>',
//                    title: 'Romance, draft A (temp, delete after)', paste: false};
// It reads the live post's body from the post API (the author's session), checks every paragraph against
// LIVE-INDEX.txt's fingerprints at that commit (the page's paragraph list: p, li, h2 to h4, in order), puts in
// REPLACEMENTS.json's new paragraphs (n live paragraphs to n new ones go one to one, so a list item stays one), leaves out
// the pictures, videos, embeds and buttons (Pangram's check of a post reads its paragraphs and list items, not those or
// the headings), and splits the post at the top heading that leaves both parts under 99,999 characters of checked text.
// With paste: false it only reports; with paste: true it sets the draft's title (which must be the lane's temporary one,
// no detector's name in it, gate E205) and pastes the part into the empty body as a paste event carrying text/html.
// It never clicks anything and never publishes. Its report gives the part's checked text's SHA-256 (the lines the
// rendered check, tools/humanization/substack_rendered_check.js, rebuilds from the secret link) and its size.
(async () => {
  const want = window.__part || {};
  const TITLES = {A: 'Romance, draft A (temp, delete after)', B: 'Romance, draft B (temp, delete after)'};
  if (!TITLES[want.part] || !want.commit) return 'set window.__part = {part, commit, title, paste} first';
  if (want.title !== TITLES[want.part]) return 'refused: the title must be ' + JSON.stringify(TITLES[want.part]);
  const raw = 'https://raw.githubusercontent.com/u-dont-existDOTcom/joel-articles/' + want.commit +
              '/articles/romance/humanize/fix-20261107/whole/';
  const get = u => fetch(u, {cache: 'no-store'}).then(r => r.ok ? r.text() : Promise.reject(u + ' HTTP ' + r.status));
  const index = (await get(raw + 'LIVE-INDEX.txt')).trim().split('\n').map(l => l.split(' '));
  const repl = JSON.parse(await get(raw + 'REPLACEMENTS.json'));
  const post = await fetch('/api/v1/posts/romance-advice-i-wish-my-parents', {credentials: 'include'}).then(r => r.json());
  const doc = new DOMParser().parseFromString('<div id="b">' + post.body_html + '</div>', 'text/html');
  const body = doc.getElementById('b');
  const norm = s => s.replace(/\s+/g, ' ').trim();
  const hex = async s => Array.from(new Uint8Array(await crypto.subtle.digest('SHA-256', new TextEncoder().encode(s))))
    .map(b => b.toString(16).padStart(2, '0')).join('');
  // the page's paragraph list has the Share button at the top but not the Subscribe button at the end, and its text has a
  // line break where the editor has <br>
  const els = Array.from(body.querySelectorAll('p, li, h2, h3, h4'));
  while (els.length > index.length && els[els.length - 1].classList.contains('button-wrapper')) els.pop();
  const seen = e => { const c = e.cloneNode(true); c.querySelectorAll('br').forEach(br => br.replaceWith('\n')); return c.textContent; };
  if (els.length !== index.length) return 'refused: the post has ' + els.length + ' paragraphs, the index ' + index.length;
  const bad = [];
  for (let i = 0; i < els.length; i++) {
    if (els[i].tagName !== index[i][1]) bad.push(i + ' tag');
    else if ((await hex(norm(seen(els[i])))).slice(0, 12) !== index[i][2]) bad.push(i);
  }
  if (bad.length) return 'refused: ' + bad.length + ' paragraphs differ from the index: ' + bad.slice(0, 12).join(', ');
  // put in the new paragraphs (keys are paragraph numbers; a list item's own <p> takes its li's text)
  for (const [k, news] of Object.entries(repl)) {
    const el = els[+k];
    const target = el.tagName === 'LI' ? (el.querySelector('p') || el) : el;
    if (!news.length) { el.remove(); continue; }
    target.textContent = news[0];
    let after = el;
    for (const t of news.slice(1)) {
      const n = doc.createElement(el.tagName === 'LI' ? 'li' : 'p');
      if (el.tagName === 'LI') { const p = doc.createElement('p'); p.textContent = t; n.appendChild(p); } else n.textContent = t;
      after.after(n);
      after = n;
    }
  }
  body.querySelectorAll('.captioned-image-container, .image-gallery-embed, .youtube-wrap, iframe, figure, picture, img, ' +
                        '.embedded-post-wrap, .subscription-widget-wrap, .subscribe-widget, .button-wrapper, ' +
                        '.instagram-embed, .tweet, .digest-post-embed').forEach(e => e.remove());
  Array.from(body.children).forEach(c => { if (!norm(c.textContent)) c.remove(); });
  // the checked text: each paragraph and each list item, one line each (headings left out)
  const lines = el => Array.from(el.querySelectorAll ? [el] : []).flatMap(x => {
    if (/^H[1-6]$/.test(x.tagName)) return [];
    if (x.tagName === 'P') return norm(x.textContent) ? [x.textContent.replace(/ +$/, '')] : [];
    return Array.from(x.querySelectorAll('p, li')).filter(e => e.tagName === 'P' || !e.querySelector('p, ul, ol'))
      .map(e => e.textContent.replace(/ +$/, '')).filter(t => norm(t));
  });
  const kids = Array.from(body.children);
  const sizes = kids.map(c => lines(c).join('\n').length + (lines(c).length ? 1 : 0));
  const total = sizes.reduce((a, b) => a + b, 0);
  let best = null, acc = 0;
  kids.forEach((c, i) => {
    if (c.tagName === 'H1' && acc <= 99999 && total - acc <= 99999) {
      if (!best || Math.abs(total - 2 * acc) < Math.abs(total - 2 * best.acc)) best = {i, acc, h: norm(c.textContent)};
    }
    acc += sizes[i];
  });
  if (!best) return 'refused: no top heading leaves both parts under 99,999 characters (total ' + total + ')';
  const part = want.part === 'A' ? kids.slice(0, best.i) : kids.slice(best.i);
  const html = part.map(c => c.outerHTML).join('\n');
  const text = part.flatMap(lines).join('\n');
  const report = {part: want.part, split_at: best.h, part_chars: text.length, total_chars: total, blocks: part.length,
                  replacements: Object.keys(repl).length, text_sha256: await hex(text), html_sha256: await hex(html),
                  first: text.slice(0, 60), last: text.slice(-60)};
  window.__built = {html, text, report};
  if (!want.paste) return JSON.stringify(report);
  const titleEl = document.querySelector('textarea[placeholder="Title"], input[placeholder="Title"]');
  if (!titleEl) return 'no title field on this page';
  if (titleEl.value && titleEl.value !== want.title) return 'refused: this draft already has the title ' + JSON.stringify(titleEl.value);
  const eds = Array.from(document.querySelectorAll('.ProseMirror[contenteditable="true"]'));
  if (!eds.length) return 'no editor on this page';
  const ed = eds.sort((a, b) => b.getBoundingClientRect().height - a.getBoundingClientRect().height)[0];
  if (norm(ed.innerText)) return 'refused: the body is not empty (' + norm(ed.innerText).length + ' characters)';
  if (!titleEl.value) {
    const setter = Object.getOwnPropertyDescriptor(Object.getPrototypeOf(titleEl), 'value').set;
    setter.call(titleEl, want.title);
    titleEl.dispatchEvent(new Event('input', {bubbles: true}));
    await new Promise(r => setTimeout(r, 800));
  }
  ed.focus();
  const dt = new DataTransfer();
  dt.setData('text/html', html);
  dt.setData('text/plain', text);
  const ev = new ClipboardEvent('paste', {clipboardData: dt, bubbles: true, cancelable: true});
  ed.dispatchEvent(ev);
  await new Promise(r => setTimeout(r, 3000));
  report.pasted = {handled: ev.defaultPrevented, editor_chars: ed.innerText.length, title: titleEl.value, url: location.pathname};
  return JSON.stringify(report);
})()
