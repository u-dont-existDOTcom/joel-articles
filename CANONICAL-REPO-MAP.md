# Canonical repository map

This file is the fast loader for ChatGPT and other workers. It does not replace `articles/INDEX.json`, `AGENTS.md`, or article-local authority.

## Current repository status

- Repository: `u-dont-existDOTcom/joel-articles`
- Default branch: `main`
- Current content posture: active governance + editorial skill/tooling home with registered article authority.
- Article authority: `articles/INDEX.json` currently registers **Romance** as a working canonical article. For Romance, follow its registered current-state/master/locks/evidence read order and exact hashes; historical Pangram branches are provenance, not competing authority.

## Always read for substantial work

1. `SKILL.md`
2. `AGENTS.md`
3. `docs/INDEX.md`
4. `state/CODEX-CURRENT-STATE.md`
5. `articles/INDEX.json`
6. the target article's registered current state/master/locks/evidence if and only if the registry contains that article

## Task-specific active sources

Load the least set that covers the task. The source families below are active
routing aids; they do not establish article authority.

### Any substantial article work

- `project-sources/MASTER-INSTRUCTIONS.md`
- `project-sources/TASK-MODES.md`

### P2S/P3/P4, detector repair, and humanization

- `project-sources/HUMANIZATION-AND-COHERENCE.md`
- `project-sources/RHYTHM-AND-THOUGHT-SHAPE.md`
- `project-sources/EDIT-CONTRACT-AND-LEDGERS.md`
- `project-sources/FINGERPRINT-PASS.md`
- `project-sources/IDIOLECT-PRESERVATION-PROTOCOL.md`
- `project-sources/BANNED-PATTERNS.md`
- the relevant current material in `u-dont-existDOTcom/pangram-humanization-lab`,
  following the fresh-read order in `SKILL.md`

Use the rhythm/thought-shape protocol to audit sentence-level verdict cadence, paragraph-level equalized thought duration, recursive mini-essay closure, objection-completion, and lost reader-facing pragmatic acts. It is an editorial gate, not a phrase blacklist or detector substitute.

Use the idiolect protocol for substantial sectional reconstruction or article-wide rewriting. It adds authorship-signal retention as a separate axis; it never replaces semantic fidelity, architecture, owner authority, or Pangram's exact-boundary gate.

### Research-heavy or contested argument work

- `project-sources/ARGUMENT-AND-EVIDENCE-ARCHITECTURE.md`
- `project-sources/ARGUMENT-LEDGER-QUICKSTART.md` when threshold-triggered
- `project-sources/CONTROVERSIAL-TOPIC-EVIDENCE-AUDIT.md` when relevant
- `project-sources/FACTS-HEALTH-FORMATTING.md` for factual and health sourcing rules
- `project-sources/argument_ledger.py.txt` when the argument-ledger tooling is needed

### Voice and corpus

- `project-sources/VOICE-REFERENCE.md`
- `project-sources/VOICE-LEXICON.md`
- `project-sources/cancer-and-research-samples.txt`
- `project-sources/community-before.txt`
- `project-sources/tender-video-transcript.txt`

Use corpus material by its documented provenance and function, never as factual
authority. For idiolect measurement, also enforce the corpus-authority, genre-match, holdout, contamination, and privacy rules in `project-sources/IDIOLECT-PRESERVATION-PROTOCOL.md`.

### Artifact families and review packages

- `project-sources/REVIEW-WORKFLOW-RULES.md`
- `project-sources/REVIEW-INTERFACE-SPEC.md`
- `project-sources/REVIEW-PACKAGE-REGRESSION.md`
- `project-sources/QUALITY-FORECAST-AND-PASS-REVIEW.md`
- `project-sources/ARTIFACT-FAMILY-LEDGER-TEMPLATE.md`
- `project-sources/COMMENT-RESOLUTION-LEDGER-TEMPLATE.md`
- `project-sources/PROJECT-STATE-TEMPLATE.md`
- `project-sources/review_package.py.txt`
- `project-sources/interactive_review.py.txt`
- `project-sources/review_interface_browser_test.py.txt`
- `project-sources/review_interface_template.html.txt`
- `project-sources/html_diff.py.txt` — optional quick static diff only; never substitutes for the interactive review

### Substack and publishing

- `project-sources/INTERLINKING-AND-HTML-SOURCE.md`
- `project-sources/CONFIRMED-SUBSTACK-HELPER.json`
- `project-sources/html_islands.py.txt`
- `project-sources/substack_transfer_helper.py.txt`
- `project-sources/html_publish_modes.py.txt`
- `project-sources/interactive_review.py.txt`
- `project-sources/review_interface_browser_test.py.txt`
- `project-sources/review_interface_template.html.txt`
- `project-sources/VISUAL-EDITORIAL-PROTOCOL.md`
- `project-sources/TOOLING-IN-PROJECT-SOURCES.md`
- video regression tests under `tests/`

The same-named current publishing helpers above supersede their historical
4.11.1 copies where the recovery manifest says so. In particular, retain the
current native-uploaded-video and video-post distinction.

The checked-in helper authorities are the `project-sources/*.py.txt` files.
Protocol commands using a plain `.py` filename describe an exact runtime
materialization. In particular, route restored references to the nonexistent
`scripts/html_islands.py` through the current
`project-sources/html_islands.py.txt`, materialized as `html_islands.py` only
when the tool is needed.

### Interlinking, recurring facts, naming, and links

- `project-sources/ARTICLE-INDEX.md` — publication/interlink working index
- `project-sources/CANON-FACTS.md` — current recurring-facts source
- the registered article's current authority files when one exists

Never confuse `project-sources/ARTICLE-INDEX.md` with `articles/INDEX.json`.
Only `articles/INDEX.json` is the canonical repository-wide article-authority
registry.

## Article-local authority once imported

`articles/INDEX.json` is the only repository-wide article registry. For a registered article, follow `docs/CONTENT-AUTHORITY-AND-IMPORT.md` and that article's current-state read order. Article-local authority, exact hashes, owner locks, evidence, architecture map, detector records, and publication provenance outrank generic skill files.

## Historical Project retirement archive

The exact pre-cutover ChatGPT Project instruction block, exact ten Project Source files, source hashes, local migration ledger, and owner-final native-video correction are preserved under:

`archive/chatgpt-project-retirement-2026-08-17/`

The exact 4.11.1 forty-source historical baseline is preserved under:

`archive/project-source-snapshots/4.11.1/`

Those files are historical evidence only. Active work uses the root skill/map and current `project-sources/` files.

## Conflict rules

- Joel's current direct correction beats repository text and must then be made durable.
- Registered article authority beats generic project protocols on article-specific state/content.
- Current `project-sources/` beats archived Project copies.
- Repository governance beats remembered chat/process assumptions.
- Pangram output never outranks article meaning, owner authority, or architecture.
- Idiolect-retention output never proves authorship or authorizes changing owner-final prose.
- If two plausible article masters compete and the registry does not resolve them, stop for an owner decision instead of merging by inference.
