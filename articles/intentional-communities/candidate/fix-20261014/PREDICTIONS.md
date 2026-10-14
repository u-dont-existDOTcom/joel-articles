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

Results of 276g (2026-10-14 UTC): E-S3P4f **Human (low; 77 words)**, 05:30:14; E-S3P10f **Human (low; 83)**, 05:30:24; S3v12 **Human (100%), "Human Written", high (558)**, 05:30:36; E-S4I1 (his reparenting paragraph with the I1 paragraph) **AI-Generated (low; 99 words), the whole pair**, 05:30:47; S4v111 **Human (100%), "Human Written", high (1,555)**, 05:31:01; E-S7P6f **Human (low; 68)**, 05:31:13; S7v4 **Human (100%), high (486)**, 05:31:25; E-S9P2f **Human (low; 65)**, 05:31:35; E-S9P18f **Human (medium; 108)**, 05:31:47; S9v15 **Human (100%), high (1,037)**, 05:31:59; E-S10P9f **AI-Generated (medium; 103 words), the whole paragraph**, 05:32:11; S10v3 **Human (100%), high (746)**, 05:32:23. Score: 10 of 12. Sections 3, 7 and 9 pass with every changed paragraph on the first try; sections 4 and 10 pass whole, but the I1 pair and P9 read AI.

## Batch 277g: sections 6, 8 and 11 with the sweep's fixes (and section 8's F10)

| text | mine | why |
|---|---|---|
| E-S6P8f | Human | the march has two breaks (the "Ok, so" and his "right?") |
| S6v22 | Human | |
| E-S8P10f (with the friend paragraph) | Human | "the usual promo video" is plainer than "another" |
| E-S8P12f | Human (weak) | the gloss makes a long first sentence longer |
| E-S8P20f | Human (weak) | "without the panic actually preventing abuse" is close to the published wording |
| E-S8P23f | Human (weak) | "A surprise has an end date." is short and flat |
| E-S8F10 | Human | his paragraph; my old sentence back at its end |
| E-S8P26f | Human (weak) | the new facts make a run of plain statements |
| S8v29 | Human (weak) | six changes in one section |
| E-S11P2f (with P1) | Human (weak) | the definition is a short last line |
| E-S11P4f | Human (weak) | a run of questions; it passed before with one more |
| E-S11P6f (with the four questions and P8) | Human | |
| E-S11P9f | Human | |
| E-S11P10f | Human | the list of signs passed before |
| S11v14 | Human (weak) | five changes |

## Batch 278g: controls for the section 4 pair (his v11 text as he gave it)

| text | mine | why |
|---|---|---|
| J4-orig-pair | AI | the pair with my one word read AI (276g); his reparenting paragraph is a definition with a list of three roles, which is likely what Pangram reads |
| J4-reparent | AI (weak) | the same paragraph alone |

Results of 277g (2026-10-14 UTC): E-S6P8f **Human (low; 69)**, 06:01:07; S6v22 **Human (100%), high (687)**, 06:01:18; E-S8P10f **Human (low; 67)**, 06:01:28; E-S8P12f **Human (medium; 109)**, 06:01:40; E-S8P20f **Human (low; 69)**, 06:01:51; E-S8P23f **Human (low; 56)**, 06:02:03; E-S8F10 **Human (medium; 136)**, 06:02:16; E-S8P26f **Human (medium; 124)**, 06:02:26; S8v29 **Human (100%), "Human Written", high (1,841)**, 06:02:37; E-S11P2f (with P1) **AI-Generated (low; 67), the whole pair**, 06:02:47; E-S11P4f **Human (medium; 147)**, 06:02:59; E-S11P6f (with the four questions and P8) **AI Detected: P6 and the questions Human (47), P8 AI (87)**, 06:03:13; E-S11P9f **Human (low; 59)**, 06:03:23; E-S11P10f **Human (low; 52)**, 06:03:34; S11v14 **"Mostly Human Written": one AI window, P4 from its second sentence to the end of its questions (82 words)**, 06:03:47. Score: 11 of 15. Sections 6 and 8 pass, every changed paragraph on its first try. Section 11 doesn't: P4's run of questions reads AI in the section though P4 passes alone.

Results of 278g: J4-orig-pair (his v11 pair as he gave it) **AI Detected: his reparenting paragraph Human (61), his "And it's built on ..." paragraph AI (36)**, 06:03:58; J4-reparent **Human (low; 61)**, 06:04:11. Score: 1 of 2. So the pair read AI before my word too: his three-sentence paragraph reads AI beside the reparenting paragraph in his own wording. The section reads 100% Human with it (276g).

## Batch 279g: section 10 wording A, and section 11's controls and other neighbors

| text | mine | why |
|---|---|---|
| E-S10P9fA | AI (weak) | this opening has failed in most wordings (s10/PREDICTIONS-s10.md, 187g to 197g); the inline example lengthens it |
| S10v3A | Human | the section passed with P9 reading AI alone (276g) |
| C-S11P12 (installed P1 and P2) | AI (weak) | P1's list of five things a founder does |
| E-S11P2f-b (P2 with the definition, and P3) | Human (weak) | |
| C-S11P23 (installed P2 and P3) | Human | |
| E-S11P6f-b (P5, P6 and the four questions) | Human (weak) | the questions run on from P5's |
| C-S11P8 (installed P8 alone) | Human | it passed alone in 207g; it read AI after the four questions then too |
