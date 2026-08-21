# Romance Part 1 — current repair checkpoint — 2026-08-21

Status: **task candidate / detector repair in progress. Canonical `main` unchanged.**

## Current exact candidate

Directory:
`work/romance-detector-repair-20260820/materialized-part1-repair-r5/`

- master SHA-256: `d205393b1724256416291050fdeb41c18afb9669fddc45cf713559e9ecd9e406`
- master words: 19,764
- Part 1 SHA-256: `e6b9e546bb2f07af8e18fc65fb6883d27bf0106d93f5f02d6674a88e034d572d`
- Part 1 words: 9,910
- Part 2 unchanged SHA-256: `20301b1bfb0052de694657411f231f82d9a45ae62ff9c4839015befce5c57dc2`
- Part 2 words: 9,703
- invariant audit: PASS (headings, native markers, Markdown link destinations, protected anchors, required repair anchors).

## Aggregate Part 1 progression

Registered baseline:
- Human `0.9205247164`
- 10,236 words.

Current repair aggregates:
- r2: Human `0.9847978949546814`
- r3: Human `0.980210542678833`
- r4: Human `0.992400050163269`, AI `0.007599963806569576`
- r5: Human `0.9838229417800903`, AI `0.01617708057165146`, assisted `0.0`.

r4 had two short AI windows at the Casual Sex opening. The complete Casual natural section had already measured 100% Human on local call 3. r5 therefore restored the registered STI/attachment realization from that exact known-passing Casual section rather than spending Casual call 6.

The r5 aggregate residual became one 156-word AI window crossing the **end of `Affection and the simmer` into the opening of `Can Casual Sex or a Situationship Actually Be Honest?`**. This is evidence of a cross-section interaction, not proof that the Casual opening itself needs another rewrite.

## Current local section state

- `part1-talk-before-sex`: repaired from 0% Human by reconstructing around Joel's father-derived `would we want to raise children together / are we ready?` question; no current aggregate residual there.
- `part1-affection-simmer`: **5/6 completed before current r6 request**; earlier versions remained AI-shaped as standalone instructional/balanced frameworks.
- `part1-casual-sex-situationship`: **5/6**; complete r3 natural section was 100% Human; call 6 remains unused.
- `part1-crucible`: 4/6; full-section repair cleared aggregate residual while preserving coercion/safety function.
- `part1-maturity-levels-cross-split`: locally repaired; patient/caregiver boundary measured 100% Human and no current aggregate residual remains.

## Current in-flight action

Final Affection section call:

- experiment: `romance-detector-repair-20260820-part1-affection-transition-r6-20260821`
- section id: `part1-affection-simmer`
- budget scope: `section`
- boundary: 274 contiguous words, including the shortened Affection section plus unchanged Casual opening context
- spec SHA-256: `e4f5d231cfb85d002d0ce9537ce0a831147dc20d67c8dc74f06a7f733ea34c9b`
- private request commit: `4e8a457e947fc74fe083c8fdf9f59f4bee9ff7c1`
- after this request, Affection is **6/6**. Do not submit a seventh Affection call.

Candidate Affection realization under test:

> Doug Toft, who has been married for fifty years, has a useful list called 50 Things I Learned from 50 Years of Marriage. One of his points is to touch his wife without an agenda. A hug, cuddle, kiss, or back rub should sometimes be allowed to end right there. If every affectionate touch becomes a bid for sex, affection itself can start feeling like pressure.
>
> Kim Anami calls the sexual current between encounters “the simmer.” If we supposedly want each other but only show it when somebody officially initiates sex, I think something is already going wrong.

The old trailing `sex is a barometer... / don't make her manufacture desire` explanatory wrap-up is removed in this candidate. The purpose is to stop the Affection thought where its two actual source-derived observations end instead of adding a generalized synthesis immediately before another explanatory section opening.

## Recovery rule

1. Recover `state/experiments/romance-detector-repair-20260820-part1-affection-transition-r6-20260821-results.json`; do not repeat the request.
2. If r6 passes, materialize only the Affection change against exact Part 1 r5, run repository/architecture gates, then do one exact aggregate Part 1 measurement.
3. If r6 fails, Affection is capped at 6/6. Do not paraphrase it again or reset its identity. Preserve the best editorial realization and request narrow owner help only if the aggregate cannot be completed without further Affection changes.
4. Casual still has one section call available, but do not spend it merely because the aggregate window contains Casual; its full natural section already has a 100% Human measurement.
5. All article-authority changes remain task-branch candidates until deliberate owner acceptance/reconciliation.

## Active lessons

See:
- `PART1-RESULTS-AND-LESSONS-20260821.md`
- `PART1-NONLINEAR-ROLLBACK-LESSON-20260821.md`
- `project-sources/RHYTHM-AND-THOUGHT-SHAPE.md`
