# Status: neuro de-armoring humanization (newest on top)

## 2026-11-03, after Joel's message of 15:22 UTC: question 1 answered; round 1 rewritten and checked; Emulate retired; three examples for him

His message (`fix-20261103/joel-20261103-1522-message.txt`): "no need to recheck i'm sure it's fine, move onto the next
article you said you were already working on it right". His answers to two questions in the app, word for word in
`fix-20261103/joel-20261103-1522-answers.txt`: question 1, "Freely, in your voice (Recommended)"; then, after round 1 read
AI and Emulate showed 0 words left, "yout old me emulate doens't even pass pangram 4.1 very well anymore so that's
pointless and emulate has done so much damage to my guides that took too long to fix as you saw with hypnosis guide.
give me a couple examples i will see how to rewrite it to train you". **The mailbox first** (`state/MAILBOX.json`,
"2026-11-03 15:22"): pull request 277 merged by him at 15:22 UTC; nothing else new.

**Round 1** (`fix-20261103/r1/`): every section rewritten freely in his voice (sections/S01 to S10.md; assemble_r1.py
makes CANDIDATE.md, fidelity_keys.py PASS on the whole, and cuts each section into stretches the API takes, his Human
(High) paragraphs left out of them); tells_lint.py on every section and its flags in my sentences fixed. Checked through
the API on the laptop with public links, predictions first: batch r1103a (`a/`, the first try of Psychology is the
Software: 40.4% and 100% AI) and batch r1103b (`b/`, 26 stretches: 19 at 100% AI, the best 12.7% AI, Psychology is the
Software's first half; RESULTS.md). Every prediction was AI, and right. Three predictions were voided, never sent: the
API counts a heading of eight words or more as a paragraph, so it refused one stretch, and the cut was made again.

**Round 2 stopped before it started** (`fix-20261103/r2/emulate_r2.py`, the 30 segments it would have sent): Emulate's
balance was 0 words, and his answer retires it (gate E333, `docs/EMULATE-FALLBACK.md`, AGENTS.md). Gate E334 says what
round 1 showed.

**His three examples** (`fix-20261103/examples/build_page_x1103.py`, REVIEW-X1103.*; published as Neuro De-Armoring Cards,
3 November, https://claude.ai/artifact/GKEbRH8VvXKzbEnZGCZUgz, capabilities db and downloads; browser test 60 of 60):
the underpinning paragraph (the science), the UMP trial (a dose with its instructions) and agmatine's interactions (a
list of warnings), each a stretch to edit, each linking its baseline result and my round-1 results.

Predictions: 28 (2 in r1103a, 26 in r1103b), all AI, all right; 3 voided. Delegations (model, piece, check, outcome):
none; the rewrite was judgment throughout.

## 2026-11-03, after Joel's message of 14:52 UTC

His message was his answers to the hypnosis guide's question 34 and "make sure this closer reading is also part of the general joel-articles skill"; nothing changed in this lane. Question 1 still waits on him; this lane is next. The word-for-sense read is now in `SKILL.md` with its tool, `tools/humanization/sense_read.py`. Predictions: none. Delegations (model, piece, check, outcome): none.

## 2026-11-03, after Joel's message of 13:46 UTC

His message was the hypnosis guide's "33a" (the guide into his post, done), his Pattern 10 version and "oily" for "old"; nothing changed in this lane. The hypnosis guide is in his post, so this lane is next; question 1 still waits on him. Gates E331 and E332 apply here (the handoff's START HERE). Predictions: none. Delegations (model, piece, check, outcome): none.

## 2026-11-03, after Joel's message of 12:18 UTC

His message was the hypnosis guide's fourth free check and a card; nothing changed in this lane. Question 1 still waits on him; this lane is next once the hypnosis guide is in his post (its question 33).

## 2026-11-03, after Joel's message of 11:19 UTC

His message was the hypnosis guide's 31a, 32a and third free check; nothing changed in this lane. Question 1 still waits on him.

## 2026-11-03, after Joel's answers of 00:39 UTC

His answers were the hypnosis guide's third cards page. Their lessons apply here too: E328 (overcompletion is read for, and cut, before a flagged window is reworded; parallel structure is no reason to keep a second explanation), E329 (a window over a heading is tested as Pangram reads it before a card advises keeping it) and E330 (a made-up word is fine in an informal piece if it sounds right). Nothing in this lane changed; question 1 still waits on him.

## 2026-11-02, after Joel's message of 23:07 UTC

His message was the hypnosis guide's second free check; nothing changed in this lane. Question 1 still waits on him.

## 2026-11-02, after Joel's message of 21:59 UTC: his second Pangram account's lessons

Read in the hypnosis lane (`articles/inner-signal/humanize/fix-20261102/joel-pangram/history2/`): E326 and E327 and linter rules O59 and O60 apply to this lane's checks and drafts. Nothing in this lane changed; question 1 still waits on him.

## 2026-11-02, after Joel's message of 20:38 UTC: checks over six paragraphs go free (E325)

His message was about the hypnosis guide's whole check ("that should be done the free way to not waste my pangram
credits"). This lane's baseline of the whole article (5,821 words, batch n1102) was one of the five halves or whole
articles the lanes sent through the API on 2 November, against his rule (E218). `tools/humanization/pangram_api.py` and
`pangram_ledger.py` now refuse a text of more than six paragraphs or 1,200 words through the API (gate E325); the
handoff's START HERE says how this lane checks a bigger section or the whole article free. Question 1 still waits on him.

## 2026-11-02, after Joel's message of 19:11 UTC: the lightest fix tried on one section; question 1

His message was about the hypnosis guide (28a, 29a); this lane's next step went on. **Part 1, C to E**
(`fix-20261102/s04/rewrite_s04.py`, CANDIDATE.md, SECTION.txt): the template labels off ("The Problem:", "The Fix:", "The
Hardening:"), the self-answered question made a statement, the closer "The engine is flooded." folded in, short sentences
joined; his own sentences kept where mine failed the linter (the side effects, the hot and cold showers). fidelity_keys.py:
PASS. tells_lint with his text as owner: REVIEW. Checked through the API with a public link (batch n1102r, lineage
ND1102-04 try 2 of 2, called AI at 0.25, right): [AI Detected, 90.6% AI](https://www.pangram.com/history/8a5c6453-c6f1-4ab3-b713-51e54e3550f2)
from 100%; only the SSRIs paragraph reads Human (Low, Medium, Low). So the template is not the main tell: question 1 on
`OWNER-QUESTIONS.md` asks how freely the science sections may be rewritten (default a: freely in his voice, every claim,
number and warning kept, nothing invented, one card per section). Gate E323 for this post: its title's "v5.1 (Sept 10,
2026)" changes with the post.

Predictions: n1102r 1 of 1. Delegations (model, piece, check, outcome): none.

## 2026-11-02, after Joel's message of 18:16 UTC: the lane set up; the baseline checked

His message (`articles/inner-signal/humanize/fix-20261102/joel-20261102-1816-message.txt`): "... then we can start on the
next one we had queued". **The mailbox first**: recorded for the turn in `state/MAILBOX.json` ("2026-11-02 18:16"), nothing new.

**The article, registered** (`articles/INDEX.json`; IMPORT-RECEIPT-20261102.md): his post read through Substack's API from
the laptop (`source/POST-20261102.json`) matches the editor copy of 28 September word for word but for the video's
placeholder text, so master.md is that copy's Markdown. Owner locks: none yet; the protected function is the protocol's
fidelity (OWNER-LOCKS.json).

**The fidelity check** (`tools/humanization/fidelity_keys.py`, tests in `tests/test_fidelity_keys.py`; `FIDELITY-KEYS.json`):
every number with its unit, every compound and term, and every warning sentence with its own rarest words, from master.md.
It fails a draft with one dose changed ("150-300 mg" to "150-250 mg"), one compound left out of a list, or "Do not push
through numbness." taken out while other "do not" lines stay.

**The baseline** (`fix-20261102/baseline/make_baseline.py`, batch n1102, through the API on the laptop with public links;
RESULTS.md): ten sections and the whole, predictions first (all AI), all eleven right. The whole:
[AI Detected, 83.3% AI](https://www.pangram.com/history/72952f09-0e99-46d6-b89f-5fa574422584). By section: the introduction
and disclaimers 63.1% AI (his introduction Human (High)), Psychology is the Software 83.5%, Part 1 A and B 76.2%, Part 1 C to
E 100%, Part 2 phosphatidylserine 99.9%, uridine 100%, 5-HTP and ATP 82.1%, Part 3 87.2%, Part 4 58.6% (the D-serine
paragraph Human (High)), Part 5 and the Aftermath 75.9%.

**Next**: the AI windows, section by section (HANDOFF's Next step).

Predictions: n1102 11 of 11. Delegations (model, piece, check, outcome): none; the read and the predictions were the lead
session's.
