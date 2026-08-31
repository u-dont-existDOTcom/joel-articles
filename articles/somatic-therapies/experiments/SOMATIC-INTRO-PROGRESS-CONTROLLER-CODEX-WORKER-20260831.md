# Somatic Introduction — progress-controller Codex worker contract

Updated: 2026-08-31
Status: **CURRENT MECHANICAL IMPLEMENTATION TASK / no prose authority**

## Role

You are the **mechanical implementation worker** for the Somatic Introduction external progress controller.

You are **not** the writer, verifier, editor, detector judge, or owner proxy. Do not write, rewrite, evaluate, rank, humanize, or repair article prose. Do not infer semantic quality. Reasoning/writing Chat and an independent reasoning verifier supply those judgments. Your job is to make their accepted progress mechanically persistent and fail closed when required evidence is missing.

## Repository and fresh read

Repository: `u-dont-existDOTcom/joel-articles`

Before implementation read fresh, in current canonical order:

1. `SKILL.md`
2. `CANONICAL-REPO-MAP.md`
3. `AGENTS.md`
4. `docs/INDEX.md`
5. `state/CODEX-CURRENT-STATE.md`
6. `articles/INDEX.json`
7. `articles/somatic-therapies/CURRENT-STATE.md`
8. `articles/somatic-therapies/experiments/SOMATIC-INTRO-CURRENT-MANUAL-TASK-20260831.md`
9. `articles/somatic-therapies/experiments/SOMATIC-MANUAL-HUMANIZATION-WRITER-STATE-20260831.md`
10. `articles/somatic-therapies/experiments/SOMATIC-INTRO-ACTIVE-LESSON-CONTRACT-20260831.md`
11. `articles/somatic-therapies/experiments/SOMATIC-INTRO-EXTERNAL-PROGRESS-CONTROLLER-20260831.md`

Do not infer current article state from chat, filenames, or old branches.

## Owner outcome

Implement the missing third layer in the humanization loop:

- generation may regress;
- independent verification may reject;
- **accepted progress must not regress or be forgotten** merely because a later writer ignores instructions.

The hard control is over **selection, promotion, and persistent state**, not over the LLM's raw generation.

A newer candidate is never automatically progress.

## Existing-work disposition

A bounded repository search found no obvious reusable frontier/promotion controller primitive under the relevant terms in `joel-articles`, `pangram-humanization-lab`, or `universal-dev-architecture`. Reuse ordinary repository validation/patterns where applicable, but do not spend this task inventing a broader orchestration framework.

Decision: **build a small article-scoped pilot with generic-enough deterministic primitives, then prove it before any universal promotion.**

## Required implementation

Create an article-scoped controller under a stable directory such as:

`articles/somatic-therapies/experiments/somatic-intro-progress-controller/`

and a deterministic Python helper under `scripts/` if needed.

The implementation must provide these durable objects.

### 1. Frontier state

Create a machine-readable frontier state with at least:

- schema/version;
- article id and exact scope (`# Introduction` only);
- current authoritative semantic-task identity/path/hash;
- current active-lesson-contract identity/path/hash;
- current best **promoted owner-facing candidate identity**, or null;
- optional retained nondominated alternatives, never owner-facing by default;
- semantic/provenance hard-constraint status;
- set of currently cleared lesson/dimension IDs;
- ranked unresolved defects;
- strongest known generative failure pattern;
- next bounded search target;
- last promotion receipt identity;
- append-only sample/adjudication history references.

The frontier must not be overwritten merely because a newer raw sample exists.

### 2. Raw-sample quarantine

Each raw writer output gets an immutable sample identity bound to exact SHA-256. Store or reference:

- candidate text identity/hash;
- writer/context identity if supplied;
- creation timestamp;
- current status: `QUARANTINED`, `ADJUDICATED`, `PROMOTED`, `RETAINED_ALT`, or `REJECTED`;
- verifier receipt identity/hash when adjudicated.

A raw candidate is disposable. It must not change the frontier until promotion succeeds.

Rejected prose may remain as historical evidence, but **must never be included automatically in the next-writer packet**.

### 3. Comparative verifier receipt

Define/validate a machine-readable verifier receipt containing at least:

- exact candidate SHA-256;
- exact current-frontier identity/hash used for comparison;
- exact active lesson-contract identity/hash;
- `hard_constraints`: `PASS|FAIL`;
- `regressions`: list of dimension IDs;
- `improvements`: list of dimension IDs/descriptions;
- `unresolved_defects`: ranked list;
- `strongest_blocking_defect`;
- `frontier_comparison`: `DOMINATES|NONDOMINATED|REGRESSES|INCOMPARABLE`;
- `next_search_target`: one bounded changed search operation;
- `promotion`: `ALLOW|BLOCK`;
- verifier identity/context marker sufficient to distinguish it from the writer when supplied.

Codex does not populate semantic judgments; it only validates and stores the receipt.

### 4. Promotion interlock

Mechanically allow replacement of the owner-facing frontier only when all of these are true:

- candidate hash matches the quarantined sample;
- verifier receipt is present and hash-bound to that sample and the current frontier;
- active task/lesson-contract hashes match current GitHub files;
- `hard_constraints == PASS`;
- `promotion == ALLOW`;
- `frontier_comparison == DOMINATES`, **or there is no existing promoted frontier**;
- no currently cleared dimension appears in `regressions`;
- required receipt fields are nonempty and schema-valid.

Fail closed otherwise.

`NONDOMINATED` or `INCOMPARABLE` may be retained as alternate evidence but must **not** silently replace the owner-facing frontier. An explicit Joel/Chat decision is required before accepting a tradeoff.

No timestamp, filename, branch order, model confidence, detector score, or recency may override this promotion gate.

### 5. Two packet builders

Implement deterministic packet generation for:

**Writer packet** — minimal generative context only:
- semantic/function authority for the Introduction;
- current cleared lesson dimensions as constraints;
- unresolved defect frontier;
- exactly one `next_search_target`;
- source-integrity prohibitions;
- **exclude rejected candidate prose and prior verifier rationales unless an explicit reasoning-Chat decision says a specific fragment is required.**

**Verifier packet** — comparative adjudication context:
- literal new quarantined candidate;
- current promoted frontier candidate if one exists;
- active lesson contract;
- semantic/function authority;
- exact hashes/identities;
- required comparative receipt schema.

Codex builds packets; it does not answer them.

### 6. Deterministic commands

Provide a minimal CLI or equivalent deterministic operations for at least:

- initialize/read frontier;
- register raw sample;
- emit writer packet;
- emit verifier packet;
- record verifier receipt;
- attempt promotion;
- show current frontier/status.

Names are implementation details. Do not create an unnecessary service/UI.

## Required tests

Add deterministic tests proving at minimum:

1. a newer rejected sample cannot replace the frontier;
2. a sample without a verifier receipt cannot be promoted;
3. candidate-hash mismatch blocks promotion;
4. stale task/lesson-contract identity blocks promotion;
5. `promotion=ALLOW` still blocks when a previously cleared dimension regresses;
6. `REGRESSES`, `INCOMPARABLE`, and `NONDOMINATED` do not replace the owner-facing frontier automatically;
7. a valid `DOMINATES` receipt promotes atomically;
8. a failed promotion leaves the previous frontier byte-for-byte/semantically unchanged;
9. next-writer packets exclude rejected candidate prose;
10. verifier packets include the exact candidate and current frontier identities needed for comparison;
11. missing required fields fail closed;
12. repeated registration/promotion is idempotent or explicitly conflict-safe rather than duplicating state.

Use synthetic placeholder candidate text in tests. Do not use or alter article prose for test fixtures unless the exact canonical task file is merely read as a hash-bound dependency.

## Hard boundaries

- Do **not** edit `articles/somatic-therapies/master.html`.
- Do **not** create a new Introduction candidate.
- Do **not** judge whether any prose looks Human or AI.
- Do **not** call Pangram or spend detector credits.
- Do **not** route article text to an external provider.
- Do **not** promote an article authority state.
- Do **not** treat Codex as the independent verifier.
- Do **not** silently choose tradeoffs between cleared dimensions.
- Do **not** build Mission Control, a general agent framework, or unrelated UI in this slice.

If an implementation choice requires semantic/editorial judgment, stop that choice and return the exact question to the reasoning Chat; continue all mechanically decidable work.

## Validation

Run the repository-required deterministic validation applicable to changed files, including at least:

- focused tests for the new controller;
- existing repository tests relevant to the changed paths;
- `python scripts/validate_content_repository.py --root .` if compatible with the branch state;
- `python scripts/audit_codex_github.py --root . --fail-on error`;
- `git diff --check`.

Do not claim a validator proves editorial correctness.

## Durable output

Commit the implementation on a task branch and push it. Do not merge without the normal review path.

Return a compact execution report containing:

- branch;
- commit SHA;
- files changed;
- exact commands/tests and pass/fail;
- controller invariants implemented;
- any unresolved mechanical blocker;
- the exact next reasoning-Chat handoff: **review the controller implementation before using it on a real candidate**.

Do not return article prose.