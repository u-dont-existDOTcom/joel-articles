# Why the cold reader "couldn't parse" Joel's clause (debugged 2026-10-11)

Joel, 18:35 UTC: "\"as I'm describing may happen in my case\" is obvious so you should debug why the cold reader can't understand it."

The clause, in his J1: "it's especially so in communities which form naturally over time as I'm describing may happen in my case."

## Tests (all Sonnet, the model the cold reads use; prompts and reports in this folder)

| test | what changed | flagged the clause? |
|---|---|---|
| A1, A2 | the lane's cold-read prompt as used all along (a three-line summary of the article before the section) | yes, 2 of 2 ("can't parse", "tangled") |
| B1, B2 | the same prompt with the whole article before the section instead of the summary | yes, 2 of 2 |
| C1, C2 | A's prompt, with a comma before "as" in the clause | yes, 2 of 2 |
| T1 | asked directly what the clause means | paraphrased it right: "which, as I'm explaining, may be how my community forms"; called it the "as I fear may happen" construction, strained by "describing", with a reread at "may happen" |
| D1, D2 | A's prompt, plus: give your best reading of a phrase before reporting it; if that reading is clearly what the author means, leave it out | no, 0 of 2 (both still raised real questions: why "especially so", why the divorce detail) |

## What was wrong

1. **Not missing context.** The whole article before the section didn't change the flag (B). It did remove other false flags that came from the summary: "circles" (explained in section 9) and the heading's "Founderism".
2. **A reviewer told to report stumbles reports a stumble as a break.** The clause makes a reader pause at "may happen" ("as I'm describing" first reads as finished), and the prompt asked for anything that "stops you" without asking whether the reader still gets it. Asked directly, the same model gets it. With the best-reading rule it stops reporting it, and keeps reporting the questions a reader really has.
3. **Underneath: this lane's cold read was a hand-written prompt, not the shared one.** The shared sense prompt (`tools/humanization/reviewer/sense.txt`) and the gate's S3 already had two fixes this prompt never got: give the reader what they've already read (2026-09-30), and a word pointing to something its own sentence gives isn't unclear (2026-10-02). The community lane wrote its own summary instead.

## Fix

- The best-reading rule goes into the shared sense prompt and the gate's S3 (pull request 159), scoped to following the words: a jump, or a sentence with no reason to be there, still gets its line.
- The community lane's section cold read is built from the whole article before the section and the shared rules (`reviewer.py sense-section`, same pull request), not written by hand.
- Checked blind with planted breaks (`tools/humanization/reviewer/sense-validation/RESULTS-20261011.md`): the clause came back OK 4 times out of 4, and every planted break was caught (a pronoun pointing at nobody 8 of 8, an aside with no reason to be there 4 of 4). The section reads with the whole article raised nothing else on v11.
- A wording note for Joel, not a fix: "describing" is a weaker host for this construction than "saying" ("as I'm saying may happen in my case"). His call.
