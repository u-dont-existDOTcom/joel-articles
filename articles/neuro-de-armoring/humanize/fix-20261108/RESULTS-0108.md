# Results, 8 November (after his answers of 00:49 UTC)

Predictions first, then the Pangram web app, one paragraph a check (ledger `../pangram-ledger.jsonl`, batches b0108).

| key | what it is | predicted | read | link |
|---|---|---|---|---|
| HIS37 | his version of block 37 (the Mechanism), typos and links fixed | Human | Human Written, Human High 137, Medium 13 | [3630663f](https://www.pangram.com/history/3630663f-3104-4ce7-86f7-462cbb26601d) |
| HIS38 | his version of block 38 (the Secondary Signal Dial) | Human | Human Written, Human High 55 | [e798ace7](https://www.pangram.com/history/e798ace7-cc92-45ff-973e-ceaf1f5ed2c4) |
| B039n | block 39 (D-serine and DCS) after the needed read: the GluD clause out | Human (miss) | AI Detected, 98% AI: Low 28, High 53, Medium 6, High 52 | [7768cb2f](https://www.pangram.com/history/7768cb2f-aa9a-4ab2-b99e-7e14ac8379f9) |
| PAIR-040-041n | blocks 40 and 41 (the Brake, the Lock) after the needed read: one picture, receptor name out, "voltage" to "calcium" | Human (miss) | AI Generated, 100% AI, High 93 | [ca20c43c](https://www.pangram.com/history/ca20c43c-e69b-4360-a7e9-fb4941bbb23f) |
| T37b | HIS37 with "swell and" cut (card SC-37) | Human | Human Written, Human High 148 | [755ca0fd](https://www.pangram.com/history/755ca0fd-b05f-4092-95b2-6e9da5daa36f) |
| T38b | HIS38 with its first clause corrected (card SC-38) | Human | Human Written, Human High 55 | [e3845c44](https://www.pangram.com/history/e3845c44-7bf0-4e7d-93a8-706b596c9c4b) |

What went in:
- His two versions (`apply_his_x1107c.py`, `APPLIED-HIS-X1107C.json`).
- B039n, B040n and B041n (`apply_0108n.py`, `APPLIED-0108N.json`): they read AI, as the versions they replace did, but
  they cut what the reader can't use and fix "less of the voltage gets through". B040n also drops the Gemini label
  "("Lock, Stock, and Barrel")": only "Lock" names a tool. `fidelity_keys.py` PASS.

What waits for him: the two science fixes in his own words, cards SC-37 and SC-38
(`x1108a/REVIEW-X1108A.md`, https://claude.ai/artifact/WKR3sLVAEMvR3RJTY7GAps).

Sources opened for the cards: [Choi 1987](https://pmc.ncbi.nlm.nih.gov/articles/PMC6568907) (early swelling depends on
sodium and chloride; calcium drives the later damage), [Goldberg and Choi 1993](https://pmc.ncbi.nlm.nih.gov/articles/PMC6576549)
(the same split), [Hansen et al. 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC6080888) (magnesium blocks NMDA at
rest, released by the depolarization AMPA activation brings; NMDA is highly calcium-permeable),
[Schmid et al. 2009](https://pmc.ncbi.nlm.nih.gov/articles/PMC2700928) (the delta2 pore, low calcium permeability).
