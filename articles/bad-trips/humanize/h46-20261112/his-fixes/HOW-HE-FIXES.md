# How my drafts differ from Joel's fixes (2026-11-12)

His question, round 36 (2026-11-12 14:45 UTC): "have you systematically looked at all of the fixes i've shown you and what
are the idfferences in how you write vs how i fix? because when i look at how you try to implement my fixes, it's
laughable, like you're not really learning much. you still use a lot of ai patterns like "this is different. that's
different, this other thing is also different" and "x but not y" and so forth".

## What was read

Every fix he sent on a review page in this repository: 112 pairs, each his version against the model text the card
showed (the article's drafted words, or a fix of mine), in six lanes (bad trips, Inner Signal, inner child, neuro
de-armoring, romance, communities; `collect.py`, `PAIRS.json`), plus his eight tries in the bad-trips teaching series read
from his Pangram history (`SERIES.json`), each a step with its reading. I read the 14 bad-trips fixes and the eight tries
myself; four fresh readers read the other 98 against one list of change types (`BRIEF.md`), each quoting the change
(`ANNOT-*.json`; every diff in `DIFFS.md`). The table is computed by `summarize.py`.

## What he changes, counted

| what he changed | in how many of the 112 fixes | the biggest change in |
|---|---|---|
| A referent made exact: who, to what, what counts ("hurt somebody" to "hurt themselves") | 67 | 15 |
| Something added that the reader needed (a missing step, case, reason or fact) | 66 | 27 |
| A spoken register: contractions, "for that matter", "go ahead and", "So" | 55 | 6 |
| Something cut as unneeded or said twice | 48 | 11 |
| Other (word choice, punctuation, joins, order) | 46 | 7 |
| A term explained right where it is used, or the plain word for jargon | 44 | 3 |
| His own stance, story or example added | 41 | 10 |
| A list unpacked: each item its own clause, with what happens or what to do | 20 | 11 |
| A quip, aphorism, thesis or summing-up line cut, or replaced by the thing to do | 18 | 5 |
| A correction or contrast frame removed ("does not mean X; it means Y", "rather than", "not X but Y") | 18 | 4 |
| The reader made the one who acts or thinks | 18 | 1 |
| A hedge or slack added ("maybe don't", "you can still change your mind") | 17 | 0 |
| Bare commands joined to their reason ("They're feeling overwhelmed, so dim the lights") | 16 | 6 |
| A repeated sentence shape broken: items built different ways, with different connectors | 10 | 5 |
| Normal versus danger said, with its limit ("not just regular sweating", "up to a point") | 9 | 1 |

Counting the surface patterns alone (`analyze.py`, `COUNTS.md`) shows little: his versions have about as many lists,
questions and hedges as the texts they replace. What he changes is what each sentence says and how it is built.

## What flipped Pangram, in his words

From his comments on those fixes, each the one change he says moved the reading:

- "the one thing that flipped it was adding "remedy" to "adjunct" since adjunct is not really clear what it's adjuncting for" (bad trips, round 5)
- "now i made it have a payoff at the start and that flipped human" (bad trips, round 8)
- "i put "or false" into parentthesis so it's less perfectly balanced, and makes more sense also, that flipped the first part human" (bad trips, round 22)
- "i flipped the whole thing high conf human by interrupting the instruction manual style to give agency to the reader", then "i took out "i'm betting it will say" and it's still high conf human, so all it needed was giving reader agency" (bad trips, round 22)
- "changed "one" to "an" and that part went from high conf ai to med conf ai" (bad trips, round 22)
- "i fixed the vague repetitive "different from is different from" phrasing, now it's is human", then "changed comma to and" ("Slow, shallow" to "Slow and shallow"), High (bad trips, round 35)
- "explaining closer to the term and clarifying what counts as a pattern, as well as varying the phrasing used a bit", then "Clinicians often use the Hunter criteria" to "We can use the same Hunter criteria that clinicians use", all High (bad trips, round 36)
- "expanding the listicle moved it to human high conf ... the listicle was the only thing pangram really demanded to be fixed" (Inner Signal, E-406)
- "i had to uncompress all the lists and add explanation -- that flipped the first and second half human individually, but the only way to get the whole thing to pass was to add that bridge to break up the list" (Inner Signal, R-audit)
- "the only change i needed to flip the low conf human all to high conf was to merge the sentences with a ", but"" (neuro de-armoring, Y-83b)
- "you were overcompleting, repeating yourself on the last line, i cut that and now it's all good" (neuro de-armoring, Y-85)
- "i added an exclamation mark where it needed to be after that crazy story and now it's high conf human" (neuro de-armoring, Y-93)
- "notice this is also the only version with a real useful ending" (Inner Signal, E-315)

None of those is an opinion of his. His stance and stories are in 41 of the fixes, and this round he said they're extra:
taking his "i'm betting it will say" back out kept the aftermath list Human, High (his comment above).

## How I write, and how he fixes it

Each with a sentence of mine from the carries that read AI (h44, h45) and what he does instead.

1. **I compress; he unpacks.** Mine: "Slow, shallow breathing (respiratory depression) is a different problem from a racing
   stimulant high, and both are different from serotonin toxicity, a seizure, dangerous overheating, etc., so each gets
   its own remedy." His: "are they suffering from slow and shallow breathing (respiratory depression, from opioids, benzos
   and alcohol)? Or is it rapid breathing, heart rate, and agitation, signs of stimulant toxicity?" Each state is its own
   clause, with the signs that show it and where it comes from.
2. **I build every item the same way; he builds each one differently.** Mine: five questions, each ending on its term in
   brackets ("... (spontaneous clonus)? ... (inducible clonus) ...? ... (ocular clonus) ...? ... (tremor and
   hyperreflexia)? ... (hypertonia and fever)?"); "is a different problem from ..., and both are different from ...". His:
   "would be one full pattern", "would be counted as one pattern altogether", "another pattern together", "Another is ...
   along with ...", "Lastly, ... as well as ...".
3. **I correct and contrast; he says the thing.** Mine: "severely altered but physically stable"; "Don't wait to see every
   one of these before you act, though."; the guide's "a recognition aid rather than a command to wait for every
   criterion". His: "So if you see any of these patterns, call medics."; "I might feel in the moment like you're damaged
   for good ... But more likely factors include ...".
4. **I leave who, what and what counts vague; he makes them exact.** The most common change, in 67 of 112. "hurt
   somebody" to "hurt themselves"; "water" to "pools of water"; "adjunct" to "adjunct remedy"; "One or more of the
   following patterns" to each pattern "counted as one pattern altogether", so the reader knows inducible clonus alone
   doesn't count.
5. **I open on the rule or the authority; he opens on what the reader gets, with the reader in it.** "Clinicians often use
   the Hunter criteria" to "We can use the same Hunter criteria that clinicians use"; "Get urgent help when somebody may
   harm themselves" to "the moment you think they might hurt themselves or anybody else, get urgent help"; "Dim the lights.
   Lower the sound." to "They're feeling overwhelmed, so dim the lights".
6. **I end on a summing-up or a line that sounds wise; he ends on what to do, or cuts it.** Mine: "If all of that's true,
   calming and stabilizing the trip may be enough."; "An emergency means act now". His endings: "call medics", "reach
   out", "you can still change your mind the next day".
7. **I keep what's true and useless, and miss what the reader needs.** Mine: "because that word alone doesn't tell you
   much"; the 7-OH-CBD point ("there's NO PAYOFF"). His: "Slow breathing is normal with iboga, but if cardiac
   irregularities come along with it, that's an extra danger sign."
8. **My joins and words are a model's.** Two short sentences where he joins with ", but" or "so"; a comma pair where he
   writes "and"; "one" for "a"; "kid"; no exclamation where a person would put one.

My carries copied what his fixes look like (the questions, the brackets) into sentences that kept 1, 2, 3, 5 and 6. All
eight read AI.

## What changes in how I work

- The linter fails, in my sentences: a correction frame outside brackets (O65) and "different" said twice in a paragraph
  (O66), the two patterns he named.
- Before any Pangram check of a text of mine, a fresh reader given these eight differences with his before and after
  (`tools/humanization/his_fixes_brief.md`) marks every sentence that still shows one; `sense_receipt.py` refuses the
  receipt until each marked sentence is changed, or says why it stays.
- `SKILL.md`, "Writing for Pangram", points here.

## The first texts written this way

Chest Pain and Injury's branch paragraph and My Brain Feels Damaged's checks, each read against these differences three
times and changed after every read (`../HIS-FIXES-READ.md`), both read AI Generated, 100%, with more Medium and Low
windows than my earlier carries ([2f1b6aa2](https://www.pangram.com/history/2f1b6aa2-e672-4b5f-aeb4-6479ccf56025),
[0eeefa6e](https://www.pangram.com/history/0eeefa6e-c72f-4ea6-b74e-fab541aca12f); `../RESULTS.md`). The reads fixed what
the texts say; they did not make Pangram read my words as his.

