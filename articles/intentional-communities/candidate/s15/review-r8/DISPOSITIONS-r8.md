# Round r8 on section 15 v8: what each finding got

Round r8 (2026-10-17, `../make_gate.py v8 review-r8 H1-P4 H2-P1 H3-P2`): two meaning traces (Sonnet) of the three paragraphs round r7's fixes changed, and one cold read of the section in the article (Sonnet). The stance check and the repeats check were not run again: the fixes since round r4's put published words back. The fix is in `../make_v9.py` (v9).

## Traces

- T1 H1-P4 (variant g, "things often go through"): OK. H2-P1 ("No, not that either!"): OK. Both shapes of H1-P4 read AI alone in 330g, so H1-P4 is rebuilt again from Emulate round e (`../make_v10.py`); the new shape gets its own trace.
- T2 H3-P2: LOST "any" and "long-term" ("They struggle to build any independence or long-term stability" had become "it's really hard to become independent or start a stable life"). Round r7's trace had read the same words as EQUIVALENT; a LOST stands, and only Joel overrules one, so the published words went back in v9: "it's really hard to build any independence or long-term stability, because they may be expected to carry everybody." Everything else EQUIVALENT, nothing ADDED.

## Cold read

All 22 paragraphs OK. Phrases paused at, for the cross-round count: "the local memory", "No, not that either!", "apology" (published), "So which is it?", "this relationship with ours" (published), "Everybody here has sheep", "the whole organism" (published), "Double click to interact with video" (the page's embed line), "It's also the thorny boundary issue", "Another aspect of outside work", "the same outside-work problem", "Westerners often start out isolated".
