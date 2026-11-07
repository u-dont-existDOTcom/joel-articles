# r31: the version for his post's update (2026-11-07)

His extension read draft E, the whole of r30, [Human Written](https://www.pangram.com/feed/1c41fbd9-580a-4036-b526-95a96cb70c46)
(`../r30/draft-e-check/`, #208 right): every window Human, document confidence High; 7 High windows cover 4,025 of its
4,040 words, and the 5 Medium ones are 1 to 5 words each, Pangram's splits at "Dr." and "And no snacking!" (on the
later list as not worth fixing). No Low window is left, so the fixes are done (AGENTS.md, "what counts as done"). Draft
B, the last whole-article check before this, had 9 High, 8 Medium and 4 Low windows (#183).

He approved all five batch-14 cards (`../../../experiments/t20-answers/`). On four he wrote "didn't need to ask", and
on F14-3 "altho oxytocin is a bonding hormone not the love hormone exactly" (lessons gut-2026-11-07b and c,
`docs/lessons/2026-11-07-0111-gut.md`). So r31 is r30 with that gloss corrected:

> He picked its bacteria for what they do: L. reuteri heals your gut lining and boosts oxytocin (a bonding hormone), and
> L. gasseri makes bacteriocins, natural antibiotics that kill SIBO.

Source: [Cleveland Clinic, Oxytocin](https://my.clevelandclinic.org/health/articles/22618-oxytocin) (its roles include
trust, romantic attachment and parent-infant bonding, which is where the "love hormone" nickname comes from). Phase 5
with the corrected gloss read [Human Written](https://www.pangram.com/history/4fc92a24-abe2-4111-97c4-513e0b39b973)
(#209), High apart from "Cleared the infection?" and one "Dr." (Medium).

## The update, ready for his OK

- `live-update/make_r31_html.py` → `live-update/r31.html`: r12.html (what the second update put in, so what the editor
  holds now; the third update, r17, never went in) with r31's words in the 36 editor paragraphs that changed, Phase 4's
  one-item step list removed since the step is in its paragraph now, the post's pictures, videos and paywall kept, and
  every quote mark curled as the checks read it (E362 (gut)). All 74 lines his extension reads are in it, exactly and in
  order (`live-update/EXPECTED-TEXT-r31.txt`: draft E's checked text with the one gloss changed).
- `../live/UPDATE-PLAN-4.json` (`make_plan.py r31.html r12.html UPDATE-PLAN-4.json`): 95 blocks before, 94 after, the same
  six native blocks.

How it goes in, once he says yes, with no email (as the second update, `../live/README.md`): in the post's editor in the
desktop app's built-in browser, `../live/update2.js` with `window.__planGut = {url, sha256}` (the plan at a pushed
commit) and `window.__srcGut` (r31.html at the same commit). It checks the editor against r12 first, so a change of his
since then stops it. Then `dispatch.js`, Continue, and "Update now", with every setting as it was and "Send via email"
unchecked; `email_sent_at` stays null. After it, the live post's text is compared with `EXPECTED-TEXT-r31.txt`
character by character (E362 (gut)).
