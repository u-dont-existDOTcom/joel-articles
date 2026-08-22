# Romance owner-integrated aggregate Part-2 Pangram result — 2026-08-21

Status: measured aggregate evidence; candidate still not canonical owner-final article.

## Exact boundary

- source: `work/romance-detector-repair-20260820/materialized-owner-integrated/candidate-part-2.txt`
- SHA-256: `9dc539ca99f8c747ecd5a551f2c72ad476c87671919863d2ad469acf6c6e696f`
- whitespace words: 9,804
- detector: Pangram 4.0
- stage: `STAGE_SUCCESS`
- prediction: Human / Mostly Human Written
- Human: `0.9761735796928406`
- AI: `0.02382640726864338`
- AI-assisted: `0.0`
- AI segments: 3
- Human segments: 4

This improves on pass 6 Human `0.9322237372398376` by about 4.395 percentage points.

## Correct accounting scope

This was submitted with `budget_scope: aggregate`. It is the seventh historical paid Part-2 aggregate measurement, but Part 2 is a multi-section article half, so the six-call **section** cap does not apply. The call ledger correctly reports `hard_cap_applies: false` and `cap: null` while preserving all seven paid aggregate measurements.

## Exact residual AI windows

1. High confidence, 153 words, `Not A Performance`: starts at `Toft’s advice after fifty years is simple...` and runs through `When a strong woman surrenders, she is choosing to.`
2. High confidence, 33 words, `Two Pillars Don't Hold The Roof Up`: `By then, the outside support isn’t really shared support anymore. There's a practical side too...` through the no-backup sentence.
3. High confidence, 39 words, `Psychedelics in relationship discernment`: `You may feel that this person understands you more deeply than anyone ever has...` through the sober/irritated/jealous/broke/bored/difficult-decision question.

## Next action

Residual repair r1 rewrites these three thought movements and is materialized under `materialized-owner-integrated-r1/`. Before another aggregate Part-2 measurement, test the three corresponding **natural sections** with 200+ contiguous reader-visible words. Each natural section has its own 0/6 local section budget. Do not treat the 33- or 39-word Pangram windows as reliable standalone certification boundaries.
