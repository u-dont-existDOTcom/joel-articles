# Turn 132: which model gets closest to his contents

Made by `score_t132.py` from the files beside it; run it again to check every number.

## Order: outlines against his own reorganization of 4 to 14 November

His version re-parents 20 of the 148 units and changes the level of 15. "His moves" counts the units an outline gives his new parent; "other moves" the units it re-parents that he left alone; tau is Kendall's tau against his order; "in his place" counts units with his parent and his preceding unit.

| Outline | His moves (of 20) | Other moves | His level changes (of 15) | Other level changes | Tau | In his place (of 148) |
|---|---|---|---|---|---|---|
| 4 November order, unchanged | 0 | 0 | 0 | 0 | 0.923 | 98 |
| FABLE-plain-1 | 2 | 9 | 0 | 14 | 0.929 | 88 |
| FABLE-plain-2 | 2 | 8 | 0 | 11 | 0.930 | 90 |
| FABLE-rules-1 | 1 | 6 | 0 | 10 | 0.847 | 89 |
| FABLE-rules-2 | 3 | 13 | 0 | 12 | 0.915 | 73 |
| FABLE-rules2-1 | 3 | 11 | 0 | 17 | 0.909 | 83 |
| GPT-gpt-plain-1-OUTLINE | 2 | 20 | 1 | 14 | 0.725 | 73 |
| GPT-gpt-plain-2-OUTLINE | 3 | 21 | 0 | 32 | 0.826 | 78 |
| GPT-gpt-rules-1-OUTLINE | 9 | 16 | 5 | 15 | 0.814 | 67 |
| GPT-gpt-rules-2-OUTLINE | 8 | 23 | 9 | 27 | 0.825 | 69 |
| HAIKU-plain-1 | 3 | 24 | 0 | 35 | 0.922 | 79 |
| HAIKU-plain-2 | 2 | 20 | 1 | 21 | 0.918 | 81 |
| HAIKU-rules-1 | 2 | 13 | 0 | 12 | 0.895 | 83 |
| OPUS-plain-1 | 2 | 5 | 0 | 14 | 0.923 | 93 |
| OPUS-plain-2 | 0 | 3 | 0 | 7 | 0.921 | 95 |
| OPUS-rules-1 | 2 | 6 | 0 | 4 | 0.912 | 89 |
| OPUS-rules-2 | 2 | 4 | 2 | 4 | 0.926 | 96 |
| SONNET-plain-1 | 3 | 12 | 1 | 8 | 0.902 | 84 |
| SONNET-plain-2 | 1 | 6 | 0 | 15 | 0.921 | 90 |
| SONNET-rules-1 | 2 | 10 | 2 | 16 | 0.928 | 93 |
| SONNET-rules-2 | 1 | 8 | 0 | 8 | 0.915 | 90 |
| SONNET-rules2-1 | 4 | 14 | 1 | 17 | 0.888 | 83 |

"plain" outlines had only the task; "rules" had RULES-ORGANIZE.md (v1), "rules2" RULES-ORGANIZE-2.md (v2).
GPT-gpt-* came from his laptop.

**What it shows.** No model, with or without either version of the rules, comes near his order. The best tau (Fable, no rules, 0.930) barely beats leaving the 4 November order alone (0.923), and the outlines closest to his order make almost none of his moves. The GPT outlines with rules v1 make the most of his moves (9 and 8 of 20) and also the most moves he didn't make (16 and 23). Rules v2, the four-pass version, did not help any model. A model's reorganization of his article is a proposal to put to him move by move, never a reorganization.

## Headings: fresh runs with RULES-HEADINGS.md against his picks

| Run | Exact (of 147) | Exact ignoring case | Judge: same | Judge: close | Judge: different |
|---|---|---|---|---|---|
| SONNET-1 | 73 | 81 | 84 | 45 | 18 |
| FABLE-1 | 73 | 80 | 85 | 49 | 13 |
| GPT-1 | 59 | 61 | 65 | 64 | 18 |

The judge (a Sonnet reader, blind to which run wrote what) called a candidate "same" when it differs from his heading at most in capitals, punctuation or an article, "close" when a reader would expect the same section, and "different" otherwise. The earlier counts in HANDOFF.md (Opus t130 132, Fable t131 121, and so on) were the lists he picked from, so they are not comparable with these.

**What it shows.** Fable with the heading rules came closest: the same or close on 134 of 147, different on 13.

Where all three runs missed his meaning (the judge said "different" for each):

- S010: his "“No. I Hate Myself.”"; the runs: "The Part That Came Here"; "The Part That Came Here"; "Notice What Brought You"
- S092: his "Altered States"; the runs: "Altered States, Intensives"; "Altered States & Intensives"; "Altered States & Intense Work"
- S095: his "Attacked by a Demon?"; the runs: "Prepare for Altered States"; "Prepare for Altered States"; "Prepare for Altered States"
- S096: his "Spirit Attacks Teach Love"; the runs: "Spiritual Attack as Gain"; "Gain from Spiritual Attack"; "Grow Through Spirit Attack"
- S139: his "If They Can’t Hear You"; the runs: "Others Have Hooks Too"; "Other Folks Have Hooks"; "Others Have Hooks Too"
