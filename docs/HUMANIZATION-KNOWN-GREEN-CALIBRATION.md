# Humanization known-green calibration guard

Status: **ACTIVE.** Direct owner workflow correction, 2026-08-23.

Use this with `HUMANIZATION-PRESERVATION-GATE.md`, `HUMANIZATION-ARCHITECTURE-GATE.md`, and `project-sources/PRODUCTION-HUMANIZATION-PREFLIGHT.md`.

## Problem this guard prevents

A detector/humanization worker can learn valid patterns from prior AI passages—balanced explainer voice, paired caveats, miniature conclusions, source ladders, taxonomy/checklist structure, recursive mini-essays—and then start treating those patterns as a reliable authorship classifier.

That is unsafe.

A passage can contain one of those shapes and still be exact detector-Human. Conversely, a rewrite designed to remove those shapes can become more detector-AI. Humanization heuristics are hypotheses about editorial/model behavior, not a substitute detector.

## Known-green boundary rule

When an exact natural boundary has already measured Pangram Human and its byte identity is known:

1. treat that exact passage as a **calibration anchor**;
2. do not reopen it for detector reasons merely because it resembles a learned AI-shape pattern;
3. an offline audit may still identify a real editorial defect—bad logic, redundancy, weak flow, genericness, false balance, unnecessary qualification, provenance/fidelity loss, or poor voice—but name that defect directly;
4. distinguish `I think this reads worse` from `I predict Pangram will call this AI`;
5. if there is no concrete editorial/fidelity defect, preserve the known-green wording.

`Looks AI to me` is not rewrite authority against exact recent Human evidence.

## Reversion rule for detector-green rewrites

Canonical registration authority and prose quality are separate dimensions.

If the registered master contains older wording and a preservation-proved working rewrite is exact detector-Human, do **not** revert to the registered wording merely because the rewrite has not yet been promoted to canonical authority.

During owner reconciliation:

- keep the detector-green working rewrite when it is faithful and at least as good editorially;
- revert only when the older wording is materially better for meaning, voice, flow, evidence, or article function **and** detector safety for the rollback is affirmatively known or deliberately re-established before treating it as the better production candidate;
- direct owner / owner-final corrections still outrank both versions;
- canonical `main` remains unchanged until deliberate reconciliation updates the registered article family.

This prevents an authority-safe rollback from silently becoming the new humanization baseline.

## Calibration failure protocol

If a worker calls known-green prose `AI-shaped`, rewrites it, and the rewrite performs materially worse on the detector:

1. reject the rewrite as a humanization improvement;
2. preserve the original known-green text as the detector baseline;
3. record the failed diagnostic hypothesis;
4. weaken or narrow the implicated heuristic rather than treating the detector failure as noise by default;
5. compare what the rewrite changed at the level of thought movement, stance, cadence, abstraction, explanation, and author-specific pressure;
6. do not spend additional production calls trying to rescue the failed rewrite unless there is an independent editorial reason to keep it.

## Romance calibration incident — 2026-08-23

Exact Romance r22 evidence:
- Part 1: Pangram 4.0 Human `1.0`, zero AI windows;
- retained Part 2: Pangram 4.0 Human `1.0`.

During subsequent canonical reconciliation, the assistant reverted several r22 rewrites because registered wording had higher authority, then subjectively labeled six resulting/restored boundaries `AI-shaped` and drafted new holistic repairs.

Joel tested the concatenated six proposals in Pangram 4.0:
- 2,347 words;
- 59.5% AI Generated;
- 40.5% Human Written;
- multiple high-confidence AI runs, including a 550-word run across rewritten spiritual-practice / `Not A Performance` / `Two Pillars` material and a 392-word run covering essentially the rewritten `After leaving` section.

The incident shows two distinct errors:

1. **authority/prose conflation** — registered canonical wording was treated as the default editorial fallback even though the r22 working realization was already preservation-proved and detector-green;
2. **heuristic overreach** — useful AI-shape lessons were treated as a classifier, causing exact Human prose to be misdiagnosed and replaced with materially more AI-classified prose.

The correction is not `trust Pangram over editing`. Human editorial quality and fidelity still outrank detector score. The correction is narrower: **do not claim detector likelihood from stylistic theory when exact detector evidence already says otherwise.**

## Pre-call implication

The production preflight question `Would an AI result genuinely surprise me?` must be interpreted against available evidence.

For unmeasured/red prose, editorial AI-shape diagnosis can help decide whether a call is premature.

For exact known-green prose, the existing measurement is the calibration baseline. A worker may revise for real editorial reasons, but the revision itself becomes the unmeasured candidate. Do not destroy the known-green baseline merely to satisfy a subjective sense of what Human prose `should` look like.
