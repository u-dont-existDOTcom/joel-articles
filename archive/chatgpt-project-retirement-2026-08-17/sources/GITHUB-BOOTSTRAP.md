# Joel Articles GitHub Bootstrap — 4.13.0-candidate

This file exists only so a fresh ChatGPT Project chat knows where the current canonical material lives. **GitHub outranks this file whenever GitHub is accessible.**

## Canonical repositories

### Editorial/article repository
Private repository:

`u-dont-existDOTcom/joel-articles`

At the start of substantial work, use the connected GitHub tool/app and read:

1. `SKILL.md`
2. `CANONICAL-REPO-MAP.md`
3. the current article state/authority files named by that map
4. the minimum protocol files required by task mode

Never answer from an old Project Source copy when the current GitHub file is available.

### Detector repository
Private repository:

`u-dont-existDOTcom/pangram-humanization-lab`

For detector/humanization work, read fresh:

1. `README.md`
2. `state/WORKING-LESSONS.md`
3. the relevant case study under `state/`
4. the latest relevant `cases/<case-id>/history.json`, plan/review/stats as needed
5. `docs/CHATGPT-OPERATING-GUIDE.md` if present

Use commit history when necessary to identify the newest completed experiment. A commit such as `state: r01 analysis` means the durable results are already available in GitHub; open the changed history/analysis files rather than asking Joel to paste them.

## Task-mode loading matrix

Always start with `SKILL.md`, `CANONICAL-REPO-MAP.md`, current article state, and:

- **Any substantial article work:** `project-sources/MASTER-INSTRUCTIONS.md` + `project-sources/TASK-MODES.md`.
- **P2S/P3/P4, detector repair, humanization:** add `project-sources/HUMANIZATION-AND-COHERENCE.md`, `project-sources/EDIT-CONTRACT-AND-LEDGERS.md`, `project-sources/FINGERPRINT-PASS.md`, plus current promoted lessons/case study.
- **Research-heavy/contested claims:** add `project-sources/ARGUMENT-AND-EVIDENCE-ARCHITECTURE.md`; for allegations/contested public figures also `CONTROVERSIAL-TOPIC-EVIDENCE-AUDIT.md`.
- **Voice questions:** `project-sources/VOICE-REFERENCE.md`, `VOICE-LEXICON.md`, and relevant owner-final article prose. Provenance matters: detector-passing model-assisted prose is not automatically natural-human gold.
- **Substack source/publishing:** `INTERLINKING-AND-HTML-SOURCE.md`, `CONFIRMED-SUBSTACK-HELPER.json`, `TOOLING-IN-PROJECT-SOURCES.md`, and current raw editor HTML/article state.
- **Review packages:** `REVIEW-WORKFLOW-RULES.md`, `REVIEW-INTERFACE-SPEC.md`, `REVIEW-PACKAGE-REGRESSION.md`, plus the relevant scripts.

Do not load every file by default. Load the smallest set that preserves correctness.

## GitHub write policy

Durable changes belong in GitHub before claiming durable completion:

- owner-final/owner-corrected article prose;
- current article master/authority/provenance/status;
- promoted editorial/humanization lessons;
- material case-study findings;
- tooling/harness fixes;
- detector experiment state/results (in the Pangram repo).

Do not write ephemeral probes into article authority. Do not overwrite owner-final material with assistant candidates. Never commit secrets or API keys.

## Pangram operating boundary

The ChatGPT chat reads/writes GitHub; the local Pangram Humanization Lab performs paid Pangram API calls on Joel's machine. Before suggesting a new run, inspect GitHub cache/history so completed or pending measurements are not repeated.

Current harness invariants are documented in the Pangram repo and should be read fresh rather than trusted from memory. As of the 2026-08-12 repair, the proven path uses `x-api-key`, explicit `model: "pangram-4"`, terminal version `4.0`, task-id checkpointing before polling, content-addressed cache reuse, no automatic repost after ambiguous POST failure, and GitHub durability before another paid call.

When a local run finishes, its commits let a fresh chat inspect the experiment without log uploads. When it fails, debug from the durable task/result/cache records first; preserve already-paid results.

## Current high-value humanization lessons

Read the GitHub files for the full, current versions. The most important triggers are:

- semantic sanity before humanization;
- touch base with ordinary lived reality before abstract theory;
- strong claims are allowed when genuinely meant—do not flatten writing merely to avoid ever being wrong;
- overcompletion is functional, not quantitative;
- the next sentence must be the next necessary move in the thought, not an explanation of a point the reader already understood;
- necessary bridges can look explanatory and still belong;
- if downstream prose seems forced to repair an earlier paragraph, inspect upstream logic/stopping point;
- short detector samples are less reliable;
- Pangram findings require controlled full-boundary contrasts, interactions, nulls/counterexamples, and exact repeats rather than lexical superstition;
- good owner prose should be reused freely in production; use fresh syntax first only when explicitly testing model generation ability;
- if a cold audit identifies a real weakness, fix it before showing Joel unless preservation is explicitly justified.

## If GitHub is unavailable

Use the other Project Source, `EMERGENCY-FALLBACK.md`, only as a temporary behavioral fallback. Do **not** assume it contains current article state or current detector results. Say that GitHub could not be read before making claims about current authority/status, and resume from GitHub once access returns.
