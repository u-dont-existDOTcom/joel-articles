# Somatic Therapies — V7 owner-review patch 027 — 2026-09-10

Status: **CURRENT NON-AUTHORITATIVE OWNER-REVIEW PATCH / SUPERSEDES PATCH 022 / ZERO UNEXPLAINED SUBSTANTIVE DELTAS / NO PANGRAM**

Base reader: `articles/somatic-therapies/WORKING-MERGED-READER-PROSE-20260905.md`.

Patch 027 retains the clean Stage-3/5 operations from patch 022 and adds the Stage-4 structural solution from candidate 026. Stage 2 and Stage 1 remain outside this patch.

## Operation 1 — Stage 3: insert exact known-green Aquatic passage

Immediately after the Stage-3 opening paragraph and before `## Brainspotting`, insert unchanged:

```markdown
## Aquatic Bodywork / Water Therapy

Hale is trained in aquatic bodywork, and she finds the water especially effective for bringing people back toward their inner child. Sometimes people get so young in the water that they feel as if they're back in the womb. There's also a physical side to it that I find interesting: floating lets somebody stretch and move you through positions that would be difficult or impossible to get into the same way on land.

Some people are just prone to ear infections, even with clean water and earplugs, and for them this may not be worth doing very often.

Hale says water therapy can open someone up emotionally a lot more than expected. Before the water, she likes to do some inner-child work and see what the person is feeling and what they want to work on. I would ask a water therapist about this before booking: if a lot gets opened up, are you still available afterward if I need more help with it?
```

Exact Aquatic boundary: owner-reported Human / medium confidence. Do not transfer that result to surrounding Stage 3.

## Operation 2 — Stage 3: delete only the `After Brainspotting` wrapper heading

Delete:

```markdown
## After Brainspotting
```

Keep the paragraph beginning `I would resist the urge to turn the rest of the day into another processing marathon.` unchanged, along with all Brainspotting prose, the Further Reading link, and native YouTube placement.

## Operation 3 — Stage 4: move exact deep-memory safety to Stage level

Move this exact protected paragraph:

```markdown
I would save deep hypnosis, immersive child dialogue, suggestive exploration, and other deep memory work for the point where you can stay present, stop voluntarily, and return to ordinary life afterward.
```

from its current position after the EMDR post-video paragraph to immediately after the Stage-4 opening paragraph and before `## EMDR`.

No wording changes.

Rationale: owner architecture assigns this rule to Stage 4 generally; moving it outside the `EMDR` H2 prevents deep hypnosis/immersive child dialogue from reading as an EMDR subtopic.

## Operation 4 — Stage 4: delete the duplicated post-video EMDR paragraph

Delete the paragraph beginning:

`I still care about regulation and what happens after the session.`

and ending:

`A stable person with one discrete event is a different case and may be ready for EMDR much earlier.`

Do not replace it.

Its functions remain in the Stage-3 -> Stage-4 hinge, Stage-3 Brainspotting treatment, Stage-4 opening, moved deep-memory safety rule, and `After EMDR` integration/safety. The 2026-09-05 accepted merge direction explicitly required avoiding this duplication.

## Operation 5 — Stage 5: delete only the nested H2

Delete:

```markdown
## Narrative and Cognitive Integration
```

Keep the paragraph beginning `CBT can show up much earlier than this.` unchanged. The Stage-5 H1 already provides the governing promise.

## Resulting Stage-3 -> Stage-5 movement

At section scale:

`Stage-3 body-before-story opening -> exact Aquatic island -> Brainspotting -> post-session guidance without a new aftercare card -> diffuse/discrete EMDR hinge -> Stage-4 target-memory opening -> Stage-level deep-memory safety -> EMDR -> technical de-armoring -> After EMDR -> Stage-5 H1 -> integration paragraph`

This is less recursive than the base reader and avoids creating a new one-paragraph `Deep Memory Work` card.

## Explicit no-change zones

- Stage 1: unchanged by this patch.
- Stage 2: unchanged by this patch; exact 144-word Human/medium SE/shaking/settling/EFT cluster remains separately frozen.
- Brainspotting prose itself: unchanged.
- EMDR introductory fit paragraph/video: unchanged.
- Neurological De-Armoring Support: unchanged and still pending its separate factual/citation review.
- After EMDR: unchanged.
- Outcome: unchanged.
- Optional high-intensity section: unchanged.
- registered stale `master.html`: unchanged.

## Preservation / source integrity

Forward traceability: **PASS**.
Reverse traceability: **PASS**.
Unexplained substantive deltas: **0**.
Source-integrity gate: **PASS**.
Known-green calibration: **PASS** — exact Aquatic wording untouched.
Native-object identity/order: **unchanged** by these operations.
Existing links: **unchanged**.

## Same-context whole-reader audit

**PROVISIONAL PASS.**

Strongest remaining risks:

1. The Stage-4 deep-memory safety sentence now appears before the first concrete Stage-4 modality. This is slightly early, but it performs a real Stage-level distinction and prevents category confusion without new connective prose.
2. The EMDR fit sentence remains an example inventory after the Stage-4 opening. It carries concrete source content and has no stronger same-function owner realization; no change is authorized here.
3. `## After EMDR` remains a visible module. Unlike the removed Brainspotting wrapper, a separate technical de-armoring H2 intervenes and the accepted merge explicitly retains the After-EMDR treatment; do not remove by analogy.

No genuinely independent fresh-reader audit was available in this same Chat context, so this PASS is non-isolated diagnostic judgment, not independent evidence.

## Installation status

Owner-review patch only. Do not install into the working reader or registered master by inertia. No Pangram call.