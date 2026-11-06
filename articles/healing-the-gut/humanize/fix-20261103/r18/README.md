# r18: a try that read worse, taken back (2026-11-06)

Gate E354 refused the whole-article check of r17 over three AI Low windows from group cuts of 2026-11-04: Phase 1's
heading with its first sentence (#125) and the stacks list (#131, #136). Following his rule ("if it's "low" we should fix
it", gut-2026-11-06a), `build_r18.py` rewrote them: Phase 1's sentence, and the list's intro and three items, his usual fixes first.
`checks/make_r18.py` wrote their receipts, and both stretches were checked in his account's web app:

- Phase 1 from its heading: [#179](https://www.pangram.com/history/dcfc1cd4-912e-4a21-865a-2e297f278f35), AI Detected
  (13.6%): my sentence AI Medium with the heading, "This part is from T.C." AI Low.
- The stacks from their heading to the kits: [#180](https://www.pangram.com/history/579da364-48c8-490e-bd68-3cf167311fdd),
  AI Generated (99.99%): the intro and my list AI High, the kits AI Low and High.

Then the ledger's older checks showed the same words had already read Human, High in their own sections: Phase 1 with its
heading ([#139](https://www.pangram.com/history/e2b76d46-7dda-4141-b156-6aef920b7306), one 244-word window) and the whole
stacks section ([#137](https://www.pangram.com/history/3513e03a-c513-4ab7-992b-ff9ead34a379), the list inside a 215-word
window). The ledger had kept only those results' labels, so the gate couldn't see it. Their windows' text is now added as
correction lines, the old words stay, and r18 goes nowhere (gate gut-2026-11-06c).

`checks/CHECK-r17-phase1.txt` and `checks/CHECK-r17-stacks.txt` are the same cuts with the old words, frozen as #181 and
#182. Neither ran: Pangram's web app had signed out in the built-in browser and showed its "Verify you are human" box,
which is his to answer, so they wait for his sign-in.
