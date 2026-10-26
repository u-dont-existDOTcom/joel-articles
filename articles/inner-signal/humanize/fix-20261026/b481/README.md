# Batch 481: the windows that read Human at less than High confidence

Joel's message of 2026-10-26 12:43 UTC (`../joel-20261026-1243-message.txt`), on batch 480's recheck
([part A](https://www.pangram.com/feed/0f1902cd-df2a-4837-9879-69979188e5f1) Human Written, 100% Human;
[part B](https://www.pangram.com/feed/1a9e674f-113e-46ad-8a07-0fb6b71ad65e) Mostly Human Written, one AI window, the audit
he kept as a list): "i also want you to fix any segments that are not high confidence human if you can, and always we
should be marking down the confidence if we have it, because less than high confidence means it's likely next pangram
version will mark it ai (that happened in pangram 4.1 update)" (gate E278).

## The windows

`../b480/recheck/read/CONFIDENCE.md` (`tools/humanization/window_confidence.py`): part A 71 High, 68 Medium, 14 Low; part
B 25 High, 20 Medium, 1 Low, 1 AI (High, the audit). Most Medium windows are 1 to 9 words (list letters, one-word answers,
short script lines): Pangram rarely gives a line that short its top label, so they are question 22 on his questions page.
The rest, every Low window and every Medium one of 10 words or more (43 windows in 22 groups of paragraphs), went to
Emulate first (E235, E237): `make_bundle.py`, `BUNDLE.json` (2,489 words), `BUNDLE-RECORD.json`; the audit separately
(`BUNDLE-audit.json`: his list, and a prose version that joins the questions). Three samples each on the laptop (`emu-hg-cm`,
`-cn`, `-co`; outputs in `cm/`, `cn/`, `co/`), beside the text in `SIDE-BY-SIDE.md`.

## The splices

`make_b481.py` writes `CANDIDATES.json` and `CANDIDATE-MASTER.md` (batch 480's candidate master with these in). Only the
flagged sentences come from a sample, and only where a sample keeps their meaning and form; every change to a sample's
words is listed with its reason. 24 spots, S11 to S36 (no S13, no S35). Four replace his own words (S12, his hidden-menu
sentence; S29, his three published requests; S31, his inner child guide's two sentences; S32, his ethical double bind
sentence): their cards show his words first, and Reject keeps them (E214).

Left, with why (`CANDIDATES.json` "left"): the windows where no sample kept the meaning or changed anything: his inner
child guide's questions in Instead of blame ("it" made "they", "stand to" dropped) and "I'm not going to force my way past
you."; "Temporary Separation." (a two-word label); the human-doing paragraph's "bargain for belonging" (every sample drops
it); the sober induction's "You don't need to tell the whole story yet." (every sample drops it); "My body may stay safe"
(every sample makes it a promise, "will be safe"); his "That's enough for today" line and appendix C's "I don't have to
obey it." (kept word for word); his reframing questions and his three forgiveness sentences to the inner child (changed);
the three BEFORE requests (S26 below) and "We just remember that it can all be true at once." (the linter, below). And the
audit: Emulate's three versions change what three of its seven questions ask, so it is question 23 on his page.

## Checks before the reviewers

- **The strict Emulate check** (`emulate-check/AUDIT.md`, `tools/humanization/emulate_artifacts.py` against his published
  post, his editor HTML and his drafts; allowed: the sentences he approved, his inner child guide and batch 480's master):
  no space before punctuation, no confusable, no spelling his texts don't have. Its 29 "new sentence" findings are the
  splices themselves (the gate's preservation reviewer reads each against his line); its one quote-marks finding, “dark
  patterns”, is as the working copy has it.
- **The gate's linter on each draft** (`owner_delivery_gate.py init`): five FAILs, each fixed the smallest way, and one
  spot dropped:
  - S11 "You can also read ..." (E41: "you can" is a coach phrase, over the limit in a short draft; the old sentence had
    it too, but there it was approved text) became "Also read ...".
  - S26: Emulate's "Please ..." in front of the three BEFORE requests made three new exclamations in a row (S1, S2, the
    exclamation rate), so only the Low request after them changed ("What is one next thing I can do?").
  - S29: three asks joined with "or" in one sentence (E125, a list of three) became two sentences.
  - S35, "We remember that it can all be true at once." (E41, "remember that"): dropped, the window left.
  - S25 and S28: Emulate's action "it" near a paragraph's start (R1) became the old sentences' "this".
  - And one meaning fix before the reviewers: S18's "wasn't that susceptible" became "didn't feel that susceptible", his
    published "didn't feel especially suggestible" being how he felt.

## The gate

`gate/` (`make_gate_files.py`, `fill_ledgers.py`, `run_gate.py`, `GATE.md`): 24 drafts, three fresh Sonnet reviewers each
(preservation, cold reader 1, cold reader 2), three drafts a reviewer, one at a time (E270), in groups a to h
(`gate/BRIEF-<role>-<group>.md`). Five drafts failed the first round, each on a point of his that Emulate or my fix had
shifted, and each was fixed the smallest way and reviewed again by fresh reviewers (groups i to l), with the two drafts
whose sections changed with them:
- S14: the FTC sentence's "their" dark patterns, "used to" and "trick and manipulate" (his: designs that "trick or
  manipulate consumers"): his words back.
- S31: "this part knows it" lost his "remembers", and "Try" lost his "works well here": Emulate's start, his ending, his
  next sentence kept.
- S32: Emulate dropped his "genuinely": back.
- S34: my fix of Emulate's "Lets" used a straight apostrophe in a section of curly ones: "Let’s".
- S36: "What boundaries do I need to set as a result?" dropped his published "still" and added a cause: that question
  stays as it was, and S36 is only "What’s theirs and what’s mine?".
`GATE.md` has every verdict and what changed during the gate, including a reviewer that wrote its files again after their
folder had moved.

## The page and the recheck

- **The marking page** (question 21): `../review/build_review_481.py`, `REVIEW-481.json`, `REVIEW-481.html`, the ten cards
  of batches 479 and 480 with how each read in batch 480's recheck, and batch 481's delivered drafts.
- **The recheck with batch 481 in** (`recheck/`): `make_recheck.py` (the payloads for both parts from `CANDIDATE-MASTER.md`),
  `CHANCES.json` and `make_changed.py` (my chance for each spot that it reads red and that it reads High), the part
  forecasts against batch 480's recheck, the ledger's predictions, the paste and the rendered checks, and each draft's
  secret preview link (`tools/humanization/substack_secret_link.js`).
