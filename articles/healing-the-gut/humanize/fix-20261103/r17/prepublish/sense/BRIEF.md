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
- **A broken sentence**: missing or doubled words, grammar that changes halfway, a pronoun with nothing to point at.
- **A slip**: a typo, a wrong number or name, a stray mark, an unclosed bracket or quote, a word in the wrong language.
- **A contradiction** with the sentence before it or with the section.

## What is not wrong (this article's style; leave it alone)

This is Joel's gut-health article, "Healing the Gut Naturally", in his own first-person voice. These are deliberate; leave them alone:

- His informal voice: casual grammar and spellings ("gonna", "altho", "lol"), "shit" for what's stuck in the gut, jokes and exclamations ("And no snacking!", "Let's Play Gardener!"), asides in brackets, questions to the reader, and his two hyphens "--" where others put a dash. Headings' capitals vary on purpose.
- The article's own structure: a first part of his and his friends' findings ("Some Causes of poor gut health"), then a recipe in Phases 1 to 6 taken from books through his Gemini "Gem" (Gut Health Gem), with "(Phase N)" pointers from the first part into the phases, and a closing section of optional ready-made supplement stacks.
- The subject's terms, as they are: SIBO, IMO, SIFO, LPS, zonulin, tight junctions, enterocytes, colonocytes, butyrate, short-chain fatty acids, glutamine, alpha-ketoglutarate (α-KG), citric acid cycle, portal vein, BPC-157, zinc carnosine, beta-glucans, colostrum (first-milking, liposomal), bifidobacterium, L. reuteri, C. diff, H. pylori, berberine, oregano oil, wormwood, black walnut, diosmin, zeolite, oxalates, phytates, FODMAP, Paleo-Low FODMAP, Low Fermentation Eating, Bile Acid Diarrhea, A1 dairy, Iyengar yoga, qi-gong, colon hydrotherapy, diverticulosis, diverticulitis, Crohn's, IBS, IBD.
- People, books and products, named as they are: Pooyan (his friend), Matt Nedin and EndSickness.org, Dr. Rhonda (Patrick), Dr. Michael Ruscio, Dr. Mark Pimentel, Dr. William Davis, Barrier (a BPC-157 maker), ZeoCharge, Designs for Health GI Revive, Hippocrates.
- Link addresses and markup are not text to read; read only the words.
- Anything in his voice can still hold a real slip: a wrong word, a typo, a missing or doubled word, a sentence that breaks. Those you report, as the brief says.

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
