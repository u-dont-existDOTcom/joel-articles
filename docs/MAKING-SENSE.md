# The making-sense read

**ACTIVE (Joel, 2026-11-04 22:14 UTC, gate E360):** "do we need to devise some kind of making sense protocol rather than
attacking this problem case by case perhaps?" This is it: one read, for every paragraph I draft or rewrite in any of his
articles, before its first Pangram try and again after every change. It collects what his own fixes have taught, lesson
by lesson (E87, E342, E345, E347, E351, E355, E357, E359, E360), so a new case is met by the same questions instead of a new
rule. His words on why it comes first: "you don't need any lived experience, you just need it to MAKE SENSE". When a
paragraph makes sense the way his versions do, the AI reading has mostly gone with it; when it doesn't, no rewording
holds ("it's almost like pangram knows how stupid it sounds somehow").

## The questions

Ask each of every sentence, as a reader who doesn't know what the writer knows and is reading this section because of
the situation its heading names.

1. **Why am I reading this sentence, and do I know it before I have to work through it?** The point comes first; a
   study comes after the question it answers, never opened bare (E357, E351, E360; `tells_lint.py` O65, O68).
   - Mine: "In a 12-week trial, a CBD skin gel reached the blood at levels like oral CBD's but did no better than
     placebo." His: "And topical CBD hasn't been well-studied. There was a short 12-week trial done, where they used a
     CBD skin gel, ..." ("don't ever say "In one study..." you need to INTRODUCE so that people understand WHY they
     are reading this stuff").
   - Mine: "If you're already agitated, manic, on serotonergic meds, or using ..., you shouldn't be casually
     experimenting with it." His: "I'd avoid casually experimenting with 5-HTP if you're agitated or manic, as it could
     sometimes push that further." (E357)
2. **What is this instruction for?** Say the purpose, in the reader's terms, when it isn't plain (E360).
   - Mine: "Put away the car keys." His: "get the car keys out of reach" ("why put car keys away, because it's messy to
     have them in the wrong spot? we want them OUT OF REACH").
   - Mine: "Begin with whatever could hurt somebody in the next five minutes." His: "Anything that could let someone
     hurt themselves in the next five minutes takes priority" ("how could anything hurt them? you mean they could HURT
     THEMSELF, so why didn't you say that?").
3. **Which thing exactly?** A word that names a whole kind, where the danger or the point is one case of it, names the
   case (E360).
   - Mine: "Move away from roads, balconies, water, ..." His: "move them away from roads and balconies, or pools of
     water for that matter" ("water isn't dangerous. POOLS of water are.").
4. **What does this word act on, or mean here?** A word whose object or sense the reader has to guess gets it said
   (E360, E342).
   - "adjuncts" became "adjunct remedy" ("since adjunct is not really clear what it's adjuncting for"; the change that
     flipped his CBD paragraph to Human).
   - "a known CBD preparation" became "a known-genuine CBD preparation ... (a lot of CBD is fake or very dilute)"
     (""known" was unknown what that meant").
   - "your large intestine (colonocytes)" became "the colonocytes lining your large intestine" (E342: a term goes into
     the sentence, not into brackets after it).
5. **Why does this follow from the sentence before?** A "but", "so", "though" or "because" has the claim it turns on;
   two facts side by side have their link said; "this", "that" and "it" point at something the reader can name (E345,
   E351, E355, E357).
   - His: "He's genetically slow-COMT, making him sensitive to too much P5P." where mine had the two facts "floating
     there, what were they for? nobody knows" (E357).
   - His: "But glutamine is still the main thing they need, because it helps build new cells ..." (E351: the claim the
     "but" turns on).
6. **Is this the order the reader is thinking in?** What was just discussed is carried on before something new starts
   (E347, E360).
   - His CBD paragraph moved the topical trial after the oral approval: "which was out of order, should go AFTER the
     oral part since we were discussing oral before that".
7. **Does this fact help this reader now?** A section's research is chosen for the situation the section is about, and
   a finding that doesn't serve that reader goes, however true (E360).
   - "think about the usefulness of the THREE YEAR STUDY when we are talking to people having seizures RIGHT NOW, so
     you did the wrong research. i took that one out." An acute section wants what helps in minutes, or says plainly
     that nothing has been tested for that ("we have no study on whether CBD could be a rescue remedy for a seizure").
8. **Does each item belong where it's put?** When a passage sorts things into groups (kinds, tiers, safe and unsafe,
   dos and don'ts), read every item against every group: an item in two groups says how it belongs to both, or it's a
   contradiction (E359, the neuro de-armoring lane).
   - The 5-HTP stop signs had two lists sharing sweating, tremor and agitation ("again the logic problem, you listed
     dangerous symptoms and less dangerous symptoms which overlapped"). His: "Other stop signs include less dangerous
     symptoms (some of which are part of serotonin syndrome, but not dangerous alone)". The tell panel saw "a two-tier
     checklist" and missed the flaw, because the original had it too: read the original's own logic before drafting.
9. **Is it compressed?** One step a sentence, plain verbs, the small words that carry the relation ("which is",
   "treatment"), no space before "mg" (E338 (gut), E342, O67).

## How it runs

1. **Before drafting:** the newcomer read of the paragraph as it stands (`tools/humanization/hidden_links.py make`),
   a fresh reader given the questions above with his pairs as examples. Each gap gets answered in the draft, in the
   order the reader asks (`hidden_links.py check`).
2. **After drafting, and after every change:** the same read of the draft's own words (E355), and my own read of it,
   sentence by sentence, with these nine questions. A sentence that fails one is fixed before Pangram sees it.
3. **After a Pangram check that reads AI or below High:** find the part that still doesn't make sense and fix that
   (E361: "I do what i know works, and if it doesn't fix it, I just try to find the next obvious thing that shoudl
   work"). Keep what helped. Another method (another writer, the tell panel, a question to him) comes only when no next
   fix of this kind is left.
4. **The tell panel** reads after two AI results (E346). A panel note that asks for lived experience, first person or
   stakes sends the paragraph back through this read; it is never a reason to ask him for his life story to cover my
   tells.

## His versions, in full

- The first five minutes' dangers paragraph (bad trips guide, round 5, PFA-YOURS), Human ("fully human, super easy"):
  "Anything that could let someone hurt themselves in the next five minutes takes priority, so get the car keys out of
  reach and turn the stove off, and move them away from roads and balconies, or pools of water for that matter. Put any
  weapons away and keep the person away from crowds and strangers. If they want to post their big revelation about the
  universe, or message an ex, take the phone."
- The CBD paragraphs (round 5, CBD-YOURS), Human, High, before he added his video link; his seven checks and what each
  changed are in his comment in `articles/bad-trips/review/r05/ANSWERS-R05-20261104-2214.json`.
