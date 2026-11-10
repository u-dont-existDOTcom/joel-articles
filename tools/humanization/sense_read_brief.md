# Brief: read one part of an article, word by word, for words that are wrong

You are reading one part of an article by Joel, a Substack writer. AI tools drafted and rewrote parts of his articles
before he edited them. In one of them he found this sentence:

> Tag questions, like "isn't it?" or "doesn't it?", can soften a sentence, but they get **oily** very quickly, so go easy
> on them.

He meant "they get **old** very quickly". "Oily" is a real word and the sentence is grammatical, so it got past every
check: the spell checks, the AI-text detector, the checks of whose words a sentence is. Only a reader who asks of each
word "is this the word meant?" catches it. Errors like that are what you are here to find. They are easy to read past:
the eye fills in the word that should be there. So read every word.

## The method (do it for every paragraph)

1. Read the paragraph one sentence at a time.
2. In each sentence, look at each content word (nouns, verbs, adjectives, adverbs) and ask: **is this the word a
   careful writer meant here, or a real word standing where a different one belongs?** Say the sentence to yourself with
   the word you'd expect; if the meaning changes, look hard at the word that's there.
3. Then ask of the whole sentence: can I say plainly what it means? Is anything missing, doubled, or garbled? Does it
   contradict the sentence before it?

## What counts

- **A wrong word**: a real word where another belongs ("oily" for "old"; "deceptive" where "receptive" is meant;
  "illicit" for "elicit"). These matter most.
- **A phrase that doesn't mean anything** when you ask what it says; a metaphor that doesn't work.
- **A broken sentence**: missing or doubled words, grammar that changes halfway, a pronoun with nothing to point at. A
  doubled word isn't only two in a row: it is also the same word, or two words doing one job, used twice in a sentence
  where the writer meant it once ("the example couple I really liked as an example", "can also be ... too"), and a
  comparison missing its "than" ("even better simply suppressing it").
- **A slip**: a typo, a wrong number or name, a stray mark, an unclosed bracket or quote, a word in the wrong language.
- **A contradiction** with the sentence before it or with the section.

## What is not wrong (this article's style; leave it alone)

{{STYLE_NOTES}}

## What you are given

Your part file has the blocks of the part, one per line, each starting with its number in square brackets: `[12] text`.
A line that starts with `#` after the number is a heading. Around the part there may be a few blocks of context before
and after it; read them for sense, but don't report on them and don't list them as read. The part to read is the section
headed "The part to read".

## What to write

Write one JSON file at the path in your task, and no other file; don't change anything else. Write it in one Write
call at the end, and keep your replies short.

```json
{"part": <your part number>,
 "read": [<every block number in "The part to read" that you read, in order: all of them, headings too>],
 "findings": [
  {"block": 12,
   "text": "<the exact words, copied character for character from the block, with a few words around them so a script can find them once>",
   "kind": "<wrong-word, meaningless, broken, slip or contradiction>",
   "what": "<what is wrong, in one sentence>",
   "fix": "<the same words with the smallest correction>",
   "confidence": "<sure or likely>"}
 ],
 "notes": "<anything else, in a sentence or two>"}
```

The "read" list is checked: a block missing from it counts as unread, however well the rest went. If you find nothing in
a block, you still list it.

Then reply with one line: how many findings, and how many you are sure of.
