# The third update of his post, ready for his OK (2026-11-06)

Draft B, the whole of r17, read [Human Written](https://www.pangram.com/feed/bb64a934-cf2c-47b3-ae93-af2a363a0644) in
his extension at 21:26 UTC: no AI window, document confidence High, 0.004% AI (`../draft-b-check/`, #183 right). His
post still has r12, which read Mostly Human, 93% (#142). The pre-publication reads passed (`../prepublish/FINDINGS.md`).

- `make_r17_html.py` → `r17.html`: r12.html (what the second update put in, so what the editor holds now) with r17's
  words in the 32 editor paragraphs that changed, the post's pictures, videos and paywall kept, every quote mark curled
  as draft B's check read it (E362 (gut)); all 75 lines the extension read are in it, in order.
- `../../live/UPDATE-PLAN-3.json` (`make_plan.py r17.html r12.html`): 95 blocks before and after, the same six native
  blocks; 56 blocks change, 32 of them beyond their quote marks.

How it goes in, once he says yes, with no email (as the second update, `../../live/README.md`): push both files; in the
post's editor in the desktop app's built-in browser, `../../live/update2.js` with `window.__planGut = {url, sha256}` (the
plan at the pushed commit) and `window.__srcGut` (r17.html at the same commit). It checks the editor against r12 first,
so a change of his since then stops it. Then `dispatch.js`, Continue, and "Update now", with every setting as it was and
"Send via email" unchecked; `email_sent_at` stays null. After it, the live post's text is compared with draft B's checked text character by character (E362 (gut)).
