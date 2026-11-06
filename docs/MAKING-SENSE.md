# The making-sense read

**ACTIVE (Joel, 2026-11-04 22:14 UTC, gate E360):** "do we need to devise some kind of making sense protocol rather than
attacking this problem case by case perhaps?" This is it: one read, for every paragraph I draft or rewrite in any of his
articles, before its first Pangram try and again after every change. It collects what his own fixes have taught, lesson
by lesson (E87, E342, E345, E347, E351, E355, E357, E359, E360, E362, E365, E366, E368, E369, E374 to E376), so a new case is met by the same questions
instead of a new rule. His words on why it comes first: "you don't need any lived experience, you just need it to MAKE SENSE". When a
paragraph makes sense the way his versions do, the AI reading has mostly gone with it; when it doesn't, no rewording
holds ("it's almost like pangram knows how stupid it sounds somehow").

**Enforced (Joel, 2026-11-05 15:14 UTC, gate E365, which enforces E362):** "why did i have to tell you this twice? fix the way you work because
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
   study comes after the question it answers, never opened bare (E357, E351, E360; `tells_lint.py` O65, O68). Ask it
   of each sentence and each paragraph, and ask where the point lands, not only whether there is one: a note that
   splits a sentence before its point, or a term explained in a sentence after the one that uses it, makes the reader
   work through it first (E368, E369).
   - Mine: "Zonulin is the molecule released to signal your intestinal tight junctions, the seals between the cells of
     your gut lining, to open." and, after the item, "Colostrum is the first milk a cow makes after giving birth, and
     liposomal means it comes in tiny fat bubbles that help you absorb it." (Human Medium, AI-Generated Medium). His
     fix, applied: "It's associated clinically with increased levels of zonulin, the molecule released to open your
     intestinal tight junctions, the seals between the cells of your gut lining." and "Liposomal first-milking colostrum,
     the first milk a cow makes after giving birth, wrapped in tiny fat bubbles that help you absorb it (esp. ...)"
     (both Human, High). His own, on the fuels stretch: "payoffs coming too late for the reader. fixed that so it reads
     easily and now it's all high conf human".
   - Mine: "In a 12-week trial, a CBD skin gel reached the blood at levels like oral CBD's but did no better than
     placebo." His: "And topical CBD hasn't been well-studied. There was a short 12-week trial done, where they used a
     CBD skin gel, ..." ("don't ever say "In one study..." you need to INTRODUCE so that people understand WHY they
     are reading this stuff").
   - Mine: "If you're already agitated, manic, on serotonergic meds, or using ..., you shouldn't be casually
     experimenting with it." His: "I'd avoid casually experimenting with 5-HTP if you're agitated or manic, as it could
     sometimes push that further." (E357)
   - The paragraph's first sentence is read too, whoever wrote it (E374). My dynorphin tries kept the model's opening,
     "To protect itself from the Glutamate storm, the brain eventually releases Dynorphin, a chemical blanket that
     suppresses dopamine.", and added the payoff at the end ("so don't read a better week as the armor coming off");
     both read AI, High. His opens on the reader's own state: "If you're feeling apathetic, gray, no desire for
     anything, you might be in a neurochemical "Void" state caused by Dynorphin & DeltaFosB." (Human, High; "i was as
     usual wondering why am i reading this?"). The receipt's `opens` asks it.
2. **What is this instruction for?** Say the purpose, in the reader's terms, when it isn't plain (E360).
   - Mine: "Put away the car keys." His: "get the car keys out of reach" ("why put car keys away, because it's messy to
     have them in the wrong spot? we want them OUT OF REACH").
   - Mine: "Begin with whatever could hurt somebody in the next five minutes." His: "Anything that could let someone
     hurt themselves in the next five minutes takes priority" ("how could anything hurt them? you mean they could HURT
     THEMSELF, so why didn't you say that?").
   - An instruction is said as something the helper does, not as a rule stated as a fact (E366). Mine: "And if they want
     to leave, someone goes with them." His: "And if they want to leave, have someone go with them" ("someone goes with
     them" was "not only compressed but has an air of snobbery to it"; his "sounds more concrete and practiacl, less
     judgey", and took the end of the paragraph from low to high confidence Human).
3. **Which thing exactly?** A word that names a whole kind, where the danger or the point is one case of it, names the
   case (E360).
   - Mine: "Move away from roads, balconies, water, ..." His: "move them away from roads and balconies, or pools of
     water for that matter" ("water isn't dangerous. POOLS of water are.").
   - Mine: "keep them from taking more of anything". His: "keep them from taking more of any substance" (""anything" was
     vague, i fixed that"; E366).
4. **What does this word act on, or mean here?** A word whose object or sense the reader has to guess gets it said
   (E360, E342).
   - "adjuncts" became "adjunct remedy" ("since adjunct is not really clear what it's adjuncting for"; the change that
     flipped his CBD paragraph to Human).
   - "a known CBD preparation" became "a known-genuine CBD preparation ... (a lot of CBD is fake or very dilute)"
     (""known" was unknown what that meant").
   - "your large intestine (colonocytes)" became "the colonocytes lining your large intestine" (E342: a term goes into
     the sentence, not into brackets after it).
   - Every term a high-school graduate wouldn't know is explained once, where it is first used (Joel, 2026-11-05: "make
     sure every term is introduced once at first, like enterocytes my readers won't know what those are. we don't need
     to introduce more common stuff like a vitamin name"; E369). Those changes are made without asking him; ask only
     when you can't tell whether such a reader knows the term, or can't explain it without guessing (his "HRP").
     `sense_receipt.py check` refuses a sentence of mine that explains a term after the text has used it.
   - A mechanism is explained by what it does in the reader's experience, not by where it sits or what it looks like
     (E375). Mine: "a chemical blanket that suppresses dopamine", "DeltaFosB is the slower one underneath, holding the
     circuit where the cycles left it", "They don't lift together". His: "dopamine is the neurotransmitter for
     motivation (by showing us what is important to pay attention to)", so suppressing it is the "no desire" the reader
     feels; "DeltaFosB keeps cementing our neural connections, preventing that learning from really "clicking" as
     durable insights"; and the loop in the reader's own terms, "because we're still reacting in the same maladaptive
     ways (same fears, etc), our psychology then asks for more DeltaFosB" ("it also wasn't explaining things well").
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
   - His first-five-minutes paragraph (bad trips guide, round 6, MOVE-YOURS) read AI with my movement sentences after
     the weapons and phone lines, and Human, High with nothing changed but their place: "actually, the problem was
     simply that you had the ideas out of their natural order, i fixed that with nothing changed apart from moving".
     Moving them away from roads, letting them pace, not letting them drive off or leave alone: where they go comes
     together, then what to put away, then the phone.
   - Things of one kind stay together: the warning-stage measures that aren't cannabis go before all the cannabis
     paragraphs, not between them ("we should move the non-cannabis para above all the cannabis info not put it
     inbetween canna paras isn't that obvious?"). When a paragraph moves, read again what its first "also", "this" or "as for" now points to: after the warning
     stage moved above it, the next paragraph's "I would also use ... as adjuncts" added to the warning-stage list
     (round 7's AFTER-MOVE card).
   - One point is said in one place (E376). I added what DeltaFosB does to the dynorphin paragraph while "The
     Hardening" paragraph said it again three paragraphs later, after the SSRI paragraphs. He folded it into his
     paragraph, in the order it happens (dynorphin clears, learning doesn't click, the old reactions call for more
     DeltaFosB), and deleted the other: "otherwise it was out of order and a bit redundant". Before adding a point, read
     the section from its heading to the next for it; the receipt's `same_point` asks it.
7. **Does this fact help this reader now?** A section's research is chosen for the situation the section is about, and
   a finding that doesn't serve that reader goes, however true (E360).
   - "think about the usefulness of the THREE YEAR STUDY when we are talking to people having seizures RIGHT NOW, so
     you did the wrong research. i took that one out." An acute section wants what helps in minutes, or says plainly
     that nothing has been tested for that ("we have no study on whether CBD could be a rescue remedy for a seizure").
   - The evidence that fits the reader's case: "why are we talking about focal seizures, when seizures from mdma and
     psychedelic overdoses are generalized seizures, right? so we should extrapolate from cbd evidence for that which we
     already stated in the para above with dravet and lennox types". Drug-induced seizures are generalized, so a
     finding about focal seizures goes unless it says why other evidence doesn't apply (the evidence to go by here is
     the Dravet and Lennox-Gastaut trials, which counted convulsive and drop seizures, both generalized).
   - **A check that takes away a point's payoff takes the point away too, his points included** (E362). His 7-OH-CBD
     point said the skin route misses "the potentially more active form"; the paper showed 7-OH-CBD works about as well
     as CBD, not better, and I kept the point and explained it at more length. He: "READ what you wrote, it literally
     is a whole big waste of time to talk about this, there's NO PAYOFF. nobody asked why CBD is better or worse than
     7-OH-CBD, the only reason to mention that is if that's important to consider which we establish it probably IS
     NOT". When a fact check weakens a point, ask what the reader would now do differently because of it; if nothing,
     propose the cut. A card's "What stays" is read with this question too: keeping his point is not a reason to keep
     a point that no longer does anything.
     After a source check, ask again whether the point still serves this reader: a correction is not a payoff.
     Enforced from round 7 by the receipt's "checked" list, where a point whose reason went must be cut (E365).
8. **Does each item belong where it's put?** When a passage sorts things into groups (kinds, tiers, safe and unsafe,
   dos and don'ts), read every item against every group: an item in two groups says how it belongs to both, or it's a
   contradiction (E359, the neuro de-armoring lane).
   - The 5-HTP stop signs had two lists sharing sweating, tremor and agitation ("again the logic problem, you listed
     dangerous symptoms and less dangerous symptoms which overlapped"). His: "Other stop signs include less dangerous
     symptoms (some of which are part of serotonin syndrome, but not dangerous alone)". The tell panel saw "a two-tier
     checklist" and missed the flaw, because the original had it too: read the original's own logic before drafting.
9. **Is it compressed?** One step a sentence, plain verbs, the small words that carry the relation ("which is",
   "treatment"), no space before "mg" (E338 (gut), E342, O67).
   - "someone goes with them" was "not only compressed but has an air of snobbery to it": see question 2.

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
- The first five minutes' dangers and movement, one paragraph (round 6, MOVE-YOURS), Human Written, 0%, High, Medium,
  High (https://www.pangram.com/history/e9d8d85c-5c0f-46b6-b780-91652f1efd15): "Anything that could let someone hurt
  themselves in the next five minutes takes priority, so get the car keys out of reach and turn the stove off, and move
  them away from roads and balconies, or pools of water for that matter. Letting them move around is fine, and pacing can
  help, but keep them from taking more of any substance. If they want to go confront somebody, that can wait. And if they
  want to leave, have someone go with them. Put any weapons away and keep the person away from crowds and strangers. If
  they want to post their big revelation about the universe, or message an ex, take the phone."
- The warning stage and cannabis paragraphs (round 6, CBD-TRIAL and SEIZ-WARN), his version and placement:
  `articles/bad-trips/review/r06/ANSWERS-R06-20261105-1514.json`.
