# r14: the fuels stretch, from his four answers (2026-11-05)

Joel, 15:18 UTC (`../../../experiments/t13-answers/`), on the four cards I had held in `../r13/fuels/CARDS-DRAFT.md`: "1agree with you / 2agree / 3.agree / 4. go ahead". And: "why did you not give me the cards as the html file in context as the repo requires?" The cards now go on the marking page the turn they're written (gate E363 (gut)). This turn's page is `b9/`.

**The marking page (batch 9):** https://claude.ai/artifact/EyKenia9ksMXj8pH6ZMCkE, five cards, its Markdown view `b9/REVIEW-CARDS.md`, built by `b9/build_review.py` on r12 (the text in his post). It keeps his answers in the artifact's store (db) and exports them as JSON.

## What each card holds, and how it was checked

Every wording below went through the same steps. A newcomer read the draft fresh (`hidden_links.py`, E355); each gap was fixed in a new draft or dropped with a note. A blind reader checked the meaning against the sources (`MEANING-VERDICTS-*.json`). Then the web app checked it with the paragraph it leans on (E349). `hidden_links.py check` passes for all three paragraphs.

### P20, glutamine (F9-1 and F9-2)

- F9-1 is r13's rewrite of the three mechanism sentences, which were AI windows in his post. It reaches him here for the first time.
- F9-2 is card 3's clause, ", on top of what they get from their meals" (`DRAFT-P20-v2.txt`). It ties "faster" to an amount, so "extra" follows.
- The fresh read (`links-p20/draft/`) raised only gaps in his kept sentences. The two gaps card 3 fixed didn't come back. Meaning check G102 passed.
- With P19, prediction #147 Human at 0.8: [Human Written, 100%](https://www.pangram.com/history/7626ceb3-21e5-41b2-b9f1-53fce9a939aa), one window, High.

### P21, the dose (F9-3, card 4)

- **The first read** (`links-p21/`) asked whether the baseline is for them at all if they don't train, in a section about a leaky gut, and how training breaks down the lining ("I thought exercise was good").
- **Eight drafts.** The page has v7 (`DRAFT-P21-v7.txt`):
  - The baseline's purpose for everyone: "to keep your enterocytes fed".
  - Training as its second job, in his words: "The 5g also counters the breakdown of the gut lining that hard or long training causes".
  - How: blood goes to the working muscles, and the swallowed glutamine still reaches the enterocytes from inside the gut.
  - What each draft's read changed:
    - v1 said "enough" before the reader knew training mattered.
    - v3 and v4 put the reason first, and readers then asked why a training sentence followed the dose.
    - v5 and v6 led with the point.
    - Two readers asked how swallowed glutamine could make up for what the blood no longer brings, so v6 to v8 say it.
- **Meaning checks** G104, G105, G107, G109, G111, G113 and G114 all passed.
- **His call, on the card:** whether the 5g is everyone's baseline, as I read it, or only for people who train hard.
- **Found:** the trials where glutamine cut training's gut leak used 0.25 to 0.9 g per kg of lean mass before a run, not 5g a day ([Pugh 2017](https://link.springer.com/article/10.1007/s00421-017-3744-4)). His claim stays as it is; the card says so.
- **Sources for the added how:**
  - Strenuous exercise cuts blood flow to the gut, and the gut lining loses its integrity ([van Wijck 2012](https://pubmed.ncbi.nlm.nih.gov/22517770/); the abstract was read on its [ACU record](https://acuresearchbank.acu.edu.au/item/87560/physiology-and-pathophysiology-of-splanchnic-hypoperfusion-and-intestinal-injury-during-exercise-strategies-for-evaluation-and-prevention)).
  - High-intensity or prolonged exercise does this; moderate exercise helps the barrier ([systematic review](https://pmc.ncbi.nlm.nih.gov/articles/PMC12175863/)).
  - The gut takes up most of a swallowed dose ([Hankard 1995](https://pubmed.ncbi.nlm.nih.gov/7485479/)).
- **The checks** (lineage r14-fuels-p21, with P20 v2):
  - #148, v6: [Human Written](https://www.pangram.com/history/9d4a68b0-f102-4ba0-b1b8-db1a13152a3b), AI 0%. His Low sentences now read High. Two new sentences of mine: Medium ("While you train ...") and Low ("The glutamine you swallow reaches them from inside your gut instead.").
  - #149, v7: [Human Written](https://www.pangram.com/history/cd90475f-4199-4cc0-b764-b3e88005929d), AI 0%. All High but "But the glutamine you swallow still gets to them, straight from inside your gut." (Medium).
  - #151, v8: [Human Written](https://www.pangram.com/history/63798a2a-0981-4934-a2c1-e90d18de6a66), AI 0%. v8 said that sentence's link ("doesn't need that blood, since it reaches them from inside your gut"), and it read Low. v7 stays as the better of the two.
  - Next try for that sentence: cut it (P20 already says the enterocytes take glutamine in as soon as it reaches them), or fold it into the blood sentence.

### P22, the caution (F9-4, cards 1 and 2)

- **Six drafts.** The page has v11 (`DRAFT-P22-v11.txt`):
  - It covers any active cancer and sends the reader to their oncologist, before the 5g and especially before the 10-30g.
  - The portal-vein sentence is gone.
  - It says how swallowed glutamine reaches a cancer, and why the bigger dose matters.
- **What each draft's read changed:**
  - v6's "any" read as any glutamine, food included.
  - v7 and v8 drew "how does it get to a cancer elsewhere?"
  - v9 and v10 drew "why would a bigger dose mean more gets through?"
  - v12 cut "to fuel their growth" and "where a cancer can get to it", which the tell panel had flagged. Its read then lost what the caution warns of and the step its "So" turns on, so the caution went back to v11.
  - Three readers asked what an oncologist is. The word stays: the people this is for have one. His article says "get cleared by a gastroenterologist" the same way.
- **Meaning checks** G101, G103, G106, G108, G110 and G112 all passed.
- **Sources:**
  - Many tumors use glutamine avidly ([Souba 1993](https://pubmed.ncbi.nlm.nih.gov/8257221/)).
  - The gut and liver take up 74% of a small swallowed dose on its first pass and 53% of a large one ([Hankard 1995](https://pubmed.ncbi.nlm.nih.gov/7485479/)).
  - Blood glutamine rises with the oral dose ([Ziegler 1990](https://scilit.com/publications/3818c7c307b06a89e57d20b459c23ead)).
  - A tumor in the liver is fed mainly by the hepatic artery ([review](https://pmc.ncbi.nlm.nih.gov/articles/PMC3036477)).
- **Try 3 of its lineage**, with P21 v7 and the tell panel's notes (`../r13/fuels/panel-p22/`). Prediction #150, Human at 0.5: [Human Written](https://www.pangram.com/history/b3f527c2-1d60-4d21-9135-2b53da1a9894), AI 0%. The whole caution reads High.

### The stretch, P19 to P22 (its one recheck)

- Lineage r12-fuels, try 2, after each paragraph was checked by itself (E343). Prediction #152, Human at 0.6.
- Result: [Human Written](https://www.pangram.com/history/8d1686ec-5214-4648-abc2-cebbeb208ebb), AI 0%, 456 words. Every window is High except P21's "But the glutamine you swallow still gets to them, straight from inside your gut." (Medium).
- In his post (r12, #140) the stretch read [AI Detected, 26%](https://www.pangram.com/history/2103ebd9-b274-4d8c-b32a-53819d5c740d), with five AI windows.

### F9-5, a question

Six readers asked about his dose sentence. It reads High in every check, so it stays as it is. Their questions:
- Is pure glutamine a powder or a pill, taken with meals or apart?
- What is an acute exposure?
- Which stress?
- How gradually, and how to pick between 10 and 30g?

The card asks whether he wants any of that said, in his words.

## Files

- **Drafts:** `DRAFT-P20-v2.txt`, `DRAFT-P21-v1.txt` to `v8`, `DRAFT-P22-v6.txt` to `v12`.
- **Reads:**
  - `links-p20/`: the first read, carried from r13, and `draft/`.
  - `links-p21/`: the first read, then `draft-v1/` to `draft-v7/`, with `draft/` for v8.
  - `links-p22/`: the first read, carried from r13, then `draft-v6/` to `draft-v10/` and `draft-v12/`, with `draft/` for v11.
- **Meaning checks:** `MEANING-PACKET-*.json` and `MEANING-VERDICTS-*.json`, items 1 to 8.
- **Check texts and results:** `CHECK-*.txt` and `RESULTS-*.json`. Their predictions are #147 to #152 in `../../pangram-ledger.jsonl`.
