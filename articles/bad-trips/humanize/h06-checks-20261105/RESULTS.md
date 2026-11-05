# Batch h06 (2026-11-05): round 6's paragraphs, in Joel's Pangram account

Run by the lane in the desktop app's browser pane (his account, signed in), each text by itself, its SHA-256 checked
before the click and read back from his history by SHA-256; predictions first in `../pangram-ledger.jsonl` (#18 to #25).

| text | what it is | result | windows | prediction |
|---|---|---|---|---|
| bt-r06-aura-his | N-AURA, his warning-stage paragraph (with his humic/fulvic hunch) | [Human Written, 0%](https://www.pangram.com/history/d442fc16-7a35-4750-827b-a38c2896b1e3) | High 135 | Human 0.70, right |
| bt-b111-nofocal | B111 with its focal sentence out (card Y-C) | [Human Written, 0%](https://www.pangram.com/history/5d3d05f7-30aa-4aef-b6cf-08deb2f4bd96) | High 83 | Human 0.70, right |
| bt-r06-canna-his | N-CANNA, his cannabis-at-an-aura and ABRACE paragraph | [Human Written, 0%](https://www.pangram.com/history/4abd4875-3777-4922-938c-404ddb6d6989) | High 99 | Human 0.60, right |
| bt-r06-gel-his | N-CBD-2, his skin-gel paragraph with the authors' reason corrected (card Y-B) | [Human Written, 0%](https://www.pangram.com/history/aa293ceb-d603-4fe1-9007-2ddc9c6a72bb) | High 88 | Human 0.55, right |
| bt-r06-forums-his | N-FORUMS, his version | [AI Detected, 62%](https://www.pangram.com/history/2419edef-dd6d-4c05-9ed3-32bf737bef33) | Human Low 31; AI Medium 38; AI Low 11 | AI 0.40, right |
| bt-r06-forums-2 | try 2: the making-sense read (what's smoked and when; the EEG woman as a study) | [AI Detected, 43%](https://www.pangram.com/history/fd1df50a-5f61-44ee-ad14-ab61bda0542c) | Human Medium 37; Human Low 12; AI Low 11; AI Low 29 | Human 0.50, miss (explained: the ending's own flaw of sense) |
| bt-r06-forums-3 | try 3: the tell panel's notes as rewording (panel-F2/PANEL.md) | [AI Detected, 98%](https://www.pangram.com/history/d3ff8463-b3c1-40f3-8852-d81cedc403ed) | AI Low 37; AI Low 56 | Human 0.50, miss (explained: rewording without a sense fix) |
| bt-r06-forums-4 | try 4: try 2 with the ending's logic fixed ("So it may come down to how much THC is in it") | [AI Detected, 41%](https://www.pangram.com/history/bbaa0976-fd6a-4cdb-bcb0-207e5e9d1265) | Human Low 49; AI Low 37 | AI 0.40, right |

Try 4 is in the guide (`put_forums_try4.py`) and goes to him on round 7's page (FORUMS-EDIT). Six of eight calls right.
His four links from the neuro lane and his three from round 6 (MOVE-YOURS) were read back from his history in the same
session: each text's SHA-256 matches what he sent (`../../review/r06/HIS-CHECKS-READ-20261105.json`).
