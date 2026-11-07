# r28 to r30: Phase 4's organ step joined to its paragraph, and batch 14

r27 (`../r27/README.md`) left Phase 4's one numbered step reading AI by itself in three wordings (#196, #199, #203), two
of them after the tell panel, while every section around it read Human (#194, #195). Joel's rule since 2026-11-06 23:59
UTC (gate gut-2026-11-07a): a paragraph or section that tests AI is fixed until it tests Human, before any whole-article
check.

The panel's second pass read the step as a summarizer relaying claims, which its rules read as a sense problem first
(E360): alone, the step has no reason in it. Its reason is the last sentence of Phase 4's first paragraph ("The problem is
likely an organ that isn't working right ..."), which its "So" points to. So from r28 the step is joined to that
paragraph, and the paragraph is what gets checked by itself.

| version | Phase 4's first paragraph, with the step joined | by itself |
|---|---|---|
| r28 | r27's post-panel wording of the two cases | [AI Detected, 51%](https://www.pangram.com/history/d18c0cd1-200b-476b-93ee-d5f54f6c20d6) (#204): the paragraph's own sentences Human, every sentence of the cases AI |
| r29 | r24's wording, which read High after this paragraph in both section checks | [AI Detected, 23%](https://www.pangram.com/history/13582f54-d1e2-4362-adac-f99aa4d96ca9) (#205): the paragraph High, the pancreas case Medium, the bile case AI Low |
| r30 | the bile case asked first, the way Phase 6 asks about mold | [Human Written, 0%](https://www.pangram.com/history/a45f149e-419f-4a39-be1a-4fd02dd738cb) (#206): High, with two short Medium windows |

What r29 showed: the bile case read AI when it copied the pancreas case's pattern word for word ("if ..., called ...,
you'd test for that with ..., and treat it with ..."), the panel's first flag. Phase 6 says the same kind of thing in
another shape and reads High in every check ("Could it be mold/mycotoxins, or Lyme? Get assessed for those, and if it
comes back positive, use specific binders ..."). r30's bile case takes that shape, with the reader asked first and then
doing the test and taking the binders:

> So check your organs, starting with your pancreas: if it doesn't make enough digestive enzymes, called Exocrine
> Pancreatic Insufficiency, you'd test for that with Stool Elastase, and treat it with high-dose enzymes. Or is it your
> bile? If too much of it reaches your colon, you get diarrhea, called Bile Acid Diarrhea. Get a SeHCAT test for it, and if
> it comes back positive, take bile binders.

Source for what Bile Acid Diarrhea is: [NICE DG44](https://nice.org.uk/guidance/dg44/documents/topic-description) (bile
acids that aren't absorbed reach the colon, and the excess there causes diarrhoea).

The protocol section with r30 in it, from its first line through Phase 6:
[Human Written, 0% AI](https://www.pangram.com/history/3ff02029-f214-43d0-a5f9-84ba75f13c07) (#207), 28 windows, all
High or Medium. The ledger names no window still open in r30, so the whole article can be checked.

## Files

- `build_r30.py` makes `r30.md` from `../r29/r29.md` (`CHANGES.json`); `../r28/` and `../r29/` hold the two tries before.
- `checks/make_r30.py` writes the check texts and their making-sense receipts (`CHECK-*.txt`, `RECEIPT-*.json`);
  `checks/RESULTS-r30-p4.json` and `RESULTS-r30-PR.json` are the two results.
- `b14/`: batch 14, five approve cards marked on r22 (r17 with batch 13's F13-1): F14-1, Phase 4; F14-2 to F14-5, Phase
  5's opener and steps (from `../r23/`). `build_review.py`, `REVIEW.json`, `REVIEW-CARDS.md`, the page and the artifact
  view; page https://claude.ai/artifact/9R79aHKAXZGaPQjbLNsvh7.
- `substack/make_payload_e.py`: draft E's payload, r12.html (the live post's editor HTML) with r30's words, and the
  one-item step list under Phase 4's first paragraph removed, since the step is in that paragraph now.
  `EXPECTED-TEXT-E.txt` is what his extension reads; it differs from draft B's on the glutamine dose paragraph, Phase 4's
  paragraph (two lines become one) and Phase 5's opener and steps. Prediction #208, frozen before the paste.
  `PASTED.json`: the draft made and pasted (words match), and its rendered text checked against `EXPECTED-TEXT-E.txt`
  exactly; the secret link went to Joel in chat, not into Git.

## Draft E's result

His extension read draft E [Human Written](https://www.pangram.com/feed/1c41fbd9-580a-4036-b526-95a96cb70c46)
(#208): every window Human, 7 High over 4,025 of its 4,040 words, 5 Medium of 1 to 5 words (the splits at "Dr." and
"And no snacking!"), no Low (`draft-e-check/`). He approved all five batch-14 cards; the version for his post is
`../r31/`.
