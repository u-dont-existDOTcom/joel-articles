# Section 3 ("Why Communities Keep Dying in the Same Two Ways"): predictions before each Pangram call

## The published text (2026-10-01; texts in `base/`)

The whole published section was 100% AI on 2026-09-29 (`intentional-communities-baseline-03`, 357 words). Only P3, P6 and P8 are long enough to check alone; the rest are checked with a neighbor, headings as published.

| text | mine | why | Pangram |
|---|---|---|---|
| b-H1P1H2P2 | AI | the list of six feelings, then two short landings ("They acquire agenda items.") | AI 100 |
| b-P3 | AI | "Yet ... can't ... It can only ..." is a contrast march ending on a joke | AI 100 |
| b-P3P4 | AI | same, then "sits nearby with its arms crossed" | AI 100 |
| b-H2P5P6 | AI | definition, then the example, then a closing irony | AI 100 |
| b-P6 | AI | ends on "unusually difficult to escape", a summing-up irony | AI 100 |
| b-P7P8 | AI | "mirror each other" plus two parallel sentences, then a four-step list | AI 100 |
| b-P8 | AI | three "may" sentences in a row, then a four-part list | AI 100 |
| b-P8P9 | AI | same, and P9's "I want X without Y, and Z without W" | AI 100 |

All eight came back 100% AI, each flagged whole. Mine: 8 of 8. So every paragraph gets rewritten.

## v1: Emulate versions with small logged fixes (`fixlog-s3.json`; texts in `r1/`)

Predictions, written before the calls:

| text | mine | why | Pangram |
|---|---|---|---|
| H1P1H2P2 | Human | Emulate's shape; the six feelings joined by "or", not commas | Human 100 |
| P3 | Human | Emulate's shape, two small fixes | Human 100 |
| P3e | Human | the same with 🙄; Joel's list | Human 100 |
| P3P4a | Human | | |
| P3P4b | Human | Emulate's P4 unchanged | Human 100 |
| H2P5P6a | Human | | |
| P6a | Human | five fixes; "It's one thing ... It's another" is a stock turn, the risk | Human 100 |
| P6b | Human | one fix fewer | Human 100 |
| P7P8a | AI | P8a's opener is mine ("The deeper problem is that") | Human 100 |
| P7P8b | AI | the (a) to (d) list reads like a report | Human 100 |
| P8a | Human | Emulate's fragment of three examples breaks the march | Human 100 |
| P8b | AI | the lettered list | Human 100 |
| P8aP9a | Human | | |
| P8aP9b | AI | P9b's "That needs ..." is close to the published sentence | Human 100 |
| P8bP9a | AI | P8b's list | Human 100 |

All fifteen came back 100% Human. Mine: 10 of 15; the five I called AI (my P8 opener, the lettered list, P9b's closeness to the published sentence) all passed. Emulate with small fixes: every version passed, as in section 2.

The picks, by Joel's choosing rule (all fifteen passed, so the rule's later steps decide): P4b (Emulate's P4 unchanged, closest to the published meaning), P6a (keeps "intimate decisions"), P8a (P8b drops that the founder, therapist and farmer may be good at their roles, and its (a) to (d) list reads like a report), P9b (keeps "That needs", the published "That requires"). Then the whole section, and the same with the proposed 🙄:

| text | mine | why | Pangram |
|---|---|---|---|
| section-v1 | Human | every part passed in its own check | |
| section-v1e | Human | the 🙄 passed in P3 alone | |

## v2: the gate's meaning fixes (`fixlog-s3.json`, "v2"; texts in `r2/`)

The blind trace, the cold read and the grounding review found meaning shifts in v1. Each fix is the smallest change that restores the published meaning: one or two words in most paragraphs, a clause in P8. Predictions, before the calls:

| text | mine | why | Pangram |
|---|---|---|---|
| H1P1H2P2 | Human | three small swaps | Human 100 |
| P3 | Human | two one-word fixes | Human 100 |
| P3e | Human | the same with 🙄 | Human 100 |
| P3P4 | Human | two one-word fixes in P4 | Human 100 |
| H2P5P6 | Human | P5's two sentences joined; three fixes in P6 | Human 100 |
| P6 | Human | "was deeply shaped by" is the published phrase, the risk | Human 100 |
| P7P8 | AI | P8's new clause is mine, and P7 got shorter | Human 100 |
| P8 | AI | same clause | Human 100 |
| P8P9 | Human | P9's fixes are small | AI 100 |
| section-v2 | Human | | |
| section-v2e | Human | | |

Every paragraph passed alone or in its pair except P8P9 (100% AI; P8 alone passed). The whole section came back 34% AI, flagging P3 with P4's first sentence, and P6. Section v1 had been 100% Human. So the meaning fixes cost the section pass, and the fixes in P3 and P6 are the published wording put back: "groups", "stop hating", "was deeply shaped by". That's the section 2 lesson again, now at the section level. With 🙄 the section was 55% AI, so the emoji proposal is dropped (EMOJI-LIST: one that flips comes out). Mine: 7 of 11.

## v3: the section's flags (texts in `r3/`)

P4 back to Emulate's own (one referent fix), P6's strength fix in Emulate's other wording ("heavily influenced by"), P3 with and without "stop hating", P9 with only "no guru owns". Predictions:

| text | mine | why | Pangram |
|---|---|---|---|
| H1P1H2P2 | Human | one more word ("communes") | Human 100 |
| P3x2 | Human | v1 plus "groups" | Human 100 |
| P3x2P4 | Human | | |
| P6 | Human | | |
| H2P5P6 | Human | | |
| P8P9v1 | Human | v1's P9 passed with v1's P8 | Human 100 |
| P8P9B | Human | one fix in P9 | AI 34% (mixed) |
| P4prop | AI | the added sentence explains, and ends on "justice" | AI 43% (mixed) |
| P3x2P4prop | AI | same | Human 100 |
| section-a | Human | the published wording is out of the flagged spans | AI 12% (mixed) |
| section-b | AI | keeps "stop hating" | AI 16% (mixed) |

- section-a: 12% AI, one span from P3's second sentence through P4's first. That text is the same as in section v1, which passed; what changed is around it.
- section-b ("stop hating"): 16% AI, with P3's last two sentences and P6's last three flagged.
- "heavily influenced by" cleared P6 in section-a.
- P9 with "no guru owns" flagged at 34% in its pair, and the v1 P9 passed. So the published relation, put back, brought the flag back.
- The P4 proposal failed alone (43% AI, on the added sentence), so it isn't offered as a candidate.
- Mine: 7 of 11.

## v4 (texts in `r4/`)

P4 as Emulate's other version (P4a, with v1's fix), and two more wordings for the guru relation. Predictions:

| text | mine | why | Pangram |
|---|---|---|---|
| P3x2P4a | Human | v1's P3P4a passed | |
| P8P9C | Human | "isn't run by a guru" | |
| P8P9E | AI | "no guru controls" is the same shape as "no guru owns" | |
| section-c | Human | P4a breaks the chain the span ran along | |
| section-d | Human | | |

## v5 (texts in `r5/`)

v4: P3x2P4a, P8P9C and P8P9E passed; section-c 10% AI and section-d 15% AI, both flagging from P3's second sentence ("But the best meeting procedure in the world won't make ...") into P4. P3 is now Emulate's other version (e2-emuB). P9 is "isn't run by a guru" (passed in its pair). Predictions:

| text | mine | why | Pangram |
|---|---|---|---|
| P3B | Human | Emulate's own, unchanged | |
| P3BP4a | Human | | |
| section-g | Human | the flagged sentence is gone | |

## v6 (texts in `r6/`)

v5: P3B and P3BP4a passed; section-g 7% AI, now only on P4a, whose first sentence is my fix. So P4 goes back to v3's (Emulate's own, with "There will be a fight"). Predictions:

| text | mine | why | Pangram |
|---|---|---|---|
| P3BP4 | Human | both Emulate's own | |
| section-h | Human | no sentence of mine left in the flagged area | |
| H2P2P3B | Human | P2 with a neighbor that passes alone | |

v6: section-h 100% Human (487 words), P3BP4 and H2P2P3B 100% Human. So every paragraph passes alone or with a neighbor that passes alone, and the section passes whole.

## v7: the final cold read's and trace's fixes (texts in `r7/`)

P3: "any other", and "whoever raises it" for "one of them". P8: Emulate's "has too much authority, or rather," cut. Predictions:

| text | mine | why | Pangram |
|---|---|---|---|
| P3 | Human | two small changes | Human 100 |
| P3P4 | Human | | |
| P8 | Human | a cut, nothing added | Human 100 |
| P7P8 | Human | | |
| P8P9 | Human | | |
| section-v7 | Human | | |

v7 (checked by the worker from a corrected copy: my build wrote literal "\n" into the files, and the rebuilt files match its texts by hash): section-v7 100% Human (482 words), P3, P3P4, P8 and P7P8 100% Human, P8P9 37% AI on P9. Mine: 5 of 6.

## v8 (texts in `r8/`)

| text | mine | why | Pangram |
|---|---|---|---|
| P8P9E | Human | passed with v2's P8 | AI 100 |
| P8P9aC | Human | Emulate's own build of P9 | Human 100 |
| section-v8 | Human | v7 passed whole; only P9 changed, to the build that passed in its pair | Human 100 |

## Where section 3 ends (v8, installed as a candidate)

- The whole section is 100% Human (481 words).
- Every paragraph passes alone, or with a neighbor that passes alone:
  - P1 and P2 with the headings, and P2 with P3 before the last two-word fixes to P3;
  - P3 alone, and P3 with P4;
  - P5 with P6, and P6 alone;
  - P7 with P8, and P8 alone;
  - P8 with P9.
- The meaning checks on the final text: the blind trace (v6, plus the two-word v7 fixes) and the cold read (`SENSE-v8.md`). What's left, and why it stays, is in the side-by-side notes and in `fixlog-s3.json`.
- The emoji proposal and the P4 proposal are out: 🙄 raised the section from 34% to 55% AI, and the added P4 sentence was 43% AI alone.
- Pangram used on section 3 this turn: about 140 credits.
