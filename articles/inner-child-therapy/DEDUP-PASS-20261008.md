# The whole-article dedup pass (turn 35, 2026-10-08)

Joel, 2026-10-07 23:18 UTC: "but some of that looked like it was duplicating other stuff from before like also look outward and the section before. did you make the dedup pass before trying to humanize? i'm a little confused"

**No, I hadn't.** His instruction for the r4 guide was "if it has new stuff add that ... just make sure it's not duplicating stuff" (2026-10-07 01:09 UTC), and the update queue's own rule says the same: "If an item is already present semantically in the public draft, consume it without duplicating prose." I put it in every writer's brief as "Don't repeat what the article already says (the paragraph before and the section are shown)". So the writers and reviewers saw the paragraph before and their own section, and nothing further away. I checked the queue items by hand against what I remembered (K was dropped as a repeat of C1), but not the r4 paragraphs, and the article as a whole had never been checked for repeats. That's E151.

## How it was done

- Four readers, each a separate agent that hadn't seen the drafting:
  - Two read the whole article for every point it makes twice, and for contradictions. They found 38 and 40 repeats, and 6 and 8 contradictions.
  - Two split each waiting guide passage into its points. They checked each point, and each draft sentence, against the whole article: SAID, PARTLY or NEW.
- Their inputs and reports are in `experiments/dedup-20261008/`. The block numbers below ([B57] and so on) are those of its `article_blocks.md`.
- The quotes in the reports were checked against the article by the readers. The ones on the turn-35 page were checked again by the page tool, which stops if a quote isn't there.
- From now on `reviewer.py dedup` and `reviewer.py repeats` build these two prompts, and the gate runs the dedup before drafting (E151).

## 1. Joel's run, against Also Look Outward and the section before

His four paragraphs are in, word for word, and pass alone, in Your Body Might Need Some Love First and in Before You Try to Go Deep. These are his words, so nothing is cut. My take is under each.

1. **Guilt isn't a verdict, said twice.**
   - [B63], his apology paragraph: "Guilt may keep shouting at you. That doesn't tell you the whole conflict was your fault, nor does it prove they're manipulating you."
   - [B53], his boundary paragraph: "Just because your stomach tightened up doesn't mean their boundary crossing indicates "They're evil."" [B54] then extends it: "Feelings about yourself work the same way."
   - Both readers called it a moderate repeat: the same move, a feeling isn't proof, here for guilt and in both directions.
   - My take: keep both. The guide puts this point in Also Look Outward ("Notice your side too. Feeling guilty does not prove that you did something wrong; it also does not prove that somebody manipulated you."), for the case where you hurt them. If you'd rather it be said once, I'd cut [B63]'s last two sentences.
2. **Explaining again.**
   - [B63]: "Maybe your first explanation sucked. Try again. 😅 And if it fails again, and you've said what you mean, well, you can't guarantee they'll understand it."
   - [B58]: "it can seem like you haven't explained yourself well enough yet. You probably have, and it makes more sense to count on what they keep showing you they can do than on the right words finally getting through to them."
   - One reader counts it as a repeat and also as a pull in opposite directions. The cases differ: in [B58] they never hear you; in [B63] you hurt them and you're apologizing.
   - My take: a reader coming from [B58] may stumble on "Try again". The guide's line for [B63] is "You do not have to make somebody understand you before you can act." Your call.
3. **Get safe first.**
   - [B61]: "But if they've actually hurt or threatened you, even once, old stuff or not, get safe first".
   - [B55], the end of Catch the Hook: "Same if something might be dangerous right now, or might be a medical warning sign: step away or get checked first."
   - The same rule for a different case. [B61] carries the guide's "you do not need repeated exposure to danger before protecting yourself", right after a paragraph about going by patterns.
   - My take: keep both.
4. **A light echo.** [B64], C1: "or that you're sure what you want". [B54]: "it doesn't settle who you are, or who you love". Keep.
5. **Not a repeat.** [B57]'s "Once you're in your happy place" picks up [B53]'s "You can defer that judgement for when you're in your happy place." on purpose.

In the same h1 there's a stronger repeat that isn't in his run: the pause before you send. [B51]–[B52] in Catch the Hook ("half the text is written"; "take a breath or three before you finish whatever you were doing"), then Write It. Don't Send It Yet. ([B66]: "But don't send it."), then Borrow One Competency later ([B87]: "If you're about to send an angry text, hit pause."). Both readers put it among the five a reader would notice most.

## 2. The waiting drafts

**Update, turn 36:** all of these except C2 are parked. Joel cut depth draft 1, and the rest came from innerSignalGraph #126 (the app's routing rules written as prose), never queued for the public guide. See `R4-ADDITIONS-PROVENANCE-20261008.md`. What follows is kept as the record.

None of these is in the article. The turn-35 page shows each one in place, with what repeats marked blue.

### Already said in the article (cut when they're redrafted)

| Draft | The words | Where the article says it |
|---|---|---|
| Depth 1 | "Your little one will still be there later." | [B33] "leave the deeper conversation until later"; [B37] "you can wait until you're calm and actually ready" |
| Depth 2 | "or calling someone who's good for you" | [B33] "You may need somebody steady there with you" |
| Pleasantness 1 | "A session can also be really intense and get you nowhere." | [B3] "I could have kept crying forever."; [B165] "that can look convincing, with the right words and maybe even tears, while nothing underneath feels any safer" (one reader: SAID; the other: PARTLY) |
| Pleasantness 1 | "whether it was good for you" | whether it helped is [B171]'s and [B76]'s point; what's new here is whether it was too much |
| Pleasantness 2 | "have someone steady with you" | [B33] "You may need somebody steady there with you" (same point, nearly the same words) |
| Pleasantness 3 | "If you're not sure yet whether you want to, you can wait." | [B37] "you can wait until you're calm and actually ready" |
| Pleasantness 3 | "They aren't evidence that what you saw in them happened" | [B146] "They can feel totally real, but that alone doesn't prove they happened." (said there for memories in an altered state; new here: dreams and session imagery, and not suggesting or rebuilding a memory) |
| Isolation 1 | "text someone first" | [B173] "like texting a friend that you're having a rough day instead of saying you're fine" (the same example for the same move) |

C2 has nothing that's said elsewhere, only a light echo ("how they take it when you say no", against [B57]'s "can they hear you disagree"). Isolation 2 has nothing either.

### Said twice between the groups

The guide's depth and pleasantness passages share points, and the drafts carried both:

- the stop-and-come-back test (Depth 2, Pleasantness 2);
- eyes open before imagery (Depth 2, Pleasantness 2);
- going shallower, making the next one easier (Depth 2, Pleasantness 2);
- coming back gradually and only when you want to (Depth 3, Depth 2's "go slow", Pleasantness 3);
- waiting (Depth 3, Pleasantness 3).

Two more pairs:

- the word "reparenting" being optional (Depth 1, Isolation 1);
- looking after yourself and seeing people carrying on (Depth 1, Depth 3).

**My proposal:** say each once, split by when it happens. The steps during a session go in the depth group, where the guide has them: coming back out to the room if you can't stop and come back, going shallower, an eyes-open hello. The read after a session goes in the pleasantness group: how the next few days went, whether you want to go back toward it, the things to change, and coming back gradually.

### What's left to add

**Depth** (after [B33]):

- Turning the depth down isn't giving up on your little one, and changing the dose isn't failing. No draft says the second part yet.
- A no to the whole inner-child idea is a different thing. Drop the words, don't sneak them back in through gentler versions or chores called reparenting, and looking after yourself goes on in your own words.
- Going shallower. If you can't reliably stop and come back, or going inward is what's making it worse, come back out to the room in the middle of the exercise, instead of trying one inward technique after another to prove you can take it.
- The gentle way back in: one protective act, or an eyes-open hello before any imagery.
- A full pause, as the last resort. Any safety problem can force one, wanted or not.
- Make the pause specific: why, the last level that worked, and the change you'd be able to see, plus your own yes, that would make a return reasonable. No peeks during it, and come back at or below that level.
- Settle how a hard session landed before stepping back up. No draft has this yet.

**Pleasantness** (after [B49] and the map):

- How pleasant a session was doesn't tell you whether it was too much. Whether it helped is already in When to Change the Strategy.
- Grief, fear, frustration, hard dreams and stuff you'd rather not meet are expected. Hard isn't harm, and staying present isn't enough by itself.
- How the next few days went, sleep included, and whether you want to go back toward it.
- Whether it felt hard but workable, or just too much. No draft has this yet.
- Don't call it harm too fast either.
- While you're finding your level, change one thing at a time. If you're getting worse, change several at once: shorter, less depth or imagery, better timing, something more symbolic, eyes open, more support. Shorter, timing and symbolic aren't in the drafts.
- Bring the challenge back gradually, when you want to and you're recovering: the edge where you can learn.
- Dreams and imagery are material about what matters now. They aren't evidence, and they aren't something to suggest or rebuild a memory from.

**Isolation and honesty** (after [B64]):

- Being alone with it as part of the wound. Reaching toward people as the grown-up's care, with "reparenting" optional.
- Not having to get yourself sorted first. The guide's examples besides texting: setting up the visit, asking the social worker, walking into a room where people share something real.
- C2's points, none of them in the article yet:
  - honesty isn't telling strangers everything;
  - trust is earned bit by bit;
  - a fake happy self in a relationship that's getting deeper;
  - safety before telling;
  - the relief of being accepted isn't proof.
- Other people aren't a reassurance machine, and support goes both ways. No draft has these yet.
- More than one place to belong. Keep the good people, and not every door has to open.
- The Protector on groups: belonging doesn't make a group good.

### Next for these

1. Redraft each group with only what's left, and with the shared points split as above.
2. Run `reviewer.py dedup` on the new drafts before the cold reads.
3. Pangram: alone, in the h2 and in the h1.
4. Isolation 1's "a lonely kid" becomes "a lonely child". (The "never 'the kid'" rule is about the inner child, but this is close to it.)

## 3. Repeats I put into the article

I installed these without a whole-article check.

- **PGQ-004 in Start With Whatever Showed Up (mine, turns 32 and 34).**
  - [B158]: "If it might be real danger, though, I'd get some distance first, and find out how right it was later. Same with something a doctor should look at."
  - That repeats Joel's paragraph right before it, [B157]: "(if you're in danger, get safe first)". It also repeats his B2, [B55]: "or might be a medical warning sign: step away or get checked first".
  - Proposal: cut the danger sentence, and keep a doctor line that stands on its own. Then check it alone, in the h2 and in the h1. Not done yet; it waits for his OK on which to keep.
  - [B159]'s "If a part hesitates about being touched or about sex, that's enough to stop." overlaps [B55]'s "if you don't want to be touched, say no now". It adds sex, going deeper and altered states, so I'd keep it.
- **PGQ-012 in The Chicken-and-Egg Problem (mine, turn 31) and PGQ-013 at the end (mine, turn 30).**
  - [B15]: "but you also have to start actually doing some of it in the rest of your life". [B173]: "Whatever you did for your little one in there, I'd try a tiny bit of it out here". Both examples are self-care over overwork.
  - Both came from his queue, and each is where the queue put it. My lean: keep the short one in the stages. His call.
- **PGQ-005 in When to Change the Strategy (mine, turn 30).**
  - [B171]: "But I wouldn't decide from it that the problem's over". [B76]: "Feeling calmer or having deeper insights or explanations for the trauma response are some possible signs of initial progress, but if that's the endgame, it's just a cope."
  - [B171] adds how long it lasted, and other reasons you might feel better. Moderate; keep.

## 4. Elsewhere: the repeats both readers found

These went in during earlier turns, some in Joel's words and some in the lanes'. Nothing changes without his OK. They're listed with the strongest first. The turn-35 page shows the first nine in place (the safety exceptions with my PGQ-004 paragraphs).

| The point | Where | Readers |
|---|---|---|
| The safety exceptions (no to touch, danger, a doctor's check) | [B55]; [B157]–[B159]; also [B61], [B87] | both: strong (section 3 above) |
| Pause before you send the angry message | [B51]–[B52], [B66]–[B67], [B87] | both: strong |
| Hear the protective part out; don't force past it | [B155]–[B156] and [B162]–[B165] | both: strong |
| "I believe you. And I love you." | [B116], [B120], and the point again in [B129] | both: strong / moderate |
| "Well-loved" twice in a row | [B22], [B23] | both: strong |
| The inner child stays out of it, four times in six paragraphs | [B35], [B37], [B38], [B40] | both: moderate / strong |
| Grieving it "correctly" twice in a row | [B73], [B74] | one reader: strong |
| Mr. Rogers two paragraphs apart | [B84], [B86] (and stage 2 of [B14]) | both: strong |
| Stage 3 says the borrowed-adulthood paragraph again | [B12], [B14] stage 3 | both: strong |
| You need an adult there before you can be one | [B11]–[B12], [B25] | both: moderate |
| Don't go deep while you're mostly the frightened child | [B14] stage 1, [B33], [B49] | both: moderate |
| A session has to carry into your life | [B15], [B173] (section 3 above) | both: moderate |
| Don't invent the answer; it may come as a feeling | [B43]–[B44], [B156]–[B157] | both: moderate / strong |
| "If it starts feeling like an obligation, stop" | [B44], [B77] | both |
| Skip the parts detective work | [B51], [B154], [B155] | both |
| Slower exhales for a tight stomach | [B47], [B130] | both: light / moderate |
| Metta ended his depression | [B22], [B40] | both: moderate / light |
| Ill will feels like power but hurts you | [B39], [B118] | both: moderate |
| A loving line that means "now stop feeling this" | [B92], [B119] | both: strong / moderate |
| Don't snap back at the sarcasm or doubt | [B89], [B110], [B123], [B129] | both |
| Small kept promises earn trust | [B109], [B134], [B136], [B166] | both |
| When their complaint is right, say so | [B110], [B121]–[B122] | both: light / moderate |
| "I'll come back when I fail" | [B133], [B167] | both |
| The skeptic remembers your past fizzles | [B161], [B164]–[B165] | both: light |
| The work isn't meant to last forever | [B10], [B21], [B29], [B76] | both: moderate |
| Feeling calmer isn't proof | [B76], [B171] (section 3 above) | both: moderate |
| Adapt the method where it doesn't fit | [B76], [B172] | both: light |
| A protective part's no | [B159], [B167], [B172] | both |

The full lists, with every quote, are in `experiments/dedup-20261008/out_A1.md` and `out_A2.md`.

## 5. Pulls in opposite directions

Both readers found these. None is explained in the article.

- [B33] (wait if you're basically the frightened kid) against [B80] ("it's plenty to start with"). They may mean different starts.
- [B37] (you can wait until you're calm, unlike a real parent) against [B137] and [B154] (answer whenever your little one shows up; hear it the first time).
- [B86] (warmth first: borrow some) against [B111] (acts first, warmth after, "which feels backwards").
- [B159] (a part's no to going deeper is a stop) against [B172] (hear a protective "nope" out first).
- [B87] and stage 2 ("Even if this still feels like the child acting like the adult, for now, that's ok.") against [B145] ("it could even be like unintentional gaslighting").
- [B43] ("ask your little one what they need" can confuse) against [B81] ("What does Little Joel need right now?").

One reader found two more:

- [B55] (throwing every passing thought away isn't healthy) against [B154] ("Let a stray thought go as just thinking");
- [B58] against [B63] (section 1 above).
