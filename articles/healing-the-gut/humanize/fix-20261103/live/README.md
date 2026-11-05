# The gut article in his post (2026-11-04)

Joel, 20:27 UTC: "publish it (don't email anyone)". His post [Healing the Gut Naturally](https://ibogaqueen.substack.com/p/healing-the-gut-naturally) (post 176569317, paid subscribers only) has r11 since 20:44 UTC, with no email sent. `LIVE-CHECK-20261104.json` has every step and check.

- **Before:** the pre-publish reads of r10 (`../r10/prepublish/FINDINGS.md`): the word-for-sense read found 3 of 3 planted errors, then the clarity read and the compare read beside his published post. One slip of mine was fixed as r11 (`../r11/make_r11.py`), and its Phase 3 read Human 100% in the web app.
- **The editor** matched the master block for block, so he hadn't changed the post since 3 November.
- **The update:** `make_plan.py` → `UPDATE-PLAN.json` (pushed at c33813a3), then `update.js` in the post's editor (one transaction, the editor's own schema, his six native blocks carried as the same nodes), then `dispatch.js`. Continue, then "Update now", with every setting as it was and "Send via email" unchecked.
- **After:** the published post equals r11 block for block (95 blocks). `email_sent_at` is still null.
- **His date rule (E323):** the post has no date or version in its title or subtitle, so there was nothing to change.

**The next update** comes after his batch-8 answers (`../r11/b8/`). Rebuild the plan with `make_plan.py NEW.html`, with `base` taken from r11 (not the master), and check the editor against r11's blocks before anything changes (E332). Run a web-app check on each changed paragraph first.
