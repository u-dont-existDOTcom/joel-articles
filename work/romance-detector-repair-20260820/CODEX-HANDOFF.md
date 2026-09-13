# Codex handoff — Romance detector repair

Updated: 2026-08-23 after r22 Part 1 reached Pangram 4.0 exact Human `1.0` and the detector evidence closeout was merged.

## Authority

Canonical `main:articles/romance/master.md` remains unchanged at SHA-256:

`af50b7b93662daf00d484ad83faa0453ff0a2a4fda2867ecfd467166b4c984fe`

PR #29 / `task/romance-detector-repair-20260820` is working detector/editorial state only. **Never merge PR #29 wholesale.** Current Joel corrections/acceptances outrank task prose; preservation proof, semantic/editorial quality, architecture, source provenance, and fidelity outrank Pangram.

Semantic-r9 remains the loss-recovery baseline: 44/44 headings aligned and ten discovered unsuperseded argumentative losses restored. Father provenance remains separate: the only exact remembered father sentence is `Sex is what you do when you are older and you find a friend you want to have children with.` Joel's later readiness/co-parenting questions are his interpretation.

## Current leading task candidate — r22

r22 combines:
- settled r19 Talk owner-final tail;
- settled r20 Casual two-deletion realization;
- owner-accepted patient/helping replacement;
- owner-accepted holistic `Affection and the simmer` repair;
- all other retained r20 content unchanged.

### Exact r22 Markdown

Path:
`work/romance-detector-repair-20260820/materialized-preservation-r22-patient-affection/candidate-master.md`

- Git blob `9f6bf7ed77093569a98fe606fda96ac277839f99`
- SHA-256 `f0f9a47eba2ac9ab1a56bdd6793316d41e7c23072b0b0c030285caf5e12f83c9`
- 20,282 words
- native objects 11→11
- Markdown links 22→22
- section order unchanged
- zero unexplained substantive deltas

### Exact reader-visible Part 1

Path:
`work/romance-detector-repair-20260820/materialized-preservation-r22-patient-affection/part1.txt`

- Git blob `70d8fa0bca4bfe52e00f5721f55cf5b7819cf899`
- SHA-256 `5ed333800b9ae7b402f26aa03e751ef8296c7e27ab70e39bc39bb9896b23e62d`
- 10,239 words

### Stable Part 2

- SHA-256 `9e4c6a522c95741c7dfc9e040b2dcc40773427cbc0aef8f45211de77208b0c85`
- 9,892 words
- exact Pangram 4.0 Human `1.0`
- do not rerun unless bytes change

## r22 preservation / architecture proof

Pre-proof:
`work/romance-detector-repair-20260820/recovery-20260823/preservation-proof-r22-patient-affection-pre.json`

Final receipt:
`work/romance-detector-repair-20260820/recovery-20260823/preservation-proof-r22-patient-affection-final.json`

Final status:
- 22/22 preservation units resolved
- exactly two authorized r22 operations
- forward traceability PASS
- reverse traceability PASS
- owner provenance separation PASS
- architecture/coherence PASS
- production preflight PASS
- zero unexplained substantive deltas

Do not reopen settled spans merely because an older aggregate once highlighted them.

## Owner-accepted r22 wording provenance

### Patient/helping

Provenance: **assistant-produced, owner-accepted**, not natural owner prose.

Durable acceptance:
`work/romance-detector-repair-20260820/recovery-20260823/OWNER-ACCEPTED-PATIENT-R21.md`

Accepted block begins:
`All three women told me at some point that they felt like my patient, and I couldn't exactly argue with them.`

and ends:
`I usually had some idea, so of course I answered. But enough moments become a pattern.`

### Affection and the simmer

Provenance: **assistant-produced, owner-accepted**, not natural owner prose.

Durable acceptance:
`work/romance-detector-repair-20260820/recovery-20260823/OWNER-ACCEPTED-AFFECTION-R22-20260823.md`

The accepted realization preserves exact Toft/Anami links and these functions: affection may safely stop as affection; the between-encounter sexual current matters; near-absence of flirting/desire is meaningful; a changed sex life prompts `what changed?`; Joel does not want his partner responsible for manufacturing his desire; and sex should not get only exhausted leftovers if it materially distinguishes romance from friendship.

Joel manually reported the natural Affection section as Pangram **100% Human, medium confidence** before the aggregate test.

## Blocking production-humanization method

Joel's direct correction on 2026-08-23:

> find all of the reasons the prose might look ai, then fix the whole thing, then double check yourself “does it still look ai?” until the answer is “no not at at all” then test with pangram

Production humanization now means:

1. diagnose all credible interacting model-shaped features across the complete natural boundary;
2. repair the whole real editorial/model-shape problem coherently inside the preservation/owner-authorized boundary;
3. repeat unpaid cold AI-shape reads/revisions until no substantive model-shape problem remains that the editor actually believes;
4. ask `if Pangram returned AI now, would I be genuinely surprised?`; if not, keep editing offline;
5. only then use Pangram to validate.

Minimal pairs/factorials/one-variable experiments are primarily detector-research tools or genuinely narrow decision-changing diagnostics, not the normal production drafting loop.

Durable protocol:
- `main:project-sources/PRODUCTION-HUMANIZATION-PREFLIGHT.md`
- article-skill merge `24ef496e5f9969cdcba4e8eb47220dcd3cc04c8c`
- Pangram lesson promotion merge `e046c7896066e4a85ac951a664ce96631afcecdb`

Generic Pangram cross-key duplicate-call protection was merged at `039b38efcd45ca81cd8e47f2b9c0f6784a9af4bf`. The live fixed-batch executor also has its section-ledger exact-repeat guard. Intentional repeats require explicit research authorization; renaming a measurement key is not repeat authority.

## r22 Part-1 Pangram result — PASS

Frozen public spec:
`u-dont-existDOTcom/pangram-humanization-lab:automation/pangram-fixed-batch/experiments/romance-detector-repair-20260820-preservation-r22-patient-affection-part1-aggregate-20260823.json`

Private immutable request:
`u-dont-existDOTcom/pangram-private-executor:main/requests/romance-detector-repair-20260820-preservation-r22-patient-affection-part1-aggregate-20260823.json`

Private request commit:
`19b9915b24a1a64e91e9f2426f7735180b3e0943`

Exact public result:
`u-dont-existDOTcom/pangram-humanization-lab:automation/pangram-fixed-batch/state/experiments/romance-detector-repair-20260820-preservation-r22-patient-affection-part1-aggregate-20260823-results.json`

Immutable result identity:
- result ref `1c54a9824964cead8069532900215fcc97c9478f`
- result SHA-256 `d7b7d6a4c5a70bf5786211439f5f834d67ed1e32fa7990efb04a9223838ef14a`

Pangram 4.0 exact result on Part-1 SHA `5ed333800b9ae7b402f26aa03e751ef8296c7e27ab70e39bc39bb9896b23e62d`:
- `stage`: `STAGE_SUCCESS`
- `prediction_short`: `Human`
- `headline`: `Human Written`
- Human `1.0`
- AI `0.0`
- AI-assisted `0.0`
- AI segments `0`
- AI-assisted segments `0`
- Human segments `1`

**There are no residual AI windows in r22 Part 1.** Do not reopen Talk, Casual, Affection, patient/helping, or remote composition-sensitive passages for detector reasons on this boundary.

Joel authorized the supported local Pangram GUI path as fallback if the API result did not arrive. The API result arrived successfully, so **no GUI detector submission was necessary**. For future fallback/recovery follow `pangram-humanization-lab:main/docs/PANGRAM-LOCAL-PLAYWRIGHT.md`; authenticated History recovery comes before any repeat click.

## Current detector status

- r22 Part 1: exact Pangram 4.0 **Human `1.0`**
- stable Part 2: exact Pangram 4.0 **Human `1.0`**
- These are two exact half/document boundaries. **Do not describe them as a measured whole-article score.** Half/section results are not mathematically composable into one whole-document measurement.
- No further Pangram call is justified by detector residuals in the retained halves.

## Detector lesson closeout — COMPLETE

The r22 result auto-registered as lesson-inbox item `Q-417c3e502e9d980f`.

Disposition: **article-specific** — exact Romance certification, with no distinct transferable mechanism beyond the already-promoted production-preflight lesson.

Closeout PR #131 passed lesson processor, lesson integrity, and repository workflow policy and was merged to Pangram `main` at:

`a0a778235635c64c8b1a122e344871c589241ae9`

The r22 detector pass is therefore durably closed.

## Stable locks / safety

- Gandarussa male contraception remains; do not remove it.
- Father exact remembered quote remains provenance-separated from later interpretation.
- Talk 6/6, Affection 6/6, Casual 6/6, Primal 6/6; no seventh local calls.
- Long-document composition/split changes can cause remote detector flips; byte-identical remote red is not rewrite authority.
- Detector score never outranks owner authority, semantic sanity, preservation, or architecture.
- Canonical `main` remains unchanged until deliberate owner reconciliation/acceptance.
- Do not publish/export.

## Next safe action

Detector repair is finished for the retained r22 halves. The next substantive task is **owner reconciliation/editorial review of the complete r22 task candidate against the registered canonical Romance article family**, using a clean preservation-controlled diff rather than merging PR #29 wholesale.

Do not spend more Pangram calls merely to improve already-green half boundaries. If a future required boundary is different, recover exact current state and apply the production preflight before testing it.
