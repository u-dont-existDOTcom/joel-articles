# Round 24's answers put in, and the checks of 2026-11-08

His round-24 export (exported 15:01 UTC, sent 15:07 UTC): `../../review/r24/ANSWERS-R24-20261108-1501.json`; his words in
`../../experiments/t26-answers/joel-20261108-1507-r24-comments.txt`.

The guide is made from `GUIDE-BEFORE-R24.md` (the guide after round 23, frozen) by these, in order:

1. `apply_r24.py`: his four versions, as he sent them, "themself" fixed;
2. `swap_dashes.py`: the dash swap's newer rule (his "--") for the 19 blocks that still had spaced en dashes;
3. `merge_why.py`: Why Bad Trips Tend to Happen said once, under his (Re)defining "Bad Trip";
4. `drug_fixes.py`: the guide drug-neutral where it speaks generally (`DRUG-READ.md`, prompt `DRUG-READ-PROMPT.md`).

Fidelity against `../h01/FIDELITY-KEYS-R24.json`: PASS. Owner edits 63 pass, 0 failed. Keep-as-is: 20 kept, 12 meant cuts,
none gone or back.

## Pangram (his account's web app; each prediction in `../pangram-ledger.jsonl` first)

| text | result | windows | link |
|---|---|---|---|
| His checks, read from his history: the first five minutes and his don'ts, first try | Human Written | High 136, Medium 41 (the reminder and its script), High 151, Medium 17 (his last sentence) | [6f85cc29](https://www.pangram.com/history/6f85cc29-5846-47cd-ae4e-64ef321cb3da) |
| the same, his fix (the reminder as one sentence, the last sentence reworded) | Human Written | High 335, one window | [82851dc3](https://www.pangram.com/history/82851dc3-bbf7-48c7-a771-974182a45f22) |
| his Give the Session | Human Written | High 429, one window | [0469ebb9](https://www.pangram.com/history/0469ebb9-2f6c-452e-9c3e-25010416da14) |
| his (Re)defining "Bad Trip", the section alone (`TEST-REDEF.txt`) | Human Written, 0% AI | High 113, Medium 18 ("Be kind to yourself ..."), High 20, Medium 17 ("But if you had no intention ..."), High 16, Medium 26 (the last two sentences) | [c192b361](https://www.pangram.com/history/c192b361-98f5-4c64-bdc4-6df38dd0b62f) |
| his (Re)defining's second paragraph with ", or how hard you pushed a practice" (`NEW-B330b.txt`) | Human Written, 0% AI | High 90, Medium 18 ("Be kind to yourself ...") | [f99fb1f0](https://www.pangram.com/history/f99fb1f0-34d7-4013-a3bb-95dc4b86645c) |
| his Give the Session's first paragraph alone, "ahead of time" (`NEW-B366a.txt` before "beforehand") | AI Generated, 100% | AI Low 22 (the changed sentence), AI Medium 31 (his second sentence, unchanged): 53 words alone | [d7b3540f](https://www.pangram.com/history/d7b3540f-e331-4ec5-ae36-3e328cc1f3c7) |
| his Give the Session, "think through beforehand" for "before you take anything" (`TEST-DRUG-START.txt`) | Human Written, 0% AI | High 426, one window | [14a16456](https://www.pangram.com/history/14a16456-64d6-4f7e-b4b6-0e6686fa3d9e) |

The paragraph alone read AI with his own second sentence unchanged, so at 53 words it tells nothing about the change; the
section is the test, and with "beforehand" (moved up, so it doesn't repeat his "ahead of time" two sentences later) it
reads as his did. Receipts: `NEW-B330b.receipt.json`, `TEST-DRUG-START.receipt.json`, `NEW-B319.receipt.json` (the needed
read in `NEEDED-READ.md`). No Rash Actions' bold line went in with its change unchecked: its stretch read Mixed before
(`../h28-20261107/TEST-base-N4.txt`), so it gets its check with that stretch's humanizing.

## Left for later

- For the Person Helping's opening line ("A good sitter is not there to win a philosophy debate, perform a rescue
  fantasy, impose an interpretation, or demonstrate spiritual advancement.") repeats his anchor line and don'ts except
  for "perform a rescue fantasy"; the paragraph left after its cut needs "Zendo-style" explained where it is first used
  (`NEEDED-READ.md`). With that section's humanizing.
- Round 25's card WHY-LESSON-CUT (the merge's repeated lesson line, warning W102).
