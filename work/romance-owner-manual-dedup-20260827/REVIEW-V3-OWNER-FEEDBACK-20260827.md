# Romance review v3 owner feedback — 2026-08-27

Status: working owner-review record; **not article authority**. Current owner corrections here outrank the prior dedup candidate and must be reconciled before promotion.

## Source review identity

Imported owner export: `romance-review-v2-comments.json`

- source/manual SHA-256: `9819e1e39fd0732305026332361678bb27a1d3181ef2f02ea4c7ece1befbf466`
- R5 revised SHA-256: `71bd17886d62e509800a7856105d10359c52c5e68a687551d3556fecd4997eda`
- exported at: `2026-08-27T11:32:49.476Z`

## Explicit owner review carried forward

### Approved actual R5 changes

These v2 `keep_r5` decisions migrate to explicit green approval in review v3:

- `M1` — casual-sex community thesis consolidation/move;
- `E6` — early community explanation reduced to setup/callback;
- `E13` — reparenting paragraph as explicit earlier-readiness callback;
- `E16` — fantasy introduction compression with owner-corrected opening;
- `E19` — honesty outcome compression while retaining heading;
- `E21` — Tough Love opening consolidation;
- `E22` — Tough Love late recap removal.

No other actual change is automatically approved merely because it exists in R5.

### E18 — unresolved; owner correction required

Owner comment:

> I liked this idea tho, that we create community by relying on friends to help our relationship. How can we ever expect to have community without bringing people in close like that?

Disposition: **NOT APPROVED pending repair.**

The earlier dedup rationale correctly noticed that the Eshwar section should not repeat the full individual self-practice inventory. It incorrectly bundled a unique claim into that repetition: relying on friends for intimate, real-life relationship help is not merely `outside support`; it is one way the couple **creates and deepens community** by bringing other people into real mutual dependence.

Next prose repair must restore that function while keeping the section's distinct third-perspective/deadlock-breaking job and avoiding a repeated reparenting/meditation/body-practice checklist.

### Lower-confidence proposals

The lower-confidence proposals were never part of R5. Therefore v2 `keep_r5` or `restore_old` decisions are migrated in v3 as **proposal not approved** rather than as approval of the proposal.

- `P1` Twin Flames shortening — not approved.
- `P2` H./shared-witness trim — not approved; v2 history included `Agree` while decision remained `keep_r5`, so do not infer authorization to cut the sentence.
- `P3` Gaslighting/community-witness compression — not approved; owner comment: `I couldn't understand your actual proposal here`.
- `P4` repeated `public demonization` opening change — not approved.
- `P5` Children village compression — not approved.
- `P6` move `Why all of this sounds artificial` — not approved.

For P3, the review interface must now show exact proposed replacement text rather than a vague instruction. The current explicit proposal for review is:

> Many say it's best to save face and work things out privately, but I'd disagree. If you don't have friends who can help with the conflict, then you're really stuck. But ask for help with the conflict, not approval for your own interpretation. Both people should have a chance to speak, and good friends shouldn't automatically validate either side.

This is a proposal only; no owner approval is inferred.

## Review-interface owner corrections

Joel identified three reusable interface failures:

1. Basic approval must be visible directly on the change card. New items default red `Not approved yet`; explicit green approval is one tap and must not open a comment window.
2. Context navigation must preserve place. `See context` opens a reversible overlay/drawer and `Back to <relation id>` returns to the exact review item instead of resetting to the review-list start.
3. Edit explanations must make the actual operation evaluable. Every card needs `WHAT CHANGED`, `WHY`, `WHAT STAYS / WHERE`, and `WHAT YOU'RE DECIDING`; proposed wording changes require exact replacement/cut boundaries.

Durable general rule: `project-sources/REVIEW-INTERFACE-DIRECT-DECISION-ADDENDUM.md`.
