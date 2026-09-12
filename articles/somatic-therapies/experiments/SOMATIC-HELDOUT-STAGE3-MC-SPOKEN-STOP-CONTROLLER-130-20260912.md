# Somatic held-out Stage-3 method test 130 — spoken answer + stop controller

Date: 2026-09-12
Status: **READY FOR FRESH-CHAT EXECUTION / NO PANGRAM / NO ARTICLE INSTALL**

## Objective

Test a materially different generation process after architectures A and B both failed first-pass architecture. The target remains the frozen Stage-3 / Brainspotting held-out boundary. This tests generation method, not article completion.

Controlling correction: `work/stage2-humanization-goal-correction-125.json`.
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

After each smallest natural publication movement (normally one or two sentences), give the controller:
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

Use a fourth genuinely fresh architecture critic if available. Critic sees only heading purpose, live reader pressure, and literal candidate. Preservation comes only after architecture PASS.

## Success / failure interpretation

Success is not `shorter`. Success is a materially cleaner first-pass movement whose stopping point follows the live thought without losing assigned semantics.

If this architecture passes first-pass architecture with lower repair burden than B, replicate on another held-out target before promoting it as a general humanization lesson.

If it still fails through restatement/closure, do not add another prohibition. Reconsider whether publication realization itself should be sentence-generated at all, or whether owner-like thought reconstruction needs a different unit than prose continuation.

## Boundaries

- no Pangram;
- no article installation;
- no Stage-2 completion;
- no citation/publishing work;
- no promotion to pangram-humanization-lab from this single test.