# Episode 007 — My Journey paragraph-level Pangram audit

Date: 2026-09-18
Status: **PARAGRAPH GATE PARTIALLY COMPLETE / ONE TESTABLE PARAGRAPH FAILED AND WAS REPAIRED / SHORT-PARAGRAPH GUI LIMIT**

Source endpoint:
`EPISODE-007-MY-JOURNEY-CANDIDATE-R8F-FINAL-RESIDUAL-20260916.json`

Original whole-boundary owner result:
Human / high / displayed 100%.

## Paragraph inventory

15 prose paragraphs, excluding headings.

## Individually measurable paragraphs on current Pangram GUI route

| Paragraph | Words | Exact result |
|---|---:|---|
| P2 — starving baby / food-bank image | 53 | **Human 1.0** |
| P4 — spiritual freedom / bypassing | 59 | **Human 1.0** |
| P5 — spirituality / conditional love | 55 | **Human 1.0** |
| P9 — no-self / therapist-resistance hypothetical | 91 | **Mixed: Human 0.5782178044 / AI 0.4217821658** |
| P13 — attachment to women / self-directed therapy | 60 | **Human 1.0** |
| P14 — protective part -> child -> adult disappears | 63 | **Human 1.0** |

All exact History identities passed on Pangram 4.0 GUI/local Playwright.

## GUI short-text limit

Current local GUI would not expose the bounded detection action for:
- P1 at 35 words;
- P3 at 48 words.

No detector submission occurred in either failed attempt.

By contrast P2 at 53 words was measurable.

Therefore paragraphs below the current GUI action threshold cannot honestly be called individually Pangram-certified. The remaining sub-threshold paragraphs are:

- P1 — 35 words
- P3 — 48
- P6 — 41
- P7 — 33
- P8 — 34
- P10 — 6
- P11 — 41
- P12 — 38
- P15 — 13

Do not pad, duplicate, or hide these inside Human anchor text to manufacture an individual paragraph pass.

Joel has directly said the My Journey section remains fairly Human overall because much of it compresses his real writing/ideas and genuine experience. Treat these short paragraphs as owner/editorially tolerated unless Joel identifies a specific problem, but keep their detector status as **not individually measurable on current GUI**, not Human-certified.

## P9 repair

Original P9 failed the new paragraph gate.

Repair A tested Human 1.0 but is rejected for fidelity because it dropped the protected possibility that the therapist may be taking the reader somewhere they do not want to go, and added `without apologizing`.

Repair B restores the full source thought and tests:

- Pangram 4.0
- Human 1.0
- AI 0.0
- exact SHA-256 `740713c10ee8f0803bdb3e9de09fe8963afbabf5ad9387980b10cc7ed3032510`
- 106 local words

Repair B remains pending Joel's editorial judgment before replacing P9 in the rolling article.

## Important diagnostic

A full My Journey boundary made with the fidelity-failing Repair A still scored only:
- Human 0.9084076881
- AI 0.0915922970

This is diagnostic only because Repair A is rejected.

It reinforces the new owner rule: whole-boundary Human-leaning results do not substitute for paragraph-level review.

## Current disposition

Leave P2, P4, P5, P13 and P14 unchanged.

P9 has a preservation-clean Human-1.0 replacement candidate.

Do not rewrite the sub-threshold paragraphs merely to make them long enough for Pangram.