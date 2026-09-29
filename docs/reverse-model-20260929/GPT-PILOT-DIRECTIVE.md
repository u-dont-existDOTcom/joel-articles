# Lean pilot: a 30B rewriter trained to turn AI text back into human text

**For GPT Work.** Written by Claude for Joel on 2026-09-29. Pro is only for the reasoning steps you choose to give it. Claude reviews the results.

## The one question

A 30B model is fine-tuned to turn AI rewrites back into the human originals. On the same inputs, does it pass Pangram as often as Emulate while keeping the meaning better?

Everything else in `TRAINING-PROPOSAL.md` waits until this is answered: preference training, the write mode, the full-tuning comparison, and a Joel mode.

## Budget

Stop and report if any of these would run over:
- **Cash:** at most $100 in all, of which at most $40 is GPU time.
- **Pangram:** at most 500 credits, through the dashboard in your cloud browser with Joel signed in. Joel says the API is too costly.
- **Emulate:** at most 3,000 words.

**Shut the GPU down whenever it isn't in use**, and always at the end. Joel chooses the GPU provider and signs in himself; he has used a GPU VPS before. Training needs one 80 GB GPU. Serving the finished model can use a smaller one.

## Rules

- **No Claude or GPT output goes into the training data**, not as inputs, targets or filter labels.
  - Anthropic's commercial terms (§D.4) bar using its services "to train competing AI models" without approval, and GPT's proposal reports a similar OpenAI clause.
  - The AI side of each pair comes from an open-weight instruct model with a permissive license. Check the license on the model card before downloading.
  - Claude or GPT may score the test outputs, but only after training is done.
- **No text by Joel goes into training.**
- **Human text from licensed sources only.** Use the Open American National Corpus (written part) and MASC. Project Gutenberg books from PG-19 may make up at most 15%, so old-fashioned prose doesn't dominate. These are the sources in GPT's proposal; confirm each license before use. Joel's own collection of other people's writing stays out of this pilot until its rights are clear.
- **Secrets:** never commit or print a key or login.
- **Git:** work on a new branch `gpt/reverse-pilot-20260929` made from `origin/handoff/claude-dangerous-adult-20260924-1631` in `joel-articles`. Never touch `main` or the handoff branch, and never force-push.
- **Adapters:** save the trained LoRA adapters somewhere private that Joel owns. Never publish them.

## Steps

1. **Human passages.**
   - Take 1,200 passages of 100–250 words each: essays, news, practical and technical writing, email and letters.
   - Split them by source document before making any pairs: 1,000 for training, 100 for development, and 100 set aside as general test material.
2. **The AI versions.** Use the 30B instruct model from step 3, with thinking turned off.
   - **One third are paraphrases:** "Rewrite this paragraph to be clearer and more polished."
   - **Two thirds are regenerated in two stages:**
     1. Extract a complete list of the passage's content: every fact, example, number, name, qualification, negation, cause and relationship.
     2. In a fresh context that never sees the original, write the paragraph from that list alone. Vary the requests the way people actually use chat models: "write this up as a blog paragraph", "turn these notes into a section", "improve this".
   - **Filter the pairs in both directions.** Use the open model as the judge. The AI version must cover every claim in the human passage, and the human passage must cover every claim in the AI version. Drop any pair that fails. A human original that says more than its AI version would teach the model to invent details.
   - **Spot-check on Pangram:** 20 AI versions should read as AI.
3. **Train two LoRA adapters,** using the same data and settings for both.
   - **The models:** the 30B Qwen base and instruct checkpoints GPT's proposal lists, Qwen3-30B-A3B-Base and Qwen3-30B-A3B.
     - Confirm them on their model cards before downloading.
     - If your training tool can't handle this mixture-of-experts model, use a dense Qwen model of about 32B, base and instruct, and note the swap.
   - **The settings:** rank 64; attention and feed-forward layers; 2 epochs; loss on the target text only.
   - **The format:** "Rewrite this so it reads like a person wrote it. Keep every fact." followed by the draft. The target is the human original.
   - **Record:** exact model IDs, the tool and its version, every setting, time taken and cost.
4. **The test set, reusing tonight's overnight run.**
   - Sets A and B in `articles/inner-child-therapy/experiments/emulate-20260929/inputs/learning/` have 53 AI inputs. The Emulate run (branch `gpt/emulate-overnight-20260929`) has Emulate's version of each, so Emulate costs nothing extra here. For Emulate, compare only its first version of each input.
   - Some of those versions may still lack a Pangram result. If so, check them yourself within this budget.
   - Add 20 general AI paragraphs, made as in step 2 from the set-aside human passages. Run those through Emulate's API too (about 3,000 words).
   - Don't touch `E_holdout/`. It's reserved for Claude.
5. **Run both models on the test set,** one output each at temperature 0.8.
   - Serve them with a server that supports LoRA adapters, such as vLLM.
   - Time each output, and report the seconds per 300 words.
6. **Score all three systems** (base with adapter, instruct with adapter, Emulate):
   - **Pangram alone,** for every output.
   - **Pangram in context,** for 20 outputs. Put each output into its real section: `CONTEXT_section_so_far.txt` for B01, and the article sections for the others.
   - **Meaning,** with the open-model judge in both directions: the points dropped, changed or added, and any invented detail. Claude will re-check 20 of them.
   - **The tells:** `articles/inner-child-therapy/tools/tells_lint.py`, as hits per 100 words.
7. **Report** in `docs/reverse-model-20260929/PILOT-RESULTS.md`.
   - A table for each system: the Pangram pass rate alone and in context, meaning kept, invented details, linter hits per 100 words, and speed.
   - Ten side-by-side examples: the input, both models and Emulate.
   - All costs.
   - Commit every output and score.

## Deciding

- **Go** (plan the next round) if either adapter passes Pangram alone within 10 points of Emulate and keeps meaning clearly better: fewer dropped, changed or invented points.
- **Stop** if its writing is incoherent, or if it passes Pangram alone less than half the time.
- **Anything else,** report the numbers and let Joel and Claude decide.

## Clarifications for the running pilot (2026-09-29, 16:20 UTC)

Claude's answers to the worker's two questions. They replace the matching parts of steps 2 and 6. Nothing here changes the frozen sources, the 1,000/100/100 split, the 400/800 split between paraphrases and regenerations, or the matched Base and Instruct training.

### Pangram in context: 7 matched cases, 21 results

"20 outputs" meant about 20 scans in all, not 20 per system.
- Score 7 inputs in context, each through all three systems: 21 results. One is already paid for, B01's first Emulate version.
- The 7 are B01 plus the six cheapest candidates in `evaluation/context-candidates.jsonl` whose fixed context is at least 150 words, taking at most one input per section heading. By the saved word counts that's A24, A07, A02, A05, A28 and A10, with ties going to the lower ID.
- Below 150 words of context, the output is most of the scanned text, so the check says little about context.
- They're chosen from the fixed word counts alone, before any model output or detector result is seen.

### Order of Pangram spending within the 500 credits

1. Pangram alone, both adapters, on the 48 A and B inputs that have a cached first Emulate result. This is the go/stop measure. Never cut it.
2. The 21 in-context results.
3. Pangram alone on the 20 general cases, all three systems.

Before the first scoring scan, add up the cost from the actual output word counts, at one credit per started 100 words. If it won't fit in what's left, cut general cases first, in threes (one per system), longest first. Then cut context cases in threes, down to five cases. If step 1 alone won't fit, stop and report. Claude's estimate is about 125, 105 and 120 credits, which leaves roughly 100 of the 452.

### Scoring

- A pass is the detailed label "Human Written". Every other label (Mostly Human, Mixed, AI Assisted, AI Generated) is a fail, reported by name. Read the cached Emulate results the same way.
- Pass rates compare the three systems on the same inputs. If an adapter's output on one of the 48 is under 50 words, drop that input from all three denominators and report how many were dropped.

### The AI-draft spot check: a diagnostic that exposed a copying leak

The 12 AI Assisted and 8 Human Written are a diagnostic on untrained data. They aren't a stop/go threshold; those apply only to the trained adapters on the test set. But the saved pairs show why 8 read as human, without another scan, and the cause needs fixing before full generation.
- **Paraphrases:** 7 of 8 read AI Assisted.
- **Regenerations:** 7 of 12 read Human Written, and they're the ones that copy the original.
  - The notes are the passage's sentences almost word for word. Their longest run shared with the original is 10–18 words.
  - Six of the seven Human Written regenerations have a word-sequence similarity to the original of 0.63–0.85 and share runs of 19–41 words with it. H0012 is the exception, at 0.43 and 8 words.
  - The five AI Assisted regenerations sit at 0.40–0.58, with runs of 11–16 words.
  - Measured with Python's `difflib.SequenceMatcher` on whitespace-split words, `autojunk=False`, from `data/generated/train-pairs.jsonl` at `6e5b9d4`.
- The regeneration never sees the original directly, but its sentences arrive through the notes. Those pairs teach the model to change almost nothing.

**The fix,** open-model only and with no detector:
1. **Notes prompt:** short fragments in the model's own words, never sentences copied from the passage. Keep names, numbers, dates, units, links and quotations exact, with quoted speech inside quotation marks.
2. **Copy check,** mechanical: outside quotation marks, neither the notes nor the regenerated draft may share a run of more than 10 consecutive words with the human passage. On a failure, redo that passage's notes and draft once with a fresh sample. If it fails again, drop the pair and record why.
3. **Pairs already accepted:** run the check on every accepted regeneration and redo only those that fail. Leave the paraphrases as they are.
4. **All splits:** use the same pipeline for train, dev and test, before training either adapter.
5. **Report** in `PILOT-RESULTS.md`: similarity and longest shared run by method for the final training set, how many pairs the check dropped, and the acceptance rate before and after the fix. The retries add GPU time; they stay inside the $40 GPU cap.
6. **No new Pangram spot check.** Keep the 48-credit result as the record of the old pipeline.
