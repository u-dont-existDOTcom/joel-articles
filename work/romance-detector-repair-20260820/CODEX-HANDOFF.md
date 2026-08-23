# Codex handoff — Romance detector repair

Updated: 2026-08-23 after the exact r22 Part-1 Pangram 4.0 pass.

## Authority

Canonical `main:articles/romance/master.md` remains unchanged at SHA-256:

`af50b7b93662daf00d484ad83faa0453ff0a2a4fda2867ecfd467166b4c984fe`

PR #29 / `task/romance-detector-repair-20260820` is working detector/editorial state only. **Never merge PR #29 wholesale.** Joel's direct corrections and accepted prose outrank task candidates; preservation proof, semantic/editorial quality, architecture, source provenance, and fidelity outrank Pangram.

Semantic-r9 remains the loss-recovery baseline: 44/44 headings aligned and ten discovered unsuperseded argumentative losses restored. Father provenance remains separate: the only exact remembered father sentence is `Sex is what you do when you are older and you find a friend you want to have children with.` Joel's later readiness/co-parenting questions are his interpretation.

## Stable settled choices

- **Talk:** r19 owner-final Talk tail is settled and outside AI windows. Preserve exact owner wording in `recovery-20260822/OWNER-TALK-FINAL-TAIL-20260822.md`.
- **Slow Steady:** retain exact local-green minimum-dose repair SHA `2def6737f8763f6e3a92405166dd27f9d0e30ec043a57a216ffbc05bf6bb72f4`.
- **Casual:** r20 is settled. Joel approved exactly two deletions: remove `Oxytocin, vasopressin, and the rest can start attaching you anyway.` and remove `You can both mean it when you say this is only sex and still have one of you get attached afterward.` Preserve `If you’re both really numb or robotic about sex, maybe not.`
- **Affection:** r22 holistic realization is assistant-produced, owner-accepted, preservation-proved, and now part of a 100%-Human exact Part-1 boundary.
- **Patient/helping:** r22 realization is assistant-produced, owner-accepted, preservation-proved, and now part of a 100%-Human exact Part-1 boundary.
- **Stable Part 2:** SHA `9e4c6a522c95741c7dfc9e040b2dcc40773427cbc0aef8f45211de77208b0c85`, 9,892 words, Pangram 4.0 exact Human `1.0`. Do not rerun unless bytes change.

Local section caps remain: Talk 6/6, Affection 6/6, Casual 6/6, Primal 6/6. No seventh local calls or invented section identities. The corrected production method below supersedes mechanistic detector ladders as the default anyway.

## r22 accepted changes

### Patient/helping

Exact accepted wording:

> All three women told me at some point that they felt like my patient, and I couldn't exactly argue with them. They asked me about almost every medical, mental-health, and practical problem:
>
> “I’m sick. What should I take?”
>
> “I’m sad. What should I do?”
>
> I usually had some idea, so of course I answered. But enough moments become a pattern.

Durable owner acceptance:
`work/romance-detector-repair-20260820/recovery-20260823/OWNER-ACCEPTED-PATIENT-R21.md`

### Affection and the simmer

Durable owner acceptance and exact complete Markdown realization:
`work/romance-detector-repair-20260820/recovery-20260823/OWNER-ACCEPTED-AFFECTION-R22-20260823.md`

The accepted realization preserves the exact Toft/Anami links and the substantive functions: affection can safely stop as affection; the between-encounter sexual current matters; near-absence of flirting/desire is meaningful; a changed sex life prompts a real `what changed?`; Joel does not want his partner responsible for manufacturing his desire; and sex should not get only exhausted leftovers if it materially distinguishes romance from friendship. Joel authorized superseding the prior balanced counseling/recap/checklist realization.

Joel manually reported this natural Affection section as Pangram **100% Human, medium confidence** before aggregate certification.

## Blocking production-humanization workflow correction

Joel directly corrected the production process on 2026-08-23:

> find all of the reasons the prose might look ai, then fix the whole thing, then double check yourself “does it still look ai?” until the answer is “no not at at all” then test with pangram

Production humanization now requires:

1. diagnose all credible interacting model-shaped features across the complete natural boundary;
2. repair the real editorial/model-shape problem coherently inside the authorized preservation boundary;
3. repeat unpaid cold AI-shape reads and revisions until no substantive model-shape problem remains that the editor actually believes;
4. ask: **if Pangram returned AI now, would I be genuinely surprised?** If not, do not spend the production call;
5. only then use Pangram to validate.

Minimal pairs/factorials/one-variable experiments are primarily detector-research tools or narrow decision-changing diagnostics, not the normal production drafting loop.

Durable protocol:
- `main:project-sources/PRODUCTION-HUMANIZATION-PREFLIGHT.md`;
- article-skill merge commit `24ef496e5f9969cdcba4e8eb47220dcd3cc04c8c`;
- Pangram lesson/evidence merged to Pangram main at `e046c7896066e4a85ac951a664ce96631afcecdb`.

A generic Pangram cache-layer duplicate-call repair was also merged to Pangram main at `039b38efcd45ca81cd8e47f2b9c0f6784a9af4bf`: same model/version/text success is reused across measurement keys by default; pending/ambiguous same-content work blocks a new POST; intentional detector-research repeats require explicit override. The live fixed-batch branch independently has a section-ledger exact-repeat guard.

## r22 exact materialized candidate

Pre-proof:
`work/romance-detector-repair-20260820/recovery-20260823/preservation-proof-r22-patient-affection-pre.json`

Hash-gated materializer:
`work/romance-detector-repair-20260820/recovery-20260823/materialize_r22_patient_affection.py`

Materialized directory:
`work/romance-detector-repair-20260820/materialized-preservation-r22-patient-affection/`

Exact Markdown candidate:
- path `.../candidate-master.md`;
- Git blob `9f6bf7ed77093569a98fe606fda96ac277839f99`;
- SHA-256 `f0f9a47eba2ac9ab1a56bdd6793316d41e7c23072b0b0c030285caf5e12f83c9`;
- 20,282 words.

Exact reader-visible Part 1:
- path `.../part1.txt`;
- Git blob `70d8fa0bca4bfe52e00f5721f55cf5b7819cf899`;
- SHA-256 `5ed333800b9ae7b402f26aa03e751ef8296c7e27ab70e39bc39bb9896b23e62d`;
- 10,239 words.

Integrity:
- native objects 11→11;
- Markdown links 22→22;
- section order unchanged;
- exactly two authorized r22 operations;
- zero unexplained deltas;
- stable Part 2 unchanged.

Final preservation/architecture receipt:
`work/romance-detector-repair-20260820/recovery-20260823/preservation-proof-r22-patient-affection-final.json`

Receipt status:
- 22/22 preservation units resolved;
- forward traceability PASS;
- reverse traceability PASS;
- owner provenance separation PASS;
- architecture/coherence PASS;
- production preflight PASS;
- unexplained substantive deltas 0.

## r22 Part-1 Pangram result — PASS

Frozen spec:
`u-dont-existDOTcom/pangram-humanization-lab:automation/pangram-fixed-batch/experiments/romance-detector-repair-20260820-preservation-r22-patient-affection-part1-aggregate-20260823.json`

Private immutable request was submitted exactly once at:
`u-dont-existDOTcom/pangram-private-executor:main/requests/romance-detector-repair-20260820-preservation-r22-patient-affection-part1-aggregate-20260823.json`

Private request commit:
`19b9915b24a1a64e91e9f2426f7735180b3e0943`

Exact public result:
`u-dont-existDOTcom/pangram-humanization-lab:automation/pangram-fixed-batch/state/experiments/romance-detector-repair-20260820-preservation-r22-patient-affection-part1-aggregate-20260823-results.json`

Immutable result identity from lesson inbox:
- result commit/ref `1c54a9824964cead8069532900215fcc97c9478f`;
- result SHA-256 `d7b7d6a4c5a70bf5786211439f5f834d67ed1e32fa7990efb04a9223838ef14a`.

Pangram 4.0 exact result on Part-1 SHA `5ed333800b9ae7b402f26aa03e751ef8296c7e27ab70e39bc39bb9896b23e62d`:
- `stage`: `STAGE_SUCCESS`;
- `prediction_short`: `Human`;
- `headline`: `Human Written`;
- Human `1.0`;
- AI `0.0`;
- AI-assisted `0.0`;
- AI segments `0`;
- AI-assisted segments `0`;
- Human segments `1`.

**There are no residual AI windows to repair in r22 Part 1.** Do not reopen Talk, Casual, Affection, patient/helping, or remote composition-sensitive passages for detector reasons on this boundary.

Joel authorized the Pangram local GUI path as a fallback if the API path did not return. The API result arrived successfully, so **no GUI detector submission was necessary**. The GUI path remains available for future authenticated History recovery/localization; follow `pangram-humanization-lab:main/docs/PANGRAM-LOCAL-PLAYWRIGHT.md` and recover-before-repeat safety.

## Current detector status

- r22 Part 1: exact Pangram 4.0 **Human 1.0**.
- stable Part 2: exact Pangram 4.0 **Human 1.0**.
- These are two exact half/document boundaries. **Do not describe them as a measured whole-article score.** Section/half scores are not mathematically composable into a whole-document result.
- No additional Pangram call is currently justified by detector residuals in either retained half.

## Lesson closeout

The r22 result auto-registered in `state/LESSON-INBOX.json` with queue id `Q-417c3e502e9d980f`. Closeout disposition: **article-specific**. It confirms the already-promoted production-preflight lesson in this Romance case but adds no distinct reusable detector mechanism. The closeout PR should be merged before calling the detector pass durably complete.

## Immediate next actions

1. Fresh-read GitHub authority before any further substantive work.
2. Verify/merge the r22 detector lesson closeout.
3. Update PR #29 to show r22 Part 1 = 100% Human and stable Part 2 = 100% Human.
4. Do **not** spend more detector calls merely to improve already-green halves.
5. The next substantive operation is owner reconciliation/editorial review of the complete r22 task candidate against registered canonical `main`, not another detector-repair loop. Use preservation proof and do not merge PR #29 wholesale.
6. Canonical `main` remains unchanged until deliberate Joel reconciliation/acceptance. Do not publish/export.
