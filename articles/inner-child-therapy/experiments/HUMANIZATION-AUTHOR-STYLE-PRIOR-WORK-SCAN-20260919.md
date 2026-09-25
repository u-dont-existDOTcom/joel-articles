# Inner Child humanization — bounded author-style prior-work scan

Date: 2026-09-19
Status: **DECISION-SUFFICIENT / COMPOSE + EXPERIMENT**
Branch: `chat/inner-child-humanization-recovery-20260918-0037`

## Independent conception frozen before outside scan

Observed project problem:
- broad generation repeatedly returns to predictable marching advancement and polished compression;
- same-context/local revision can diagnose the problem while reproducing it;
- Episode 007 succeeded only after large Human regions already existed and the repair scope narrowed around residual red spans;
- the unresolved Episode 008 target is closer to an all-red substrate;
- Joel reports that GPT-5.6 Pro was materially better in prior writing trials, while Work Ultra also looked good but is too expensive for routine use.

Candidate mechanism before research:
1. use Pro to create a better initial substrate rather than asking cheaper models to endlessly repair an all-red paragraph;
2. generate as a continuation from accepted local article prose rather than as a rewrite of known-AI prose;
3. freeze any genuinely good/Human regions;
4. use cheaper local engineering only after localization exists.

## Bounded prior-work findings

### Author-specific style transfer is genuinely hard
Khan et al. (2023), *Learning to Generate Text in Arbitrary Writing Styles*, reports that instruction-tuned models can struggle to reproduce an author-specific style from a small sample. Their stronger method adds author/style representations plus sequence-level control rather than relying only on instruction prompting.

Implication here:
more verbal style instructions are not a strong reason to expect the same generator to escape its prior.

### Few-shot and completion context can materially improve style matching
Jemama & Kumar (2025), *How Well Do LLMs Imitate Human Writing Style?*, compared zero-shot, one-shot, few-shot, and completion prompting and found large style-fidelity gains from few-shot/continuation conditions. The paper also found that high style similarity did not make model text statistically human-like.

Implication here:
local continuation from accepted article prose is worth testing, but style resemblance alone does not establish the owner's Human-writing target or Pangram robustness.

### Explicit register analysis can improve example-based style transfer
Yang & Carpuat (2025), *Steering Large Language Models with Register Analysis for Arbitrary Style Transfer*, reports better style-transfer strength and meaning preservation when the prompt explicitly analyzes register rather than relying on an undifferentiated exemplar.

Implication here:
a small, positive author-calibration layer may be useful after the clean continuation control. Do not begin with a large anti-pattern stack.

### Self-revision is not a reliable universal escape
Jiang et al. (2024), *SELF-[IN]CORRECT*, found that models were not reliably better at discriminating/refining their own generated responses than at initial generation.

Implication here:
this is consistent with the project evidence that repeated same-generator critique/repair becomes correlated. Prefer an independently generated Pro seed over another same-context revision loop.

## Existing-work map

Already useful:
- few-shot/local continuation for authorial-style conditioning;
- compact positive style/register characterization;
- sequence-level evaluation separate from semantic preservation.

Partially solved:
- generic author-style transfer. Existing work does not solve Joel-specific thought shape, article-function preservation, or Pangram robustness.

Incompatible as direct acceptance:
- pure stylometric similarity, because Joel's target includes editorial quality, provenance, semantic fidelity, and robust detector behavior;
- iterative self-refinement as the main architecture, because local project evidence already shows correlated failure.

Novel remainder:
- build a high-quality Human substrate for this exact Joel-byline article from model-generated prose without owner publication wording;
- determine whether Pro materially changes that substrate;
- decide how to combine Pro seeding with cheaper residual engineering.

## Disposition

**COMPOSE + EXPERIMENT**

Use:
- Pro for an isolated continuation-style seed;
- current accepted local article prose as the continuation context;
- minimal target-local generative deltas rather than the full prohibition archive;
- preservation + owner/editorial judgment as primary gates;
- Pangram only after the prose survives cold review;
- residual sentence engineering only after a real green/red map exists.

Strongest external baseline:
author-conditioned few-shot/continuation generation, not repeated zero-shot rewriting.

## Stop rule

Do not infer that Pro solves the problem from one attractive paragraph. Require a second fresh target transfer before promoting the method as a reusable generation skill.
