# Somatic conversation handoff supplement — V7 anchor + specificity reconciliation 050 — 2026-09-10

Status: **CURRENT V7 RECOVERY SUPPLEMENT / CORRECTS SPECIFIC DEFECTS IN 048 AND 049 / NOT ARTICLE PROSE AUTHORITY / NO PANGRAM / NO INSTALLATION**

This supplement continues `SOMATIC-CONVERSATION-HANDOFF-SUPPLEMENT-20260910-V7-SOURCE-RESTORATION-049.md` after a fresh source/native-object reconciliation and specificity check against the current Pangram-lab Somatic controls.

Where this file conflicts with 049 on exact detector-boundary identity or with Stage-1 assembly 048 on protected-object installation readiness, this file controls the recovery state.

## 1. Exact Stage-2 detector-boundary identity correction

Handoff 049 gives an incorrect SHA-256 for the exact owner-reported Human / medium Stage-2 cluster.

The controlling local detector record is:

`SOMATIC-STAGE2-CLUSTER-OWNER-REPORTED-HUMAN-MEDIUM-20260910.md`

The Pangram-lab record independently stores the same exact boundary and identity.

Correct exact identity, with **one trailing newline**:

- whitespace word count: **144**
- UTF-8 bytes: **813**
- SHA-256: `de702d03dfa29c866b1da337175436bef01a092267e7de2a10ff617dac236436`

The `702466...` value in handoff 049 is metadata drift and must not be used as the boundary identifier.

This correction does **not** change the prose or detector result. The exact boundary remains owner-reported **Human / medium confidence**. No detector rerun is warranted merely to correct metadata.

## 2. Stage-1 assembly 048 is not protected-object installation-safe as written

Assembly 048 remains useful as a prose/architecture owner-review surface, but its preservation verdict missed two source-object deltas in the Gentle Shaking / TRE boundary.

### A. TRE YouTube native object omitted

The 2026-09-05 live-source merge receipt proves that the current live-source object manifest contains, in order:

- source island 6: YouTube — Somatic Experiencing;
- source island 7: YouTube — TRE/shaking;
- source island 8: YouTube — Brainspotting;
- source island 9: YouTube — EMDR.

The working merged reader also explicitly marks the TRE YouTube embed at its current local position.

Assembly 048 preserves a placeholder for the Somatic Experiencing YouTube object but omits the TRE/shaking YouTube object entirely.

**Required installation correction:** preserve the exact live-source TRE/shaking native object (source island 7) in its existing local relation: after the Gentle Shaking owner-source paragraph and before the adjacent neck-safety paragraph.

Do not reconstruct the object from stale `master.html`; use the current live-source/native-object manifest and canonical helper workflow when materializing raw editor HTML.

### B. TRE hyperlink silently changed

The 2026-09-05 working merged reader carries:

`https://traumaprevention.com/frequently-asked-questions/`

for the Stage-1 TRE heading link.

Candidate 047 / assembly 048 instead use:

`https://treprovider.com/`

The recovered owner-source record 030 supplies the stronger owner shaking thought but does not supply authority for changing this link. The link mutation is therefore unexplained.

**Required installation correction:** retain the current live-source TRE link unless Joel explicitly changes it or later source review establishes a deliberate replacement. Do not change the owner-source shaking prose merely to fix the link.

### Revised verdict for 048

- prose/source-restoration architecture: remains preferred/provisionally usable for owner review;
- semantic safety correction from 047: retained;
- protected native-object/link preservation: **FAIL as written; repair is mechanical and specified above**;
- installation readiness: **withheld until those object corrections are applied in any materialized assembly**.

This is not a humanization-strategy failure. V7 already classifies links/native objects as protected objects. The failure occurred at assembly verification.

## 3. Stage-3–5 patch 045 protected-object reconciliation

Patch 045 is compatible with the current live-source native-object manifest on the touched boundaries, contingent on using the live-source objects rather than reconstructing them:

- Aquatic insertion occurs before Brainspotting and does not consume or replace a native object;
- Brainspotting replacement explicitly preserves the existing Brainspotting YouTube object (live-source island 8) in place;
- the Further Reading link remains reader-visible after that object;
- Stage-4 EMDR replacement explicitly preserves the existing EMDR YouTube object (live-source island 9) in place;
- the new `Deep Hypnosis and Other Deep Memory Work` H2 and exact protected deep-memory paragraph occur after the EMDR object, so they do not alter the object identity;
- Stage-5 removes only the nested heading and leaves its paragraph/links untouched;
- downstream Sky Hypnosis/native objects are outside the patch and remain untouched.

No new protected-object defect was found in patch 045 during this bounded reconciliation.

This is still an owner-review patch, not installed authority.

## 4. V7 specificity check against detector controls

The current detector evidence supports V7 more narrowly than a generic `natural cadence` theory.

### Positive / tolerated boundaries

- Aquatic Bodywork / Water Therapy: owner-reported **Human / medium**; thought content/topology substantially owner-supplied; sentence realization model/editorial.
- Stage-2 144-word SE -> shaking -> optional settling -> EFT/head-massage cluster: owner-reported **Human / medium**; mixed provenance with direct owner cognition/owner-backed material plus bounded model/editorial realization and assembly.
- V5 83-word thought specification: owner-reported **Human / low**; model realization tightly constrained by direct owner thought topology.
- compact SE boundary: owner-reported **Human / low** in the existing lab record.

### Negative controls

- independent night-walk prose from only the topic `why people enjoy walking at night`: owner-reported **AI / high**, despite varied sentence length, concrete sensory detail, and locally plausible prose flow.
- Stage-1 Yoga generation probe: owner-reported **AI / medium**; it used Joel-relevant content but repeatedly completed positive propositions with neat contrasting/negating closures (`That can be...`, `It doesn't have to...`, `I'm talking about X, not Y...`).
- earlier broad model-only Somatic Job-2 rewrites remain the replicated **AI / high** stop-rule evidence recorded by V7.

### Discriminating hypothesis

Current evidence does **not** support `humanization = more sensory detail`, `more sentence-length variation`, `first person`, `shorter passages`, or a phrase blacklist.

The best-supported production distinction is currently:

**preserve owner cognition/topology and reduce the model's authority to select, complete, balance, and serialize conceptual jobs.**

The positive boundaries let the model realize or minimally assemble thought whose substantive topology already came from Joel/owner source. The strongest negative control let the model originate both the thought sequence and prose from a bare topic. The Yoga negative further shows that owner-relevant subject matter alone is insufficient when the model resumes its own contrast-completion architecture.

This remains a hypothesis, not a causal detector law. Boundary length, exact wording, context, and other correlated variables are not isolated.

## 5. Operational refinement to V7

Do **not** create V8 merely from these findings. V7's causal premise remains supported enough to continue, and adding more generation prohibitions would risk turning the rule set itself into the writing environment.

Instead, add one execution gate to V7 practice:

### Protected-object manifest gate

Before calling any whole-stage or multi-section assembly preservation-clean / installation-ready:

1. identify the newest controlling live-source/native-object manifest for the touched span;
2. enumerate protected native objects and source links that must survive;
3. map every placeholder in the reader candidate to the corresponding source object identity;
4. compare link destinations as objects, not merely visible anchor text;
5. preserve local safety/native-object adjacency unless direct owner/source authority changes it;
6. withhold preservation PASS if an object disappears, moves across a governing boundary, or changes identity without authority.

Do not use stale `master.html` as the current object manifest when a newer live-source receipt controls.

This gate is mechanical custody verification. It must not become another composition checklist for prose generation.

## 6. Current production state after reconciliation

### Stage 1

Assembly 048 remains the current preferred owner-review prose architecture **subject to the two mechanical object corrections above**.

The anti-endless-capacity / capacity-building-as-avoidance function remains unresolved at explicit Stage-1 surface level. Do not equate it automatically with the Jules/MCT anti-processing off-ramp: they overlap but target different failure modes. The owner-rejected `endless waiting room` wording remains retired.

### Stage 2

Preserve the exact known-green 144-word cluster unchanged.

The substantive blocker is still global topology, not sentence humanization:

- opening realization G1 remains model-only;
- first substantive island G2 lacks owner order authority;
- Louka relative to the SE/shaking relation G3 remains unresolved and same-source inference is exhausted;
- technical Shaking reference-surface placement G4 remains unresolved;
- the local post-shaking -> EFT relation is supported but is not global Stage-order authority;
- solar/heart remains the accepted end-of-Stage island before Stage 3.

Do not attack these with another model rewrite.

### Stages 3–5

Patch 045 remains the current preferred owner-review patch. The bounded object reconciliation found no new anchor defect.

### Whole article

Do not create a combined near-final installation candidate until Stage-2 topology receives owner authority. No publication/export. No Pangram unless Joel explicitly requests it.

## 7. Smallest genuine owner-cognition boundary

Autonomous source recovery and same-context inference have now done what they can without laundering model order into authorial order.

The next useful owner input is not a prose rewrite. It is topology:

- what thought Joel naturally wants immediately after the Stage-2 heading/function;
- whether Louka's testimonial belongs before or after the SE/shaking explanation, or in its own Shaking-Qigong location;
- whether the Shaking dose/use/mechanism material should appear as a compact reference surface, and where Joel expects to encounter it.

Until that arrives, preserve Stage 2 as a partial assembly and continue no same-method topology inference.
