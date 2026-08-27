# Love, Honestly v0.5.0 — Fresh Conversation Handoff

Continue from the verified v0.5.0 bundle rather than reconstructing the game from chat history.

## Authority

- Product: **Love, Honestly**
- Release: `v0.5.0`
- Verified application release commit: `400f64f0c8acc815bd9b12a075ab324de76d4cff`
- Annotated tag object: `6807866e938582a7588e05e9bee021d9a1959dc8`
- Final documentation/recovery bundle head: `46f7e616779377d49e2b3d5d8df1786b0ab38d25`
- Immediate predecessor: `v0.4.0` at `ffb7c1ef7dca4585944d1acf78802ce4107658d6`
- Primary product source: U-Dont-Exist Romance Guide
- Current guide file SHA-256: `e51bae5277c2e0f86b75ff11a304a7d99a56e39d36203eeff7d6f9cc5c8391c7`
- Additional source: owner-supplied Long distance section from 2026-08-27
- Exact visible source line: `Based on the U-Dont-Exist Romance Guide`
- Exact href: `https://romance.u-dont-exist.com`

## Recovery order

1. Recover complete source from `Love-Honestly-Card-Game-v0.5.0.bundle`.
2. Verify every artifact against `Love-Honestly-v0.5.0-SHA256.txt`.
3. Clone the bundle and confirm `main` resolves to `46f7e616779377d49e2b3d5d8df1786b0ab38d25` and `v0.5.0^{}` resolves to `400f64f0c8acc815bd9b12a075ab324de76d4cff`.
4. Read `PRODUCT.md`, `DESIGN.md`, `surfaces/game.md`, `CURRENT-STATE.md`, and `README.md`.
5. Read `docs/GAME-FLOW.md`, `docs/CARD-FUNCTION-MATRIX-v0.5.0.md`, `docs/ARTICLE-MAPPING.md`, and `DECISION-LOG.md`.
6. Read the v0.5.0 release notes and release manifest.
7. Create an isolated branch before changing behavior.

## Governing product loop

**Private answer → evidence basis → spoken answer + mirror → private judgments → overt ordinary-life experiment → scheduled reminder target → Review now whenever desired → private revisit.**

## v0.5.0 decisions not to rediscover

The owner reviewed the existing v0.4.0 deck and said the cards were fine. Preserve them unless the owner explicitly changes one.

New functions intentionally added:

- `community-06` — whether the pair wants intentional-community/commune living and what values/environment fit.
- `community-07` — when to explore communities together, what prior visits taught, and which candidate to visit next.
- `life-design-long-distance-01` — whether distance is wanted/tolerated and for how long.
- `life-design-long-distance-02` — how jobs/opportunities compete with physical togetherness and what closes the distance.
- `ordinary-long-distance-evidence` — what remote contact cannot establish about ordinary in-person life.
- `spiritual-twin-flame-model` — one destined person vs repeatable sacred/archetypal connection vs another meaning/non-belief, and the practical expectations each model creates.
- revised `sex-03` — making love vs sex, preferred modes/depth, and eventual cervical-sex interest.

All seven apply to new and existing relationships: `discover`, `build`, `repair`, and `full`.

The source-wide recheck found no other missing card that justified duplicating an accepted function or turning article evidence, history, or memoir into a play card. The complete disposition is in `CARD-FUNCTION-MATRIX-v0.5.0.md`.

## Preservation locks

- Actual answers are spoken and never stored.
- Epistemic labels are metadata, not answers.
- No text answer field.
- Two private classifications remain separate.
- Reality steps are overt; no secret tests.
- Scheduled dates are reminder targets; Review now is always available.
- Schema v2 and every earlier card ID remain stable.
- Optional Polarity, Altered States, and Spiritual Practice remain off by default.
- The Twin Flame card remains in optional Spiritual Practice because the guide marks that material as skippable when irrelevant.
- Cervical-sex interest is a conversation question, not an obligation or sexual performance test.
- Intentional-community cards ask about community as a way of life, not merely a support network.
- Long-distance cards ask preference, duration, closure plan, and the in-person evidence gap without diagnosing every distant couple as intimacy-avoidant.
- No compatibility score or automatic external request.

## Verification

Run:

```bash
npm run verify:release
git diff --check
```

The release tag passed 46 Node tests and the complete browser suite before tagging.
