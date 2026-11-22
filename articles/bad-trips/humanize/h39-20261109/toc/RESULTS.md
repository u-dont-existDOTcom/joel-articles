# The table of contents, read alone (2026-11-09, turn 30)

His answer on round 28's helper card (2026-11-09 17:22 UTC): "idk i'm thinking maybe it would hlep if you look only at
the ToC first, have you tried that? make sure the ToC is optimized then we can make sure the stuff in each section is
what belongs there rather than merging or moving?" (lesson bad-trips-2026-11-09e).

## How it was read

A tree test: fresh readers got only the contents (each heading at its level, with its word count, [TOC-NOW.md](TOC-NOW.md)),
the brief ([BRIEF.md](BRIEF.md)) and 16 situations a reader comes with ([SITUATIONS.md](SITUATIONS.md)), and said for each
where they'd look first and whether they were sure. The sections each situation should find are in
[EXPECTED.json](EXPECTED.json), which the readers didn't see. Two readers read the contents as it is (a Sonnet agent,
[READ-NOW-1.md](reads/READ-NOW-1.md); an Opus agent, [READ-NOW-2.md](reads/READ-NOW-2.md)), and each proposed the
contents it would want. A third, fresh Sonnet agent read option A ([TOC-A.md](TOC-A.md),
[READ-A-1.md](reads/READ-A-1.md)) the same way.

| | Guesses (of 16) | First pick right | Notes |
|---|---|---|---|
| As it is, reader 1 | 6 (1, 11, 12, 13, 14, 15) | 15; for 14 ("might hurt themselves or someone else") "Call medics for:" | would stop at beach morning glory for "end the trip now" |
| As it is, reader 2 | 5 (1, 11, 12, 14, 15) | 15; for 14 "Bring in mental-health support when:" | "I'd have stopped at Beach Morning Glory and missed niacin" |
| Option A, reader 3 | 4 (11, 12, 13, 14) | 16 | niacin now in the same group as beach morning glory |

## What both readers found on their own

- Every remedy group sits under "How I label the evidence", an 85-word legend, so the remedies are four levels deep and
  look like part of the evidence key.
- "My Acute Rescue Hierarchy" reads like more of "Acute Medical and Neurological Rescue".
- "Some Remedies Require More Caution" comes after every remedy, so a reader picks one before seeing the caution.
- The two ways to end a trip are split ("When the Goal Is to Stop a Psychedelic Trip" and "A Final Trip Killer"), with
  the stabilizers between them.
- Who to call and when is split between the top part and "Who to Contact, and When", under Get One Human Anchor.

Reader 1 also moved the Grounding Menu next to first aid and put the euphoria section next to The Other Bypass; reader 2
split the psychological part into "Tripsitting Yourself or Others" and "Shadow Work", put the hard content before the
reflective sections, made After the Storm a part of its own, moved the brain section to the end of the medical part, and
moved DMSO next to humic acid.

## The options on round 30's TOC card

[plan_toc.py](https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/bad-trips-20261105/articles/bad-trips/humanize/h39-20261109/toc/plan_toc.py) makes each one from the guide's blocks, moving whole sections and changing heading levels only, and checks
that no block is lost or doubled ("A Final Trip Killer" is joined to the niacin heading).

- **A (my pick):** the five fixes both readers found; the emergencies first in the medical part, the brain section last,
  leading into the remedies; DMSO next to humic acid; the psychological part split, in his words, into "Tripsitting
  Yourself or Others" (his greeting still opens it, keep-as-is K1) and "Shadow Work", the hard content before the
  reflective sections; the Grounding Menu next to first aid; After the Storm a part of its own, with "Bring in
  mental-health support when:" right after the aftermath list (his AFT-HOW-MUCH answer: "if it were right after this
  section it would be an easy choice") and the healing treadmill after it; Give the Session a part of its own at the end.
  The guide in A's order, [GUIDE-TOC-A.md](GUIDE-TOC-A.md), passes the fidelity keys (R28), his edits (64 pass) and the
  keep-as-is list, and [tools/humanization/section_refs.py](https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/bad-trips-20261105/tools/humanization/section_refs.py) finds no pointer that turns wrong (11 mentions of sections); its "above" and
  "below" lines all still point the right way.
- **B:** only the five fixes both readers found.
- **C:** as it is.

What A leaves: three headings still make a fresh reader guess. "Give the Session a Beginning and an End" doesn't say it's
for planning, "Hang up the phone" says nothing until the section is read, and harm is answered in three places (the top
part, the helper's "When the Content Turns Toward Harm" and the call-medics list). Renaming them is a later card, if he
wants it. Not taken from the readers: moving "When the Content Turns Toward Harm" to the top (it's how the helper handles
the talk itself, and the top part already says when to get urgent help for harm), and renaming "Do" and "Who to Contact".

## His answer, and the contents as it went in (2026-11-09 18:43 UTC)

"a sure rename them so readers can find them, and brain should be at top yeah that's kind of one of the most common
things people say." So option A went in with the brain section first, and the three headings readers had to guess at
renamed, his words kept with a lead a reader would look for: "Risk of Harm: When Peer Support Isn't Enough", "When What
They Say Turns Toward Harm", "Trip After Trip? Hang up the phone, get off the Healing Treadmill" and "Planning a Trip or
Ceremony? Give It a Beginning and an End" ([plan_toc.py](plan_toc.py) A --apply, run by [review/r30/apply_r30.py](https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/bad-trips-20261105/articles/bad-trips/review/r30/apply_r30.py)). A fourth
fresh reader read the renamed contents ([TOC-A2.md](TOC-A2.md), [READ-A2-1.md](reads/READ-A2-1.md)): 3 guesses (1, 11,
14), every first pick right; planning a ceremony and "ceremony after ceremony" became sure.

| | Guesses (of 16) | First pick right |
|---|---|---|
| As it was, reader 1 | 6 | 15 |
| As it was, reader 2 | 5 | 15 |
| Option A, reader 3 | 4 | 16 |
| A as he chose it, renamed, reader 4 | 3 | 16 |

The guesses left: shaking and not responding (a seizure or serotonin syndrome, which the medics list covers either
way), a week later the world feels unreal (the aftermath list or the support section, now next to each other), and harm
(the top part or the helper's section, now named for what each covers).
