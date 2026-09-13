# CHAT-SURFACE-EXPERIMENT-005 — Human EFT anchor × AI portability tail factorial

Task: `somatic-r15-clean-continuation-20260830`

Status: **FROZEN CHAT-AUTHORED DETECTOR EXPERIMENT / CODEX EXECUTION ONLY**

## Decision basis

The cross-transport calibration established that the short Pangram API recognizes both exact R15 spans that the whole-document GUI classified `Human / High`. The prior `Building Enough Safety to Stay Present` family is therefore valid negative evidence and remains closed at `6 / 6`.

This experiment moves to a different, sharper boundary inside exact R15:

- GUI window 3 is a 65-word `Human / High` EFT paragraph;
- the immediately following GUI window 4 is a 54-word `AI-Generated / High` portability paragraph.

The experiment keeps the exact Human paragraph fixed and tests two surface operations on the adjacent AI paragraph:

1. paragraph boundary: separate paragraph versus merged into the Human paragraph;
2. tail realization: exact original tail versus one Chat-authored direct realization preserving every substantive function.

This is a same-location, same-function comparison. The Human paragraph is calibration/context at its original destination, not insertion authority for another section.

## Worker role

Mechanical executor only.

Do not:

- generate, revise, normalize, select, or apply prose;
- diagnose or interpret detector results;
- infer causality;
- recommend a next edit;
- modify the article candidate or registered `master.html`;
- submit any whole-document or GUI action.

## Exact article/source authority

Article repository: `u-dont-existDOTcom/joel-articles`

Article branch: `task/somatic-r15-clean-continuation-20260830`

Source boundary file:
`articles/somatic-therapies/experiments/R15-WHOLE-ARTICLE-PANGRAM-BOUNDARY-20260830.txt`

Expected source Git blob:
`542012646469032eb836865b0e89b8fa368a1d0b`

Expected complete source UTF-8 SHA-256:
`9a81bd04252a2ee851dd111040c600837bdf0a7bbf71c42c293e3b763c99a707`

Source article candidate remains:
`articles/somatic-therapies/experiments/R15-DIRECT-OWNER-VOICE-CANDIDATE-20260830.md`

Expected source article candidate SHA-256:
`9c2e8fe57335d51ac925bc9b63cee8125c24e471e2b9b8fda50cc44cf28f5b31`

GUI localization authority:
`u-dont-existDOTcom/pangram-humanization-lab@0588d51d15dc4087c72adc4c35fd78d6be826887`

Localization map:
`state/recovery/somatic-r15-clean-continuation-20260830/exact-result-window-map.json`

Relevant prior GUI windows:

- window 3: `Human / High`, GUI AI likelihood `0.07161108404397964`, raw source offsets `8638:8998`, exact raw-span SHA-256 `00a753034b417b7512cd814ee3e78bc292961892a0fb85be31c5c269e3fc2c2d`;
- window 4: `AI-Generated / High`, GUI AI likelihood `0.9381056427955627`, raw source offsets `8998:9284`;
- combined exact source control: raw source offsets `8638:9284`.

All offsets are zero-based Unicode-codepoint offsets, end-exclusive.

## Frozen experiment inputs

Directory:
`tasks/somatic-r15-clean-continuation-20260830/surface-experiment-005/`

### H0 — exact GUI-Human anchor only

Path:
`H0-gui-human-anchor.txt`

Git blob:
`1a343e51e0b719894a8794a8c701bb99e14cf4b7`

UTF-8 SHA-256:
`00a753034b417b7512cd814ee3e78bc292961892a0fb85be31c5c269e3fc2c2d`

Whitespace words: `65`
Unicode characters: `360`
UTF-8 bytes: `360`
Terminal newline: `false`

This file must be byte-identical to source slice `8638:8998` and to GUI window 3's exact raw span.

### A — separate paragraphs, exact original tail

Path:
`A-separate-original-tail.txt`

Git blob:
`3a8501231c0bd5acf61321c6d91977617d0d37a6`

UTF-8 SHA-256:
`08b7db6171c196adc4409daec084a240649f1ce3524a360269bfba2e30379046`

Whitespace words: `119`
Unicode characters: `646`
UTF-8 bytes: `646`
Terminal newline: `false`

This file must be byte-identical to source slice `8638:9284`.

### B — merged paragraph, exact original tail

Path:
`B-merged-original-tail.txt`

Git blob:
`07047a4e53e0886ab55e598d705458fe430c8c10`

UTF-8 SHA-256:
`c3a831f5d71d1b8ab4208ee154acb04c1004d5416f35a4ee1fbdb1f5d00631e4`

Whitespace words: `119`
Unicode characters: `645`
UTF-8 bytes: `645`
Terminal newline: `false`

B must differ from A only by replacing the single paragraph separator between anchor and tail (`\n\n`) with one ordinary space.

### C — separate paragraphs, direct tail

Path:
`C-separate-direct-tail.txt`

Git blob:
`28b491f8e4268e77c46663e304cb6264c9a28f9e`

UTF-8 SHA-256:
`7cdcf4412116d289c73409054e1f7cd4bedd450e0853b690de3d3e2e5767fff6`

Whitespace words: `104`
Unicode characters: `581`
UTF-8 bytes: `583`
Terminal newline: `false`

### D — merged paragraph, direct tail

Path:
`D-merged-direct-tail.txt`

Git blob:
`b471cff87b1e68c831081830ee8dcbf36b305f8c`

UTF-8 SHA-256:
`fd752aa944bfa3abc2eb137765e33dd4f8fd1b742e4d52a97e11430e713a243b`

Whitespace words: `104`
Unicode characters: `580`
UTF-8 bytes: `582`
Terminal newline: `false`

D must differ from C only by replacing the single paragraph separator between anchor and tail (`\n\n`) with one ordinary space.

## Exact factor structure

- A: separate + original tail
- B: merged + original tail
- C: separate + direct tail
- D: merged + direct tail

The exact direct tail in C/D is:

`I can use EFT almost anywhere—before a hard conversation, right after somebody triggers me, or when my mind is looping and my body has joined in. It takes some pressure off. The deeper trauma can still be sitting there.`

## Mechanical preflight

1. Fetch/read the committed bytes without any transformation.
2. Verify each Git blob, SHA-256, word count, Unicode-character count, UTF-8 byte count, and terminal-newline state.
3. Verify source file blob and complete SHA-256.
4. Verify H0 equals exact source slice `8638:8998`.
5. Verify A equals exact source slice `8638:9284`.
6. Verify every A/B/C/D file begins with exact H0 bytes.
7. Verify the A→B and C→D differences are each exactly one `\n\n` to ` ` replacement at the anchor/tail boundary.
8. Verify article candidate mutations `0` and registered-master mutations `0`.
9. Fail closed on any mismatch.

## Mechanical preservation assertions for C/D

Verify that the direct tail preserves all original tail functions:

- EFT is portable/usable in ordinary situations;
- use before a hard conversation;
- use immediately after being triggered;
- use while the mind loops and the body participates in the loop;
- EFT can reduce/take pressure off;
- pressure reduction does not mean the deeper trauma has been completed or removed.

No other semantic change is authorized.

Preservation assertion must be `PASS` before C or D is submitted.

## Detector family and accounting

Stable family:
`somatic-r15-eft-human-anchor-tail-factorial-20260831`

Detector evidence repository:
`u-dont-existDOTcom/pangram-humanization-lab`

Detector branch:
`task/somatic-r15-exact-recovery-20260830`

Expected detector starting head:
`57db7a082636ebaca56c5618d7f654b675cdbce1`

If the branch has advanced only through already-returned evidence and contains no conflicting work, continue from its current tip and record the exact start head. Do not reset or discard evidence.

Maximum new paid detector actions in this packet: **5 short-section API calls total**.

Stable-family cap: `6` calls. This packet may use at most `5`, leaving one unspent refinement/confirmation slot.

Whole-document GUI calls authorized: `0`.
GUI actions of any kind authorized: `0`.

## Detector execution

For H0, A, B, C, and D separately:

1. check exact Pangram-4 cache, task, checkpoint, reservation, and ambiguity state;
2. reuse an exact completed API result if present;
3. otherwise submit exact committed bytes once through the approved short-document API route;
4. explicitly request `pangram-4`;
5. persist task identity before polling;
6. require terminal version `4.0` and `STAGE_SUCCESS`;
7. record exact Human, AI, and AI-assisted fractions, prediction/headline, confidence, all returned windows, `ai_assistance_score`, and `humanizer_score` where present;
8. do not repeat after ambiguous work.

## Required output

Write under:
`state/experiments/somatic-r15-eft-human-anchor-tail-factorial-20260831/`

Required:

- exact copied input files;
- task/checkpoint/cache evidence;
- `RESULT-PACKET.json` with all exact identities and results;
- raw result deltas for:
  - A minus H0;
  - B minus A;
  - C minus A;
  - D minus A;
  - D minus B;
  - D minus C;
- a deterministic 2×2 table of target fractions for A/B/C/D;
- call accounting and stable-family state.

Do not supply causal interpretation or an editorial recommendation.

## Stop boundary

After all five exact results complete or are safely recovered:

- stop;
- do not apply B, C, or D to the article;
- do not draft another variant;
- do not use the sixth family slot;
- do not submit any GUI or whole-document action;
- do not modify the article candidate or registered master;
- do not interpret the result;
- do not recommend a next action.

Chat owns diagnosis and the next versioned directive.
