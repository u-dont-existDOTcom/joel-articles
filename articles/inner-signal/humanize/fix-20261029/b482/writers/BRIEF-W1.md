# Batch 482: new versions of sentences that read AI (writer W1)

You are writing for Joel, a Substack writer, in his self-hypnosis guide ("The Inner Signal"). The guide was rewritten so
that Pangram, an AI-text detector, reads it as human-written. In its newest check (version 4.1) the sentences below read
AI. Your job: for each item, write **two new versions of only the flagged sentences**, so that they say exactly what they
say now, just as clearly, in Joel's voice, without the patterns that read AI.

Joel's rule, which outranks the detector: "we never publish nonsense because it passes pangram." A version a reader can't
follow on a first read, or that drops or changes a point, is worthless however human it sounds.

## What each new version must do
- Say everything the flagged sentences say now: every point, step, condition, contrast and example, with the same
  strength. The current wording already passed a careful read beside Joel's published version (shown as PUBLISHED, which
  is the meaning reference: it says what the passage is for, but its wording is the AI-written original, so don't copy
  its phrasing).
- Be clear on a first read to someone who only sees the new paragraph.
- Fit the paragraph: the sentences before and after stay as they are, so no repeating them, and no "it"/"this" without
  something to point to.
- Keep his terms exactly: the inner adult's three jobs are the Nurturer, the Protector and the Guide; a protective part
  from childhood is a guard; the inner child is also "your little one"; "borrowed adulthood" is his term. American
  spelling.
- Add nothing: no new claim, example, warning, safety line or reassurance.

## What reads AI to Pangram 4.1 (avoid it)
- Wry quips, joke similes and punchlines ("a tiny wellness trade show"); aphorisms and balanced closers that wrap a
  thought up ("trance has a door in both directions"); tidy follow-ups that restate, sum up or reassure.
- Definitions and explanations in a textbook shape ("X means A and then B", "X places A inside B"); parallel pairs and
  "not X, but Y" contrasts; colon reveals and signposting ("one advantage ...: immediate dialogue").
- Lists of abstract nouns, especially in threes ("kinder behavior, more humility, better judgment"); say it about people
  and what they do instead.
- Generic "you"/"imagine" scenarios; stock words (journey, profound, navigate, delve, crucial, genuinely, truly).

What reads human: plain sentences of uneven length, his particulars, a reason or a doubt in his own words, casual
first-person asides ("I", "honestly", "for me") where the paragraph already speaks that way, concrete actions. The
document's own voice is casual and direct (see the paragraphs around each item).

## What to return
Write your answer with a single Write call to `/home/claude/joel-articles/articles/inner-signal/humanize/fix-20261029/b482/writers/VERSIONS-W1.json`, as JSON:

{"<item id>": {"v1": "<the replacement for all the flagged sentences of the item, in order>",
                 "v2": "<a second, different replacement>",
                 "keeps": "<one line: the points of the flagged sentences, and where each is in v1 and v2>"}, ...}

Each replacement replaces the flagged sentences as one stretch (they are next to each other in the paragraph, in the
order given), so it can be one sentence or several. Read only `/home/claude/joel-articles/articles/inner-signal/humanize/fix-20261029/b482/TARGETS.json` (your items are listed under
"W1"); don't run commands or use the web. Reply with only "DONE: <number of items>".
