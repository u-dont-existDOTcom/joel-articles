# Round r7 on section 15 v6: what each finding got

Round r7 (2026-10-17, `../make_gate.py v6 review-r7 H1-P4 H2-P1 H2-P7 H3-P2`): two meaning traces (Sonnet) of the four paragraphs v6 changed since round r4's traces (H1-P4 variant c and H3-P2 variant l from Emulate round d; H2-P1 and H2-P7 as v5 left them). The cold read, the stance check and the repeats check were not run in this round: round r4 ran them on v4, and the changes since then put published words back. The fixes are in `../make_v7.py` (v7) and `../make_v8.py` (v8); every changed paragraph goes to Pangram again (330g), and round r8 traces the three fixed paragraphs once more and reads the section cold.

## Traces

- T1 H1-P4 (variant c): "so much is taken care of by the extended family" made the family handle most of it; the published says these things "often pass through" it, alongside the formal systems. Fixed two ways, both screened in 330g: g, "things often go through the extended family and the local memory" (the published words), and m, "a lot often goes through" (closer to Emulate's "so much"). The rest EQUIVALENT ("Who needs a workshop called...?" for "Nobody needs to announce a workshop called...", "when some aunt has already given three people a task").
- T1 H2-P1: LOST "either" (the published adds this to what he already said he doesn't want). Fixed: "No, not that either!"
- T2 H2-P7: OK.
- T2 H3-P2 (variant l): "because they're expected to carry everybody" dropped the published "may" ("the person earning cash may still be expected to carry everybody"), so a reader took the expectation as certain. Fixed: "because they may be expected to carry everybody." Everything else EQUIVALENT, with each "it" checked: the Black Tax, the obligation, the obligation as described.
