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

**What this lane still owes him is in [PROMISES.md](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/work/toc-long-articles-20261122/PROMISES.md)** (his ask of 2026-11-25 16:14 UTC). Read it
at the start of a turn and again before the reply; a promise goes on it the turn it is made.

**The Self-Hypnosis contents is in the post, in two edits on 2026-11-25** (12:00:39 and 16:28 UTC):
[what went in, the section checks, every heading before and now](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/articles/inner-signal/experiments/toc-20261123/APPLIED.md). His picks
([01:08](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/articles/inner-signal/experiments/toc-20261123/answers/JOEL-20261125-0108.md)), his answers to the nine questions
([11:18](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/articles/inner-signal/experiments/toc-20261123/answers/JOEL-20261125-1118.md)), his marking-page answers and the two names for question 4
([16:00 and 16:14](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/articles/inner-signal/experiments/toc-20261123/answers/JOEL-20261125-1600.md)). 160 headings, none cut off; 39 links to its own sections,
written `#§slug` so they scroll (lesson toc-2026-11-25c). The inner child guide's 24 and the Nirvāna guide's 13 scroll
too. The post's live text, link catalog and the registry of shared passages are read from the post as it is after
the second edit (`articles/inner-signal/LIVE-SECTIONS.json`, `SECTION-LINKS.json`, `articles/DEPENDS.json`: 0 changed).

Next step for the lane, in order (each is a promise on the list):

1. **The daily watcher's first run on GitHub** (promise 3): start `depends-watch` by hand
   (`gh workflow run depends-watch.yml`, from the laptop if the cloud shell can't), read the run, and fix or report
   what it shows. If Substack refuses GitHub's machines, the job says so in one issue; then the fetch moves to a
   place that can reach Substack and the job only compares.
2. **The rest of the catch-up** (promise 17): 12 smaller additions and 10 smaller differences between this guide and
   the two it is built on, listed as "behind" and "his to settle" in
   [articles/DEPENDS.md](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/articles/DEPENDS.md). Draft the
   additions from his own sentences, read each source sentence's links with `tools/humanization/carried_links.py`
   (lesson toc-2026-11-25f), check each in its section, and put all 22 on a second marking page built the way
   `review/build_review.py` builds the first. Then one small editor edit
   (`apply_plan2.py` is the pattern: base = the live body, `apply_in_editor.js`, then
   `tools/humanization/substack_update.js`), the live post fetched from the laptop, `live_sections.py`,
   `depends.py check`, and `last_brought_in_line` set in `articles/BUILT-ON.json`.
3. **"EFT Tapping" and "Gendlin Focusing"**, which read AI by themselves, and the five Medium windows of his
   (promises 6 and 7), in the same pass as 2 where they touch the same sections.
4. **The whole post, the free way** (promise 5): his extension, or in parts on his word.
5. **The bad trips guide's 42 section links** (promise 2) are that lane's files; read its live post each turn until
   the guide is in with links that scroll.

Pangram is signed in in the desktop app's browser pane (478 credits left on 2026-11-25, after the second edit's
checks; a check costs 1 credit per 100 words).

Then Escuelitas, Romance (the romance lane is active: it does the edit).
