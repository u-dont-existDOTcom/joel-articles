# Romance r23 Part 2 highlight-recovery checkpoint

Updated: 2026-08-24

## Exact detector state

- r23 Part 2 SHA-256: `a0dce58d2958e8467c1ba66cbed20b7c7ae075b8eddc7e1365eb8728485ff7f3`
- 9,917 words
- Pangram 4.0 Human `0.9965084195`
- AI `0.0034915956`
- AI-assisted `0.0`
- stored report summary: `A single AI-generated segment`
- no repeat detector submission was used to localize this result.

## Read-only recovery history

1. Structured History localization and direct-report structured binding both failed closed at `bind_exact_history_record`; neither submitted text to the detector.
2. DOM inspector v1 falsely treated Pangram orange navigation styling as a highlight.
3. DOM inspector v2 inspected only the first report page and found no anomalous article-text style there.
4. Report-page inspector v3 paginated all seven stored report pages. Every page-level Details classification was Human. The residual was therefore smaller than a report page.
5. The three r23 Part-2 authorized edits land on different stored report pages:
   - R23-03 `Can making love be a spiritual practice?`: page 1;
   - R23-04 owner-final mutual-friend sentence: end of page 3;
   - R23-05 `I can hear a whole future...`: page 4.
6. Tooling review then found Pangram's actual `AI Highlight` control; v1-v3 had not activated it. Private-executor v4 was built to do so without detector submission.

These failures are tooling limitations, not evidence against any Romance sentence.

## Localization resolved by owner visual read

Joel manually read the already-paid Pangram report and supplied the exact AI-highlighted span:

`Community isn't magic either; if both people are falling apart, there is only so much anyone else can do. But sometimes a friend who actually knows us both sees the pattern before either of us does.`

This is direct owner-supplied localization evidence from the existing report. No new Pangram call was made.

The highlighted span crosses the exact r22 → r23 edit boundary:

- `Community isn't magic either; if both people are falling apart, there is only so much anyone else can do.` is unchanged r22 wording inside exact known-green r22 Part 2;
- `But sometimes a friend who actually knows us both sees the pattern before either of us does.` is R23-04, Joel's owner-selected missing-function sentence.

Therefore the residual is a **contextual transition window**. It does not prove either sentence independently caused the classification. It also removes R23-03 and R23-05 from the first repair target.

Pangram lab issue #110 now records this manual localization while remaining open for the generic automated History/recovery defect.

## Editorial repair decision

Cold review of the full `Two Pillars Don't Hold The Roof Up` natural section identifies one narrow realization defect created by the new juxtaposition.

In r22, `Community isn't magic either; ...` was followed directly by the B. lived example and was detector-green in that context. R23-04 inserts a generalized positive community function immediately after it. In the new transition, `Community isn't magic either;` becomes a generic defensive/qualifying wrapper immediately before `But sometimes...`, producing an unnecessarily neat caveat → counterpoint sequence.

The substantive community-limit claim remains necessary and is fully contained in the rest of the sentence: `if both people are falling apart, there is only so much anyone else can do.`

Frozen r23r1 candidate:

`Maybe an unusually strong couple can get away without much community. I think that's rare. If both people are falling apart, there is only so much anyone else can do.`

`But sometimes a friend who actually knows us both sees the pattern before either of us does.`

Only `Community isn't magic either;` is removed. Joel's R23-04 sentence remains exact and in the same place.

Full candidate and reduced D2 preservation proof:
`R23R1-TWO-PILLARS-TRANSITION-REPAIR-20260824.md`.

Preservation status for this local repair:
- forward traceability PASS;
- reverse traceability PASS;
- unexplained substantive deltas 0;
- substantive claim changes none;
- R23-04 owner wording exact;
- B./H. examples and all other Part-2 prose invariant.

The previously frozen R23-03 voice fallback is no longer the active repair target and must not be materialized from this evidence.

## Next action

1. Materialize exact r23r1 from exact r23 with only the four-word `Community isn't magic either;` deletion.
2. Verify exact delta, Two Pillars natural-section preservation, and article-wide architecture/dependency checks.
3. Certify only the changed exact Part-2 reader boundary through the authenticated GUI under the current large-text cost rule.
4. Never resubmit r23 Part 1.
5. If exact r23r1 Part 2 returns Human `1.0`, reconcile the r23r1 evidence into PR #46 and proceed toward deliberate promotion; do not alter registered main before the gate passes.
