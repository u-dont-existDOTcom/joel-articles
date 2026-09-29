# Handoff 3: training a model that turns AI text back into human text

Written by Claude on 2026-09-29.

## The idea

Take human writing from before late 2022. Have an open-weight chat model turn it into typical AI text. Then train a model to turn the AI version back into the human original, so that it does in one fast pass what Emulate does, but keeps the meaning better.

It gets two modes, like Emulate: rewrite (humanize a draft) and write (from a prompt). A general model comes first. A mode in Joel's voice may come later, as a separate option.

## Where it lives

All in `docs/reverse-model-20260929/` in `joel-articles`:
- **`GPT-PROPOSAL-DIRECTIVE.md`:** what GPT Pro was asked to propose.
- **`TRAINING-PROPOSAL.md`:** GPT Pro's proposal, on branch `gpt/reverse-model-proposal-20260929`.
  - Pilot $1,400–2,500; full version $16,000–27,000. Both are mostly Pangram checks at API prices.
  - Worth keeping from it:
    - the terms-of-service point: no Claude or GPT output in training data (Anthropic's commercial terms §D.4);
    - the serving-cost point: a GPU left running for one person costs far more than Emulate's plan.
- **`GPT-PILOT-DIRECTIVE.md`:** the lean pilot Joel chose.
  - It compares the 30B Qwen base and instruct models (Qwen3-30B-A3B, as GPT's proposal lists; confirm on the model card), each with a LoRA adapter, against Emulate on the same inputs.
  - Budget: at most $100 cash, 500 Pangram credits and 3,000 Emulate words.

## Joel's decisions so far

- 30B rather than 8B: better writing makes the test more telling, and he has run a 30B Qwen cheaply on one GPU before.
- Pangram's API is too costly, so use the dashboard in the cloud browser with Joel signed in.
- General first; his voice later and optional.
- He has plenty of other people's writing from before AI, but little of his own.

## What it's waiting on

- **The Emulate run's output checks.** The pilot's test set reuses Emulate's versions of learning sets A and B, with their Pangram results, from the Emulate run (Handoff 2). If those aren't checked yet, the pilot checks them itself within its budget.
- **Joel:** picks the GPU provider and signs in. He also says whether this is a private tool or a service, which decides whether serving costs matter.

## What Claude does

- Reviews the pilot results and re-checks the meaning of 20 outputs.
- Decides with Joel. **Go** if the model is within 10 points of Emulate on Pangram and clearly better on meaning. **Stop** if it's incoherent or passes less than half the time.
