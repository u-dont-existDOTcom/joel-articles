# How often the tells show up in human prose (blind audit, 2026-09-27)

Joel, 2026-09-27 22:53: "run the ai tells list against the known human prose to see how often human prose has those ai tells… a human could write all of these ai tells also, but the chances are just much less. so by having a binary tell list we are being overly strict."

## What was done

- **Texts:** 28 with known Pangram 4.0 results: 14 Human (Joel's own paragraphs, and passing paragraphs of mine) and 14 AI (failing drafts, and the GPT-lane Also Look Outward P1). The Also Look Outward r3 draft was hidden among them.
- **Batches:** shuffled into four batches, one per fresh subagent, with no labels. Each agent applied the full inventory (T01–T29, C01–C04) row by row, quoting the words for every PRESENT or UNCERTAIN row.
- **Data:** results and key in `tools/calibration/TELL-AUDIT-BLIND-20260927.json`.

## Results (P = 1, U = 0.5; out of 14 texts in each group)

| row | human | AI | AI/human ratio |
|---|---|---|---|
| T23 generic-specific scenery | 1.0 | 4.0 | 3.0 |
| T05 convenient props | 0 | 1.0 | 3.0 |
| T08 image, then explanation | 0 | 1.0 | 3.0 |
| T18 premise and knock-down | 0 | 1.0 | 3.0 |
| T10 permission formula | 1.5 | 4.0 | 2.3 |
| T03 complication without setup | 1.5 | 3.5 | 2.0 |
| T20 engineered landing | 2.0 | 3.5 | 1.6 |
| T02 instruction-manual cadence | 5.5 | 9.0 | 1.6 |
| T21 condensed list sentence | 2.5 | 3.5 | 1.3 |
| T22 coach register | 1.0 | 1.5 | 1.3 |
| T12 matched pairs | 2.0 | 2.5 | 1.2 |
| T09 equal efficiency | 5.0 | 6.0 | 1.2 |
| T17 finished principle | 2.5 | 3.0 | 1.2 |
| T06 generic therapy abstraction | 3.5 | 3.5 | 1.0 |
| T28 forced closure | 2.5 | 2.0 | 0.8 |
| C02 referent | 4.5 | 3.5 | 0.8 |
| T04 scene skinning a checklist | 1.5 | 0.5 | 0.5 |

Rows not listed were almost never flagged in either group.

## How well the list separates the two groups

AUC: 1.0 would separate them perfectly; 0.5 is chance.

| score | AUC |
|---|---|
| count of PRESENT rows | 0.59 |
| count of PRESENT + UNCERTAIN rows | 0.76 |
| weighted sum (log ratios), fitted on the same texts | 0.91 |
| weighted sum, leave-one-out | 0.51 |

## What it means

- **Human prose has these tells too, often.**
  - Joel's own Also Look Outward P2 had 3 PRESENT and 5 UNCERTAIN, more than five of the AI texts.
  - T06, the "look at their own part" kind of abstraction, is as common in the human texts as in the AI ones. That bears out Joel's example.
- **As hard stops, the rows are too strict.** "A PRESENT row blocks the call" (E88) would have blocked 7 of the 14 human texts. It's withdrawn.
- **The weights overfit.** With 28 texts, weighting each row by its ratio looks good on the texts it came from, then drops to chance on a text it hasn't seen. Weights need far more texts before they mean anything.
- **The plain count of flagged rows (PRESENT + UNCERTAIN) carries a modest signal.** At 7 or more flagged rows, 9 of the 14 AI texts are caught, and 3 of the 14 human ones.
- **Who applies the list matters a lot.** On Also Look Outward r2, my own row-by-row audit found 13 PRESENT, and the blind agent found 0 PRESENT and 6 UNCERTAIN. The definitions leave too much to the reader.

## How the list is used now

- **Pangram is the gate, with the sense step before it.** No tell score can pass a paragraph Pangram flags, so there's no "only 88% AI, pass". A tell count also can't block a paragraph that makes sense and that Pangram reads as Human.
- **The list is a repair aid.** Every row gets a line with its words (no bulk clearing, E88). Repairs go first to the rows that lean AI in this data (T23, T10, T03, T02, T20) and to T05, T08 and T18 when they appear.
- **7 or more flagged rows is a warning.** It means rebuild before spending a call, but it isn't a verdict.
- **Rerun this calibration as texts accumulate** (the table in `HUMANIZATION-GATE.md` has 73), and redo the weights only on a leave-one-out basis.

## Correction, 2026-09-28 (Joel, 2026-09-27 23:52)

> "you could say while skydiving and it would still have the same marching order predictable cadence with optimized structure. you're telling me that's not a strong predictor of AI prose? … the idea that your independent reviewer said they aren't, shows the independent reviewer doesn't know what it's talking about."

He's right. The table above measures the reviewer, not the tells. The blind reviewer gave Also Look Outward r2 no PRESENT row at all, although Pangram rates it 100% AI and its march is plain: a command, a test question, the counter-question, an authority, a method, a caution, a reason, a rule. A reviewer that can't see the march in that paragraph can't tell us whether the march predicts AI. So "most rows show up in human prose too" and "the count barely separates the groups" are findings about that reviewer. The tells' own value is unmeasured here.

Outside evidence says structure does predict AI. SlopShape's game figures (`experiments/SLOPSHAPE-GAME-FINDINGS-20260926.md`):
- a closing move that restates or reframes the thesis: 77% of AI posts, 12% of human ones;
- the thesis stated before the first part: 93% against 51%.

**Model judges were tested the same night** (`tools/calibration/JUDGE-BLIND-HUMAN-OR-AI-20260928.json`). A fresh Sonnet and a fresh Opus each labeled the same 28 paragraphs HUMAN or AI, blind.
- Both got 18 of 28 right, and they agreed on only 12.
- Opus caught 11 of the 14 AI paragraphs, and called 7 of the 14 human ones AI.
- Sonnet let 8 of the 14 AI paragraphs through as human. It called two human paragraphs AI, and one of them was Joel's own P2.
- Sonnet's 15 of 15 in the SlopShape game was on 600–2,500-word, single-pass AI blog posts against pre-ChatGPT human posts. That's an easier test than short, edited paragraphs judged against Pangram.

**So the list is used like this:**
- **Blocks the call:** T02 (instruction-manual cadence), T09 (equal efficiency) and T13 (nothing noticed), the marching order Joel names. If one is present, rebuild before any call, and don't explain it away.
- **Repair hints:** the other rows, each still written out with its words.
- **The gate:** Pangram, with the sense step before it.
- **No model judge**, Sonnet or Opus, stands in for Pangram. Neither was reliable on these paragraphs.
