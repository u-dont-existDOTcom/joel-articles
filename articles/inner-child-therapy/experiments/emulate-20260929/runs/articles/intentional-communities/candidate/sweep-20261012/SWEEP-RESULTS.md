# Sweep of the article for the breaks Joel found in section 12 (2026-10-12)

Joel, 05:33 UTC: "p3 got b roken ... then you broke p7 ... p16 also broke the meaning ... debug the error so it doesn't happen again". The gate's correction rule asks for a sweep of the article for the same problem ("Every correction teaches the system", `docs/HUMANIZATION-GATE.md`).

**How.** Eight fresh Sonnet agents, each given a section or a few, published and rewritten, and only the three kinds of break (`PROMPT-G1.txt` to `PROMPT-G8.txt`; inputs `in-G*.md`; reports `sweep-G*.md`): a pronoun or vaguer word where the published sentence names something, a narrower thing in place of a general one, and a dropped word that sets a claim's standard or says how long it holds. Sections 1 to 11 as installed, and section 12 v10c. Sections 13 to 17 are still the published text.

**What it found: 18 places.** 14 are in Joel's own paragraphs, where the change is his (his rewrites and rulings, in `OWNER-EDITS.json` or his texts in the section folders), and several are his deliberate corrections of the published text (section 3's "people who've done the healing first": "he does want people to come in largely healed"). Those stay as he wrote them. 4 are in my text:

| Section | Published | Mine | Kind | Disposition |
|---|---|---|---|---|
| 12, P13 | "equipment repaired" | "fix the cars" | narrower | **fixed**: "fix whatever breaks" (v10f; 263g, 265g) |
| 12, P22 | "instead of converting every limit into rejection" | "not flat-out rejecting people who fall into these categories" | narrower | **fixed**: "... who fall into these categories, or anyone else it can't take right now" (v10f; 265g). "Every time it hits a limit" passed with L4 but took the section to 45% AI |
| 11, P5 | "If every adaptation still needs the founder's approval" | "If it needs the founder's “blessing”" | pronoun; "every" and "still" dropped | **fixed**: "If every change they make still needs the founder's “blessing”" (v13; the section 100% Human, 267g; with P4 100% Human, 268g). Three other wordings brought an AI window onto P4 (264g to 267g) |
| 4, Relational pl/ork P6 | "whether the founding document acknowledges romance or pretends everybody has transcended it" | "no matter how much your founding document says that you're all beyond romance" | narrower (one case of two) | **kept**: "no matter how much" covers both cases, so a reader still takes away that dyads happen whatever the document says. Section 4's trace (TRACE-v6-A) had marked the same phrase for "pretends" becoming "says"; Joel reviewed section 4 after that (his edits of 21:16 and 23:49) |

Joel's paragraphs the sweep flagged, for the record (no change): section 1 "a highly structured political system" (`s1-rulings`); section 2 "leeching off the group", "developing healthier forms of relationships", "stop trying to act helpless" (`s2-c10`, `s2-c10-fix`), "the old way of living", "the group runs out of money, a baby is born" (`s2-c11b`); section 3 "people who've done the healing first" (`s3-p9`); section 4 "And it's built on somatic regulation first." (`s4-p12`); section 8 "if they are known to be honest", "may get mixed up telling what happened", "hopefully including non-intrusive help from outside", "Kids in or outside of intentional communities" (his texts of 2026-10-07 15:05, `s8/joel-1505/`); section 11 "nobody has to take medicine to have equal respect", "when communal therapy processes are pre-reqs" (his rewrite of 2026-10-11 18:35, `s11/joel-1835/`).

Sections 5, 6, 7, 9 and 10: no findings.
