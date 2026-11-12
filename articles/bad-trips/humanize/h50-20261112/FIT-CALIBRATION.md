# The fit read, scored before use (turn 40, 2026-11-12)

Joel, 2026-11-12 19:44 UTC, after cutting "It's their first seizure" ("that's what we are expecting if the overdose causes
a seizure"), "Another seizure starts before they've recovered from the last one" ("how would someone know") and "Check if
their vision has changed" ("they are tripping, their vision should change") from texts every fresh read had passed: "we
need to have a better sense check in general."

The read (`tools/humanization/fit_read_brief.md`) asks of every line that says what to look for or do: is it true anyway
of someone tripping or overdosing; could a friend tell; is it a rule from another setting. Scored on a list of twelve
lines none of his fixes had touched (`fit/fit-heldout.txt`), with the flags I expected written down first:

- should be marked: very dilated pupils, a pounding heart, seeing things, not knowing the year or the president, an
  irregular pulse (a friend can't reliably tell), vomiting more than twice, trouble standing up straight;
- should pass: the lead-in, can't be woken up, a temperature that keeps climbing after cooling, blue or gray lips, one
  side of the face drooping.

| reader | marked of the seven | passed of the five |
|---|---|---|
| Sonnet (`fit/ans-sonnet.txt`) | 7 | 4: it marked the drooping face as "a stroke-clinic sign" |
| Haiku (`fit/ans-haiku.txt`) | 6 (missed the pulse) | 5, but it answered "TELL yes" for lines a friend can tell, the question read backwards |

So the read catches the kind of line he cut (true anyway of someone tripping), on lines it has never seen. Two wording
fixes before use: the second question is now "CAN'T TELL", so a "yes" always marks a problem, and the third says that a
danger sign which holds everywhere fits. It is a gate from now on (`sense_receipt.py`'s "fit" field, gate
bad-trips-2026-11-12j), read by a Sonnet agent.
