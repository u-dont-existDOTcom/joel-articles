# Turn 38 (2026-11-12): his Chest Pain move carried

His round-37 export of 2026-11-12 16:47:47 UTC (`../../review/r37/ANSWERS-R37-20261112-1647.json`): TEACH-CHEST revised
with his version and twelve checks (`../../experiments/t37-answers/JOEL-TRIES-TEACH-CHEST.md`), now in the guide
(`../../review/r37/apply_r37.py`). His try 7 changed one thing on my chest-c3: the action said before the list of signs
("For the following more serious signs (or if unsure), I'd also call medics:"), the two sentences after the list cut. It
read Human Written where chest-c3 had read AI Generated, 100%.

Two of my texts said what to do only after their checks: My Brain Feels Damaged's checks (brain-c3, h46) and Acute
Medical's opening (acute-r1-fix2, h45). Each test with its reads (`reads/`, `HIS-FIXES.json`, `NEEDED.json`), its receipt
(`make_receipts.py`), the fidelity check with it in (`apply_h48.py --dry`, PASS) and its prediction (#460, #461).

| test | what | result | link |
|---|---|---|---|
| brain-p1 | brain-c3 with only his move: the action and the can't-answer case said before the checks, the two sentences after them cut | AI Generated, 100%: AI High 61 (the heading through the first check), Low 11, Medium 84, High 19 (the last line) | [33a63991](https://www.pangram.com/history/33a63991-6b34-445a-b107-c9b91f1906a1) |
| acute-c1 | Acute Medical's opening rebuilt around the move: what to do first, its conditions after it, and the Call medics list pointed to instead of its six signs said again | Human Written: Human High 62 | [97bf9589](https://www.pangram.com/history/97bf9589-ad17-4cee-835f-a51fe47956fd) |

acute-c1 is in the guide (`apply_h48.py acute-c1`): B100 is its paragraph and B76 goes. I had predicted it AI at 0.45,
a miss (explained in the ledger).

brain-p1 read AI in every window, with the action now before the checks. So the move carried where the paragraph was
rebuilt around it, and not where it was added to checks that already read AI. Its windows still cover the opening (the
stroke-signs sentence the read against his fixes marked as opening on an authority), the checks, and the last line. The
lineage has read AI twice, so a next try of mine goes through the tell panel first; round 38's teaching card is these
checks instead (`../../review/r38/`).
