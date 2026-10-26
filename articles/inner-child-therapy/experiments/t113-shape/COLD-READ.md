# Turn 113: the cold reads of the proposed sections, and what I did with each note

Four fresh Sonnet readers read every proposed section cold, each from one brief: [COLD-READ-BRIEF-B.md](COLD-READ-BRIEF-B.md),
[-A1.md](COLD-READ-BRIEF-A1.md), [-A2.md](COLD-READ-BRIEF-A2.md) and [-A3.md](COLD-READ-BRIEF-A3.md). (The first A brief,
[COLD-READ-BRIEF-A.md](COLD-READ-BRIEF-A.md), covered six sections and its reader ran out of output room before writing, so it
was split three ways.) Each read the section as it is (NOW), then as proposed (PROPOSED, headings skimmed first), then my reason
(WHY), and gave one verdict per section. Their reports: [COLD-READ-B.md](COLD-READ-B.md), [COLD-READ-A1.md](COLD-READ-A1.md),
[COLD-READ-A2.md](COLD-READ-A2.md), [COLD-READ-A3.md](COLD-READ-A3.md).

- The files in read/ are what B, A2 and A3 read. A1 read Start With Whatever Showed Up one step earlier, before its split at
  "I think a fear that keeps turning up".
- Provenance: each reader was an Agent-tool subagent with only its brief and the read/ files, though this session's hooks also put
  the UDA AGENTS.md and a memory snapshot in its context, so "only its brief" is not literally exact (as in turn 110).
- What changed after them is in [proposals.py](proposals.py) (SECTIONS), which checks every operation; every heading with new
  words in a section that changed went through gate round 3 ([../t113-gate/GATE.md](../t113-gate/GATE.md)).

## Every section: heading size and case

A1 (note 6) caught that at ###, Start With Whatever Showed Up's case headings would stand level with its own subsections (Two
Common Guarding Patterns, Hear the Guard First, When to Change the Strategy, When the Urge to Escape Arrives), which would then read
as more cases. Four other headed sections have the same shape: When Escape Leaves Reality Behind (### Gentle Meditation and Mantra),
Other Folks Also Have Hooks (### Write It. Don't Send It Yet.), Borrow One Competency at a Time (### If the Love Isn't Coming Yet)
and When the Adult Voice Feels Fake (## The Parent You Inherited and the two after it).

Done: every case heading is a ####, the size the guide already uses for its small headings. Joel's own "#### Non-altered states can
feel like this too" sits the same way, inside ## Altered States Can Require Reparenting and before its ### subsections.

B (note 4) asked for Title Case to match the section titles. Kept in sentence case, like his "Non-altered states can feel like this
too" and "This human life is the most precious opportunity": with the small size, it keeps them looking like signposts beside his
Title Case sections. The sheet's intro says so.

## Hear the Guard First (A1: FIX AS SUGGESTED, light)

1. "If it feels like it's all your fault" can read as the guard's feeling, next to three headings whose "it" is the guard. Done:
   "If it all feels like your fault".
2. "Earning its trust" names no case and says no when. Done: "Earning its trust, day to day".
3. The roommate image runs across a heading ("move out", "living there"). A1 accepts it, since only the image is lost; kept.
4. Optional, a heading for "If that voice isn't there in you yet, borrow it from someone who's been safe for you." Not done: it is
   one sentence that finishes "I'd still keep the Nurturer voice", and A1 also counts the unbroken opening exchange as a gain.
5. to 7. No failure; nothing lost.

## Start With Whatever Showed Up (A1: FIX AS SUGGESTED, moderate)

1. "Which thoughts to talk to" didn't match "How you picture all that is up to you..." and cut "all that" off. A1 read the version
   before the split; since the split, the heading stands over "I think a fear that keeps turning up...", which it matches. Kept.
2. Optional, a heading for the second half of "I wouldn't spend long deciding what to call each part, though." Not done: the two
   sentences after it are its reason (every part learns from how the others treat it), so they stay with it.
3. "If you do get an answer" holds two cases, and the cautions on an instruction are buried. Done: the paragraph splits before "If
   it tells you to do something", his words, which become its heading. "How you picture all that is up to you, as long as it
   helps, and the simpler the better." moves up three sentences, to right after the forms an answer can take, which "all that" is
   about; without the move it would have sat under the new heading, after the cautions. The move is the one change of order on
   the sheet (proposals.py checks that no word is added or lost).
4. "If nothing comes" can read as "nothing showed up", under this section's title. Done: "If no answer comes", which pairs with "If
   you do get an answer".
5. "When to stop" names no trigger; A1 suggests "When a part says no". Gate round 1 had failed "If a part says no" (it
   leaves out the hesitation and the cases, touch, sex, going deeper and an altered state, and says the sentence's opening
   twice), and round 3 failed "When to stop" too, for A1's reason. Done, with no new words: the heading is his whole
   condition, "If a part hesitates about being touched or about sex, or says no to going deeper in this work or to an altered
   state", and the rule starts "I'd stop there and not test it, even when it sounds like a prediction." It is long, and every
   case is in it once.
6. The heading level: done for every section (above).

## When to Change the Strategy (A2: FIX AS SUGGESTED)

1. "How many tries would I give it?" holds a second case, speaks as "I" and promises a number. Kept: it is his question, a reader's
   question, and the paragraph's second case (change course sooner if it's making things worse) is part of its answer.
2. "these steps" lost what it points at, and "keep" was lost. Done: the heading is his condition, word for word, "If you keep
   following the reparenting steps correctly without getting the expected results", so "these steps" has "the reparenting steps"
   right above it, with no new words.
3. "When the words sound empty" doesn't say which words. Done: "When your kind words sound empty".
4. to 7. Two openers that restate their heading with a concrete example, which A2 says to leave; the rest no change.

## When Escape Leaves Reality Behind (A2: FIX AS SUGGESTED)

1. "Your own drug history" is a topic label. Done: "If a past trip went badly". His "Your own drug history matters too." leaves the
   paragraph (on the sheet).
2. "Paranoia" is a bare noun that the first sentence repeats. Done: "Is your paranoia a warning sign?", which the first sentence
   answers.
3. The split put the THC line between the paranoia examples and what to do after. Done: the split moves to before "If you can’t
   clearly understand what happened yourself".
4. "Any of those reactions" points across two headings. Kept: its own "from mania to paranoia" says what they are, and rewording
   would put new words into a paragraph that reads Human.
5. "By trusted, I mean ..." is a rule for anyone choosing a helper, hidden under the mania heading. Done: its own heading, "Who
   counts as trusted".
6. "Coming back from trips confused or spaced out" lost "keep". Done: "If you keep coming back from trips confused or spaced out".
7. The medication and withdrawal warning is hidden under the spaced-out heading. Done: the paragraph splits before "And don't
   suddenly stop a medication", under "Before you quit a medication or alcohol", and the "And" leaves.
8. "What you mix" is vague. Kept: his words, said in full by the paragraph's first sentence; A2's "Mixing: medicines, plants and
   ayahuasca" is a colon list.
9. Optional, a split for 5-MeO-DMT. Not done: it is the example of what "slow and gentle protocols" are against.
10. and 11. Nothing else lost.

## When the Adult Voice Feels Fake (A3: FIX AS SUGGESTED, headings 2 and 3)

1. "In an altered state" is a fragment that its sentence then repeats. Done: the heading is his clause, "For some people it only
   stops feeling fake in an altered state", and the paragraph starts "Like on MDMA or deep in meditation."
2. "The Ideal Parent Figure method" is a name, gives away sentence two, and the dropped "And" was the only link back. Done: the
   heading is his whole first sentence, "Picturing one ideal parent seems to help some people" (its "And" goes with it), so the
   paragraph starts "There's a whole method built on it", and the name still comes in its own sentence. A3's "Another way through:
   picturing one ideal parent" repeats the sentence's first words and adds a colon label.
3. "Sometimes kindness feels scary more than fake" works; nothing may go between it and "One study's title has a word for that".
   Kept.

All three headings are now his own sentences or clauses, so this section has no new words.

## Finding a Therapist to Borrow Adulthood (A3: FIX AS SUGGESTED, all four)

1. The vetting tip ("you can ask a therapist to check it out ... as a great way to vet them") sits under "Inner Child Reparenting
   therapists". Kept: the sentence starts "I can consult", which answers "There are none which work with my guide yet", so it can't
   move without what it answers (E264), and the wider heading A3 offers is two headings in one. The heading also repeats the
   paragraph's first words; his sentence can't start without them.
2. "IFS and Schema Therapy" leaves "come close" without its anchor and leaves IFS unexpanded. Done: "If you want a licensed
   therapist", the reader's case beside the often-unlicensed reparenting therapists above; the next sentence ("Schema Therapy comes
   closest to my approach") says close to what.
3. "Before choosing a therapist". Kept: his words, which say when it applies; "their" has the heading's "a therapist" right above.
4. "AI therapy". Kept: his words; a reader looking for it finds it.

## Other Folks Also Have Hooks, Borrow One Competency at a Time, How Would You Know It's Helping?, How to Forgive Without Forgetting, Borrow Love (B)

- Other Folks Also Have Hooks, FIX AS SUGGESTED.
  - Note 1, done in round 2: his own words as the heading "If a relationship keeps making you feel less safe", and the danger line
    split off under his "If they've actually hurt or threatened you".
  - Note 2, done: "Also easier said than done" drops its "Also".
  - Note 3, checked: the bare note is his reply about trust being granular ("it's hard to trust people who trust people that
    disrespect [or distrust] you ... but that doesn't mean i don't trust them in other ways"), which goes with the realistic
    boundary that ends "Can they change?", so it stays there.
  - Note 4: sentence case (above).
  - Note 5, for Joel: his second paragraph answers only the first of his two questions. On the sheet as a side note, with my pick
    to leave it.
- Borrow One Competency at a Time, KEEP AS PROPOSED. The case note is above; "For warmth" is his word.
- How Would You Know It's Helping?, KEEP AS PROPOSED.
- How to Forgive Without Forgetting, KEEP AS PROPOSED.
- Borrow Love (his 109 A), KEEP AS PROPOSED. The added words sit outside both links ("psychological trick" and "Solomon’s
  paradox"). The curly apostrophes in that paragraph are his, kept as he typed them.
