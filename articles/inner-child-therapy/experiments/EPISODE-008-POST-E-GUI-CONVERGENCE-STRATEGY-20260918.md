# Episode 008 — strategy correction after Candidate E Pangram failure

Date: 2026-09-18
Status: **CANDIDATE E FAILED / OWNER-DOMINATED GREEN DOES NOT COUNT AS MODEL PROGRESS / ITERATE RED REGIONS WITH GUI DETECTOR**

Evidence:
`EPISODE-008-PHASE-B-CANDIDATE-E-OWNER-PANGRAM-RESULT-20260918.json`

## Owner correction

Joel correctly pointed out that the previous localization claim was overstated:
the Human/high middle was overwhelmingly his already-known owner-authored paragraph.

Candidate E then returned:
- opening 113 words AI/high;
- middle 110 words Human/high;
- ending 74 words AI/high.

The model-written repairs therefore failed.

## Process correction

Do not treat a detector segment as evidence of model humanization merely because it is green when almost all of its content is already owner-authored Human prose.

For model-capability progress, track the **model-written red surfaces** separately.

The combined middle block remains useful as a stable context boundary, but it is not evidence that the model learned to humanize.

## Detector cadence correction

The owner had already authorized and preferred the cheaper Pangram GUI route.

The previous Candidate E workflow incorrectly inserted an owner-visual checkpoint before using the detector again.

That gate is removed for the current convergence loop.

New rule for this lane:

`generate localized red-region repair -> preservation check -> negative blocker check -> if not trivially broken, run Pangram GUI -> use segmentation -> repeat`

Owner review still outranks detector evidence, but it is not a mandatory gate before every GUI measurement.

## Next edit scope

Keep exact:
- owner paragraph;
- `If you really did hurt them, repair it.`;
- `You can mean the apology.`

Reason:
these sit inside the current Human/high middle context. This is a working contextual lock, not proof that the two short model sentences are independently Human.

Repair only:
1. AI/high opening region;
2. AI/high final region beginning `Then you notice you're also apologizing...`.

## Measurement routing

Use Pangram GUI for the next candidate.

Prefer:
Remote Desktop Commander -> Joel laptop -> deterministic `pangram-local` / dedicated profile.

Do not use API unless GUI/local execution genuinely fails and Joel authorizes the fallback.

## Success signal

Progress means:
- either AI/high region shrinks or flips Human in the complete integrated boundary;
- or the detector supplies a new useful boundary that changes edit scope.

Do not celebrate owner-dominated green as model progress.