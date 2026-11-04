# The word-for-sense read of the guide (turn 124)

Gate E331 (SKILL.md, "Word-for-sense read before publication"), on HUMANIZED-ARTICLE-SO-FAR.md d57d4a7bc09f (526 blocks, 28608 words): tools/humanization/sense_read.py make, 3 parts, 3 planted errors in each (seed 124), the brief with this guide's own style notes (STYLE.md). One fresh reader per part, given only its task line; the planted list (CANARIES.json) was out of the folder while they read. Part 3's first reader missed one planted error, so a second fresh reader read it again (pass1/ keeps the first reader's read and scores).

| Pass | Part | Blocks | Read | Planted errors found | Findings |
|---|---|---|---|---|---|
| first | 1 | 0-165 | 166 of 166 | 3 of 3 | 11 |
| first | 2 | 166-343 | 178 of 178 | 3 of 3 | 6 |
| first | 3 | 344-525 | 182 of 182 | 2 of 3; missed: "wealth" for "warmth" (block 455) | 11 |
| second | 3 | 344-525 | 182 of 182 | 2 of 3; missed: "wealth" for "warmth" (block 455) | 9 |

Recall: 8 of 9. Both readers of part 3 missed the same one, "wealth" where "warmth" belonged, in a list of what to picture ("wealth, protection, steadiness, rest"), where the planted word fits the sentence; so in part 3 the readers' silence counts for a little less. The planted errors:

- part 1, block 16: "peace" for "piece"
- part 1, block 85: "glisten" for "listen"
- part 1, block 133: "than" for "then"
- part 2, block 173: "quite" for "quiet"
- part 2, block 239: "glisten" for "listen"
- part 2, block 302: "thrust" for "trust"
- part 3, block 345: "then" for "than"
- part 3, block 455: "wealth" for "warmth"
- part 3, block 516: "quiet" for "quite"

Under the read, the non-word net (sense_read.py nonwords, NONWORDS.json): 96 tokens a dictionary doesn't know; 95 are names, terms, or his own words and spellings, every one in his guide, and one is a link address. Nothing to fix.

## Every finding, and its fate

The cards are on the marking page (https://claude.ai/artifact/RKJUWjR4MRCyRkpTqfDoZA; REVIEW.json, REVIEW.html, built by build_sense_page.py from CARDS.json). Every finding is in his own words (his reorganized guide of 2026-11-03), so none is changed without him.

| Card | Kind | Found by | The words | Suggested | Why |
|---|---|---|---|---|---|
| SR-10 | slip | reader 1 | "Unfortunate in the sense that" | "Unfortunately in the sense that" | The sentence before starts "Fortunately in the sense that", so this one pairs with it as "Unfortunately in the sense that". |
| SR-11 | form | reader 1, reader 3 | "handling--we see"; "test--"First" | "handling – we see"; "test – "First" | These two places have "--" where the rest of your guide has your spaced dash ( – ). |
| SR-68 | slip | reader 1 | "a free new-age get-out-of-jail-free card" | "a new-age get-out-of-jail-free card" | A get-out-of-jail-free card is free already, so the first "free" says it twice. |
| SR-69 | meaning | reader 1 | "Even if every case is different" | "Even if every case is debatable" | An "even if" grants something against the cases before you say you'd still read them. Every case being different doesn't count against them, so a word like "debatable" seems meant. |
| SR-76 | form | reader 1 | "you're moulding" | "you're molding" | Near the start your guide spells it "molding", and it uses American spelling everywhere else; here it's the British "moulding". |
| SR-96 | slip | reader 1 | "that's where Guide-building comes." | "that's where Guide-building comes in." | The saying is "that's where X comes in", and the sentence stops one word short. |
| SR-98 | slip | reader 1 | "scared." might be" | "scared" might be" | The quote sits in the middle of your sentence, so its full stop makes the sentence look finished before "might be the most adult thing". |
| SR-156 | slip | reader 1 | "to a glass "half full perception."" | "to a "glass half full" perception." | The quote marks hold "half full perception." where "glass half full" belongs, the way "glass half empty" has them earlier in the sentence. |
| SR-212 | slip | reader 2 | "giving into it" | "giving in to it" | You give in to a want, so "into" is two words here. |
| SR-212b | leave | reader 2 | "a rung on the desire treadmill" | leave it (the reader: "a step on the desire treadmill") | a treadmill has no rungs, so the picture doesn't work. |
| SR-262 | slip | reader 2 | "regardless whether" | "regardless of whether" | "Regardless whether" is missing its "of". |
| SR-373 | ask | reader 3, reader 4 | "I still played around with half-hanging out the windows" | Did the hanging out of the windows happen before your parents put the bars on? | Read in order, the bars go on, and then you "still" half-hang out of the windows, which the bars would stop. |
| SR-384 | leave | reader 3 | "something bigger than you, before that love starts to feel like yours, and then bit by bit it starts to become your own" | leave it (the reader: "something bigger than you, and then bit by bit that love starts to become your own") | the sentence says the same step twice. |
| SR-417 | meaning | reader 4 | "feels like water dripping through your hand" | "feels like water slipping through your hand" | The picture is what you knew getting away from you, which water does by slipping through your hand; dripping is slower, and the water stays. |
| SR-438 | meaning | reader 3, reader 4 | "So I'd ask this person" | "So you could ask this person" | You say "So I'd ask this person" the question, and two sentences later "personally I wouldn't even bother with that", so it reads as if you'd both ask and not ask. |
| SR-439 | slip | reader 3, reader 4 | "with TalkSpace therapy bot" | "with the Talkspace therapy bot" | The sentence is missing "the", and the company spells its name Talkspace. |
| SR-462 | slip | reader 4 | "Do you want to break someone mighty down?" | "Do you want to bring someone mighty down?" | The saying for toppling someone powerful is "bring someone down", and "break someone mighty down" reads like two sayings run together. |
| SR-465 | meaning | reader 4 | "call yourself out for it instead." | "call yourself out for it first." | "Instead" says not to call them out at all. The verse just before it takes the log out of your own eye first, and the words you and Tyler came up with call yourself out first and then name what he was doing. |
| SR-514 | meaning | reader 3 | ""meet the protector first"" | ""meet the guard first"" | Your rule is that "protector" never means a guard, and here the quote calls IFS's protective parts "the protector". Your readers know the Protector as one of the grown-up's three jobs, so "meet the protector first" can read as meeting that job first. |
| SR-516 | meaning | reader 4 | "in very powerful meditations." | "in very powerful altered states." | The example that follows is getting super high on weed, which isn't a meditation. |
| SR-517 | slip | reader 3 | "to whomever accesses it" | "to whoever accesses it" | It's the one who accesses it, so the word is "whoever". |

(Readers: 1 and 2 read parts 1 and 2; 3 and 4 are the first and second readers of part 3.)

## Findings that aren't cards

| Block | Found by | Whose words | The words | Fate | Why |
|---|---|---|---|---|---|
| 8 | part 1 | his guide | like another ex of mine (X) | kept: KEEP-AS-IS.json K4 | his turn-116 card A1: two exes are X on purpose, so nobody takes the unnamed one for Key |
| 105 | part 1 | his guide | "What's a 'boundary'?", I might be asking. | kept: KEEP-AS-IS.json K2 | his turn-116 card A3: "I", not "you": he is learning this too |
| 506 | part 3 (both readers) | his guide | Below are the differences between Lucia's approach and my guide's approach: | not real | the list is his picture right after it ("How This Reparenting Guide Differs From: Lucia Capacchione"), which the parts leave out |
| 518 | part 3 (both readers) | his guide | Anthony de Mello) is an excellent example | not real: a tool bug, fixed | the link's address holds brackets (Anthony_de_Mello_(Jesuit_priest)), and suggestion_review.py cut it at the first one, so the parts showed a stray bracket; the post never had it (CHECK-B.txt). Fixed this turn (LINK; tests/test_suggestion_review.py), with a link inside emphasis, which showed its markup |
| 19 | part 1 (notes) | his guide | the five stages list | not real | the list's first item is "1." in the article; the part file shows list items without their numbers |
| 377 | part 3 (notes) | his guide | Yep. Exactly like that. | not real | it answers the drawing just above it (an IMAGE note the parts leave out) |
| 405 | part 3, second reader (notes) | his guide | a double space before "It can help" | left | a double space doesn't show in the post |
| 157 | part 1 (notes) | his guide | tuberculosis from a cave | kept | his own history |
