# r23: the stretch of Phases 3 to 6 fixed until it tests Human

Joel, 2026-11-06 23:59 UTC: "make sure you're fixing any paras or sections that test ai before you ask for whole
articel checks" (gate gut-2026-11-07a). The stretches that tested AI were the cut of Phases 4 and 5 (#186, 30% AI) and
the cut of Phases 3 to 6 (#187, 28% AI), unchanged text included; try 2's steps read AI in the whole article as well
(draft C, #189).

r23 is r22 (the article with every answer in, batch 13 included) with five changes (`build_r23.py`, `CHANGES.json`),
from the moves his own fixes make (neuro-2026-11-06b and e, his Phase 1):

| where | before | r23 |
|---|---|---|
| Phase 4, second organ case | If it's Bile Acid Diarrhea, the test is SeHCAT, and the treatment is bile binders. | And if bile is spilling into your colon and giving you diarrhea, called Bile Acid Diarrhea, you'd test for that with SeHCAT, and treat it with bile binders. |
| Phase 5, opening | Once you're clear of infection, you have to rebuild a diverse ecosystem to prevent relapse. | Cleared the infection? Then it's time to rebuild a diverse ecosystem in your gut, so the overgrowth doesn't come back. |
| Phase 5, step 1 | Start by re-seeding with Davis's high-dose "SIBO Yogurt", fermented for 36 hours. It contains L. reuteri, to heal the lining and boost oxytocin, and L. gasseri, to produce bacteriocins that kill SIBO. | Start by re-seeding your gut with Davis's high-dose "SIBO Yogurt", which you ferment at home for 36 hours. He picked its bacteria for what they do: L. reuteri heals your gut lining and boosts oxytocin (the "love hormone"), and L. gasseri makes bacteriocins, natural antibiotics that kill SIBO. |
| Phase 5, step 2 | Then feed the new healthy bacteria. Bulsiewicz says to slowly titrate plant diversity back into your diet, aiming for 30+ different plants per week. | Then feed the new healthy bacteria with plants, slowly, the way Bulsiewicz says: add a few new kinds at a time, until you eat 30+ different plants a week. |
| Phase 5, step 3 | Continue Pimentel's strict meal spacing from Phase 2 (4+ hours), forever, to keep the MMC cleaning wave active. | Keep spacing your meals 4+ hours apart, as in Phase 2, forever. |

His "Does anyone count their plants?" stays right after the number it jokes about.

## What the checks showed

| check | text | result |
|---|---|---|
| #191 | Phases 4 and 5, r23 | [Human Written, 0% AI](https://www.pangram.com/history/8dc695e5-8976-40c8-a4f4-f88bd96ef5e9): every window High or Medium, no Low |
| #192 | Phases 3 to 6, r23 | [Mostly Human Written, 4.2% AI](https://www.pangram.com/history/f6ccbb09-9b19-406e-947f-2b6357d97e67): Phase 5 and Phase 6 all High or Medium; one AI Low window, Phase 4's first organ case, after "So check your organs (Brown)." (Low) |
| #193 | Phases 4 and 5, try 3 (`../r21/`) | [Human Written, 0% AI](https://www.pangram.com/history/fa4cd031-8b4f-41e0-b580-40ecdf57fbe0): High and Medium, Low only on the one-word split at "Dr." |

So both moves lift Phase 5's steps out of AI in the cut of Phases 4 and 5; r23 also takes Phase 5 and Phase 6 to Human
in the longer cut. What's left is Phase 4's first organ case, which r24 (`../r24/`) joins to the check it starts.

Sources for the facts r23 states: [NICE DG44](https://nice.org.uk/guidance/dg44/documents/topic-description) (bile acids
that aren't absorbed reach the colon and cause diarrhoea); [Davis, Defiant Health Radio, "Here's a microbe you should
know about: Bacillus subtilis"](https://www.buzzsprout.com/1795054/episodes/17783323-here-s-a-microbe-you-should-know-about-bacillus-subtilis)
(he chose the original SIBO yogurt's strains, among them L. reuteri and L. gasseri, to make bacteriocins, "natural
peptide antibiotics effective in killing the species of SIBO"). Every window, with its text, is in
`checks/RESULTS-r23.json`; the receipts are `checks/RECEIPT-*.json` (`checks/make_r23.py`).
