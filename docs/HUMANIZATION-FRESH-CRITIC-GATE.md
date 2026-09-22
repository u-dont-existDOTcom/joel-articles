# Humanization Fresh-Critic Gate

Status: **BLOCKING** when a fresh model/context is used as pre-Pangram model-shape evidence in Joel-byline humanization.

Use with `HUMANIZATION-COLD-AUDIT-GATE.md`, `project-sources/PRODUCTION-HUMANIZATION-PREFLIGHT.md`, the current post-generation tell library, and the preservation/architecture gates.

## 1. Role

A fresh critic is a **falsification surface**, not a voting surface.

Its task is to find a reason the candidate is still model-shaped before detector admission. Positive Human-facing features never offset an unresolved AI-shaped operation.

Freshness addresses context contamination. It does **not** establish critic competence, sensitivity, or completeness.

## 2. Packet

Give the critic:
- the literal target candidate **inside its natural reading boundary**;
- enough accepted prose immediately before/after to judge continuity, antecedents, register, and section placement;
- intended reader;
- heading promise/local purpose;
- current post-generation tell rubric.

Withhold:
- prior candidate history;
- prior defenses;
- detector scores/windows;
- preservation-unit ledgers and source-obligation checklists;
- same-context reasoning about why the candidate should work.

`candidate + rubric` alone is invalid when the possible defect concerns audience, transition, antecedent, or section function.

## 3. Adversarial order

Before cataloguing Human-facing features, require the critic to make the strongest case that the prose is model-shaped.

It must inspect:
- local realization;
- paragraph/section topology;
- reader model: **who is this talking to?**
- live reader pressure: **why does this matter now?**
- antecedents/referents;
- cumulative instruction-manual/listicle cadence;
- one-clean-teaching-job-per-beat / optimal semantic efficiency;
- abrupt complication;
- checklist/taxonomy flow;
- explanatory aftercare;
- source/requirements ledger made reader-visible.

### Content-neutralized scaffold test

Before crediting vivid detail, self-talk, humor, metaphor, direct reader address, unresolvedness, first person, strong opinion, or another Human-looking device, mentally replace topic nouns, names, doctrines, therapies, objects, and examples with placeholders and reduce each sentence/beat to its function.

If the remaining passage is still an unusually clean semantic staircase—such as setup -> qualification -> example -> distinction -> verdict, command -> exception -> contingency, or problem -> taxonomy -> synthesis—the surface device does **not** rehabilitate it merely because it is concrete, apt, emotionally plausible, or source-grounded.

A model can deliberately simulate:
- concrete reaction and self-talk;
- relevant-seeming authorial judgment;
- unresolved endings;
- reader recognition/social address;
- sustained metaphor;
- colloquial friction.

Count a Human-facing feature against the AI hypothesis only when it creates **Human surplus** that materially disrupts the optimized scaffold: unnecessary-but-real context dependence, uneven attention not optimized for instruction, unresolved social residue, authorial partiality beyond the passage's thesis, recurrence/digression with a separate lived function, or non-interchangeable detail that changes more than delivery of the lesson.

Purpose-built concreteness can skin a staircase. Engineered unresolvedness can also be part of a staircase. If every vivid element maps neatly to one teaching obligation, that mapping is AI-shape evidence rather than Human evidence.

## 4. Mixed aggregation

A finding does not become nonblocking merely because it is individually labelled `mixed`.

Before PASS, aggregate mixed findings at paragraph/section scale. If several features combine into a known model-shaped operation, the aggregate is blocking even when each feature could occur naturally by itself.

Human-facing features are recorded separately. They do not cancel AI-shape.

## 5. Candidate dispositions

Before PASS, disposition the three strongest credible AI-shape candidates, or all if fewer than three:

- `REPAIR`
- `PRESERVE-EXACT-REALIZATION-WITH-SPECIFIC-REASON`
- `NOT PRESENT`
- `UNRESOLVED`

`UNRESOLVED` blocks.

**Protected meaning/function is never by itself a reason to preserve current wording, cadence, paragraph topology, or another realization choice.** A preserve disposition must explain why the exact realization—not merely the cognition—is required by owner wording, quotation/provenance, safety, architecture, evidence, or genre.

## 6. Two-sided critic calibration

A non-detection can gate only when the critic configuration has current evidence of both specificity and sensitivity.

The one-good/one-bad pair is a **smoke test only**, not sufficient general calibration.

For the current Joel-byline humanization critic, a materially changed rubric/provider/model configuration must also pass a frozen **20-item blinded provenance holdout at 20/20** before its non-detection can function as a production Pangram-admission gate. Treat 20/20 as a starting calibration threshold, not proof of universal authorship detection.

Benchmark rules:
1. use balanced, provenance-secure Human and AI passages in the relevant Joel registers;
2. `HUMAN` ground truth comes from natural/unaided owner provenance or other explicit Human authorship, not Pangram status;
3. `AI` ground truth comes from explicit model provenance even when Pangram happened to classify the passage Human;
4. freeze passages, labels, prompt, shuffle/order, and hashes before the first classification response;
5. hide provenance, labels, detector results, prior judgments, and neighboring benchmark answers from the critic;
6. if the rubric is changed after seeing an error, that set becomes development data permanently. A later 20/20 validation claim requires a **new untouched holdout**;
7. keep Pangram-passing model prose as a useful detector-disagreement stress set, but never let Pangram passing redefine it as Human ground truth.

Do not reveal labels, provenance, or detector status to the critic.

Accepting Human controls alone proves only that the critic can avoid overcalling AI. It does not show adequate sensitivity to model prose. Missing any known-AI holdout means its target non-detection is **non-gating evidence**.

Reuse a still-current successful holdout result for the same materially unchanged critic configuration; do not rerun the benchmark on every candidate.

Current small regression fixtures and expected classifications are in `HUMANIZATION-AUDIT-ADMISSION-REGRESSION-20260922.md`. Versioned larger benchmark evidence lives in the Pangram humanization lab.

## 7. Admission

`no definite AI tells` is not an admission result.

Fresh-critic PASS requires all of:
- no unresolved credible AI-shape candidate;
- no cumulative mixed pattern;
- content-neutralized functional-skeleton check passes;
- any claimed Human-facing signal provides Human surplus that **materially breaks** rather than merely decorates the model-shaped scaffold;
- reader-model check passes;
- why-now check passes;
- antecedent/referent check passes;
- the current materially unchanged critic configuration has passed the required blinded provenance calibration.

A PASS here still does not prove human authorship. Continue separately through preservation, architecture/cold-read, final preservation, and Pangram in the normal order.

## 8. Failure handling

If the critic finds a blocking issue:
1. repair internally;
2. invalidate affected downstream gates;
3. use a new genuinely fresh context/request on the repaired target;
4. do not spend Pangram until this gate and the remaining non-detector gates pass.

If the same failure class recurs despite materially similar repairs, apply the strategy-efficacy rule and change architecture rather than adding another local prohibition.
