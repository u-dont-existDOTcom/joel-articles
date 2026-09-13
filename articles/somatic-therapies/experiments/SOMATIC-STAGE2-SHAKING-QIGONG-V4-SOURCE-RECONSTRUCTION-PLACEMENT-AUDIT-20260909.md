# Somatic Stage 2 — Shaking Qigong V4 source reconstruction + placement audit — 2026-09-09

Status: **SOURCE RECONSTRUCTION COMPLETE / V4 GATE D FAIL FOR NEW NARRATIVE PROSE / ROUTE 3 BOUNDARY / NO NEW PROSE / NO PANGRAM**

Branch:
`task/somatic-intro-progress-controller-20260831`

Controlling strategy:
`articles/somatic-therapies/experiments/SOMATIC-HUMANIZATION-STRATEGY-V4-AUTHORITY-FIRST-COMPOSITION-ROUTING-20260909.md`

Trigger:
`articles/somatic-therapies/experiments/SOMATIC-STAGE2-SHAKING-QIGONG-V3-PROSPECTIVE-001-AUDIT-AND-STRATEGY-SWITCH-20260909.md`

Target working reader:
`articles/somatic-therapies/WORKING-MERGED-READER-PROSE-20260905.md`

No article authority, working reader prose, publication state, or detector state is changed by this audit.

## 1. Why this audit was required

V3 prospective-001 failed because the supervisor correctly identified different source/genre roles and then allowed those diagnostic roles to become publication paragraph structure.

V4 therefore required source reconstruction before any more Shaking prose:

1. recover the exact supplied-source material where durable evidence permits;
2. separate semantic custody from model realization;
3. determine destination obligations without freezing current paragraphing by inertia;
4. determine the composition frontier;
5. run the Gate-D sufficiency test before writing.

## 2. Exact recovered source evidence

The Pangram humanization lab's `automation/pangram-fixed-batch` branch contains frozen exact-text experiment specs from the original 2026-08-22 Shaking audit. These files are used here only as durable exact-text provenance. No detector result is inferred or requested.

### A. Original supplied-source Shaking boundary

Experiment:
`somatic-therapies-shaking-qigong-r02-original-source-20260822-a`

Variant:
`SHAKING_QIGONG_R02_ORIGINAL_SOURCE`

Frozen experiment blob SHA:
`726371cd3786c7d539bafa6ed41b855dfa6fc9b5`

The exact source was explicitly card-structured:

- `Goal: Daily autonomic discharge and energetic decompression.`
- Louka/source recommendation paragraph;
- Stage/Phase distinction paragraph;
- `Mechanism, mainstream interpretation:` followed by six items;
- `Mechanism, qigong interpretation:` followed by four items;
- `Best use:` followed by five items;
- `Not ideal as:` followed by four items;
- `The Discharge → Settle Stack` followed by the three-step sequence and yin caveat.

This is crucial: the supplied source establishes **semantic content**, but its visible topology is itself the repeated modality-card architecture the humanization work later tried to dismantle. It is therefore not evidence of a natural Joel thought route merely because Joel supplied the article source.

### B. r01 Shaking realization

Experiment:
`somatic-therapies-shaking-qigong-r01-baseline-20260822-a`

Frozen experiment blob SHA:
`ae47e403f2a28590c68f902ecca474ca746ab73b`

The r01 prose converted the source cards into continuous prose. Relevant transformations include:

- source `Goal:` -> `Here the job is daily autonomic discharge and energetic decompression.`
- source Phase-1/Phase-2 distinction -> continuous Stage/Job paragraph;
- source `Best use:` inventory -> `A regular practice might run 10–45 minutes. I think of the use cases as ...`
- mainstream mechanism list -> one sentence beginning `You do not have to accept the qigong explanation...`
- qigong mechanism list -> one explanatory paragraph;
- `Not ideal as:` list -> one catharsis/primary-modality/skilled-help warning paragraph.

This confirms that `I think of the use cases as...` is an r01 realization wrapper, not wording recovered from the original supplied source.

### C. Historical r02 source-stack candidate

Experiment:
`somatic-therapies-shaking-qigong-r02-source-stack-20260822-a`

Frozen experiment blob SHA:
`13623386b9e7aa43630916a3e9ebd257c79c6ac6`

This historical candidate selected:

1. the Louka source paragraph;
2. the gentle-early-shaking versus regular-discharge distinction;
3. the Discharge → Settle sequence and yin caveat.

It omitted the standalone Goal label, both mechanism blocks, the Best-use inventory, and the Not-ideal block from that candidate boundary.

`articles/somatic-therapies/HUMANIZATION-REPORT.md` records this as a frozen rollback/consolidation candidate that had not been submitted at that checkpoint.

Disposition here:
**editorial experiment evidence only.** It shows that an earlier worker also saw a possible narrower source spine, but it does not establish Joel's natural thought order and is not article authority.

## 3. Provenance correction — the use contexts are source-derived

The V3 audit had already established that the 10–45 minute range was source-derived. Exact source recovery now resolves the remaining ambiguity too.

The original supplied source's `Best use:` block contains:

1. `10–45 minute regular practice`
2. `Non-verbal emotional processing`
3. `Chronic freeze patterns`
4. `Stress accumulation between therapy sessions`
5. `Post-therapy discharge when activation remains in the body`

Therefore the current r01/merged working-copy content:

`A regular practice might run 10–45 minutes. I think of the use cases as chronic freeze, non-verbal emotional processing, stress that accumulates between therapy sessions, and leftover activation after a deeper session.`

contains **source-derived semantic content** for the duration and four contexts.

But the following are r01/model realization rather than recovered source wording/topology:

- `I think of the use cases as`;
- the reordered list;
- `leftover activation after a deeper session` as a rephrasing of the source's `Post-therapy discharge when activation remains in the body`;
- the decision to put the whole inventory into one continuous narrative paragraph after the Stage distinction.

This means the content has semantic custody, while the wrapper/order/paragraph role does not have owner-topology authority.

## 4. V4 Gate A — authority/source-role map

| Material | Highest supported role | Reason |
|---|---|---|
| Louka tried many modalities/basic TRE and this class finally helped him | `SOURCE_SEMANTIC` + current protected function | Present in exact supplied source; current owner locks protect Louka's report. Current r01 wording is a later realization, not proven natural-owner exact prose. |
| Shaking Qigong is shaking + qigong / linked class context | `SOURCE_SEMANTIC` | Present in supplied source; wording changed in r01. |
| Daily autonomic discharge + energetic decompression | `SOURCE_SEMANTIC` + `ARCHITECTURE_OBLIGATION` | Exact source Goal content; Stage 2 current architecture preserves regulation/discharge function. Goal label itself is scaffold. |
| Early/Stage-1 shaking gentle/exploratory versus Stage-2 regular discharge | `SOURCE_SEMANTIC` + `ARCHITECTURE_OBLIGATION` | Exact supplied source plus current Stage-2 state explicitly requires the small Stage-1 dose versus regular Stage-2 discharge distinction. |
| Ability to stop, orient, and settle afterward | `SOURCE_SEMANTIC` + protected safety function / `TECHNICAL_OBJECT` | Exact supplied source; current safety locks preserve stop/return capacity. |
| 10–45 minute regular practice | `SOURCE_SEMANTIC` + `TECHNICAL_OBJECT` | Exact supplied-source Best-use item; also independently recorded as source-derived in `HUMANIZATION-REPORT.md`. |
| Non-verbal emotional processing | `SOURCE_SEMANTIC` | Exact Best-use item. |
| Chronic freeze patterns | `SOURCE_SEMANTIC` | Exact Best-use item. |
| Stress accumulation between therapy sessions | `SOURCE_SEMANTIC` | Exact Best-use item. |
| Post-therapy discharge when activation remains in the body | `SOURCE_SEMANTIC` | Exact Best-use item; current r01 wording is a paraphrase. |
| `I think of the use cases as...` | `MODEL_REALIZATION` | Not present in recovered source; introduced by r01 continuous-prose realization. |
| Mainstream mechanism items | `SOURCE_SEMANTIC` + `TECHNICAL_OBJECT` | Exact supplied-source mechanism inventory. |
| Qigong mechanism/explanatory items | `SOURCE_SEMANTIC` + `TECHNICAL_OBJECT` + current evidence-plane function | Exact supplied-source energetic inventory; current state protects evidence-plane separation. |
| Not-ideal / catharsis / severe-PTSD / primary-modality / skilled-help limitations | `SOURCE_SEMANTIC` + safety `TECHNICAL_OBJECT` | Exact supplied-source block; current state protects catharsis/instability safety function. |
| Discharge → Settle three-step sequence | `SOURCE_SEMANTIC` + current protected sequence / `TECHNICAL_OBJECT` | Exact supplied source and current state explicitly keeps the sequence. |
| `Goal`, `Mechanism...`, `Best use`, `Not ideal as` labels as prose architecture | `MODEL_REALIZATION` / inherited scaffold for current humanization purposes | Their semantic contents survive, but the repeated card taxonomy is the known source architecture being humanized. |

No `OWNER_TOPOLOGY` is established for the transition from Louka's report through the Stage distinction, duration, use contexts, mechanisms, and warning.

## 5. V4 Gate B — custody/destination map

This audit distinguishes `where content must survive` from `what the next paragraph must say`.

### Louka report
Disposition: **`SEMANTIC_HERE` / same Shaking subsection**, currently protected in this location absent a real defect.

### Stage-1 small dose versus Stage-2 regular discharge
Disposition: **`SEMANTIC_HERE` / same Shaking subsection**.

Reason: current Stage-2 state explicitly preserves this distinction as part of the current article architecture.

### Stop / orient / settle capacity
Disposition: **`SAME_SUBSECTION` with safety adjacency to the regular-discharge distinction**.

It must not be lost, but this does not prescribe sentence position or make safety the automatic closing beat of a narrative paragraph.

### 10–45 minute range
Disposition: **`SAME_SUBSECTION`**.

Reason: source-derived Shaking parameter with no current supersession. Exact sentence/paragraph placement is not locked.

### Four source-derived use contexts
Disposition: **`SAME_SUBSECTION`**.

Reason: they are source content in the Shaking `Best use` block and no owner deletion/supersession was recovered. Their order/grouping/wrapper is not locked.

### Mechanism / qigong explanatory material
Disposition: **`SAME_SUBSECTION`**; current working placement is compatible with the owner-accepted merge direction and current evidence-plane requirement.

### Not-ideal / catharsis / instability safety
Disposition: **`SAME_SUBSECTION` with safety adjacency**.

### Discharge → Settle sequence
Disposition: **next named subsection/sequence, current destination preserved**.

This is a genuine finite sequence; V4 does not treat its list structure as a humanization defect.

## 6. V4 Gate C — composition frontier

The key result is that semantic custody is much richer than the narrative frontier.

### `LIVE_NOW`
**None established beyond the already protected Louka report.**

The exact supplied source moves from Louka to a Phase/Stage distinction because its card architecture says that is the next slot. That is source ordering, but not enough evidence to call it Joel's natural cognitive movement.

### `SUPPORT_NOW`
If/when a natural Stage-2-use thought is recovered, the stop/orient/settle safety condition is eligible as local support because it materially constrains the practice.

### `CUSTODY_ONLY`
Until a real thought route reaches them:

- 10–45 minute range;
- non-verbal emotional processing;
- chronic freeze patterns;
- stress accumulation between sessions;
- post-therapy discharge/remaining activation.

These must survive, but V4 specifically blocks using them as the writer's composition checklist.

### `TECHNICAL_SURFACE`

- mainstream mechanism inventory;
- qigong explanatory inventory/evidence-plane distinction;
- catharsis/severe-instability safety limitations;
- Discharge → Settle finite sequence;
- 10–45 minute range may also be treated as a finite parameter when its final surface is decided.

### `NEEDS_AUTHOR_COGNITION`

The missing unit is not another fact. It is the **governing authorial relation after Louka's report**:

> Why does Shaking Qigong belong in Stage 2 for Joel, and which of the source-derived dose/use facts are actually part of that live thought rather than reference material that merely needs to survive somewhere in the subsection?

### `SCAFFOLD_DROP`
As composition drivers:

- Goal-card wrapper;
- Mechanism-card wrapper;
- Best-use-card wrapper;
- Not-ideal-card wrapper;
- r01 `I think of the use cases as` first-person taxonomy wrapper;
- any new supervisor-created `narrative paragraph` / `reference paragraph` division that simply reproduces those cards under new names.

## 7. V4 Gate D — sufficiency result

Question:

**After removing model/card scaffold and custody-only obligations, is there enough authorial/source thought movement left to justify a new reader-facing narrative realization?**

Result: **NO. GATE D FAIL.**

What remains is:

- a protected/source-grounded Louka report;
- a required Stage-1 versus Stage-2 distinction;
- a safety condition;
- several source-derived parameters/use contexts;
- technical mechanism/evidence/safety objects;
- a real later Discharge → Settle sequence.

That is a strong semantic/source bank but not a recovered authorial thought topology.

The historical r02 source-stack candidate does not change this verdict. Its narrower selection is an editorial experiment, not direct owner cognition.

## 8. Route after V4 gates

### Louka
Preserve under current Route 0/1 treatment absent a named defect.

### Mechanism/evidence/safety/stack
Route 4 as appropriate finite technical/evidence/safety material. Do not narrativize merely to sound Human.

### Missing Stage-2 Shaking narrative relation
**Route 3.**

Source recovery is now sufficiently exhausted for this local question: exact original supplied-source text and the historical rollback candidate were recovered, and neither supplies a natural owner thought route.

Do **not** generate another prose candidate from the existing bank.

## 9. Exact high-information owner variable

The one irreducible cognition needed before another Shaking narrative realization is:

**After the Louka paragraph, what is the actual reason Joel wants Shaking Qigong in Stage 2, and how much of the source's regular-dose / 10–45-minute / freeze / non-verbal-processing / between-session-stress / post-session-discharge material belongs to that thought rather than merely being useful reference information?**

Reader-visible placement context:

- article: Somatic Therapies;
- Stage 2: `Regulate or Discharge Accumulated Activation Energy`;
- subsection: `Shaking Qigong / Shaking Medicine`;
- immediately before: Louka report that the linked class helped him after many modalities/basic TRE had not;
- immediately after the unresolved narrative slot: ordinary mechanism explanation, qigong evidence-plane explanation, catharsis/instability warning, then the separate Discharge → Settle sequence.

This question targets reasoning/priority/stopping point, not wording and not autobiography.

## 10. Strategy evidence disposition

This audit materially supports V4's distinction between:

`semantic custody`

and

`composition eligibility`.

The exact source recovery demonstrates the failure mode cleanly: a source can contain valid material under a `Best use` card, while a later continuous-prose rewrite can preserve every item yet still lack any evidence that the list is the author's next live thought.

However this remains **same-context, article-specific strategy evidence**. Do not promote V4 project-wide yet.

## 11. Current stop state

- Shaking V3 prospective-001: rejected.
- Shaking V4 source reconstruction: complete.
- Source provenance of duration/use contexts: resolved as source-derived semantic content.
- Natural owner topology for the narrative transition: not recovered.
- Gate D: FAIL.
- Route: Route 3 for the missing narrative relation; Route 4 for technical surfaces.
- New Shaking prose: **BLOCKED pending the one authorial cognition variable above.**
- Pangram: **NOT RUN.** Existing historical Shaking detector reservation remains quarantine-only and must not be repeated from this task.
