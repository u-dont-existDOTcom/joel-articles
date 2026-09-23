# Humanization Fresh-Context Defect Audit Gate

Status: **BLOCKING** when fresh-model audit evidence is used before a paid Pangram call in Joel-byline humanization.

Use with `HUMANIZATION-COLD-AUDIT-GATE.md`, `project-sources/PRODUCTION-HUMANIZATION-PREFLIGHT.md`, the current post-generation tell library, and the preservation/architecture gates.

## 1. Role

Freshness solves only one problem: same-context contamination. It does **not** make a model a competent global Human/AI judge.

Do not ask one fresh critic to certify hidden authorship or emit a global `Human vs AI` verdict for production admission. That family failed to generalize across multiple blinded experiments.

Use fresh models as **specialized falsification auditors** for concrete observable defects. Each auditor asks one narrow question, cites exact spans, and stays inside its axis.

A narrow FAIL is a repair candidate. It is not proof of AI authorship.
A set of PASS results is not proof of Human authorship.

## 2. Packet

Give each applicable auditor:
- the literal target inside its natural reading boundary;
- enough accepted prose immediately before/after to judge that axis;
- heading/local purpose when relevant;
- only the instructions needed for that axis.

Withhold:
- detector scores/windows;
- prior defenses;
- preservation-unit ledgers and source-obligation checklists unless the axis specifically requires them;
- prior global Human/AI judgments;
- same-context reasoning about why the candidate should pass.

Context must be sufficient but not artificially clipped. Do not create a false orphan/continuity failure by withholding context the real reader has.

## 3. Current specialized audit axes

These are the initial production axes proven useful by the dangerous-present-adult debugging. They are not exhaustive.

### Reader-purpose / pragmatic act

Ask only:
- who is the visible reader here?
- what live question/pressure makes this passage necessary now?
- what practical or interpretive job does it perform for that reader?

FAIL when the passage silently switches audience/role, introduces a new decision with no visible reason, or requires inventing a clinician/evaluator/hypothetical-reader frame not established by the article.

### Antecedent / referent coherence

Audit only context-dependent references:
- quoted/metalinguistic terms;
- pronouns/demonstratives;
- explicit backward references;
- references to earlier prompts, wording, examples, or claims.

Distinguish:
- introduction/definition;
- explicit backward reference;
- bridging/generic reference;
- forward reference;
- self-contained use.

FAIL only when a **material explicit backward reference** lacks visible setup and the missing setup affects normal reading. Generic category language is not automatically orphaned.

Prefer controlled calibration where the same target is tested with and without the relevant antecedent.

### Cumulative instruction-manual / listicle cadence

Map consecutive speech-act/function beats.

FAIL only when the cumulative movement becomes a procedural/teaching staircase: several consecutive beats each perform one clean instructional/explanatory job, producing manual/checklist/listicle rhythm.

A list, imperative, rhetorical question, direct advice, concise explanation, or polished sentence alone is not a failure. Genuine enumeration of hypotheses/examples may be Human.

### Other narrow axes

Add another specialized auditor only when a concrete defect class is actually implicated and there is enough evidence to calibrate that question. Examples include explanatory aftercare/overclosure, abrupt audience/topic complication, or another owner-identified operation.

Do not turn every tell in the library into a mandatory model call.

## 4. Calibration

**Calibration labels are editorial defect judgments, not hidden authorship provenance.**

For each axis whose model result will affect detector admission:
1. use positive and negative controls for that exact defect;
2. prefer controlled context ablation/restoration or closely matched realizations when possible;
3. hide expected labels from the auditor;
4. include at least one known PASS and one known FAIL;
5. if a control is malformed or omits context the real reader would have, fix the experiment rather than teaching the model to reproduce the artifact;
6. if the auditor misses a control, its output for that axis is non-gating until repaired;
7. reuse a still-current calibration for the materially unchanged model/prompt/axis; do not rerun controls on every candidate.

Current project evidence in the Pangram lab, 2026-09-23:
- reader-purpose/pragmatic act: **2/2** seeded controls;
- cumulative instruction-manual/listicle cadence: **4/4** seeded controls, including Human list/advice counterexamples;
- corrected antecedent/referent coherence: **4/4** controlled cases.

These are scoped development results, not universal accuracy estimates.

### Retired global-judge calibration

Do **not** require or rely on a 20/20 hidden-authorship classifier.

The global-judge family failed to generalize:
- abstract provenance classifier v1: 14/20;
- hard scaffold-veto v2: 10/20;
- seven-pair absolute contrastive holdout v3: 10/20 after 11/12 development;
- matched pairwise realization-defect chooser: 5/8.

Those experiments are useful research evidence about method failure. They are not production admission gates.

## 5. Admission

There is no single `fresh-critic PASS`.

Fresh-audit admission requires:
- every **applicable calibrated axis** reports no unresolved FAIL;
- any model FAIL has been repaired or explicitly rejected as a false positive with an exact editorial reason;
- uncalibrated-axis model output is treated as advisory only;
- direct natural-boundary editorial reading still finds no substantive model-shape/coherence defect the editor actually believes;
- preservation and architecture/coherence gates pass separately.

Absence of narrow FAILs is not a completeness certificate. The editor must still ask the plain questions the model may miss.

For the dangerous-present-adult incident, unpaid review should have blocked before Pangram on at least three independently observable grounds:
- cumulative instruction-manual/listicle cadence;
- missing reader-purpose/pragmatic setup;
- the orphaned `“ask”` reference after removal of the source `voice / ask / answer` setup.

## 6. Failure handling

If a calibrated axis reports FAIL:
1. inspect the cited span and verify the defect editorially;
2. repair internally;
3. invalidate affected downstream gates;
4. use a new fresh context/request on changed bytes when model re-audit is needed;
5. do not spend Pangram while a substantive unpaid FAIL remains.

If the model result conflicts with direct owner/editorial evidence:
- owner/editorial authority controls;
- record the disagreement;
- update or retire the affected calibration control if needed;
- do not train the model by merely adding another global prohibition.

## 7. Research boundary

Hidden-authorship classification, broad Human/AI scoring, detector-passing stress sets, and pairwise global judges may still be studied in the Pangram lab.

They are detector/method research, not production certification.

Pangram remains downstream. It cannot rescue a failed unpaid editorial or specialized audit.
