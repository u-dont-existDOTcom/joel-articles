// substack_secret_link.js - the secret preview link of a temporary Substack draft, in the paid subscriber view, for Joel.
//
// Joel, 2026-10-26 12:43 UTC: "why is it that you know how to make the preview, while inner child lane only makews a draft
// without making a preview of it? make sure that's a durable instruction to save me some steps". The hypnosis guide lane
// gave him each draft's secret preview link (paid view) and he only opened it in Brave and ran the Pangram extension; the
// Inner Child lane gave him the draft, so he had to open the editor, Preview, switch to the paid view and Share himself.
// Every lane now gives the link (AGENTS.md; docs/PANGRAM-PRODUCTION-BUDGET-20261020.md step 2; gate E277).
//
// Run it in the app's built-in browser, in any tab on the publication's site (the draft's editor tab after the paste):
//   window.__draft = {id: 222109105, cache_key: 'recheck-a-27'};   // the number in /publish/post/<id>; any new cache key
// The cache key goes in the link's "updated" parameter, which only makes Substack serve a fresh page: give each new paste
// a new one, or the link can show the text from before. It never clicks anything and never publishes.
// It returns the link, or why not: the draft must exist, be unpublished, and carry a temporary title ("TEMP ...", or one
// saying "temp, delete after"; gate E205: never "Pangram" in it). Then open the link in the built-in browser, check the
// rendered text (tools/humanization/substack_rendered_check.js), and give Joel the link itself, never the editor address.
(async () => {
  const want = window.__draft || {};
  if (!want.id || !want.cache_key) return 'set window.__draft = {id: <the draft number>, cache_key: <a new key>} first';
  const r = await fetch('/api/v1/drafts/' + encodeURIComponent(want.id), {credentials: 'include'});
  if (!r.ok) return 'refused: the draft API answered HTTP ' + r.status + ' (open a page of this publication, signed in, first)';
  const d = await r.json();
  const title = d.draft_title || d.title || '';
  if (d.is_published) return 'refused: draft ' + want.id + ' is published; this is only for temporary drafts';
  if (!/^TEMP\b|temp, delete after/i.test(title) || /pangram/i.test(title))
    return 'refused: the title ' + JSON.stringify(title) + ' is not a temporary draft\'s (TEMP ..., no detector name)';
  if (!d.uuid) return 'refused: the draft has no uuid';
  const link = location.origin + '/p/' + d.uuid + '?postPreview=paid&updated=' + encodeURIComponent(want.cache_key) +
    '&audience=only_paid&free_preview=false&freemail=';
  return JSON.stringify({link, title, draft: location.origin + '/publish/post/' + want.id, audience: d.audience,
                         updated_at: d.draft_updated_at, body_chars: (d.draft_body || '').length});
})()
