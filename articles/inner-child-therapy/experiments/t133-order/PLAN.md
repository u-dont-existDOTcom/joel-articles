# Turn 133: building the contents from small questions (written before any run)

Joel, 2026-11-20 21:49 UTC: "i'm surprised that Ai is so incapable of figuring out how to move things around in the
guide. why is that? [...] there's no way to fix that?" and, 22:32 UTC: "yes, run the new ToC building test on 4 to 14 as
you suggested, let's see if you can get closer."

## Why the models failed in turn 132

Every model got local moves right and missed his big ones, and every big one was a move by role: shame and forgiveness
under the Nurturer, the spiritual sections under the Inner Guide, the vow under Practicing. To make those moves in one
pass, a model has to hold each role's work in mind while placing 148 sections across 28,000 words, with every move
affecting the others: many interdependent decisions at once, where models are weakest (AGENTS.md, "Method fit": meaning
goes to a model, structure to code).

## The method

1. **Frame** (one fresh reader, the whole guide): the guide's parts and the job each does, and its roles with the work
   each does, in the guide's words. No moves. `input/TASK-FRAME.md`, out `out/FRAME.json`.
2. **Cards** (four fresh readers, a quarter of the sections each, in parallel): the same small questions of every section,
   one at a time: the reader's question it answers, its kind, whose work it is (a role, or none) and how sure, which part's
   job it serves and how sure, whether it only continues another section, and what a reader needs first.
   `input/TASK-CARDS.md`, out `out/CARDS-A.json` to `D`.
3. **Assembly** (code, `assemble.py`, written before the cards exist): start from the 4 November outline; a section whose
   card names a role with high confidence, when that role's heading isn't already above it, moves under the role;
   otherwise a section whose card names another part with high confidence moves under that part. A section moves with
   the sections under it; parts, role headings and empty grouping headings stay; inside each parent the 4 November order
   holds; a child sits one level below its parent.
4. **Score** with `../t132-toc-links/order/score_order.py`, the same as turn 132's 21 outlines.

Primary result: the assembly above. Secondary, reported as such: role moves only; part moves only; role moves at high or
medium confidence. Model: Sonnet for the frame and the cards (the point is that small questions don't need the biggest
model).

## Predictions

Turn 132's best on his moves was GPT with the rules (9 of 20, with 16 moves he didn't make, tau 0.814); leaving the order
alone scores 0 of 20, tau 0.923.

- The primary assembly makes more of his 20 moves than any turn 132 outline: 10 to 14.
- It makes fewer moves he didn't make than GPT with the rules: 10 or fewer.
- Its tau is at least 0.92.
- Role moves do most of the work; part moves add little and cost the most wrong moves.

## Run 1 failed, and why (written before run 2)

The primary assembly moved nothing: every high-confidence card agreed with the 4 November outline (RESULTS.md). The
framework reader had described each part and role by what sat under it, so the Nurturer was "loves the little one,
borrows love..." and Healing Old Patterns was "how distrust and shame reproduce, forgiveness...". Carded against that,
shame and forgiveness belong where they already were. A frame read off the current outline can only confirm it. Most of
his other moves were local (Borrow Hindsight and You Did It Well Before went under "Borrow a Guide to Build It", a heading he added; turn 136 found that run 1's report had named the nearest older heading instead),
which run 1's questions didn't ask about.

## Run 2 (written before it ran)

Two changes, each aimed at one of those causes:
1. The frame comes only from the guide's introduction, the parts' own text and the three roles' own sections, with the
   instruction to say what each is for in general terms, never by what sits under it (`input/FRAME2-SOURCE.md`,
   `input/TASK-FRAME-2.md`, out `out/FRAME-2.json`).
2. The cards add one question: which section, anywhere in the contents, a reader would expect this one to sit directly
   under, and how sure (`input/TASK-CARDS-2.md`, out `out/CARDS2-A.json` to `D`).

Assembly (`assemble2.py`): (a) run 1's rule with the new frame; (b) each section with a high-confidence "sits under" that
differs from its 4 November parent moves there. Same scorer.

Predictions: (a) moves shame and forgiveness under the Nurturer and makes 3 to 6 of his 20 moves with 6 or fewer others;
(b) makes more of his moves (6 to 10) but also more he didn't (10 to 20). Neither beats leaving the order alone on tau.

## Run 2 failed too, and why (written before run 3)

RESULTS-2.md: at high confidence one section moved, not one of his. For 18 of his 20 moves, the card's "sits under"
named the section's current parent, and shame and forgiveness stayed "Healing Old Patterns" with no role. The readers
saw each section in order, under its current heading and level, after the sections it follows, and the text was written
for that place. The instruction to ignore where it sits didn't undo that.

## Run 3: a blind card sort (written before it ran)

The sections shuffled with a fixed seed and dealt to four readers, each with its heading but no level and no neighbours
(`input/SHUFFLED-A.md` to `D`); every heading in one alphabetical list, no levels (`input/HEADINGS-FLAT.md`); the
function-only frame (`out/FRAME-2.json`). One question: which heading each section would be filed directly under, and
how sure, plus whose role's work it is (`input/TASK-CARDS-3.md`, out `out/CARDS3-A.json` to `D`). Assembly: run 2's
"sits under" rule (`assemble3.py`), high, and high or medium.

Predictions: at high confidence, 4 to 8 of his moves with 8 to 20 others; it beats run 1 and run 2 on his moves, and
tau falls below 0.92. Shame and forgiveness go under the Nurturer: no better than even.

## Run 4: the blind sort with his own view (written before it ran)

Run 3 (RESULTS-3.md) made 1 of his 20 moves at high confidence; every reader filed shame and forgiveness under Healing
Old Patterns. His answer to question 114 (2026-11-20 23:03 UTC) is the missing input: "love accepts. protection blocks.
guide directs. shame and forgiveness need acceptance", a catch-all part isn't the home for a primary obstacle, and a
practice goes under a role only when the role must do it, otherwise "where the flow lands". Run 4 is run 3 with his words
added to the frame and the instruction to sort by them (`out/FRAME-3.json`, `input/TASK-CARDS-4.md`, out
`out/CARDS4-A.json` to `D`), assembled and scored by `assemble4.py` the same way.

Predictions: shame and forgiveness go under the Nurturer (likely); at high confidence 4 to 8 of his 20 moves with 10 or
fewer others; still short of his moves inside the Guide's part (Borrow Hindsight under Between Spoiling and Clamping),
which his answer doesn't speak to.

Turn 136 correction, the prediction left as written: he put Borrow Hindsight under "Borrow a Guide to Build It", a
heading he added; the report had named the nearest older heading (his answer to question 115, 2026-11-20 23:22 UTC:
"what are you looking at?"). RESULTS-3-NAMED.md and RESULTS-4-NAMED.md list his 20 moves by his current headings and
where he really put each section. RESULTS-3.md and RESULTS-4.md stay as first written, since the article registry
keeps experiment results unchanged; their counts and scores are the same.
