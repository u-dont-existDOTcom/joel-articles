# Codex handoff — Romance detector repair

Updated: 2026-08-21

## Owner instruction

Continue the Romance repair autonomously through routine next steps. Human/editorial quality and owner fidelity outrank Pangram. Do not merge canonical `main` until the candidate is deliberately accepted/reconciled. Do not ask Joel to approve routine continuation.

Joel's newest detector-boundary correction: very short passages are too noisy for confident editorial use. The current natural-owner reference is 97 words; future local diagnostics should normally use roughly **200+ contiguous reader-visible words** unless the real deliverable itself is shorter. If good natural-owner prose is merely low-confidence Human at ~100 words, widen the boundary before rewriting it.

## Mandatory recovery order

Fresh-read `u-dont-existDOTcom/joel-articles` first:

1. `SKILL.md`
2. `CANONICAL-REPO-MAP.md`
3. `AGENTS.md`
4. `docs/INDEX.md`
5. `state/CODEX-CURRENT-STATE.md`
6. `articles/INDEX.json`
7. `articles/romance/CURRENT-STATE.md`
8. `articles/romance/OWNER-LOCKS.json`
9. `articles/romance/ARCHITECTURE.md`
10. this task directory, especially the owner-rewrite/provenance files and `materialized-owner-integrated/`.

For detector work also fresh-read `u-dont-existDOTcom/pangram-humanization-lab` in the current lesson-index order. GitHub is canonical; current owner instruction outranks repo text and must then be persisted.

## Canonical article authority remains unchanged

`main:articles/romance/master.md` is still the registered canonical working master:

- SHA-256 `af50b7b93662daf00d484ad83faa0453ff0a2a4fda2867ecfd467166b4c984fe`.

The current task candidate is deliberately separate. PR #29 remains draft and must **not** be merged wholesale as article authority.

Registered Part 1 remains exact and must not be submitted again:

- SHA-256 `ae88df0f4156537239cb984337196703b88629c3588a5e58ee50c0888d3b39f8`
- 10,236 words
- registered Pangram 4 Human `0.9205247164`.

## Part 2 measured progression

Registered baseline:
- SHA `2df878093bc05fefa98ca30e9a97bdd52e212370f432bf0408e90f1b60c54bb0`
- Human `0.8983033895`.

Pass 1:
- SHA `30f61fb0c490ec1275f3c39c834a38a956041865b63e5592c270d51cc22d5498`
- Human `0.9137498736`.

Pass 2:
- SHA `679daa77fb92ea71bb85716e6ece671e093b49412b149e2f5129079a204d24d2`
- Human `0.9114283323287964`.

Pass 3:
- SHA `c6ef42419a3db2e82b1ff4f9370fc85bca4fa8c061c61dd6a1b5d28171d9908c`
- Human `0.9153165817`.

Pass 4:
- SHA `a21b9670bc0cc61b4fc850761ca57ffa5dc5d1a02bdd5df90b820d6f9d437a0e`
- Human `0.9215877056121826`.

Pass 5:
- SHA `a5b1cf38a81537492d08a8eac2e930012fbf10264beadfc252a3efc1bd794c20`
- Human `0.9247636795043945`.

Pass 6:
- master SHA `e09cb2309653d3ba9fc14526e7a49b1bef6f27a7494783489895a9c32fba93c5`
- Part 2 SHA `6166fb2c17022e978de1019210067429f749071e53581bbe184adb721dbe8215`
- 9,685 words
- Pangram 4.0 / `STAGE_SUCCESS`
- Human `0.9322237372398376`
- AI `0.06777624040842056`
- assisted `0.0`.

Part-2 paid-call cap is now **6/6**. Do not make an automatic seventh full-Part2 Pangram call. Transport changes, new chats, branches, or renamed audits do not reset this cap. A seventh same-section call requires explicit owner authorization.

## Owner-integrated candidate — current task checkpoint

Deterministic source: exact pass 6 above.

Generated directory:
`work/romance-detector-repair-20260820/materialized-owner-integrated/`

Exact candidate identities:

- master SHA-256 `dee776ada0db4dc2940d3815b9512ad5034e3224b0c569a9d29f6a69d9bb75a9`
- master whitespace words: **20,191**
- Part 1 SHA unchanged `ae88df0f4156537239cb984337196703b88629c3588a5e58ee50c0888d3b39f8`
- Part 1 words: **10,236**
- Part 2 SHA-256 `9dc539ca99f8c747ecd5a551f2c72ad476c87671919863d2ad469acf6c6e696f`
- Part 2 words: **9,804**.

Materialization commit:
`fbf3dcfd106f49ff062a6efc273cd63951ca59f6` (`github-actions[bot]`, `Materialize Romance owner-integrated candidate`).

The materializer is hash-gated to exact pass 6 and applies exactly four replacements. Its invariant audit passed:

- headings identical;
- native markers identical;
- Markdown link destinations identical;
- canonical protected anchors missing: none;
- owner-required new anchors missing: none.

The dedicated workflow runs the owner-integrated regression, materializes the candidate, runs the full repository unittest suite, content-authority validation, article-architecture validation, repository audit, and `git diff --check` before it can reach the commit step. The generated bot commit therefore records completion of those sequential gates for the materialized candidate.

## Four integrated replacements and provenance

### 1. Muses / polarity — direct owner rewrite

Authority/provenance:
- `OWNER-MUSES-REWRITE-LESSON-20260821.md`
- direct Joel prose.

Only two already-authorized D1 typo normalizations were applied in the candidate:
- `as the grow` -> `as they grow`
- `she see sees` -> `she sees`.

Do not otherwise smooth the owner's `gonna`, `tho`, asymmetric argument, archetype ontology, epistemic friction, or money/decision-authority claim.

### 2. Leadership / `Not A Performance` — assistant-produced, owner-accepted provisional

Authority/provenance:
- `OWNER-ACCEPTED-LEADERSHIP-REWRITE-20260821.md`.

Joel reported the exact local reader-visible rewrite as Pangram 4 **100% high-confidence Human**, but also said it still looked a little AI-shaped. Carry it as the current accepted candidate, but do **not** label it natural-owner or owner-final prose. Detector status and owner stylistic judgment remain separate.

### 3. `Attraction and exclusivity` — direct owner rewrite

Authority/provenance:
- `OWNER-EXCLUSIVITY-REWRITE-20260821.md`.

Joel's richer owner version is current local authority and tested HIGH-confidence Human in his short Pangram check. It preserves `Sexclusivity`, carrots/peas, the bureaucratic-romance judgment, bonobo qualification, flexible pair-bonding claim, and direct causal movement into the B. experiment.

A near-minimal owner control differed only by adding `have you ever looked?` and moved MEDIUM -> HIGH confidence. Treat that as local short-boundary evidence about live reader pragmatics, **not** a rhetorical-question token rule.

### 4. Former `pinkest elephants` span — owner-final local replacement

Authority/provenance:
- `OWNER-PINKEST-REWRITE-20260821.md`.

The exact natural-owner `When did you two last dance?` passage supersedes the assistant checklist and its generalized conclusion. Joel reports the 97-word passage as Human / low confidence and explicitly chose it anyway because it is his actual writing. Do not rewrite it for detector confidence; widen future diagnostic context first.

## Cold transition / architecture audit after assembly

Current result: **PASS** for the four inserted joins.

- Muses: `Maybe women are poetry...` now moves into the owner's archetype clarification, lived epistemic friction, argument/listening example, Big Picture/details polarity, micromanagement, and money/authority consequence. No mandatory symmetry or safety-taxonomy expansion was reintroduced.
- Muses -> leadership: the next passage usefully complicates authority by distinguishing a woman having real domain expertise from takeover/micromanagement; the direct-direction example then follows without a model-written summary bridge.
- Leadership -> `Not A Performance`: heading/function preserved; the current owner-accepted prose moves from chosen role asymmetry into the cost of performing masculinity and then Bee's `wife` joke. The owner's residual stylistic reservation remains recorded.
- Exclusivity: the vow/history material now stays in one causal current and reaches the B. experiment directly; there is no separate assistant mini-essay conclusion before the lived example. The following meditation/Magic-8-Ball material remains intact.
- Pinkest -> outside help: the natural-owner dance/resentment/wandering-eye passage ends on the lived consequence, then the Eshwar example supplies the next move. The old checklist and `perfectly worded speech` aftercare are gone.
- Article headings/order, native-object placement, link destinations, Gandarussa, Crucible safety, community function, children obligations, Hale/Heidi separation, and Bear close remain protected by the automated invariant gate.

No structural heading/section reordering was introduced, so the registered architecture topology remains unchanged for this task candidate.

## Current detector interpretation

Do not aggregate short local results into a full-Part2 score. Current measured full-Part2 authority remains pass 6 at Human `0.9322237372398376`. The owner-integrated Part2 `9dc539...` is **not yet measured as a whole**.

Short local detector evidence is useful only as diagnostics:
- leadership rewrite: owner-reported 100% high-confidence Human, with owner still perceiving some AI residue;
- exclusivity owner rewrite: owner-reported HIGH-confidence Human;
- natural-owner dance passage: owner-reported Human / low confidence at only 97 words.

The dance case establishes the workflow correction: widen short diagnostics to ~200+ contiguous reader-visible words before editing good owner prose for confidence.

## Current next safe action

1. Keep PR #29 draft and do not merge canonical main.
2. Do not retest Part 1.
3. Do not automatically buy a seventh full-Part2 Pangram call.
4. If further local diagnosis is useful, use contiguous ~200+ word natural contexts, preserve exact boundaries/hashes, and treat them as diagnostics rather than full-Part2 certification.
5. Continue editorial/cold-audit work from `materialized-owner-integrated/`, not from pass 6 or chat reconstruction.
6. If Joel explicitly authorizes another full-Part2 Pangram measurement later, freeze the exact `9dc539...` boundary first and preserve the 6/6 provenance rather than resetting the audit.
7. Only after owner acceptance should a clean reconciliation update `articles/romance/` on canonical main; do not merge this task branch wholesale.

## Do not lose these generation lessons

Current owner-confirmed article-specific AI-shape findings:

- objection-completion replacing thought-completion;
- mandatory symmetry replacing actual asymmetric judgment;
- clean abstraction replacing lived epistemic friction;
- safety/checklist expansion after the concrete point is already made;
- topic-sentence scaffolding replacing causal movement;
- equalized thought duration / regular conceptual bar-length;
- metrical antithesis / repeated verdict cadence;
- mirrored opposites used as closure machinery;
- recursive mini-essay rhythm / outline pulse / nested closure;
- compression can worsen model shape by deleting live thought pressure;
- live pragmatic/social acts can matter even when they add little propositional content.

Do not imitate typos, slang, rhetorical questions, fragments, or arbitrary sentence-length variation as detector tricks. The correction is upstream: recover the author's actual thought, causal pressure, asymmetry, social act, and true stopping point.
