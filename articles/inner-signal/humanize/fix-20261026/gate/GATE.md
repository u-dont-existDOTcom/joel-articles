# The owner-delivery gate for batches 479 and 480

Made by `run_gate.py` (this folder); the numbers come from the review files. Main's owner-delivery gate (`docs/HUMANIZATION-OWNER-DELIVERY-GATE.md`): model-written words in Joel's byline, shown to him as a proposed revision, pass `tools/humanization/owner_delivery_gate.py deliver` first: the linter, the writer's tell ledger, and three reviewers, each a fresh agent with only its brief and the files (preservation, cold reader 1, cold reader 2). Here the words are Emulate's (with the splices' small fixes, each named in `the_change`); the card for each delivered draft is on his marking page (`../review/REVIEW-480.json`).

## Gated: 10 drafts, 10 delivered

| NAME | spot | the new words | preservation | cold reader 1 | cold reader 2 | delivered |
| --- | --- | --- | --- | --- | --- | --- |
| G-S2 | b479 S2 | So, I came up with the idea of constructing a bridge – a temporary fix – a borrowed adulthood, if I can put it that way. It’s made up of a number of familiar practices (such as modeling and supported action), even though I’m not claiming the whole sequence has been proven as one treatment. | PASS | PASS | PASS | yes (`G-S2/FOR-JOEL.txt`) |
| G-S3a | b480 S3a2 | If you are already partially or fully opened, use the later 'Already open? Contain before you deepen' section to help orient yourself, but do not attempt to deepen yourself if you are not stable. | PASS | PASS | PASS | yes (`G-S3a/FOR-JOEL.txt`) |
| G-S3b | b479 S3b | Remind yourself that if you say 'stop' at any time, the induction will end. If you say 'less', you will be asked to do less. If you say 'quiet', the talking will stop. | PASS | PASS | PASS | yes (`G-S3b/FOR-JOEL.txt`) |
| G-S4 | b479 S4 | It should make sense to you and if it's something big or hard to undo, wait till you're calm and then check it out with what you know. | PASS | PASS | PASS | yes (`G-S4/FOR-JOEL.txt`) |
| G-S5 | b480 S5b | If you can’t do this in a loving way today, just put your hands there and see what you feel, no faking required. | PASS | PASS | PASS | yes (`G-S5/FOR-JOEL.txt`) |
| G-S6 | b479 S6 | Is this way of responding helping you to be clearer and steadier and less hooked? | PASS | PASS | PASS | yes (`G-S6/FOR-JOEL.txt`) |
| G-S7 | b480 S7 | It’s one person doing three jobs rather than getting three more people to move in with you to help with the rent! Each job keeps the others in balance. | PASS | PASS | PASS | yes (`G-S7/FOR-JOEL.txt`) |
| G-S8 | b480 S8 | Before figuring out what/where it is, make sure to ask what it is trying to stop or what it wants. It may, of course, be your inner child, mad that it’s taken you so long to come back, or it may be your inherited parent script, or something from earlier in the day, or a bit of each. | PASS | PASS | PASS | yes (`G-S8/FOR-JOEL.txt`) |
| G-S9 | b480 S9 | Your parent script is made up of a collection of rules and ways of treating yourself that you adopted as a child (mostly based on how you were treated by your parent(s)). It doesn’t always take the form of a voice. This is not the inner adult (Nurturer, Protector, Guide) that you consciously build. | PASS | PASS | PASS | yes (`G-S9/FOR-JOEL.txt`) |
| G-S10 | b480 S10 | Borrow some from someone else if you need to, but make sure they're stable and not someone who will try to direct your trip. | PASS | PASS | PASS | yes (`G-S10/FOR-JOEL.txt`) |

## What changed during the gate

- **G-S5.** Its first draft ended "Don't fake it." (batch 479's third sample, after "You don't have to fake it!" failed the linter's coach register). The preservation reviewer failed it: his line is a release ("no faking required") and the draft made it a rule (`superseded/G-S5-dont-fake-it/REVIEW-preservation.json`; the two cold readers had passed it). The new draft ends on his own three words, "no faking required", and went through all three roles again (`BRIEF-<role>-e.md`). Cold reader 1 of group b, which had read the first draft, also reviewed the new one when its files changed under it; group e's fresh cold reader 1 wrote after it, so the file on record is that fresh reader's (`G-S5/REVIEW-cold_read_1.json`, context id `b480-gate-cold_read_1-subagent-e`).
- **G-S8 and G-S9** failed the linter before any review (E125, a list of three without a casual catch-all; R2, the paragraph's "This" made "It"), so each got the smallest fix first: IC-A14's own "or a bit of each" for Emulate's "or a combination", and "This" put back (`../b480/make_b480.py`). **G-S7** got his "keeps" back for Emulate's "helps to keep" on the meaning read (`../b480/REVIEW-1.md`).
- **The writer's lint reasons.** Several reviewers noted that the D9 and B7 reasons in G-S2 to G-S6's manifests were written once for the batch and cite asides from other drafts ("if I can put it that way", "Don't fake it."); each reviewer judged those findings on the draft itself. G-S5's new draft and G-S7 to G-S10 have reasons written for each draft (`fill_ledgers.py` LINT_BY).

## The reviewers

- cold_read_1, `b479-gate-cold_read_1-subagent-a`: G-S2, G-S3a, G-S3b
- cold_read_1, `b479-gate-cold_read_1-subagent-b`: G-S4, G-S6
- cold_read_1, `b480-gate-cold_read_1-subagent-c`: G-S7, G-S8
- cold_read_1, `b480-gate-cold_read_1-subagent-d`: G-S9, G-S10
- cold_read_1, `b480-gate-cold_read_1-subagent-e`: G-S5
- cold_read_2, `b479-gate-cold_read_2-subagent-a`: G-S2, G-S3a, G-S3b
- cold_read_2, `b479-gate-cold_read_2-subagent-b`: G-S4, G-S6
- cold_read_2, `b480-gate-cold_read_2-subagent-c`: G-S7, G-S8
- cold_read_2, `b480-gate-cold_read_2-subagent-d`: G-S9, G-S10
- cold_read_2, `b480-gate-cold_read_2-subagent-e`: G-S5
- preservation, `b479-gate-preservation-subagent-a`: G-S2, G-S3a, G-S3b
- preservation, `b479-gate-preservation-subagent-b`: G-S4, G-S6
- preservation, `b480-gate-preservation-subagent-c`: G-S7, G-S8
- preservation, `b480-gate-preservation-subagent-d`: G-S9, G-S10
- preservation, `b480-gate-preservation-subagent-e`: G-S5
