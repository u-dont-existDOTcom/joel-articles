# Turn 73 (2026-11-27): his round-62 answers into Beach Morning Glory

His round-62 export of 17:16 UTC ([the answers](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/articles/bad-trips/review/r62/ANSWERS-R62-20261127-1716.json);
[what happened to each point](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/articles/bad-trips/review/r62/RESULTS-R62.md)). Both answers first went into a draft of the
whole section, which three fresh readers read ([needed](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/articles/bad-trips/humanize/h81-20261127/reads/need-final-bmg-sec.txt),
[his fixes](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/articles/bad-trips/humanize/h81-20261127/reads/his-final-bmg-sec.txt), [fit](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/articles/bad-trips/humanize/h81-20261127/reads/fit-final-bmg-sec.txt)): the draft packed
each answer into one long sentence and said "absorbs" twice. Then each answer went in one piece a check, in its
paragraph's own lineage, from the version that read High (lesson neuro-2026-11-27a). Every text was checked through the
API on his laptop with his key, plain, each with its prediction in the ledger first: 8 checks, 8 calls right. Every dose
and warning held (the R62 fidelity keys: R61 with his two amounts as numbers his card gave, the owner-edits and
keep-as-is checks). The texts are built from Git by [build_h81.py](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/articles/bad-trips/humanize/h81-20261127/build_h81.py), so his
answers' words are copied, never retyped.

## LEAF-JUICE, the handling paragraph (B174), checked with B171 before it ([apply_h81.py](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/articles/bad-trips/humanize/h81-20261127/apply_h81.py))

| Step | What | Pangram |
|---|---|---|
| try 1 (turn 72) | as the guide had it | [Human High 92](https://www.pangram.com/history/bb2893ad-0b54-4a9c-aa6f-7f7f8c882681) |
| 1 | "relax" for "affect", his word for what the juice does | [Human High 92](https://www.pangram.com/history/6f434514-16f1-4213-853d-4338ecab5d01) |
| 2 | "Its juice works through the skin almost as well as eating it does." | [High 92, Medium 13](https://www.pangram.com/history/5884722d-9667-4164-81eb-f164e27614e5), the new sentence alone |
| 2 again | "eating it" made "eating the leaf" ("it" could be the juice) | [High 92, Medium 14](https://www.pangram.com/history/0253376f-369b-46d0-b3e9-ebe8e06fc758) |
| 3 | his armpits: "..., so to give it on purpose, you can put the juice under the armpits, for example." | [**Human High 122 in one window**](https://www.pangram.com/history/6026d11b-3fe2-4dc8-b6dc-da84f960f053), in the guide |

## NIBBLE-SIZE, the amounts paragraph (B173), checked by itself: not in

| Step | What | Pangram |
|---|---|---|
| try 1 (turn 72) | as the guide has it, without his amounts | [Human High 67](https://www.pangram.com/history/6bc70ed9-07ac-4541-8f72-68f9ab8c5e2a) |
| try 2 (turn 72) | "sometimes smooths" | [Medium 35, High 31](https://www.pangram.com/history/99d65f8f-a9b9-4e0f-b467-9a8bd940e204) |
| 3 | his amounts, a sentence of their own after the nibble: "For nausea I'd try 200mg of leaf at a time, or 10mg of the extract paste." | [High 20, **Medium 16**, High 48](https://www.pangram.com/history/ddea8d92-30a7-4ecc-9c27-92b2fcaddfee) |
| 4 | his "more": "I'd give more than that only if the person doesn't mind their trip getting less intense." | [High 20, **Medium 16**, High 66](https://www.pangram.com/history/10d2a2a5-4b40-4e70-be85-78168a936f31) |
| 5 | "A tiny nibble, though, can ..." (built unlike the whole-leaf sentence) | [**Low 37**, High 66](https://www.pangram.com/history/b771d740-e2d4-4d0d-90b0-b12e30a8ccc5): the first two sentences in one window |
| 6 | "Eating a whole leaf" (the his-fixes read: say how the leaf is taken) | [High 21, **Medium 16**, High 66](https://www.pangram.com/history/5772af1d-708e-42f6-90a6-5126b6148ad9) |

Each piece of his answer read High; the window below it is the nibble sentence, "A tiny nibble can sometimes smooth
psychedelic nausea and even improve the trip without ending it.", unchanged, which Pangram sets apart in a window of its
own once the paragraph passes about 80 words (in turn 72's section check, the same sentence with the one before read Low
36). The lineage has used its six tries, so the paragraph stays as it is and goes to him with my best try as round 63's
TEACH-B173 (OWNER-EDITS.json r62-nibble-size waits for it).

**The section's second check waits** for his B173: it would hold a paragraph that is about to change.

## What I fixed in the tools

The near-miss rule (`tools/humanization/pangram_ledger.py`, `best_near_miss`) ranked tries by Pangram's likelihood
unrounded, as the API gives it, so try 3 above (2.6e-31, a Medium window) ranked as the paragraph's best over try 1
(7e-29, High in every window). It now ranks the likelihood in whole percent, as the web app shows it, and the words below
High decide a tie, as turn 50 meant (lesson bad-trips-2026-11-27i; test:
`tests/test_pangram_ledger.py`, the near miss ranks likelihoods as the web app shows them).

[What is left](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/articles/bad-trips/humanize/h81-20261127/LEFT.md): **117 of 222 blocks** (B171 and B174 now read High in their latest check).
