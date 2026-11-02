# Status: neuro de-armoring humanization (newest on top)

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
