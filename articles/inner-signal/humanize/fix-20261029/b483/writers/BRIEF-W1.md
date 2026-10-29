# Batch 483: the next try at sentences that read AI (writer W1)

You are writing for Joel, a Substack writer, in his self-hypnosis guide ("The Inner Signal"). The guide was rewritten so
that Pangram, an AI-text detector (version 4.1), reads it as human-written. The flagged sentences below read AI in its
check, and so did the new version another writer made of each in the last round: that version is shown, with how it
read. Your job: for each item, write **two new versions of only the flagged sentences**, saying exactly what they say now,
just as clearly, in Joel's voice, in shapes that don't read AI.

Joel's rule, which outranks the detector: "we never publish nonsense because it passes pangram." A version a reader can't
follow on a first read, or that drops or changes a point, is worthless however human it sounds.

**Item J5 is Joel's own sentence** (he wrote it on 28 October). Nothing goes in without him: your versions are
suggestions he will see beside his own words. Stay as close to his words as the job allows (keep his four factors, in his
words), and change only what most likely reads AI: here, most likely the colon and the list in one breath. Item J5 has no
last try: his sentence itself read AI (Low) twice.

## What each new version must do
- Say everything the flagged sentences say now: every point, step, condition, contrast and example, with the same
  strength. The current wording is clear and was read beside Joel's published version (shown as PUBLISHED, the meaning
  reference; its wording is the AI-written original, so don't copy its phrasing).
- Be clear on a first read to someone who only sees the new paragraph.
- Fit the paragraph: the sentences around it stay as they are, so no repeating them, and no "it"/"this" without
  something to point to.
- Keep his terms exactly: the inner adult's three jobs are the Nurturer, the Protector and the Guide; a protective part
  from childhood is a guard; the inner child is also "your little one"; "borrowed adulthood" is his term. American
  spelling.
- Add nothing: no new claim, example, warning, safety line or reassurance.

## What read AI last time (don't repeat these shapes)
Each item shows the last round's version (LAST TRY) and how it read in place. Several were casual rewrites of the same
length and order as the sentence they replaced: "Stick to the one thing you're doing, with one anchor or image to get
started and one way to come back. You can also set yourself a tone if you want one, maybe warm or bounded or directed or
neutral witnessing, or whatever else." read AI at High, and so did the untouched sentences around it. A casual word or
"maybe ... or whatever" on top of the same shape doesn't change how it reads. Change the shape.

## Shape rules from the rewrites that passed
These come from 98 of Emulate's rewrites of this guide beside the sentences they replaced, with their Pangram readings
(`../emulate-lessons/LESSONS.md`), and from the last round. In the last round, where the writer kept the same number of
sentences, 9 of 12 versions read Human; where the writer split into more sentences, 2 of 9 did.

- **Keep the number of sentences, or join two; don't split.** A stretch of one sentence stays one sentence. Two short
  sentences that belong together can become one. Splitting into shorter, tidier sentences is the single most common
  thing that read AI last round.
- **Chain steps in one spoken sentence**, joined by commas, "and" or "then", the way a person says them out loud. A run of
  one-command sentences reads AI however plain each one is.
- **Let a sentence run long** when it carries a condition, a step and a reason together, beside a short one. "Plain"
  means easy to follow, not short.
- **Keep a list inside its sentence**: in brackets, after a dash, or as things the reader may want to do, and an open list
  can end on a rough "or something like that". Never one- or two-word sentences, and never options strung on "or ... or
  ... or".
- **Where the text frames a test** ("the useful question is whether ..."), ask the reader that question directly, once. No
  runs of questions, and no question the next sentence answers.
- **Break runs.** Three or more sentences of the same shape read AI whatever words fill them: make them unequal in length
  and build, or fold two into one.
- **Don't give a "you don't have to" / "no need to" permission its own sentence or clause.** Fold it into the step it
  qualifies ("Instead of X, try Y", "just rest your hands there without faking anything").
- **When a published point has to stay** (a definition, a list, a caveat), say it in the paragraph's own shape, never as
  the published sentence with its colon, definition shape or closing line.
- **No new idioms, similes or wrap-up lines** to make it sound casual. Casual words on top of the same shape don't
  change how it reads.
- **When you join or loosen a sentence, carry every small qualifier across** ("only", "first", "even then",
  "automatically", "before"): looser rewrites drop exactly these, and a dropped qualifier changes the meaning.
- **Saying an item in full is fine** (it isn't a new example), and repeating a noun or verb where a person talking would
  is fine, as long as it stays clear on a first read.

## What else reads AI to Pangram 4.1 (avoid it)
- Wry quips, joke similes and punchlines; aphorisms and balanced closers that wrap a thought up; tidy follow-ups that
  restate, sum up or reassure.
- Definitions and explanations in a textbook shape ("X means A and then B"); parallel pairs and "not X, but Y"
  contrasts; colon reveals and signposting; a label and a colon before each step.
- Lists of abstract nouns, especially in threes; options strung with "or" in one breath; fragment lists.
- Generic "you"/"imagine" scenarios; stock words (journey, profound, navigate, delve, crucial, genuinely, truly).

## The hardest items (nobody has a version of these that reads Human yet)
- **T2** is an outcome list. Keep all five outcomes; one long spoken sentence (or two, not more) that says them as what you notice in yourself and your days, not a colon list or an "or ... or" string.
- **T7** is a free-standing definition. Keep what fractionation is and what doing it openly teaches; say it as what you do when you add it (one or two sentences, chained), not "Fractionation means" or "In fractionation".


## What to return
Write your answer with a single Write call to `/home/claude/joel-articles/articles/inner-signal/humanize/fix-20261029/b483/writers/VERSIONS-W1.json`, as JSON:

{"<item id>": {"v1": "<the replacement for all the flagged sentences of the item, in order>",
                 "v2": "<a second replacement, different in shape from v1>",
                 "keeps": "<one line: the points of the flagged sentences, and where each is in v1 and v2>"}, ...}

Each replacement replaces the flagged sentences as one stretch (they are next to each other in the paragraph, in the
order given), so it can be one sentence or several. Read only `/home/claude/joel-articles/articles/inner-signal/humanize/fix-20261029/b483/TARGETS.json` (your items are listed under "W1"); don't run
commands or use the web. Reply with only "DONE: <number of items>".
