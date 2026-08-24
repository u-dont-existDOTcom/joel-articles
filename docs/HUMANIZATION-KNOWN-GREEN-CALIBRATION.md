# Humanization known-green calibration guard

Status: **ACTIVE.** Direct owner workflow correction, 2026-08-23; function-first feature-recovery correction added 2026-08-24.

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

## Reconciliation rule for older vs known-green wording

Canonical registration authority and prose quality are separate dimensions.

If the registered master contains older wording and a preservation-proved working rewrite is exact detector-Human, do **not** revert to the registered wording merely because the rewrite has not yet been promoted to canonical authority.

During owner reconciliation:

- keep the detector-green working rewrite as the **baseline realization** when it is faithful;
- compare the older/canonical realization anyway for anything it did materially better: sharper claim, clearer logic, stronger transition, better example, useful qualification, stronger joke/image, more precise evidence framing, better rhythm, better setup/payoff, or a distinctive owner thought/voice feature;
- record every such **feature deficit** in the green version explicitly, even when the older wording itself is detector-AI or detector-unknown;
- present meaningful feature deficits to Joel for an owner decision instead of silently throwing them away or automatically restoring the old passage;
- a good feature may be transplanted or freshly re-realized without reverting the whole older passage;
- detector safety is required for the **resulting wording**, not for the abstract idea/feature merely to be considered valuable;
- if the old wording itself is proposed for verbatim rollback, treat that wording as a newly changed detector boundary unless exact current detector evidence already covers it;
- direct owner / owner-final corrections still outrank both versions;
- canonical `main` remains unchanged until deliberate reconciliation updates the registered article family.

This prevents two opposite errors: treating canonical age/authority as proof that old prose is better, and treating detector-Human status as proof that the new prose has nothing left to learn from the old version.

## Function-coverage gate before any transplant

A diff proves that wording changed. It does **not** prove that a rhetorical or semantic function was lost.

Before proposing any older sentence, paragraph, joke, qualification, example, transition, evidence frame, or other feature for reinsertion:

1. **Decompose the older span into separate functions.** Do not treat a paragraph as one indivisible feature. Identify each claim, example, qualification, joke, transition, evidence role, diagnostic, setup/payoff, and reader-facing move separately.
2. **Inspect the complete current natural section for every function.** Also inspect adjacent or linked sections when the function is article-wide or may have been deliberately relocated. Search by meaning, not phrase matching. A function may now live inside a concrete story with none of the old vocabulary.
3. **Classify current coverage** for each old function as `absent`, `partial`, `equivalent`, or `stronger/more concrete`. Quote or identify the exact current realization when the function survives.
4. **Recover only the unresolved remainder.** If an old three-sentence block contains three functions and the current section already carries two, do not propose the whole block. Propose only the missing third function.
5. **Prefer the smallest integration that fits the current thought movement.** Historical prose is a feature source, not an insertion source. Exact old wording is optional even when the underlying feature is valuable.
6. **Cold-read the literal resulting paragraph and complete natural section before delivery.** Check whether the addition duplicates a conclusion, explains what the story already demonstrates, breaks sequencing, creates a generic summary layer, or answers no live reader question.
7. **Check durable detector history before recommending verbatim historical prose in a known-green boundary.** Detector history never decides editorial value, but already-paid evidence must not be ignored when presenting exact reuse as a recommendation.

No feature-recovery recommendation is complete until this gate has been performed. Phrase absence must never be equated with function absence.

### Romance `Two Pillars` incident — function-level example

An older three-sentence mutual-friends block carried three distinct functions:

1. mutual friends may notice a pattern neither partner sees;
2. someone else may help or comfort a partner when the other partner has become the wrong person to do it;
3. people who know both partners can reality-check a one-sided account against the person they know.

The detector-green r22 section already carried functions 2 and 3 more concretely through the B. and H. material. Only function 1 was actually missing. Proposing the entire old block therefore duplicated two functions and reintroduced generic explanatory prose. The correct recovery target was the one missing function only.

Joel's preferred review wording for that remainder was:

`But sometimes a friend who actually knows us both sees the pattern before either of us does.`

This is the model for future reconciliation: **map function coverage first; recover only what is truly absent.**

### Required feature-deficit report

For every substantive older→known-green rewrite being reconciled, record:

```text
Current green realization: <identity / span>
Older realization: <identity / span>
Meaning/fidelity: equal / changed / unresolved
Old functions: <enumerated rhetorical/semantic functions>
Current coverage by function: <absent / partial / equivalent / stronger, with current locations>
What green does better: <specific advantages>
What old does better after function-coverage check: <specific recoverable advantages, or none>
Genuinely missing remainder: <only functions not already realized>
Recommended disposition: keep green / transplant missing function / owner choice / rollback candidate
Literal integration cold-read: pass / fail + reason
Detector implication: known-green baseline preserved; any changed wording requires appropriate re-certification
```

Do not use `old is AI` as a reason to suppress a genuinely better feature from the report. Do not use `new is Human` as proof that every editorial choice in it is superior. Do not use lexical difference as proof that a function disappeared.

## Calibration failure protocol

If a worker calls known-green prose `AI-shaped`, rewrites it, and the rewrite performs materially worse on the detector:

1. reject the rewrite as a humanization improvement;
2. preserve the original known-green text as the detector baseline;
3. record the failed diagnostic hypothesis;
4. weaken or narrow the implicated heuristic rather than treating the detector failure as noise by default;
5. compare what the rewrite changed at the level of thought movement, stance, cadence, abstraction, explanation, and author-specific pressure;
6. also inspect whether the failed rewrite was trying to recover a legitimately better feature from an older version; if so, preserve that feature as an editorial requirement and seek a different realization rather than discarding the feature;
7. do not spend additional production calls trying to rescue the failed rewrite unless there is an independent editorial reason to keep it.

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

Joel then added a third correction: an older detector-AI or detector-unknown version may still contain **better editorial features**. Reconciliation must surface those features rather than choosing one whole version solely by detector status.

The 2026-08-24 `Two Pillars` correction added a fourth: **feature discovery must be function-level, not sentence-level.** An old sentence can look absent in a diff while its job is already performed elsewhere in the current section. Blindly transplanting the old wording can create redundancy even when the underlying old feature was genuinely valuable.

The correction is not `trust Pangram over editing`. Human editorial quality and fidelity still outrank detector score. The correction is narrower: **do not claim detector likelihood from stylistic theory when exact detector evidence already says otherwise, do not let detector status erase useful editorial information from competing versions, and do not mistake wording difference for functional loss.**

## Pre-call implication

The production preflight question `Would an AI result genuinely surprise me?` must be interpreted against available evidence.

For unmeasured/red prose, editorial AI-shape diagnosis can help decide whether a call is premature.

For exact known-green prose, the existing measurement is the calibration baseline. A worker may revise for real editorial reasons, but the revision itself becomes the unmeasured candidate. Do not destroy the known-green baseline merely to satisfy a subjective sense of what Human prose `should` look like.
