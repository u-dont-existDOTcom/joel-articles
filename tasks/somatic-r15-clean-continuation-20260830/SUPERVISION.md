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
