# CHAT-SURFACE-EXPERIMENT-006 — final EFT production-compatible confirmation

Task: `somatic-r15-clean-continuation-20260830`

Status: **FROZEN CHAT-AUTHORED DETECTOR EXPERIMENT / CODEX EXECUTION ONLY / FINAL SLOT IN EFT FAMILY**

## Decision basis

`CHAT-SURFACE-EXPERIMENT-005` produced a clean factorial result:

- exact Human anchor alone: Human `1.0`;
- Human anchor + original portability tail, separate or merged: AI `1.0`;
- Human anchor + direct portability tail, separate or merged: Human `1.0`.

The paragraph boundary was null. The portability-tail realization determined the result in this exact boundary.

The direct tail is therefore the first experimentally supported surface repair in this Somatic task. Before Chat applies it to the current candidate, one remaining family slot will test it with the current candidate's attribution-correct EFT anchor rather than the older R15 anchor.

This call closes the stable EFT family at `6 / 6` regardless of result.

## Worker role

Mechanical executor only.

Do not:

- generate, revise, normalize, select, or apply prose;
- diagnose or interpret detector results;
- infer causality;
- recommend an edit;
- modify the article candidate or registered `master.html`;
- submit a GUI or whole-document action.

## Exact article authority

Article repository: `u-dont-existDOTcom/joel-articles`

Article branch: `task/somatic-r15-clean-continuation-20260830`

Source candidate:
`articles/somatic-therapies/experiments/R15-DIRECT-OWNER-VOICE-CANDIDATE-20260830.md`

Expected source-candidate SHA-256:
`9c2e8fe57335d51ac925bc9b63cee8125c24e471e2b9b8fda50cc44cf28f5b31`

## Exact Candidate E

Path:
`tasks/somatic-r15-clean-continuation-20260830/surface-experiment-005/E-current-anchor-direct-tail.txt`

Source commit:
`70c891981bce58c243ac3e1d7bdc810a0fd6af9f`

Git blob:
`46f7c1f8f735a648ef9808007bd1929cf924d206`

UTF-8 SHA-256:
`e9d2969aadbdd648ccd6b5aa36d6b7712b059a5b24a2acfcf95d29a4d458b7eb`

Whitespace words: `104`

Unicode characters: `570`

UTF-8 bytes: `574`

Terminal newline: `false`

Exact bytes:

```text
I think of the different tapping points as activating different parts of the brain. That is my thought; I am not presenting it here as a neuroscience result I proved. I move through the points and see how I feel at each one. It is also a little massage. Actually, shaving my head and massaging it works really well for me—maybe even better than EFT.

I can use EFT almost anywhere—before a hard conversation, right after somebody triggers me, or when my mind is looping and my body has joined in. It takes some pressure off. The deeper trauma can still be sitting there.
```

## Mechanical source assertions

Before detector submission, verify:

1. exact Git blob, SHA-256, word count, Unicode count, UTF-8 byte count, and terminal-newline state;
2. Candidate E contains exactly two paragraphs separated by one `\n\n`;
3. paragraph 1 is byte-identical to the current source candidate's paragraph beginning `I think of the different tapping points` and ending `maybe even better than EFT.`;
4. paragraph 2 is byte-identical to the direct tail already tested in experiment 005 C/D;
5. no article or registered-master mutation occurred.

## Mechanical preservation assertions

Verify Candidate E preserves:

- tapping-point/brain relation explicitly as Joel's thought, not an established neuroscience result;
- moving through the tapping points and noticing how each feels;
- tapping as a small massage;
- shaved-head massage comparison and `maybe even better than EFT`;
- EFT portability;
- use before a hard conversation;
- use immediately after being triggered;
- use during a thought loop involving both mind and body;
- pressure reduction;
- pressure reduction does not imply completion/removal of deeper trauma.

Preservation assertion must be `PASS` before submission.

## Detector family and accounting

Stable family:
`somatic-r15-eft-human-anchor-tail-factorial-20260831`

Current completed calls: `5`.

Maximum newly paid detector actions: **1 short-section API call**.

After completion, family state must be `CLOSED_6_OF_6`.

Detector evidence repository:
`u-dont-existDOTcom/pangram-humanization-lab`

Detector branch:
`task/somatic-r15-exact-recovery-20260830`

Expected detector starting head:
`caf33baebea29856e4f780a70367e969e53e69f4`

If the branch has advanced only through already-returned evidence and has no conflicting work, continue from its current tip and record the exact start head. Do not reset or discard evidence.

Whole-document GUI actions authorized: `0`.

Other GUI actions authorized: `0`.

## Detector execution

For exact Candidate E only:

1. check exact Pangram-4 cache, task, checkpoint, reservation, and ambiguity state;
2. reuse an exact completed result if present;
3. otherwise submit exact committed bytes once through the approved short-document API route;
4. explicitly request `pangram-4`;
5. persist task identity before polling;
6. require terminal version `4.0` and `STAGE_SUCCESS`;
7. record exact Human, AI, and AI-assisted fractions, prediction/headline, confidence, all returned windows, `ai_assistance_score`, and `humanizer_score` where present;
8. do not repeat after ambiguous work.

## Required output

Write under:
`state/experiments/somatic-r15-eft-human-anchor-tail-factorial-20260831/`

Required result file:
`RESULT-PACKET-E.json`

It must contain:

- exact article and detector branch heads;
- source candidate and Candidate E identities;
- preflight and preservation PASS/FAIL;
- cache/reuse/new-call/ambiguity accounting;
- exact Candidate E detector result and windows;
- raw E-minus-H0, E-minus-A, E-minus-C, and E-minus-D target/latent deltas using existing completed evidence;
- article mutations: `0`;
- registered-master mutations: `0`;
- GUI actions: `0`;
- whole-document calls: `0`;
- stable-family state: `CLOSED_6_OF_6`.

Do not supply interpretation or an editorial recommendation.

## Stop boundary

After exact E result completion or safe recovery:

- mark the family `CLOSED_6_OF_6`;
- stop;
- do not apply E to the article;
- do not create another variant;
- do not open another detector family;
- do not run a GUI or whole-document action;
- do not interpret the result;
- do not recommend a next action.

Chat owns the diagnosis and next exact directive.
