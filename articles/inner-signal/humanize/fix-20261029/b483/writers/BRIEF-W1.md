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
(none yet)

## What else reads AI to Pangram 4.1 (avoid it)
- Wry quips, joke similes and punchlines; aphorisms and balanced closers that wrap a thought up; tidy follow-ups that
  restate, sum up or reassure.
- Definitions and explanations in a textbook shape ("X means A and then B"); parallel pairs and "not X, but Y"
  contrasts; colon reveals and signposting.
- Lists of abstract nouns, especially in threes; lists of options strung with "or" in one breath.
- Generic "you"/"imagine" scenarios; stock words (journey, profound, navigate, delve, crucial, genuinely, truly).

## What to return
Write your answer with a single Write call to `/home/claude/joel-articles/articles/inner-signal/humanize/fix-20261029/b483/writers/VERSIONS-W1.json`, as JSON:

{"<item id>": {"v1": "<the replacement for all the flagged sentences of the item, in order>",
                 "v2": "<a second replacement, different in shape from v1>",
                 "keeps": "<one line: the points of the flagged sentences, and where each is in v1 and v2>"}, ...}

Each replacement replaces the flagged sentences as one stretch (they are next to each other in the paragraph, in the
order given), so it can be one sentence or several. Read only `/home/claude/joel-articles/articles/inner-signal/humanize/fix-20261029/b483/TARGETS.json` (your items are listed under "W1"); don't run
commands or use the web. Reply with only "DONE: <number of items>".
