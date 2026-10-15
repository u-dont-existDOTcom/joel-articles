# Predictions and Pangram results: batch 299g (2026-10-15, after Joel's 32 b)

Pangram's web app (the dashboard in the desktop app's browser pane, Joel's Pro account). Section 13 v21 read 56% AI as a whole (298g, [check](https://www.pangram.com/history/5e450ea7-ed52-402b-bae4-de06d266aec7)), though each of its 32 parts reads Human on its own text (`s13/b298/COVERAGE.md`). Its windows, mapped onto the paragraphs: Human over the heading, H1-P1 and H1-P2; AI from H1-P3 through about the end of H3-P4 (894 words); Human from H3-P5 into H4-P9; AI from the middle of H4-P9 through H5-P2 (240); then the last two sentences of each of H5-P3 and H5-P4. This batch: runs of two paragraphs across the first AI window, the stretch of the second, and the last three subsections whole (the first two fail the linter's landing rule, B7/B13, so they go as pairs). A stretch can pass alone and fail in the section (`docs/HUMANIZATION-GATE.md`, 248g), so a pass here shows where not to look first, not what passes. A span's records are its parts' records (`s13/b298/GATE.json`); built by `make_batch.py`, texts in `drafts.json`, records in `GATE.json`. Pass means 100% Human; "Mostly Human" is not a pass. Predictions written before the call; results from the History, each with its check link (E175).

## Batch 299g

| text | mine | why | Pangram |
|---|---|---|---|
| S13v21-1P3P4 | Human | each read Human alone (H1-P3 with its neighbors, H1-P4 medium); the window starts on H1-P3's first sentence, but a pair is short evidence | |
| S13v21-2P1P2 | Human | the vacation-rental monologue and the list to bring; both read Human alone and as a pair before (S13v10-2P1P2) | |
| S13v21-2P3P3b | Human | the questions on sexuality and gender, then "Willing to experiment?"; both read Human alone, low confidence | |
| S13v21-2P4h3P1 | Human | the comparison questions, the heading and way B, which read Human with its heading (294g) | |
| S13v21-3P2P3 | AI | the most list-heavy pair: the legal forms and the decisions, then three "important" sentences and two lists of resources, 228 words | |
| S13v21-H3 | AI | the land subsection whole, 430 words, nearly all of it inside the first window | |
| S13v21-H4 | Human | the visitor subsection read Human in the section (679 words) up to the middle of H4-P9; the risk is P9's tail | |
| S13v21-4P9h5P2 | AI | the second window's stretch: the rights of non-members, the heading, the safe-community paragraph and the run of seven questions | |
| S13v21-H5 | AI | three of the section's AI windows fall in it: H5-P2 and the tails of H5-P3 and H5-P4 | |
