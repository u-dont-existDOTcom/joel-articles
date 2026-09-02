# CHAT-CROSS-TRANSPORT-CALIBRATION-001 — exact GUI-Human windows through short API

Task: `somatic-r15-clean-continuation-20260830`

Status: **FROZEN CHAT-AUTHORED DETECTOR CALIBRATION / CODEX EXECUTION ONLY**

## Decision basis

The stable `Building Enough Safety to Stay Present` short-section family is closed at `6 / 6`. A, B, C, and D all returned Pangram API Human `0.0`, and the persisted API responses contain no signal finer than one full-text window.

Before Chat treats those API results as evidence about the owner’s actual Pangram GUI target, the short API route must be checked against exact spans that the already-completed Pangram 4 GUI whole-R15 result classified `Human / High`.

This packet does not test or alter article prose. It tests cross-transport discriminability using already-measured exact R15 material. No GUI call is authorized.

## Worker role

Mechanical executor only.

Do not:

- generate, rewrite, select, normalize, or apply prose;
- interpret why any text looks AI or Human;
- infer causality;
- recommend an edit or next action;
- submit a GUI request;
- mutate the article candidate or registered `master.html`.

## Exact source authority

Article repository: `u-dont-existDOTcom/joel-articles`

Article branch: `task/somatic-r15-clean-continuation-20260830`

Source file:
`articles/somatic-therapies/experiments/R15-WHOLE-ARTICLE-PANGRAM-BOUNDARY-20260830.txt`

Expected Git blob:
`542012646469032eb836865b0e89b8fa368a1d0b`

Expected complete UTF-8 SHA-256:
`9a81bd04252a2ee851dd111040c600837bdf0a7bbf71c42c293e3b763c99a707`

Decode the exact UTF-8 file to a Unicode string. All slice offsets below are zero-based Unicode-codepoint offsets, end-exclusive. Slice without adding, deleting, collapsing, or normalizing any character. Encode each slice directly as UTF-8. Do not append a terminal newline unless it is already inside the slice.

GUI localization authority:
`u-dont-existDOTcom/pangram-humanization-lab@0588d51d15dc4087c72adc4c35fd78d6be826887`

Localization map:
`state/recovery/somatic-r15-clean-continuation-20260830/exact-result-window-map.json`

## Exact calibration inputs

### H1 — GUI Human window 5

GUI evidence:

- window index: `5`
- label: `Human`
- confidence: `High`
- GUI AI likelihood: `0.14797909557819366`
- GUI Pangram word count: `223`
- section route: `Louka, TRE, blockage, natural shaking, and qigong`

Exact raw slice:

- Unicode start: `9284`
- Unicode end: `10502`
- Unicode characters: `1218`
- expected UTF-8 SHA-256: `d9a1fcd6ed832117b32e07844300f5b30d9067884481b14a63740dcc5bfe5d3b`

Save exact bytes as:
`state/experiments/somatic-r15-api-gui-human-window-calibration-20260831/inputs/H1-gui-human-window-5.txt`

### H2 — GUI Human window 7

GUI evidence:

- window index: `7`
- label: `Human`
- confidence: `High`
- GUI AI likelihood: `0.219383105635643`
- GUI Pangram word count: `215`
- section route: `outcome definition and housemate Brainspotting experiment`

Exact raw slice:

- Unicode start: `17379`
- Unicode end: `18571`
- Unicode characters: `1192`
- expected UTF-8 SHA-256: `1d7bb2473eea7c4c42229726aaeb953fc5fb6f30c1cfc316f2673e90be56f3aa`

Save exact bytes as:
`state/experiments/somatic-r15-api-gui-human-window-calibration-20260831/inputs/H2-gui-human-window-7.txt`

## Stable detector family

`somatic-r15-api-gui-human-window-calibration-20260831`

Detector evidence repository:
`u-dont-existDOTcom/pangram-humanization-lab`

Detector branch:
`task/somatic-r15-exact-recovery-20260830`

Expected detector starting head:
`0588d51d15dc4087c72adc4c35fd78d6be826887`

If the live branch has advanced only through the previously returned forensic result and contains no conflicting work, continue from its current tip and record the exact start head. Do not reset or discard evidence.

Maximum new paid detector actions: **2 short-section API calls total**.

Whole-document GUI actions authorized: **0**.

GUI actions of any kind authorized: **0**.

## Mechanical preflight

For the complete source and each exact slice:

1. verify source blob and complete source SHA-256;
2. verify slice offsets and Unicode-character count;
3. verify exact slice UTF-8 SHA-256;
4. compute and record whitespace-word count, UTF-8 byte count, and terminal-newline state;
5. verify each slice text is an exact substring of the authorized source;
6. verify the GUI localization map identifies the corresponding exact raw span hash as `Human / High`;
7. fail closed on any mismatch;
8. confirm article candidate mutations `0` and registered-master mutations `0`.

## Detector execution

For H1 and H2 separately:

1. check exact Pangram-4 cache, task, checkpoint, and ambiguity state;
2. reuse an exact completed API result if present;
3. otherwise submit the exact slice once through the approved short-document API route;
4. explicitly request `pangram-4`;
5. persist task identity before polling;
6. require terminal version `4.0` and `STAGE_SUCCESS`;
7. record exact Human, AI, and AI-assisted fractions, prediction/headline, confidence, all returned windows, `ai_assistance_score`, and `humanizer_score` where present;
8. do not repeat after ambiguous work.

## Required deterministic classification

Do not interpret the cause. Report only one mechanical route-comparison classification from exact results:

- `API_RECOGNIZES_BOTH_GUI_HUMAN_WINDOWS` — both H1 and H2 return API Human fraction `1.0`;
- `API_RECOGNIZES_ONE_GUI_HUMAN_WINDOW` — exactly one returns API Human fraction `1.0`;
- `API_RECOGNIZES_NEITHER_GUI_HUMAN_WINDOW` — neither returns API Human fraction `1.0`;
- `INCOMPLETE_OR_AMBIGUOUS` — either exact result is unavailable or ambiguous.

Also report raw API-vs-GUI label agreement for each window without causal explanation.

## Outputs

Write under:
`state/experiments/somatic-r15-api-gui-human-window-calibration-20260831/`

Required:

- exact input files;
- task/checkpoint/cache evidence;
- `RESULT-PACKET.json` containing all identities, GUI prior metadata, exact API results, route-comparison classification, call accounting, and durable paths/hashes.

## Stop boundary

After both exact results complete or are safely recovered:

- stop;
- do not generate prose;
- do not open another experiment;
- do not submit any GUI action;
- do not modify the article or master;
- do not interpret the result;
- do not recommend a next action.

Chat owns diagnosis and the next versioned directive.