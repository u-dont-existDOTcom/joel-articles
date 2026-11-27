# Rules audit: find the rules that look sus

You are checking rules that an AI editor wrote for itself. The editor works on Joel's articles (long guides on his
Substack about psychedelics, therapy, health and relationships). It makes them make sense to readers and "humanizes"
them so the AI detector Pangram reads them as human-written. Almost every rule was drawn from one of Joel's corrections
or messages, and most quote him. Joel has just found that the editor sometimes draws the wrong lesson from what he says,
and he wants every rule double-checked.

Your batch: `{BATCH}`. Read all of it. Each unit starts with `[id | file]`.

## What makes a rule sus

A rule is sus when following it to the letter could make the editor do something Joel didn't ask for, doesn't want, or
that misses his point. For each rule, find what Joel actually said (his quoted words, and the case they were about) and
ask:

1. What was his point, and what reason did he give for it?
2. Does the rule's instruction carry that point and that reason, or a different one? Watch for a rule whose method is
   something that merely happened to be true of his fix or his example, when his own words give a different reason; a
   rule narrower or broader than what he said; a rule that drops a condition he gave, or adds one he didn't.
3. Applied to a new case, would the rule make the editor do what he meant? Or would it force something he'd find silly:
   a mechanical test (a word list, a word count, "every word", a fixed number, a string match) standing in for a judgment
   of meaning; an always/never made from one case; a word banned where he said it is only overused.
4. Does the rule put words in his mouth: a claim he didn't make, or his quote stretched to cover something it doesn't?
5. Does its conclusion follow from its own evidence? (A test result that shows one thing, used to justify another.)
6. Does it add steps, checks, refusals or questions to him that nobody asked for, and that would slow the work or block a
   good result? He has said slow turns frustrate him, and that he wants fewer questions on things that are clearly fine.
7. Does it conflict with another rule in the batch, or with something he says elsewhere in the batch?

Not sus: a rule that is strict or specific but follows from his words; a rule you would only phrase differently; a
reasonable tool or bookkeeping rule. Don't flag style. Be selective: flag what a careful person would want to ask Joel
about, and say nothing about the rules that are fine.

## Answer

Write your flags to `/home/claude/work/audit/out/{BATCH_NAME}.md`, one line each, most serious first:

`- ID: the rule (at most 20 words) | Joel said: "his words" (at most 30 words, quoted exactly) | why sus (at most 40
words) | it should say (at most 30 words) | high or medium`

Use the unit's id as written in its `[id | file]` line; when the unit names a lesson or gate inside (such as
`neuro-2026-11-27g` or `E301`), give that name too. If nothing in the batch is sus, write `- none`. Read only your batch
file (and, at most for three rules, the file a rule points to if you need Joel's exact words: the repository as the rules
stood is at `/home/claude/work/audit/snapshot/`, and a path in a rule is from that folder). Don't open anything else, and
change no file but your answer. Be brief. Your final message: the number of flags and their ids, nothing else.
