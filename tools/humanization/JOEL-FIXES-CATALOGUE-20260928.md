# Joel's humanization fixes, read in full (2026-09-28)

Joel, 20:13: "you're just winging this, rather than trying to understand how i've been humanizing thigns, because i've given a LOT of humanization fixes thru the various articles i've humanized." This file is what I found when I read them.

**Sources read, pair by pair, by me:**
- **This article:** every before/after pair on record, pulled out word for word from the experiment records, calibration files and ledgers by seven reader subagents, then de-duplicated. That gave 125 entries, 58 of them with the AI "before".
- **The lab repo:** its generation notes, owner corpus, benchmark and holdout sets, experiments and cases, handled the same way.
- **Romance:**
  - the owner-final sections ("If you're already in it", "Tough Love", "exclusivity");
  - the r23 five owner edits;
  - the Two Pillars reorder.
- **Nibbana:** the 2026-08-01 AI/hybrid baseline against the current master. The master mixes Joel's own passages and AI-assisted ones, so not every change there is his.
- **Sleep and detox,** uploaded 2026-09-28. These are Pangram 4.0 reports of the before versions, with segment labels: sleep 24% AI, detox 14% AI. The 13 AI-flagged segments (9 in sleep, 4 in detox) were matched to his humanized versions. Those two texts stay out of git; only short fragments are quoted here.

**Not read as pairs:**
- The lab's 84 lesson closeouts. They are its rules in its own words, and Joel's point is that models re-anchor on paraphrased lessons.
- The somatic article's AI original. It isn't on disk; only a later model reconstruction (r01) and his published v4.2 text are, plus fragments of his rewrites.
- The old r19, r20, r22 and r25 cases (older Nibbana, Inner Child, Romance and "Different Levels"). Their exact texts were never recovered.

## What he cuts

1. **The last line that sums up.**
   - Joel: "just remove the last sentence since it was obviously doing that ai thing of ensuring the thought is fully complete and summed up perfectly".
   - Cut: "So an afternoon of coloring badly together might do more than another hour of going over what went wrong." The paragraph went from 100% AI to Human.
   - Cut: "One who never does has basically sold you a subscription." Joel: "matched pair ending on punchline gives it away."
   - Gone in his sleep article: "The best use of a sleep tracker is pattern recognition, not sleep perfectionism."
2. **"Not X. It's Y." and its cousins.**
   - Sleep: "The point is not perfect measurement. The point is pattern recognition." became "You won't measure stuff perfectly, but this way you might start seeing some important patterns jump out."
   - Also cut: "The goal is not to become obsessive about sleep. The goal is to remove the biggest blockers…" and "that is not just 'bad sleep hygiene.' That is a medication-review question."
3. **Reassurance and commentary about the text itself.**
   - Cut: "This is not meant to scare you. It is meant to save time. Sometimes the missing 'sleep hack' is a diagnosis."
   - "Treat the complete sequence as a provisional synthesis: some components have direct research behind them, while the full arrangement is my own:" became "For now, I think of it in five fairly predictable stages. You might be starting at any point here (and it may change even from hour to hour as well):"
4. **Wry quips.** Nibbana baseline to master (the master mixes his own and AI-assisted edits, so these may not all be his hand):
   - "which is useful when people expect answers instead of a beatific vegetable." became "just like in Ud 5.10."
   - "People can visit heaven for an afternoon and then forget to ask for directions back to Albuquerque." was cut.
   - "a therapist, a saint, or even a competent roommate." became "therapist, let alone a saint."
   - Joel, 19:51: "the wry humor is also an AI tell. it's wry in a strange way".
5. **Mechanism talk and over-precise sourcing.**
   - Detox: "routes methylation through the BHMT pathway as a slower, more buffered alternative. Niacin (B3) also 'burns off' excess methyl groups and can damp over-methylation. Practitioners titrate among these." became "taking TMG (trimethylglycine / betaine) and Niacin (B3) can help."
   - Sleep: "CDC lists 7 or more hours for adults 18–60…" was cut.
6. **The bridge sentence that announces the next move.**
   - Catch the Hook: cutting only "Later, ask the fun question: what actually happened?" took the boundary from AI/medium to Human/medium.
   - Romance: "Community isn't magic either;" went.
7. **The third item of a condensed function list.**
   - Cut: "or they're honestly hoping therapy will make them better at working people". Joel: "a 3 part function list and quite condensed".
8. **Taxonomy inside a list item.**
   - "experience one reliable adult function through someone real, remembered, imagined, or symbolic" became "learn a bit of adulting through someone real. Or someone you remember. Even just imagination or someone symbolic could work."
   - Only that stage changed, and the map went from AI/high to Human/high. The results are his; the file doesn't say who wrote the Human wording.
9. **The moral stated as an antithesis.**
   - Goodwill: "And it doesn't mean they get to come back over for coffee." became reasoning that goes somewhere: "since if they were all of those, they wouldn't have done what they did, and then they actually would be lovable."

## What he does to a list (he keeps most lists)

Joel, 2026-09-25: "Notice it still has listicles. Listicles are sometimes necessary, but it still tests as human (med. conf), because it has a lot of human tells".

1. **Telegraphic fragments become whole sentences to "you".**
   - Detox: "Misread as anxiety, insomnia, 'wine intolerance,' random congestion." became "You might feel it as anxiety or insomnia, or you might notice random congestion."
   - "Tyramine — aged cheese, cured meats, fermented soy. Migraine trigger." became "Tyramine — this amino acid is a normal part of the diet, but it's highest in aged cheese, cured meats, fermented soy. Can cause migraines, or if you're slow COMT, you might feel too amped up."
2. **An aside on some items, not all.**
   - Sleep log: "Bedtime (do you even have one?))", "Lights-out time (please please don't sleep with lights on)", "Estimated time to fall asleep (video-record it)", "Daytime sleepiness, mood, focus, and driving safety (you're only allowed to crash your car once per week)".
   - Items like "Meds and supps" and "Exercise timing" stay bare.
3. **A spec list becomes questions to the reader.**
   - "confirm the apnea subtype and severity: obstructive vs central/mixed, AHI/RDI, oxygen nadir, time below 90%, positional data, REM-worse apnea…" became "Is your apnea due to airway obstruction, or breathing regulation, or a mix? What's your lowest oxygen level (nadir)? … How's your body position? Does apnea get worse while dreaming?"
4. **One item gets a real person or a stake, in plain words.**
   - "drowsy driving" became "drowsy driving like my buddy Pooyan did".
   - "sudden severe insomnia" became "sudden severe insomnia (days without sleep is super dangerous)".
   - "violent dream enactment" became "violent dreams spilling into real life".
5. **Items as separate sentences with varied starts, the oddest one last.**
   - Borrow One Competency: "Perhaps a therapist or your grandmother really cared for you. Perhaps your teacher at some age was a great guide. Maybe an older sibling protected you well. Even Mr. Rogers could help here if you felt some nice vibes from his show as a kid. And there's always your future healed self if you can imagine that."
6. **A loose tail.**
   - "and so on", "whatever", "or anything else just like, obviously urgent".
7. **Bare items that were already fine stay bare.**
   - "Nickel — oats, cocoa, soy, leafy greens; eczema flares." is unchanged in the passing detox article.
8. **Two lists in one paragraph become two items each, with the rest in sentences of their own** (2026-10-03).
   - "ask it what it's trying to stop, or what it wants, or if it just has something to say. It could be your little one, mad that you took so long to come back, or a part of you that's trying to protect you, or the parent you inherited, or something from earlier today, or a bit of each." (66% AI) became "ask it what it's trying to stop, or what it wants. Maybe it just has something to say. It could be your little one, mad that you took so long to come back, or a part of you that's trying to protect you. Maybe it's that parent you inherited, or something from earlier today, or a bit of each." (Human, medium on his check). Joel: "P! failed b ecause it has 2 lists of 3"; "lists of 3 in general are an ai pattern".
9. **A list of three that doesn't need all three loses the item that matters least** (2026-10-03). Joel: "when there's no actual need for 3 items you can remove one of them, the one that matters the least. when you need all 3 items to be there for meaning, then split it up like i did."
   - "all of a sudden your phone, dinner, or the laundry feels urgent" became "all of a sudden your phone or the laundry feels urgent".
   - "What was missing? Some ability, or help, or someone protecting you?" became "What was missing? Some ability, or help/protection from someone else?"
   - "What can you learn, repair, or do differently now?" became "What can you learn or repair now, and how would you act differently in such situations?"

## What he adds

1. **A reaction to his own sentence.**
   - "Oh. That's what I was just saying."
   - "Mentioned this before."
   - "(which is paradoxical)"
   - "I absolutely agree."
   - "That's awesome I could notice it!"
2. **His stance, stated plainly.**
   - "IMO"
   - "in my testing (admittedly in 2024)"
   - "It has worked wonders for people I know"
   - "and it's also not a true cure"
   - "Causes all kinds of disease."
3. **The thing named flatly.**
   - Romance: "I think something is already wrong." became "that's called taking each other for granted."
4. **A concrete extension instead of an abstraction.**
   - "so communication should remain open beyond a simple interview." became "If our libidos later diverge, it's better to talk about what we'd do before either person is already hurt."
   - "…at bedtime" became "…at bedtime just based on the flirting you did 5 years ago."
5. **Self-talk or dialogue in place of an instruction.**
   - "look around and say you're hooked." became "look around and just take a moment to enjoy some free honesty: 'Oh! I'm hooked again! That's awesome I could notice it!'"
   - Added: "It shouldn't become relationship homework, either: 'Hey babe, Kim Anami told me to flirt with you more.'"
6. **Goofy, open humor, never dry.**
   - "Don't be a silly rabbit!"
   - "a patented 2 step plan"
   - "(NOT with a hammer!)"
   - "thrown in the round bin from the three-pointer line"
   - "Take note, young grasshopper."
   - "on a book tour with Oprah" (this and "young grasshopper" are from the mixed Nibbana master)
   - Emojis where a line begs for one.
7. **Everyday words for clinical ones.**
   - "fixed" for "cured"; "slow CYP1A2 folks will notice caffeine lasts longer in their system" for "slow CYP1A2 alleles produce long half-life".
8. **The caveat moved last, with "On the other hand".**
   - Two Pillars, his checks: the assistant's order was caveat first ("…if both people are falling apart, there is only so much anyone else can do.") and then "But sometimes a friend…". Even with "Community isn't magic either;" removed, that order was AI, low.
   - His reorder was Human, low: "I think that's rare.  But sometimes a friend who actually knows us both sees the pattern before either of us does. On the other hand, If both people are falling apart, there is only so much anyone else can do."
9. **Rough edges he leaves: typos, double spaces, missing periods.** These come from typing. They aren't something for me to imitate.

## In his words (verbatim)

- "stop giving each sentence exactly a job and start giving instructions that think about each other with parenthetical realizations, interesting/cute examples, self talk, and other human tells." (2026-09-21)
- "yeah it's again that marching order where the next sentence lands like code without a hitch." (2026-09-26)
- "you could say while skydiving and it would still have the same marching order predictable cadence with optimized structure." (2026-09-27)
- "Ai stuff overuses 'i wouldn't call that X' and the 3 part conditional syntax. Then you have the instruction manual features and the ending is bringing it all together in the most defensible way possible." (2026-09-26)
- "AI often doesn't have deep insight, and if it does, it tends to set it up too much rather than throw it in where it naturally arises." (2026-09-24/25)
- "it's not that you can't have an organized essay. it's that your organization needs to be not reducible to code … it needs to notice things naturally in the midst of the organization" (2026-09-26)
- "first of all the stuff ahs to make sense then we look at humanizing, you can't just move stuff around willy nilly to humanize it" (2026-09-26)
- "you're cheating a bit there by using my life story to hide your ai tells" (2026-09-25)
- "'doesn't get to decide' sounds SO ai … an optimal efficiency quippy formulation which humans just rarely use for non-humans." (2026-09-28)
- "i told you to stop saying 'Fine, Good, Great' as clauses before" (2026-09-28)
- "i'm not saying to ban made-up scenes, they can be useful, but you're overusing them here." (2026-09-28)

## Minimal-fix lesson 1: the boundary question (2026-09-28 22:12)

**My draft** (100% AI, 97 words): "Set one boundary. Say no to something that's costing you too much (money, time, whatever it is). Handle that task you've been putting off, or the money mess, even if all you do today is open the envelope. …"

**His minor changes, AI/medium on his check:** "So set one boundary.", "Throw the moldy bread in the trash.", and "or the tax man, or your DUIs in Maryland" in place of "or the money mess".

**His one change, Human/medium on his check** (100% Human, 121 words, on mine): "So set one boundary. \"What's a 'boundary'?\", I might be asking. That looks like saying no to something that's costing you too much (money, time, whatever it is). …"

Joel: "look how i flipped it to human med conf with only one little change that broke up the marching order". The change has two parts:
- a plain question in his own voice about the jargon word the list had just used;
- the next item rewritten as the answer ("That looks like…").

That turns a run of commands into sentences that react to each other. The summing-up last line stayed and still passed. The run was the problem, not the ending.

**What it does in the section** (my checks, 2026-09-28):
- Joined to the 2 a.m. paragraph, his paragraph tests 100% AI, in either order, with or without "So".
- Followed by my paragraph 2 draft s2c, the pair is 37% AI (219 words). The flagged window is his last line plus s2c's first four sentences:
  - a topic-sentence opener ("Some of it happens where nobody else can see.");
  - two parallel "When…, don't…" lines;
  - an "is a kind of love, … but it's not the whole thing" line.

  It turns human again at s2c's question ("\"So what else is there?\" Well, …").
- My try at an opening that reacts to his last line ("Will they, though? Maybe not right away.") failed alone. It also pulled the whole pair to 100% AI.

## The test after reading (2026-09-28)

I wrote three versions of the guide's first "Make the Protector Visible" paragraph (the six-act list and its reason) with these moves:
- the guide's items kept;
- asides on some items;
- a plain reaction;
- "Clean your room!";
- no summing-up antithesis.

All three were 100% AI (111, 97 and 100 words). Knowing the moves isn't enough yet. My sentences still carry the signal the moves are supposed to remove. That's the gap the minimal-fix lessons are for (`experiments/MAKE-THE-PROTECTOR-VISIBLE-20260928.md`).

## Joel's fixes, 2026-09-29 19:14 UTC

**The h2.** "Keep Your Word how did you come up with that for the heading? I don't see anything about keeping your word here… This is about making the protector visible, not keeping your word." He changed it to "Not Every Hero Wears A Cape". Claude had picked "Keep Your Word" only because it was the one of six that passed Pangram (see the gate, "Headings").

**P1 under the new h2.** "on this version after title change, last sentence was ai (yes, and it does sound like it)". His fix, "also more in line with the guide":
- "So set one boundary." became "Set one boundary.";
- he added "The only reason you're in it anyway is because of a lack of self-love, and you can build that now." between "…which is not a small thing at all, I know." and the last sentence.

The flagged last sentence stayed word for word. What cleared it was a new sentence in front of it that reasons about the reader instead of listing another act. (Pangram, Claude's checks: the section is 100% Human, 387 words.)

**P2, his logic corrections.**
- "You said 'they're right' not 'if they're right' which lost the meaning." A condition dropped by sentence shape: "They complain about something, they're right, and you say so."
- "it's not 'proof you love them' it's evidence you're safe and accepting of them. The original guide said it's 'evidence of love' -- that's true (evidence is not proof). Although I'd be more clear about exactly what it's really evidence of. Love requires that much, but that's not love."
- "With a little bit of logic you should have figured that out so there's a lack of logic going on in the sentence reviewer i guess." That led to the grounding reviewer (`reviewer/grounding.txt`).

**P3, his version** (Human/medium on his check). He kept wA2's first two sentences and cut the rest: the meal, the cancelled obligation, "Take one act from all this…", the rehearsal and the last sentence. Then he added: "But yeah, bonding starts somewhere. And this is not to say you've never done anything to care for yourself. If not, you'd be dead right now. But we're making additional acts of care intentional now as a base for love to grow."
- His reasons: "line it up better with the guide", and "you were conflating protection from nurturing (giving a meal is nurturing, throwing away moldy food is protection, and we already have that in P1). So I threw away the duplicated examples of protection, and you should have seen to do that also."
- What it teaches:
  - one guide paragraph per paragraph (the merge was wrong);
  - check every example against the job it's offered for, even when the guide's own list supplies it (the guide files eating under the Protector twice);
  - cut examples that repeat earlier ones instead of rewording them;
  - end on a plain statement of what the acts are for ("a base for love to grow"), not on a technique.

## Joel's fixes, 2026-09-30 03:29 UTC

**P4's ending.** "i like how you're integrating prior examples in parentheticals i feel that's human-sounding (in P4). The last sentence in p4 was not what i was expecting/hoping for. A question isn't necessarily a bad way to put things." His ending in place of "At first it'll probably come out sounding like a question.": "Then put yourself in their shoes to see how it sounds, and go back & forth like that a couple times until both sides feel good about it, or good enough." (Pangram, Claude's check: P4 100% Human, 100 words.)
- Keep doing: a callback to an earlier example in parentheses ("(like with the envelope)").
- A practice paragraph ends on the next move of the practice, not on a prediction of how the reader will sound. Mine also quietly judged sounding unsure, which he doesn't.

**P5, his final** (Human/medium on his check), built on z1 (44% AI, its last two sentences flagged):
- "If you did it" became "If you did the protector action(s)". The paragraph before had ended on a hard conversation, so the nearest "it" was the wrong one ("for P5 the first 'it' is unclear referent… You explained in the next sentence"). No reviewer caught it: grounding and cold read, 4 runs, all read "it" as the act. Name the thing at a paragraph's start; `tells_lint.py` R1 now warns on "did it"-type openers.
- "doesn't mean it failed" became "is information to learn from. It doesn't mean failure, because the process is dynamic." That turns the no-relief case into something to use, and gives a reason.
- The flagged span shrank. "Fear is the first guess, and it might be right, but maybe you didn't know how, or weren't sure what you were going for." became "Fear is the first guess, but maybe you didn't know how or why." The hedge "and it might be right" went, and the two reasons folded into "how or why".
- He kept "Being worn out can stop you too, and sometimes whoever said they'd help couldn't make it." word for word, and added a warm aside with an emoji: "Hey, we've all been there. 🤗"
- My rewrite of the same span (z1b, his causal chain) had gone to 100% AI. His fix cut words where mine added reasoning.

**The relationship line in P1.** He rethought the guide's "Leave a relationship that keeps eroding safety" from his own experience: someone can feel less and less safe with a partner for reasons that come from inside them, so "leave it" is too simple ("it just depends on how things were going for [them] at the time"). His wording: "meditate on why it makes you feel unsafe, and what keeps you in it, and whether either may be due to a lack of the healed inner child/inner adult relationship." "Although that might deserve its own section, idk."
- In P1 it tested 100% AI (132 words), and so did a version with a danger line (150). On its own, as a paragraph in Also Look Outward, it's 100% Human (58; 61 with the fixes). The same words read differently in a list of visible acts than in a section about looking at a relationship.
- He asked whether I could have seen the problem. The article already teaches that a hook can be old material; "leave it" acted on the less-safe feeling as settled. The reviewer passed it because it matched the guide. MISFIRES now tests instructions against different readers (`reviewer/grounding-validation/RESULTS-20260930.md`).

**His Substack note.** Embedded by bare URL in Also Look Outward, because "it reads also more human and captivating when it's a back-and-forth discussion with other substackers rather than just the narrative voice all the time". Other voices in the piece are a humanizing move of their own, and they're real, not staged.

## Joel's notes, 2026-09-30 04:44 UTC

He agreed with two reviewer flags on his own lines and asked me to write the fixes ("i know what i'd say now but i want to see what you'll say"):
- **P4's "both sides."** It was "…until both sides feel good about it, or good enough." It's now "…until both sides feel good about it, or good enough, as long as what you needed to say is still in there." The clause keeps the "no" through the rehearsal and leaves his sentence whole. 100% Human alone (112 words); the reviewer: every line OK.
- **P1's "sweet things."** It was "Your little one has had enough grown-ups who said sweet things and then did nothing, so this is how they start to believe you." It's now "Maybe your little one had grown-ups who said sweet things and then did nothing, and maybe you've done it too, so this is how they start to believe you." His phrase stays. The history becomes a "maybe", and the reader's own broken promises are the case that fits almost everyone, including readers whose parents did love them. 100% Human alone (98 words); the reviewer: every line OK.

**Scope** (his words, now the default push level): "in general we should assume the user doesn't want to massively increase the article size, but small increases or decreases may be fine if warranted. for any uncertainty ask the user."

## Joel's notes, 2026-10-01 04:53 UTC

- **The 😉 after "you might not be some people."** He tried "a few different more appropriate emojis" there, "but all tested as ai", and put "people (hehe)." instead, "which tested as human". On my check (turn 10, try 1): the paragraph 100% Human (74 words), the section 100% Human (232).
- **The 😄 after Elmo.** "same trick for the elmo emoji, i used :) instead and it passed as human." On my check: 100% Human alone (68), and the section with its h1 100% Human (163), where the 😄 had made it 30% AI.
- **The lesson in both:** ASCII emoticons and "(hehe)" read human where an emoji reads AI ("ai slop generally doesn't use ascii art like that"), and "lol is different from hehe, it's more wry." Pointers, 😉 and gratuitous emojis are banned (E97; `tools/humanization/EMOJI-LIST.md`).
- **P8, the Fred Rogers scene.** "check what the exchange was really [...] why not just check what was actually said for improving the vagueness?" The paragraph now carries the film's lines (E98).
- **P7.** "P7 proposal is good." It's installed as proposed.

## Joel's notes, 2026-10-01 13:57 UTC

- **P9, finished.** "P9 yes, it absolutely does make sense to finish that thought otherwise it's unclear." And of the proposal: "I like the proposal, but the reviewers are right that the other side and nothing to win are unclear." His P9 keeps my turn-10 text through "the right way", adds "The resentment can be purely visceral: being doubted after you've tried feels unfair, but there's nothing unfair in them going over your track record.", keeps the next two sentences, and ends "Be careful not to take the accusation as proof your love really is conditional, when it could just be another part talking." Human, medium on his check; 100% Human on mine (145 words, try 1). What it teaches: a plain word for a figure, no wrap-up clause, and a direct caution where I had an "if you do, you might" consequence (E100).
- **Emojis.** His own list, his preference for dark skin tones, and when one is warranted (E101; `tools/humanization/EMOJI-LIST.md`).
- **The merge.** "yes you can merge the lane so it shows 10 altho i don't quite understand your jargon about main and lanes and all that."

## Joel's fixes, 2026-10-01 14:49 UTC (community article, section 2)

He rewrote two argument paragraphs of the published section himself, after 34 of 35 Pangram checks of system drafts had failed. Both of his came back 100% Human alone.

- Before: "Communal ownership therefore needs named stewardship, visible duties, consequences for chronic freeloading, and enough relational capacity to confront the problem before resentment becomes the real government. A community cannot run on the assumption that removing bosses removes passivity, selfishness, theft, or learned helplessness."
  After: "Communal ownership entails folks taking on visible and named stewardship duties. It requires knowing what to do if someone is leeching off the group and how to deal with it. It requires developing healthier forms of relationships. No, taking away the idea of a boss does not make everyone less passive, selfish, steal less, or try to act helpless." (One spelling fixed: he wrote "leaching".)
- Before: "The desire to return to a natural way of living together has outrun the knowledge. People know they’re lonely and exhausted. They usually don’t know why so many earlier communities failed, why the same conflicts keep returning, or how quickly beautiful land becomes irrelevant once money, children, jealousy, and ownership enter the picture."
  After: "People want to go back to the old way of living, but they have no idea why it failed or what to do when someone wants to own land, they run out of money, a baby is born or someone thinks they own something. They just know they are tired and alone and want to change it."

What he did: the list became one requirement per sentence, with "It requires" repeated; abstractions became happenings ("chronic freeloading" became "someone is leeching off the group", "children" became "a baby is born"); a spoken "No," answers the hope that removing the boss fixes people; and the polished lines went ("before resentment becomes the real government", "how quickly beautiful land becomes irrelevant"). Of the published line "Suddenly “maybe we should form a village” sounded less like a 1972 leftover and more like a backup plan" he said: "the 1972 line is witty altho it's kind of an obvious ai quip".

## Joel's answers, 2026-10-02 23:49 UTC (community article, section 4)

- **P21: a meaning change he keeps.** Emulate's "While there may be some pure learning that could come from having several altered members figure out what rules and boundaries are needed on the spot, it's not something I recommend" lost the published irony, and the whole-article check and the trace both flagged it. Joel: "the reviewer is correct that emulate lost the irony. so it did change the meaning slightly. although the new meaning is actually better for this. and it does read as a concession which is warranted yes i think so." A flagged change goes to him; he can take it.
- **P5: "These four parts", not "These four categories".** "they are the four parts from the prior section. the actual article uses an image." The diagram under the heading names them; the review prompts had shown it as "[an image]". And "plant medicine" declined: "plant medicine isn't the only kind of medicine."
- **P13:** "it should say staying, not still", with the missing "what": "while staying devoted to following what they've decided on so far."
- **P28:** "yes drop often": "And if they do, it's still something that needs a sober thinking-through."

## Joel's fixes, 2026-10-02 21:16 UTC (community article, sections 3 and 4)

He rewrote seven paragraphs of the section 4 candidate and one of section 3, and checked each on Pangram himself. With them, section 3 reads 100% Human (563 words), and section 4 does after two more rounds on the paragraphs his changes exposed (1,519 words).

- **Section 3, P7.** Before: "...but because it's inner being shaped by outer as a condition of membership..." After: "...leave the inner life mostly private or ignored. ... but because it's the inner world being shaped by the outer as a condition of membership..." My two-word version ("the inner being shaped by the outer") had passed alone and flipped the section to 13% AI; his rewrote more of the sentence and passed both ways.
- **Section 4, P5.** Before (Emulate's): "how people deal with jealousy is going to be intertwined with how people run the community, how people use common things, how people parent, how people deal with medicine etc." After: "These categories leak into one another almost immediately. Governance can end up slyly incorporating personal tensions like jealousy. Those who have positions with more control of shared resources will automatically be affected by that psychologically (power corrupts, as they say). Those who know medicine tend to have another type of god complex since they may make life or death decisions for people routinely. How folks choose to raise children can expose values the founders never discussed. And myriad other categories arise, of course." His reason: "Emulate started implying that jealousy intertwines with everything rather than each thing intertwining specifically with something. ... this vagueness has to be rejected."
- **P7.** Before (the published quip): "which can become equally sacred—just with longer meetings and fewer robes." After: "When agreements get frozen, religious communities tend to call the frozen version doctrine. Secular communities on the other hand often call it “the process,” which can become just as sacred." His note: "no matter how i worded fewer robes and longer meetings it got flagged as AI, which yeah, it does look ai after ai colonized it."
- **P11 to P13.** Emulate's "not the other way around" went ("Idk if anyone thought the child was goin to reaprent the adult lol"); "Guide" for "Guru/Leader", as in his Inner Child article; reparenting "built on somatic regulation first", with his own view that body-before-mind "symbolizes the adult/child relationship to me"; the Abhidhamma line cut ("not needed"), and the published "devoted enough to practice them and secure enough to disagree" replaced: it "looks super highly polished", and it failed once the paragraphs before it were his.
- **P26.** "it may be impossible because of government requirements" became "it may be impractical in some locations because of government requirements": the original was "a bit too imprecise and strong on the impossibility".
- **P28.** The published claim was wrong: "people do come back from ecstatic visions with those kind of practical ideas, i've seen that, but they are often not quite as amazing as they sound to the experiencer." After: "It's rare to see someone come back from an ecstatic vision with news of how to revamp the community’s policies ... And if they do, it's often still something that needs a sober thinking-through."
- **P29.** "when one person owns the land and has the final say" became "owns the land or has the final say" (Emulate had narrowed the published "ownership that gives one person the final say").

What his fixes teach:
- Specific pairings that become a general tangle are a changed claim, to reject, not a lighter version to offer.
- A polished quip AI has colonized may fail in every wording; keep its point and let the form go.
- Making one paragraph more human can expose the next one; recheck what follows.
- A balanced "X enough to A and Y enough to B" pair reads as polished AI, even when Pangram passes it.
- Abstract agents are one of the top tells to weigh, not banned: worst when highly polished or overused (his words, the same day).
- The published text can be wrong about the world; his correction replaces it, and the stance check, which holds a rewrite to the published essay, reports it to him as information.

## Joel's fixes, 2026-10-02 00:52 UTC (community article, section 3)

He rewrote three paragraphs of the section 3 candidate and fixed one proposal. Each came back 100% Human on Pangram, alone and in the section, once his own characters were kept.

- **P4 (a proposal).** Before: "...but the meeting agenda is the one place the group lets you push for something and win, so the anger goes there, trying to get some justice."
  After: "...so the angry communard goes there, trying to get some justice."
  His reason: "the usage of abstract concepts or feelings as agents is one AI tell because it permits high efficiency of words. I minimal fixed it." The proposal read 43% AI alone; his fix read Human.
- **P6.** Before: "But in the early days, the community’s spirituality and social life was heavily influenced by Stephen Gaskin. ... It’s one thing to talk about a universal consciousness. It’s another to struggle to escape one man’s opinions."
  After: "But in the early days, the community’s spirituality and social life followed the founder, Stephen Gaskin. ... This is how it often goes: folks talk about oneness with the universe, while one man defines what the universe is."
  His reasons: "heavily influenced" became "followed"; and Emulate's "one thing ... another thing" "is not quite showing that the truth was Y not X".
- **P7.** Before (Emulate, with my fixes): "Both approaches fail for symmetric reasons. Secular approaches fail to address the inner life (while distributing power), whereas spiritual approaches do address the inner life but concentrate power."
  After: "The two failures mirror each other. Secular groups distribute power but leave the inner life largely private or ignored. Spiritual groups attempt to address the inner life, but because it's inner being shaped by outer as a condition of membership, we tend to find both real-world and spiritual power concentrating around whoever defines the path."
  His reason: "emulate lost the meaning of the original. Here's the human fix which also enhances understanding". He put back why the power concentrates: the inner life is shaped from outside as a condition of membership.
- **P9.** Before: "I want a way to work in depth that isn’t run by a guru, and a way of being in a community with distributed authority where people don’t come in pre-healed, that also has peer practice..."
  After: "I dream of a way to work in depth that isn’t run by a guru, and a way of being in a community with distributed authority. A place where people who've done the healing first can join without pretending they're fully finished, and that also has peer practice and enough play that it doesn’t become a permanent repair shop."
  His reason: "Emulate changed 'without pretending that people arrive emotionally finished' into 'where people don't come in pre-healed' which is nearly the opposite of what i want. I DO want people to come in largely pre-healed ... Did the reviewers not look at the article?" On "I want": "'I want' is generally banned as a way to introduce my opinion, as it sounds very AI. But in this article it does work because we are talking about a community that I want." He still chose "I dream of".

What his fixes teach:
- An abstraction or a feeling doing a person's job ("the anger goes there") reads as AI; give the job back to the person ("the angry communard").
- A contrast has to say which side is true. "It's one thing to X. It's another to Y" sets two things side by side; his "folks talk about X, while one man defines Y" says what was really going on.
- A paraphrase that drops a "without pretending" can flip a stance. Check a stance-bearing sentence against the whole article, not only its own source paragraph (the gate's whole-article stance check).
- His characters are part of his text: with the same words, his P9 read 100% Human with his straight apostrophes and 100% AI with curly ones.

## Joel's notes, 2026-10-01 15:59 UTC

- **P11, his.** "for P11, this one is human and works better". He kept my last draft's first, second and last sentences and rewrote the third: "And actually, not to beat a dead horse here, but every age of you was stuck with whatever it had then, even the adult you were last year. Hindsight being 20/20 doesn't change that." Mine was "Every age of you was stuck with whatever it had then, and that includes the adult you were last year, even if they seem like the one who should have known better." Every checked draft of mine was 100% AI; his is 100% Human on my check (83 words, try 1). What it teaches: say so when you're going over old ground, and give an objection its own plain sentence, in the words people use for it (E104).
- **P10.** "P10 proposal is good." Installed as proposed.
- **Emojis.** "your emojis are fine" (🫶🏿, ❤️, 😇). 😊 goes on his list, "altho the angel emoji was prob better there", so 😇 stays. "the breathing easier emoji was good though, otherwise, "breathing easier" sounds flat and it's too abrupt to jump to the next sentence for me, so put that back" (E102).
- **Proposals.** "on the proposals please highlight the new part that's proposed so it's easier to read" (E103).
- **His WhatsApp favorite.** "https://emojipedia.org/distorted-face that's the one i meant" (E105).
- **Merging.** "hm ok i'm not sure when the merge should be i guess it should be when i say "continue" right?" So a "continue" is his OK to merge at the end of that turn.

## Joel's notes, 2026-10-01 17:50 UTC

- **Love Doesn't Wait P12 and P13.** "P12 proposal accepted, P13 proposal accepted". Both installed as proposed; the section with them is 100% Human (1,236), try 1.

## Joel's notes, 2026-10-01 20:51 UTC

- **Make a Simple Vow P1.** "the last line is like a semi quip, but actually it should say that it does really help to imagine holding a baby in your arms to make the vow feel real. Imagine you just had a baby, how would you feel? Would you look at him/her with adoration and joy? Carry that into visualizing yourself with your own inner child." Installed in his words in place of the swing (E106). 100% Human alone (73), try 1.
- **P3.** "for P3 i'd change mean to feel. So it's not like we are accusing people of lying about loving their inner child, but they might be faking it til they make it. Which i did advocate before, but i think that was the protector part? I don't think faking love is a good idea because that's not an action that speaks for itself, it's a feeling that we have to trust is there." And "I think P3 proposal is over-explaining why this is important to be honest about love before promising honesty. I'd cut P3 to:" his 49 words, installed word for word (E107, E108). His memory is right: "Fake it til you make it" is in Borrow One Competency at a Time, about the Protector's acts.
- **P5.** "For P5 actually it sounds too biased towards adulting. P5 proposal is good but the base needs to be modified. I'd say:" his text, word for word, ending on the proposal (E109). 100% Human alone (105), try 1.
- **Proposals.** "P2 proposal is good", "P4 proposal is good". Both installed.
- What his fixes teach: a feeling can't be faked the way an act can be practiced; a proposal's why has to be one a reader would miss; and the little one isn't only a problem to manage.

## Joel's notes, 2026-10-02 00:16 UTC

- **Make a Simple Vow P1.** On the reviewers' points: "yes as i said, i'm changing the "with or without a visualization" to more of a guidance (with or without X is not quite guidance) about the usefulness of the visualization. I think we have said previously people can take the parts that work." (The article has it: "Take the parts that work, and innovate on the rest.") On a reader who can't feel love for a newborn: "we don't need to throw it in their face by explicitly saying so, and then we do address that possibility quite soon after." On grief: "the point is not whether they wanted the baby but, if it's here now, how would they feel when they see it and hold it?" Then his rewrite, installed word for word: "As many real-life parents know, your heart really explodes in such an unexpected and wonderful way when you hold your newborn baby for the first time (happened to me!). And if you're not yet a parent, it can really help to imagine …". 100% Human alone (111), try 1 (E114).
- **The line after the vow.** "Oops, you put in a referent to something sections ago nobody will remember ... I'd simply remove that reference to those grown ups." Cut; the cut line read as a summing-up (65% AI with the vow, try 1), so it opens "Notice it" now, 100% Human with the vow on try 2 (E111).
- **P4.** "cut out the "or just keeping an appointment, eating, or going to bed." that sounds almost ridiculous". Cut; 100% Human alone (76), try 1 (E112).
- **Give the Vow a Physical Reminder.** "you lost the meaning of the original with the last 2 sentences ... I would simply cut out the last 2 sentences entirely. I don't think people will be confusing the stuffed animal with an oracle. And if it does seem to connect them with their inner child they can talk to it if they want to like that, i don't see that as a problem either." (E113.) True details: "I do not keep an object, note, or pet. Some people do, and it seems to help them. Especially i hear people like to keep childhood photos ... I actually used my son (i shouldn't say "used") to reconnect with my inner child, and I think that's very common for parents." His merged P1 ("human, low conf") and his P2 ("human, low conf"; "those 2 combined are human med conf"), installed word for word, with his note's quote marks made a matching pair. Each is 100% Human alone (75, 51), try 1; together without a heading 100% Human (126); under the guide's h3, 100% AI (132). The heading goes to him.
- What his fixes teach: a pointer back names its thing or goes; an example has to show what it's said to show for the common reader; a caution nobody needs gets cut, not blurred; and a point his own words already settle doesn't go back to him.

## Joel's notes, 2026-10-02 01:08 UTC

- **The Physical Reminder heading.** "changed the title and now it's human: Remind Yourself", with his two paragraphs. Installed.
- **E111.** "it's not that aref back has to say what it means, but it depends how far back it's referring to. nobody will remember something sections away. If it's from the last paragraph and it's clearly referring then it may be fine." The gate's line and E111 now say distance; three of my pointers sections back came out or wait on their section, and his P3's goes to him as a proposal.
- **Repeat checks.** "it seems like you're pangram testing stuff i already told i pangram tested? that's not necessary. only if i don't tell you i tested it. if you want to test combinations i didn't test, you can." (E116.)
- "continue".
- What his notes teach: a reader can't use what they don't remember, so distance decides; and his own check is a result, not a claim to verify.

## Joel's notes, 2026-10-02 03:15 UTC

- **Scott's quote.** "he said that, altho i'm not sure word for word but yes that's how i remembered it." It stays as his source has it.
- **The vow's P3.** "agree with proposal". Installed; with Remind Yourself the section is 100% Human (587), try 1.
- **Who is feeling fake (E118).** "yes i used to think that. but what P3 is really missing is who is feeling fake? if the little one, it could be persistence. if the adult feels fake, more fake sessions could be more damaging than just not doing the fakery in the first place. your reviewer should have caught that." The grounding review now asks whose feeling a piece of advice answers, and tests the advice for each.
- **His new P3.** "new p3, tested human (i also added myown exp)". Installed word for word and not re-checked alone; the h1's opening with it is 100% Human (207), try 1.
- "continue".
- What his notes teach: advice for a feeling says whose feeling it is, because the little one's remedy can hurt the grown-up; and a reviewer line that names a split like that is a question about the advice, not an extra.

## Joel's notes, 2026-10-02 18:56 UTC

- **His P3.** "i said unintentional so it's not blaming"; "it sits "correctly" next to unintentional ... there's a diff between me blaming someone and me pointing out how their inner child may blame them. It's not my place to blame, but their inner child does have that right to say what they think about their treatment." His P3 now has "(from the inner child's view)"; it passes on his check (E119).
- **His P4.** "the script part iw ant to keep it's important"; "embarrassing crying fit so we can encompass anger and crying and embarassing us, from the original"; "more specific since we're not talking about bad behaviors". Human, medium on his check (E120, E121).
- **His P6.** ""that call" it's quite obvious as a referent to lettinjg the phoen ring right? fix the reviewer"; ""new grown up can start outside your head" is what i would have flagged as unclear"; his version opens "But with the borrowed adulthood trick," and passes on his check (E122).
- "continue".
- What his notes teach: ask whose view a judgment is before calling it a contradiction; keep the guide's word for what kind of thing something is; let one example carry as much of a list as it can; and a cold reader that flags an obvious referent is the one to fix.

## Joel's notes, 2026-10-02 22:44 UTC

- **P1's list.** "i agree to add that part of you trying to protect you in p1". In the ledger; the list with it was 66% AI alone, so it waits for a version that passes.
- **The two protectors (E123).** "you're right that could be confused for the adult protector, which is the one we are consciously building rather than the inherited protector that came from trauma responses". In the briefs as context; the text calls it a part of you that's trying to protect you.
- "continue".

## Joel's notes, 2026-10-03 00:00 UTC

- **P1, his minimal fix.** "P! failed b ecause it has 2 lists of 3. I did a minimal fix and now it's human med conf". In word for word; the h1 with it is 100% Human (673).
- **00:01.** "lists of 3 in general are an ai pattern". The linter fails two in one paragraph and flags one (E125); his bans, with this line, go into every writer prompt.
- What his note teaches: a list of three is the pattern itself, not only when it's long; and the first fix is the smallest one to that structure.

## Joel's notes, 2026-10-03 01:06 UTC

- **Lists of three, the order of fixes.** "when there's no actual need for 3 items you can remove one of them, the one that matters the least. when you need all 3 items to be there for meaning, then split it up like i did." (E126)
- **His fixes.** "in these cases i'd just remove dinner"; questions 5 and 6 of Love Doesn't Wait P12 in his words. All in, and they pass.
- "continue".

## Joel's fixes, 2026-10-03 04:31 UTC (Start With Whatever Showed Up P3–P5)

- **P3's last line cut.** "i'd remove the last line in p3, doesn't it seem redundant? and plus like you said then it's taking over p4."
- **Four paragraphs of mine became three of his** ("I fixed p3-p5 for you, it reads much better now and human high conf as a whole"):
  - "Then wait. Don't grill the silence, and if nothing comes, don't answer for that part just because you'd set this up as a healing session." became "Then wait and listen patiently. If nothing comes, that's fine for now. No need to answer for that part just because you'd set this up as a healing session."
  - "Even then, you can notice what sets the reaction off, and what it has you doing instead. Maybe the laundry suddenly feels urgent… Whether that's what the reaction is trying to stop is only a guess, and it might not be protecting you at all." became one sentence at the end of his P4: "Even without the answer, you can notice what sets the reaction off, and you can understand what the reaction is propelling you toward, and away from."
  - "Or you might get an answer, as a voice or just a hunch." became "Or if you do get an answer, it could come in different forms, like as a voice or just a hunch. It's often more like a feeling. Maybe grief or anger. If so just listen and be present for it if that's what it wants." The feeling comes before the advice tests, and "Those checks are only for advice, though, and if what comes is grief or anger, you'd listen whether it passes them or not." is gone.
- "idk why you had a hard time this time because normally your writing is better than this?" (E130)
- "continue".

## Joel's fixes, 2026-10-03 16:16 UTC (the altered-states paragraph)

- **The marching order.** "P3, yeah it's the marching order that's why it's AI. you can't see that? and it has nothing to do with the rest of the guide's order matching, pangrram checks it alone." (E131)
- **His minimal fix of try 3, with my proposed last sentence** ("you suggested ending sentence is good"): "like on mushrooms" became "like on MDMA", and "All of a sudden your little one is right there, and the love or grief that sounded like therapy talk is just obvious." became "All of a sudden your little one is right there! Oh my gosh! And the love or grief that sounded like therapy talk is just obvious." Human, medium on his check; the h1 with it 100% Human (1,078). "i'm not saying to make oh my gosh into a rule but just see how it can break up the marching order of code instructions translated to english ok?"
- **The parked question.** "you just simply look back and you know... i don't understand how that would be hard to know? the only thing is most people don't even think like this until someone brings it up, that they may actually have state-dependent awareness." (E132)
- "i can fix the apragraph easily but i'm surprised you can't? what are you trying exactly and why?"
- No "continue".

## Joel's notes, 2026-10-03 21:18 UTC (the marching-order check)

- "yeah i'm not saying my version of it has no AI tells, but the biggest one, the marching, was mostly fixed by that."
- **What breaks the march in his P4 and P5.** "On reading P4, there is a break from the marching though, \"or however you'd actually say that\" sentence is a break. And actually the rest of it is not really instruction manual style. \"Wait and listen. If nothing comes, that's fine for now...\" is a break from the instructions, and then it comes back to instructions after that, so it's really not one long instruction text." "P5 has more reflection than general AI prose. It's stopping again with considering what something might feel like, and then stopping the instructions at \"just listen.\" and then restarting right after that." (E133)
- "maybe these are not quite reasons to disregard the marching order check and rather ways to optimize it (altho we should be sure this pattern actually holds for optimizing it, so let's look at other examples)": tested blind on 100 paragraphs, and it holds (MARCH-READER-TEST-20261003.json, v2).
- "continue".

## Joel's fix, 2026-10-04 01:03 UTC (the sequence's P2, in four steps)

- "when you can't get something to human iw ant you to explain the AI tells that your reviewers found. if they found them, then why couldn't you fix them? are you seeing the march there?" (E134)
- **Step 1, the third sentence.** "Let it say the whole thing, and tell it you heard it before you answer." became "\"Tell me what you remember, I'm listening.\" works well here." (and "Maybe you have fooled yourself" became "Maybe you've fooled yourself"): "that made the first part human, then the rest after was ai".
- **Step 2, the next sentence.** "As the Nurturer, you're there to take in what that part has been carrying, so if you catch yourself arguing back, you can let that go." became "It puts you into the role of the Nurturer, which alleviates the instinct to argue back.": "that became human, but the rest still ai".
- **Step 3.** "Peek-a-boo!" after "Usually your little one only comes forward after that part feels heard.": "which did the same thing, then everything after that was ai".
- **Step 4, the last sentence.** "It can look convincing, too, with the right words and maybe even tears, while nothing underneath feels any safer." became "Even if you didn't win an Emmy last year, that can look convincing, with the right words and maybe even tears, while nothing underneath feels any safer.": "100% human, med conf".
- "so this one was a stubborn little paragraph, because it really did have a lot of AI shape ... i can see why you might have given up after a few tries. so maybe we need to brainstorm how to approach it smarter so you understand what you're doing and don't think of it as just 2 random guesses ?"
- "your heading is fine." On the parked questions: "one small step has been talked about a lot in this guide"; "if nobody safe comes to mind, go back to the first para in Borrow one function at a time, right?"
- On length: "it's quite possible this guide could be shortened, if you see repetitive stuff that could be cut or merged lmk because AI stuff tends to be more verbose, but i am trying to get it to explain the innersignal therapy map basically."
- No "continue".

## Joel's fix and notes, 2026-10-04 01:33 UTC (the sequence's P3, and how to break the march)

- "hm i see, you can't mimic me for some reason. well, it's not about better explaining. it's about breaking up the instruction manual flow, which requires some kind of within-the-thought reflection or jumping or something like that because people will gloss over fast if everything is one long stepwise instruction sheet. you don't need to know what i would say, you just need to think like \"how would a human think right here, how would a human author re-engage the reader here?\" but yeah i mean obviously you are also trying to mimic my voice not the voice of Shakespeare, right. but my voice also isn't completely unique … close is good enough." (E135)
- **His P3, one insertion** ("just one insertion that anyone could have thought of"): "A new roommate doesn't win you over with a speech on move-in day." became "A new roommate doesn't win you over with a speech on move-in day (hopefully, right?)." Nothing else changed. Turn 26's version was 100% AI (5d85e7fe); his is 100% Human, high (81, 3af6f4e3), checked on turn 27 since he hadn't said he'd checked it.
- On shortening: "yes i agree with your shortening sugggestions." More from the map updates is coming, to be merged in and deduped.
- No "continue".

## Joel's notes, 2026-10-04 03:58 UTC (the sequence's P4)

- "yeah that reads much more natural now and more inside the thought." (of P4 as installed on turn 27)
- "that's cool you're learning by yourself."
- "i liked the proposal at the end yeah": the cold read's clarity fix of P4's third sentence, which had passed alone but put a 7% AI window into the h1. It went in less its "to see" (the h3 100% Human; the h1 3% AI, a window in Two Common Protective Patterns P2).
- "continue".

## Joel's fixes, 2026-10-06 16:55 UTC (community section 5, after his check in Pangram's web app)

The web app read v60 at 9% AI (the heading with P1, P19's last two sentences, P25's last sentence with P26's first); he fixed those and more, and pasted the section as fully human. The API reads his version 100% Human too (batch 45, one window at 0.05). Before → after, his words:

- **The heading.** "The Medicine Part, Without Pretending It Isn't There" → "The Medicine Part - Yes, I'm Naming It". "oh yeah that heading looks way ai for sure. always trying to do an x not y statement ... humans don't do x not y as much."
- **The opener.** "Key here is that most of the writing on communities hasn't caught up with psychedelics." → "Most of the writing on communities hasn't caught up with psychedelics." "'Key here' can't be how you open a section. that's referring to something."
- **P19's end (flagged in both the web app and the API).** "who is a sexual predator, who is financially dependent on people coming back to them specifically, or who is simply wrong. And the more deeply someone is opening up, the more it costs not to know which one you're getting." → "maybe even a sexual predator, or financially dependent on people coming back to them for more feather-waving. And the more deeply someone is opening up, the more it costs not to personally know who's running their ceremony." The parallel "who is … who is … or who is" list became a looser one with a hedge ("maybe even"); "for more feather-waving" calls back to P11's "the person with the feather"; the abstract "which one you're getting" became the concrete "who's running their ceremony". He also opened it "My basic issue".
- **P22's first sentence: advice, not an observation.** "This is not to say that peer led ceremonies are ever casual." → "Just because it's a peer-led ceremony doesn't mean it's ok to be casually irresponsible." "it sounds like it's making an observation about peer-led ceremonies in general but it is supposed to advise".
- **P25's joke (flagged).** "learning to listen without fixing, … regardless of how mindblowing the geometric shapes they saw were." → "learning to listen without imposing their solution, … regardless of how many self-transforming fractalized machine elves told them they are the re-incarnation of King David & Elvis.😂" A specific, silly image for a generic one, and the emoji so the joke lands glad.
- **P26 (flagged).** "Integration is everyday life. The ceremony opens something up in you. Look at your life in the weeks after the ceremony and see how things have changed, if at all. Look at your relationships, your behavior, your sleeping habits, your decision-making, and how well you can deal with frustration without declaring a new spiritual emergency." → "Integration is a term thrown around so much that I'm not sure if it still has meaning. But basically, it's your everyday life. The ceremony is supposed to open something up in you. Look at your life in the weeks after the ceremony and see how things have changed. That includes your relationships, behaviors, sleeping habits, your decision-making, and perhaps most importantly, how well you can deal with frustration without declaring a new spiritual emergency. 😂" His own reaction to the term opens it; "is supposed to" hedges the claim; the list gets a ranking ("perhaps most importantly"), so it isn't five even items; the emoji marks the quip. "i fixed the whole ai part, and added some emojis because they were clearly needed to prevent the humor from being so wry."
- **P18, his lessons, in two paragraphs.** What he took from the lineages, with specifics: "some 'dos & don't dos' from their sensible practices and less sensible practices"; what he values (loving kindness, inner child reparenting, nibbana meditation) against ceremonies dressed as "some kind of abstract mix of indigenous rituals & props"; a book ("God is Red"); the shadow side ("making the spiritual seem like another world apart from your regular life, which is sort of opposite to integration"); the shaman who heals well and may "send evil spirits to kill someone, if that hit job is lucrative"; the Huni Kuin claim about the knotted vine; "modern folk do very often decide they're ready to lead ceremonies"; and "they will continue to develop their understandings as well" for "they could still learn a lot from me".
- **P33's end, a human touch on a paragraph that passed.** "…that communes are just privileged escape pods" → "…, which gets double dipped with the objection that psychedelics are also priveleged escape pods (or, alternatively, as some say, "a vacation for the poor")."
- "make sure you're learning lessons each time..." and "continue".

## Joel's answers and fixes, 2026-10-06 20:38 UTC (community sections 5 and 6)

- **Typos.** "sectoin 5: typo, don't preserve my obvious typos. no need to recheck pangram to fix a typo." ("priveleged" → "privileged"; his "social meda" → "social media" in his own P5 addition.) A word that recurs or is defined is not a typo: "pl/ork" is his coinage (play + work, section 4), and I nearly "fixed" section 7's "inner pl/ork".
- **P4, which feed.** "the original 'after spending ten years optimizing my feed' is a bit unclear what feed. I'd change that to social media feed i guess."
- **P5, his addition.** At the end of the live question ("What connections to the technosphere do you keep, and which do you limit, when you're designing a community?"): "This is also one area where many modern folk will balk. Let the community decide if I can use my social media, or ChatGPT? Are you kidding? I get it. I really do. You're not a child anymore. But on the other hand, these technologies don't just affect you, they affect how you relate to the community as well." (API alone 0.00 Human.)
- **P8, the published modality wasn't his.** "i don't like replacing 'think through' with 'decide on in advance' that's a huge meaning shift. Not every new treatment etc can be decided on in advance." The published (AI-drafted) text said "It should decide in advance"; the audits had held every draft to it. And "i would change couplings to dependencies rather than the more vague connections."
- **P9, idioms are claims.** "proving ideological loyalty is not the same as jumping through ideological hoops. do you understand what those mean? jumping through hoops means making some extra effort. proving loyalty means proving loyalty, which may mean goin against your own needs, not just making extra effort." I had judged the swap the same meaning.
- **Notes he can read.** "idk what you were trying to say with 'An agreement, not each member's burden; all five protections.'" A note on the side-by-side page is plain sentences.
- **His question.** "why is it that words you write yourself are AI still? we should be making progress on learning to stop that. i think innerchild article is making progress on that without emulate, so you are using the same lessons as that chat right?" (Answered in the reply of that turn; the section 7 numbers are in `docs/HUMANIZATION-GATE.md`, "What section 7's runs taught".)
- "continue".
## Joel's notes, 2026-10-04 05:48 and 05:50 UTC (stopping)

- "i am confused. why did you stop there. you want me to help or what?" (E136)
- "no worries on pangram checks i have a ton of them this month because i'm working on a bunch of articles"
- No "continue".

## Joel's fixes and notes, 2026-10-06 19:04 UTC (When to Change the Strategy, the yawn, the update queue)

- **P1, meaning:** "your P1 is missing most of the actual meaning of the original. The original is asking to see what exactly is blocking rather than giving up on everything." Turn 29 had cut the guide's blockers as a repeat, and the instruction they served went with them. Now P1 says it outright: "Before either one, I'd look for what exactly is in the way. … Whatever it turns out to be, I'd work on that one thing instead of giving up on everything." (E137)
- **P1, logic:** "the original said if you're trying to comfort but the adult function is not really there, you changed that to if it WAS comforting ... and now it doesn't amke sense. why would it be comforting if adult was not there? what caused you to be so illogical here?" Turn 29's "And if it was comforting your little one, was the loving grown-up really there?" is now "Maybe you've been trying to comfort your little one for weeks, and the words are all there, but the loving grown-up behind them isn't, not yet." (E137)
- **P2's ending, his sentences word for word:** "And if you keep doing it right and what was supposed to happen still doesn't, I think you've learned something real about it. Something with clearly better research behind it is worth switching for too." became "And if you keep following the reparenting steps correctly without getting the expected results, consider if you have a unique case these steps don't match yet. Maybe you'll find something that works better for you, or you can ask me what I'd do for this case, or ask a therapist you work with. Either way, I'd like to hear about it!" His reason: "you took something vague "better-supported route" and instead of clarifying what the guide is saying, you made it seem like they should go do some other research to find what works for people on average or somethign which the guide is actually not about." Checked alone, in the h2 and in the h1 (he hadn't said he'd checked it): 100% Human, high each time.
- **P3 cut:** "P3 honestly looks like it could be cut." (the trap of explaining away every miss; his P2 sentences carry its point)
- **The yawn:** "it's not that yawning itself is a problem, but it can feel like you're tired of whatever you're doing when you notice yawning. actually, in re-evaluation counseling, yawning is a form of emotional discharge. so that's an interesting angle for that. sort of the opposite of how most people would think of it in this case." Now: "(even a yawn can come with an "I'm so done with this" feeling)" … "That yawn might actually be the opposite, though. Re-evaluation Counseling, a kind of peer counseling, counts yawning as emotional discharge, a feeling on its way out."
- **The updates:** "also check your lane in github, i added a bunch of suggested guide updates from the map/rules updates" (innerSignalGraph's PENDING-PUBLIC-GUIDE-CHANGES.md; where each goes: articles/inner-child-therapy/GUIDE-UPDATE-QUEUE-20261006.md).
- No "continue".

## Joel's fixes and notes, 2026-10-07 01:09 UTC (Two Common Protective Patterns, When to Change the Strategy, the queue)

- **Two Common Protective Patterns P2, a referent:** "Your "Both kinds" is referring to what? it's hard to understand since you've now talked about two different inerpretations of yawning. you should specify both waht." Now: "The skeptic and the pull both started out trying to prevent something that really hurt" (with "That yawn might actually be the opposite of checking out, though.", from the turn-30 cold reads).
- **When to Change the Strategy P1, a word:** "you should change "getting ready to," to getting ready,"".
- **P2, a contradiction (E138):** "this part is contradictory: "I'd probably want to fix it by saying sweeter and sweeter things, which won't work, and I wouldn't decide reparenting is useless over it, either. I'd borrow that grown-up first." change to this, it's human on pangram:" and his paragraph, word for word: "Maybe you've been trying to comfort your little one for weeks, and the words are all there, but the loving grown-up behind them isn't, not yet. Some people at that point might try saying sweeter and sweeter things, and then upon that not working, perhaps just "throw the baby out with the bathwater," and decide reparenting is useless. I'd borrow that grown-up first. Then try again, and see if your little one can tell the difference." The move: the mistaken try goes to "some people", not "I".
- **Weekdays (E139):** "PGQ-012 you are forgetting the rules abouut Tuesday and Wednesday etc. i told you, AI is always saying Tuesday, on Tuesday, or some specific day like this. on a regular Tuesday is the worst. Ai always saying ordinary boring regular now it's regular tuesday heheheh combinding all the ai tells". Queue draft A's "shows up on a regular Tuesday too" is "shows up out here too" (then rewritten for Pangram), P5's "by Wednesday" is "a few days later".
- **Numbers (E139):** "it's ok to say 5% is enough altho i feel it's a bit ai, like AI wants to put concrete numbers on stuff all the time, then people are wondering "how much is 5%?"". P5 says "a tiny bit of it".
- **The Pangram route:** "nope, you have to use GUI now. it's a diff google account from before tho".
- **The r4 guide:** "r4 guide ok, yeah if it has new stuff add that, i thought i had given you that but maybe not, just make sure it's not duplicating stuff".
- **A question that came from nowhere (E140):** "i'd prob consider a diff dr, maybe same sex etc or whichever one doesn't seem to creep them out. if their reactions are overly broad they can do some inner child reparenting on it, but might bea useful signal to take seriously, some drs are creeps. but your question is coming from where? it wasn't talking about a doctor touching someone. it was saying some sensations need medical checking."
- "continue" (merge at the end of the turn).

## Joel's note, 2026-10-07 03:24 UTC (cautions and bans)

- "ok i mean boring, regular etc are not for sure AI tells, almost nothing is a for sure AI tell, but they are way overused by AI." (E141: a frequency signal is a caution, not a ban; his own "ordinary life" and "boring" stay.)
- "continue".

## Joel's answers and fixes, 2026-10-07 01:43 UTC (community sections 5, 6 and 7)

- **Section 5, spellings.** "section 5 unusual spellings should help pass pangram, but that's also cheating i'd say, so you can fix them." ("contra-indications", "pre-requisite", "re-incarnation", "priveleged" → standard spellings; the section read 100% Human in the web app, 2,331 words scanned.)
- **Section 6, P8 and P9, overcompleting.** "i fixed p8p9, it was way overcompleting itself, now it passes pangram together". P8 lost its closing line ("These are all questions that a community should consider in advance."). P9 before: "There should be pre-existing agreements in place so that if a member gets catastrophically ill, their choices will be protected, they will have access to common resources or external funds if needed, they will be transported if needed, their privacy will be maintained, and there's room for the possibility that the community's preferred methods are not sufficient." After: "There should be pre-existing agreements in place so that their choices will be protected, both for catastrophic illness and end of life care. Medical privacy should be discussed, but may not be guaranteed, since some medical conditions are contagious." (His "may not guaranteed" and "contageous" fixed as typos.)
- **Section 7, P3, normal syntax.** "p3 is really interesting, you replaced commas and even 'or' with 'and and and and' that looks like emulate trying to cheat, and it wasn't needed. still passes pangram with normal syntax": "Rigid monogamy can turn fear and possession into a moral law. If people are doing free love, but aren't doing the inner pl/ork, they can just end up with a larger spreadsheet to distribute their fear over. It's not like calling something by a certain name dissolves the childhood panic, the comparison, the terror of abandonment, or the desire to control another person."
- **Section 7, my question.** "there's no need to question, 'their' is correct based on emualte's active voice."
- **Section 7, P4 to P6.** "p4 reads fine to me with as they wish, i agree with you it's not confusing"; "p5 ok"; "p6 ok".
- "ok fine not bad continue".

## Joel's fixes and rulings, 2026-10-07 15:05 UTC (community section 8, "The Grown Children Get the Final Review")

His texts are kept verbatim in the community lane's `s8/joel-1505/joel-20261007-1505.json`.
- **The pages.** "why this time did you give me section 5, 6, 7, and 8 side by side? am i supposed to look at all those?" (Only section 8 needed him.)
- **P7 and the subsection.** "P7 is in the wrong section. You moved it from "the mother is primary" to the prior section? why? although even in the original it seems to come from nowhere. I think cut this paragraph, it's pretty much stated by the other paras in this mothers section, and replace the headline with "Communal Parenting Adds On". We can change P10 so it fulfills the role." His P10 adds "If the father is unknown, the whole community can do the fathering, but the biological mom's role should always be honored." (The page had P7 under the wrong heading; the article didn't.)
- **P13.** "boss is fine".
- **P18.** "P18 has 2 lists of 3, super AI., Another AI tell is "may be X and still Y" make sure that's in the shared tells list. Humans don't use that as much. and it's unclear even in the original version what the point is in this para. The point is dishonest kids won't be protected because nobody will believe them. The reviewer didn't notice that? Totally contradicting itself saying their words carry power so they must be honest, then saying this has nothign to do with dismissing a report? ridiculous". His P18 opens "Protecting children is the duty of adults, but it requires them to help also." and brings in "The Boy Who Cried Wolf", the Buddha teaching his son honesty, labeling make-believe, and adults' lies (Santa).
- **P21.** "P21 doesn't make sense. Read that first sentence. "for an actual case" is referring to something that was not stated yet. It makes sense in the original. And the original was also incorrectly stating my position at the end. Why should the home community not control the interaction they have with outside? That would violate my entire guide to force communities to accept outside intervention. They should get help. I fixed it, it's human med conf". His ending: "competent help and review, hopefully including non-intrusive help from outside the home community."
- **Answers.** Q1 (P2b's "only saying that…"): "agree". Q2, his P3: "this one passes pangram". Q3, P17's spelled-out surprise: "i liked the spelled out version i don't think that's overcompletion, overcompletion is when you already have it explained and then you explain it again. there is still some actual overcompletion in this article i'm sure." Q4: "fixed it for you, human high conf. learn some lessons" (his six paragraphs from "If a community's kids never leave" to "belonging and freedom should go hand in hand"; two typos fixed by his rule, "althoug" and "able to access to their own records"; and the page's "~~rather than~~" diff marking, which came along with his P10, taken out).
- **Order.** "i would move p27-p28 to the top of the section".

## Joel's fixes and answers, 2026-10-07 20:21 UTC (community section 8, v26 to v27)

His texts are kept verbatim in the community lane's `s8/joel-2021/joel-20261007-2021.json`. v27 read 100% Human as a section (1,812 words scanned) and went into the article so far.
- **The pages.** "i didn't tell you to remove the full humanized article so far, that's still good for each turn."
- **P28.** "\"goodwill doesn't answer\" is that AI tell again, in the linter. abstracts doing things. p28 looks better now yes." (The cut of its first sentence stands; the linter's O6 now catches the sentence.)
- **The old H4 heading.** "ok" (it stays out).
- **P26.** "idk where p26 is now, are you talking about something you didn't show me? I went b ack to the previous turn, now i see i left that out by accident." His first paragraph of the last subsection now ends: "And kids coming back isn't necessarily the best thing for the communal movement either. If they then start their own communities, we may see more evolution than if they simply return and continue what their parents started."
- **P10.** "you're wrong, it says more than the published version. The published version says the community can do much of the fathering, but why does it say that? doesn't explain. My version explains. The mother point is also fine the way I put it. Here's a better version tho:" His new P10 opens "Tamera's Children's Place has repeated some of these old Kibbutz failings, taking children away from biological parents" and ends "since that attachment is formed already from years of nursing."
- **P18.** "yes fix that" ("it requires them to help also" → "it requires children to help also").
- **P21.** "it might rule out an emergency service, depending what you call an emergency service. non-intrusive means outsiders come in to disrupt the community. that's not like an ambulance coming because you called them. it's like what happened to Island Pond." (No change.)
- **P22.** "yes that's better" ("a commitment they choose on their own" → "a commitment they make as adults").
- **Overcompletion.** "p22 , unlimited freedom is not just overcompleting every childhood narrows the future, it's talking about the specific freedoms that can be given to children as they grow up e.g. Rumspringa. It's required in that sentence to explain the rest of it. But i agree with your suggestion to shorten the last line." (P25's last line is now "Belonging and freedom should go hand in hand.")
- "continue".

## Joel's question and fix, 2026-10-07 23:22 UTC (the linter's O6; community section 8 P22)

- **O6.** "wait are you saying you have a "list of nouns"? that sounds brittle... is that the best way to handle the abstracts doing things check? abstract nouns are a real vast open-ended list in my mind" (The check now reads the grammar with spaCy and WordNet, the list kept only as the fallback.)
- **P22.** "yes fix p222 take out second adults that's obvious" ("a commitment they make as adults" → "a commitment they make"; that text read 100% Human in 146g.)
- "continue".

## Joel's ruling and question, 2026-10-07 23:50 UTC (the linter's O6)

- **O6.** "\"modern life trains us\" is actually very human to say, so it seems we need an exception to the rule. not a brittle one. you don't understand just intuitively which abstractions are normally used and which are not? like modern life trains us... is so common it's almost cliche, it's not a witty AI quip, you know? i'm confused why you can't simply look at a word and know it's an abstract concept, isn't that what LLMs are great at?" (The linter's O6 flags are now candidates; a fresh agent judges them with `abstract_agents_prompt.py` against his ratings.)
- **Section 8 P19.** "yeah we can leave nobody's status buys silence, that's intermediate between an ai quip and what a human would normally say, and it passed pangram so it's ok..."
- "continue".

## Joel's fixes and requests, 2026-10-09 05:02 UTC (community section 9 P9 to P12; the UDA rule; the pages)

His texts are kept verbatim in the community lane's `s9/joel-0502/joel-20261009-0502.json`; four obvious typos in P12 were fixed under his rule (`s9/joel-0502/joel-0502-fixed.json`).
- **P9 to P12.** "i fixed p9-p12. hum high conf now, learn lessons and continue". Before (mine, every group wording read AI): "Most institutions get more and more layers and offices as they age. The Zapatistas did a review of theirs, and then pushed authority down. Did they put out a book on leadership and open a certification program? Nope. They just went and changed the system they were actually living in." After (his): "Institutions get more and more layers and offices as they age. We see this same pattern happen repeatedly, everywhere in history, except usually it goes one way without reversal, unless there's a revolution." And P11 opens "But there is a special reason the Zapatistas were successfully able to reverse this degeneration."; P12 "And that's not me saying that. Despite actually trying to train people in their model, …". What it does: `docs/HUMANIZATION-GATE.md`, "What section 9's runs and Joel's P9 to P12 taught".
- **The UDA rule.** "yeah i mean the MC rule should have been a UDA rule actually. so fix that. and it's not specific to this exact case." (The strategy fit and efficacy rule is now in UDA's `patterns/reasoning-selection.md` universal core, u-dont-existDOTcom/universal-dev-architecture#345; `AGENTS.md`, "Method fit and switching".)
- **The pages.** "on every turn you need to give me the in-context review page and the full humanized page, just like the innerchild lane does. that's assuming you have something for me to review." (`OWNER-FACING-TURN-CONTRACT.md`, "Every turn: the review page and the whole article".)

## Joel's answers and fix, 2026-10-09 22:08 UTC (community section 9, v13 to v14)

His message is kept verbatim in the community lane's `s9/joel-2208/joel-20261009-2208.json`.
- **P7.** "doesn't seem like a hedge to me, sounds just more conversational, so fix those reviewers" ("the closest thing to a whole example that I found" stays; the trace brief and the logic audit brief now say conversational is not a shift).
- **P8 and P9.** "agreed altho i'd say Juntas (Boards) at first per the rule on explaining things at first" (P8: "a rehearsal for the Good Government Juntas (Boards)").
- **P13.** "i fixed P13 so it's better and no longer reads as AI to pangram in the P9-13 block". Before (mine, v13): "Now, the Zapatistas also don't prove my whole economic path, from unpriced internal necessities, to a common purse, to getting rid of outside money. Do their communities use collective work to support their schools and clinics, and their autonomous government and resistance? Yes. …" After (his): "Now, the Zapatistas also don't prove my whole money-free economy goal. They still use money internally in some cases, not others, and they still use it externally for trade. They've also benefitted from outside economic help, while at the same time making efforts to remain politically independent from donors and more self-sustaining."
- "continue".

