# Love, Honestly Card Game — Current State

Updated: 2026-08-17

## Repository status

Durable private architecture/recovery snapshot: `artifact/love-honestly-card-game-v0.3.2`. The verified Git bundle remains the complete source-history carrier.

## Exact release boundary

- Product version: `0.3.2`
- Release tag: `v0.3.2`
- Release commit: `b76d18642df026c63fb75ccaa9d221d6b25cf165`
- Annotated tag object: `59397ba3fd20fe8fe354f7d23e676b0ce15670d5`
- Final bundle head: `22e306e9264f0957e69395dbb5e1d2a65561a2d8`
- Predecessor: `v0.3.1` / `1f023dd8a2f48b01e01c1f80b8fee9c047c7964c`

## Product invariant

**Private answer formation → evidence basis → spoken primary/follow-up answers → two private judgments → overt ordinary-life experiment → scheduled reminder target → review whenever the pair chooses → private revisit → comparison without scoring.**

A scheduled date is a reminder target, never an access lock.

## v0.3.2 correction

- Pending reviews surface on the welcome screen when a saved session is reopened.
- Each shows `Scheduled for ...` plus upcoming/due/overdue timing.
- Each exposes `Review now` before, on, or after its target date.
- The Evidence map repeats the scheduled date and the same anytime-review rule.
- Copied Evidence-map text retains the date.
- Pending plans are surfaced chronologically.

## Preserved boundaries

- Actual answers are spoken and never stored.
- Epistemic labels are metadata, not answers.
- Storage schema remains v2 and card IDs remain stable.
- No compatibility score, secret tests, or due-date enforcement.
- Anonymous safety exits remain anonymous.
- Exact guide credit remains `Based on the U-Dont-Exist Romance Guide` → `https://romance.u-dont-exist.com`.
- No automatic external request.

## Verification

`npm run verify:release` passed 34/34 Node tests, standalone build verification, a future-dated review returning to welcome, exact scheduled-date notice, early `Review now`, normal/legacy/safety/storage/revisit flows, no-network monitoring, and screenshot capture. ZIP and Git-bundle verification passed; the bundle contains tags `v0.1.0` through `v0.3.2`.

## Final source-carrier checksums

- HTML: `2bcb59988438256330e7744d5d7027d40bda18dc372d06d94d51c854d9b03ef3`
- ZIP: `db0293196f66deedcccbaefd665d13322a1b142e76fb1fbb538102c59c233400`
- bundle: `b219e0fdfcda5a2722057d7ccc247f82a917b944350081b64510049899c4ba99`
- scheduled-review screenshot: `2c732aa440c1132ec981df314c79debee32f38d4bc430e1398ce2375e11bd276`

## Recovery

Recover `Love-Honestly-Card-Game-v0.3.2.bundle`, verify against `Love-Honestly-v0.3.2-SHA256.txt`, confirm `main` = `22e306e9264f0957e69395dbb5e1d2a65561a2d8` and `v0.3.2^{}` = `b76d18642df026c63fb75ccaa9d221d6b25cf165`, then read the product/design/surface/current-state/game-flow/handoff files before editing. Do not add due-date enforcement unless the owner explicitly reverses this decision.
