# Episode 008 — Write It. Don't Send It Yet — Railway Agent 20-generation P3 search

Date: 2026-09-19
Status: **COMPLETE / 20 RAILWAY GENERATIONS / 7 PANGRAM TESTS / 0 PASSES**

## Owner-authorized search

Joel directed:

> just iterate yourself with railway agent and test pangram if you think it passes, continue through 20 iterations or until you find a pass

Execution followed that boundary:
- exactly 20 Railway Agent P3 generations;
- structurally weak/redundant candidates rejected before Pangram;
- only candidates judged materially plausible were measured;
- stop at generation 20 because no pass was found.

## Generation accounting

R1 — first-person pencil image; rejected pre-detector: tidy explicit `one job / another job` closure.

R2 — dialogue-heavy; rejected pre-detector: still ends in tidy explicit `one job / another job` closure.

R3 — uneven reflective turn; Pangram tested.

R4 — voice-note/self-correction; banked, not stronger than later R5.

R5 — concrete pencil scene with self-correction and unfinished return; Pangram tested.

R6 — ordinary-social-language version; banked, not stronger than R5.

R7 — longer rereading/digression; rejected because it invented an unsupported time-of-day detail.

R8 — second-person lived rereading, ending on discovered `no`; Pangram tested.

R9 — child-to-adult perspective shift; rejected pre-detector: balanced explanatory structure remained strong.

R10 — almost entirely adult/child dialogue; Pangram tested.

R11 — late emergence of child/adult labels; banked, but more polished than R13/R14/R18.

R12 — physical page/pencil scene; rejected because it invented unsupported material scene details.

R13 — self-questioning that changes its own inference; Pangram tested.

R14 — sparse narration/dialogue with a misfire and correction; Pangram tested.

R15 — digressive third-person adult/child scene; rejected as a voice/POV mismatch with surrounding first-person section.

R16 — short plain version; rejected as too compressed/explanatory and weaker than other finalists.

R17 — free-indirect hurt-part voice; rejected for vague `thing` placeholder and tidy explanatory movement.

R18 — editor role becomes inadequate mid-paragraph; Pangram tested.

R19 — one long breathy sentence + short close; rejected as too designed/architectural.

R20 — very short plain contact scene; rejected as below useful richness and detector length confidence.

## Exact Pangram results

All used:
- Pangram 4.0;
- STAGE_SUCCESS;
- local authenticated Playwright GUI;
- exact UTF-8 History binding PASS;
- no API;
- one submission per candidate.

### R3
SHA:
`b7f170b9d5a2296c8384c885426167b901a0d464f73f40e8acc1bd48cb1a383a`

Words: 142.

Result:
- AI 1.0
- Human 0.0

### R5
SHA:
`0ea676099f81783f2b56eeec85dbb2fcc5afb6f4f0b9d438f9d49e59744a1e45`

Words: 122.

Result:
- AI 1.0
- Human 0.0

### R8
SHA:
`b13c2ad503b564151e36f5ac44f9a491199becf033eb81b3722a447e78ede3fe`

Words: 203.

Result:
- AI 1.0
- Human 0.0

### R10
SHA:
`a20fd7bc7f9ab31fde6cffd7bbde7a44ad75c2d687fdc67261a108e4b066e799`

Words: 169.

Result:
- AI 1.0
- Human 0.0

### R13
SHA:
`2edbb1bd4e6643b23834218088bee9e85a880de2196dda70fd3ebd34261fec21`

Words: 128.

Result:
- AI 1.0
- Human 0.0

### R14
SHA:
`136271574f0e25d10eae0f26e9d8fb01caf54196e7e6ed17b060f5f6a38a9c9b`

Words: 108.

Result:
- AI 1.0
- Human 0.0

### R18
SHA:
`9620f34a55067ec427b8c39efdd559c61d099edd6f312e111d582b7d74e24d29`

Words: 140.

Result:
- AI 1.0
- Human 0.0

## Evidence location

Pangram raw evidence branch:
`u-dont-existDOTcom/pangram-humanization-lab@evidence/inner-child-p3-railway-20260919`

Each tested SHA has its own:
`state/gui-runs/pangram-4/<SHA>/result.json`

## Interpretation

This bounded search is strong evidence that **Railway Agent, on this P3 target, did not produce a detector-Human paragraph across a broad range of discourse architectures**.

The tested set included:
- reflective first-person;
- concrete scene with self-correction;
- second-person lived observation;
- almost-pure dialogue;
- genuine self-questioning;
- dialogue misfire/correction;
- editor-role reversal.

Every measured candidate saturated at AI 1.0.

Do not infer:
- that Railway Agent can never produce Pangram-Human prose on another target;
- that Pangram is a universal authorship oracle;
- that any individual phrase caused the failures.

## Method disposition

**RAILWAY P3 SEARCH EXHAUSTED AT OWNER-AUTHORIZED 20-GENERATION BOUND.**

Do not run generation 21 as a continuation of this lane without a new owner instruction or materially new evidence.

P1 and P2 remain frozen.
P3 remains unresolved.
