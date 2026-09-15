# Inner Child Therapy — humanization writer state

Updated: 2026-09-15

Status: **ACTIVE PARAGRAPH-LEVEL OWNER-TEACHING LOOP / article still unregistered**

## Current episode state

Episode 001 produced the first prospective retrieval-first transfer success. The exact candidate tested Human / low confidence, while both the model cold read and Joel independently identified its final tidy sentence as still model-shaped. That sentence was deleted because the following paragraph already carried the leadership function.

Episode 002 then transferred the lesson to a different source paragraph in one pass. The repaired paragraph 1 plus model-generated paragraph 2 remained owner-reported Human / low confidence.

Episode 003 is the first clear detector-instability teaching case. The exact model candidate at SHA-256 `95cd572da40a2588744d7958ec5fb3938880eb42de092fbfc9ed40ad7c7684d4` initially tested AI / low confidence. Four fresh Pangram 4 API repeats on the exact same bytes then returned Human, Human, Human, AI, all at Medium confidence. The repeat experiment therefore establishes that this candidate sits on an unstable detector boundary.

Joel supplied an aligned same-thought rewrite at SHA-256 `04378a6a51cc40b8bab131f72480c28e8cc3969d16612f9ba0448cc1083d7ef1`, owner-reported Human / low confidence.

Episode 004 then showed a boundary-interaction failure: Joel's aligned chicken-and-egg paragraph and the first borrowed-adulthood realization each tested Human / low confidence in isolation, yet the combined boundary tested AI / medium confidence. The larger boundary exposed a recursive mini-essay shape that the short pieces masked.

Episode 005 repaired the full natural boundary rather than paragraph 2 alone. Exact combined SHA-256 `7011597dd41eefb5ec292d36d7bb37f0c3f5376fe58014a1615dec5a64ab07d6`, 166 whitespace words. Joel reports **five checks, all Human**; the first reported result was Human / medium confidence. Confidence levels for the remaining four checks were not individually supplied. This is accepted as the current working natural-boundary realization, still non-authoritative because the article family remains unregistered.

Exact Episode 003 bytes/repeats live in `experiments/EPISODE-003-RESULT-20260915.json`; Episode 004 boundary evidence is in `experiments/EPISODE-004-BOUNDARY-INTERACTION-20260915.json`; Episode 005 candidate/preservation/audit/repeat evidence is in `experiments/EPISODE-005-NATURAL-BOUNDARY-CANDIDATE-20260915.json`.

## Direct owner correction — instability is not acceptance

The prior inference that we should stop rewriting the Episode 003 model candidate because its single AI result might be detector noise is **superseded**.

The correct distinction is:

- the 3-Human / 1-AI repeat distribution means the detector label is unstable and must not be described as reliable evidence that the prose is intrinsically AI-authored;
- but Joel's production goal is not majority-Human or pass-once behavior. He wants Pangram to recognize the intended delivery boundary as solidly Human rather than randomly flip;
- therefore a candidate already shown to flip AI across fresh exact repeats is **not an accepted production humanization endpoint**;
- detector instability is a reason to continue faithful repair or use a stronger owner-aligned realization, not a reason to preserve the borderline candidate;
- the known-green calibration guard does not protect a candidate whose current exact repeat evidence is contradictory;
- short-boundary noisiness affects confidence and testing strategy. It does not convert a demonstrated flip into completion.

This correction is about the acceptance criterion, not detector authorship provenance. Pangram red does not prove AI authorship, and Pangram green does not override editorial defects. Meaning, fidelity, owner language, and article architecture still outrank detector optimization.

## Direct owner correction — repeat attention is confidence/boundary-sensitive

Joel's 2026-09-15 working production rule after Episode 005:

- concentrate repeat-instability concern on **low-confidence** results, especially short boundaries or boundaries with contradictory evidence;
- do **not** make repeated Pangram checks a routine burden for a larger natural boundary that is already Human at medium/high confidence and has no contradictory evidence;
- Episode 005's five Human checks on the exact 166-word boundary are accepted as sufficiently stable for this production loop;
- preserve this as an owner operating rule and local empirical observation, **not** as a universal claim that medium/high Pangram results can never flip.

## Direct owner correction — owner-facing admission is blocking

Joel's 2026-09-15 correction: **do not give him a humanization candidate to check when the model's own cold read already sees a credible AI-shaped problem in it.**

The earlier Episode 001/003 behavior violated the operation goal by detecting a residual weakness and then surfacing the same candidate for Joel to catch or confirm. The cold audit is therefore not commentary; it is an owner-facing admission gate.

Before showing Joel any new humanization candidate:

1. Run the normal cold audits on the literal candidate and natural boundary.
2. Ask whether any credible model-shaped feature remains that the editor actually believes is present: tidy close, explanatory aftercare, generic synthesis, artificial sequencing, equalized cadence, abstract relationship announcement, or another substantive AI-shape problem.
3. If **yes**, mark `OWNER_DELIVERY_ADMISSION = FAIL`, withhold the candidate, and revise internally. Do not use Joel as the first-line critic for a defect already detected here.
4. Re-run the cold audit after repair. Repeat until `OWNER_DELIVERY_ADMISSION = PASS` or the method has genuinely exhausted faithful repairs.
5. If faithful repair is exhausted, make an explicit narrow authorial handoff explaining what is unresolved and what cognition is needed. Do not disguise a knowingly weak draft as a candidate for routine checking.
6. A Pangram Human result never overrides this gate; a candidate that passes the detector but retains a known editorial/model-shaped defect remains blocked from delivery.

This is the task-local enforcement of the existing repository rule that a legitimate cold-audit weakness must be fixed before delivery. It adds no phrase blacklist and does not require artificial roughness.

## Direct owner correction — objection → best repair → final version

For every future owner-facing humanization candidate, expose the cold-audit reasoning in a useful form **without making Joel review a knowingly defective draft**.

For each strongest objection:

1. identify the exact span/pattern and why it is a plausible model-shape risk;
2. show the **best faithful repair** available for that objection;
3. state whether the repair was applied;
4. if it was not applied, state why the repair would damage meaning, cadence, voice, continuity, or another protected function more than it helps;
5. after all objections, give **one final integrated fixed version** for Joel to check.

The object shown for checking is the final repaired candidate, not Draft 0. A hypothetical repair may be shown as comparison when the objection is only a risk rather than a true defect.

Episode 005 candidate 3 remains a watch item for future larger-boundary work: the gradual-internalization sentence can read like a tidy tapering close. If later context provides a natural next consequence that can carry the same source function, prefer that less-closing realization **only if it improves the prose without losing the gradual-internalization claim**.

## Current production method

1. Retrieve the closest literal owner-teaching demonstrations before generation.
2. Preserve the complete source thought and paragraph job.
3. Work on the full natural reader-visible boundary when adjacent Human snippets interact; do not assume paragraph-level Human results compose.
4. Cold-read the whole natural boundary. If a credible model-shaped feature remains, repair it before paying Pangram **or showing the candidate to Joel**.
5. For owner delivery, present strongest objection → best faithful repair → applied/not-applied rationale → one final integrated fixed version.
6. Use Pangram to validate a fully considered candidate, not to draft by trial and error.
7. If fresh exact repeats expose a real Human/AI flip, preserve the repeat distribution and treat the candidate as detector-unstable rather than averaging the labels into a pass.
8. Continue faithful repair until the intended delivery boundary meets Joel's standing Humanization gate. Do not manufacture quirks, factual changes, or owner imitation merely to create detector margin.
9. Concentrate repeat testing on low-confidence, short, or contradictory boundaries; do not repeat medium/high larger natural boundaries by default without decision value.
10. `OWNER_DELIVERY_ADMISSION` must be `PASS` before routine owner review.

## Episode 003 disposition

The model candidate `95cd572d…684d4` is **rejected as a production baseline because it is detector-unstable**.

Joel's aligned rewrite `04378a6a…d7ef1` is the current teaching target and is owner-reported Human / low confidence. It has **not** been established as repeat-stable in isolation, but its exact wording now participates in the Episode 005 166-word natural boundary that Joel reports Human on five checks.

## Episode 005 disposition

The exact 166-word combined candidate `7011597d…07d6` is the current accepted working boundary for this manual loop: preservation clean, same-context cold-audit admitted, and owner-reported Human on five checks. The first explicitly reported confidence was medium. Do not spend further repeat calls merely to reconfirm it absent new contradictory evidence or a materially changed boundary.

## Authority boundary

The raw Substack editor source is hash-bound and the owner-teaching experiments are durable, but the Inner Child Therapy article family is still unregistered. These teaching candidates are non-authoritative experimental realizations until the complete article family is created and registered. Do not silently promote them into a canonical master before that authority step.
