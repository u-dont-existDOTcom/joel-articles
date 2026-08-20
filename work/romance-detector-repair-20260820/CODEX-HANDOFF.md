# Codex handoff — Romance detector repair

Updated: 2026-08-20

## Owner instruction

Continue the Romance Pangram-repair workflow autonomously. Do not stop after each detector pass to ask whether to continue. Human/editorial quality and owner fidelity outrank Pangram. Do not merge canonical `main` until the candidate is editorially accepted and the authority package is deliberately reconciled.

## Mandatory recovery order

Fresh-read `u-dont-existDOTcom/joel-articles` first:

1. `SKILL.md`
2. `CANONICAL-REPO-MAP.md`
3. `AGENTS.md`
4. `docs/INDEX.md`
5. `state/CODEX-CURRENT-STATE.md`
6. `articles/INDEX.json`
7. `articles/romance/CURRENT-STATE.md`
8. `articles/romance/OWNER-LOCKS.json`
9. `articles/romance/ARCHITECTURE.md`
10. task files under `work/romance-detector-repair-20260820/`

For detector work also fresh-read `u-dont-existDOTcom/pangram-humanization-lab`:

1. `README.md`
2. `state/CURRENT-STATE.md`
3. `state/LESSON-INDEX.md`
4. current `state/WORKING-LESSONS*.md` in index order
5. `docs/CHATGPT-OPERATING-GUIDE.md`
6. `docs/PANGRAM-LOCAL-PLAYWRIGHT.md`
7. issue #110

GitHub is canonical. Current owner instruction outranks repo text and must then be persisted back to GitHub.

## Canonical article boundary

`main:articles/romance/master.md` remains unchanged canonical authority.

Registered Part 1 detector boundary:
- SHA-256 `ae88df0f4156537239cb984337196703b88629c3588a5e58ee50c0888d3b39f8`
- 10,236 words
- Pangram 4 Human `0.9205247164`
- do not submit Part 1 again; pass-1's sole Part-1 edit was reverted exactly.

## Part 2 measured progression

Baseline registered Part 2:
- SHA `2df878093bc05fefa98ca30e9a97bdd52e212370f432bf0408e90f1b60c54bb0`
- Human `0.8983033895`

Pass 1:
- SHA `30f61fb0c490ec1275f3c39c834a38a956041865b63e5592c270d51cc22d5498`
- Human `0.9137498736`
- transport local Playwright

Pass 2:
- SHA `679daa77fb92ea71bb85716e6ece671e093b49412b149e2f5129079a204d24d2`
- Human `0.9114283323287964`
- AI `0.08857167512178421`
- 5 AI segments
- transport API

Pass 3 current candidate:
- source: `work/romance-detector-repair-20260820/materialized-pass3/`
- Part 2 SHA `c6ef42419a3db2e82b1ff4f9370fc85bca4fa8c061c61dd6a1b5d28171d9908c`
- 10,043 words
- Human `0.9153165817`
- AI `0.0846834108`
- AI-assisted `0.0`
- Pangram 4.0 / `STAGE_SUCCESS`
- exact stored-text match `exact_utf8`
- transport local Playwright
- evidence branch `u-dont-existDOTcom/pangram-humanization-lab:evidence/romance-pass3-gui-20260820`
- result path `state/gui-runs/pangram-4/c6ef42419a3db2e82b1ff4f9370fc85bca4fa8c061c61dd6a1b5d28171d9908c/result.json`

The attempted pass-3 API route returned HTTP 402 `Insufficient credits` before task creation. It had no task ID, was non-ambiguous, and is not counted as a paid measurement. Cross-transport evidence is durable on the pass-3 GUI evidence branch.

Part-2 paid measurement count in the current audit: **3 of maximum 6**.

## Pass-3 editorial changes

Pass 3 preserved Part 1 byte-for-byte and changed only Part 2.

Queen of Orgasms:
- removed generic `Many people are not even aware...` setup;
- collapsed the cervical/whole-body orgasm taxonomy into one spoken thought;
- removed `That laboratory evidence establishes the uniqueness of the phenomenon.` as explanatory aftercare;
- preserved the lived cervical-sex claim, `life/work` joke, Komisaruk/Whipple laboratory claim, and Anami/Richardson practitioner claims.

Two Pillars/community:
- corrected the section toward its unique job: shared people who know both members and can reality-check the relationship;
- removed duplication of the earlier `Don’t make your partner your whole world` burden argument;
- preserved practical-resilience content and the strong/weak-couple caveat;
- preserved the personal Bee/community evidence.

Post-edit invariant audits passed: headings, native markers, Markdown link destinations, protected anchors, actors, chronology, source attribution.

## Important corrected localization finding

The earlier assessment incorrectly mapped historical red windows 17/19/21 to `After leaving`. Exact historical offset/source review showed those windows were in Twin Flames -> `Two Pillars Don't Hold The Roof Up` / community.

This correction is durable in `PASS-3-STATE.md` and PR #29.

## Current blocker: read-only localization bug

Do **not** buy call #4 until current pass-3 windows are localized from the already-paid History record if practicable.

`run_pass3_localize.sh` performed no detector submission but failed at `bind_exact_history_record`:
- `detector_submission_attempted: false`
- `direct_report_requested: true`
- `exact_history_record_found: false`
- `history_list_candidate_count: 10`
- failure path on evidence branch: `state/gui-runs/pangram-4/c6ef42419a3db2e82b1ff4f9370fc85bca4fa8c061c61dd6a1b5d28171d9908c/localization-failure.json`

This matches known issue #110: direct-report localization can miss the record response listener even when the immediately preceding detector run successfully exact-bound the same History report.

## Best next tooling repair

Fix the localizer rather than making Joel manually shuttle another command.

Likely robust route:
- for a known `https://www.pangram.com/history/<uuid>` report URL, derive the corresponding `https://web.pangram.com/api/history/<uuid>/` route;
- use Playwright `BrowserContext.request` (authenticated context shares cookies) to GET that API record directly, read-only;
- pass the JSON payload plus API URL through the existing `match_exact_history_record(...)` exact-text identity gate in `history_api_record.py`;
- only if exact source SHA/word-count binding succeeds, feed that `ExactHistoryRecord` to `localize_history_record(...)`;
- preserve the privacy contract: do not commit UUID/report URL/raw submitted text/cookies/headers;
- add deterministic unit tests for direct authenticated API lookup and fail-closed mismatch;
- no detector-submit code in this path.

Do not debug issue #110 with paid Pangram calls.

## After localization succeeds

1. Read exact pass-3 AI-labeled windows/spans from the already-paid record.
2. Map each window against the pass-3 Part-2 source.
3. Run semantic sanity + heading promise + curious-reader + article-wide duplication/protected-function audit before drafting.
4. Build pass 4 with minimum edit dose against only current residual failures.
5. Run two cold audits.
6. Materialize and Git-persist candidate before detector work.
7. If a new measurement is warranted, use local GUI while API credits remain exhausted. This would be paid Part-2 measurement #4 of max 6.
8. If ambiguous, recover first; never auto-repeat.
9. Persist detector evidence in pangram-humanization-lab and editorial decisions/task state in joel-articles.

## Do not merge yet

PR #29 is a task/experiment branch with tooling, state, and generated artifacts. Do not merge it wholesale into `main` as canonical article authority. After the detector/editorial loop ends, create a clean owner-final content reconciliation deliberately.
