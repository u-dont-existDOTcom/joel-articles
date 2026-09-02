# CHAT-DETECTOR-FORENSICS-001 — cached A/B/C/D response forensics

Task: `somatic-r15-clean-continuation-20260830`

Status: **FROZEN CHAT-AUTHORED READ-ONLY FORENSICS / CODEX EXECUTION ONLY**

## Decision basis

The stable short-section family `somatic-r15-surface-calibration-building-safety-visible-20260831` is closed at `6 / 6`.

Exact target results:

- A control: Human `0.0`, AI `1.0`;
- B replacement: Human `0.0`, AI `1.0`;
- C replacement: Human `0.0`, AI `1.0`;
- D replacement: Human `0.0`, AI `1.0`.

No candidate from this family is authorized for article use. No additional candidate or paid call in this family is allowed.

The returned `humanizer_score` is not the owner target and must not be assumed to be a monotonic human-likeness gradient. This packet recovers all finer-grained evidence already present in the completed cached responses before Chat designs any new experiment elsewhere.

## Worker role

Mechanical executor only.

Do not:

- generate, revise, select, or apply prose;
- interpret why text looks AI;
- infer causality;
- recommend a next edit;
- submit any detector request;
- reserve any detector request;
- mutate the article candidate or registered `master.html`.

## Exact repositories and starting state

Article repository: `u-dont-existDOTcom/joel-articles`

Article branch: `task/somatic-r15-clean-continuation-20260830`

Source article candidate:
`articles/somatic-therapies/experiments/R15-DIRECT-OWNER-VOICE-CANDIDATE-20260830.md`

Source article candidate SHA-256:
`9c2e8fe57335d51ac925bc9b63cee8125c24e471e2b9b8fda50cc44cf28f5b31`

Detector repository: `u-dont-existDOTcom/pangram-humanization-lab`

Detector branch: `task/somatic-r15-exact-recovery-20260830`

Expected detector starting head:
`b77476b5c81029002ccecf5caabb8276728c3fad`

Stable family:
`somatic-r15-surface-calibration-building-safety-visible-20260831`

## Exact completed inputs and cache records

### A

Input SHA-256:
`11c553978685e355af6ef89b3de42380e724b4b0bb6eafef4fe6362ca26ef233`

Cache record:
`cache/pangram-4/4.0/11c553978685e355af6ef89b3de42380e724b4b0bb6eafef4fe6362ca26ef233/somatic-r15-surface-calibration-building-safety-visible-20260831-A-visible-control.json`

### B

Input SHA-256:
`cf67cc5760b7282caa4aaa13e06b6ec7d86c0885fb3e9b7eaaa52e1d79f72b97`

Cache record:
`cache/pangram-4/4.0/cf67cc5760b7282caa4aaa13e06b6ec7d86c0885fb3e9b7eaaa52e1d79f72b97/somatic-r15-surface-calibration-building-safety-visible-20260831-B-visible-chat-replacement.json`

### C

Input SHA-256:
`4717688560a3b08056da9eb77638186d0ae353861f024a4c24a65837a6d8a2a1`

Cache record:
`cache/pangram-4/4.0/4717688560a3b08056da9eb77638186d0ae353861f024a4c24a65837a6d8a2a1/somatic-r15-surface-calibration-building-safety-visible-20260831-C-visible-chat-replacement.json`

### D

Input SHA-256:
`58bd3babc5467fb4cba3792defd02624eb65366b69e9f65a6a2b7a8ba2f5db02`

Cache record:
`cache/pangram-4/4.0/58bd3babc5467fb4cba3792defd02624eb65366b69e9f65a6a2b7a8ba2f5db02/somatic-r15-surface-calibration-building-safety-visible-20260831-D-visible-chat-replacement.json`

Completed result packets:

- `state/experiments/somatic-r15-surface-calibration-building-safety-visible-20260831/RESULT-PACKET.json`
- `state/experiments/somatic-r15-surface-calibration-building-safety-visible-20260831/RESULT-PACKET-C.json`
- `state/experiments/somatic-r15-surface-calibration-building-safety-visible-20260831/RESULT-PACKET-D.json`

## Read-only forensic operations

For A, B, C, and D separately:

1. Verify the cached input SHA-256 and exact stored text identity.
2. Locate the most complete persisted raw Pangram response available for that exact completed task, including task/checkpoint/raw-response files if the normalized cache omits fields.
3. Emit a deterministic recursive schema inventory of every response field:
   - JSON pointer;
   - value type;
   - array length or object-key count;
   - scalar value for non-sensitive numeric/boolean/status fields;
   - never print credentials, cookies, request headers, or unrelated History data.
4. Recover every existing finer-grained score or span object, including any sentence-, token-, paragraph-, chunk-, probability-, logits-, feature-, attribution-, or alternate-window fields. Do not invent fields that are absent.
5. Bind each returned span to exact input offsets and SHA-256.
6. Segment the exact input deterministically into:
   - paragraphs by blank lines;
   - sentences using one fixed documented rule;
   - heading-label lines.
7. For every detector span, report overlap with each paragraph and sentence:
   - absolute start/end offsets;
   - overlap characters;
   - overlap percentage;
   - exact paragraph/sentence SHA-256.
8. If the raw response contains no localization finer than the single full-text window, record exactly:
   `NO_FINER_GRAINED_DETECTOR_SIGNAL_PRESENT`.

## Exact textual comparison operations

Without interpretation, produce A→B, A→C, and A→D deterministic maps containing:

- exact unchanged/deleted/inserted/replaced spans;
- sentence and paragraph count changes;
- sentence-length and paragraph-length vectors;
- punctuation counts;
- contractions counts;
- first-person and second-person pronoun counts;
- question-mark, parenthesis, colon, semicolon, dash, ellipsis, quotation-mark, and list/heading-line counts;
- repeated sentence-initial token sequences of length 1–4;
- repeated contiguous word n-grams of length 3–8 within each candidate;
- no style labels and no causal interpretation.

## Outputs

Write under:

`state/experiments/somatic-r15-surface-calibration-building-safety-visible-20260831/forensics/`

Required files:

1. `RAW-SCHEMA.json`
2. `SPAN-OFFSET-MAP.json`
3. `TEXT-STRUCTURE-METRICS.json`
4. `A-B-C-D-DIFF-MAP.json`
5. `FORENSIC-RESULT-PACKET.json`

`FORENSIC-RESULT-PACKET.json` must contain:

- exact detector branch/head before and after;
- all input/cache/result identities;
- whether a more complete raw response than the normalized cache existed;
- whether any finer-grained detector signal existed;
- paths and SHA-256 values for every output;
- confirmation of `new_paid_calls: 0`;
- confirmation of `detector_reservations_created: 0`;
- confirmation of `article_mutations: 0`;
- confirmation of `registered_master_mutations: 0`;
- confirmation that the stable family remains `CLOSED_6_OF_6`.

## Stop boundary

After committing and pushing the required read-only forensic packet, stop.

Do not draft Candidate E.
Do not open a new detector family.
Do not submit Pangram.
Do not interpret the evidence.
Do not recommend a next action.

Chat owns the diagnosis and the next versioned execution directive.
