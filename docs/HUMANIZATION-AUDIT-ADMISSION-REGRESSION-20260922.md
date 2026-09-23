# Humanization audit admission regression — 2026-09-22

Status: ACTIVE PROCESS REGRESSION / NO DETECTOR CALL

## Failure being prevented

The Inner Child dangerous-present-adult campaign produced a false pre-Pangram PASS even though the active rule set already contained the relevant instruction-manual/listicle and abrupt-complication tells.

The failed operational criterion was effectively:

`fresh critic says no definite AI tell + at least one Human-facing tell -> advance`

That criterion was too weak because:
- `mixed` findings could pass without aggregate adjudication;
- positive Human-facing findings could psychologically balance unresolved AI-shape;
- the critic packet could be target-only and therefore unable to judge reader model, why-now, transition, or antecedents;
- critic calibration used a known-good control but did not require a known-bad control, testing specificity without testing sensitivity;
- cold-audit `preserve-with-reason` could be satisfied by saying the **function** was source-protected even when the **realization** remained model-shaped.

## Regression cases

These are process fixtures, not reusable prose and not detector authority.

### Negative control A — instruction-manual readiness

Owner-labeled failure:

> How much of the grown-up you is actually here right now? Try looking around the room, pausing before you act, making a choice and following through on it. If you can't do that because you're basically the frightened kid, leave the deeper conversation until later. You may need somebody steady there with you, or to do whatever helps you come back a bit before you try to talk to the child.

Expected audit result:
- FAIL;
- cumulative instruction-manual/listicle cadence must be surfaced;
- a Pangram-Human result on a larger boundary cannot clear it.

### Negative control B — dangerous-adult paragraph

Owner-labeled failure:

> Think about this as if there were an actual child in the room. If you genuinely enjoy frightening or humiliating vulnerable people, that's different from having an intrusive thought you hate, holding a strange belief, or having done something harmful in the past. Would you bring the child over just to see how the child reacts? No. If the child recoils, that reaction only tells you the child is frightened. It doesn't tell you that you're safe for the child, and it may give you exactly the reaction you wanted. The child shouldn't be brought into this at all.

Expected audit result:
- FAIL;
- compact distinction + question/verdict + recoil/fear/not-safety/reward/exclusion must be aggregated rather than left as separate `mixed` items;
- reader-model/why-now check must ask who is being addressed and why this sequence matters to that reader.

### Positive control — owner-accepted checking paragraph

> If you're feeling guilty because you didn't put your seat belt on, just put it on. If you still want to investigate it later, fine. Perhaps now and then you feel bad about that time you refused to put it on, broke your collar bone in a crash, and then got blamed for not wearing it. That's natural, but doesn't mean there's something new to look at. Then the background checker goes, “But are you really listening?” There it is. Seat belt's on. Where were we?

Expected audit result:
- must not be rejected merely because it contains direct advice, questions, short sentences, or a compact practical movement;
- any critic configuration used as non-detection gate evidence must distinguish this control from both negative controls without being told their labels.

## Admission assertions

A critic configuration is **not calibrated** merely because it accepts the positive control.

A critic non-detection is **non-gating** if:
- the target was not supplied in its natural reading boundary;
- intended reader/local purpose was omitted when relevant;
- a known-bad same-register control is missed;
- unresolved `mixed` findings remain;
- several mixed findings aggregate into a known cumulative AI-shape;
- preservation/source necessity is used to defend the exact realization rather than the cognition.

No Pangram call is required to run this regression.


## 2026-09-22 blinded provenance benchmark result

A 20-item blind benchmark was frozen before classification:
- 10 provenance-secure Human passages;
- 10 provenance-secure model-written passages;
- Human/AI labels were based on authorship provenance, not Pangram outcome;
- the critic used stateless GPT-5.6 Sol through the authenticated UDA Venice gateway;
- labels remained hidden until all 20 literal responses were frozen.

Result under the then-current critic logic:
- overall: **14/20 (70%)**;
- Human: **10/10**;
- AI: **4/10**;
- six errors were all model-written passages classified Human.

The critic often identified the model-shaped semantic topology but then let a concrete reaction, strong judgment, unresolved ending, social address, or sustained metaphor override that topology. This establishes that Human-looking devices are not positive votes merely because they are apt. It did **not** establish that genuine Human prose must contain surplus that breaks a clean functional scaffold.

The 20 examples used for this diagnosis became development data. A revised rubric then made content-neutralized scaffold analysis a hard veto and required Human evidence to materially break that scaffold.

## 2026-09-23 untouched holdout v2 — overcorrection result

A new untouched 20-item provenance holdout was frozen before classification:
- 10 Human / 10 AI;
- 61–201 words;
- zero exact-SHA overlap with v1;
- labels stored separately until all 20 Venice responses were frozen;
- same GPT-5.6 Sol Venice route and temperature 0.

Result:
- overall: **10/20 (50%)**;
- Human: **1/10**;
- AI: **9/10**.

The v2 hard-veto theory is therefore falsified. Genuine Human prose can be compact, coherent, instructional, causal, self-contained, carefully sequenced, and easy to summarize as a functional staircase. Requiring Human evidence to “break” the scaffold caused massive false-AI overcalling.

The two tests together establish a method boundary:
- v1 was too permissive toward model-simulated Human-facing features;
- v2 was too aggressive toward structured Human prose;
- adding another abstract prohibition/exception layer is no longer justified.

A literal contrastive global classifier was then tried as a materially different architecture. Development looked promising, but the untouched seven-pair GPT-6 Sol holdout collapsed to **10/20**, and a matched pairwise realization-defect chooser scored **5/8**. The global-judge family is therefore retired for production admission.

The production benchmark target was also corrected: hidden model authorship is not the same thing as a remaining model-shaped editorial defect. A model-authored passage can become Human-facing; Human-authored prose can still have manual/listicle cadence. Authorship provenance remains useful experiment metadata but is not the production gold label.

### Specialized defect-audit replacement — 2026-09-23

The production task was decomposed into narrow observable audits using GPT-6 Sol:
- reader-purpose / pragmatic act: **2/2** seeded controls;
- cumulative instruction-manual/listicle cadence: **4/4** seeded controls, including Human list/advice counterexamples;
- corrected antecedent/referent coherence: **4/4** controlled cases using the same target with/without its required setup plus self-contained/corrupted Human controls.

Combined current owner-correction-relevant controls: **10/10**.

This is scoped process evidence, not an authorship detector. The new rule is:
- one axis per audit;
- exact spans and observable defect only;
- axis-specific positive/negative calibration;
- owner/editorial defect judgment, not hidden provenance, supplies the label;
- an auditor that misses its controls is non-gating;
- a narrow FAIL is a repair candidate, not proof of AI authorship;
- absence of narrow FAILs still requires a direct natural-boundary editorial read;
- Pangram remains downstream and cannot rescue a failed unpaid audit.

The earlier HTTP 402 event was transient transport evidence only; later neutral probes and complete GPT-6 Sol runs succeeded through the same Venice gateway. Do not treat the 402 as a lasting credit-state fact.

No Pangram call was used for these debugging benchmarks.


## Requirement-accretion correction — 2026-09-23

The prior mandatory `20/20 hidden-authorship holdout` was an **ASSISTANT_INFERENCE**, not an owner-required production outcome.

Parent owner outcome: prevent obvious model-shaped defects from reaching paid Pangram and stop process loops that miss defects Joel can immediately see.

What the 20/20 requirement was supposed to protect: critic sensitivity/specificity.

Strongest simpler alternative: narrow defect auditors calibrated on the exact observable failure classes, plus direct natural-boundary editorial review.

Evidence:
- global authorship/good-vs-bad judge variants failed to generalize across four materially different designs;
- the hidden-authorship label diverged from the actual production question;
- narrow reader-purpose, cadence, and corrected antecedent audits reproduced the owner-correction-relevant defects at 10/10 scoped controls.

Necessity state for the global 20/20 authorship prerequisite: **NOT_NECESSARY**.

Disposition: remove it as a production blocker; preserve the benchmark history as research evidence.
