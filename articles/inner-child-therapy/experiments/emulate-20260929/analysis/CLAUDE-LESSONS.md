# What the Emulate run taught me about passing Pangram

**By Claude, 2026-09-30.** From the 56 sentence checks GPT ran on 2026-09-29 (`runs/sentence-check-queue.json`, results in `runs/pangram.jsonl`), the slop comparison (`CLAUDE-SLOP-COMPARISON.md`), and Joel's own fixes in set A. Each rule gives its evidence by check id, how sure I am, and what would prove it wrong. A put-back is one of my draft sentences put back into a version of Emulate's that had passed 100% Human.

## What the checks showed

- **Put-backs:** 32 of 36 stayed 100% Human. The four that came back AI: `putback-A18-03` (30% AI), `putback-B01-02` (31%), `putback-A10-05` (35%) and `putback-B07-02` (100%).
- **Fixes to versions of Emulate's that passed:** 13 of 13 stayed 100% Human. Seven only fixed noise (spacing, quote marks, a typo, British spellings). Six fixed content: an invented "my kids", an invented "toddler" and "McDonald's", "12 pm" for "midnight", a reversed point, a wrong pronoun, and "tell them" for "tell yourself". Two of the six replaced a whole clause with my own wording.
- **Controls on Joel's one-sentence fixes:**
  - A12: my draft was 100% AI. Joel's one-clause change made it 100% Human. Two tiny word swaps elsewhere ("for a minute" to "for now", "clue" to "idea") left it 100% AI.
  - A21: my draft was 100% AI. Cutting its "So…" closing (Joel's cut) and cutting its first sentence instead both made it 100% Human.

## The rules

**1. Don't rewrite everything. One of my sentences among human ones usually passes; it's AI-shaped sentences together that get caught.**
- Evidence: 32 of 36 put-backs stayed Human. About half the words in Joel's set A fixes come straight from my drafts (47% on average), and his fixes pass.
- Confidence: high that a single sentence rarely sinks a human paragraph. This says nothing yet about how many of my sentences a paragraph can hold; my full drafts were 100% AI.
- Wrong if: paragraphs where I keep most sentences and change a few, the way Joel does, keep failing.

**2. Don't list concrete examples in one breath. Give one example its own sentence, two at most, and drop the rest.**
- Evidence:
  - `putback-A18-03` flagged exactly my sentence "Maybe what's actually happening is a knot in your stomach, an urge to leave, some image that keeps coming up, a song that suddenly feels relevant." Joel's A18 fix of that sentence kept two examples in two sentences: "Maybe what's actually requiring your attention now is a knot in your stomach. Or perhaps you're in a place you want to leave."
  - `putback-B01-02`: "Care might start as locking the door at night, eating an actual meal, cancelling something you didn't have the energy for, or putting your phone down at midnight." The flag covered it and the two sentences before it.
  - A12: Joel's change that flipped the verdict turned "The jaw is already tight, the stomach is already involved" into "The jaw and stomach are already tight", which also breaks up a series.
  - `putback-A10-05` put one item of a parallel list back. The flag landed on the next list item and the closing.
- Against it: `putback-B01-04` put back a five-part list of reasons ("fear, not knowing what you were aiming for, not knowing how, being exhausted, or something practical getting in the way") and stayed Human. `putback-A08-03` put back three questions in a row and stayed Human. The lists that flipped were concrete and vivid; the one that didn't was a list of reasons.
- Confidence: moderate.
- Wrong if: splitting such lists in new drafts doesn't change verdicts, or lists of reasons flip as often as lists of vivid examples.

**3. Don't sum a point up in a "what X ends up doing is Y" sentence.**
- Evidence: `putback-B07-02` turned a 75-word passing text 100% AI with "What your little one ends up trusting is what the Protector does out in your life, and at its biggest it can mean leaving a relationship that keeps wearing down your safety."
- Confidence: low. It's one case, and the put-back also repeated the next sentence's point about leaving a relationship.
- Wrong if: the same shape put into other human texts doesn't flip them.

**4. When Pangram is sure, change a sentence's shape; swapping words doesn't help.**
- Evidence: A12's two tiny swaps stayed 100% AI; Joel's change to one sentence's structure flipped it.
- Confidence: moderate, from one paragraph.
- Wrong if: word-level edits flip other paragraphs Pangram is sure about.

**5. A cut can flip a short paragraph, and it doesn't have to be the "right" sentence.**
- Evidence: in A21, cutting either end worked.
- Confidence: low. Both cuts left 53 words, close to Pangram's 50-word floor, where it may lean Human.
- Practical: check a paragraph at the length it will really have in the article, not trimmed.

**6. Fix facts after the fact. A passing text survives small corrections, even in my words.**
- Evidence: 13 of 13 fixes stayed Human. The noise in Emulate's output (typos, "do n't", odd quote marks) isn't what made it pass.
- Confidence: high for one or two small edits per text. Untested for several edits in one paragraph.
- Wrong if: texts with several corrections go back to AI.

**7. Always check a paragraph in its section, and recheck its neighbors after any change.**
- Evidence:
  - In community section 1, rewriting the flagged opening moved the flag onto the next paragraph, which was Human in the baseline.
  - In `putback-A10-05` the flag landed on Emulate's own lines after my item.
  - B01 version 2 passed alone and showed 8% AI after the section before it.
- Confidence: high.

**8. The linter's contrast and coaching rules don't predict Pangram.**
- Evidence: three sentences the linter flags stayed Human when put back, two at High confidence:
  - "If there's a hard moment you can see coming, it can help to practice what you'll say ahead of time." (`putback-B01-03`)
  - "And if you did it and didn't feel better right away, that doesn't mean it failed, but doing it doesn't prove it helped either." (`putback-B01-05`)
  - "Keep what actually makes your little one safer, closer to you, more capable, or happier, not just what gets a check mark." (`putback-B01-06`)
  
  Joel's fixes also have more of these than my drafts.
- Joel's bans still apply: they're his taste, not Pangram's.
- Confidence: moderate to high.

## What a chat model can't copy

Emulate passes by retelling everything in another writer's words. Only 9% of its words sit in 4-word runs from the draft. That comes from a model trained on human text, from its word probabilities, and I can't follow it as a rule.

Joel's route I can follow: keep what's already right, and change the thought where it's generic. He cuts a point, disagrees with the draft, or pins it to one specific, slightly odd detail.
