# Batch 478g: question 66's changed paragraphs (2026-10-25, after Joel's message of 23:05 UTC)

Joel's answers to 66 (`../RECORD-66.json`) change four paragraphs of the community article, whose post he pasted on
2026-10-25 and which read Human Written as a whole (IC-whole#1, 0 of 72 windows AI). Each changed paragraph was checked
where it sits, through the Pangram API on the laptop (Joel's key, model pangram-4, which answered 4.1;
`/home/joel/ai-work/claude-dangerous-lane/pangram-api/ic-b478/`, `round1.log` and `round2.log` here, SHA-256 checked
both ways). The web app in the desktop app's browser was signed out ("Log in", "Verify you are human"), and signing in is
Joel's. Predictions were in the ledger (`../../../pangram-ledger.jsonl`) before each call; four were first recorded as
469g, a number the hypnosis guide lane had used, voided unsent and recorded again as 478g.

| Key | Predicted | Chance | What | Pangram |
| --- | --- | --- | --- | --- |
| IC-E1-p+prev | Human | 90% | IC-E1's paragraph (45 words) with the one before it, 104 words | **Mixed** (AI Detected, 27% AI): the AI window (Low, 36 words) is the second sentence of the paragraph before, unchanged; IC-E1's paragraph, its new clause included, two Human windows. [check](https://www.pangram.com/history/07e5a128-04f5-485f-96d8-2c69dcdc5ee3) |
| IC-E2-p | Human | 85% | IC-E2's paragraph, 80 words | **Human** (High). [check](https://www.pangram.com/history/39c38460-b4cd-4010-ace5-7c29f11907e3) |
| IC-E3-p | Human | 75% | IC-E3's paragraph, 110 words | **Human** (High). [check](https://www.pangram.com/history/bd553e51-fe5f-446d-9845-0f1cff0d2f8a) |
| IC-T1-p | Human | 85% | IC-T1's paragraph, 57 words | **Human** (High). [check](https://www.pangram.com/history/be320a55-fcc7-47c1-b480-7274d72fa0af) |
| IC-W2-p | AI | 50% | the paragraph before IC-E1 alone, 59 words, to see whether its window was real | **Human** (High, one window). [check](https://www.pangram.com/history/710c78cf-92db-43bb-9a42-9053b5ca2d06) |

Results of 478g: 3 of 5 right. Both misses are the same window: the pair's boundaries put the second sentence of the
paragraph before IC-E1 in a window of its own, and Pangram read that window AI at Low; alone, the paragraph is one Human
window at High. Every changed paragraph reads Human where it sits, so the four cards go to Joel as words to change in
Substack (`../SUBSTACK-EDITS.md`).
