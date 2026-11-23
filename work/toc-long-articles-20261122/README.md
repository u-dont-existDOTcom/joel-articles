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
   bad-trips-2026-11-09f), built with `tools/humanization/contents_picks_page.py` (his own-words box shows the sidebar's
   cut-off; lesson toc-2026-11-23a), with the link plan for every section the text mentions (lesson toc-2026-11-23b).
7. Apply: `section_links.py build` a `SECTION-LINKS.json`, rename through `section_links.py rename`, fix the sentences on
   either side of each renamed heading (gate inner-child-2026-11-20d), and a heading with new words reads Human High in
   Pangram before it goes into his post.

## Order and next step

Joel picked the Nirvāna guide first (2026-11-23 14:37 UTC: "ok start with the nirvana guide ToC").

1. **Nirvāna: in his post since 2026-11-23 18:01:47 UTC.** His picks and six answers (17:24 UTC), checked in Pangram
   section by section, and 13 links to sections: [APPLIED.md](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/articles/nibbana/experiments/toc-20261123/APPLIED.md);
   the test and every heading's reason: [RESULTS.md](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/articles/nibbana/experiments/toc-20261123/RESULTS.md).
   **Waiting on him, first:** the whole check of the post as published (NB-toc-live#41) read the flashbacks section's
   first two sentences as AI (one High) after its move into the manual; back at the end without "Appendix" they read
   Human High and the post has one AI window (NB-toc-live-END#43). That version is saved as a draft in the editor, not
   published (the app blocked the click on "Update now"); his OK publishes it.
   **Then:** two of his picks read Human Low in their sections ("Did It Work or Go Wrong?" and "Is It Safe When
   "I" Vanish?"), so those two sections keep their old headings, cut off in the sidebar, until he picks again. Offered:
   Fable's "Did It Work? Is It Safe?" or his own words for the first; 'Vanishing "I": Dangerous?' (readers found it 4 of
   4), "Disappearing Flashbacks?" (his words) or his own words for the second. Each goes through Pangram in its section
   first, then `section_links.py rename` against `articles/nibbana/SECTION-LINKS.json` and the editor.
2. Then the Self-Hypnosis guide (the most headings and the most cut off, 90 of 164, and 43 h1s, two of them notes rather
   than sections: "How to use this very large guide", "The table of contents is hiding on the left"), Escuelitas, Romance.
   Build its picks page with `tools/humanization/contents_picks_page.py`, run the section-link check with the contents
   test (lesson toc-2026-11-23b), and check the picks in Pangram section by section before they go in.

Next step: his OK on the saved draft (or keeping his move), and his answer on the two Nirvāna headings; then steps 1 and 2 for the Self-Hypnosis guide, from
`articles/inner-signal/`.
