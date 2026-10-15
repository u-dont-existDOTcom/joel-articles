# Predictions and Pangram results: batch 291g (2026-10-15, Joel's 31 a)

Pangram's web app (the dashboard in the desktop app's browser pane, Joel's Pro account). Section 13 v10 paragraphs whose records came back clean in gate round r8 (`s13/review-r8/`), and H2-P2 again beside H2-P1, which now reads Human alone (289g). Texts in `drafts.json`, records in `GATE.json` (built by `make_batch.py`). Predictions written before the call; results from the History, each with its check link (E175).

## Batch 291g

| text | mine | why | Pangram |
|---|---|---|---|
| S13v10-2P1P2 | Human | the monologue paragraph (Human alone) and the values list (Human in a window of 288g) | **Human** (medium; 103 words), 16:29:40, [check](https://www.pangram.com/history/53f10379-9ba7-4786-ac7c-f4bf3426e5d0) |
| S13v10-2P3 | AI | five questions in a row, and the meaning fixes made the first and fourth nearly the published ones ("Could an LGBTQ+ member live openly", "taught to question their sexual identities at an early age") | **Human** (low; 77 words), 16:29:51, [check](https://www.pangram.com/history/dc84debe-4b05-42e1-8588-6f9c0ed3d677) |
| S13v10-2P3P3b | AI | goes with the paragraph above | **Human** (medium; 119 words), 16:30:04, [check](https://www.pangram.com/history/1b705e5a-900b-47bc-850f-168a91f6d270) |
| S13v10-2P4 | Human | Emulate's frame and its parenthesis; four short questions; the closing remark | **Human** (low; 76 words), 16:30:14, [check](https://www.pangram.com/history/1f34a5f2-3597-4a7f-ae10-5011087402ec) |
| S13v10-2P3bP4 | Human | the experiment line (a question and an exclamation) before the paragraph above | **Human** (medium; 118 words), 16:30:25, [check](https://www.pangram.com/history/f71ecdc3-4a8f-4e02-b20f-f6246269e475) |
| S13v10-5P2 | AI | his line, then five questions that now carry the published list nearly item by item | **AI** (AI Detected: AI-Generated, medium, 71 words from "That said" through "without endangering others?"; Human, medium, 43), 16:30:37, [check](https://www.pangram.com/history/6f743823-7d92-4bb4-b576-368896475b56) |
| S13v10-5P4 | Human | "Why bother? Because ...", Emulate's "And remember that although ..." | **AI** (AI-Generated, low; 70 words, the whole text), 16:30:49, [check](https://www.pangram.com/history/8592c980-ad7c-4480-8f65-c44a1a4cd78a) |

Results of 291g (Pangram's History, 2026-10-15 UTC): the values heading's paragraphs all read Human: the vacation-rental paragraph with the values list after it, the sexuality and gender paragraph alone and with the experiment line, and the compare-your-values paragraph alone and with the experiment line before it. The removal process (H5-P2) read AI over its first 71 words, the opening, Joel's line and the first three questions (the rest Human), and the mediator paragraph (H5-P4) read AI over its whole length, low confidence. Both go to a fresh Emulate round from v11 (round f). Score: 4 of 7 (right: S13v10-2P1P2, S13v10-2P4, S13v10-2P3bP4, S13v10-5P2). Every text checked is the one in `drafts.json` (same SHA-256).
