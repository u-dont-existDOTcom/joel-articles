# Predictions before Pangram calls (E86)

Each Pangram call gets a prediction in its record before the call. This log scores them, so the audit has a hit rate. It started 2026-09-27; earlier drafts had no written prediction.

| date | text | prediction | result | hit |
|---|---|---|---|---|
| 2026-09-27 | Also Look Outward r2, first paragraph alone | Human, low confidence | 100% AI | miss |
| 2026-09-27 | Also Look Outward r2, the section | Human, low confidence | 57% AI | miss |
| 2026-09-27 | Also Look Outward r5, first paragraph alone | Human, low confidence | 100% AI | miss |
| 2026-09-28 | Also Look Outward r7 alone | Human, low confidence | 100% AI | miss |
| 2026-09-28 | Loop draft r3B2, the tangled one (fails the cold sense read) | Human: the Opus reviewer said HUMAN 65 and HUMAN 70 | 100% Human (109 words, short text) | hit |
| 2026-09-28 | Loop draft r4sf1, r3B2 with the sense fixes | AI: the Opus reviewer said AI 60 twice | 100% Human (118 words, short text) | miss (reviewer too strict) |
| 2026-09-28 | Loop draft r5v2 ("promising to be more careful how you bring things up") | Human: the Opus reviewer said HUMAN 60 | 100% Human (105 words, short text) | hit |
| 2026-09-28 | Loop draft r6b, r4sf1 with a two-word sense fix ("don't go only by"; passed the cold sense read) | Human (my call: a two-word change to r4sf1, which passed); the Opus reviewer called its near twin r6a AI 65 | 100% Human (122 words, short text) | hit |
| 2026-09-28 | Also Look Outward section with r6b as P1 (heading, r6b, Joel's P2, the repair lines) | Human (my call; the installed section passed with the old P1) | 100% Human (313 words, full confidence) | hit |
| 2026-09-28 | Outward expectations paragraph, draft d1 alone ("Afterward, though, you can often point to the sentence where it went wrong…") | Human, low (my call: its last sentence reacts to the advice; no summary) | not checked: failed the cold sense read | — |
| 2026-09-28 | Outward expectations paragraph, draft d2 alone ("Maybe what they can do is text you something kind the next day…") | Human, low (my call: ends on a small true-to-life detail) | 100% Human (66 words, short text) | hit |
| 2026-09-28 | Outward expectations paragraph, draft d3 alone ("Notice, too, whether each new attempt is gentler on them…") | AI, low (my call: claim, instruction, then another instruction) | 100% Human (63 words, short text) | miss |
| 2026-09-28 | Also Look Outward section with Joel's final P1 and d2 after it | Human (my call: both pass alone; the section passed with r6b) | 100% Human (375 words, full confidence) | hit |

Hit rate so far: my own calls 4 of 9 (0 of 4 before the loop, 4 of 5 since); the Opus reviewer 2 of 3, and its miss was a false alarm (it said AI, Pangram said Human). From 2026-09-28 the prediction is the new Opus reviewer's (tools/REVIEWER-VALIDATION-20260928.md), made before the call. The two blind model judges (Sonnet, Opus) both called r6, r7's near twin, HUMAN.
