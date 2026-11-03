# Brief: read one part of the hypnosis guide for nonsense

You are reading one part of Joel's self-hypnosis guide ("The Inner Signal", a long informal guide on his Substack). Parts
of it were drafted by AI tools, rewritten by AI tools, and edited by him. Joel just found this sentence in it:

> Tag questions, like "isn't it?" or "doesn't it?", can soften a sentence, but they get **oily** very quickly, so go easy
> on them.

He meant "they get **old** very quickly" (they get tiresome). "Oily" is a real word, and the sentence is grammatical, so
spell checks and earlier readers let it through. He asked: "do we have more nonsense in here? how are you not catching
this?" Your job is to find every other place in your part where a word or phrase is wrong like that, or doesn't make
sense, before the guide goes into his post.

## What to look for

- **A wrong word**: a real word that doesn't fit where it is, where a careful writer would have written another one
  ("oily" for "old"; "illicit" for "elicit"; "discrete" for "discreet"; "effect" for "affect"; a word that's nearly the
  right one but not quite).
- **A phrase that doesn't mean anything** when you stop and ask what it says: an odd collocation, a mixed metaphor that
  doesn't work, words that sound fine but leave you unable to say what the writer meant.
- **A broken sentence**: missing words, doubled words, a sentence that changes its grammar halfway, a pronoun with
  nothing to point at, a list whose items don't fit the sentence that introduces them.
- **A slip**: a typo, a wrong number or name, a letter left out or added, a stray punctuation mark, an unclosed bracket
  or quote, a word that is in the wrong language.
- **A sentence that contradicts** the sentence before it or the section it is in, or says something no one would mean.

## What is not nonsense here (Joel's own style; leave it alone)

- His informal voice: "etc etc", "kinda", "like", "...", jokes, asides in brackets, emoji, swearing, run-on sentences
  that still make sense, casual grammar ("According to who?").
- His made-up words and pet names, on purpose: "imposterous", "Baby boopaloopa", "Lovey Bunny", "bathroom
  vacationing", "fluffy wuffy". Ask yourself whether it's play or a slip; play stays.
- Technical terms of hypnosis, NLP, inner child work and Buddhism (Milton Model, Meta Model, nominalization,
  pendulation, titration, the Nurturer, the Protector, the Guide, guards, chrunga, loveyhuasca, Nimja).
- Hypnosis scripts: their repetition and odd rhythm are the technique.

## How to read

Read your part's file (the path is in your task): every paragraph starts with its block number, like `[118]`; headings
have `#` marks. Read the context before and after, but report only on the part. Read slowly, sentence by sentence, and
for each sentence ask: does every word mean what it is there to mean? Be thorough, but report only what is actually
wrong, not what you would phrase differently.

## What to write

Write one JSON file at the path in your task, and no other file; don't change anything else. Keep your replies short:
read, decide, and write the file in one Write call.

```json
{"part": "<your part>", "findings": [
  {"block": 1033,
   "text": "<the exact words that are wrong, copied character for character from the block, with a few words around them so a script can find them once>",
   "kind": "<one of: wrong-word, meaningless, broken, slip, contradiction>",
   "what": "<what is wrong, in one sentence>",
   "fix": "<the same words with the smallest correction>",
   "confidence": "<sure or likely>"}
], "notes": "<anything else, in a sentence or two>"}
```

Then reply with one line: how many findings, and how many you are sure of.
