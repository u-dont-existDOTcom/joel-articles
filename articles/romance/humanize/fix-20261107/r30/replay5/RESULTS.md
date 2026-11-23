# Round 5 of the blind test: the two passages he fixed on the sixth page (2026-11-23)

His standing rule (2026-11-22 23:43 UTC: "make sure whenever you learn lessons in this repo you see if you can apply them
to pass pangram on the paragraphs that i fixed yourself without seeing my fixes exactly") applied to lesson
romance-2026-11-23h, drawn from his versions of B257 and B442 on the sixth marking page.

The writer: a Fable agent told to answer briefly, given [BRIEF.md](BRIEF.md) (round 4's brief with way 10's new lines, way
24 and rule 4, "change only what is the problem", each illustrated outside the test) and [PARAS.md](PARAS.md) (the two
passages in their sections as they stood before his fix, with the reader's flag the r35 fixer had). It wrote
[OUT.md](OUT.md) in 33 seconds. Each rewrite was checked by itself in the Pangram web app; the predictions were committed
first (9b3155e0), [CHECKS-R5.txt](CHECKS-R5.txt).

| Passage | The blind rewrite by itself | His version | My r35 tries |
|---|---|---|---|
| B257 (Different levels) | [Human, High](https://www.pangram.com/history/4a466ef6-514a-4879-9e57-4c326500f6c0) | [Human, High](https://www.pangram.com/history/126e846d-7968-4de2-a5ba-4124a5685dae) (his check) | [Human with a Low window](https://www.pangram.com/history/d05b3f9e-b70a-4eeb-8519-84aa6300e405), then [Mixed, 55%](https://www.pangram.com/history/049a89d6-54c5-40e3-a273-5e1ce4bb45f8) |
| B442 (What will honesty produce?) | [Human, High](https://www.pangram.com/history/f233a20b-3168-4910-a729-8a193134335b) | [Human, High](https://www.pangram.com/history/48952c2b-ff84-4e2c-97f8-c6bff836ceac) (his check) | [Mixed, 72%](https://www.pangram.com/history/2267fb23-7b39-47a6-9295-77ca69fefb79) |

Both read Human High from the lessons alone. I had predicted AI for both (0.35 and 0.4): two misses.

Where each falls short of his:
- **B257.** The writer checked the reader's "which question?" flag, as rule 4 asks, and judged it right ("nothing in the
  section asks one"), so it said the question again: "Then the question is whether the romance actually does need less
  intensity, becomes friendship, or ends." He didn't need that: "i don't think the question is so hard to understand
  after maybe this or maybe that". It fixed the stock phrase his way ("where to start"; his "the first step in figuring
  it out"), kept the parenthesis he turned into a "but" clause, and moved the condition to the front ("But once a partner
  has become ..."), which he left where it was.
- **B442.** It made his order: the point right after the list it answers, the Bee story last, as one sentence. It named
  what "won't look" and "it" left out ("look at the relationship honestly", "make the honesty mutual"; his "look at the
  truth", "make honesty a mutual value"). It joined "Honesty doesn't produce a certain outcome. It is its own reward."
  into the opening sentence with "because", where he kept both as they were, and kept "it also became more permanent",
  where he wrote "it became less temporary as time went on".

What the rounds show together: Pangram read both High even where the rewrite said the question again or joined more than
he would, and my r35 tries read AI where they added something new (that every outcome takes both people) and rebuilt the
passage. Adding nothing holds across every try of these two passages. What the blind rewrites miss is fidelity, not
Pangram: a run of "maybe ..." possibilities is the question, with or without a question mark, and "that question" points
back to it; saying it again as "whether ..." says it twice. That is the next line of way 10 in
`tools/humanization/his_fixes_brief.md` (lesson romance-2026-11-23h).
