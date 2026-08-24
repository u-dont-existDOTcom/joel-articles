# Owner correction — known-green recalibration — 2026-08-23

Status: **direct owner correction; supersedes the prior subjective AI-shape audit as a reason to reopen r22 prose.**

## Owner correction

Joel's correction after reviewing the reconciliation work:

- r22 had already reached exact Pangram 4.0 Human `1.0` on Part 1 and exact Human `1.0` on the retained Part 2;
- the assistant then decided several already-green r22/canonical-comparison passages `looked AI`, rewrote them, and Joel tested the resulting six-proposal bundle;
- that rewrite tested substantially **more AI**, not less;
- therefore the assistant's pattern-based `AI-shape` intuition was miscalibrated and may not override exact known-green detector evidence;
- reverting a detector-green rewrite merely because canonical wording has higher registration authority is not an editorial reason to prefer the canonical wording. Registration authority and prose quality are separate questions.

Owner reconciliation rule going forward:

> When a current preservation-proved working rewrite is already exact detector-Human, keep it as the leading working prose unless the older/canonical wording actually reads better **and** is detector-safe. Do not revert simply because the rewrite was assistant-produced or had not yet been promoted to canonical `main`.

Canonical promotion still requires owner reconciliation and preservation/authority bookkeeping. This rule changes which prose remains the **leading working candidate** while that reconciliation happens; it does not silently merge task prose into `main`.

## Exact r22 evidence already durable

Task handoff:
`task/romance-detector-repair-20260820:work/romance-detector-repair-20260820/CODEX-HANDOFF.md`

r22:
- Markdown SHA-256 `f0f9a47eba2ac9ab1a56bdd6793316d41e7c23072b0b0c030285caf5e12f83c9`;
- Part 1 SHA-256 `5ed333800b9ae7b402f26aa03e751ef8296c7e27ab70e39bc39bb9896b23e62d`, Pangram 4.0 Human `1.0`, AI `0.0`, AI-assisted `0.0`, zero residual AI windows;
- retained Part 2 SHA-256 `9e4c6a522c95741c7dfc9e040b2dcc40773427cbc0aef8f45211de77208b0c85`, Pangram 4.0 Human `1.0`.

The task handoff explicitly says not to reopen settled/remote passages merely because an older aggregate once highlighted them.

## Owner-supplied test of the six assistant `holistic repair` proposals

Source: owner-supplied Pangram 4.0 PDF report, 2026-08-23, on the concatenated six proposed rewrites.

Report boundary:
- 2,347 words;
- Pangram 4.0;
- overall **59.5% AI Generated**;
- **40.5% Human Written**;
- headline: mixed AI/human content.

The report includes multiple high-confidence AI runs, notably:
- 62-word high-confidence AI block in the rewritten `window of clarity` attachment explanation;
- 126-word high-confidence AI block across the rewritten interview/fantasy/ordinary-life explanation;
- 550-word high-confidence AI block spanning the rewritten spiritual-practice tail, `Not A Performance`, and beginning of `Two Pillars`;
- additional AI/AI-assisted blocks through `Two Pillars` and `What are you actually choosing together?`;
- 392-word high-confidence AI block covering essentially the rewritten `After leaving` section.

This test **rejects** `HOLISTIC-REPAIR-PROPOSALS.md` as a humanization improvement and falsifies the audit claim that those rewrites contained `no remaining model-shape problem`.

## Recalibrated interpretation

The prior audit overgeneralized real detector/editorial lessons into a style classifier. Terms such as `balanced`, `explainer`, `therapy voice`, `paired caveat`, `taxonomy`, `source ladder`, or `mini-essay` remain useful hypotheses when a passage is actually weak or detector-red. They are **not sufficient evidence that exact detector-green prose is AI-like**.

A subjective audit may still identify real editorial defects in a detector-green passage: bad logic, redundancy, poor flow, weak voice, false balance, unnecessary qualification, or loss of owner meaning. If so, name the editorial defect directly. Do not convert that judgment into an unsupported prediction that Pangram will call the prose AI.

### Known-green calibration guard

Before rewriting text whose exact natural boundary is already Pangram Human:

1. treat that exact text as a calibration anchor, not as an unmeasured suspect;
2. require a concrete editorial/fidelity defect independent of detector theory;
3. distinguish `I dislike this sentence` from `this looks AI`;
4. if an older version is proposed as a rollback, require that it actually reads better and that its detector safety is known or deliberately re-established before treating it as the better production candidate;
5. if a supposed humanizing rewrite performs materially worse than the known-green source, reject the rewrite and recalibrate the heuristic rather than blaming detector noise by default.

## Reconciliation consequence

The exact r22 candidate returns to **leading working-candidate status**. The conservative canonical-heavy hybrid remains useful as a provenance/authority comparison artifact, but it is not the prose baseline for further humanization.

The six holistic proposals are rejected. No Pangram call should be spent repairing r22 merely because of the superseded subjective audit.
