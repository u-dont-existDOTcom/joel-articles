# Somatic R15 supervision ledger

Task id: `somatic-r15-clean-continuation-20260830`

Conversation identity: existing authenticated ChatGPT conversation whose visible recent history contains Joel's literal correction `no R65 was not the frontier it was a long failed branch you forgot`.

## SOMATIC-R15-BOOTSTRAP-001

Request sent: 2026-08-30

The bootstrap packet bound the clean task branch, exact R15 candidate and receipt blobs, exact candidate and Pangram-boundary hashes, failed-line quarantine, unchanged registered master, and the absence of any Pangram action by this task. A browser timeout occurred during send. The exact conversation was inspected before any retry; one user-authored request with this ID and one matching assistant response were present, so the request was not resent.

Matching response prefix:

`SUPERVISOR_DECISION SOMATIC-R15-BOOTSTRAP-001`

Decision: **APPROVED WITH ONE REQUIRED CORRECTION**.

Authorized direction:

- correct the ambiguous provenance claim about the materializer;
- prove R15 identity directly as immutable R15 candidate blob -> deterministic materialization -> exact R15 boundary SHA-256;
- treat historical R16 only as evidence for the general extraction convention, never as R15 identity proof;
- complete the cold production preflight and exhaustive exact-boundary detector-state recovery;
- persist exactly one of `EXACT_R15_RESULT_EXISTS`, `EXACT_R15_ACTION_AMBIGUOUS`, or `EXACT_R15_NEVER_SUBMITTED`;
- perform exactly one whole-document Pangram 4 GUI measurement without another approval request only if the preflight finds no concrete high-confidence defect, the identity chain is clean, and recovery proves `EXACT_R15_NEVER_SUBMITTED`;
- if recovery is ambiguous, recover only and do not repeat;
- after obtaining or recovering the exact result, send `WORKER_SUPERVISION_REQUEST SOMATIC-R15-RESULT-002` with the complete binding and diagnosis before detector-driven rewriting.

Provenance correction implemented: the recovery checkpoint and PR language now distinguish the R15 identity chain from the R16 convention regression test. The R15 and R16 boundary blobs are not represented as identical.

No Pangram action occurred during this bootstrap round trip.

## SOMATIC-R15-RESULT-002

Request sent: 2026-08-30

Status: **DECIDED / INDEPENDENT READER AUTHORIZED**

The result packet bound:

- article branch `task/somatic-r15-clean-continuation-20260830` at `f5b4f0ac587fef079b05a0ee477bb502455ccfe5`;
- detector branch `task/somatic-r15-exact-recovery-20260830` at `0d03264302bb7deaf168dae0842c97b7b80ccb57`;
- immutable R15 candidate blob and SHA-256;
- exact reader-visible boundary `9a81bd…`;
- Pangram 4.0 Human `0.1547368467`, AI `0.8452631831`, AI-assisted `0.0`, `STAGE_SUCCESS`, with exact UTF-8 History binding;
- all nine High-confidence window routes and the localization-transport caveat;
- the controller's diagnosis of each AI run;
- the negative evidence that R15's earlier red-run reconstruction preserved approximately the same detector topology;
- the R16, R17–R58, R59–R65, and PR #72 quarantines;
- a recommendation against another broad detector rewrite and in favor of the required fresh detector-blind independent reader.

The browser timed out at the send interaction. The exact conversation was then reopened before any retry. A fresh authenticated view proved the request appeared exactly once as a new user message and the composer was empty. The packet was not resent.

The packet itself transcribed both full branch hashes incorrectly by extending their eight-character prefixes with guessed suffixes. Fresh Git verification proved the article result commit was `f5b4f0ac587fef079b05a0ee477bb502455ccfe5`, not `f5b4f0ad…`, and the detector head was `0d03264302bb7deaf168dae0842c97b7b80ccb57`, not `0d032643ba55…`. Immediately before the correction commit, the article branch had advanced through this request receipt to `17f5a9ccefd108ac253374d31bfab09dc9b43a25`; the detector branch remained at the corrected head above.

Matching response prefix:

`SUPERVISOR_DECISION SOMATIC-R15-RESULT-002`

Decision: **NO DETECTOR-LED REPAIR AUTHORIZED. PROCEED TO GENUINELY INDEPENDENT, DETECTOR-BLIND FINAL READER.**

The supervisor accepted the controller diagnosis for W0, W2, W4, W6, and W8, explicitly barred editing/testing the EFT portability hypothesis now, and authorized no further Pangram call. The exact result is diagnostic evidence, not a repairable defect.

Before the reader, mechanically correct the false full-head references and stale PR descriptions without changing article prose. Then give one genuinely separate fresh context only the reader-facing article beginning at `# Introduction`, ordinary headings/prose in order, neutral native-media positions, and the minimal description that it is a first-person practical article for readers considering somatic approaches. Withhold Pangram, `R15`, detector filenames, all later-round history, preservation defenses, prior audits/rationales, this supervision conversation, and rejected alternatives.

The reader diagnoses only; it does not rewrite. Persist its exact input identity and findings, adjudicate them against source/preservation/architecture, then return as `WORKER_SUPERVISION_REQUEST SOMATIC-R15-READER-003`. Do not edit the candidate or make a paid detector call before the matching reader decision.

## SOMATIC-R15-READER-003

Status: **DECIDED / BOUNDED REPAIR AUTHORIZED**

The genuinely separate detector-blind reader is complete. It ran in a new ordinary ChatGPT conversation outside the article project and supervising conversation, received no detector or drafting-history context, and had diagnostic authority only. Its input article, transmitted packet, and exact response are frozen at SHA-256 `460dc342…`, `6cc91944…`, and `3d9d96d…` respectively.

The privacy-safe reader receipt is in `FINAL-READER.md`; detailed findings stayed outside the public branch. The full packet was sent once to the exact supervising conversation. The send interaction timed out, but a fresh view proved exactly one user request, an empty follow-up composer, and an active supervisor response, so the packet was not resent.

Matching response prefix:

`SUPERVISOR_DECISION SOMATIC-R15-READER-003`

Decision: **BOUNDED REPAIR AUTHORIZED**.

The response is bound locally at SHA-256 `46e58fffc6e0c0d04acc2fb17ab33cb1c2625079fec3f5c121646114d05ff825` (9,924 Unicode characters / 9,968 UTF-8 bytes). It authorized four independently diagnosed, source-grounded repair scopes and required separate provenance/whitelist/preservation gates before drafting. It rejected the uncorroborated W4 hypothesis, broad rewriting, protected-personality removal, failed-branch reuse, detector optimization, another Pangram call, and `master.html` promotion.

After a minimum combined repair passes traceability, preservation, architecture, multiscale and cold-audit gates, run a new genuinely separate detector-blind reader on that repaired candidate. Then return `WORKER_SUPERVISION_REQUEST SOMATIC-R15-REPAIR-004`; no Pangram call or promotion may occur first.

The minimum combined A–D candidate is locally frozen at SHA-256 `85c09a28036a80ff25afd3e3474ad6160fe162f2e120db711fe8ce7c7bc9ea00` and local commit `ac5eaefcf970b511562909d082b993cebb582716`; all pre-reader gates pass. Its initial push was rejected at the host safety boundary because the destination repository is confirmed PUBLIC and the full article contains personal/health material. The required new blind-reader transmission was separately paused at its action-time privacy confirmation boundary.

Joel explicitly confirmed both transmissions in the current Codex chat on 2026-08-30 and directed the controller to continue without another approval request. This authorizes pushing the already frozen repaired candidate to public PR #73 and transmitting that exact candidate to one fresh detector-blind ChatGPT reader. It does not authorize another Pangram call, registered `master.html` promotion, or Substack publication.
