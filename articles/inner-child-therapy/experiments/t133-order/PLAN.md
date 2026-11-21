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

## Run 5: the blind sort with only the guide's own words and his answers (written before it ran)

Turn 136 found what the earlier frames got wrong: the Nurturer and 7 of the 9 parts had no text of their own on 4
November, and the model that wrote the frame for runs 2 to 4 described them by what sat under them, which gave the old
place to 8 of his 20 moves (DOUBT.md, second section; lesson inner-child-2026-11-20r). Turn 137 asked him only what the
article doesn't answer (question 116, Healing Old Patterns; `../t137-questions/ASKED.md`), and he answered on
2026-11-21 at 01:47 UTC.

Run 5 is run 4 with one change to the frame and one addition to the cards. The frame (`out/FRAME-5.json`, made by
`make_frame5.py`) is no model's description: it is the 4 November text's own words, verbatim (the opening, Five Stages,
and each part's and role's own text, empty where there is none), and his framework answers: 114 as run 4 had it, 115 (1)
on divine love, the rule he agreed to in 115 (3) (a problem goes where the reader meets it), and 116's definition of
Healing Old Patterns. What his answers say about his own moves stays out ("i moved most of the sections from here into
their role sections"), so the run tests the method and not his outline. Each card also names a second home: where the
section would go if not the first. Same readers as runs 2 to 4 (Sonnet, one per shuffled batch), same headings list,
same assembly and scoring (`assemble5.py`, from `assemble4.py`).

Predictions: the spiritual sections go to the Guide's side (at high or medium confidence, 3 to 5 of the five: Ask God for
a Loan, Invite Your Little One In, When the Spiritual Relationship Hurts, How Much Happiness Do You Know Is Possible?,
The Joy In Sorrow); shame and forgiveness stay under the Nurturer, as in run 4; How Distrust Reproduces goes under Finding
People and Building Trust (likely, by 115 (3)). At high confidence, 6 to 10 of his 20 moves with 12 or fewer others; tau
at or above run 4's 0.943. Second homes: his real heading is the first or second home for more of his 20 moves than it
is the first (prediction: 4 or more more), at no more than about 30 questions (unsure sections with a second home).

## Run 5 result, and run 5b (written before 5b ran)

Run 5 (RESULTS-5.md) did worse than run 4: 2 of his 20 moves at high confidence with 9 others, tau 0.933 (run 4: 3, 9,
0.943); at high or medium, 33 other moves (run 4: 24). Every prediction failed except one: no spiritual section went to
the Guide's side; his real heading was the second home for 4 more of his moves, as predicted, but at 84 questions, not
about 30, and with fewer of his moves among them than chance (7, against 11.4).

The cards say why the spiritual sections stayed. The readers did take his answer to 115 (1): they gave Ask God for a
Loan, Your Loan is PRE-APPROVED! and How Much Happiness Do You Know Is Possible? no role ("none"), not the Nurturer. But
nothing in the frame named the role that leads there, so they filed the sections where they were, under the Nurturer or
under Ask God for a Loan. His answer said where divine love doesn't go, not where it does. Question 4 of "Before the
sort" asks both ("which role points to it?"), and turn 135's question 115 put the second half only as a guess of mine,
which he didn't take up in words.

Run 5b is run 5 with the other half, in his own words from his guide: under Divine Love: Bigger Door he wrote "This is
what the Inner Guide can bring you to" (`out/FRAME-5B.json`, made by `make_frame5.py --b`; `input/TASK-CARDS-5B.md`).
Nothing else changes: same batches, readers (Sonnet) and assembly (`assemble5.py 5b`).

Predictions: at least 3 of the 5 spiritual sections (Ask God for a Loan, Invite Your Little One In, When the Spiritual
Relationship Hurts, How Much Happiness Do You Know Is Possible?, The Joy In Sorrow) land on the Guide's side (under the
Guide, or under a section filed under it); his other moves change by at most 2 either way. If fewer than 3 move, an
explicit destination is not enough either, and the next question is what else the readers need.

## Run 5b result

The prediction held: with his one line added, all 5 spiritual sections landed on the Guide's side (run 5: none), 3 of
them exactly where he put them (Invite Your Little One In and How Much Happiness Do You Know Is Possible? under the
Guide, The Joy In Sorrow under How Much Happiness), and the readers gave Ask God for a Loan, Invite Your Little One In and
How Much Happiness the Guide's role. So one sentence naming where a thing goes moved what a sentence saying where it
doesn't go could not. The other prediction failed: at high or medium confidence his moves went from 4 to 7, 3 more than
the 2 allowed, all of them spiritual sections. At high confidence alone, 5b is no closer than run 4 (2 of his moves with 7
others, tau 0.924; run 4: 3, 9, 0.943), and at high or medium it makes 31 moves he didn't make: with no words of their
own for 7 of the 9 parts, the readers scatter more than with a model's description. Second homes didn't narrow the
questions in either run: 84 and 94 unsure sections with a second home, with fewer of his moves among them than chance.

## Run 6 (not run; for Joel to say)

Combine what each frame did well: a model's description only for the parts and roles the 4 November text describes in
its own words (run 4 kept those sections steadier), and his words for the ones it doesn't: the Nurturer (questions 114
and 115, with "This is what the Inner Guide can bring you to"), Healing Old Patterns (116), and the five other parts
with no text of their own, asked first. The prediction would be written here before it runs.
