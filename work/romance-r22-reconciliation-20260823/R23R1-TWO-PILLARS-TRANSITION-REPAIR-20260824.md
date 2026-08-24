# Romance r23r1 — Two Pillars localized transition repair

Updated: 2026-08-24
Status: **SUPERSEDED / REJECTED BY OWNER TEST.** Joel reports this ordering tested AI / low confidence. It was not materialized into article authority; exact owner-final r23r2 supersedes it.

## Exact localization evidence

Joel manually read the already-paid Pangram 4 report and supplied the exact AI-highlighted span for r23 Part 2 SHA-256 `a0dce58d2958e8467c1ba66cbed20b7c7ae075b8eddc7e1365eb8728485ff7f3`:

`Community isn't magic either; if both people are falling apart, there is only so much anyone else can do. But sometimes a friend who actually knows us both sees the pattern before either of us does.`

This is owner-supplied visual localization evidence from the existing report. It is **not** a new detector call. The stored Part-2 result remains Pangram 4.0 Human `0.9965084195`, AI `0.0034915956`, AI-assisted `0.0`.

## Localization interpretation

The highlighted span crosses the r22 → r23 edit boundary:

- `Community isn't magic either; if both people are falling apart, there is only so much anyone else can do.` is unchanged r22 wording inside the exact known-green r22 Part 2.
- `But sometimes a friend who actually knows us both sees the pattern before either of us does.` is the owner-selected R23-04 missing-function recovery.

Therefore the highlight is evidence for a **contextual transition residual**, not proof that either sentence independently caused the classification. It specifically rules out the previously frozen R23-03 voice fallback as the first production repair target.

## Editorial diagnosis

In r22, the community-limit sentence was followed directly by the B. example and lived normally inside the known-green boundary. R23-04 inserts a generalized positive community function immediately after it. In the new combined transition, the abstract opener `Community isn't magic either;` now performs largely defensive/qualifying work that the remainder of its own sentence already performs concretely: `if both people are falling apart, there is only so much anyone else can do.`

The pair therefore becomes a neat caveat → counterpoint sequence:

- community is not magic / has limits;
- but sometimes a mutual friend sees what the couple cannot.

The substantive limitation is worth preserving. The generic `Community isn't magic either;` wrapper is no longer needed to preserve it.

## Frozen r23r1 repair candidate

Authoritative r23 local source:

`Maybe an unusually strong couple can get away without much community. I think that's rare. Community isn't magic either; if both people are falling apart, there is only so much anyone else can do.`

`But sometimes a friend who actually knows us both sees the pattern before either of us does.`

Candidate:

`Maybe an unusually strong couple can get away without much community. I think that's rare. If both people are falling apart, there is only so much anyone else can do.`

`But sometimes a friend who actually knows us both sees the pattern before either of us does.`

Only the four-word realization wrapper `Community isn't magic either;` is removed. Joel's R23-04 sentence remains byte-exact and in the same location.

## Reduced D2 preservation proof

Preservation units:

1. `PU-R23R1-01` — unusually strong couples may sometimes manage without much community; must remain here. **Preserved exact.**
2. `PU-R23R1-02` — Joel thinks such couples are rare; must remain here. **Preserved exact.**
3. `PU-R23R1-03` — community has limits when both partners are falling apart; may reword semantically. **Preserved by** `If both people are falling apart, there is only so much anyone else can do.`
4. `PU-R23R1-04` — a mutual friend who knows both partners may see a pattern neither partner sees; owner-selected wording; must remain exact. **Preserved byte-exact.**
5. `PU-R23R1-05` — transition into the B. lived example remains immediately after R23-04. **Preserved.**

Authorized change whitelist:

- may remove only the generic `Community isn't magic either;` wrapper from the preceding known-green sentence to repair the newly localized transition;
- may not change the substantive community-limit claim;
- may not change, move, paraphrase, or punctuate Joel's R23-04 owner wording;
- may not change the B./H. examples or any other Part-2 prose;
- may not reopen R23-03 or R23-05 without independent evidence.

Forward traceability: **PASS**.
Reverse traceability: **PASS**.
Unexplained substantive deltas: **0**.
Claim/certainty/agency/chronology changes: **none**.
Owner-final R23-04 wording: **preserved exact**.

## Cold audit

The repaired thought movement is:

1. two people alone are usually not enough;
2. even outside help has a real limit when both people are collapsing;
3. nevertheless, one concrete thing a mutual friend can sometimes do is see a pattern the couple cannot;
4. the B. example immediately makes that claim lived rather than theoretical.

No additional explanation is required before the B. example. The repair removes a generic disclaimer wrapper but keeps its substantive limit.

AI-shape issue still believed after repair: **none in this localized transition**.

## Detector status / cancelled historical gate

Supersession update: Joel manually tested this r23r1 ordering and reported **AI / low confidence**. He then supplied the structurally reordered exact r23r2 realization, reported **Human / low confidence**, and accepted it as `good enough`. The steps below are retained only as historical provenance and must not be executed as current routing.

The following planned gate is cancelled and retained only to show what r23r1 would have required before Joel superseded it:

1. materialize exact r23r1 from exact r23, changing only the frozen four-word deletion above;
2. verify zero other deltas and rerun the bounded Two Pillars + article architecture/preservation checks;
3. certify only the changed exact Part-2 reader boundary through the authenticated GUI under the current large-text cost rule;
4. never resubmit r23 Part 1.

Do not execute those steps. Current routing is exact r23r2 under `R23-CURRENT-STATE.md`.
