# Fresh-conversation handoff: Love, Honestly v0.3.2

Continue from the verified v0.3.2 bundle rather than reconstructing the game from chat history.

## Authority

- Release: `v0.3.2`
- Release commit: `b76d18642df026c63fb75ccaa9d221d6b25cf165`
- Annotated tag object: `59397ba3fd20fe8fe354f7d23e676b0ce15670d5`
- Final bundle `main`: `22e306e9264f0957e69395dbb5e1d2a65561a2d8`
- Predecessor: `v0.3.1` / `1f023dd8a2f48b01e01c1f80b8fee9c047c7964c`
- Exact visible source line: `Based on the U-Dont-Exist Romance Guide`
- Exact href: `https://romance.u-dont-exist.com`

## Governing product loop

**Private answer formation → evidence basis → spoken primary and follow-up answers → two private judgments → overt ordinary-life experiment → scheduled reminder target → review whenever the pair chooses → private revisit → comparison without scoring.**

## v0.3.2 decision not to rediscover

A scheduled review date is **not an access lock**. It is a target date that brings the experiment back to attention.

Therefore:

- pending reviews appear on the welcome screen when the saved session is reopened;
- each shows `Scheduled for ...` plus relative timing;
- pending plans are surfaced chronologically;
- each always exposes `Review now` before, on, or after the target date;
- the Evidence map repeats the target date and reminder-not-lock boundary;
- do not add due-date enforcement unless the owner explicitly reverses this decision.

## Preserved boundaries

- Spoken answers are not stored.
- Epistemic labels are metadata, not answers.
- No compatibility score or secret tests.
- Anonymous safety stop remains anonymous.
- Storage schema remains v2 unless a real migration requires change.
- No automatic external request.
- v0.1.0 Article Edition remains byte-preserved.

## Recovery

1. Recover `Love-Honestly-Card-Game-v0.3.2.bundle`.
2. Verify against `Love-Honestly-v0.3.2-SHA256.txt`.
3. Confirm bundle `main` = `22e306e9264f0957e69395dbb5e1d2a65561a2d8` and `v0.3.2^{}` = `b76d18642df026c63fb75ccaa9d221d6b25cf165`.
4. Read product/design/surface/current-state/game-flow records before editing.
5. Run `npm run verify:release` and `git diff --check` after changes.

The browser regression must keep proving that a future-dated review can be opened immediately by choice.
