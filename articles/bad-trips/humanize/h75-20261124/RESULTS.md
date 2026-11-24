# Turn 67 (2026-11-24): his round-56 answers, and the kidney paragraph by two methods

His round-56 export of 21:26 UTC ([the answers](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/articles/bad-trips/review/r56/ANSWERS-R56-20261124-2126.json);
[what happened to each point](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/articles/bad-trips/review/r56/RESULTS-R56.md)).
Every text was checked by itself through the API on his laptop with his key, plain (no links or bold), each with its
prediction in the ledger first. Every dose, event and warning held (`facts.py`, the R55 fidelity keys).

## His answers, in

| Paragraph | What changed | The API |
|---|---|---|
| B115, his amounts and why magnesium chloride | The absorption study's link out, his claim as what he knows: "I use it mostly because it's what I know works best: it absorbs faster and better than any other form, so you can see how it's helping, usually within a minute." | [Human High 118, one window](https://www.pangram.com/history/f330e220-03a5-4821-9919-6427d4660e2a) |
| B118, his second wife | Its last phrase, his choice (a): "since potassium gets depleted once magnesium runs low" | [Human High 77, one window](https://www.pangram.com/history/e74a7e6b-7047-4e54-af54-64070d2b5879), checked last turn |

## The kidney paragraph (B120): the section's last paragraph below High

| Text | Method | The API |
|---|---|---|
| His post's paragraph, as it stands in the guide | checked by itself for the first time | [AI Generated: High 100, one window](https://www.pangram.com/history/df3704bf-5de7-4067-aa11-f5b231f3e310) |
| a1 (`TEST-a1-b120.txt`) | Small fixes from his text, a third of its words, one for each sentence the tell panel agreed on, by the ways of his round-55 fixes: the pivot runs on into what the MDMA can cause ("since"), the list in two shapes with the kidney injury first, the dash aside as its own clause after "although", the mirrored pair as one sentence with its reason | [AI Generated: High 109, one window](https://www.pangram.com/history/7afc3e5b-d752-4d67-bf4c-41045d98fb45) |
| w1 (`TEST-w1-b120.txt`) | A second writer's rewrite (Haiku) from the panel's notes, the points to keep and three paragraphs of his (`rewrite-b120/REWRITE-PROMPT.txt`): short plain statements, the advice as instructions. I restored his bold lead, "more cautious" and the link, and took out the writer's gloss of rhabdomyolysis and "no excuse" | [AI Generated: High 106, one window](https://www.pangram.com/history/f880b3a3-fb7c-4da4-828b-80b9f6bba5cf) |

Both predictions were AI (0.30 and 0.15) and both were right. With turn 65's two tries ([Mixed](https://www.pangram.com/history/258a5b17-a2da-49d3-8da5-86655418be03),
with the first two sentences Human Low; [AI](https://www.pangram.com/history/230891b4-4860-4f70-aa2b-f80f19baecb2)) and turn 66's
([AI](https://www.pangram.com/history/e2566e53-84ec-45c7-880d-87b8cbdcecda)), that is five tries by three methods. The guide keeps his post's
paragraph, and round 57 asks him for it as a teaching card (TEACH-KIDNEY).

**The tell panel** on his post's text ([PANEL.md](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/articles/bad-trips/humanize/h75-20261124/panel-b120/PANEL.md)) had
two readers, Sonnet and Haiku. The third (Codex, on his laptop) could not run: this session's permission check declined
the command, and I did not work around it. The readers agreed on four of its five sentences (the pivot standing alone,
the four-item list, the dash correction, the mirrored "I would not tell ...; I would tell them"), and both said the same
of the whole: a caution, a pivot, a list of risks, a contrast and a closing disclaimer, evenly weighted.

**What the two tries show.** Fixing each agreed sentence left the paragraph AI High, and so did another writer's
rewrite with the same five points in the same order. What neither changed is what both readers named: the order of the
points and their even weight. Changing that means deciding which point leads and which is said in passing, and what
"get help sooner" means for someone whose kidneys are impaired, which are his to say (turn 66's fresh readers asked
"sooner than what?", and one read "not a reason to sit there" as "kidney problems are no reason to hold back magnesium":
[their reads](https://github.com/u-dont-existDOTcom/joel-articles/tree/main/articles/bad-trips/humanize/h74-20261124/reads)). A try of mine that answered those would add advice to a medical caution that he hasn't given.

**One mistake in the method, fixed in passing.** I first put the second writer's support files (the points, the
paragraphs around, his lines) in the panel's folder, and `tell_panel.py rewrite-prompt` read them as readers' replies.
They are in [their own folder](https://github.com/u-dont-existDOTcom/joel-articles/tree/main/articles/bad-trips/humanize/h75-20261124/rewrite-b120), and the brief was rebuilt before any writer saw it.

## The next five on the list, each by itself as it stands

Each had only readings inside section checks. By itself, through the API, with its prediction first:

| Block | Section | The API | My call |
|---|---|---|---|
| B111, magnesium, DMSO and CBD during a seizure | Seizure: What Else Helps | [Human High 87, one window](https://www.pangram.com/history/e2e90101-4127-45cd-acf8-db5aa934890f): done | AI at 0.30, a miss |
| B133, the five patterns | How to Check for SS | [Human High 82, one window](https://www.pangram.com/history/6d78093f-18c6-467b-9d77-015394d39638): done | AI at 0.25, a miss |
| B127, activated charcoal | Swallowed Too Much? | [AI Generated: High 52, Medium 2](https://www.pangram.com/history/954b40f7-6e83-440d-bef6-a258a79fd1a5) | AI at 0.10, right |
| B127 with B128, poison control (41 words, so with its neighbour) | Swallowed Too Much? | [AI Generated: High 95, one window](https://www.pangram.com/history/862a4a34-aeee-4b38-921d-64db9367992b) | AI at 0.10, right |
| B130, the section's opening | Serotonin Syndrome (SS)? | [AI Generated: Low 20 on its first sentence, High 31 on the rest](https://www.pangram.com/history/c068929c-f8fb-444a-b182-12ce7bf2d60a) | AI at 0.15, right |

B127, B128 and B130 are his post's text with no version of his on record (the guide's record of his edits holds none of
their sentences), so they are mine to try next: three fresh reads and the tell panel, one small-fix try each, and a
card the same turn for any that stays below High (lesson bad-trips-2026-11-24w). Both misses were paragraphs with his
own asides in them ("a lot of CBD is fake or very dilute", "Another is tremor (shaking) along with ..."): a paragraph
that read AI inside a section check can read High by itself, so the by-itself check comes before any try, as in turn 49.

## What is left

[The list](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/articles/bad-trips/humanize/h75-20261124/LEFT.md): **139 of 222 blocks**, regenerated after this turn's
checks. The count had been overstated since turn 65 (160, then 157): the map took each block's latest check by sorting
the results' times as text, and older results carry a time of day only ("21:07:12"), which sorted after every dated
one, so a section check of 2026-11-11 counted as later than a by-itself check of this month. A result's time now counts
only when it has its date (lesson bad-trips-2026-11-24y; the fix is in the map itself). In MDMA: Magnesium Alarm only
B120 is left.
