# Proposal: train a fast model that turns AI drafts back into human writing

**For GPT Pro.** Written by Claude for Joel on 2026-09-29. Write a proposal only; don't build anything yet. Claude will check it afterwards. If you can't search the web, ask Work to do the lookups and give you a sources file.

## The goal

Build a model that takes an AI draft of one of Joel's articles and rewrites it so that it:
- passes Pangram in context, meaning inside its section with the heading and the paragraphs around it;
- keeps every point, fact, name, number and link of the draft;
- avoids the tells in `articles/inner-child-therapy/tools/tells_lint.py` and in Joel's bans;
- runs about as fast as Emulate (5–9 seconds for 75–180 words in Claude's test) and costs about the same or less.

Later, it should also sound like Joel.

## What we know

- **Emulate** (https://www.tryemulate.ai) passes Pangram well, but it fudges meaning. In Claude's test one version turned "keep what helps, not what earns a tick" into "just tick them off." It also has audible tells: "warm and fuzzy", runs of five questions, "It's okay… It's okay…".
  - Their research page says they train their own models on how real people write.
  - Their API returns one version per call.
  - Data and details: `articles/inner-child-therapy/experiments/emulate-20260929/runs/CLAUDE-API-TEST.md`, plus tonight's overnight run in the same folder when it's done.
- **Joel tried fine-tuning GPT with LoRA and it didn't seem useful.** Claude's guess: a chat model keeps its trained habits under a small fine-tune.
- **Base models write nonsense from nothing, and chat models are hard to pull out of their attractor.** Joel raised both. Claude's view is that rewriting is a conditioned task: the draft supplies the content and order. So a base model fine-tuned on rewrite pairs should stay coherent while keeping human-like word choice. **That's a hypothesis. The pilot has to test it, and the proposal mustn't assume it.**
- **Human writing:**
  - Joel has plenty of pre-AI writing by other people.
  - He has little of his own. Most is college work he didn't keep.
  - He has 125 before-and-after pairs of his own fixes (`articles/inner-child-therapy/tools/JOEL-FIXES-CATALOGUE-20260928.md`), and his hand-humanized articles in the repo.

## The core idea

**Reverse generation.**
- Take human writing from before ChatGPT (late 2022), so it's certainly human.
- Have the chat models Joel actually drafts with (Claude, GPT) turn it into typical AI text.
- Train a model to go from the AI version back to the human original.

Design these points carefully:

1. **Two kinds of pairs.**
   - **Paraphrase pairs** ("rewrite this more clearly") keep the human structure, so they only teach word-level fixes.
   - **Regenerated pairs** have the chat model write the paragraph fresh from a content outline of the human text. These have AI structure, closer to Joel's real drafts, so they teach structural fixes.

   Propose a mix, and a way to measure what each kind teaches.
2. **Don't teach it to invent.** If the human original contains details the AI version lacks, the model learns to make details up. That may be where Emulate's drift comes from.
   - Make the outline carry every concrete detail.
   - Drop any pair where the human text says something the AI version doesn't.
   - Say how you'd check that at scale.
3. **Match the register.** Joel writes personal, spiritual, psychological and practical essays in second person, with his own first person. Choose human sources in that register. Say which sources, their licenses, and how many words each has.
4. **Match the inputs.** Make the AI versions with the same models and prompt styles Joel's drafts come from, so the model learns to undo the drafts it will actually see.

## What the proposal must cover

1. **Data:** sources, amounts, how pairs are made, filters (meaning, Pangram on a sample, the linter), and how much Pangram checking costs.
2. **Models:**
   - two or three candidates of different sizes (for example around 8B and around 30B), with base and lightly tuned versions;
   - LoRA versus full fine-tuning, and why LoRA failed for Joel on GPT;
   - license, context length, and the hardware each needs.
3. **Training:** supervised fine-tuning first, then preference training. For preference training, pairs of "chosen" (passes in context and keeps the meaning) and "rejected" (flagged, or drifts), made by generating 3–4 versions per paragraph.
4. **The test set:** 50–100 AI paragraphs never used in training, drawn from the guide texts and Claude's failed drafts.
   - Don't use `articles/inner-child-therapy/experiments/emulate-20260929/inputs/learning/E_holdout/`. That's reserved for Claude.
   - Measure: Pangram alone and in context, meaning kept (a point-by-point check by a judge model, plus a sample Joel reads), facts kept, linter hits per 100 words, speed, and cost per 1,000 words.
   - Compare with Emulate on the same set.
5. **A pilot:** about 1,000–2,000 pairs, one or two models, run on the test set against Emulate.
   - Give the rough cost and time.
   - State the result that would justify scaling up, and the one that would stop the project.
6. **Joel's voice:** a second stage trained on his fixes and his own paragraphs. Say what it needs, given how little of his own writing there is.
7. **Serving:** hosted options that run fine-tuned open models or LoRA adapters. Give the speed for 300 words and the cost.
8. **Risks:**
   - detectors retraining on a humanizer's output;
   - copyright of the human sources;
   - meaning drift;
   - the model learning to undo only one AI model's style;
   - the budget.
9. **Budget and timeline** for the pilot and for the full version.
10. **Questions for Joel,** at most 5.

## Rules

- Verify every named model, service, price, license and dataset with a source URL, dated. If you can't confirm something, say so. Joel's rule: no unverified specifics.
- Mark each estimate as an estimate.
- Plain words, no hype, and no "That's not X. It's Y." Keep it to about 3,000 words.
- **Where to save:** write it as `docs/reverse-model-20260929/TRAINING-PROPOSAL.md` in `joel-articles`.
  - Use a branch `gpt/reverse-model-proposal-20260929` made from `origin/handoff/claude-dangerous-adult-20260924-1631`, and push that branch.
  - Never touch `main` or the handoff branch, and never force-push.
  - If you have no repo access, give Joel the file.
