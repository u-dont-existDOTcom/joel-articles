# Episode 008 — Write It. Don't Send It Yet — controller refinement after R5 baseline

Date: 2026-09-18
Status: **R5 IS BEST MEASURED BASE / USE CONTROLLED REGIONAL CHANGES + CONTINUOUS SIGNAL**

## What the baseline taught us

All candidates A-G and the R5 baseline are still Pangram AI 1.0 at the segment level.

But the document prediction probability is not flat:

- new Candidate F, best new rewrite: 0.992172 AI probability;
- exact R5 baseline: **0.935703** AI probability.

So the new humanization rewrites were making the detector more confident in AI even though the coarse fraction stayed at 1.0.

## Controller correction

Do not throw away the continuous detector signal when the segment label is saturated.

For the next experiments:
- keep the R5 literal baseline as the control;
- change one paragraph/region at a time;
- preserve the unchanged regions exactly;
- run GUI immediately;
- prefer changes that lower AI probability or create a Human segment;
- revert regressions.

This is not a detector-only optimization rule. Preservation and Joel editorial quality remain blocking.

## First controlled region

Keep:
- the R5 opening sentence/paragraph exact;
- the R5 final caring-for-writer paragraph exact.

Change only the middle editing paragraph, because it has the densest directive/list structure.

If the probability worsens, revert and probe a different region.