# CHAT-SURFACE-EXPERIMENT-009 — current Human Shaking anchor × residual social function

Task: `somatic-r15-clean-continuation-20260830`

Status: **FROZEN CHAT-AUTHORED DETECTOR EXPERIMENT / CODEX MECHANICAL EXECUTION ONLY**

## Decision basis

The completed Shaking guidance/social family established:

- current Shaking anchor C: Pangram 4.0 Human `1.0`;
- C + current two-sentence tail D: Human `0.77868855` / AI `0.2213114798`;
- C + prior direct full-function tail E: Human `0.8036776781` / AI `0.1963223368`.

The full tails are not production-compatible with the current anchor.

The current Human anchor already contains the substantive functions that those tails partly repeat:

- Louka got nothing from basic TRE and benefited from the class;
- the class contains many movements and positions;
- more angles may improve the chance of finding the stuck place;
- the practice is guided without being one fixed predictable TRE routine;
- it sits between fully standardized TRE and completely unstructured shaking.

The only clearly unique residual function in the rejected current tail is the social/observational point: the practice happens around other people rather than alone, and seeing others get results may help.

This experiment therefore keeps exact current Human anchor C unchanged and tests only that residual social function. It does not repeat the broader guidance/non-standardization/TRE-nonresponse explanation that C already performs.

Variant A uses the exact same-function source-native wording already present in the current candidate. Variant B uses one minimum direct realization. A is tested first. B is eligible only if A is not exact Human `1.0`.

## Worker role

Mechanical executor only.

Do not:

- generate, revise, normalize, select, apply, diagnose, or interpret prose;
- infer causality;
- recommend an edit;
- modify any article candidate or registered `master.html`;
- submit through the API;
- run a whole-document detector action;
- use `--force`;
- create another variant or detector family.

## Exact article authority

Repository: `u-dont-existDOTcom/joel-articles`

Branch: `task/somatic-r15-clean-continuation-20260830`

Current non-authoritative production candidate:
`articles/somatic-therapies/experiments/R15-EFT-REPAIR-CANDIDATE-20260831.md`

Expected candidate Git blob:
`6f9251f51d79a6b322b8c6f6cae95a9a5d80f760`

Expected candidate UTF-8 SHA-256:
`5a6226ca0056610b4492de7713a43bb152dde1079d81b5c05896c70fcf138679`

Registered `master.html` must remain unchanged at SHA-256:
`1e7e94717f40e7a4de77974a896f600a1bf2769d9c1846cbe84275e136ff5202`

## Known-Human control H0 — reuse only

Exact H0 is the prior current Shaking anchor C:

Path:
`tasks/somatic-r15-clean-continuation-20260830/surface-experiment-008/C-current-anchor.txt`

Source commit:
`6be6e6513326bb437faceeed2579a87c41ff1d83`

Git blob:
`2993757f24707297f1c8dd7b3fbf6c4e017e9e0b`

UTF-8 SHA-256:
`b36e1e46c06d764a080d407dce5412defe76ccb9202deb1a8a14e265acf40370`

Identity:
- 293 whitespace words;
- 1631 Unicode characters;
- 1641 UTF-8 bytes;
- no terminal newline.

Completed exact result authority:

Detector branch/head:
`u-dont-existDOTcom/pangram-humanization-lab@d809006f58e97b352b4d790e876d06f85cbf4f8e`

Result packet:
`state/experiments/somatic-r15-shaking-human-anchor-guidance-social-tail-20260831/RESULT-PACKET-GUI-CDE-RECOVERY-002.json`

Required H0 result:
- Pangram `4.0`;
- `STAGE_SUCCESS`;
- Human `1.0`;
- AI `0.0`;
- AI-assisted `0.0`;
- exact UTF-8 History binding.

Do not resubmit H0.

## Variant A — source-native residual social tail

Path:
`tasks/somatic-r15-clean-continuation-20260830/surface-experiment-009/A-current-anchor-source-social-tail.txt`

Git blob:
`b3f255fa5481ac79eae81b9444879ac1a4398944`

UTF-8 SHA-256:
`03037241afe8827df5b1ca2b81bc877704d5e198229a9759237b76245807ecd1`

Identity:
- 315 whitespace words;
- 1758 Unicode characters;
- 1768 UTF-8 bytes;
- no terminal newline.

Exact appended tail:

`It is social too. Many people do better when they see other people getting results instead of doing the whole practice alone.`

Tail SHA-256:
`6667faded75427a60fd82b7eadeb834966074f7b45712a10e5aec380b3c6f4ec`

## Variant B — minimum direct residual social tail

Path:
`tasks/somatic-r15-clean-continuation-20260830/surface-experiment-009/B-current-anchor-minimal-social-tail.txt`

Git blob:
`854bee133e39537276e77ecddea32d09f37fdd7d`

UTF-8 SHA-256:
`fa8625ab5686641eb2c1e15b7799992a43023fe2814a68737df88f17091542b5`

Identity:
- 310 whitespace words;
- 1731 Unicode characters;
- 1741 UTF-8 bytes;
- no terminal newline.

Exact appended tail:

`You're also doing it with other people instead of alone. Seeing other people get results may help.`

Tail SHA-256:
`9f4493273464986150565d6405eadfcf6a132229d3fcaf8ae86191d55c34db44`

## Mechanical identity and preservation assertions

Before any detector action:

1. Verify the production candidate identity and registered-master identity.
2. Verify H0, A, and B exact blobs, SHA-256 values, counts, and terminal-newline state.
3. Verify A begins with exact H0 bytes and differs only by `\n\n` plus the exact A tail.
4. Verify B begins with exact H0 bytes and differs only by `\n\n` plus the exact B tail.
5. Verify A and B preserve the residual functions:
   - practice occurs with/around other people rather than alone;
   - seeing other people get results may help.
6. Verify H0 already preserves the non-residual functions:
   - Louka's standard-TRE nonresponse and class benefit;
   - multiple movements/positions and more ways/angles in;
   - guided but not fully standardized;
   - middle ground between predictable TRE and unstructured shaking.
7. Verify article mutations `0` and registered-master mutations `0`.
8. Fail closed on any mismatch.

## Detector state and transport

Detector repository:
`u-dont-existDOTcom/pangram-humanization-lab`

Detector branch:
`task/somatic-r15-exact-recovery-20260830`

Expected starting head:
`d809006f58e97b352b4d790e876d06f85cbf4f8e`

Stable family:
`somatic-r15-shaking-current-anchor-residual-social-tail-20260831`

Transport:
authenticated local Pangram GUI through deterministic `pangram-local` Playwright/Brave runner.

API actions authorized: `0`.

Whole-document GUI actions authorized: `0`.

New short-document GUI clicks authorized: `0..2`.

## Serial decision rule

### Step A

For exact A:

1. verify exact cache, reservations, checkpoints, and authenticated History;
2. persist `EXACT_GUI_RESULT_EXISTS`, `EXACT_GUI_ACTION_AMBIGUOUS`, or `EXACT_GUI_NEVER_SUBMITTED`;
3. recover an existing result if present;
4. only if never submitted, push a durable pre-click reservation and click exactly once;
5. require exact History binding, Pangram `4.0`, and `STAGE_SUCCESS`;
6. persist the complete result.

If A is exactly:

- Human `1.0`;
- AI `0.0`;
- AI-assisted `0.0`;

then stop. Do not submit B.

If A completes but is not exact Human `1.0`, proceed to B.

If A becomes ambiguous, stop before B.

### Step B — conditional

For exact B, only after a completed non-Human-1.0 A:

1. verify exact cache, reservations, checkpoints, and authenticated History;
2. persist the pre-action classification;
3. recover an existing result if present;
4. only if never submitted, push a durable pre-click reservation and click exactly once;
5. require exact History binding, Pangram `4.0`, and `STAGE_SUCCESS`;
6. persist the complete result;
7. stop.

Never repeat an ambiguous action. Never use `--force`.

## Durable output

Write under:
`state/experiments/somatic-r15-shaking-current-anchor-residual-social-tail-20260831/`

Required packet:
`RESULT-PACKET.json`

Include:

- exact detector heads before/after;
- H0 reuse identity/result;
- exact A classification/result;
- exact B classification/result if conditionally executed;
- Human/AI/AI-assisted fractions;
- prediction/headline/confidence;
- all returned windows and offsets;
- exact History/input binding;
- H0→A and, if available, H0→B and A→B deltas;
- cache/reservation/recovery/click accounting;
- `new_api_calls: 0`;
- `new_short_gui_clicks: 0..2`;
- `whole_document_calls: 0`;
- `force_overrides: 0`;
- `article_mutations: 0`;
- `registered_master_mutations: 0`;
- exact family state.

Carry forward:

- `FULL_HISTORY_FIX: PASS`;
- `REMAINING_VALIDATOR_FINDINGS: PRE_EXISTING_UNRELATED_MERGE_DEBT`;
- `MERGE_BLOCKED_UNTIL_RECONCILED: YES`.

## Stop boundary

After A passes exact Human `1.0`, or after B completes/ambiguously stops:

- do not apply A or B to the article;
- do not generate another variant;
- do not open another detector family;
- do not run the final whole-document call;
- do not interpret results;
- return only the mechanical packet;
- stop.

Chat owns interpretation and any production-application directive.