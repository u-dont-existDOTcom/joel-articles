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
