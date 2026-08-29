# Romance reader-gap / Obsidian pilot

Status: **EXPERIMENT / DIAGNOSTIC ONLY.** Nothing in this directory is article authority or edit authorization.

The pilot intentionally lives under `docs/experiments/`, not inside `articles/romance/`, because the registered article-family inventory is fail-closed: every file inside a registered article family must itself be registered. A disposable diagnostic Canvas should not acquire article-authority status merely because it visualizes an article.

Frozen article under test:

- article: `romance`
- canonical master: `articles/romance/master.md`
- SHA-256: `f1c2b9a3f0f3d9e123c3870ca5d741af8ed99bbf6f138e68b845de04b1a12a2c`
- required structural map remains: `articles/romance/ARCHITECTURE.md`

## Question being tested

Does a promise-first + blind-prefix reader-question layer reveal material editorial negative space that the existing Mermaid architecture map, multiscale editorial ledger, and whole-article cold/independent-reader audits do not make easy to see?

The experiment is not trying to maximize completeness. A reader question can be valid and still deserve `out-of-scope`, `leave-implicit`, `interlink`, or `reject` rather than new prose.

## Existing-work composition

This pilot does not introduce a new article theory. It composes:

- the existing Mermaid section/function map;
- the existing multiscale reader-state/question and paragraph-job ledger;
- the existing argument/evidence ledger for factual premises and countermodels;
- lightweight RST-style relation labels when useful;
- IBIS-style question/answer/argument objects;
- Obsidian JSON Canvas only as a spatial diagnostic view.

## Blind-test architecture

The fresh-reader test is deliberately split into two stages so mechanical retrieval cannot contaminate editorial reasoning.

### Stage 1 — collector

The collector may access GitHub but performs **no editorial analysis**.

`scripts/compile_blind_reader_packet.py` verifies the exact canonical source SHA-256, splits the bytes into contiguous 90-line windows, hashes every window, and writes a deterministic manifest. Concatenating the windows must reproduce the exact canonical source SHA-256.

Use `COLLECTION-PROTOCOL.md` for this stage.

Generated windows are ephemeral and are **not committed to the repository**.

### Stage 2 — Pro reader

The Pro reader must have no GitHub/web access and no access to the complete packet. A human/controller reveals exactly one frozen window at a time. The reader freezes its checkpoint before receiving the next window.

This is stronger than placing the full article in context and merely instructing a model not to look ahead: unrevealed content is actually unavailable.

Use `FRESH-READER-BLIND-PROTOCOL.md` for this stage.

## Hosted validation of the collector

The PR-hosted regression run on 2026-08-29 passed **117/117 tests**. The canonical integration test reads the checked-out `articles/romance/master.md`, verifies its exact SHA-256 against `f1c2b9a3f0f3d9e123c3870ca5d741af8ed99bbf6f138e68b845de04b1a12a2c`, compiles 90-line windows, and verifies that their exact byte reconstruction has the same SHA-256.

The workflow then stops at the repository's existing authority validator because of four pre-existing base-repository findings in unchanged article/governance files. Those are separate from this pilot and are not suppressed or repaired here.

## Pilot passes

### A. Promise-first

Read only the opening promise/scope first. Generate the material questions a reasonable intended reader would expect the guide to resolve. Only then compare those questions with the full article.

### B. Blind-prefix

At consequential boundaries, preserve the reader's actual information state by looking only backward. Record the strongest live question, freeze it, then reveal the next source window.

### C. Final coverage pass

After the final window only, merge semantic duplicates and classify whether each surviving question was answered, answered later, partial, thin, unanswered, intentionally out of scope, or rejected by the article. A live question is not automatically a defect.

### D. External benchmark

After the article-internal result is frozen, compare it with mature relationship-assessment/education domains, relevant research, and sampled actual-reader questions. External prevalence is evidence of reader demand, not a completeness mandate.

## Independent blind result

The exact fresh-Pro result received on 2026-08-29 has SHA-256:

`355f02e2af2cfc4d9d9a987dd1418e6d68230798eb6ef70738ce6133c731d1fd`

It contains:

- 4 frozen promise questions;
- 11 immutable checkpoints;
- 32 surviving questions after hindsight merging;
- 2 `candidate` defects;
- 6 `unclear` questions;
- 24 questions explicitly classified `not-a-defect`.

This is important negative evidence against generic omission generation: the model preserved many live questions while still recognizing that most were answered, deliberately unresolved, or outside the article's required burden.

## Comparison result

### Strongly convergent cluster

The hidden pilot and independent reader both identified the same underlying pressure:

- temporary strain versus durable incompatibility or ending;
- repairable trigger versus a structurally wrong match;
- broken trust and mismatch workability;
- safety as a distinct boundary.

The fresh reader expressed this through narrower domain questions rather than a global “relationship health score.” G001, G002, and G004 should therefore be merged analytically into one workability/trajectory cluster.

### Clearest new independent candidate

The fresh reader asked how a couple can tell whether poor sexual fit may deepen through a co-created bond or instead means they should remain friends. It classified this `thin / candidate`. This was not explicit in the hidden register.

### Distributed governing question judged answered

The fresh reader reproduced grounded love versus idealization but judged the article's distributed treatment sufficient. This supports using a question map to visualize coverage across sections; it does not support adding a checklist merely because the answer is distributed.

### Hidden candidates not independently reproduced

The independent article-internal test did not reproduce these as defects:

- maintaining the partnership after children arrive;
- money/labor/household/dependency alignment;
- a compact ordinary-conflict repair model.

They remain legitimate framework/research/actual-reader opportunities, but their previous status as leading article-internal gaps is downgraded.

### Other independent review questions

The reduced live register retains:

- the scope of masculine–feminine generalizations;
- jealousy as remembered insecurity versus a present signal;
- broken trust: repair, relationship-form change, or ending;
- parental-figure obligations when contact is blocked or risky;
- the boundary for post-breakup truth disclosure.

## Architecture decision

### Reader-question method

**Validated as an optional diagnostic for broad long-form publication preparation.** It independently reproduced a deep hidden cluster, found a genuinely new candidate, correctly recognized delayed/distributed answers, and falsified or downgraded several initial hypotheses.

### Obsidian Canvas

**Promising but not yet established as necessary.** The test validates durable question objects and typed answer relationships. It does not yet prove Canvas is more useful to Joel than the reduced table/register.

Do not make this a mandatory repository gate. Retain it as an optional observatory until owner inspection shows that the spatial view improves a real editorial decision.

## Reduced production shape

If reused, keep the workflow minimal:

1. promise-first freeze;
2. sequential blind-prefix checkpoints;
3. final hindsight coverage classification;
4. retain only `candidate`, `unclear`, a few answered controls, and separately labeled external-only opportunities;
5. generate Canvas from the reduced register only.

Do not turn every transient checkpoint question into a permanent editorial task.

## Files

- `reader-gap-register.json` — original hidden diagnostic register.
- `romance-reader-gap.canvas` — original generated Canvas.
- `EXTERNAL-BENCHMARK.md` — established-work and actual-reader pressure test.
- `COLLECTION-PROTOCOL.md` — mechanical GitHub/source collection stage.
- `FRESH-READER-BLIND-PROTOCOL.md` — isolated Pro reader stage.
- `HANDOFF-PROMPTS.md` — collector, Pro startup, window, and closeout instructions.
- `results/INDEPENDENT-PRO-COMPARISON-20260829.md` — complete hidden-versus-independent comparison and architecture decision.
- `results/reduced-reader-gap-register.json` — reduced post-comparison question register.
- `scripts/compile_blind_reader_packet.py` — deterministic source → hashed-window compiler.
- `scripts/generate_editorial_gap_canvas.py` — diagnostic Canvas generator.

## Current next boundary

The blind comparison is complete. The remaining Obsidian-specific test is owner inspection of a reduced Canvas generated from `results/reduced-reader-gap-register.json`.

If the spatial view makes the unresolved cluster and distributed answers materially easier to understand, retain Obsidian as an optional editorial observatory. If the comparison table is equally usable, keep the reader-question method and remove the Obsidian dependency.
