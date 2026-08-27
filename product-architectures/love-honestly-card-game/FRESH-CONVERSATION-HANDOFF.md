# Love, Honestly v0.4.0 — Fresh Conversation Handoff

## Recover first

Use the verified Git bundle when available. Resolve `v0.4.0^{}` and confirm it equals `ffb7c1ef7dca4585944d1acf78802ce4107658d6` before changing product behavior. Preserve all earlier tags.

The final documentation/recovery bundle head is `1e5b0ef63177a9d411ce677990a2c2ee1494c111`.

Read in order:

1. `PRODUCT.md`
2. `DESIGN.md`
3. `surfaces/game.md`
4. `CURRENT-STATE.md`
5. `docs/GAME-FLOW.md`
6. `docs/CARD-FUNCTION-MATRIX-v0.4.0.md`
7. `docs/CARD-FUNCTION-MATRIX-v0.3.0.md`
8. `docs/ARTICLE-MAPPING.md`
9. `docs/RELEASE-NOTES-v0.4.0.md`
10. `RELEASE-MANIFEST-v0.4.0.md`

## Source boundary

The v0.4.0 reconciliation used the Romance Guide supplied on 2026-08-27:

`e51bae5277c2e0f86b75ff11a304a7d99a56e39d36203eeff7d6f9cc5c8391c7`

Do not infer a new deck function from an isolated paragraph. Reconstruct the guide's full argument and check the current card-function matrices first.

## Current product invariant

**Private answer formation → evidence basis → spoken primary and follow-up answers → two private judgments → overt ordinary-life experiment → scheduled reminder target → review whenever the pair chooses → private two-person revisit → comparison without scoring.**

## v0.4.0 decisions not to rediscover

- Most of the revised guide was already covered; do not inflate the deck paragraph-by-paragraph.
- The only new decision functions added in this pass are:
  - `spiritual-bypass-intimacy` — practice may reduce deprivation distress without resolving an intimacy need;
  - `spiritual-relationship-spirit` — stewardship of the relationship can mean repair, changed form, space, or ending, not forced permanence.
- `altered-03` follows the revised guide's narrower wording: first-time sexual-consent decisions should not be negotiated while high. Do not restore the older categorical `cannot negotiate consent` wording unless the guide changes again.
- Bundling is an imperfect historical illustration of the Missing Middle, not a recommended system.
- Higher female income or lower male income is not itself a polarity defect; decision rank, humiliation, uselessness, domination, or enforced shrinking is the operative problem.
- A romantic partner should not be the only source of beauty, softness, sensuality, inspiration, support, or purpose.
- Sobonfu Somé is a credited source for the spirit-of-relationship framing, not a co-author.
- Do not invent content from incomplete source fragments such as the current Helen Fisher brain-chemistry bullet.

## Preserved boundaries

- Answers are spoken aloud and never stored.
- Epistemic labels are metadata, not answers.
- No compatibility score.
- No secret tests.
- Anonymous safety stop remains anonymous.
- Storage schema stays v2 unless a real migration requires change.
- Scheduled review dates are reminder targets and `Review now` is available before, on, or after the date.
- Exact linked credit remains `Based on the U-Dont-Exist Romance Guide` → `https://romance.u-dont-exist.com`.
- No automatic external request.
- v0.1.0 Article Edition remains byte-preserved.

## Verification

Run:

```bash
npm run verify:release
git diff --check
```

The browser smoke must continue to test a future-dated plan returning to welcome and being reviewable immediately before the target date.
