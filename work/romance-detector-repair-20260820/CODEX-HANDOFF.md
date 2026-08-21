# Codex handoff — Romance detector repair

Updated: 2026-08-21

## Owner instruction

Continue the Romance repair autonomously through routine next steps. Human/editorial quality and owner fidelity outrank Pangram. Do not merge canonical `main` until the candidate is deliberately accepted/reconciled. Do not ask Joel to approve routine continuation.

## Blocking owner corrections

### Pangram paid-call cap is per genuine local repair section

Joel corrected the earlier rule on 2026-08-21. The hard six-paid-call guard applies to a **genuine local repair section**, not to an article, article half, or other multi-section aggregate certification boundary.

- local repair section: `budget_scope: section`; hard cap = 6 new paid POSTs for that stable section/audit identity;
- whole article / article half / other multi-section aggregate: `budget_scope: aggregate`; fully cached/accounted, but no six-call section cap;
- never split or rename one real local section to evade its cap;
- aggregate calls still require exact-cache, recovery-before-repeat, version, durability, and decision-value gates.

The Pangram lab implementation/docs were updated and CI-tested. Historical Part-2 calls remain cost/provenance evidence but do not make the ~10k-word Part 2 a single exhausted section.

### Short detector boundaries

For comparable Romance diagnostics, default to roughly **200+ contiguous reader-visible words** unless the real deliverable is shorter. If good natural-owner prose is low-confidence Human at ~100 words, widen context before rewriting it for detector confidence.

## Canonical authority

Canonical `main:articles/romance/master.md` remains unchanged and registered at SHA-256:

`af50b7b93662daf00d484ad83faa0453ff0a2a4fda2867ecfd467166b4c984fe`

PR #29 remains a draft task/experiment branch. Do **not** merge it wholesale as article authority.

Part 1 remains exact and must not be resubmitted merely because Part 2 changes:

- SHA-256 `ae88df0f4156537239cb984337196703b88629c3588a5e58ee50c0888d3b39f8`
- 10,236 words
- registered Pangram 4 Human `0.9205247164`.

## Aggregate Part-2 history

Registered baseline Human: `0.8983033895`.

- pass 1: `0.9137498736`
- pass 2: `0.9114283323287964`
- pass 3: `0.9153165817`
- pass 4: `0.9215877056121826`
- pass 5: `0.9247636795043945`
- pass 6: `0.9322237372398376`
- first owner-integrated aggregate, SHA `9dc539ca99f8c747ecd5a551f2c72ad476c87671919863d2ad469acf6c6e696f`, 9,804 words: Human `0.9761735796928406`, AI `0.02382640726864338`, assisted `0.0`, Pangram 4.0 / `STAGE_SUCCESS`.

The owner-integrated aggregate left three local AI windows in:

1. `Primal attraction / Not A Performance`;
2. `Two Pillars Don't Hold The Roof Up`;
3. `Psychedelics in relationship discernment`.

Those were then repaired and measured as distinct natural sections under their own section budgets.

## Local section repair results

### `primal-not-a-performance`

Calls used: **3/6**.

- r1: Human `0.7653250694274902`; generalized female-side mirror remained AI.
- r2: Human `0.6025727987289429`; paraphrasing the same symmetry worsened it.
- r3: **100% Human**, high confidence, 229-word boundary.

Winning editorial change: remove the reflexive generalized female-side symmetry paragraph rather than rewrite it again. Preserve the personal masculine-performance material, then move directly into concrete Toft/Anami receiving examples and the invitational material.

Exact result:
`pangram-humanization-lab:automation/pangram-fixed-batch/state/experiments/romance-detector-repair-20260820-owner-integrated-r3-local-sections-results.json`

### `community-two-pillars`

Calls used: **2/6**.

- r1: 100% Human but contained an editorially redundant repeated `eventually neither of us wants...` line.
- r2: duplicate removed; **100% Human**, high confidence, 716-word full section.

Winning change: keep the personal one-sided-friend-circle mechanism in one continuous causal movement into the practical two-person backup-system problem; remove the detached `outside support isn't really shared support anymore` mini-summary.

Exact result:
`pangram-humanization-lab:automation/pangram-fixed-batch/state/experiments/romance-detector-repair-20260820-owner-integrated-r4-local-sections-results.json`

### `psychedelic-relationship-discernment`

Calls used: **2/6**.

r2 reached **100% Human** on the complete section. The local repair replaces the list-like `sober, irritated, jealous, broke, bored...` explanatory window with the direct thought that psychedelic intimacy can be real without telling you whether the two people actually work together sober.

Exact result:
`pangram-humanization-lab:automation/pangram-fixed-batch/state/experiments/romance-detector-repair-20260820-owner-integrated-r2-local-sections-results.json`

## Current article candidate

The three exact locally passing repairs were deterministically applied to the prior owner-integrated candidate.

Directory:
`work/romance-detector-repair-20260820/materialized-owner-integrated-r2/`

Exact identities:

- master SHA-256 `7ff7a4c20ed879b6b9ff4c5d41cac406db5c5b3a726dc99f5bb4591b11368b48`
- master words: **20,090**
- Part 1 SHA unchanged `ae88df0f4156537239cb984337196703b88629c3588a5e58ee50c0888d3b39f8`
- Part 2 SHA-256 `20301b1bfb0052de694657411f231f82d9a45ae62ff9c4839015befce5c57dc2`
- Part 2 words: **9,703**.

The hash-gated materializer changed exactly three spans:

1. `Not A Performance` r3;
2. `Two Pillars` r2;
3. psychedelic discernment r2.

Invariant audit passed: headings, native markers, Markdown link destinations, Gandarussa, Bear terminal callback, community claim, and required repaired anchors are intact. The materialization workflow also runs repository tests, content-authority validation, article-architecture validation, repository audit, and `git diff --check` before committing generated output.

Manifest:
`work/romance-detector-repair-20260820/materialized-owner-integrated-r2/candidate-manifest.json`

## Aggregate certification state

A fresh aggregate Pangram-4 measurement has been frozen/submitted for exact Part 2 SHA:

`20301b1bfb0052de694657411f231f82d9a45ae62ff9c4839015befce5c57dc2`

Experiment:
`romance-detector-repair-20260820-part2-owner-integrated-r2-20260821`

This is an **aggregate** accounting boundary, so the local six-call section cap does not apply. Do not duplicate the submission. Recover its committed result or pending task state before any repeat.

At the time of this checkpoint, the result file had not yet appeared on `automation/pangram-fixed-batch`; treat it as pending/in-flight, not failed and not absent.

## Existing owner-integrated provenance that remains in r2

- Muses/polarity: direct Joel rewrite, with only already-authorized typo normalization.
- Leadership immediately before `Not A Performance`: assistant-produced, Joel-accepted provisional; Joel reported the local passage 100% high-confidence Human while still perceiving slight residual AI shape.
- Attraction/exclusivity: direct Joel rewrite, owner-reported high-confidence Human locally.
- `When did you two last dance?`: owner-final local replacement; preserve despite its 97-word low-confidence Human result.

## Generation lessons currently active

Do not lose these:

- objection-completion replacing thought-completion;
- mandatory symmetry replacing actual asymmetric judgment;
- clean abstraction replacing lived epistemic friction;
- generalized checklist/safety expansion after the concrete point is made;
- topic-sentence scaffolding replacing causal movement;
- equalized thought duration / regular conceptual bar-length;
- metrical antithesis / repeated verdict cadence;
- mirrored opposites used as closure machinery;
- recursive mini-essay rhythm / outline pulse / nested closure;
- compression can worsen model shape by deleting live thought pressure;
- genuine reader-facing pragmatic/social acts are part of prose, not detector charms.

Current active reusable protocol:
`project-sources/RHYTHM-AND-THOUGHT-SHAPE.md`

## Next safe action

1. Recover the pending exact aggregate result; **do not resubmit** while pending/ambiguous.
2. If the 9,703-word Part 2 is 100% Human, run final editorial/architecture/provenance closeout and present the candidate for owner acceptance/reconciliation.
3. If aggregate residual AI remains, localize it and assign each genuine natural section its own existing/new section budget; do not treat Part 2 itself as a capped section.
4. Do not retest Part 1 merely because Part 2 changes.
5. Do not merge PR #29 wholesale. A clean owner-approved reconciliation must update canonical `articles/romance/` deliberately.
