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
| 2026-09-28 | Make the Protector Visible, whole-section draft w1 (heading, the 2 a.m. paragraph, the writer's paragraphs) | AI, partial (my call: all three drafts follow the plan's order almost identically, a how-to run of instructions) | not checked: failed the sense read, and w2's twin failed | — |
| 2026-09-28 | Make the Protector Visible, whole-section draft w2 (heading, the 2 a.m. paragraph, the writer's paragraphs) | AI, partial (my call: all three drafts follow the plan's order almost identically, a how-to run of instructions) | 100% AI (557 words) | hit (AI; all of it, not partial) |
| 2026-09-28 | Make the Protector Visible, whole-section draft w3 (heading, the 2 a.m. paragraph, the writer's paragraphs) | AI, partial (my call: all three drafts follow the plan's order almost identically, a how-to run of instructions) | not checked: one UNCLEAR in the sense read, and w2's twin failed | — |
| 2026-09-28 | Make the Protector Visible, combo X (2 a.m. paragraph, then slot drafts A1, B2, C1) | Human, low (my call: three short paragraphs written separately, each with its own detail, no summary at the end) | 100% AI (361 words) | miss |
| 2026-09-28 | Make the Protector Visible, combo Y (2 a.m. paragraph, then A2, B1, C2) | Human, low (my call: same reason) | not checked: six UNCLEAR in the sense read, and X failed | — |
| 2026-09-28 | Make the Protector Visible slot draft A1 alone (diagnostic: combo X failed as a section) | AI (my call: the section failed at 100%, so at least some paragraphs are AI alone; which ones is the question) | 100% AI (98 words, short text) | hit |
| 2026-09-28 | Make the Protector Visible slot draft B2 alone (diagnostic: combo X failed as a section) | AI (my call: the section failed at 100%, so at least some paragraphs are AI alone; which ones is the question) | not run: the browser batch stopped before it, and the reviewer's tickets on combo X came back first | — |
| 2026-09-28 | Make the Protector Visible slot draft C1 alone (diagnostic: combo X failed as a section) | AI (my call: the section failed at 100%, so at least some paragraphs are AI alone; which ones is the question) | not run: same reason | — |
| 2026-09-28 | Make the Protector Visible, tX1: combo X after the reviewer's tickets, writer 1 (walk after work, broken zipper, sugar jar, the sister at family dinner) | AI, low (my call: the box labels and the closer are gone, but the sentences are long and even, and each paragraph still runs example, reason, rule) | 100% AI (438 words) | hit |
| 2026-09-28 | Make the Protector Visible, tX2: combo X after the same tickets, writer 2 (walk before dinner, work shoes, envelope since March, the mother at Sunday lunch) | AI, low (my call: same reason) | 100% AI (439 words) | hit |
| 2026-09-28 | Make the Protector Visible, one-point paragraph out_a alone ("Most days the Protector's job is more ordinary than…") | Human, low (my call: one plain example, then a far-end case, then the trust point with a trailing clause) | 100% AI (74 words, short text) | miss |
| 2026-09-28 | Make the Protector Visible, one-point paragraph out_b alone ("Your little one has heard kind words before and…") | Human, low (my call: ends on the bill moved from the counter to the table and back) | 100% AI (78 words, short text) | miss |
| 2026-09-28 | Make the Protector Visible, one-point paragraph in_a alone ("The Protector keeps watch inside you as well. When…") | Human, low (my call: ends on a new small thought, the feeling saying it has to be now) | 100% AI (58 words, short text) | miss |
| 2026-09-28 | Make the Protector Visible, one-point paragraph in_b alone ("The Protector also has a job inside you. Fear,…") | Human, low (my call: the last sentence reacts, your little one is still lonely) | 100% AI (62 words, short text) | miss |
| 2026-09-28 | Make the Protector Visible, one-point paragraph between_a alone ("Some of the protecting happens only between you and…") | AI, low (my call: colon case, then the balanced "is one way of showing them love, but it doesn't take the place" line) | 100% AI (80 words, short text) | hit |
| 2026-09-28 | Make the Protector Visible, one-point paragraph between_b alone ("Your little one might tell you that you only…") | Human, low (my call: a case, a reaction, an open last sentence) | 100% AI (67 words, short text) | miss |
| 2026-09-28 | Make the Protector Visible, one-point paragraph first_a alone ("If you can't find the Nurturer in you yet,…") | Human, low (my call: "That sounds colder than it is" reacts to the sentence before) | 100% AI (61 words, short text) | miss |
| 2026-09-28 | Make the Protector Visible, one-point paragraph first_b alone ("If you can't find the Nurturer in you yet,…") | Human, low (my call: same shape as first_a, with longer details) | 100% Human (72 words, short text) | hit |
| 2026-09-28 | Make the Protector Visible, one-point paragraph pick_a alone ("Pick one protective act and give it a time,…") | Human, low (my call: a single worked case, the motel and the mother) | 100% AI (76 words, short text) | miss |
| 2026-09-28 | Make the Protector Visible, one-point paragraph pick_b alone ("Choose one way to protect your little one and…") | Human, low (my call: ends on the sentence coming out as a question) | 100% AI (80 words, short text) | miss |
| 2026-09-28 | Make the Protector Visible, one-point paragraph after_a alone ("Afterward, look at what actually happened, because feeling no…") | AI, low (my call: three rules, one per sentence, with a list) | 100% AI (81 words, short text) | hit |
| 2026-09-28 | Make the Protector Visible, one-point paragraph after_b alone ("Afterward, look at what actually happened, and if you…") | AI, low (my call: two lists, then a caveat) | 56% AI (82 words, short text; mixed) | hit (mostly) |
| 2026-09-28 | Make the Protector Visible, round-2 one-point paragraph out3A alone (prompt with Joel's sentences and passing paragraphs) | not written beforehand (my lapse) | 100% AI (70 words) | — |
| 2026-09-28 | Make the Protector Visible, round-2 one-point paragraph in1B alone (prompt with Joel's sentences and passing paragraphs) | not written beforehand (my lapse) | 100% AI (64) | — |
| 2026-09-28 | Make the Protector Visible, round-2 one-point paragraph between2B alone (prompt with Joel's sentences and passing paragraphs) | not written beforehand (my lapse) | 100% AI (81) | — |
| 2026-09-28 | Make the Protector Visible, round-2 one-point paragraph pick3A alone (prompt with Joel's sentences and passing paragraphs) | not written beforehand (my lapse) | 100% Human (72) | — |
| 2026-09-28 | Make the Protector Visible, round-2 one-point paragraph after1A alone (prompt with Joel's sentences and passing paragraphs) | not written beforehand (my lapse) | 100% AI (82) | — |
| 2026-09-28 | Make the Protector Visible, round-2 one-point paragraph out1A alone (prompt with Joel's sentences and passing paragraphs) | not written beforehand (my lapse) | 100% AI (77) | — |
| 2026-09-28 | Make the Protector Visible, round-2 one-point paragraph in1A alone (prompt with Joel's sentences and passing paragraphs) | not written beforehand (my lapse) | 100% AI (60) | — |
| 2026-09-28 | Make the Protector Visible, round-2 one-point paragraph between1B alone (prompt with Joel's sentences and passing paragraphs) | not written beforehand (my lapse) | 100% AI (69) | — |
| 2026-09-28 | Make the Protector Visible, round-2 one-point paragraph after2A alone (prompt with Joel's sentences and passing paragraphs) | not written beforehand (my lapse) | 100% AI (80) | — |
| 2026-09-28 | Make the Protector Visible, round-2 one-point paragraph out2B alone (prompt with Joel's sentences and passing paragraphs) | not written beforehand (my lapse) | 100% AI (82) | — |
| 2026-09-28 | Make the Protector Visible, round-2 one-point paragraph in2B alone (prompt with Joel's sentences and passing paragraphs) | not written beforehand (my lapse) | 100% AI (59) | — |
| 2026-09-28 | Make the Protector Visible, round-2 one-point paragraph between2A alone (prompt with Joel's sentences and passing paragraphs) | not written beforehand (my lapse) | 100% Human (72) | — |
| 2026-09-28 | Make the Protector Visible, round-2 one-point paragraph after3B alone (prompt with Joel's sentences and passing paragraphs) | not written beforehand (my lapse) | 100% AI (86) | — |
| 2026-09-28 | Make the Protector Visible, round-2 one-point paragraph out2A alone (prompt with Joel's sentences and passing paragraphs) | not written beforehand (my lapse) | 100% Human (81) | — |
| 2026-09-28 | Make the Protector Visible, round-2 one-point paragraph in2A alone (prompt with Joel's sentences and passing paragraphs) | not written beforehand (my lapse) | 100% AI (72) | — |
| 2026-09-28 | Make the Protector Visible, round-2 one-point paragraph in3A alone (prompt with Joel's sentences and passing paragraphs) | not written beforehand (my lapse) | 100% Human (75) | — |
| 2026-09-28 | Make the Protector Visible, round-2 one-point paragraph in3B alone (prompt with Joel's sentences and passing paragraphs) | not written beforehand (my lapse) | 100% AI (66) | — |
| 2026-09-28 | Make the Protector Visible, round-2 one-point paragraph after2B alone (prompt with Joel's sentences and passing paragraphs) | not written beforehand (my lapse) | 100% AI (82) | — |
| 2026-09-28 | Make the Protector Visible, round-2 one-point paragraph after3A alone (prompt with Joel's sentences and passing paragraphs) | not written beforehand (my lapse) | 100% AI (84) | — |
| 2026-09-28 | Make the Protector Visible, round-2 one-point paragraph after1B alone (prompt with Joel's sentences and passing paragraphs) | not written beforehand (my lapse) | 100% AI (83) | — |
| 2026-09-28 | My own afterward paragraph afA1 alone | not written beforehand (my lapse) | 100% AI (94 words) | — |
| 2026-09-28 | My own afterward paragraph afA2 alone | not written beforehand (my lapse) | 100% AI (87 words) | — |
| 2026-09-28 | Guide paragraph 1, my versions s1v1, s1v2, s1v3 (after Joel's 19:51 notes) | not written beforehand (my lapse) | 100% AI each (91, 94, 86 words) | — |
| 2026-09-28 | Guide paragraph 1, my versions s1n1, s1n2, s1n3 (after reading all of Joel's fixes) | not written beforehand (my lapse) | 100% AI each (111, 97, 100 words) | — |

Joel rejected the four round-2 passes (19:51: invented scenes, a "Fine," clause, wry humor), so a Pangram pass that leaves the guide isn't a success here.

Hit rate so far: my own calls 4 of 9 (0 of 4 before the loop, 4 of 5 since); the Opus reviewer 2 of 3, and its miss was a false alarm (it said AI, Pangram said Human). From 2026-09-28 the prediction is the new Opus reviewer's (tools/REVIEWER-VALIDATION-20260928.md), made before the call. The two blind model judges (Sonnet, Opus) both called r6, r7's near twin, HUMAN.
