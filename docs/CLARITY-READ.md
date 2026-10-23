# The clarity read: what passes Pangram but is hard to understand

**ACTIVE, standard for every article (Joel, 2026-10-23 16:55 UTC):** "let's make sure this kind of check is standard for
articles as we write them and as we finalize before publishing in future, i thought it already was".

It wasn't. Two reads came close and neither is this one:
- the section cold read (`tools/humanization/reviewer/sense_section.txt`) reads text a worker drafted, a section at a time,
  for where the sense breaks, and lets a passage stand that a reader gets on a second look ("a reader who pauses and then
  gets it isn't lost");
- the reader-question audit (`docs/READER-QUESTION-AUDIT.md`) is optional, offered, and looks for the questions an article
  leaves open, not for passages that are hard to follow.
Nothing read a whole article, Joel's own words included, for what a smart general reader would have to reread. The first
whole-article clarity read was Nibbāna's, after his question of 2026-10-23 14:14 UTC ("is there any other stuff in the
nibbana guide that's hard to understand but still passing pangram?"): three fresh readers found 29 passages, 12 of them
hard enough that most readers wouldn't get them (`articles/nibbana/humanize/fix-20261023/clarity/CLARITY.md`).

## When

1. **As an article is written:** once a full draft of a new article, or a long new section, is complete, before its
   whole-article Pangram check. The section cold read still runs on each drafted section as it is written; this read comes
   once the whole thing exists, because what a reader needs explained depends on what came before.
2. **Before publishing:** on the final candidate, once every other change is in, and before the final whole-article
   Pangram check, so that the passages it changes are read in place by that check.
3. **After a large batch of changes to a published article** (a humanization pass, a restructure), at the next stable
   point.

A short piece, a typo fix or a one-paragraph change doesn't need it.

## How

1. `python3 tools/humanization/clarity_read.py make ARTICLE DIR --parts 3 --about "..." [--question "..."]` writes the
   reading text, the parts (split at headings, about 30,000 characters each) and a brief for each part. The brief carries
   Joel's own fixes as the examples of what counts (`tools/humanization/clarity_examples.json`; add one each time he fixes a
   passage for clarity, with his words).
2. Give each `BRIEF-k.txt` to a fresh reader: a new agent that has seen nothing else (Sonnet is enough; Opus for an article
   whose argument is technical). Each writes `READER-k.md`: each passage, what's hard, a score (3: most readers wouldn't get
   it; 2: most would have to reread; 1: a small snag) and a plainer version.
3. `clarity_read.py collect DIR` puts them in `ITEMS.json`, each found in the article (or marked not found).
4. **Check every item against the whole article yourself**, since each reader saw only its part. An item explained
   elsewhere gets `"status": "drop"` and a note saying where; a small one `"minor"`; `"my_score"` overrides a reader's
   score; `"check"` names any step of a plain version that guesses at his reasoning. In Nibbāna's read, 7 of 36 flags were
   things another part explained.
5. `clarity_read.py page DIR --out CLARITY.md` writes the list for him, numbered, hardest first, with the small snags and
   what wasn't counted at the end. Send it to him as a link he can click, with the number of passages and what kind they
   are, and ask him to rewrite or pass each one (his answers are numbered the same way).
6. Put his answers in word for word (his rewrites, and the plain versions he passes), with every link, italic and bold back
   on the same words, and each changed passage read in place in the next whole-article Pangram check with a part forecast
   (`tools/humanization/part_forecast.py`; gate E238).

## What the plain versions are for

A reader's plain version says what a reader needs; it is rarely the text that goes in. Of Nibbāna's 28 plain versions that
he checked, he called 13 AI and rewrote them (and one more without a verdict), and passed 14 (3 of them as "possibly
human"). His rewrites passed. What his rewrites did that the plain versions didn't is the gate's E241: his stance and his
reasons in the sentence ("which I'd explain as", "tellingly", "it's pretty clear that", "that's a relief"), his own images
("buys a mirror from the local mirror shop", "my dad's favorite oxymoron: 'military intelligence'"), and no summing-up line
("Put together, that says ...", "That's why, in this article, ..."). So the brief now asks for the smallest change to his
own words, and the list goes to him expecting his rewrites, not as text to install.
