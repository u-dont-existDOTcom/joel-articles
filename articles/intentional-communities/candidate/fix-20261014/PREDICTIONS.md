# Predictions and Pangram results, 2026-10-14 (Joel's message of 03:04 UTC)

Pangram's web app (the dashboard in the desktop app's browser pane, Joel's Pro account). Each batch's predictions are written here before its call; the results come from the History, with Pangram's own UTC time for each check (this turn reads the clock only at its start and end, so the History's times stand in for mid-turn clock reads). Batches go through `tools/humanization/pangram_gate.py` (texts in `drafts.json`, gate records in `GATE.json`).

## Batch 274g: section 12 v13 (Joel's W1 P2 and P3)

| text | mine | why |
|---|---|---|
| J12-P2 | Human | his P2; he said his first version of it read human once the quip and the second "we have" sentence came out, and this one only adds contractions and "We're given" |
| J12-P3 | Human | his P3, the same words as the pair he checked ("human med conf") |
| J12-P2P3 | Human (weak) | the pair he checked was Human, medium; his preferred P2 differs from the one in that pair |
| S12v13 | Human (weak) | v12 was 100% Human by his check; his new P2 and P3 now follow each other, but a medium pair can drag a section to Mostly Human |

Results of 274g (Pangram's History, 2026-10-14 UTC): J12-P2 **Human (Human, low; 62 words)**, 04:30:09; J12-P3 **Human (Human, low; 93 words)**, 04:30:19; J12-P2P3 **Human (Human, medium; 155 words)**, 04:30:30; S12v13 **Human (100%), "Human Written", Human high** (950 words), 04:30:41. Score: 4 of 4. Section 12 v13 passes on its first try.

## Batch 275g: section 2 v3.2 (Joel's F4 and F6)

| text | mine | why |
|---|---|---|
| J2-P38 | Human | his paragraph; the F4 sentence's "thieving, nor suddenly unlearning" is the kind of loose grammar a person writes |
| J2-P39 | Human | his paragraph; "jealousy rears its head" is a stock idiom, but the paragraph around it is his and passed before |
| S2v32 | Human | v3.1 was 100% Human; two sentences of his changed |

Results of 275g (Pangram's History, 2026-10-14 UTC): J2-P38 **Human (Human, low; 58 words)**, 05:11:02; J2-P39 **Human (Human, low; 58 words)**, 05:11:12; S2v32 **Human (100%), "Human Written", Human high** (627 words), 05:11:23. Score: 3 of 3. Section 2 v3.2 passes on its first try.

## Batch 276g: sections 3, 4, 7, 9 and 10 with the sweep's fixes

Gate records in `GATE.json` (kind "edit", E173: a fix of a few words in a paragraph that passed before; the march reads in `gate/MARCH-labels.txt` and `gate/MARCH2-labels.txt` give each edited paragraph the same labels as its installed version).

| text | mine | why |
|---|---|---|
| E-S3P4f | Human (weak) | the new last sentence is closer to the published one ("whose turn it is ... a second"), which read AI in the published section |
| E-S3P10f | Human (weak) | "can use it in all their other roles" is plain; "gifted" back from the published |
| S3v12 | Human | v11 was 100% Human; two sentences changed |
| E-S4I1 | Human | his two paragraphs with one word of mine ("inner pl/ork" for "it") |
| S4v111 | Human | his final section, checked by him, with that one word |
| E-S7P6f | Human (weak) | two appositive glosses in the opening sentence (the linter's packed-sentence REVIEW) |
| S7v4 | Human | |
| E-S9P2f | Human | his story voice; the gloss sits in the middle of it |
| E-S9P18f | Human | shorter by a closing disclaimer |
| S9v15 | Human (weak) | section 9 took many rounds before; two small changes |
| E-S10P9f | Human (weak) | the new opening sentence names two principles in a row, a slightly abstract run |
| S10v3 | Human | |
