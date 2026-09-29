# Why Emulate's output can still sound like AI

**By Claude, 2026-09-29.** This compares Emulate's versions of Claude's drafts with Joel's own fixes of the same drafts (set A), plus the other Emulate outputs. The data is on `gpt/emulate-overnight-20260929` at `dcc0489` (GPT's Pangram results) and the Emulate outputs in `runs/emulate/`. The numbers come from `analysis/slop_numbers.py` (run it from the experiment folder).

## The short answer

Pangram passes almost everything Emulate writes, including versions a reader would stop at. What readers hear is two things Pangram doesn't score:

1. **The AI draft's skeleton.** Emulate keeps the draft's points, in the draft's order, one new sentence for each old one.
2. **A stock self-help voice** in place of the AI voice. These are phrases nobody chose, the same feeling AI prose gives, only human-made.

Joel's fixes do almost the opposite. He keeps most of Claude's sentences, then changes the thought: he cuts a point, disagrees with the draft, or adds one specific, slightly odd detail.

## What Pangram said

Of the 57 whole Emulate outputs checked on Pangram, **56 came back 100% Human**. Every paragraph checked alone was 100% Human too. The exceptions:

- **A02** was *AI Detected*, 59% AI. The flagged half is the part that follows the draft sentence for sentence. The draft says "you might have breezed through the check above and figure, 'I'll just bring the kid out for a second'". Emulate's flagged version: "it is possible that you ignored some of the above and are thinking 'I can just have the child out for a second'". The freer first half wasn't flagged.
- **B01 version 2 in its section** showed 8% AI, flagged at "It’s okay for the Protector to go first. It’s okay for you to start by…"
- A16, A24 and A26 weren't checked: they're under Pangram's 50-word minimum.

So passing Pangram isn't the hard part with Emulate. Choosing a version is about meaning and voice once one passes in its section.

## How much each one rewrites

Set A has 25 pairs where Joel's fix is a whole rewrite. A19 and A21 are left out here, because their "after" is only the sentence Joel added.

| | Emulate | Joel |
|---|---|---|
| Draft sentences kept nearly word for word (85%+ the same) | 1 of 139 | 54 of 139 |
| Words that sit in a run of 4+ words copied from the draft | 9% on average | 47% on average |
| Pairs where half the words or more are copied | 0 of 25 | 11 of 25 |
| Length compared with the draft (median) | 108% | 109% |

Emulate retells the whole paragraph in another writer's words, so Joel is right that it isn't paraphrasing in the usual sense. Paraphrasers swap words and keep sentences. Emulate keeps almost no sentence and keeps the argument.

Joel does the reverse. In A04 he keeps three of the five sentences and replaces "No insults, including the ones that sound like advice. No rushing them." with "Obviously no insults. Helpful advice is great, we all need advice. Let them absorb it at their pace." That's a disagreement with the draft, in the draft's own frame.

Both pass. **So there are at least two routes past Pangram:** retell everything in a different voice, or change the thought in one or two places. The splice experiments (Part 4) should show which sentences carry the verdict when only some change.

## Where Emulate shows (my opinion)

**It keeps the skeleton.** In almost every pair, Emulate's points come in the draft's order. Joel cuts whole points: in A02 he drops the scene of bringing the little one out to scare it, and in A20 the line about shaving his head. He also argues with the draft. In A07 the draft brushes off leaving a session calmer and full of insight; Joel counts those as early progress, then adds "if that's the endgame, it's just a cope."

**It swaps AI phrasing for stock self-help phrasing:**
- "embark on this journey to put radical honesty at the forefront of your relationship" (A27)
- "It’s important to point out" (A03), "It’s important to remember" (D2, second pass of B02)
- "warm fuzzy feelings" (B01 version 1), "warm and fuzzy" (B12)
- "a better worker bee" (A03)
- "you’re wasting your time" (A07)
- "In a series of illuminating and often hilarious conversations, Brooke will confront your deep shame" (B23, which reads like a book blurb)

**Lists get longer.** A01's six feelings become ten: "as vulnerable, as unimportant, as lonely, as helpless, as impotent, as impulsive, as scared, as incapable, as in despair…". In B01, one "it could have been" list becomes five questions in a row: "Were you afraid? Did you not know what you wanted? Did you not know how to do what you wanted? Were you too tired? Was something getting in the way?" Joel bans lists that over-explain.

**It invents people and facts.** This is the part that can't go into Joel's articles:
- "I always tell my kids that the hard part in therapy is pl/ork" (A21);
- "Brooke" and "$500 boots" (B23);
- "your toddler" and "McDonald’s" (B12);
- "maybe you want to figure out how to better exploit your employees at work" (D1, A02's second run).

It also gives the little one a gender: "her" in A10, "him" and "he" in A18 and A19.

**The meaning slips:**
- "the imps child" (A02);
- "a few would like the job to work better after therapy" (A02), where the draft said therapy would make them "better at working people";
- "tell them that they’ve hooked you" (A15), where the draft means naming it to yourself;
- "most of the time you can just tick them off" (B02 version 1), which reverses the draft's point.

**It's noisy.** A18 and B19 have "do n't" and ``` `` ''``` quote marks. That's the spacing old text-processing tools put into stored text, so my guess is that Emulate learned partly from text kept in that form. There's also "afterwords" (A05), a space before a comma ("as Pema Chödron has explained ,", A12), and British spellings ("behaviour", "no-one", "cancelling", "afterwards"). A reader takes these for errors, not for AI.

**It pushes its own persona onto human text too.** In Joel's C2 paragraph he puts himself in the reader's place: “What's a 'boundary'?”, I might be asking. Emulate turns that into a jab at the reader: "If you’re saying, 'What’s a ‘boundary’?' at this point, we may not have much further to go."

## Surface voice: Emulate moves toward Joel's rates

On the markers that are easy to count, Emulate lands near Joel. So the difference readers hear isn't in these (per 100 words, set A):

| | Claude's drafts | Emulate | Joel |
|---|---|---|---|
| we / us / our | 0.41 | 1.23 | 1.11 |
| exclamation marks | 0.00 | 0.28 | 0.26 |
| parentheses | 0.09 | 0.56 | 0.30 |
| "etc." | 0.00 | 0.12 | 0.04 |
| I / me / my | 1.73 | 1.31 | 1.19 |

On set B (Claude's second-person drafts), Emulate adds questions (0.09 to 0.77 per 100 words) and first person (0.23 to 0.93).

## The linter doesn't separate these groups

Hits per 100 words from `tools/tells_lint.py`:

| rule | Claude's drafts (set A) | Emulate (set A) | Emulate (all 60) | Joel's fixes | Claude's passing paragraphs |
|---|---|---|---|---|---|
| B11 tic | 0.00 | 0.00 | 0.03 | 0.00 | 0.07 |
| B2 contrast | 0.00 | 0.08 | 0.15 | 0.21 | 0.15 |
| B1 finished principle | 0.40 | 0.24 | 0.25 | 0.37 | 0.18 |
| B5 announces the paragraph | 0.09 | 0.16 | 0.07 | 0.08 | 0.04 |
| E41 coach phrase | 0.75 | 0.56 | 0.46 | 0.86 | 0.35 |
| B4/E15 list or packed sentence | 0.71 | 0.56 | 0.67 | 0.37 | 0.64 |
| B3 short knock-down | 0.09 | 0.08 | 0.04 | 0.16 | 0.07 |
| B7 short landing | 0.18 | 0.24 | 0.25 | 0.21 | 0.15 |
| E23 paragraph of instructions | 0.00 | 0.04 | 0.07 | 0.04 | 0.04 |
| **all sentence rules** | **2.20** | **1.95** | **2.01** | **2.31** | **1.69** |

Joel's fixes get more hits than the drafts they fixed. Only one rule clearly points the right way: packed sentences and lists, where Joel is lowest (0.37).

**I find this inherited check unhelpful here, and I suggest we change it.** Joel's choosing rule uses "fewer `tells_lint.py` hits" as its fourth tiebreak. For Emulate output, I'd replace that with three checks the linter doesn't make: nothing invented (people, numbers, facts about Joel), nothing reversed from the input's meaning, and fewer stock phrases. The linter was built on Claude's own tics, and Emulate doesn't have them.

## The 10 passing outputs with the most linter hits

Required by the directive, for Pro. The heavy-"you" note is left out.

1. **A18** (148 words, 7 hits): "Even if you do n't have any words coming to mind…" (finished principle, coach); "But if this feels like homework, skip it-he may be responding…" (finished principle, list, coach); "…instead of just talking to him in your imagination" (contrast); "But that does n't matter-you can still use words…" (coach).
2. **B01 version 2** (203 words, 7): "It’s okay for you to start by doing something…" (finished principle, coach); "Locking the door, eating a meal, cancelling something…" (list); "Keep only those things that help your little one to feel safe, to feel close to you, to be more functional, or to be happy" (list); "Pick one thing from the above that you can do" and "What’s the first step you can take?" (coach); the second paragraph (instructions).
3. **A27** (146 words, 6): "First, be sure that you and your partner both want to embark on this journey…" and "Second, if you do…" (announcing, twice each, since the paragraph repeats); "If he does, he's making a choice, too." (short landing, twice).
4. **B02 version 1** (160 words, 6): "Remember that if you didn't feel better after doing something it doesn't mean…" (contrast, coach); "Some things are useful to do to keep you safe, or to be close to someone, or…" (list, coach); "Maybe you didn't feel able to do it, or maybe…, or maybe…" (list); "Once you've done it (or not!) you can then see what happened…" (coach).
5. **B01 version 1** (202 words, 6): "They probably can think of a few things they do…" (list); "Keep in mind that doing something that should make your little one safe or close or competent or happy doesn’t necessarily mean it did" (list, coach); "The warm fuzzy feelings can come later." and "Only do things that actually help." (short landings); the second paragraph (instructions).
6. **C1** (126 words, 5): "Well, let's say you call yourself an idiot…" (finished principle, list); "…as well as they could see the clean room…" (the "clean" tic, though here it's literal); "…instead of snapping back, you let it go because, well, they don't really trust you, yet" (contrast, list).
7. **D2, second pass of B02** (163 words, 5): "It’s important to remember that if you didn’t feel any better…" (coach); "Maybe it’s something you need to do to keep you safe, or…, or…" (list, coach); "Maybe you didn’t feel you could do it, or…" (list); "Then, once you’ve done it (or not!) you can then see…" (coach).
8. **B03** (545 words, 5): "Most of the time your actions as a protector are seen by the little one." (finished principle); "Stopping yourself from acting on fear, rage, cravings, shame etc in terms of what you say, send, buy, take, do, have sex with, commit to etc." (list); "Leaving a degrading relationship is also a protector thing!" and "Or the office was shut?" (short landings); "It may take a while to develop the nurturing side but you can start." (coach).
9. **A13** (81 words, 4): "But wait!" (short knock-down); "You can get to that later." (short landing, coach); the paragraph (instructions).
10. **A12** (102 words, 4): "Sometimes you won't notice it until you've already tensed up your jaw, or whatever…" (list); "Just be aware, as Pema Chödron has explained , that…" (list); "She calls this shenpa ." (short landing); "It's okay to forget, for the time being…" (coach).

## What this suggests for the transfer test

When I write the `E_holdout` paragraphs by hand, I'll try Joel's route rather than Emulate's: keep what's already right, find the one or two sentences that carry the machine's thought, and change the thought itself (cut it, argue with it, or pin it to one specific detail). A02 hints that sentence-for-sentence retelling is where the AI verdict survives. The splice results will test that before I rely on it.
