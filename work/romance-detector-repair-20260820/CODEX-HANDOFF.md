# Codex handoff — Romance detector repair

Updated: 2026-08-23 after Joel's production-humanization workflow correction, owner acceptance of the patient and Affection repairs, exact r22 materialization/preservation proof, and submission of the single r22 Part-1 aggregate request.

## Authority

Canonical `main:articles/romance/master.md` remains unchanged at SHA-256:

`af50b7b93662daf00d484ad83faa0453ff0a2a4fda2867ecfd467166b4c984fe`

PR #29 / `task/romance-detector-repair-20260820` is experimental working state only. **Never merge PR #29 wholesale.** Current Joel wording/acceptance outranks task candidates; preservation proof, semantic/editorial quality, architecture, source provenance, and fidelity outrank Pangram.

Semantic-r9 remains the loss-recovery baseline: 44/44 headings aligned and ten discovered unsuperseded argumentative losses restored. Father provenance remains separate: the only exact remembered father sentence is `Sex is what you do when you are older and you find a friend you want to have children with.` Joel's later readiness/co-parenting questions are his interpretation.

## Stable settled task choices

- **Talk:** r19 owner-final Talk tail is settled and outside current AI windows. Preserve exact owner wording in `recovery-20260822/OWNER-TALK-FINAL-TAIL-20260822.md`.
- **Slow Steady:** retain exact local-green minimum-dose repair SHA `2def6737f8763f6e3a92405166dd27f9d0e30ec043a57a216ffbc05bf6bb72f4`.
- **Casual:** r20 is settled. Joel approved two deletions only: remove `Oxytocin, vasopressin, and the rest can start attaching you anyway.` and remove `You can both mean it when you say this is only sex and still have one of you get attached afterward.` Preserve `If you’re both really numb or robotic about sex, maybe not.`
- **Stable Part 2:** SHA `9e4c6a522c95741c7dfc9e040b2dcc40773427cbc0aef8f45211de77208b0c85`, 9,892 words, Pangram 4.0 exact Human `1.0`. Do not rerun unless bytes change.

Local section caps: Talk 6/6, Affection 6/6, Casual 6/6, Primal 6/6. No seventh local calls or invented identities. Maturity/patient cross-split is 4/6 after the r4 diagnostic probe, but no further local call is currently needed.

## r20 aggregate baseline

r20 Markdown:
`work/romance-detector-repair-20260820/materialized-preservation-r20-casual-two-deletions/candidate-master.md`

- master SHA `8b60f2916a4c050c6295b858889c3a7e3e80c87e18307a2c3e2cf9e276e8637d`;
- 20,343 words;
- native objects 11→11;
- Markdown links 22→22;
- zero unexplained deltas.

r20 Part 1:
- SHA `04ea13442d4044ee56733b75771cb62c5cd44ba1b5da1bbb57d637c4f2ec4316`;
- 10,300 words.

Pangram r20 Part 1:
- Human `0.9639888405799866`;
- AI `0.03601117804646492`;
- assisted `0.0`;
- three AI windows.

Casual is completely outside all r20 AI windows. r20 detector closeout merged into Pangram main at `7e8b15540ff7d6ed2f5b6a3237f3d7495ce70486`.

## r22 owner-accepted changes

### 1. Patient/helping

Joel accepted this exact assistant-produced wording; provenance is **assistant-produced, owner-accepted**, not natural owner prose:

> All three women told me at some point that they felt like my patient, and I couldn't exactly argue with them. They asked me about almost every medical, mental-health, and practical problem:
>
> “I’m sick. What should I take?”
>
> “I’m sad. What should I do?”
>
> I usually had some idea, so of course I answered. But enough moments become a pattern.

Durable owner acceptance:
`work/romance-detector-repair-20260820/recovery-20260823/OWNER-ACCEPTED-PATIENT-R21.md`

Joel manually reports the short snippet tests Human at low confidence. Historical/wider-boundary evidence is stronger: the accepted realization sits inside a previously High-confidence Human patient boundary, and in the r4 `known-green + pattern` probe the first 223 words remained High-confidence Human while the detector moved downstream into unchanged prose. Probe closeout merged to Pangram main at `59d09ca910d89c5f35fd1112b96f5b91414d7cf7`.

### 2. Affection and the simmer

Joel accepted the holistic repair direction and reported it tests **100% Human, medium confidence** on the natural section. Provenance is also **assistant-produced, owner-accepted**.

Durable owner acceptance and exact complete Markdown realization:
`work/romance-detector-repair-20260820/recovery-20260823/OWNER-ACCEPTED-AFFECTION-R22-20260823.md`

Current exact r22 Affection realization:

> Doug Toft, who has been married for fifty years, has a useful list called [*50 Things I Learned from 50 Years of Marriage*](https://dougtoft.substack.com/p/50-things-i-learned-from-50-years). One of his points is to touch his wife without an agenda. A hug, cuddle, kiss, or back rub should sometimes be allowed to end right there. If every affectionate touch becomes a bid for sex, affection itself can start feeling like pressure.
>
> Kim Anami calls the sexual current between encounters [“the simmer”](https://kimanami.com/meet-another-well-fked-man/). Maybe she texts from work, “I can’t wait to touch you.” Maybe he tells her what he wants to do later. If we supposedly want each other but hardly ever flirt or let each other know it, I think something is already wrong. Great sex probably isn't going to materialize out of nowhere at bedtime.
>
> And if our sex life suddenly changes, I want to know what changed. Maybe we're pissed off at each other. Maybe somebody's sick, stressed, on a new medication, whatever.
>
> I also don't want my partner to have to manufacture my desire for me. And if sex is one of the main things separating our relationship from friendship, giving it whatever exhausted scraps are left after everything else seems pretty dumb.

Owner acceptance authorizes removing/superseding the prior counseling-style `opposite failure`, standalone `relationship homework` caveat, `You need both` recap, exhaustive barometer checklist wording, and generalized symmetric responsibility framing while preserving the underlying owner-accepted functions and exact Toft/Anami links.

## New blocking production-humanization workflow

Joel directly corrected the process on 2026-08-23:

> find all of the reasons the prose might look ai, then fix the whole thing, then double check yourself “does it still look ai?” until the answer is “no not at at all” then test with pangram

Production humanization now separates from detector research:

1. diagnose **all credible interacting model-shaped features** across the whole natural boundary;
2. repair the whole real editorial/model-shape problem coherently inside the preservation/owner-authorized boundary;
3. repeat unpaid cold AI-shape reads and revisions until no substantive model-shape problem remains that the editor actually believes;
4. use the readiness question: **if Pangram returned AI now, would I be genuinely surprised?** If not, do not spend the production call;
5. only then submit Pangram.

Minimal pairs/factorials/one-variable experiments remain useful primarily for explicit detector research or one narrow uncertainty that will genuinely change the next editorial decision. Do not spend a hard-capped production section budget discovering prose through mechanistic detector tests.

This correction is now durable and blocking:
- `joel-articles:main/project-sources/PRODUCTION-HUMANIZATION-PREFLIGHT.md`, merged in main commit `24ef496e5f9969cdcba4e8eb47220dcd3cc04c8c`;
- `CANONICAL-REPO-MAP.md` routes humanization work through it;
- Pangram evidence `state/PRODUCTION-HUMANIZATION-PREFLIGHT-VS-DETECTOR-RESEARCH-2026-08-23.md`, evidence commit `2736e153bbdd912a54d5f5e046992d747971d9d5`;
- Pangram lesson promotion merged to main at `e046c7896066e4a85ac951a664ce96631afcecdb`.

## Affection six-call audit / duplicate-call lesson

The six historical Affection calls were not an efficient production budget:
1. baseline 259 words, Human 0%;
2. broad R2B rewrite 229 words, Human `0.2138554`;
3. **byte-identical paid R2C repeat** of #2, same SHA `636a4312...`, same score;
4. broad R3 rewrite, Human `0.1954577`;
5. compressed 132-word R4B, Human `0.3731932`, useful diagnostic but incomplete candidate;
6. transition R6, Human 1.0 High confidence, but it omitted most Affection and crossed into Casual, so it localized context rather than solving the full section.

The audit confirmed the old loop changed surface realization while retaining substantially the same balanced therapist/explainer architecture. The owner-accepted holistic repair above is the first current production example of the corrected method.

A generic Pangram cache-layer duplicate-call fix was merged to Pangram main at `039b38efcd45ca81cd8e47f2b9c0f6784a9af4bf`: same model/version/text success is reused across measurement keys by default; pending/ambiguous same-content work blocks new POSTs; intentional detector-research repeat requires explicit override. The live `automation/pangram-fixed-batch` branch also already has a later section-ledger exact-repeat guard (`allow_exact_repeat` is explicit). Do not infer the historical Affection duplicate is still an unguarded current fixed-batch behavior.

## r22 exact materialized candidate

Pre-proof:
`work/romance-detector-repair-20260820/recovery-20260823/preservation-proof-r22-patient-affection-pre.json`

Hash-gated materializer:
`work/romance-detector-repair-20260820/recovery-20260823/materialize_r22_patient_affection.py`

Materialized r22 directory:
`work/romance-detector-repair-20260820/materialized-preservation-r22-patient-affection/`

Manifest:
`candidate-manifest.json`

Exact r22 Markdown:
- path `.../candidate-master.md`;
- Git blob `9f6bf7ed77093569a98fe606fda96ac277839f99`;
- SHA-256 `f0f9a47eba2ac9ab1a56bdd6793316d41e7c23072b0b0c030285caf5e12f83c9`;
- 20,282 words.

Exact r22 Part 1:
- path `.../part1.txt`;
- Git blob `70d8fa0bca4bfe52e00f5721f55cf5b7819cf899`;
- SHA-256 `5ed333800b9ae7b402f26aa03e751ef8296c7e27ab70e39bc39bb9896b23e62d`;
- 10,239 words.

Integrity:
- native objects 11→11;
- Markdown links 22→22;
- section order unchanged;
- exact two authorized operations only;
- zero unexplained deltas;
- stable Part 2 unchanged at prior Human 1.0.

Final preservation/architecture receipt:
`work/romance-detector-repair-20260820/recovery-20260823/preservation-proof-r22-patient-affection-final.json`

Final receipt:
- 22/22 units resolved;
- forward traceability PASS;
- reverse traceability PASS;
- owner provenance separation PASS;
- architecture/coherence PASS;
- production preflight PASS;
- unexplained deltas 0;
- detector eligibility ELIGIBLE.

## r22 aggregate request — SUBMITTED EXACTLY ONCE, DO NOT RESUBMIT

Frozen Pangram spec:
`u-dont-existDOTcom/pangram-humanization-lab` branch `automation/pangram-fixed-batch`:
`experiments/romance-detector-repair-20260820-preservation-r22-patient-affection-part1-aggregate-20260823.json`

Spec:
- Git blob `eebefa277203ce5a8e15c307a4c526add192dc8a`;
- SHA-256 `3a78832211004d7f917258905ad2988294889a8dff6be238b604f421ec58ab28`;
- text source is exact `joel-articles` r22 Part-1 blob `70d8fa0bca4bfe52e00f5721f55cf5b7819cf899`;
- text SHA `5ed333800b9ae7b402f26aa03e751ef8296c7e27ab70e39bc39bb9896b23e62d`;
- budget scope `aggregate`;
- no local Affection call.

Private immutable request:
`u-dont-existDOTcom/pangram-private-executor:main/requests/romance-detector-repair-20260820-preservation-r22-patient-affection-part1-aggregate-20260823.json`

Private request commit:
`19b9915b24a1a64e91e9f2426f7735180b3e0943`

**As of this handoff update, no r22 public result file and no r22 SHA reservation are yet present in the public call ledger.** The private executor is serialized (`queue: max`, `cancel-in-progress: false`) and had other work immediately ahead of this request. Treat this as queued/unresolved exact work, not a failure. Do not touch or recreate the request. Recover from the existing exact request/result/ledger only.

Expected result path once complete:
`pangram-humanization-lab:automation/pangram-fixed-batch/state/experiments/romance-detector-repair-20260820-preservation-r22-patient-affection-part1-aggregate-20260823-results.json`

## Immediate next actions

1. Fresh-read GitHub authority before resuming substantive work.
2. Resolve the **existing** r22 aggregate only: check exact result path and call ledger for SHA `5ed333800b9...`; **do not resubmit**.
3. When the result lands, extract score + windows and compare to r20. Affection and patient should be evaluated in aggregate; do not start another local one-variable ladder.
4. Treat the remote idealization/dependability passage as composition-sensitive unless a new holistic editorial read identifies a real model-shape problem independently of Pangram.
5. If a remaining natural boundary genuinely still looks model-shaped, use the new production preflight: diagnose all credible interacting reasons, repair holistically, cold-read until no credible AI-shape problem remains, preservation proof, then one aggregate validation call if needed.
6. Close out r22 evidence in Pangram lesson system; likely article-specific unless it adds a distinct reusable lesson beyond the already-promoted production-preflight rule.
7. Update PR #29 and this handoff with the exact r22 result.
8. Canonical `main` remains unchanged until deliberate Joel reconciliation/acceptance. Do not publish/export and never merge PR #29 wholesale.
