# Brief: draft the meaning fixes for one part of sample bf

You are fixing a rewrite of one section (the induction) of Joel's long self-hypnosis guide. A paraphrasing tool wrote the
rewrite ("sample bf") from Joel's published section, and a Pangram check read the rewrite as Human in every window. A
second reader then compared it with the published section point by point. Your job is to draft the smallest set of edits
that puts back what a reader of the guide would need, while changing the rewrite as little as possible, because every
restored phrase risks making it read as AI again (an earlier sample had every point put back in plain words and then read
AI).

## What to read

- `VERIFY-partN-PROMPT.txt` in this folder: under "THE PUBLISHED SECTION:" is Joel's published part, and under
  "THE REWRITE:" is sample bf's part. Its first paragraphs are the instructions the second reader had; skip them.
- `VERIFY-partN.md`: the second reader's report, one "## P<n>" part per published paragraph (P0 is the first block of the
  published part), each point KEPT, CHANGED, LOST or ADDED, and an ADDED list at the end.
- `SAMPLE-partN.txt`: the rewrite's part, exactly as the fixes will be applied to it.

Read nothing else, run no commands, and don't use the web.

## Which items to fix (the triage)

Fix an item only when the rewrite would make a reader of the guide do or believe something different from what Joel
published:
- a LOST point that is an instruction, a step of a script, a safety or exit statement, a condition on when to do
  something, a reason the reader needs in order to follow the step, or a link;
- an ADDED-CLAIM: take it out, or make it say what the published says;
- a CHANGED point when the change alters what the reader does or believes: a permission turned into a duty or the other
  way round, a hedge turned into a promise ("may" into "will"), a condition dropped, a step dropped or reordered in a way
  that matters, the subject changed (yourself into another person), the strength of a claim changed.

Let stand, and list under "let_stand" with a few words why: tone, looser or more casual wording, a paraphrase that keeps
the point, "Say something like" before a script, the rewrite's personal voice, examples it adds that change nothing a
reader does, small words dropped ("fully", "gently", "exactly") unless the word carries the instruction, and the items
the report itself lists as "none acted on". When in doubt, let it stand.

## How to write each fix

- The smallest edit inside the rewrite's own sentence: a word or two, a clause, or at most one short new sentence. Never
  rewrite a whole paragraph, and don't touch sentences the fix doesn't need.
- In the rewrite's own casual voice and words. Use Joel's published wording only for a line the reader says aloud in a
  script, and only when the meaning needs it.
- Don't bring in shapes that read as AI: "without ...ing"; "not X but Y" or a ", not Y" tail; an idea doing what a person
  does ("silence doesn't authorize"); a tidy closing line, aphorism or balanced contrast; a reassurance after the point; a
  list of three parallel items where the rewrite has none; a doubled "and ... and".
- `old` is copied exactly, character for character (curly quotes and apostrophes included), from `SAMPLE-partN.txt`, and
  occurs there exactly once; make it longer until it is unique. Fixes must not overlap one another. `new` is what replaces
  `old`.
- Links don't cost words: for each link in the published part (a `[words](url)` there), give the words in the rewrite
  (after your fixes) that should carry it, exactly as they will read, and the URL. If the rewrite has no words for the
  link's subject, a fix brings in the fewest words that can carry it.

## Specific points

PART_SPECIFIC

## What to write

Write one JSON file with a single Write call to `FIXDRAFT-partN.json` in this folder, shaped like this:

```
{"fixes": [{"p": "P12", "old": "...", "new": "...", "answers": "the report's item, quoted", "why": "a few words"}],
 "links": [{"words": "...", "url": "..."}],
 "let_stand": [{"p": "P1", "item": "the report's item, quoted", "why": "a few words"}]}
```

Then reply with only one line: `fixes N, links N, let stand N`.
