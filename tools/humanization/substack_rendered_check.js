// substack_rendered_check.js - read a Substack post or secret draft link as Pangram's check of it reads it, and compare
// with the text a recheck was forecast from (2026-10-23).
//
// After a payload is pasted into a temporary draft (paste_payload_lane.js), open the draft's secret link in the built-in
// browser, set window.__expect = '<DRAFT-TEXT.txt's SHA-256>' and run this in that tab. It walks the post body
// (div.body.markup) the way tools/humanization/substack_check_text.py's _lines() walks a payload: headings, rules, embeds,
// figures and image containers and galleries are left out; each paragraph and each list item without nested blocks is a
// line; an embedded Substack note's paragraphs keep their straight quotes; every other line has its quotes curled like
// smart(); the emoji joiners and presentation selectors go. The lines joined with newlines must hash to DRAFT-TEXT.txt's
// SHA-256; when they don't, window.__rendered holds the text to compare line by line.
//
// Until 2026-10-23 this walk was retyped in each turn (the Nibbāna rechecks 5 to 7); it is the same walk, kept here.
(async () => {
  const SKIP = new Set(['H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'HR', 'IFRAME', 'FIGURE', 'PICTURE', 'IMG', 'SOURCE']);
  const out = [];
  const walk = (el, note) => {
    if (el.nodeType !== 1) return;
    if (SKIP.has(el.tagName)) return;
    const cls = el.classList;
    if (el.tagName === 'DIV' && (cls.contains('captioned-image-container') || cls.contains('image-gallery-embed'))) return;
    note = note || cls.contains('FeedProseMirror');
    if (el.tagName === 'P') {
      const txt = el.textContent;
      if (cls.contains('button-wrapper') && el.outerHTML.includes('checkout_url')) return;
      if (/^https?:\/\/\S+$/.test(txt.trim())) return;
      if (txt.trim()) out.push([txt.replace(/ +$/, ''), !note]);
      return;
    }
    if (el.tagName === 'LI') {
      if (Array.from(el.children).some(c => ['P', 'UL', 'OL'].includes(c.tagName))) { for (const c of el.children) walk(c, note); }
      else if (el.textContent.trim()) out.push([el.textContent.replace(/ +$/, ''), !note]);
      return;
    }
    for (const c of el.children) walk(c, note);
  };
  const smart = s => s.replace(/(^|[\s(\[{“"—-])'/g, (m, a) => a + '‘').replace(/'/g, '’')
    .replace(/(^|[\s(\[{‘—-])"/g, (m, a) => a + '“').replace(/"/g, '”');
  const body = document.querySelector('div.body.markup');
  if (!body) return 'no div.body.markup on this page: open the post or the secret draft link first';
  for (const c of body.children) walk(c, false);
  const text = out.map(([x, curl]) => curl ? smart(x) : x).join('\n').replace(/‍/g, '').replace(/️/g, '');
  const hex = Array.from(new Uint8Array(await crypto.subtle.digest('SHA-256', new TextEncoder().encode(text))))
    .map(b => b.toString(16).padStart(2, '0')).join('');
  window.__rendered = text;
  return JSON.stringify({lines: out.length, chars_js: text.length, sha256: hex,
                         match: window.__expect ? hex === window.__expect : 'set window.__expect to compare'});
})()
