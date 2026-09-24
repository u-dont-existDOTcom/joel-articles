# Humanization Fresh-Context Defect Audit Gate

Status: **BLOCKING** when fresh-model audit evidence is used before a paid Pangram call in Joel-byline humanization.

Use with `HUMANIZATION-COLD-AUDIT-GATE.md`, `project-sources/PRODUCTION-HUMANIZATION-PREFLIGHT.md`, the current post-generation tell library, and the preservation/architecture gates.

## 1. Role

Freshness solves only one problem: same-context contamination. It does **not** make a model a competent global Human/AI judge.

Do not ask one fresh critic to certify hidden authorship or emit a global `Human vs AI` verdict for production admission. That family failed to generalize across multiple blinded experiments.

Use fresh models in two layers:

1. **global tell-ledger sweep** — inspect the complete current tell catalog in one pass and return one PRESENT / ABSENT / UNCERTAIN row per tell, with exact evidence and no global Human/AI verdict;
2. **specialized falsification audits** — ask one narrow question for a tell or coherent tell-family when the global sweep returns PRESENT/UNCERTAIN, when the tell is high-risk, or when direct editorial review still disputes the result.

**Neither layer replaces or shortens the full Human-facing tell catalog.** The full post-generation tell ledger remains the master audit: every applicable known AI-shaped operation/tell must still receive an explicit disposition on the literal candidate. If an applicable catalog tell has no reliable model check yet, it remains a manual/editorial blocking check rather than silently disappearing from the gate.

Current bounded evidence favors **Claude Opus 5.5** as the full-ledger sweep model. UDA routing applies first: use an already-authenticated provider-native Claude Code CLI when it can provide the required model/effort/output/isolation; use OpenRouter only as an authorized fallback or when provider/API behavior itself is the evidence target.

The two provider surfaces have now been calibrated separately.

**Claude Code CLI:** on the frozen six-case / twelve-cell benchmark, medium scored 9/12 with 3 UNCERTAIN and 0 wrong-polarity calls; high scored 10/12 with 2 UNCERTAIN and 0 wrong polarity in two independent runs; xhigh scored 10/12 with 2 UNCERTAIN and 0 wrong polarity while using materially more thinking tokens and latency. Therefore **high is the current CLI efficiency target for the global sweep**. This does not make high a sole clearing authority: a later T01/T10/T11 development holdout exposed under-calibrated tell logic/controls, so PRESENT/UNCERTAIN and under-calibrated tell families still require narrow or direct editorial resolution.

**OpenRouter fallback:** xhigh scored 11/12 and 10/12 across two runs with 0 wrong-polarity calls at roughly $0.45–$0.48 per six-case run; max scored 11/12 with 0 wrong polarity at roughly $3.00. Thus OpenRouter uses xhigh routinely and max only for decision-changing unresolved/disputed tells.

Treat UNCERTAIN as unresolved, never as ABSENT.

TypeSafe Jev may be used only as optional **positive triage**. On the current twelve scored cells it caught 6/9 known defects, left all 3 known-negative controls ABSENT, and all 6 Jev PRESENT calls were correct; its three errors were confident false ABSENTs. Reported cost was about $0.00073 across six 12-tell cases (~$0.00012 per candidate), with sub-second to ~1.5 s latency per case. A Jev PRESENT can therefore surface an already-blocked candidate cheaply before a slower Opus sweep, but this saving has not yet been measured prospectively. A Jev ABSENT cannot clear a tell and Jev cannot override Opus, a calibrated narrow audit, or direct editorial judgment.

A narrow FAIL is a repair candidate. It is not proof of AI authorship.
A set of PASS results is not proof of Human authorship, and it cannot clear tell families that were not audited.

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

## 3. Global sweep protocol

For the preferred high-rigor sweep:
- use a genuinely fresh stateless request;
- use the literal natural reading boundary plus enough context for the tell definitions to be meaningful;
- supply the complete current tell inventory;
- require every tell ID exactly once;
- require PRESENT / ABSENT / UNCERTAIN plus minimal exact evidence;
- prohibit an overall Human/AI classification;
- do not allow Human-looking features to cancel a tell that is actually present;
- do not force a tell merely because another tell is present or because the prose is model-authored;
- treat any missing row, malformed row, PRESENT, or UNCERTAIN as unresolved.

When Opus 5.5 is used, set an explicit reasoning effort on the selected route rather than assuming `temperature=0` implies the desired effort. **Do not transfer effort calibration across surfaces.** For OpenRouter fallback, current evidence supports xhigh routinely and max only when an xhigh uncertainty/dispute is consequential enough to justify the extra cost/latency. For Claude Code CLI, current evidence supports high as the routine efficiency target; xhigh did not improve the frozen benchmark enough to justify its extra thinking/latency. Escalate tell-by-tell only when a high-effort uncertainty/dispute can change the decision.

The global sweep is an execution aid, not a completeness certificate. Direct editorial review remains responsible for noticing defects outside the current catalog.

## 4. Current specialized audit axes

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

## 5. Calibration

**Calibration labels are editorial defect judgments, not hidden authorship provenance.**

For each axis whose model result will affect detector admission:
1. use positive and negative controls for that exact defect;
2. prefer controlled context ablation/restoration or closely matched realizations when possible;
3. hide expected labels from the auditor;
4. include at least one known PASS and one known FAIL;
5. if a control is malformed or omits context the real reader would have, fix the experiment rather than teaching the model to reproduce the artifact;
6. if the auditor misses a control, its output for that axis is non-gating until repaired;
7. reuse a still-current calibration only for the materially unchanged axis/model/prompt/provider configuration; do not rerun controls on every candidate.

Current project evidence in the Pangram lab, 2026-09-23:
- reader-purpose/pragmatic act: **2/2** seeded controls;
- cumulative instruction-manual/listicle cadence: **4/4** seeded controls, including Human list/advice counterexamples;
- corrected antecedent/referent coherence: **4/4** controlled cases.

These are scoped development results, not universal accuracy estimates.

### Current full-ledger rubric-development boundary — 2026-09-24

A first attempt to make the global rubric more explicit by expanding every tell into gates/subtests **failed** a new T01/T10/T11 development holdout and cost more tokens/latency than the compact V1 prompt. Do not promote that expanded V2.

The failure also exposed one malformed control: an owner-preferred permission sentence had been labeled T10 ABSENT without a tell-specific judgment. Owner authorship/preference is not an ABSENT label.

Current experimental repair:
- keep V1 as the production base;
- T01 needs to distinguish author-specific cognition/evidence from a general criterion merely wrapped in first person;
- T10 negative controls must pass the permission gate and be logically anchored to the local passage, not merely owner-authored;
- T11 should use a subject-matter state-change/deletion test so necessary time/case/premise transitions are not confused with generic relevance/connective statements.

A compact V2.1 exists in the Pangram lab as **experimental only** and must pass a genuinely fresh tell-specific holdout before production promotion. Do not use the consumed development cases as validation.

### Retired global-judge calibration

Do **not** require or rely on a 20/20 hidden-authorship classifier.

The global-judge family failed to generalize:
- abstract provenance classifier v1: 14/20;
- hard scaffold-veto v2: 10/20;
- seven-pair absolute contrastive holdout v3: 10/20 after 11/12 development;
- matched pairwise realization-defect chooser: 5/8.

Those experiments are useful research evidence about method failure. They are not production admission gates.

## 6. Admission

There is no single `fresh-critic PASS`.

Fresh-audit admission requires:
- the complete tell ledger has been dispositioned on the literal candidate;
- when a fresh global sweep is used, every tell row is present and every PRESENT/UNCERTAIN finding has been resolved rather than averaged away;
- every **applicable calibrated narrow axis** reports no unresolved FAIL;
- any model FAIL has been repaired or explicitly rejected as a false positive with an exact editorial reason;
- uncalibrated-axis model output is treated as advisory only;
- direct natural-boundary editorial reading still finds no substantive model-shape/coherence defect the editor actually believes;
- preservation and architecture/coherence gates pass separately.

Absence of narrow FAILs is not a completeness certificate. The editor must still ask the plain questions the model may miss.

For the dangerous-present-adult incident, unpaid review should have blocked before Pangram on at least three independently observable grounds:
- cumulative instruction-manual/listicle cadence;
- missing reader-purpose/pragmatic setup;
- the orphaned `“ask”` reference after removal of the source `voice / ask / answer` setup.

## 7. Failure handling

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

## 8. Research boundary

Hidden-authorship classification, broad Human/AI scoring, detector-passing stress sets, and pairwise global judges may still be studied in the Pangram lab.

They are detector/method research, not production certification.

Pangram remains downstream. It cannot rescue a failed unpaid editorial or specialized audit.
