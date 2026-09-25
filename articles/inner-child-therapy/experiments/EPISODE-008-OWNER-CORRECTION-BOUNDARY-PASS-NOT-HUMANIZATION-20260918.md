# Episode 008 — owner correction: full-boundary detector pass is not humanization proof

Date: 2026-09-18
Status: **OWNER METHOD CORRECTION / K RECLASSIFIED AS DETECTOR-BOUNDARY PASS, NOT MODEL-HUMANIZATION SUCCESS**

Joel's correction:

> your parts alone still read AI to me and pangram so we basically just learned to trick it but that should break when they update it to work better.

This supersedes any prior language treating anchored Candidate K's Pangram Human 1.0 as evidence that the model-written flanks themselves had been humanized.

## Correct interpretation of K

K proves only:
- a mixed boundary containing a large owner-written Human anchor can be arranged so Pangram 4.0 labels the complete boundary Human 1.0;
- the detector is strongly context-sensitive;
- anchor placement/boundary geometry can mask or alter the score of adjacent model prose.

K does **not** prove:
- the model-written opening is Human;
- the model-written ending is Human;
- the model learned a robust Human realization;
- the passage will survive a stronger/future detector;
- the model-written spans would pass independently.

Joel's direct editorial judgment is that the model spans still read AI.

Joel also reports that Pangram reads the model parts alone as AI.

Therefore K fails the actual owner outcome of humanizing the model prose.

## Stronger production criterion

A model-humanization success now requires:

1. **Owner/editorial pass on the model-written prose itself** — not merely on a mixed full boundary.
2. **Detector evidence that does not depend on masking by a known-Human owner anchor.**
3. Preservation remains exact.
4. Full-boundary Pangram remains useful secondary evidence, but cannot by itself establish humanization when model-only spans remain AI.

## Historical re-audit implication

Previous detector-Human model results must be separated into:
- **owner/editorially accepted model humanization**, versus
- **detector-only boundary pass**.

Known examples already reclassified in the humanization lab as detector-only/weak style evidence include:
- EFT successful model transfer;
- `The same principle extends...` / `This also happens...`;
- explanatory completion controls.

Episode 007 My Journey R8F remains stronger because Joel explicitly judged the final boundary:
`perfect, 100% human high conf. looks like we've nailed the process now at least for this style of writing.`

But even R8F does not prove its changed 39-word model sentence would pass Pangram in isolation; its evidence is whole-boundary + owner acceptance.

## Current disposition

Do not promote K into the rolling article as humanized prose.

Treat the owner anchor as valuable teaching/source material, not as a detector shield to make adjacent AI prose count as Human.