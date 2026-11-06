# r21: Phase 5's first two steps, try 3, and the whole-article checks of tries 2 and 3

r21 is r17 with the same two clarity fixes as r20 and a third try at Phase 5's first two steps, the three sentences his
extension read Human at Low confidence in the whole article (draft B, #183; calibrated 0.79, 0.58 and 0.63). Built by
`build_r21.py`; the changes, reasons and sources are in `CHANGES.json`.

## Why this try

- Try 1 (`../r19/`) joined each step to what it does and read worse than its control in the cut of Phases 4 and 5 (59%
  AI against 30%, #184 and #186).
- Try 2 (`../r20/`) put the reader's situation first and read no better than its control in the cut of Phases 3 to 6
  (#188 against #187). That cut reads the steps AI even unchanged, so it can't judge a fix (lesson gut-2026-11-06f).
- His own fix of the model's Phase 1, after three of our versions read AI, kept its frames and glossed each term in a
  plain parenthesis or clause ("which in medical lingo is called", "not flowing well", "an extract of beet greens"), and
  it reads High in the whole article. Try 3 does that for Phase 5's steps: the frames and words stay, and a plain gloss
  goes where the reader would ask.

The two steps as try 3 has them:

> 1. Start by re-seeding with Davis's high-dose "SIBO Yogurt", fermented for 36 hours (store yogurt is fermented for 6 to
> 12, so this one ends up with hundreds of times more bacteria). It contains L. reuteri, to heal the lining and boost
> oxytocin (the "love hormone"), and L. gasseri, to produce bacteriocins (natural antibiotics) that kill SIBO.
>
> 2. Then feed the new healthy bacteria. Bulsiewicz says to bring more and more kinds of plants back into your diet,
> slowly (go too fast and you can get gassy and bloated while your gut bacteria adapt), until you're eating 30+
> different plants per week. Does anyone count their plants?

Sources for the two new facts:
- Davis on the 36 hours: [Defiant Health Radio, "Will eating yogurt change your life?"](https://defianthealthradio.buzzsprout.com/1795054/episodes/16962045-will-eating-yogurt-change-your-life)
  (a factory ferments yogurt "for about 6 to 12 hours"; his 36 hours gives "hundreds of times greater numbers of
  microbes").
- Bulsiewicz on going slowly: [Plant Based News, 27 April 2025](https://plantbasednews.org/lifestyle/health/gut-doctor-survival-guide-bloating-plant-based-diet/)
  (a switch to more fiber can bring gas and bloating while the gut microbes adapt).

The making-sense receipt for Phase 5 with try 3 is `checks/RECEIPT-r21-P5.json` (`checks/make_r21.py`; it passes).

## The whole-article checks

No cut can judge these steps (Phase 5 alone reads them High unchanged, #165; Phases 3 to 6 read them AI unchanged,
#187), so both tries go to the whole article through temporary Substack drafts, read by his Pangram extension (the free
route), each beside draft B:

| draft | text | prediction | result |
|---|---|---|---|
| B | r17 | #183 | Human Written; the two steps Low |
| C | r20 (try 2) | #189 | waiting for his extension |
| D | r21 (try 3) | #190 | waiting for his extension |

`substack/make_payloads.py` builds both payloads the way draft B's was built (r12.html, the live post's editor HTML,
with the new words; marks curled) and the text his extension reads (`substack/EXPECTED-TEXT-C.txt` and `-D.txt`). They
differ from draft B's text on three lines only: the glutamine dose paragraph and Phase 5's two steps.
