# Contents of Joel's very long posts (from 2026-11-22)

Joel, 2026-11-22 17:23 UTC: "and while you're at it lets fix the ToCs if any very long articles the same way we did
with innerchild article and Bad trips article so people can navigate easily"

## Which posts

All 102 published posts of U-Dont-Exist.com were read on 2026-11-22 (each post's API body). Substack's contents sidebar
lists every h1 to h4 on one line and cuts it with "…" past 217, 205, 193 and 181px (`tools/humanization/toc_sidebar.py`).
"Repeats" are `tools/humanization/toc_check.py` candidates: a heading sharing a word with its parent or the one before it;
each still needs a reader's call.

| Post | Words | Headings (h1/h2/h3/h4) | Sidebar: cut, tight, whole | Repeats | Lane |
| --- | ---: | --- | --- | ---: | --- |
| Inner Signal Guide to Self-Hypnosis (& APP) | 29,614 | 164 (43/96/23/2) | 90, 11, 63 | 36 | registered (inner-signal); no commit on main since 11-14; post updated 11-20 |
| Inner Child Self-Love Reparenting Guide | 28,787 | 149 (8/43/80/18) | done | | inner child lane, turns 130 to 133 |
| Romance Advice I Wish My Parents Taught Me | 19,925 | 71 (16/23/27/5) | 31, 2, 38 | 13 | registered (romance); idle since 11-08 |
| Building Healing Community "Escuelitas" | 15,269 | 65 (9/30/24/2) | 39, 5, 21 | 14 | registered (intentional-communities); idle |
| What If Everything Is Already Perfect? (Nirvāna) | 15,265 | 60 (5/30/25/0) | 38, 5, 17 | 16 | registered (nibbana); post updated 11-21 |
| Trip-Sitting: Medical Triage, Shadow Work, Therapy | 13,484 | 83 (8/47/18/10) | not measured | | the bad trips guide: its lane is active (turn 59, 11-21) and its new contents isn't on this post yet (the post's headings date from 10-03); the lane publishes it |

Next tier, 5,000 to 7,000 words, not "very long": Best Sleep (18 headings), Somatic Modalities Map (32), Hearthwork
(23), Detoxing (24), Beyond the Standard of Care for Cancer (7), Neurological De-Armoring (25), Do Your Own Research
(28), Haoma (38).

Beside this file, for each of the four: `<slug>.TOC.md` (its headings as live on 2026-11-22), `<slug>.sidebar.txt` (how
the sidebar shows each), `<slug>.CONTENTS.json` (for `toc_check.py`) and `<slug>.repeats.txt`.

## The method (as for the inner child and bad trips guides)

`docs/FIXING-AN-ARTICLE.md`, section 3, in this order:

1. Read the article's `CURRENT-STATE.md` and check for a `PARALLEL-WRITE-LOCK.json`; the article's master is the
   authority, and its own lane, if one is active, does the edit.
2. Contents first (gate bad-trips-2026-11-09e): an agent that has seen no contents writes real reader situations from the
   text with its headings taken out; fresh readers get only the headings, at their levels with word counts, as the sidebar
   shows them, cut-offs included (gate inner-child-2026-11-16a), and say where they would look first and how sure they
   are; they write their hardest headings as "HARD: line | why".
3. New names with `tools/humanization/headings_brief.md` (Fable), his words and capitals first, the words that say
   what's under a heading first, a child not repeating its parent; `tools/humanization/heading_case.py` for title case.
4. `toc_check.py --fates`: every repeat and hard heading changed or kept with a reason (lessons bad-trips-2026-11-21a, b).
5. Check the pick with fresh readers (gates inner-child-2026-11-17a to g); a model's reorganization is only a proposal,
   move by move, after asking him what each part holds (gate inner-child-2026-11-20a).
6. His picks on a page, each option shown as it would look, with your pick and how sure you are (gate
   bad-trips-2026-11-09f), built with `tools/humanization/contents_picks_page.py` (a copy made to test it is built with
   "test": true and ends its turn pointing to his page, lesson toc-2026-11-24c; his own-words box shows the sidebar's
   cut-off; lesson toc-2026-11-23a), with the link plan for every section the text mentions (lesson toc-2026-11-23b).
7. Apply: `section_links.py build` a `SECTION-LINKS.json`, rename through `section_links.py rename`, fix the sentences on
   either side of each renamed heading (gate inner-child-2026-11-20d), and the body text the change touched (a sentence
   fixed beside a heading, a line set on its own, a moved section) reads as high in Pangram as before: in its section,
   without the heading, and a moved section in one whole-post check too, the free way (his extension on the live post
   as it was and on a temporary draft's secret preview link), never the web app, which is for a section of 5 or 6
   paragraphs (lesson toc-2026-11-23d: the Nirvāna run's six whole checks there cost about 930 credits). A rename alone
   changes no window in his extension, which leaves headings out, and a heading's own window may read Low (lessons
   toc-2026-11-23c and e).

## Order and next step

Joel picked the Nirvāna guide first (2026-11-23 14:37 UTC: "ok start with the nirvana guide ToC").

1. **Nirvāna: done on 2026-11-23** (his picks at 18:01 UTC, the flashbacks section back at the end at 19:39, his two
   second-pick headings at 19:46): [APPLIED.md](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/articles/nibbana/experiments/toc-20261123/APPLIED.md);
   the test and every heading's reason: [RESULTS.md](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/articles/nibbana/experiments/toc-20261123/RESULTS.md).
   His extension on the live post (2026-11-23 23:50 UTC, NB-toc-ext-live#48): Human Written, 100% Human, 52 High, 43
   Medium, 8 Low windows, no heading in its text; the three windows that read lower in my web-app checks read High
   there (lesson toc-2026-11-23e), as does every sentence this lane changed. The 51 windows below High are short
   pieces between the long High ones; on the post his extension shows it all High (Joel, 2026-11-24 21:35 UTC:
   "nirvana post reads all high conf on substack"), so they are recorded and closed (lesson toc-2026-11-24d).
2. Then the Self-Hypnosis guide (the most headings and the most cut off, 90 of 164, and 43 h1s, two of them notes rather
   than sections: "How to use this very large guide", "The table of contents is hiding on the left"), Escuelitas, Romance.
   Build its picks page with `tools/humanization/contents_picks_page.py`, run the section-link check with the contents
   test (lesson toc-2026-11-23b), and check the picks in Pangram section by section before they go in.
   **Started 2026-11-23:** step 1 done (no PARALLEL-WRITE-LOCK.json; the article's last commit on main is of 11-12 and no
   branch works on it; its `master.html` is of September, behind the live post, last updated 2026-11-20, v. 7.0, so the
   contents work starts from the live post, as Nirvāna's did). Step 2 done the same day, on the live post (165 sections,
   164 in the sidebar, 90 cut off, 29,554 words): [RESULTS.md](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/articles/inner-signal/experiments/toc-20261123/RESULTS.md).

**His picks are all in (2026-11-25 01:24 UTC).** [His record and how each answer is read](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/articles/inner-signal/experiments/toc-20261123/answers/JOEL-20261125-0108.md);
[the contents that goes in](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/articles/inner-signal/experiments/toc-20261123/FINAL-CONTENTS.md) (159 headings, none cut off; `make_final.py`). Two fresh readers found
61 and 60 of the 64 situations on the first look (the live post: 54 and 56). His answers on the earlier pages
(`answers/JOEL-20261124-*.md`) are history; the picks page is done with.

Next step, in order:

1. **His answers to [the nine questions](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/articles/inner-signal/experiments/toc-20261123/QUESTIONS-20261125.md)** (each has a default, which goes in where he says
   nothing; question 6, his words for the past-life section, has none). They change `make_final.py` (structure, the
   inner-adult heading) and `apply_plan.py` (`--pointer`, the breathing lines, the borrowed-adulthood pointer).
2. **The carry-overs from the guides it is built on** (the list at the end of the questions page, from
   `catchup/CATCHUP-INNER-CHILD.md` and `catchup/CATCHUP-SOMATIC.md`): write each in from his own sentences in the
   source guide, fresh reader against `tools/humanization/his_fixes_brief.md`, making-sense receipt, each checked in
   its section in the web app, then all of them on the marking page (`tools/humanization/suggestion_review.py`) for
   his yes. They go into `apply_plan.py` as new paragraphs and edits.
3. **The section checks still open** (each a sentence of mine in its section, so each needs its receipt before
   `pangram_ledger.py predict`): `pangram/SEC-S143-after.txt`, `SEC-S077-S080-after.txt`, `SEC-S122-after.txt`, and
   `SEC-S007-after-pointer.txt` if he says yes to question 3. Done: the merged S131 and S001, both Human Written, one
   window, High (IS-toc-S131#277, IS-toc-S001#278). Pangram is signed in in the desktop app's browser pane (623
   credits on 2026-11-25).
4. **The one editor transaction:** `python3 apply_plan.py` (after `make_final.py`), then in the post's editor tab load
   `apply_in_editor.js` and `EDITOR-OPS.json`, `window.__applyContents(ops, {dry: true})` until the report shows no
   errors, no heading differences and only the planned text gone and new, then `{dry: false}`, Update, "Update now"
   (no email), and the date in the subtitle (gate E323). It has not been run in the editor yet, so the first dry run
   is also the test of the block fingerprint against the editor's own blocks.
5. **After it:** `section_links.py build` the post's `SECTION-LINKS.json` from the live post, every new link opened,
   then the whole post the free way in parts (his extension on temporary drafts' secret links) for the moved sections,
   and `articles/BUILT-ON.json` gets its `last_brought_in_line`.

Then Escuelitas, Romance (the romance lane is active: it does the edit).
