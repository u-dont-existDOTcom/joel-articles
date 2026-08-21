# Romance Part 1 — rhythm/architecture diagnosis — 2026-08-21

Status: task working diagnosis. Current owner instruction is to fix Part 1 using lessons learned from the owner-integrated Part 2 repair. Canonical `main` remains unchanged.

## Exact baseline

Current candidate Part 1 remains byte-identical to the registered reader-visible Part 1:

- SHA-256 `ae88df0f4156537239cb984337196703b88629c3588a5e58ee50c0888d3b39f8`
- 10,236 words
- historical Pangram 4 Human `0.9205247164`, AI `0.0794752836`, assisted `0.0`.

Historical Part-1 AI windows were broad/short detector localization, not natural rewrite boundaries. Current repair therefore diagnoses whole natural sections at roughly >=200 words under their own section budgets before rewriting.

## Natural-section diagnostic set

Frozen experiment on `pangram-humanization-lab:automation/pangram-fixed-batch`:

`experiments/romance-detector-repair-20260820-part1-natural-sections-r1-20260821.json`

Exact spec SHA-256:

`feb9097c0e18ec033f04eeb9db59e28e7858e58b544909253f4cecf2f959ed82`

Five genuine section identities, each beginning at call 1/6 if uncached:

1. `part1-talk-before-sex`
2. `part1-affection-simmer`
3. `part1-casual-sex-situationship`
4. `part1-crucible`
5. `part1-maturity-levels-cross-split` — deliberately reconstructed across the arbitrary Part1/Part2 half split so the detector sees the natural section rather than the file boundary.

Private self-hosted request:
`romance-detector-repair-20260820-part1-natural-sections-r1-20260821`.

Do not duplicate while pending; inspect cache/ledger/result first.

## Cold editorial hypotheses before detector result

These are architecture diagnoses, not detector conclusions. Do not change a section merely because it appears here if the exact natural section is already editorially sound and detector-green.

### Talk before sex

The historical attempted repair only paraphrased `Sex drives are independently alive...` into `Sex drives have lives of their own...`; the aggregate Part1 result slightly worsened and that edit was reverted.

Likely deeper issue: the section is already asking what sex means to each person, then stops to create a separate abstract mini-lesson about libido `discordance`, then resumes the live question `can you actually say all that once you're naked?`

If the natural section fails, repair the thought route rather than synonym-swapping the sex-drive paragraph: keep changing desire inside the ongoing conversation about what sex means, so the practical reason to discuss mismatch arrives before either person is hurt without creating a freestanding taxonomy/lesson.

### Affection and the simmer

The section currently presents Toft's no-agenda affection, then Anami's erotic `simmer`, then adds:

`You need both. Affection has to be safe from escalation, and the erotic current has to stay alive.`

The examples already establish both functions. This sentence is a strong candidate for explanatory synthesis after the thought has already been demonstrated. If the section fails, test removal before inventing a third formulation. Also inspect `The opposite failure...` only if necessary; the real relation can be spoken directly without manufacturing a symmetrical two-pole framework.

### Casual sex / situationship

The historical short AI window includes:

`The STI part is easy: say what you know, or say you don’t know. Feelings aren’t.`

This is the same metrical-antithesis / paired-verdict shape Joel identified in Part 2. The next sentence already performs the substantive point: two people can sincerely intend `only sex` and one can still become attached.

If the full section fails there, remove the `easy / aren't` verdict machinery and move directly from honest STI disclosure into the unpredictable attachment consequence. Do not add a new abstract principle explaining the contrast afterward.

### Crucible

The historical AI window is the protected safety exit:

`One warning before I romanticize the crucible too much...`

The function is non-negotiable: distinguish mutual wounded triggering from terror/control; preserve fear of saying no, telling the truth, or leaving; get other people involved; safety first.

Do not rewrite this paragraph merely because the old short window was red. First test the complete natural Crucible section. If a faithful alternative is actually required, preserve all actors/agency and make the safety limit a direct boundary on how far Joel applies the crucible idea, not a generalized safety taxonomy.

### Maturity levels — cross-half natural section

The arbitrary half split occurs inside the patient/guru sequence, so the historical final Part1 red window may be a boundary artifact. Diagnose the whole natural section across both halves.

Independent editorial issue at the opening: the heading already says `When you and your partner are at different levels of maturity`, but the first paragraph re-explains the category in abstract terms (`different maturity levels ... extremes ... too unequal ... pendulum swing or backlash`) before reaching Joel's actual experience.

If the natural section fails, begin with what happened in the three reference relationships: Joel repeatedly became the responsible one — therapist/guru/doctor/dad — and once that became the default, he also became the person held responsible for everything that went wrong. Preserve the pendulum/backlash idea and the later Toft, daddy/little-girl, patient/guru, self-implication, and complementarity material. Do not manufacture a symmetrical maturity taxonomy.

## Part-2 lessons being applied upstream

1. **Do not paraphrase the same architecture indefinitely.** Two faithful rewrites of the generalized female-side symmetry in `Not A Performance` failed/worsened; deleting the unnecessary symmetric container produced 100% Human.
2. **Challenge the paragraph's job before version three.** A stubborn span may be a duplicate summary, mandatory symmetry, or mini-essay closure rather than badly worded necessary content.
3. **Natural sections outrank detector windows as rewrite units.** A tiny AI window may disappear in a coherent section, while individually Human thoughts can compose into a model-shaped section.
4. **Let examples/consequences conclude the thought.** Do not add a synthesis sentence after the examples have already made the inference available.
5. **Preserve asymmetric thought.** Fairness does not require mirrored male/female, self/partner, pro/con, or safety counterweights when Joel's causal route is genuinely uneven.
6. **Rhythm is multi-scale.** Inspect metrical antithesis at sentence scale, equalized thought-duration at paragraph scale, and recursive mini-essay/outline pulse at section scale.
7. **Preserve epistemic friction and reader relation.** Do not convert odd observations, uncertainty, jokes, or genuine direct address into neutral report prose; also do not add these as detector charms.
8. **Compression can make prose more model-shaped.** Remove scaffolding and aftercare, not the causal/personal material that makes the thought live.
9. **Detector green is not editorial authority.** A green variant with a duplicate or residual owner-perceived AI shape still gets repaired/cold-audited.
10. **Six-call guard is per genuine local section.** Aggregate halves remain fully accounted/cached but are not one capped repair section.

## Next action

Recover the pending five-section baseline batch before any repeat. Leave green/coherent sections alone. For each failing section, apply the smallest architecture-level repair justified by this diagnosis, test that complete natural section under its own budget, then deterministically integrate only passing/editorially sound realizations into the current `materialized-owner-integrated-r2` article candidate. After Part1 local repair, run a fresh changed-Part1 aggregate measurement; do not infer an aggregate pass from section greens.
