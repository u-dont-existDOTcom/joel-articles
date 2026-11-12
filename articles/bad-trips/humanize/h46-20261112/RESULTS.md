# Turn 37 (2026-11-12): his round-36 answers, the read of his 112 fixes, and the first carries written against it

His round-36 export of 2026-11-12 14:45:53 UTC (`../../review/r36/ANSWERS-R36-20261112-1445.json`): MEDICAL-HOW "a", with
"have you systematically looked at all of the fixes i've shown you and what are the idfferences in how you write vs how i
fix?"; TEACH-SS revised with his version and three checks (52abd79e AI, 54dd2f4b Mostly Human, 9e32c090 Human High 121).

## His Serotonin Syndrome version, as it goes in

| test | what | result | link |
|---|---|---|---|
| ss-his | his version with "the these", his missing period and "Hypertonia" fixed | Human Written: Human Medium 17, High 64, Medium 10, High 19, Medium 10 | [9cb1844e](https://www.pangram.com/history/9cb1844e-99e8-4fe3-bcad-a917ed10f1aa) |
| ss-his-fix2 | his exact text with only "the these" made "these" | Human Written: Human Medium 17 (the heading and first sentence), High 103 | [0dfe5d10](https://www.pangram.com/history/0dfe5d10-9de1-43ad-8062-4dedd8b8fea2) |

The second is in the guide (`../../review/r36/apply_r36.py`); his exact text read High throughout (9e32c090), so the one
fix is on round 37 as his call.

## The read of his fixes

`his-fixes/HOW-HE-FIXES.md`: 112 fixes in six lanes and his eight teaching tries; what he changes, counted; what flipped
Pangram, in his words; eight ways my drafts differ from his fixes. From it: `tools/humanization/his_fixes_brief.md` (a
fresh reader marks every sentence of mine that still reads one of the eight ways; `sense_receipt.py` refuses a receipt
without that read), and the linter's O69 (two correction or contrast frames in a paragraph) and O70 ("different from"
twice), each measured against his 112 versions first.

## The first carries written against it

TEACH-SS's promise: "I test what it teaches on the sections above." Each draft read against his fixes, three drafts each
(`HIS-FIXES-READ.md`), its needed read (`NEEDED-READ.md`), its receipt (`make_receipts.py`), the fidelity check with it in
(`apply_h46.py --dry`, PASS) and its prediction in the ledger (#458, #459).

| test | what | result | link |
|---|---|---|---|
| chest-c3 | Chest Pain and Injury's branch paragraph: the mild case first, one serious sign a line, the action after | AI Generated, 100%: AI High 61, Medium 19, High 19, Medium 19, High 14, Medium 17 | [2f1b6aa2](https://www.pangram.com/history/2f1b6aa2-e672-4b5f-aeb4-6479ccf56025) |
| brain-c3 | My Brain Feels Damaged's checks: one check a line, what to do when one shows a sign said after them | AI Generated, 100%: AI Medium 19, High 17, Low 11, Medium 100, High 39 | [0eeefa6e](https://www.pangram.com/history/0eeefa6e-c72f-4ea6-b74e-fab541aca12f) |

Both predicted AI; neither went in. The reads changed what the texts say (a missing "call medics", the signs named, no
repeated shapes the readers could find), and Pangram still read them AI, with more Medium and Low windows than before. So
round 37's teaching card is Chest Pain's branch paragraph, a shape none of his lessons has had yet: two cases, how to tell
them apart, and what to do when you can't.
