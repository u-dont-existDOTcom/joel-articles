# The community article's full read by the lead model (planned 2026-10-30)

Joel, 2026-10-30 20:15 UTC, after the hypnosis guide's full read: "i guess we need to go back and re-read the community
article as well after this then" (`articles/inner-signal/humanize/fix-20261030/joel-20261030-2015-message.txt`).

**Why.** The hypnosis guide's own read by the lead model found 122 places the Sonnet reads had passed (gate E294). Most
of this article's meaning reads ran on Sonnet too (`../STATUS.md`, the "Delegations" lines): the meaning traces and cold
reads of sections 10 to 16 (2026-10-10 to 10-17), the repeats checks of 23 October, the six caveat readers of 24 October,
and the eight paragraph-pair readers of the strict Emulate check of 25 October. The five faithfulness readers of 17
October ran on Opus, but the text has changed a lot since (his edits, the Emulate passages, the caveat cuts, the
restructure), and nothing has read the whole of it, as it is now, beside his published version with Opus.

**What is read.** `master.md` (the post as it is live: compared paragraph by paragraph with his Substack post on
2026-10-30, "Updated: Oct 25 2026", it differs only where the walk skips images, captions, rules and embeds, and where a
list is one Markdown block) beside `original.md` (his published post before the humanizing). `compare_read.py make` made
the ten parts here (PART-n.txt, BRIEF-n.txt, PARTS.json; 619 to 2,937 words each).

**How.**
1. The lead model reads each part, sentence by sentence, and writes READER-n.md in the brief's format (never a cheaper
   model: E294).
2. `compare_read.py collect` with the article's history (`--git-path articles/intentional-communities/master.md`): each
   finding gets the commit its words came in with and every change to its paragraph (`changes`, E301), and his own words
   are marked (`--owner` with his messages, answers and edits in this lane).
3. Every finding checked against the whole article and his decisions before anything is fixed: a point he cut, or an
   earlier read found said already, stays out (E298, E301); his own words go to him as suggestions (E299).
4. The post is live, so nothing changes in it without him: the fixes go on his marking page (suggestion_review.py), each
   with the exact old and new words to change in Substack's editor, and the Markdown copy in Git.
