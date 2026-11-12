# Turn 41 (2026-11-12): his round-39 answer, and his message of 22:34 UTC

His round-39 export of 2026-11-12 22:34:10 UTC (`../../review/r39/ANSWERS-R39-20261112-2234.json`) and his message of the
same minute. His versions are in, whole (`../../review/r39/apply_r39.py`; his tries:
`../../experiments/t39-answers/JOEL-TRIES-TEACH-EVID.md`): the evidence paragraph (5b09da6c, Human High 137), his pointer to
the humic acid evidence after the protocol's humic acid step, and his fix of my rescue medicine paragraph (9320d4ec, Human
High 73 by itself).

From his message, two durable changes before any text of mine (lessons bad-trips-2026-11-12k and l):

- The fit read is universal (`../../../../tools/humanization/fit_read_brief.md`): it is told what the text is and who reads it,
  and asks ANYWAY, CAN'T TELL, FROM and MISREAD of every line. On twelve lines written for a gut-healing article's reader it
  marked five of six (Sonnet) and six of six (Haiku), with one wrong mark each (`FIT-CALIBRATION-2.md`).
- Nothing of mine goes in below Human High, checked by itself (`../../../../tools/humanization/apply_gate.py`, with tests);
  `apply_h51.py` calls it.

Then his seizure points ("you're right about over 5 minutes that's an epilepsy rule ... explain that they can lower seizure
threshold even with a normal dose and people with already low seizure thresholds might have seizures which are most likely
less dangerous than an actual drug overdose seizure"; "you can tell by touching someone's forehead how hot it is"). Every
draft went through the needed read, the read against his fixes and the universal fit read (`reads/`, each mark changed or
kept with its reason in `NEEDED.json`, `HIS-FIXES.json`, `FIT.json`), with its receipt (`make_receipts.py`) and prediction
(#473 to #479, `predict.py`). The reads moved the paragraph from a reason with no action ("That's most likely less
dangerous ...") to its scope first ("Waiting the 5 minutes is only for a seizure on a normal dose."), and the overdose
line to say what to do when the dose isn't known.

| test | what | result | link |
|---|---|---|---|
| explone-c5 | the paragraph after the call list, by itself: which seizure the 5 minutes is for, his reason, his comparison | Human Written, Human High 56 | [fa2258eb](https://www.pangram.com/history/fa2258eb-9f83-497d-a25c-7a1877a73608) |
| callp-c3 | the call list by itself: an overdose seizure its own line, the 5 minutes for a seizure on a normal dose, the heat line "Their forehead feels very hot (not just sweaty)." | Human Written: High 36 (the lead-in and my two lines), Medium 32 (his breathing, lips and injury lines, and my heat line) | [4d0a5d11](https://www.pangram.com/history/4d0a5d11-8a2e-49fa-8539-c6c5e87989d5) |
| callp-c4 | his heat line with my clause ("They get dangerously hot, which you can feel on their forehead (not just regular sweating).") | AI Generated, 100%: AI Low 42, Medium 21, Low 12 | [14de8a4b](https://www.pangram.com/history/14de8a4b-0a31-4cf0-9be6-db18bb676461) |
| callp-c5 | the heat line as what the reader does ("When you touch their forehead, it's very hot, not just sweaty.") | Human Written: High 36, Medium 36 | [639a15d5](https://www.pangram.com/history/639a15d5-0abf-4c09-b38d-d2637d406f80) |
| callp-c6 | his heat line exactly as he wrote it | AI Generated, 100%: AI High 36, Medium 12, High 20 | [10d05b15](https://www.pangram.com/history/10d05b15-8e9e-41bc-b4fa-ce45834ffaad) |
| seize-c10 | Active Seizure as a whole with callp-c3's list, the paragraph and his rescue paragraph | Human Written, Human High 265 in one window | [c00d2cae](https://www.pangram.com/history/c00d2cae-f984-451a-8b26-f790150280e6) |
| seize-c11 | the same with callp-c4's heat line | Human Written: High 40, Medium 4 ("- Loosen any tight clothing."), High 60, Medium 6 ("- Their breathing gets slow and shallow."), High 162 | [1d90cd9d](https://www.pangram.com/history/1d90cd9d-7014-4d9b-b19f-e49424a87f94) |

In the guide (`apply_h51.py`, through the gate): the paragraph (H51-SEIZE-WAIT) on its own Human High; the call list
(callp-c3) on his exception, since its lines are about the friend the section is about and in its section it read Human
High in one window. By itself the list kept a Medium window over its last four lines, three of them his, whatever my heat
line said, and his own heat line read AI there: the one place this turn where something of mine went in without reading
Human High by itself, said to him. The list's lineage has read AI twice, so its next try goes through the tell panel first.
The Call medics list at the top says the same seizure line the same way ("A seizure after taking too much (or an unknown
amount), or one on a normal dose lasting over 5 minutes"); that list read AI as a whole before (h42-02) and is still to
humanize.
