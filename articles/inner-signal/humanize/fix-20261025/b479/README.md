# Batch 479: the red windows of the whole guide's recheck of 2026-10-25

Joel's message of 2026-10-25 23:50 UTC (`../joel-20261025-2350-message.txt`) gave the result pages of both parts of the
recheck: [part A](https://www.pangram.com/feed/4c912830-87c4-4ee1-bff1-5acc606dc4f7), Mostly Human Written, 0.9% AI, 7 of
161 windows AI; [part B](https://www.pangram.com/feed/6b07dbba-8dc6-42a0-b562-b46dbe778919), Mostly Human Written, 2.2%
AI, 8 of 61 windows AI (`../recheck/RESULT-A.json`, `RESULT-B.json`; scored in `SCORE-A.md` and `SCORE-B.md`). This batch
makes a candidate for each red stretch, and a recheck with all of them in (`recheck/`). The working copy
(`HUMANIZED-SO-FAR.md`) is unchanged: the candidates go on his page with how each read in place.

## The red stretches and where they came from

| Spot | Part, window | What's red | Where it came from |
| --- | --- | --- | --- |
| S1 | A, Low | "That's one grown-up doing three jobs, and each job keeps the others in balance." | IC-A2 (his 19:42 page): his inner child guide's sentence with its middle cut, "not three more people moving in to help with the rent", which is his own edit there |
| S2 | A, High | the borrowed adulthood paragraph, both sentences | Emulate's first sentence, and EM-2's plainer words for his published second one (gated, approved by him) |
| S3 | A, five Low, marked humanized | the safe-place paragraph's pointer to "Already open? Contain before you deepen", "Deciding to do it." and the stop lines after it | RR-4.6, TY-6 and RR-4.1 (his quote marks back, and "say"); the last two lines were the same in recheck A4, where it all read Human |
| S4 | B, Low and High | "It should make sense, too. Even then, anything big or hard to undo can wait ..." | IC-B12: his own words in his inner child guide (its owner edit sws-p3-p5-joel) |
| S5 | B, High (Low and Medium around it) | "No warmth today? Then rest your hands there ..." and the quote before it | IC-B14: his inner child guide's fallback; the same line is in part A (IC-A10), where it read Human |
| S6 | B, High | "The useful question is whether this way of responding helps you become clearer, steadier, and less hooked." | EM-16: his published test, put back word for word |
| - | B, High | the hypnosis audit's questions | his answer 2c keeps them a list; red in recheck B2 too |

## What was made

- **Emulate first** (E237, E235): three samples of each red paragraph, with the one before it where the red one is short
  (`BUNDLE.json`, `make_bundle.py`; on the laptop `emu-b479-84d0138afe71` and `emu-hg-cg`, `-ch`, `-ci`; outputs in `cg/`,
  `ch/`, `ci/`; 2,091 words, 50,514 left).
- **S1 is his own whole sentence**, from his inner child guide, word for word; no Emulate.
- **Splices** (`make_b479.py`, `CANDIDATES.json`): only the red sentences come from a sample; every change to a sample's
  words is listed there with its reason. S2 from ch, S3a from ci, S3b from cg, S4 from ci, S5 from ch, S6 from cg.
- **Meaning reads** by fresh readers, two or three items each (E270): round 1 (`REVIEW-A1.md`, `REVIEW-A2.md`,
  `REVIEW-B.md`; prompts beside them) and round 2 on the three that changed after it (`REVIEW-A3.md`). What they found and
  what was done:
  - S2: "I don't know if the whole sequence has been tried before" was about his knowledge, not his claim: now "I'm not
    claiming the whole sequence has been proven as one treatment", from his published line. Both readers also named two of
    his four practices as lost; they stay out, as in EM-2, which he approved, because the section carries both as its
    steps (witnessing is the next paragraph; the gradual handing over is the apprentice hat and its return, "even if it's
    only 5%").
  - S3a: sample cg narrowed his "unstable state" to "can't be safe" and lost "is for orientation"; ci keeps "to help orient
    yourself", with the heading's own words, his "later", and "if you are not stable" (round 2 found ci's "not in a safe
    state" weaker than "unstable").
  - S3b: only the two sentences RR-4.1 changed are replaced; cg's versions of the two after them read as a promise of a
    full return and lost "stop", so those stay as they were in recheck A4.
  - S4, S5, S6: kept (REVIEW-B.md). On S6 the reader noted that the paragraph's first sentence, his own revision in EM-16,
    has no "a comforting response doesn't prove an interpretation"; that is his sentence, unchanged here.
- **API checks** of the four High spots alone (Joel's key on the laptop, `/home/joel/ai-work/claude-dangerous-lane/pangram-api/hg-b479/`;
  `api/round1.log` and `api/round2.log`, SHA-256 checked both ways), each predicted in the ledger first:

| Key | Predicted | Chance | What | Pangram |
| --- | --- | --- | --- | --- |
| b479-S4-p | Human | 65% | the Core prompts answer paragraph, 68 words | **Human** (High, one window). [check](https://www.pangram.com/history/84252ea4-c838-465a-8ae9-4700fd94be2c) |
| b479-S5-p | Human | 70% | the Inner child love paragraph, 94 words | **Human** (five windows, two High, three Medium). [check](https://www.pangram.com/history/65540c43-b4db-4f23-b013-5dd0b0da2185) |
| b479-S6-p+prev | Human | 60% | the response check's last paragraph with the one before it, 91 words | **Human** (High, one window). [check](https://www.pangram.com/history/1ce0b7d9-6ff7-48e7-87f2-798fbe88a7b9) |
| b479-S2-p | Human | 55% | the borrowed adulthood paragraph, 55 words | **Human** (High, one window). [check](https://www.pangram.com/history/0ff4a58c-01af-4a70-a743-a64c81dbe275) |

  4 of 4 right. S1 and S3 were Low windows, which the API doesn't reproduce alone (E226), so the recheck in place decides
  them.
- **The recheck** (`recheck/`): `make_recheck.py` builds both parts from `CANDIDATE-MASTER.md` (the working copy with every
  candidate in), as the last recheck was built; part B again starts at Closing. Predicted first (HG-whole#66, AI at 0.20;
  HG-rest-B#67, AI at 0.02 for the audit) with part forecasts (`CHANCES.json`, `make_changed.py`, `FORECAST-A.json`,
  `FORECAST-B.json`). Pasted into the same two temporary drafts, each body cleared first, and checked rendered:
  `RECHECK-POST-A.json`, `RECHECK-POST-B.json`.

## Next

When Joel sends the two result pages: read them as in `../recheck/` (WINDOWS, META, RESULT, the ledger result, the part
forecast's score). Every candidate that reads Human in place goes on his page beside the words it replaces, after the
owner-delivery gate for Emulate's words (S2 to S6); S1 is his own sentence. A spot that reads red again goes to him with
the check's link and part number.
