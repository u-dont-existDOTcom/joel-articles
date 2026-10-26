# Batch 480: what batch 479's recheck read red, and the marking page

Joel's message of 2026-10-26 00:54 UTC (`../joel-20261026-0054-message.txt`) gave the result pages of batch 479's recheck:
[part A](https://www.pangram.com/feed/9b9bedd2-a7d1-4141-9d85-168fbe3e81e4), Mostly Human Written, 0.9% AI, 7 of 153
windows AI; [part B](https://www.pangram.com/feed/84384f22-e09d-4a3b-bd39-a6617cd21cd1), Mostly Human Written, 1.5% AI, 2 of
53 windows AI (`../../fix-20261025/b479/recheck/`: WINDOWS-A/B.txt checked against the pages' SHA-256, META, RESULT,
SCORE). HG-whole#66 and HG-rest-B#67 were right (Mixed). The part forecasts: A 21 of 23 parts right (Brier 0.102), with two
red windows outside every part; B 13 of 16 (Brier 0.170), its misses the audit's lead-in and last line (0.05 each, red with
the questions) and "Borrowed is fine" (a Low window at 0.02).

## How batch 479's candidates read in place

| Spot | Read in place | |
| --- | --- | --- |
| S1, his inner child guide's whole three-jobs sentence (IC-A2) | **AI, High, 27 words**, alone in its window | Emulate's version is S7 below |
| S2, the borrowed adulthood paragraph | Human (light) | on the page |
| S3a, the pointer to "Already open?" | Human (light) | on the page, without "you can" (S3a2) |
| S3b, the stop words | Human (light) | on the page |
| S4, his two inner child guide sentences | Human | on the page |
| S5, the no-warmth fallback | Human (light) | on the page, ending on his "no faking required" (S5b) |
| S6, his published test | Human | on the page |

Red where nothing had changed, after the edits above it (E276):

| Spot | Part, windows | What's red | Where it came from |
| --- | --- | --- | --- |
| S8 | A, Medium 21 and High 48 | IC-A14's two sentences ("But before you decide where it's coming from ...") and the start of the guard prompt | the alignment card he approved on 2026-10-25; Human (Low, 96 words) the check before |
| (S8) | A, Medium 10 and Low 17 | the guard prompt's next lines ("I'm not going to force my way past you." ...) | his inner child guide (IC-A15), unchanged |
| S9 | A, Low 35 and Medium 18, both marked humanized | the parent script paragraph's two middle sentences | unchanged since recheck A4, Human the check before |
| S10 | B, Low 21 | "Borrowed is fine, as long as it's from someone steady who won't try to run your trip for you." | IC-B19, his inner child guide's sentence; Human (Low) the check before |
| - | B, High 120 | the hypnosis audit, from its lead-in to its last line | his answer 2c keeps it a list |

## What was made

- **Emulate first** (E235, E237): three samples of each red paragraph (`BUNDLE.json`, `make_bundle.py`; on the laptop
  `emu-hg-cj`, `-ck`, `-cl`; outputs in `cj/`, `ck/`, `cl/`).
- **Splices** (`make_b480.py`, `CANDIDATES.json`, `CANDIDATE-MASTER.md`): only the red sentences come from a sample, each
  change to a sample's words listed with its reason. S7 from cl ("rather than getting three more people to move in with you
  to help with the rent!"), S8 from ck, S9 from cj and ck, S10 from cl. Two of batch 479's candidates got the smallest fix
  the owner-delivery gate needed: S3a2 (S3a without "you can", the linter's coach register) and S5b (S5 ending on his own
  "no faking required" from his inner child guide: "You don't have to fake it!" failed the linter, and "Don't fake it."
  failed the gate's preservation review as a rule where his line is a release).
- **Meaning reads** by fresh readers, two items each (`REVIEW-1.md`, `REVIEW-2.md`, prompts beside them): S7 CHANGED, its
  "Each job helps to keep the others in balance" softer than his "each job keeps the others in balance", so his verb is
  back; S8, S9 and S10 kept.
- **Linter fixes before the gate's review** (`make_b480.py`): S8 ends on IC-A14's own "or a bit of each" for Emulate's "or
  a combination" (E125: a list of three in model words fails unless it ends on a casual catch-all); S9's last sentence
  starts "This" again, the paragraph's word, for Emulate's "It" (R2).
- **API checks** (Joel's key on the laptop, `/home/joel/ai-work/claude-dangerous-lane/pangram-api/hg-b479/`, round3-480.log;
  `api/TEXTS-1.json`, `api/round1.log`, SHA-256 checked both ways), each predicted in the ledger first, before the two
  linter fixes (the in-place recheck reads those):

| Key | Predicted | Chance | What | Pangram |
| --- | --- | --- | --- | --- |
| b480-S7-p | Human | 60% | the three-jobs paragraph, 80 words | **Human** (High, one window, 84 words). [check](https://www.pangram.com/history/52b86d77-b680-4366-a544-3854ae540784) |
| b480-S8-p+next | Human | 55% | the guards paragraph with the guard prompt after it, 185 words | **Human** (five windows, three High, two Medium). [check](https://www.pangram.com/history/8cc85c99-3638-4495-ac87-ca83d725c67c) |
| b480-S9-p | Human | 60% | the parent script paragraph, 127 words | **Mixed** (AI Detected, 41%): Emulate's three sentences with the first read Human (High, 73 words); the last two, unchanged, read AI (Low 30, Medium 27). [check](https://www.pangram.com/history/0998d046-5087-4d3c-8ca0-388a19abca28) |

  2 of 3 right. The miss is explained in the ledger ("context: Human in the whole guide, red alone"): the last two
  sentences read Human in place last time, so the recheck decides them. S10 is one sentence, too short to check alone.
- **The owner-delivery gate** (`../gate/`, `GATE.md`, `GATE-OUTCOMES.json`): all ten drafts on the page (G-S2 to G-S10)
  through the linter, the writer's tell ledger and three fresh reviewers each (preservation, cold reader 1, cold reader
  2), two or three drafts a reviewer, one at a time (E270); 10 of 10 delivered.
- **The marking page** (`../review/build_review_480.py`, `REVIEW-480.json`, `REVIEW-480.html`; `BROWSER-TEST.json` 74 of
  74): his working copy with ten cards, each new sentence the gate's delivered text byte for byte and each changed paragraph
  as the recheck has it. Published at https://claude.ai/artifact/TpZbfBZcwuj8PL7KFLhmjP with `{"db": {}, "downloads":
  true}`; its store answered once after the publish (empty).
- **The recheck** (`recheck/`): `make_recheck.py` builds both parts from `CANDIDATE-MASTER.md`; part B again starts at
  Closing. Predicted first (HG-whole#71, AI at 0.08; HG-rest-B#72, AI at 0.02 for the audit) with part forecasts
  (`CHANCES.json`, `make_changed.py`, `FORECAST-A.json`, `FORECAST-B.json`; the audit is one part now, lead-in to last
  line, and the guard prompt and the parent script's last two sentences have chances of their own). Pasted into the same two
  temporary drafts, each body cleared first, and checked rendered: `RECHECK-POST-A.json`, `RECHECK-POST-B.json` (part A's
  first 99,999 characters hash to TEXT-A.txt, part B without its card line to TEXT-B.txt).

## Next

When Joel sends the two result pages: read them as in `../../fix-20261025/b479/recheck/` (compact mode, WINDOWS checked
against the page's SHA-256, META with part B's card line in "embeds", RESULT rebuilt from `recheck/PAYLOAD-A.html` and
`PAYLOAD-B.html`), the ledger results for HG-whole#71 and HG-rest-B#72, `part_forecast.py score` on `recheck/FORECAST-A.json`
and `FORECAST-B.json`. When his answers come back from the page: a script puts them into `HUMANIZED-SO-FAR.md` (as
`../../fix-20261025/emulate-check/apply_answers_20.py` did), recording each card's fate. A card he approved that reads red
in place gets Emulate's re-run of that sample (E235), or goes back to him with the check's link and part number (E214).
