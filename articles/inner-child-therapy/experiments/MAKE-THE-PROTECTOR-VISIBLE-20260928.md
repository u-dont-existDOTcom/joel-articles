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

