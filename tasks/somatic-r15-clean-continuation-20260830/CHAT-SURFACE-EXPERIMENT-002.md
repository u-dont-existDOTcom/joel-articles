# CHAT-SURFACE-EXPERIMENT-002 — reader-visible transport correction

Task: `somatic-r15-clean-continuation-20260830`

Status: **FROZEN CHAT-AUTHORED EXPERIMENT / CODEX EXECUTION ONLY**

## Decision and prior-result disposition

`CHAT-SURFACE-EXPERIMENT-001` did not test the production reader-visible representation. Its A and B inputs retained Markdown heading markers, Markdown link destinations, two synthetic all-caps native-object placeholder labels, emphasis markers, bullet markers, and the terminal horizontal rule. The established whole-document Pangram materializer strips those non-reader-visible artifacts: headings become visible heading text, links become visible anchor text, native-object placeholders disappear, list markers disappear, and the horizontal rule contributes no text.

Therefore experiment 001 proves only that both raw-Markdown task representations scored AI `1.0`. It does **not** establish that the prose intervention is null in the actual reader-visible transport. Candidate B is not promoted: even within the confounded representation its humanizer score was lower than A. The correct next experiment repeats the exact A/B prose comparison in the same reader-visible representation used for whole-document Pangram boundaries.

## Worker role

Do not diagnose, rewrite, normalize, render, improve, select alternatives, or interpret detector results. Do not derive these files again from Markdown. Use the two Chat-frozen UTF-8 input files below byte-for-byte.

## Frozen source identity

- article branch: `task/somatic-r15-clean-continuation-20260830`
- source article candidate: `articles/somatic-therapies/experiments/R15-DIRECT-OWNER-VOICE-CANDIDATE-20260830.md`
- source article candidate SHA-256: `9c2e8fe57335d51ac925bc9b63cee8125c24e471e2b9b8fda50cc44cf28f5b31`
- natural section: `Building Enough Safety to Stay Present`

The article candidate is not changed by this experiment.

## Stable detector audit identity

`somatic-r15-surface-calibration-building-safety-visible-20260831`

Maximum new paid calls for this packet: **2 short-section API calls total**.

If both are uncached and complete successfully, cumulative calls for this stable section family become 4 of the 6-call cap. This packet authorizes no whole-document call and does not consume or alter the unused sixth whole-document GUI call.

## Exact Chat-frozen inputs

### A-visible-control

- path: `tasks/somatic-r15-clean-continuation-20260830/surface-experiment-002/A-reader-visible-control.txt`
- exact UTF-8 SHA-256: `11c553978685e355af6ef89b3de42380e724b4b0bb6eafef4fe6362ca26ef233`
- whitespace words: `378`
- Unicode characters: `2346`
- UTF-8 bytes: `2374`
- final newline: required

### B-visible-chat-replacement

- path: `tasks/somatic-r15-clean-continuation-20260830/surface-experiment-002/B-reader-visible-chat-replacement.txt`
- exact UTF-8 SHA-256: `cf67cc5760b7282caa4aaa13e06b6ec7d86c0885fb3e9b7eaaa52e1d79f72b97`
- whitespace words: `390`
- Unicode characters: `2361`
- UTF-8 bytes: `2387`
- final newline: required

## Mechanical preflight

For each file:

1. fetch/read the committed bytes without applying any Markdown or HTML transformation;
2. verify the exact SHA-256, word count, Unicode-character count, UTF-8 byte count, and terminal newline above;
3. fail closed on any mismatch;
4. confirm the file contains no `http://`, `https://`, `[EXISTING`, Markdown heading marker, Markdown link destination, emphasis marker, bullet marker, or horizontal-rule line;
5. record that the article candidate and registered `master.html` were not changed.

This is a representation correction, not a new semantic edit. The preservation assertion from experiment 001 remains PASS because A and B retain the same visible functions; the two files merely remove non-reader-visible transport artifacts.

## Detector execution

For A and B separately:

1. check the exact Pangram-4 cache/task/reservation state using model `pangram-4` and expected result version `4.0`;
2. reuse an exact completed result if present;
3. otherwise submit exactly once through the approved **short-document API route**, explicitly requesting Pangram 4;
4. persist the task identity before polling;
5. require terminal version `4.0` and `STAGE_SUCCESS`;
6. record exact Human, AI, and AI-assisted fractions, prediction/headline, confidence, and returned windows;
7. do not repeat after ambiguous work.

## Stop boundary

After both exact results are complete or safely recovered, stop. Do not apply B to the article. Do not draft Candidate C. Do not recommend a next edit. Do not run a whole-document measurement.

## Required return packet

Return only:

- exact article branch/head read;
- exact detector branch/head written;
- A and B hashes/counts and preflight PASS/FAIL;
- cache/reuse/new-call/ambiguity accounting;
- exact detector outputs and windows;
- raw B-minus-A deltas, including `humanizer_score` and `ai_assistance_score` where available;
- durable evidence paths and commits;
- explicit confirmation of zero article/master mutations and zero whole-document calls.

Chat owns interpretation and the next versioned directive.
