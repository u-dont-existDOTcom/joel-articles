# Make the Protector Visible, first attempts (2026-09-28, 17:16–19:30 UTC)

Nothing from this section is installed. The drafts are in the session scratch folder (`mpv/`), and failed prose stays internal.

## What was tried, and what Pangram said

| attempt | drafts checked | passed alone |
|---|---|---|
| Whole-section drafts (w1–w3) | 1 (w2) | 0 (100% AI, 557 words) |
| Section built from slot drafts (combo X), and its A1 slot alone | 2 | 0 |
| Combo X after the reviewer's 15 tickets, two writers (tX1, tX2) | 2 | 0 (100% AI, 438 and 439 words) |
| One point per paragraph, bare brief (12 drafts) | 12 | 1 (first_b); after_b 56% AI |
| One point per paragraph, with Joel's own sentences, three passing paragraphs and this section's failed openers in the prompt (30 drafts) | 20 | 4 (out2A, in3A, between2A, pick3A) |
| My own versions of the afterward paragraph | 2 | 0 |
| My own versions of guide paragraph 1, in the shape of Joel's Borrow One Competency opening (after Joel's 19:51 notes) | 3 | 0 |

(My 19:30 update said 21 of the 30 were checked; it was 20.)

## Joel's verdict (19:51)

He rejected the passing drafts:
- "doesn't get to decide" is AI-colonized. It came from my brief, and the writers copied it.
- "Fine," as a clause is "super AI".
- The wry humor is an AI tell.
- There are too many invented scenarios, e.g. the cinnamon roll: "is that in the guide?"
- He wants every draft shown in context, next to the guide's original.

These are now in `tools/reviewer/owner_bans.txt`, in every writer and reviewer prompt, in the linter (O1, O2) and in `tools/HUMANIZATION-GATE.md`.

## Lessons

- **P1. I broke his one-paragraph-at-a-time rule** (project preferences). Whole-section and parallel per-point drafting both cost more time than they saved.
- **P2. Passing Pangram isn't enough.** Four of the five passing drafts left the guide: new scenes, wry lines, and points shrunk to one example. A pass that isn't the guide's content is a failure.
- **P3. A brief's wording goes straight into the drafts.** That includes wording I wrote myself.
- **P4. The side-by-side page is the review format** (`make-the-protector-visible-in-context.html`).

## After reading all of Joel's fixes (21:31–21:44)

**What I read:**
- every before/after pair of his on record (`tools/JOEL-FIXES-CATALOGUE-20260928.md`);
- his sleep and detox articles against the Pangram reports of their before versions;
- the Nibbana baseline against its current master.

**The test:** three more versions of guide paragraph 1 in his list moves. All three were 100% AI (111, 97 and 100 words).

**What changed in the tools:** his pairs now go into the draft prompt (`reviewer.py draft`).

**What's next:** a minimal-fix lesson from him on one of those three versions, so the diff shows what carries the signal.

## Paragraph 2 with Joel's move, and the heading (after his 22:12 lesson)

Every check below is on Joel's account, written down with a call before it ran (tools/PREDICTIONS.md). "Joined" means Joel's paragraph 1, a blank line, then the draft.

| draft | its opening | joined | alone |
|---|---|---|---|
| s2c (before the lesson) | "Some of it happens where nobody else can see." | 37% AI: his last line through the "When…, don't…" run | 100% Human |
| s2f | "And repair after you attack yourself. "Repair?"" | 100% AI, his paragraph too | — |
| s2e | "Some of the protecting happens between you and your little one, like repairing after an internal attack. "Internal attack, what's that?"" | 100% AI | — |
| s2g | "Then there's repairing after an internal attack. "What's an 'internal attack'?"" | 24% AI: only the seam, his last two sentences plus that first sentence | — |
| s2i | "Repair after an internal attack too." | 67% AI | — |
| s2h | "If there's been an internal attack, repair it." | 100% Human | 100% Human |
| s2j | "You can protect your little one from yourself too, like by repairing after an internal attack." | 100% Human | 100% Human |

s2g, s2h, s2i and s2j share everything after the first sentence (s2b's plain "They…, and you…" lines).

**Headings.** Joel's paragraph 1 is 100% Human alone and 100% AI with only "Make the Protector Visible" above it (125 words). With the h1, an h2 and both paragraphs:

| h2 | Pangram |
|---|---|
| Make the Protector Visible (the guide's) | 100% AI |
| The Protector Can Go First | 100% AI |
| Let Them See It | 100% AI |
| Do Something They Can See | 85% AI |
| Show Up for Them | 18% AI: his last two sentences |
| (no h2, h1 only) | 18% AI: his last two sentences |
| (no headings) | 100% Human |
| Keep Your Word | 100% Human; also 100% Human over paragraph 1 alone (130 words) and with the Adult Apprentice paragraph above the headings (325 words, with s2j or s2h) |

Installed as a candidate: "Keep Your Word" and s2j. The linter fails s2j (B11, B2, E36/E41, E41 coach), and it fails Joel's paragraph 1 on the same kind of rules (B1, B11, B4/E15, E36/E41), so I went by Pangram.

**Lessons**

- P5. His move carries over. Keep one of the guide's jargon words, let the reader ask what it means, and make the next item the answer. In s2g everything after the question read Human, and the flag stayed only on what came before it.
- P6. At a seam, the new paragraph's first sentence gets scored with the last lines of the paragraph before. After his summing-up close, a topic opener ("Then there's…", "Some of the protecting happens…") was flagged, and so was carrying on his list of commands ("And repair…", "Repair… too."). Two openers passed: the article's own "If…, do it" shape, and a plain "You can… too, like by…".
- P7. A heading is part of what Pangram reads, and it moves the windows. Five of six h2 wordings failed, and the flagged span always took in his last two sentences. So "Keep Your Word" passing is probably luck, not a fix. The fix that would last is at that span, and it's his text.


## Guide paragraph 3, folded into the first half of paragraph 4 (2026-09-29, turn 2)

**The move (my call, reported to Joel).** Guide paragraph 3 is 30 words: "When the Nurturer is unavailable, the Protector can begin the relationship. Care may first appear as a locked door, a meal, a cancelled obligation, or a phone put down at midnight. Warmth can come later." Most of it is already in the article:
- the acts are in P1 and P2;
- "if there isn't any yet, borrow some" and "lock the door and get help" are in Borrow One Competency;
- the phone at midnight belongs to the 2 a.m. paragraph, which is out for now.

The new idea is that you can start with protective acts before you feel any warmth, and that's the reason to pick one act. So it now opens paragraph 4, and paragraph 4 splits in two: before the act (pick one, make it specific, rehearse), then afterward (look at what happened, and so on).

Earlier this turn, three fresh writers drafted paragraph 3 on its own (d1–d3, target `make-the-protector-visible-p3.json`). The two that were checked were 100% AI (71 and 75 words).

| draft | how | cold read | linter | Pangram alone |
|---|---|---|---|---|
| w1–w3 | fresh writers, target `-p3b` (brief in sentences) | w2 only: follows on | FAIL, all three (coach 2.5/100) | not run |
| w4–w6 | fresh writers, target `-p3c` (brief as bare notes) | w5 clean; w4 "two paragraphs joined", "the first care"; w6 "catches up", "one of these" | REVIEW | — |
| w5b | w5, "tends to come later" set back to the guide's "can" | — | REVIEW | 100% AI (124 words), whole paragraph |
| wA | w5b after reviewer A's tickets (two reviewers, both blind, both AI 80) | follows on; "Your first care" misread, the last sentence's turn unclear | REVIEW | — |
| wB | w5b after reviewer B's tickets | fails: the plate, "whichever act", "her", the stacked questions; one invented coworker scene throughout | REVIEW | not run |
| wA2 | wA with two cold-read fixes ("The first care you give them", "but your little one") | — | REVIEW | 100% AI (158 words), whole paragraph |

Reviewers ran without `local/human_items.json` (the blog, somatic and romance examples). It isn't in the container or in the laptop lane, so their prompts had only the calibration examples.

**Lessons**

- P8. The brief's wording went straight into the drafts again. All three writers wrote "you can start with the Protector anyway", word for word from my brief. Bare notes stopped the copying.
- P9. The writers converge on the same choices: rehearsing "in the car" (w1–w3), needing "a ride" (w1–w3), and "cancelling the thing you only said yes to so nobody would be upset" (w3, w4, w6). None of those are in the brief or the guide.
- P10. Eleven drafts of this material, five checked, all 100% AI with the whole paragraph flagged. Every one kept the guide's order (no warmth, the Protector starts, examples, warmth later, pick one, the questions, rehearse). The reviewer's tickets changed the frame and the ending, but they kept the opener and the "Take one act…" list, and Pangram still flagged all of it. By the stop rule this is structural, and I've asked Joel for a minimal fix on wA2.
- P11. Both reviewers called w5b AI 80 without being told the Pangram result, and my own calls went 1 of 2 this turn.

**Tools:** `reviewer.py draft` now takes an optional `length` in the target, for merged paragraphs.

## Joel's fixes and the grounding reviewer (2026-09-29, turn 3, from 19:17 UTC)

**Joel's edits, installed:**
- the h2 "Not Every Hero Wears A Cape";
- P1 without "So", plus his self-love sentence;
- P3, his version.

His P3 undoes my merge. It carries guide paragraph 3 only, so guide paragraph 4 is next, whole. All three edits are in `OWNER-EDITS.json` (mpv-h2-hero, mpv-p1-self-love, mpv-p3-joel), applied.

**P2, after his two logic corrections and three more of mine:**

| version | change | Pangram alone | section (h1, h2, P1, P2, P3) |
|---|---|---|---|
| Joel's fixes | "and if they're right, you say so"; "It's evidence you're safe to be around and that you accept them, which love needs, but they can still tell…" | 100% Human (130) | 100% Human (387) |
| + "can show" | the guide's "can be as visible" (the reviewer flagged the flat "shows" in 4 of 4 runs) | 100% Human (131) | 100% Human (388) |
| p2b | a callback ("Oh, so NOW you care?") and "without warmth they can still feel like they're only being put up with" | 100% Human (136) | not run |
| p2c, installed | no callback; "you hear it out instead of snapping back"; "can be as visible to them as the clean room was"; "It's evidence you're safe to be around and that you accept them. Love needs both, but without warmth…" | 100% Human (130) | 100% Human (387) |

**The grounding reviewer** (`tools/reviewer/grounding.txt`, `reviewer.py grounding`). Its validation is in `tools/reviewer/grounding-validation/RESULTS-20260929.md`:
- Blind, on Joel's catches, it found 4 of 7. It missed the dropped "if", the meal and the cancelled obligation.
- On planted errors in unseen text, with his rulings as an input, it found 5 of 5.

**Lessons**

- P12. A heading chosen by Pangram result is a heading chosen by luck. "Keep Your Word" passed and meant nothing for this section. The gate now says never to pick a heading that way, and to run candidate headings through the grounding review first.
- P13. My sentences failed on logic that a line-by-line sense read can't see:
  - a condition dropped by sentence shape ("they're right");
  - evidence turned into proof;
  - "can" turned into a flat "shows";
  - a word ("accept") that slid into its opposite ("put up with") within one sentence;
  - a Nurturer act (the meal) listed as the Protector's;
  - an example (cancelling) that repeated one already in the article.

  Each of these needs the guide and the article in view. That's what the grounding reviewer reads.
- P14. Merging guide paragraphs to get past the detector was the wrong move. Joel lined P3 back up with guide paragraph 3 and cut everything else, and it passed. One guide paragraph per paragraph, with examples only where they add something the article doesn't already have.

**Open for Joel:**
- his self-love sentence, which the reviewer flagged in 4 of 4 runs as a single cause the guide doesn't give (and the guide's next step says "don't decide which without looking");
- the moldy bread, which repeats Borrow One Competency's "smelling that old food… and then trashing it" (5 of 5 runs).

## Turn 4 (2026-09-29, from 20:37 UTC): Joel's rulings, P4 in, the afterward half stuck

**Joel's 20:35 rulings, applied:**
- "shows as clearly" is back in P2 ("a bit pedantic… the logic should be grounded in the meaning the reader needs to understand"); `reviewer/grounding.txt` now flags a strength shift only when it would change what the reader believes or does.
- P1's "The only reason" became "The underlying reason": the error was the "only", and his stance is that lack of self-love underlies the other reasons.
- The moldy bread went from P1. He asked me to choose. Borrow One Competency's old food carries the guide's Borrowed Protector "Eat" and comes first, while P1's bread was an extra beyond the guide's six acts.
- Pangram: P1 100% Human (135 words), P2 100% Human (129), the section 100% Human (379).

**Guide paragraph 4, split at its natural break.** It has two beats (before the act, after it), and Joel breaks paragraphs at two beats. Each half does one beat of the same guide paragraph; nothing crosses into another.

| draft | round | cold read / grounding | Pangram alone |
|---|---|---|---|
| P4a x1 → x1b ("Intentional, meaning you pick one of those acts…") | 1 | the envelope and "those acts" come from P1/P2; "say it out loud ahead of time" was ambiguous, so it became "to yourself" / grounding all OK | 100% Human (81); section 100% Human (460). Installed as P4 |
| P4a x2 → x2b (the sigh, "until there's no 'sorry' in front of it") | 1 | "a part you're dreading" read as a part of you; "the sigh" had no source; both fixed / grounding all OK | 100% AI (94) |
| P4a x3 | 1 | — | linter FAIL (coach 4.3/100) |
| P4b y1 → y1b, y2 → y2f, y3 → y3f | 1 | "the tick" unclear; y2 and y3 judged the act by how it felt, right after saying feeling better isn't the test; fixed to what actually changed / grounding otherwise OK | 100% AI, all three (111, 103, 110) |
| P4b z1 (brief named the failed skeleton; the "doesn't prove it helped" point as a callback to the Checking section's question) | 2 | "again" points to the Checking section / grounding all OK | 44% AI (96): flagged only its last two sentences, the reasons |
| P4b z1b (my rewrite of that span as Joel's own causal chain) | 2 | grounding all OK (chain backed by his ruling) | 100% AI (112) |
| P4b z2 | 2 | grounding: MISSING "doesn't prove it helped" | not run |
| P4b z3 | 2 | — | linter FAIL (coach 2.1/100) |

**Lessons**

- P15. Ground logic flags in what the reader needs. A plain "shows" where the guide says "can be" isn't worth a flag; "love will grow" is.
- P16. Picking up the paragraph before's last word worked again. x1b opens "Intentional, meaning…" on Joel's "intentional", the way his "What's a 'boundary'?" did, and it passed on the first round.
- P17. Vivid isn't human. x2b (the sigh, no "sorry" in front of it) was 100% AI; the plainer x1b passed.
- P18. The afterward half has now failed in every form tried here and earlier (B02, B16, y1–y3). The first partial pass (z1, 44%) came from naming the failed skeleton in the brief: the parallel "If you didn't… / If you did…" frame, the reasons packed into one "or… or…" sentence, the list ending. Its flagged span is the reasons.
- P19. My rewrite of a flagged span took the whole paragraph from 44% to 100% AI, even carrying Joel's own reasoning, like "Will they, though?" on 2026-09-28. Span fixes are his.

**Open:** a minimal fix from Joel on z1's last two sentences.

## Turn 5 (2026-09-30, Joel's 03:29 message)

**Joel's changes, installed:**
- P4 ends on his sentence ("Then put yourself in their shoes…"). It's 100% Human alone (100 words).
- P5 is his final (Human/medium on his check). I capitalized "Protector", as it is everywhere else in the article.
- His Substack note goes in Also Look Outward as a bare URL, after the paragraph about what you can still count on someone for.

**The relationship line.** Joel rethought "leave it" and gave new wording, and wondered whether it "might deserve its own section".

| version | where | Pangram alone | grounding |
|---|---|---|---|
| A0: his wording in place of "leave it" and the self-love reason | P1 | 100% AI (132 words), whole paragraph | MISFIRES: a reader whose partner is violent gets only an inward inquiry. UNCLEAR: "keeps making you less safe" vs "feel unsafe" |
| A1: A0 + "If you're in danger, get safe first, which is not a small thing at all, I know." | P1 | 100% AI (150), whole paragraph | — |
| P1 without the relationship lines | P1 | 100% Human (92) | no MISSING: the item is carried in Also Look Outward. "sweet things and then did nothing" flagged again (for Joel) |
| v1: his sentence as its own paragraph, "And" dropped, + "But if you're in danger, get safe first…" | Also Look Outward | 100% Human (58) | CHANGED ×2: the "less safe" condition, and "in danger" doesn't carry the guide's "you do not need repeated exposure to danger" |
| **v2, installed:** "keeps making you feel less safe…", "But if it's been dangerous even once, get safe first, which is not a small thing at all, I know." | Also Look Outward | 100% Human (61) | (v1's flags fixed) |

- Sections: Also Look Outward 100% Human (433 words with v1, 436 with v2). Not Every Hero Wears A Cape 100% Human (539, with both headings).
- **The move is my call.** P1 is a list of acts the little one can see. The meditation is looking inward at a relationship, which is Also Look Outward's job: what the other person actually does, and your side. Its danger line also carries the guide sentence that section was missing.

**Lessons**

- P20. A faithful carry of the guide can misfire. The guide's "leave it" passed every review because it matched the guide. Joel's case showed the reader it fails, and the article's own teaching (a hook can be old material) was enough to see it. MISFIRES is in the grounding reviewer now (`reviewer/grounding-validation/RESULTS-20260930.md`).
- P21. The same sentence tested 100% AI in P1 and 100% Human as its own paragraph where it belongs. When one of Joel's sentences flips a paragraph, check whether it's in the right place before asking him to rewrite it.
- P22. Reviewers resolve a paragraph-opening "it" the way the writer meant, because they read "After the day" as pinning it. Joel didn't. Name the thing at a paragraph's start (lint R1).
- P23. End a practice paragraph on the next move of the practice (Joel's "put yourself in their shoes… go back & forth"), not on a prediction about the reader.

## Turn 6 (2026-09-30, Joel's 04:44 message)

| text | grounding (default push) | Pangram alone | section |
|---|---|---|---|
| P1: "Maybe your little one had grown-ups who said sweet things and then did nothing, and maybe you've done it too, so this is how they start to believe you." | every line OK; no open questions | 100% Human (98) | Not Every Hero 100% Human (557) |
| P4: "…or good enough, as long as what you needed to say is still in there." | every line OK; 2 parked | 100% Human (112) | same |
| Relationship paragraph v3: "But if they've actually hurt or threatened you, even once, old stuff or not, get safe first…" | the MUST all three push levels raised is now answered | 100% Human (68) | Also Look Outward 100% Human (443) |

**Lessons**

- P24. Reader questions catch what a claim-by-claim check can't. v2's danger line matched the guide ("even once"), but the reader had just been told the feeling may come from inside them, so they couldn't tell which case they were in. All three push levels found it.
- P25. The knob decides what gets raised and how big a fix can be. The MUST was the same at every level, and COULD came up only at wide. The runs disagreed on "get safe = help", so that goes to Joel, not into the text.

