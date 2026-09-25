# Checking R13/R14 — sentence-engineering outcome and owner-help gate

Date: 2026-09-20
Status: **TRUE SENTENCE ENGINEERING IMPROVED LOCAL DETECTOR MARGIN BUT DID NOT PASS / SAME-CONTEXT LOCAL REPAIR STOP**

## R13

R13 was the first post-R10 candidate produced from a frozen sentence-by-sentence engineering guide rather than a fresh holistic rewrite.

Exact model-only section:
- 177 words
- SHA-256 `2f4bb7c0daf2a16dfe926e5a6fad9c6275b92627233e7316ceddb77172603f2a`
- Pangram 4.0: AI 1.0 / Human 0.0
- prediction probability 0.9945067167
- exact_utf8.

R13 long discrimination paragraph:
- 75 words
- SHA-256 `5f019e5baea5c17c5418b5f95bc0c1cdc22675a6fb81212a38691ead7c661ca9`
- Pangram 4.0: AI 1.0 / Human 0.0
- prediction probability 0.5882422328
- short-text confidence limited
- exact_utf8.

The lower internal probability is **not** treated as a Human percentage or production success. It only motivated one final, local, meaning-preserving residual repair.

## R14

R14 replaced only R13's stubborn long discrimination paragraph with the best of four local sentence-engineered realizations.

Exact model-only section:
- 172 words
- SHA-256 `dd1e168619f9c28f972fe06de4deb34436be6040e651d6554c638683fe0d50ae`
- Pangram 4.0: AI 1.0 / Human 0.0
- prediction probability 0.9998726845
- exact_utf8.

R14 residual paragraph:
- 70 words
- SHA-256 `32c9633a41c424d0c6dfac61ac1dc87c745f484a7031c2d58e7a2f41c55015c2`
- Pangram 4.0: AI 1.0 / Human 0.0
- prediction probability 0.8437833786
- exact_utf8.

R14 regressed relative to R13's internal score and did not change the binary result.

## What the experiment establishes

1. The owner's sentence-engineering hypothesis was executed in its intended form:
   exact existing sentence/span -> disposition -> causal defect -> protected function -> local operation -> integration.
2. This representation changed the writing more usefully than vague whole-paragraph instructions, but it did not independently humanize this checking section in the current Chat.
3. The local residual remains the main blocker. Repeated same-context prose variations are now correlated evidence and must stop.
4. The tell ledgers were useful for catching some known model features, but three successive ledger gates produced false positives. The ledger is not a reliable substitute for owner/cold judgment or detector evidence.
5. Adding more anti-pattern rules now would be the wrong architecture response.

## Exact owner-help target

The useful owner input is **one free same-meaning rewrite of the stubborn discrimination paragraph**, not the entire section and not a Pangram-minimal tweak.

### Original source paragraph

> Handle whatever safety issue or practical thing actually needs doing. Then, before another round, ask what changed the last time you processed this. Did you finally feel something you had only been thinking about? Did you notice something new enough to change a decision or how you respond? Or are you asking the same question again because the answer didn't feel certain enough? Grief can come back to familiar ground. Repetition by itself doesn't mean the child has a new request.

### Latest model residual

> Before another round, I'd look back at the last one. Did anything actually change? Maybe you finally felt something you'd only been thinking about, and then you responded differently. If not, and you're back because you still don't feel sure, I wouldn't assume the question itself means the child has something new to say. Grief comes back to familiar ground too, which is what makes this annoyingly hard to judge.

Owner rewrite request:
preserve the original paragraph's substantive meaning as much as possible, but prioritize how Joel would naturally write the thought if the current wording did not exist. Meaning additions/clarifications are allowed but must be identified afterward so they are not mislabeled as pure style transfer.

Why free rewrite rather than minimal Pangram patch:
the current project goal is reusable Human writing competence, not merely detector evasion. Minimal detector repair can teach local Pangram sensitivity; a freer same-meaning rewrite is stronger evidence about thought order, emphasis, sentence duration and what Joel leaves implicit.

## Stop rule

Do not generate another same-context model rewrite of this paragraph before owner input. After owner rewrite:
- preserve exact before/after;
- classify meaning changes;
- derive sentence/topology transformation;
- test a **different** model paragraph for transfer rather than simply copying Joel's rewrite back onto this one.
