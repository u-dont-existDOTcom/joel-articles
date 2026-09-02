# CHAT-APPLY-EFT-REPAIR-001 — apply the detector-validated EFT portability repair

Task: `somatic-r15-clean-continuation-20260830`

Status: **FROZEN CHAT-AUTHORED PRODUCTION PATCH / CODEX EXECUTION ONLY**

## Decision basis

The EFT factorial and production-compatible confirmation established:

- the current attribution-correct EFT anchor plus the original portability paragraph is detector-AI in the tested boundary;
- the same current anchor plus the exact direct tail below is Pangram 4.0 Human `1.0` / High;
- paragraph merging was null;
- every substantive portability/depth-distinction function was preserved;
- the EFT family is closed at `6 / 6`.

This packet applies only that experimentally validated tail replacement to a new non-authoritative article candidate. It does not modify the source candidate, registered `master.html`, or article authority.

## Worker role

Mechanical executor only.

Do not:

- generate, revise, normalize, select, or interpret prose;
- alter any text except the exact replacement below;
- diagnose humanization;
- recommend another edit;
- submit Pangram or create a detector reservation;
- modify registered `master.html`;
- promote article authority.

## Exact source identity

Repository: `u-dont-existDOTcom/joel-articles`

Branch: `task/somatic-r15-clean-continuation-20260830`

Required starting head: `ac1570f3e8945fecf80585d8fbe336c2a19ffbd6`

Source candidate:
`articles/somatic-therapies/experiments/R15-DIRECT-OWNER-VOICE-CANDIDATE-20260830.md`

Expected source Git blob:
`442349c82d92ac844447f27208924b720d9fa92a`

Expected source UTF-8 SHA-256:
`9c2e8fe57335d51ac925bc9b63cee8125c24e471e2b9b8fda50cc44cf28f5b31`

## Exact operation

Create a new file; do not overwrite the source candidate:

`articles/somatic-therapies/experiments/R15-EFT-REPAIR-CANDIDATE-20260831.md`

Copy the complete source candidate byte-for-byte, then replace exactly one occurrence of this complete paragraph:

```text
The big advantage is that EFT travels. Before a difficult conversation. Immediately after somebody triggers me. In the middle of a thought loop that has recruited my whole body. It can take the pressure down. I don't confuse that with finishing the deeper trauma work.
```

with exactly:

```text
I can use EFT almost anywhere—before a hard conversation, right after somebody triggers me, or when my mind is looping and my body has joined in. It takes some pressure off. The deeper trauma can still be sitting there.
```

Preserve the two surrounding newline separators exactly as they exist in the source file. The replacement changes only the paragraph bytes, not its position.

The old paragraph must occur exactly once. Fail closed if occurrence count is not `1`.

## Exact detector evidence binding

Detector repository: `u-dont-existDOTcom/pangram-humanization-lab`

Detector branch/head carrying Candidate E result:
`task/somatic-r15-exact-recovery-20260830@ede777c4455d699f64f46e7850e92c707fa31378`

Candidate E input SHA-256:
`e9d2969aadbdd648ccd6b5aa36d6b7712b059a5b24a2acfcf95d29a4d458b7eb`

Candidate E result:

- Pangram `4.0`;
- `STAGE_SUCCESS`;
- Human `1.0`;
- AI `0.0`;
- AI-assisted `0.0`;
- confidence `High`.

Result packet:
`state/experiments/somatic-r15-eft-human-anchor-tail-factorial-20260831/RESULT-PACKET-E.json`

Verify read-only that the exact replacement paragraph in this packet is byte-identical to Candidate E paragraph 2 and to the direct tail used in experiment 005 C/D. Do not submit anything.

## Mechanical preservation assertions

Require all of the following:

1. The current attribution-correct paragraph beginning `I think of the different tapping points` is byte-identical before and after.
2. The replacement preserves:
   - EFT portability;
   - use before a hard conversation;
   - use immediately after a trigger;
   - use while the mind loops and the body joins the loop;
   - pressure reduction;
   - the distinction between pressure reduction and completed deeper trauma work.
3. Every byte outside the one replaced paragraph and its changed length is identical to the source candidate.
4. Exactly one source paragraph is deleted and exactly one replacement paragraph is inserted.
5. Heading order is unchanged.
6. The ordinary-link URL multiset remains exactly `16` and byte-identical to the source candidate.
7. All seven reader-visible native-placeholder strings remain byte-identical and in the same order.
8. No text from R16–R65 or PR #72 is introduced.
9. Registered `articles/somatic-therapies/master.html` remains unchanged at SHA-256 `1e7e94717f40e7a4de77974a896f600a1bf2769d9c1846cbe84275e136ff5202`.
10. Forward traceability: PASS.
11. Reverse traceability: PASS.
12. Unexplained substantive deltas: `0`.

## Required artifacts

Create:

1. `articles/somatic-therapies/experiments/R15-EFT-REPAIR-CANDIDATE-20260831.md`
2. `articles/somatic-therapies/experiments/R15-EFT-REPAIR-BOUNDARY-20260831.txt`
   - materialize the complete reader-visible Pangram boundary using the same deterministic production materializer already validated for this task;
   - do not submit it.
3. `tasks/somatic-r15-clean-continuation-20260830/EFT-REPAIR-PRODUCTION-RECEIPT-20260831.md`
4. `tasks/somatic-r15-clean-continuation-20260830/EFT-REPAIR-DIFF-20260831.patch`
   - exact zero-context or minimal-context source-candidate → new-candidate patch;
   - must show only the one paragraph replacement.

The receipt must record:

- source and output Git blobs and SHA-256 values;
- source and output word/character/byte counts;
- exact reader-visible boundary blob/SHA/counts;
- exact deleted and inserted paragraph SHA-256 values;
- all preservation assertions and results;
- exact link and placeholder checks;
- exact detector evidence identity;
- article mutations limited to the new non-authoritative files;
- registered-master mutations `0`;
- paid detector calls `0`;
- detector reservations `0`;
- whole-document calls `0`.

## Validation

Run the repository-required mechanical checks applicable to this task, including:

- `python scripts/check_somatic_r15_task.py --preflight`
- preservation/source-integrity tooling for the exact changed scope;
- link/native-placeholder identity checks;
- quarantine check on the exact inserted paragraph;
- `python -m unittest discover -s tests`
- `python scripts/validate_content_repository.py --root .`
- `python scripts/audit_codex_github.py --root . --fail-on error`
- `git diff --check`

If a repository-wide test fails for a pre-existing unrelated reason, record it precisely and still fail closed on any failure that touches this candidate, task contract, authority, preservation, source integrity, links, placeholders, or Git hygiene.

## Commit and stop boundary

Commit and push only after every exact-scope assertion passes.

Do not update registered article authority.
Do not modify `master.html`.
Do not run Pangram.
Do not design the next experiment.
Do not interpret the patch.

Return only:

- exact starting and ending branch heads;
- exact source/output candidate identities and counts;
- exact reader-visible boundary identity and counts;
- exact diff/receipt paths and hashes;
- all assertion/test outcomes;
- article-authority/master mutation count `0`;
- detector call/reservation count `0`;
- confirmation that the EFT family remains `CLOSED_6_OF_6`.

Then stop. Chat owns the next diagnosis and directive.
