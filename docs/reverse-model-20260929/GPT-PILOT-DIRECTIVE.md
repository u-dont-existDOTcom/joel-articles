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
