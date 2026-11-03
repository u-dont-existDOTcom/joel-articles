# Brief: read one part of the hypnosis guide, paragraph by paragraph, for words that are wrong

You are reading one part of Joel's self-hypnosis guide ("The Inner Signal", a long informal guide on his Substack). AI
tools drafted and rewrote parts of it before he edited it. He just found this sentence in it:

> Tag questions, like "isn't it?" or "doesn't it?", can soften a sentence, but they get **oily** very quickly, so go easy
> on them.

He meant "they get **old** very quickly". "Oily" is a real word and the sentence is grammatical, so it got past every
check. He asked: "do we have more nonsense in here? how are you not catching this?" Errors like that are what you are
here to find. They are easy to read past: the eye fills in the word that should be there. So read every word.

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
- **A broken sentence**: missing or doubled words, grammar that changes halfway, a pronoun with nothing to point at.
- **A slip**: a typo, a wrong number or name, a stray mark, an unclosed bracket or quote, a word in the wrong language.
- **A contradiction** with the sentence before it or with the section.

## What is not wrong (Joel's style; leave it alone)

His informal voice ("etc etc", "kinda", "...", casual grammar like "According to who?", jokes, asides in brackets,
emoji, swearing); his made-up words and pet names, on purpose ("imposterous", "Baby boopaloopa", "Lovey Bunny",
"bathroom vacationing", "fluffy wuffy", "trancier", "choochoo"); the terms of hypnosis, NLP, inner child work and
Buddhism (Milton Model, nominalization, pendulation, titration, the Nurturer, the Protector, the Guide, guards,
chrunga, loveyhuasca, Nimja, "gather your attention"); hypnosis scripts, whose repetition is the technique; a phrase
that is unusual but means exactly what it should.

## What to write

Write one JSON file at the path in your task, and no other file; don't change anything else. Write it in one Write
call at the end, and keep your replies short.

```json
{"part": "<your part>",
 "read": [<every block number in your part that you read, in order: all of them>],
 "findings": [
  {"block": 1033,
   "text": "<the exact words, copied character for character from the block, with a few words around them so a script can find them once>",
   "kind": "<wrong-word, meaningless, broken, slip or contradiction>",
   "what": "<what is wrong, in one sentence>",
   "fix": "<the same words with the smallest correction>",
   "confidence": "<sure or likely>"}
 ],
 "notes": "<anything else, in a sentence or two>"}
```

Then reply with one line: how many findings, and how many you are sure of.
