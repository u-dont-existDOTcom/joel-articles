# Somatic held-out Stage-3 method test 130 — spoken answer + stop controller

Date: 2026-09-12
Status: **READY FOR FRESH-CHAT EXECUTION / CONDITIONAL PANGRAM AUTHORIZED / NO ARTICLE INSTALL**

## Objective

Test a materially different generation process after architectures A and B both failed first-pass architecture. The target remains the frozen Stage-3 / Brainspotting held-out boundary. This tests generation method, not article completion.

Controlling corrections:
- `work/stage2-humanization-goal-correction-125.json`;
- `work/humanization-pangram-antidrift-owner-correction-131.json`.

Prior executed comparison: `SOMATIC-HELDOUT-HUMANIZATION-TRANSFER-TEST-126-20260912.md`.

## Hypothesis

Architecture B reduced semantic job-switching but still restated and over-completed one thought. The next hypothesis is that two controls may attack different causes:

1. **ordinary spoken-answer generation** may recover a more natural thought endpoint before publication-writing priors take over;
2. an **independent stop controller** may prevent the publication writer from continuing once the live reader pressure is already answered.

This is a process change, not another writer blacklist.

## Frozen semantic nucleus

Stage heading context: `Stage 3: Work With Trauma Feelings Before the Story Comes In`.

Live reader pressure:
`If Stage 3 is specifically before the story comes in, what does Brainspotting let someone work with here?`

Minimum semantic custody:
- some difficult material is felt before it becomes a coherent story;
- Brainspotting can stay with that felt material through gaze, bodily attention, and therapist attunement without requiring clean narration first.

Withhold fit/population lists, dosing distinctions, later modalities, post-session advice, prior candidates, prior critic findings, preservation ledgers, detector feedback, and Stage-2 failure vocabulary.

## Architecture C — ordinary spoken answer -> publication realization

### C1. Fresh speaker

Use a genuinely fresh GPT-5.6 Sol / Extra High chat.

Give only the heading context, live reader pressure, and minimum semantic nucleus above.

Instruction:
`Answer the reader's question as if a thoughtful friend had asked you in conversation. Do not write article copy. Do not explain your writing method. Say only what you would naturally need to answer the question, then stop.`

Freeze exact output before any review.

### C2. Fresh publication writer

Use a different fresh GPT-5.6 Sol / Extra High chat. Do not show prior experiment history.

Give:
- heading context;
- the exact frozen spoken answer from C1 as semantic source, explicitly not wording authority;
- instruction: `Write the next publication-surface movement. Preserve the answer's meaning and semantic endpoint; do not expand beyond it. Return only prose.`

Freeze exact first output before critique.

## Architecture D — independent stop-controller gate

Use a third fresh GPT-5.6 Sol / Extra High chat as controller. It must not be the publication writer.

After each smallest natural publication movement, normally one or two sentences, give the controller:
- live reader pressure;
- literal accumulated candidate so far;
- no preservation inventory and no prior failure ledger.

Controller returns exactly one of:
- `STOP — reader pressure sufficiently answered`
- `CONTINUE — <one short unresolved reader pressure>`

If STOP, generation ends. If CONTINUE, return only the controller's short unresolved pressure to the publication writer and request the next smallest natural movement. Do not tell the writer why the controller rejected or what anti-pattern to avoid.

Maximum: four writer/controller cycles. If still CONTINUE after four, classify the architecture as failed rather than increasing the budget.

## First-pass measurement

Freeze the untouched assembled publication candidate before architecture critique.

Measure:
- architecture PASS/FAIL;
- repeated paraphrastic restatement;
- explanatory aftercare;
- hidden enumeration;
- conceptual job switching;
- mini-essay completion;
- false symmetry;
- natural semantic persistence;
- number of writer/controller cycles;
- whether controller STOP occurs before the writer would otherwise continue;
- semantic sanity.

Use a fourth genuinely fresh architecture critic if available. Critic sees only heading purpose, live reader pressure, and literal candidate.

## Preservation gate

Only after architecture PASS:
- run forward preservation for the assigned semantic nucleus;
- run reverse traceability for substantive additions;
- require zero unexplained substantive deltas.

Do not append withheld obligations to make the passage complete.

## Pangram calibration gate

Pangram is now authorized **only as a sparse falsification check** for a candidate the supervisor genuinely expects to pass.

Admission requires all of:
1. exact candidate frozen;
2. fresh architecture critic PASS;
3. supervisor architecture PASS;
4. preservation/reverse-traceability PASS with zero unexplained substantive deltas;
5. explicit prediction recorded before detector submission: `EXPECTED_PANGRAM = HUMAN`.

Then run exactly one Pangram 4 measurement on that exact boundary using the current canonical guarded transport and no-repeat/cache rules.

Interpretation:
- `Human` supports the human-likeness prediction for this exact boundary; it does not prove authorship or generalization.
- `AI` or `Mixed` means the prediction was wrong. Pangram localizes evidence but does not explain causality. Diagnose the literal prose and compare against the method hypothesis; do not treat detector windows as phrase instructions.

## Anti-drift experiment budget

For this held-out target:
- maximum method-level candidates: **2**;
- maximum new Pangram calls: **2**;
- maximum writer/controller cycles per candidate: **4**.

If the first detector-qualified candidate fails Pangram:
1. freeze the result;
2. perform one bounded diagnosis of why the literal prose still looks model-shaped;
3. allow exactly one materially changed generation-method attempt;
4. do not run minimal-pair/factorial phrase experiments, token hunts, candidate swarms, adjacent-section rewrites, citation work, Stage-2 completion, sidecar work, or publishing work.

After the second method-level candidate or second Pangram result, whichever arrives first, **stop and return an owner checkpoint**. Do not open another experiment family without new owner direction.

The owner checkpoint must state:
- exact first-pass architecture result(s);
- exact Pangram result(s), if run;
- whether the supervisor's Human prediction was right or wrong;
- what method hypothesis was eliminated or strengthened;
- whether owner correction was still required;
- whether the method is ready for replication on a second held-out target.

## Success / failure interpretation

Success is not `shorter` and not merely `Pangram Human`. Success requires:
- materially cleaner first-pass architecture than B;
- lower critic repair burden;
- assigned semantics preserved;
- supervisor Human prediction confirmed by Pangram when measured.

If this architecture passes those gates, replicate on another held-out target before promoting it as a general humanization lesson.

If it still fails through restatement/closure, do not add another prohibition. Reconsider the generation unit or method at the owner checkpoint rather than launching another local loop.

## Boundaries

- Pangram only under the calibration gate above;
- no article installation;
- no Stage-2 completion;
- no citation/publishing work;
- no promotion to pangram-humanization-lab from this single test.