# Somatic held-out humanization transfer test 126

Date: 2026-09-12
Status: FROZEN TEST DESIGN / FIRST PASS NOT YET GENERATED / NO PANGRAM / NO ARTICLE INSTALL

## Objective

Test whether the Stage-2 humanization method transfers to a different passage by measuring untouched first-pass generation quality. This is a generator-learning experiment, not article completion.

Controlling owner correction: `work/stage2-humanization-goal-correction-125.json`.
Source strategy: `articles/somatic-therapies/experiments/SOMATIC-STAGE2-FRESH-WRITER-SEMANTIC-CUSTODY-STRATEGY-094-20260911.md`.

## Frozen held-out source

Branch selection tip: `03a15714af007f59cef89fcc8bb5dbb86c237e62`.
Source artifact: `articles/somatic-therapies/WORKING-MERGED-READER-PROSE-20260905.md`.
Source Git blob: `4bf5535647af6c52d3daf27e296a7bbfe207eb6e`.
Boundary: start at `# Stage 3: Work With Trauma Feelings Before the Story Comes In`; include the Stage-3 opening and complete `## Brainspotting` subsection; end after the `Further reading` line; exclude `## After Brainspotting` and later material.

This source is working model-written prose, not owner-final wording. It has recoverable semantics and has not been through the Stage-2 fresh-writer/local-pressure process.

## Positive generation method under test

1. Recover the actual thought.
2. Identify one live reader pressure.
3. Give the writer only the semantic material needed to pursue that pressure.
4. Let that thought persist naturally.
5. Stop when the thought stops.

The preservation inventory is verification input, not composition architecture.

## Writer-side thought

Actual thought: some material is experienced before it becomes a coherent story; Brainspotting is relevant here because it can stay with emotionally charged, body-led material without requiring a complete narrative first.

Live reader pressure: `If Stage 3 is specifically before the story comes in, what does Brainspotting let someone work with here?`

A fresh writer must not receive prior Stage-2 candidates, detector feedback, preservation ledgers, sentence-specific repair history, critic diagnoses, or the supervisor's held-out baseline diagnosis.

## First-pass rule

Freeze the exact first fresh-writer output before any repair. Mark it `UNTOUCHED_FIRST_PASS`. Do not use a repaired candidate as evidence of first-pass improvement.

Evaluate the untouched first pass for:
- architecture PASS/FAIL;
- preservation-unit serialization;
- explanatory aftercare;
- hidden enumeration;
- mini-profile or mini-essay completion;
- false symmetry;
- repeated conceptual job switching;
- whether one thought persists naturally;
- semantic sanity;
- number and severity of critic interventions required.

## Critic and preservation order

Use a genuinely fresh architecture critic before preservation defense. Give the critic the literal candidate, heading purpose, and local reader pressure, but not the preservation inventory or prior failure ledger.

Only after architecture PASS run forward preservation and reverse traceability for the semantic material assigned to this bounded movement. Require zero unexplained substantive deltas. Do not append withheld obligations to make the passage complete.

## Transfer judgment

After first-pass findings are frozen, compare them with the Stage-2 failure classes. Ask whether familiar defects recurred without being named to the writer, whether first-pass architecture improved, how much critic repair was required, whether the prompt itself preloaded the defect, and whether Joel later identifies an obvious defect the critic missed.

If the same structural failure recurs, change the generation architecture rather than adding another prohibition.

## Independence boundary

The current supervising conversation has already read the Stage-2 failure history and the held-out source. It is therefore not a valid fresh-writer context. Same-context role-play would not count as transfer evidence.

Execution state: `FRESH_WRITER_CONTEXT_REQUIRED`.

No article authority, publishing state, citation state, or detector state is changed by this experiment.