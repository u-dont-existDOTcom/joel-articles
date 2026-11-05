# The making-sense read

**ACTIVE (Joel, 2026-11-04 22:14 UTC, gate E360):** "do we need to devise some kind of making sense protocol rather than
attacking this problem case by case perhaps?" This is it: one read, for every paragraph I draft or rewrite in any of his
articles, before its first Pangram try and again after every change. It collects what his own fixes have taught, lesson
by lesson (E87, E342, E345, E347, E351, E355, E357, E359, E360, E362 to E364), so a new case is met by the same questions
instead of a new rule. His words on why it comes first: "you don't need any lived experience, you just need it to MAKE SENSE". When a
paragraph makes sense the way his versions do, the AI reading has mostly gone with it; when it doesn't, no rewording
holds ("it's almost like pangram knows how stupid it sounds somehow").

**Enforced (Joel, 2026-11-05 15:14 UTC, gate E362):** "why did i have to tell you this twice? fix the way you work because
i'm not telling you the same stuff over and over." Question 7 was written here on 2026-11-04, and my round-6 card still
kept a point with no payoff, because nothing made me answer the questions sentence by sentence before the card went out.
Now the read leaves a receipt (`tools/humanization/sense_receipt.py`): for every sentence I write, what this section's
reader does or understands differently because of it and why it comes where it does; for every point I checked against
a source, whether its reason for being there survived the check (if not, it's cut); where the paragraph sits and why;
and each question answered. `pangram_ledger.py predict` refuses a text of mine without a receipt that passes, and
`suggestion_review.py` refuses a marking page whose new words have none (reviews built from 2026-11-05). Joel's own text
is predicted with `--his "whose words"` and needs no receipt.

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
   - An instruction is said as something the helper does, not as a rule stated as a fact (E364). Mine: "And if they want
     to leave, someone goes with them." His: "And if they want to leave, have someone go with them" ("someone goes with
     them" was "not only compressed but has an air of snobbery to it"; his "sounds more concrete and practiacl, less
     judgey", and took the end of the paragraph from low to high confidence Human).
3. **Which thing exactly?** A word that names a whole kind, where the danger or the point is one case of it, names the
   case (E360).
   - Mine: "Move away from roads, balconies, water, ..." His: "move them away from roads and balconies, or pools of
     water for that matter" ("water isn't dangerous. POOLS of water are.").
   - Mine: "keep them from taking more of anything". His: "keep them from taking more of any substance" (""anything" was
     vague, i fixed that"; E364).
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
   - The first five minutes, round 6 (E363): my two paragraphs had the movement lines after the phone line, and his
     merge read AI until he moved them, word for word, to sit after the dangers they belong with: "actually, the problem
     was simply that you had the ideas out of their natural order, i fixed that with nothing changed apart from moving
     ... now it's all high conf human".
   - A paragraph on another subject doesn't sit inside a group on one subject: the warning-stage paragraph (light,
     smell, a quiet room) went between two cannabis paragraphs on my page; he put it before all of them: "we should move
     the non-cannabis para above all the cannabis info not put it inbetween canna paras isn't that obvious?" When a
     paragraph moves, read what its first "also", "this" or "as for" now points to.
7. **Does this fact help this reader now?** A section's research is chosen for the situation the section is about, and
   a finding that doesn't serve that reader goes, however true (E360).
   - "think about the usefulness of the THREE YEAR STUDY when we are talking to people having seizures RIGHT NOW, so
     you did the wrong research. i took that one out." An acute section wants what helps in minutes, or says plainly
     that nothing has been tested for that ("we have no study on whether CBD could be a rescue remedy for a seizure").
   - A point that is now correct can still have no payoff (E362). His round-5 paragraph said the skin gel skips the
     liver's conversion to "the potentially more active form (7-OH-CBD)". I checked it, found 7-OH-CBD about as active as
     CBD in mice, and made the point longer and correct, when the check had taken away its only reason for being there:
     "nobody asked why CBD is better or worse than 7-OH-CBD, the only reason to mention that is if that's important to
     consider which we establish it probably IS NOT". After a source check, ask again whether the point still serves
     this reader; a correction is not a payoff.
   - The reader's case, not just the topic (E362). A trial in adults with focal epilepsy was brought in for a reader
     facing a seizure from MDMA or a psychedelic overdose: "why are we talking about focal seizures, when seizures from
     mdma and psychedelic overdoses are generalized seizures, right?" Evidence is picked for the kind of thing the reader
     faces (here the Dravet and Lennox-Gastaut trials, whose counted seizures are generalized), and a study of another
     kind is said to be another kind, or left out.
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

0. **The receipt:** `python3 tools/humanization/sense_receipt.py make TEXT --section "..." --reader "who, facing what
   exactly" [--his HIS.txt] --out RECEIPT.json`, filled in by me sentence by sentence (a sentence whose payoff I can't
   write is cut, not padded), then `sense_receipt.py check TEXT RECEIPT.json`. Pangram (`pangram_ledger.py predict
   --receipt RECEIPT.json`) and the marking page (each suggestion's `"receipt"`) take nothing of mine without it.
1. **Before drafting:** the newcomer read of the paragraph as it stands (`tools/humanization/hidden_links.py make`),
   a fresh reader given the questions above with his pairs as examples. Each gap gets answered in the draft, in the
   order the reader asks (`hidden_links.py check`).
2. **After drafting, and after every change:** the same read of the draft's own words (E355), and my own read of it,
   sentence by sentence, with these nine questions. A sentence that fails one is fixed before Pangram sees it.
3. **After a Pangram check that reads AI or below High:** find the part that still doesn't make sense and fix that
   (E361: "I do what i know works, and if it doesn't fix it, I just try to find the next obvious thing that shoudl
   work"). Keep what helped. Another method (another writer, the tell panel, a question to him) comes only when no next
   fix of this kind is left. `pangram_ledger.py predict` refuses a retry that changes more than 40% of the words of the
   last try without `--big-change` (moves don't count as changes): a rewrite is a new strategy, not the next obvious fix.
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
- The first five minutes, merged (round 6, MOVE-YOURS), Human, High, after he moved the movement lines: "Anything that
  could let someone hurt themselves in the next five minutes takes priority, so get the car keys out of reach and turn
  the stove off, and move them away from roads and balconies, or pools of water for that matter. Letting them move around
  is fine, and pacing can help, but keep them from taking more of any substance. If they want to go confront somebody,
  that can wait. And if they want to leave, have someone go with them. Put any weapons away and keep the person away from
  crowds and strangers. If they want to post their big revelation about the universe, or message an ex, take the phone."
- The warning stage and cannabis paragraphs (round 6, CBD-TRIAL and SEIZ-WARN), his version and placement:
  `articles/bad-trips/review/r06/ANSWERS-R06-20261105-1514.json`.
