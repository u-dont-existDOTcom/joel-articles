# CHAT-SURFACE-EXPERIMENT-007 — Human housemate anchor × hour-later tail production test

Task: `somatic-r15-clean-continuation-20260830`

Status: **FROZEN CHAT-AUTHORED DETECTOR EXPERIMENT / CODEX EXECUTION ONLY**

## Decision basis

The EFT family produced the first exact production repair: a Human anchor plus the original polished tail was Pangram AI `1.0`, while the same anchor plus a direct three-sentence tail was Human `1.0`. The EFT repair has now been applied mechanically to a new non-authoritative candidate.

This experiment tests the next sharp Human→AI boundary in exact R15:

- GUI window 7, the outcome definition and housemate Brainspotting experiment, was `Human / High` and has already been independently confirmed by the short API as Human `1.0`;
- the immediately following GUI window 8 was `AI-Generated / High`;
- the first paragraph of that AI window performs the hour-later durability distinction.

The experiment asks whether replacing only that first post-anchor paragraph with one direct realization preserves every idea while flipping the exact boundary, and whether the same operation remains valid with the current candidate's attribution-correct housemate anchor.

## Worker role

Mechanical executor only.

Do not:

- generate, revise, normalize, select, or apply prose;
- diagnose or interpret detector results;
- infer causality;
- recommend an edit;
- modify the article candidate or registered `master.html`;
- submit any GUI or whole-document action.

## Exact article/source authority

Article repository: `u-dont-existDOTcom/joel-articles`

Article branch: `task/somatic-r15-clean-continuation-20260830`

Required live packet/input head: the commit containing this packet, to be supplied in the external execution directive.

Current production candidate:
`articles/somatic-therapies/experiments/R15-EFT-REPAIR-CANDIDATE-20260831.md`

Expected current production-candidate Git blob:
`6f9251f51d79a6b322b8c6f6cae95a9a5d80f760`

Expected current production-candidate UTF-8 SHA-256:
`5a6226ca0056610b4492de7713a43bb152dde1079d81b5c05896c70fcf138679`

Exact R15 reader-visible source:
`articles/somatic-therapies/experiments/R15-WHOLE-ARTICLE-PANGRAM-BOUNDARY-20260830.txt`

Expected R15 source Git blob:
`542012646469032eb836865b0e89b8fa368a1d0b`

Expected R15 source UTF-8 SHA-256:
`9a81bd04252a2ee851dd111040c600837bdf0a7bbf71c42c293e3b763c99a707`

GUI localization authority:
`u-dont-existDOTcom/pangram-humanization-lab@0588d51d15dc4087c72adc4c35fd78d6be826887`

Prior exact API confirmation for the R15 Human anchor:

- detector path: `state/experiments/somatic-r15-api-gui-human-window-calibration-20260831/RESULT-PACKET.json`;
- variant: `H2`;
- input SHA-256: `1d7bb2473eea7c4c42229726aaeb953fc5fb6f30c1cfc316f2673e90be56f3aa`;
- Pangram 4.0 Human `1.0` / AI `0.0` / High;
- task id: `6f8d20fe-4470-48ef-9867-7554f17f384f`.

## Frozen input directory

`tasks/somatic-r15-clean-continuation-20260830/surface-experiment-007/`

### H0 — exact R15 GUI/API-Human anchor

Path: `H0-r15-human-anchor.txt`

Git blob: `d3846d9c0747f540a66fbe63208d7ecbb984d48c`

UTF-8 SHA-256: `1d7bb2473eea7c4c42229726aaeb953fc5fb6f30c1cfc316f2673e90be56f3aa`

Whitespace words: `214`

Unicode characters: `1192`

UTF-8 bytes: `1196`

Terminal newline: `false`

H0 must be byte-identical to R15 source Unicode slice `17379:18571` and to the previously completed H2 API input. Reuse its exact completed Human `1.0` result. Do not resubmit H0.

### A — R15 Human anchor + original R15 hour-later tail

Path: `A-r15-anchor-original-tail.txt`

Git blob: `13f043d23e44d3655437293a8bf8ea0d6f581189`

UTF-8 SHA-256: `574a317204c05ac0e05a0d924db4a5dcb66f6dafcbfd27b1da8f16783e001d94`

Whitespace words: `291`

Unicode characters: `1591`

UTF-8 bytes: `1595`

Terminal newline: `false`

A must equal exact R15 source Unicode slice `17379:18970`.

Original tail alone SHA-256: `8c3a231b8189d760297ea4a8e241a637e6fd2ea0beb01adcd41d72f1a238832b`.

### B — R15 Human anchor + direct hour-later tail

Path: `B-r15-anchor-direct-tail.txt`

Git blob: `a0202b4a631feb92f03898a2977f5cd5a5e0a9a9`

UTF-8 SHA-256: `9796246dad4b35cb761939724a57e6bbb4b3a4d46119968741144401edae1e11`

Whitespace words: `273`

Unicode characters: `1496`

UTF-8 bytes: `1500`

Terminal newline: `false`

### C — current candidate housemate anchor only

Path: `C-current-anchor.txt`

Git blob: `6850cd60a4a9d6d3a97994292dcfb0c8f1ef53c7`

UTF-8 SHA-256: `dddae7f8802de8c38cc6df7ba03ab87fc12b9493736160f278f684ae26be2e4d`

Whitespace words: `223`

Unicode characters: `1257`

UTF-8 bytes: `1257`

Terminal newline: `false`

C must equal the current production candidate's reader-visible material beginning with the two linefeeds immediately before `How I Know Whether It Actually Helped` and ending with `That only tells me what happened right then.`

### D — current candidate housemate anchor + current hour-later tail

Path: `D-current-anchor-current-tail.txt`

Git blob: `8c76f61ac91354889c8184d207a15abcb578e2c9`

UTF-8 SHA-256: `29d4af12b023c3a71ba2d16583b101e3ffe2f042652b36c4e57dce42e7d16abc`

Whitespace words: `292`

Unicode characters: `1637`

UTF-8 bytes: `1637`

Terminal newline: `false`

D must equal C plus the exact current production-candidate paragraph beginning `The important version of me is the one an hour later` and ending `one EMDR session is often not enough either.`

Current tail alone SHA-256: `983402687ae007fd83e6aa1343a5369825513b751ae4da80276ade789791eda8`.

### E — current candidate housemate anchor + direct hour-later tail

Path: `E-current-anchor-direct-tail.txt`

Git blob: `945b17ef01eceaf1ee8fd3586f703a2bda06279b`

UTF-8 SHA-256: `13a08874c69e675d432c2e14a59aeab81933b6a2d5c31d9e736c402a71d3ded9`

Whitespace words: `282`

Unicode characters: `1561`

UTF-8 bytes: `1561`

Terminal newline: `false`

## Exact direct tail

The direct tail used in B and E is exactly:

`I check again an hour later. If I'm still stewing just as hard, it probably didn't last, and I may need to work with it again. If I can remember the event and it doesn't grab me as hard, now that's interesting. I don't expect one pass to erase every trigger; EMDR often takes more than one session too.`

Direct tail alone SHA-256: `d351ef58bd06ea4f6e2853f697d662d644b59e1e286884f1b10f82f47c608929`.

## Mechanical identity assertions

1. Verify every file's Git blob, SHA-256, word count, Unicode-character count, UTF-8 byte count, and terminal-newline state.
2. Verify H0 equals exact R15 source slice `17379:18571` and the previously completed H2 input.
3. Verify A equals exact R15 source slice `17379:18970`.
4. Verify A and B begin with exact H0 bytes.
5. Verify C is the exact reader-visible current-candidate anchor described above.
6. Verify D and E begin with exact C bytes.
7. Verify B and E use byte-identical direct-tail bytes after the paragraph separator.
8. Verify A differs from B only in the complete post-anchor tail.
9. Verify D differs from E only in the complete post-anchor tail.
10. Verify article candidate mutations `0` and registered-master mutations `0`.
11. Fail closed on any mismatch.

## Mechanical preservation assertions for the direct tail

The direct tail must preserve all functions of both the R15 and current hour-later paragraphs:

- the result must be checked again approximately one hour later;
- still stewing just as hard means the immediate shift probably did not last;
- another attempt or further work may be needed;
- remembering the event without it grabbing/restimulating the author as hard is the meaningful improvement;
- one pass/treatment is not expected to erase every trigger/everything;
- EMDR often takes more than one session.

Preservation assertion must be `PASS` before B or E is submitted.

## Detector family and accounting

Stable family:
`somatic-r15-housemate-human-anchor-hour-later-tail-20260831`

Detector evidence repository:
`u-dont-existDOTcom/pangram-humanization-lab`

Detector branch:
`task/somatic-r15-exact-recovery-20260830`

Expected detector starting head:
`ede777c4455d699f64f46e7850e92c707fa31378`

If the branch has advanced only through already-returned evidence and contains no conflicting work, continue from its current tip and record the exact start head. Do not reset or discard evidence.

H0 exact completed result is reused and counts as the calibration/control result.

Maximum new paid detector actions in this packet: **5 short-section API calls total** for A, B, C, D, and E.

Stable-family cap: `6` result slots including reused H0.

Whole-document GUI calls authorized: `0`.

GUI actions of any kind authorized: `0`.

## Detector execution

For A, B, C, D, and E separately:

1. check exact Pangram-4 cache, task, checkpoint, reservation, and ambiguity state;
2. reuse an exact completed result if present;
3. otherwise submit exact committed bytes once through the approved short-document API route;
4. explicitly request `pangram-4`;
5. persist task identity before polling;
6. require terminal version `4.0` and `STAGE_SUCCESS`;
7. record exact Human, AI, and AI-assisted fractions, prediction/headline, confidence, every returned window, `ai_assistance_score`, and `humanizer_score` where present;
8. do not repeat after ambiguous work.

## Required output

Write under:
`state/experiments/somatic-r15-housemate-human-anchor-hour-later-tail-20260831/`

Required:

- exact copied input files;
- task/checkpoint/cache evidence;
- `RESULT-PACKET.json` with all exact identities and results;
- raw result deltas for A−H0, B−A, C−H0, D−C, E−C, E−D, and E−B;
- deterministic target-fraction table for H0/A/B/C/D/E;
- call accounting and stable-family state.

Do not provide causal interpretation or an editorial recommendation.

## Stop boundary

After A, B, C, D, and E complete or are safely recovered:

- stop;
- do not generate or apply prose;
- do not open another detector experiment;
- do not submit any GUI action;
- do not modify the article candidate or master;
- do not interpret the result;
- do not recommend a next action.

Chat owns diagnosis and the next versioned directive.
