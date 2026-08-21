# Romance Part 1 — current repair checkpoint — 2026-08-21

Status: **Part 1 detector target reached on task candidate; canonical `main` unchanged.**

## Current exact candidate

Directory:
`work/romance-detector-repair-20260820/materialized-part1-repair-r7/`

- master SHA-256: `1c30999ce795bc07e3c3fbc04691506ce544c9402236086a2dfe02033a6e8a90`
- master words: 19,573
- Part 1 SHA-256: `08bcfc48ec9cc948641c53aca24abc8dd104cdc14734f3cab83e098f33af8941`
- Part 1 words: **9,719**
- Part 2 unchanged SHA-256: `20301b1bfb0052de694657411f231f82d9a45ae62ff9c4839015befce5c57dc2`
- Part 2 words: 9,703
- invariant audit: **PASS** — headings, native markers, Markdown link destinations, protected anchors, required repair anchors.

## Exact aggregate Part 1 result

Experiment:
`romance-detector-repair-20260820-part1-aggregate-r7-20260821`

- Pangram `4.0`
- `STAGE_SUCCESS`
- Human **`1.0`**
- AI `0.0`
- AI-assisted `0.0`
- headline `Human Written`
- exact reader-visible Part 1 SHA-256 `08bcfc48ec9cc948641c53aca24abc8dd104cdc14734f3cab83e098f33af8941`
- 9,719 words.

Part 1 therefore satisfies Joel's standing Pangram-4 detector target on this exact task candidate. This does not by itself make the article owner-final or alter canonical `main`.

## Aggregate progression

Registered baseline:
- Human `0.9205247164`
- 10,236 words.

Repair sequence:
- r2: Human `0.9847978949546814`
- r3: Human `0.980210542678833`
- r4: Human `0.992400050163269`
- r5: Human `0.9838229417800903`
- r6: Human `0.9811084866523743`
- r7: Human **`1.0`**.

The non-monotonic scores are important evidence: locally correct changes can move an aggregate score down before later architecture/interaction repairs clear the complete boundary. Do not optimize solely by retaining whichever intermediate draft has the highest partial aggregate percentage.

## Final local repairs that cleared r7

### `part1-affection-simmer`

Used **6/6** section calls. Final 274-word transition boundary passed 100% Human/high confidence.

Winning move: stop `Affection and the simmer` after its two actual source-derived observations rather than adding the generalized `sex is a barometer / don't make her manufacture desire` wrap-up immediately before the next explanatory section.

No seventh Affection call is permitted.

### `part1-casual-sex-situationship`

Used **5/6** section calls. The complete 796-word natural section had already measured 100% Human on call 3. Do not spend call 6 merely because an aggregate window later touched its opening.

Key lesson: a downstream assistant cleanup changed STI wording after the section had passed; restoring the higher-authority/known-passing wording was preferable to inventing another variant. Aggregate localization proved contextual rather than causal.

### `part1-conversation-flaws`

Used **3/6** section calls. Final 260-word context passed 100% Human/high confidence.

Winning move: delete the duplicate `spiritual depth doesn't tell me dependability` mini-argument, because the article had already made that point earlier through the meditation/relationship-conflict evidence. Also delete the `hold your horses / ask what flaws` instructional wrap-up. Let the personal `I've been through the wringer... Okay, thanks` line be the stopping point.

### `part1-slow-steady`

Used **1/6** section call. Final 224-word context passed 100% Human/high confidence.

Winning move: replace the balanced mini-essay `slow reveals X / cannot reveal sex / first sex isn't final` with the live uncertainty:

> I could know a woman for twenty years and still get into bed with her for the first time knowing almost nothing about how our bodies will relate. Polarity, touch, smell, desire levels, kinks, sexual openness—conversation only goes so far.

The following Bee story itself demonstrates that the first sexual experience is not the final ceiling, so no abstract recap is needed.

### Other repaired sections

- `part1-talk-before-sex`: reconstructed around Joel's father-derived `would we want to raise children together / are we ready?` thought instead of a generic sex-conversation curriculum.
- `part1-crucible`: localized repair preserved the coercion/safety exit and removed model-shaped explanatory/summary pressure.
- `part1-maturity-levels-cross-split`: repaired against the full natural section crossing the arbitrary half split; patient/caregiver material measured Human in context.

## Durable lessons

1. **Natural sections outrank detector windows for diagnosis.** Old 50–100 word windows often cut across the actual rhetorical unit.
2. **Detector localization is not causal localization.** A changed downstream sentence can make Pangram highlight an earlier span; compare exact draft identities before rewriting the red text.
3. **Rollback is a first-class repair operation.** Restore higher-authority / already-passing wording before generating another paraphrase.
4. **Transitions can be the classification unit.** Two individually sound sections can create an AI-shaped run where one ends with a generalized synthesis and the next starts with explanation.
5. **Delete duplicate miniature arguments.** If a point is already established elsewhere, do not preserve a second recap container and keep humanizing it.
6. **Let lived evidence perform the conclusion.** The Bee sexual-development story did the work of `the first night isn't necessarily the final ceiling`; the abstract sentence was aftercare.
7. **Do not chase monotonic aggregate scores.** r4 at 99.24% was numerically higher than r5/r6, but r7 reached 100% only after following architecture and local evidence rather than score hill-climbing.
8. **Use 200+ words for meaningful Romance diagnostics when possible.** Short residuals became interpretable only when widened into natural context.

See also:
- `PART1-RESULTS-AND-LESSONS-20260821.md`
- `PART1-NONLINEAR-ROLLBACK-LESSON-20260821.md`
- `project-sources/RHYTHM-AND-THOUGHT-SHAPE.md`

## Next safe action

Part 1 needs no further Pangram repair unless its exact text changes.

Continue recovery of the already-paid Part 2 aggregate r2; **do not resubmit it**. Once Part 2's exact status is resolved, perform the whole-candidate editorial/provenance/architecture closeout and deliberate owner reconciliation. PR #29 remains draft and must not be merged wholesale.
