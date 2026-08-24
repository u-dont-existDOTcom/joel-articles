# Romance r23 current state

Updated: 2026-08-24

## Status

**r23r2 is the active candidate and the exact registered working-master promotion prepared on PR #46.** It is fully materialized, preservation-clean, architecture/dependency-clean, and owner-accepted at the bounded detector gate.

The PR branch copy of `articles/romance/master.md` is now byte-identical to the materialized r23r2 candidate. `main` remains unchanged until PR #46 is deliberately merged. No publication/export action is authorized or performed.

The prior r23r1 transition proposal is **superseded/rejected by Joel's owner test**: Joel reports r23r1 tested AI / low confidence. The exact r23r2 local realization tested Human / low confidence and Joel explicitly accepted it as `good enough`. The `R23R1-R03-VOICE-ROLLBACK-CANDIDATE.json` fallback remains provenance only and was not applied.

## Known-green rollback baseline

Exact r22 remains durable rollback evidence:

- master SHA-256 `f0f9a47eba2ac9ab1a56bdd6793316d41e7c23072b0b0c030285caf5e12f83c9`; 20,282 words;
- Part 1 SHA-256 `5ed333800b9ae7b402f26aa03e751ef8296c7e27ab70e39bc39bb9896b23e62d`; 10,239 words; Pangram 4.0 Human `1.0`;
- Part 2 SHA-256 `9e4c6a522c95741c7dfc9e040b2dcc40773427cbc0aef8f45211de77208b0c85`; 9,892 words; Pangram 4.0 Human `1.0`.

These are two exact half measurements, not a measured whole-article score.

## Exact r23 source

Canonical evidence source:
`u-dont-existDOTcom/pangram-humanization-lab@f4f2d6404e7362441c9ac0969dfc79313bea6ba1`, branch `evidence/romance-r23-gui-20260824-a`.

- master SHA-256 `322953b5d6f6ad49f7a3b41e5c6795b36404508f7768669cdcc72223f2f21a0d`; 20,364 words;
- Part 1 SHA-256 `620972febec1957403d261c4426c8fbba58763df2c0b78eb87a79da368f1f50b`; 10,296 words;
- Part 2 SHA-256 `a0dce58d2958e8467c1ba66cbed20b7c7ae075b8eddc7e1365eb8728485ff7f3`; 9,917 words.

The r23 candidate contains the five authorized editorial features / six exact operations recorded in `R23-FIVE-OWNER-EDITS-MANIFEST.json`: R23-01, R23-02A, R23-02B, R23-03, R23-04, and R23-05. Those operations remain intact in r23r2.

## r23r2 authorized delta

Exact delta and preservation ledger:
`R23R2-OWNER-FINAL-DELTA.json`

One operation only, `R23R2-01`, replaces the r23 Two Pillars local realization with Joel's exact owner-final tested bytes:

`Maybe an unusually strong couple can get away without much community. I think that's rare.  But sometimes a friend who actually knows us both sees the pattern before either of us does. On the other hand, If both people are falling apart, there is only so much anyone else can do.`

Owner-final text SHA-256: `cd8de93fda39fcdf13c4b1f6ba2f9250c11c40f8c8298f281055e37bafed6291`.

Required byte locks:

- retain the double space after `rare.`;
- retain capitalized `If` after `On the other hand,`;
- do not apply the older r23r1 four-word deletion ordering;
- do not apply the R23R1-R03 fallback;
- do not change any other r23 byte.

## Exact r23r2 materialization

Materialized artifacts:
`materialized-r23r2-owner-final/`

- master SHA-256 `f1c2b9a3f0f3d9e123c3870ca5d741af8ed99bbf6f138e68b845de04b1a12a2c`; **20,364 words**;
- Part 1 SHA-256 `620972febec1957403d261c4426c8fbba58763df2c0b78eb87a79da368f1f50b`; **10,296 words**; byte-identical to r23 Part 1;
- Part 2 SHA-256 `fbbcf64af313488b2ad8bb8969422f5bc85895eca908e41e9f796b2c0724e4eb`; **9,917 words**;
- Two Pillars natural-boundary SHA-256 `1bd239b9b56926b2a2dabc5a2f106ca58f50bcccd993b950e924fc481c27736e`; **734 words**.

The retained split topology remains exact: Part 1 ends after the initial patient paragraph; Part 2 begins `Key at first asked me innocently, "Can you be my guru?"`.

## Preservation / architecture proof

Full receipt:
`R23R2-PRESERVATION-RECEIPT.json`

Human-readable receipt:
`R23R2-PRESERVATION-RECEIPT-20260824.md`

- source identity freeze: PASS;
- preservation units: 5;
- forward traceability: PASS;
- reverse traceability: PASS;
- unexplained substantive deltas: **0**;
- claims/certainty/agency/chronology: unchanged;
- Part 1 byte identity: PASS;
- heading order/content: unchanged;
- native objects: 11 → 11;
- Markdown links: 22 → 22;
- protected father quote, Gandarussa, children-war warning, Bear callback, and terminal Rumi line: present;
- B. and H. examples: unchanged;
- architecture/dependency gate: PASS;
- section topology, community routing, setup/payoff relationships, native-object placement, and stopping point: unchanged.

## Detector evidence and owner acceptance

Exact r23 GUI evidence remains recorded:

- r23 Part 1: Pangram 4.0 Human `1.0`, AI `0.0`, AI-assisted `0.0`;
- r23 Part 2: Pangram 4.0 Human `0.9965084195`, AI `0.0034915956`, AI-assisted `0.0`; one AI-highlighted transition segment.

r23r2 Part 1 is byte-identical, so the Part-1 result remains exact evidence. The r23 Part-2 fractions do not transfer to the changed r23r2 bytes.

Joel reports:

- prior r23r1 local ordering: **AI / low confidence**;
- exact r23r2 local realization: **Human / low confidence**;
- owner disposition: **`good enough`**.

That explicit owner acceptance satisfies the bounded local detector gate. No new Pangram call was bought or run, and no full Part-2 or whole-article score is claimed or required before working-master promotion solely for detector confidence.

## Superseded / closed proposals

Superseded and not applied:

- r23r1 `Community isn't magic either;` four-word deletion with the old caveat → counterpoint order;
- `R23R1-R03-VOICE-ROLLBACK-CANDIDATE.json`.

Still closed unless Joel explicitly reopens them:

- slow/brakes purpose clause;
- Muses analytical/prose-function addition;
- Psychedelics sober stress-test list;
- generic three-sentence Two Pillars block;
- Attraction/exclusivity history→vow bridge;
- already-in-it stay-in-conversation diagnostic.

## Registration / merge posture

The exact r23r2 candidate is promoted inside the PR branch's registered Romance family as status `working`. Citation review and a fresh whole-article editorial pass remain pending, and the whole article is not marked owner-final or published.

Those pending review/publication planes do not block registering this owner-accepted working master. They do block claims that citation review is complete, the whole article is owner-final, or publication/export is authorized.

## Next safe action

Complete exact branch validation and hosted readback. If the recorded non-detector gates remain green, PR #46 is ready to merge into `main` as the registered working Romance authority. Do not publish/export, mark the whole article owner-final, or claim a whole-article detector result.
