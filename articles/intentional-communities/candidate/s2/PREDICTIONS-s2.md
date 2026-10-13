# Section 2 v2.1: predictions, written before the Pangram calls (2026-10-01)

The reviewer's calls are blind (`review-v2/reviewer/prompt.txt`, answers in `review-v2-reviewer-answers.txt`, key in `review-v2/reviewer-key.json`). They were made on v2.0; v2.1 changed a few words in C1, C2, C9 and C12 (fixlog `v2.1`). On this article's own controls it called 1 of 2 known-Human section 1 paragraphs AI (P12, at 70) and both known-AI ones AI; on the Inner Child controls, 1 of 2 right (a known-Human called AI at 70). It isn't calibrated on this article (`HUMANIZATION-GATE.md`, "How to read it"), so its calls are logged, not used.

| text | reviewer (v2.0) | mine | why (mine) | Pangram |
|---|---|---|---|---|
| C1a-C2 | AI 78 | AI | Joel's "rather than a sentimental extra" back in, and C2's list of five in one breath | AI 100 |
| C2 | AI 60 | Human | Emulate's opener and "starvin'" carry it; the list is the risk | Human 100 |
| C3-C4a | AI 80 | AI | C4a's four-item list ("jobs, feeds, relationships, and expectations") is Joel's, restored | AI 100 |
| C4a | AI 74 | AI | same list, plus the "less like X, more like Y" closer | AI 100 |
| C6a-C7a | AI 74 (C6 v2.0, without the restored verdict) | AI | the restored verdict line closes C6; C7a is close to Joel's sentence | AI 100 |
| C8-C9a | AI 66 | AI | C9a's last two sentences are Joel's, word for word | AI 100 |
| C8o-C9a | AI 70 | AI | Joel's wry line plus the same C9a | Human 100 |
| C9a | AI 58 | AI | as above | AI 100 |
| C11a | AI 76 | AI | close to Joel's paragraph, with its list of four | AI 100 |
| C12 | HUMAN 62 | Human | mostly Emulate's shape | Human 100 |

C10 isn't checked: the sweep (T02) and the reviewer (AI 76: "requirement, requirement, generalizing principle") both read it as marching, and I agree, so it's rebuilt first (the gate: the march blocks the call).

## Results (Pangram, 2026-10-01, this turn; `pangram-s2.jsonl`)

Every result was 100% one way or the other ("Confidence limited — short text"), and each AI result flagged the whole text.

Scores: mine 9 of 10, the reviewer's 8 of 10 (it called C2 and C8o-C9a AI; both came back Human).

The fallbacks, checked because the a versions failed: C1b-C2 AI, C3-C4b AI, C4b AI, C6b-C7a AI, C9b AI, C8-C9b **Human**, C11b AI.

What passed: C2, C12, C8o-C9a (Joel's own wry line before C9a) and C8-C9b. Seven of the ten v2.1 texts failed. They're the ones where the trace fixes had put Joel's published sentences back nearly whole: C1 (his opening plus the advisory sentence), C4 (his four-item list), C7 (his objection sentence), C9 (his last two sentences), C11 (his whole paragraph, near enough).

## Writers round 1 (fresh Opus writers, three per unit; `writers-r1/`, texts in `r1/`)

Written before the calls. No reviewer run: the fast order runs it only when nothing passes. Mine, with a word on why:

| text | mine | why | Pangram |
|---|---|---|---|
| U1w1-C2 | Human | plain, a bit stiff ("dealt with ... as") | AI 100 |
| U1w2-C2 | Human | "There's a ... advisory" is spoken | AI 100 |
| U1w3-C2 | AI | two tidy clauses joined by "and" | AI 100 |
| U2w1 | AI | ends on the 1972 line, a landing | AI 100 |
| U2w1-p2 | AI | same | AI 100 |
| U2w2 | Human | the doubt split into two sentences | AI 100 |
| U2w2-p2 | Human | same | AI 100 |
| U2w3 | AI | "you'll see" plus the landing | AI 100 |
| U2w3-p2 | AI | same | AI 100 |
| U3w1 | Human | "It was chaotic." alone, then a turn | AI 100 |
| U3w2 | AI | the three verdicts in one sentence | AI 100 |
| U3w3 | Human | odd order, "It's the oldest one" | Human 100 |
| U4w1 | AI | point, concession, mechanism, consequence | AI 100 |
| U4w2 | Human | the long last sentence | AI 100 |
| U4w3 | AI | same march as w1 | AI 100 |
| U5w1 | AI | the four-item list in one breath | AI 100 |
| U5w2 | AI | same | AI 100 |
| U5w3 | AI | same | not checked (49 words; Pangram needs 50) |
| U6w1 | AI | close to the published order | AI 100 |
| U6w2 | Human | "Or how fast..." as a fragment | AI 100 |
| U6w3 | Human | same fragment | AI 100 |

Scores: mine 9 of 20. Only U3w3 passed. **Correction (2026-10-01, 15:30):** I first described U3w3 as the draft that put the objection first and only then called it the oldest one. That was another writer's draft, matched to the wrong file. U3w3 is "Later, when another influencer with a big following floated the commune idea, the comment section started to become a recruitment board. It was chaotic, but sincere, and it was revealing. ..." with "The oldest objection, that maybe ..., showed up almost right away." The wrong description went into the round 2 and round 3 writer prompts as "the one that passed". The Pangram results are by file, so they stand. The briefs gave the writers Joel's published paragraph and told them to carry everything and add nothing, so most kept his order, reworded. That's the paraphrase Pangram is built to catch.

## Writers round 2 (bare-point briefs, the article so far, one noticing allowed; `writers-r2/`, texts in `r2/`)

Not checked, on meaning: U2w1 invents a claim about Joel's father ("My father never thought of it as a leftover."); U4w2 speculates about the East Wind factory manager ("Maybe the woman running the nut butter factory at East Wind got some of her power that way."), against section 1's own account of her power. Predictions, written before the calls:

| text | mine | why | Pangram |
|---|---|---|---|
| U1w1-C2 | Human | advisory first, then a callback to his father's question | AI 100 |
| U1w2-C2 | Human | "Loneliness was already in my father's question" reacts to the longing | AI 100 |
| U1w3-C2 | AI | ends on a tidy "decades after he made it" | AI 100 |
| U2w2 | Human | the 1972 line moved up; the doubt follows it | AI 100 |
| U2w2-p2 | Human | same | AI 100 |
| U2w3 | Human | same move | AI 100 |
| U2w3-p2 | Human | same | AI 100 |
| U4w1 | AI | "Some people really would." is a short knock-down | AI 100 |
| U4w3 | Human | starts from the concession; "Even in a small one" reacts | AI 100 |
| U5w1 | Human | ends on the reader's objection, open | AI 100 |
| U5w2 | Human | ends on an irony | AI 100 |
| U5w3 | Human | ends on the weekly-meeting callback | AI 100 |
| U6w1 | Human | ends on the father's-question callback | AI 100 |
| U6w2 | AI | the berry line is a landing | AI 100 |
| U6w3 | Human | "lonely and exhausted, though" moved to the end, reacting | AI 100 |

Scores: mine 3 of 15. All 15 failed. The callbacks and the reordering didn't carry a paragraph alone.

## The whole section, most faithful version (`r3/section-faithful.md`), a diagnostic check

v2.1's C1, C2, C3, C4a, C9a, C10a, C11a and C12, with writers round 1's U3w3 for C6 and C7, and Joel's own C8 line ("as Instagram comments sometimes do"), headings as published. It's in for a diagnosis, not as a candidate: C10a still has T02 present, and both rebuild rounds of it (six drafts) failed alone. The question it answers is whether the section carries the paragraphs that fail alone. The published section as a whole was 92% AI (`intentional-communities-baseline-02`, 2026-09-29).

| text | mine | why | Pangram |
|---|---|---|---|
| section-faithful | AI | five of its paragraphs fail alone, and the flag usually spreads | AI 41 (598 words; three flagged spans) |

The flagged spans: (1) the title and C1, the Surgeon General paragraph; (2) C4 from "That's around when AI stopped being a tech-news curiosity" to the 1972 line, i.e. the four-item list and the line after it; (3) from C9's second sentence ("Shared ownership can blur responsibility...") to the end of C11. Not flagged: C2, C3, C4's first sentence, Joel's Instagram paragraph, U3w3's two paragraphs, Joel's C8 line, C9's first sentence and C12. Credits 1055 to 1049.

## v3 (after Joel's answers, 2026-10-01 14:49; texts in `r4/`)

Joel's own C10 and C11 (he says his check came back Human, medium confidence); Emulate-based versions with small logged fixes (`fixlog-v3.json`); writers round 3, whose brief carried Joel's own rewrite as the model of his voice. Predictions, before the calls:

| text | mine | why | Pangram |
|---|---|---|---|
| C10j | Human | Joel's own | |
| C11j | Human | Joel's own | |
| C1e1-C2 | Human | Emulate's shape, facts fixed | |
| C1e2-C2 | Human | Emulate's question opener | |
| C1e2 | Human | same | |
| C4e1q | AI | the 1972 quip ends it | |
| C4e1p | Human | Emulate's shape, plain ending | |
| C3-C4e1q | AI | the quip | |
| C3-C4e1p | Human | | |
| C9e1 | Human | Emulate's flourishes kept | |
| C9e2 | Human | Emulate's shape | |
| C1w1-C2 | AI | advisory, then "That's the same longing" | |
| C1w2-C2 | Human | the father looking for connection | |
| C1w2 | Human | same | |
| C1w3-C2 | Human | "Or about the loneliness under it, at least." corrects itself | |
| C1w3 | Human | same | |
| C4w1 | AI | one long list sentence | |
| C4w2 | Human | Joel's repeated "It started changing" | |
| C4w3 | Human | "It used to sound like something from the seventies." | |
| C3-C4w1 | AI | | |
| C3-C4w2 | Human | | |
| C3-C4w3 | Human | | |
| C9w1 | Human | "IMO", spoken | |
| C9w2 | AI | close to the published order | |
| C9w3 | Human | reordered, the reason last | |

C3, the Google Trends line, is what flags the C3-C4 pairs: every C4 that passed alone failed after it. Two Emulate-based C3s (`fixlog-v3.json`), each paired with both C4s, plus Joel's C8 line before the round 3 C9, and Joel's edited Instagram paragraph alone. Predictions:

| text | mine | why | Pangram |
|---|---|---|---|
| C3e2-C4e1p | Human | Emulate's "Check out ... After years of decline" | |
| C3e2-C4e1q | Human | same, with the quip | |
| C3e3-C4e1p | Human | Emulate's question | |
| C3e3-C4e1q | Human | same, with the quip | |
| C8o-C9w1 | Human | both pass in shorter checks | |
| SEBAj | Human | Joel's own | |

The cold read (`SENSE-v3.md`, [20]) had to reread C7's objection sentence, so it's split, with "that" added (`build_v3_section.py`). Prediction:

| text | mine | why | Pangram |
|---|---|---|---|
| C6-C7fix | Human | the split gives the objection its own sentence; nothing else changed | |

The split turned the passing C6-C7 pair 100% AI ("paraphrased or rewritten"), so it's undone and only "that" goes in. The v3 trace (`TRACE-v3.md`) found two meaning shifts in Emulate's words: C3's present tense ("is climbing") and C4's "uptick", against "sharply". Each gets a one-word fix, checked in the pair and alone. Then the whole section, with the plain C4. Predictions:

| text | mine | why | Pangram |
|---|---|---|---|
| C6-C7b | Human | one word added to the pair that passed | |
| C3e2f-C4e1pf | Human | two one-word fixes | |
| C4e1pf | Human | one-word fix | |
| C3e2f-C4e1qf | AI | the same pair with the quip failed before | |
| C4e1qf | Human | one-word fix | |
| section-v3 | Human | every paragraph passes in its own check | |

## v3.1 (Joel's edits of 2026-10-01 18:06; texts in `r5/`)

- **P4:** Joel's last sentence: "Suddenly, forming a village sounded like a good backup plan, not just a hippie utopian whim." Joel checked P3+P4 together himself: it passes.
- **P9:** "I'd say" for "IMO".
- **P10 and P11:** the fixes he agreed to.

Each changed paragraph alone, P9 after his seminar line, then the section. Predictions:

| text | mine | why | Pangram |
|---|---|---|---|
| P4j | Human | his sentence; the rest passed alone | Human 100 |
| P9d | Human | two words changed in a passing paragraph | Human 100 |
| C8o-P9d | Human | same | Human 100 |
| P10f | Human | two words changed in his passing paragraph | Human 100 |
| P11f | Human | three small changes in his passing paragraph | Human 100 |
| section-v3.1 | Human | every part passes | Human 100 |

All six came back 100% Human. The section was 630 words scanned, with no span flagged.

## 2026-10-02: a proposal from the abstract-agent sweep (text in `r5/`)

Joel's rule of 2026-10-02 (abstract concepts or feelings as agents are an AI tell): the sweep of sections 1 to 3 (`../ABSTRACT-AGENTS-s1-s3.md`) found one clear case in a rewrite, "The oldest objection, that … , showed up almost right away." The proposal gives the action to the commenters without splitting the sentence (a split turned this pair 100% AI on 2026-10-01).

| text | mine | why | Pangram |
|---|---|---|---|
| C6-C7agent | Human | one clause moved, no split | Human (92) |
