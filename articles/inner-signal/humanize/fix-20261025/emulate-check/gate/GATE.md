# The owner-delivery gate for the two Emulate check pages

Made by `run_gate.py` (this folder); the numbers come from the review files. Main's owner-delivery gate (`docs/HUMANIZATION-OWNER-DELIVERY-GATE.md`, 2026-10-25 17:44 UTC): model-written words in Joel's byline, shown to him as a proposed revision, pass `tools/humanization/owner_delivery_gate.py deliver` first: the linter, the writer's tell ledger, and three reviewers, each a fresh agent with only its brief and the files (preservation, cold reader 1, cold reader 2). His own words are exempt. The pages: the hypnosis guide's (`../REVIEW-EMULATE.json`) and the community article's (`articles/intentional-communities/candidate/joel-20261025/emulate-check/REVIEW-EMULATE.json`).

## Gated: 10 drafts, 10 delivered

| NAME | card | the new words | preservation | cold reader 1 | cold reader 2 | delivered |
| --- | --- | --- | --- | --- | --- | --- |
| G-EM2 | EM-2 | It’s built from familiar practices like modeling and supported action, but I’m not suggesting that the whole sequence has been formally tested and proven as one treatment. | PASS | PASS | PASS | yes (`G-EM2/FOR-JOEL.txt`) |
| G-EM5 | EM-5 | You were too busy avoiding pain, reading what was dangerous and what you had to do to stay in a good bond, etc. | PASS | PASS | PASS | yes (`G-EM5/FOR-JOEL.txt`) |
| G-EM9 | EM-9 | to help me know what I need to know, only in a form and at a time that will be useful | PASS | PASS | PASS | yes (`G-EM9/FOR-JOEL.txt`) |
| G-EM14 | EM-14 | Nominalizations are words that turn a process into a noun, like 'healing', 'safety', 'trust', 'integration', 'communion', 'clarity', 'rest', etc. | PASS | PASS | PASS | yes (`G-EM14/FOR-JOEL.txt`) |
| G-EM15 | EM-15 | I do not tell people to override their fear before asking what it’s protecting. | PASS | PASS | PASS | yes (`G-EM15/FOR-JOEL.txt`) |
| G-EMS2 | EM-S2 | Also, Adam Eason and Benjamin Parris's article about self hypnosis for the International Society of Hypnosis should be a useful thing to read | PASS | PASS | PASS | yes (`G-EMS2/FOR-JOEL.txt`) |
| C-E2 | IC-E2 | It’s already a real piece of community, and it can still make a difference when people are going through a divorce, an illness or grief. | PASS | PASS | PASS | yes (`C-E2/FOR-JOEL.txt`) |
| C-E3a | IC-E3 | Who has to step aside because they’re too close to it? | PASS | PASS | PASS | yes (`C-E3a/FOR-JOEL.txt`) |
| C-E4 | IC-E4 | And a community’s autonomy doesn’t let it take away rights a person can’t sign away, or make the law outside disappear. | PASS | PASS | PASS | yes (`C-E4/FOR-JOEL.txt`) |
| C-T1 | IC-T1 | Just because taking part in the ceremonies is optional doesn’t mean people don’t have to work with the other parts. | PASS | PASS | PASS | yes (`C-T1/FOR-JOEL.txt`) |

## Withdrawn after round 1: the card shows his own words

| NAME | card | why |
| --- | --- | --- |
| G-EM11 | EM-11 | both reviewers failed "instead of getting them looked at" as a condition his rule lacks; the card uses his "or to suppress medical symptoms" |
| G-EM13 | EM-13 | his own two sentences fit the place as they are ("A manipulative double bind ... An ethical one offers two genuinely safe routes."); the card uses his second one |
| G-EM16 | EM-16 | both reviewers failed it for dropping "clearer" from his three-part test; the card uses his own sentences |
| G-EMS3a | EM-S3 | the preservation reviewer failed "what really happened" for his "historical verification"; the card uses his words |
| G-EMS3b | EM-S3 | both reviewers failed it for dropping "every use of hypnosis"; the card uses his "rather than validating every use of hypnosis" |
| C-E3b | IC-E3 | the preservation reviewer failed "safely" for losing whose safety ("without endangering others"); the card uses his words |

## Outside the gate: his own words, a word or mark of his, or quote marks off

| card | page | title | what it does |
| --- | --- | --- | --- |
| EM-Q1 | guide | Quote marks Emulate put around words (85 places) | One card, like the spaces on your last page. Revise if one of them should keep its quote marks. |
| EM-1 | guide | Belongs to life before anything else | Puts back your "before it belongs to"; the rest of Emulate's sentence stays. |
| EM-3 | guide | Which families and religions | Your three words back; the quote marks Emulate put around "takes over" go too. |
| EM-4 | guide | Not choosing yet | One word. |
| EM-6 | guide | One refrain, as the heading says | One word. |
| EM-7 | guide | Not when intoxicated | Your word; it changes who should stop. |
| EM-8 | guide | Reverse what you did going in | Your word, "enter". |
| EM-10 | guide | Ask to be shown, not show yourself | Your three requests, word for word. |
| EM-12 | guide | What would help the part trust you | Your question, word for word. |
| EM-S1 | guide | EFT: several trials, not a few | Your "several of them". |
| IC-E1 | community | Your "don't freeze into doctrine" | Your words, word for word. |
| IC-Q1 | community | Quote marks Emulate put around three words | The same kind of quote marks you asked about in the hypnosis guide. |

Cards whose only drafts were withdrawn, so they now carry his own words: EM-11, EM-13, EM-16, EM-S3.

## Rounds

- Round 1 (`GATE-INPUTS-ROUND1.json`, sixteen drafts, `BRIEF-<role>.md`): the preservation reviewer and cold reader 2 wrote all sixteen reviews. Cold reader 1 read all sixteen drafts before writing anything, hit its output limit twice while thinking, and was stopped at 21:58 UTC after 46 minutes with no review written. Six drafts were withdrawn on round 1's fails (above).
- Round 2 (`make_round2_briefs.py`, `BRIEF-r2-*.md`, `GATE-INPUTS.json`): the ten drafts left, in four groups, one fresh cold reader 1 each, one NAME at a time with its file written before the next. C-E3a's context changed after round 1 (its card's other question became his own words), so it got all three roles again; its round-1 files are in `C-E3a/superseded/`.

## The reviewers

- cold_read_1, `emulate-gate-cold_read_1-subagent-r2a`: G-EM2, G-EM5, G-EM9
- cold_read_1, `emulate-gate-cold_read_1-subagent-r2b`: G-EM14, G-EM15, G-EMS2
- cold_read_1, `emulate-gate-cold_read_1-subagent-r2c`: C-E2, C-E3a
- cold_read_1, `emulate-gate-cold_read_1-subagent-r2d`: C-E4, C-T1
- cold_read_2, `emulate-gate-cold_read_2-subagent`: G-EM2, G-EM5, G-EM9, G-EM14, G-EM15, G-EMS2, C-E2, C-E4, C-T1
- cold_read_2, `emulate-gate-cold_read_2-subagent-r2f`: C-E3a
- preservation, `emulate-gate-preservation-subagent`: G-EM2, G-EM5, G-EM9, G-EM14, G-EM15, G-EMS2, C-E2, C-E4, C-T1
- preservation, `emulate-gate-preservation-subagent-r2e`: C-E3a
