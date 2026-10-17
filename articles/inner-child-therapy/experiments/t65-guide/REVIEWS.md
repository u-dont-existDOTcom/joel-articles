# Turn 65: the 12-hour run

Joel, 2026-10-17 02:11 UTC (`experiments/t65-answers/JOEL-20261017-0211.md`): "work continuously for 12 hours doing as much as you can. if you find that you are stumbling on a paragraph too much, just leave it for later and go to an easier one, then at the end we will see what you needed help with for the whole article". Also 31, A (his P5 stays), and #186's conflicts (fixed: main's #183 and this lane had both added tests at the end of the same file; both kept).

## How the run works

- Order: The Inner Guide Comes Later, groups 12 to 16 (dedup: `experiments/t56-guide/DEDUP-REPORT.md`); then the guide's next sections in order, each with a dedup first (`reviewer.py dedup`), easier ones first.
- Each paragraph the E181 way: a target from the dedup; four drafts with the moves that have read Human, linted and fixed; one `pangram_round.py` round (each draft alone, beside the paragraph before, in its section); one grounding (Opus) and one cold read (Sonnet) on the best draft that reads Human alone; installed only when it reads Human alone (E180); pushed with the state's next step.
- Parking: a paragraph with no draft that reads Human alone after three rounds is parked in `PARKED.md` (its faithful draft, every try with its result and link, the tells I see), and the run goes on to the next. Parked paragraphs are the list of what needs Joel at the end.
- While a paragraph's reviews run, the next paragraph is drafted and screened.

## P12, group 12 (love bombing): in

- Round a (p12-a to d): all AI alone (0.76 to 0.99); every one opened on the guide's amount-versus-judgment contrast in its own words.
- Round b (p12-e to h): p12-f Human alone (0.105, low) with a joke aside ("are the red flags from last week starting to look kind of cute?"); the h1 Human (0.065, high).
- Reviews of p12-f: cold read OK; grounding: two CHANGED ([1] the "not just too much affection" point missing; [2] "somebody's one and only" narrowed praise and special attention to romance). Round d: four versions with both fixes, all Human alone (0.14 to 0.26); installed p12-f2 (0.14; the h1 0.079, high).
- Every P12 read AI beside P11 (eight of eight); the gate goes by the paragraph alone and the section (gate: "The section and each paragraph are the test, not a group").

## P13, group 13 (humor): in

- Round c (p13-a to d, after p12-f): p13-d Human alone (0.048), beside P12 (0.41, medium) and in the h1 (0.108, high). Grounding and cold read OK. Installed. The linter's B13 refused a first p13-b that would have made a third paragraph opening "The".

## P14, group 14 (timing is individual): parked

Three rounds (e, f, g), twelve drafts: one read Human alone and left an AI window in the h1; under the guide's own subheading the heading with P14 read AI every time. In `PARKED.md`, with my best draft and the tries.

## P15, groups 15 and 16 (the integration test)

- Group 15 is all in the article already; P15 carries group 16: did the opening deepen or widen love, and does it show (more honest and dependable, protective, compassionate, better at relationships).
- Round h, under "## Timing Is Individual": p15-a Human alone and with the heading but AI in the h1; p15-c and p15-d the other way round. Round i, after P13 without the heading: p15-d Human alone (0.30), beside P13 (0.34, medium) and in the h1 (0.099, high).
- Grounding of p15-d (`GROUNDING-p15d.md`): a DRIFT (the first test is whether the opening's love has reached your little one, before how you treat people) and an UNCLEAR start ("big opening came long before any of this", right after the humor paragraphs). Cold read (`COLD-READ-p15d.md`): the same stop at P15's first sentence.
- Round j: p15-d6 under the guide's subheading "## Timing Is Individual", opening "keep their own schedule, too" and asking "Has it reached your little one yet?": alone Human (0.06, low; https://www.pangram.com/history/c7944fca-9673-4fb0-b668-05c6cbe4034d), the heading with P15 Human (0.056), the h1 Human Written (0.108, high; https://www.pangram.com/history/2ace607d-f5cd-481e-8d3b-f6397305ea39). Cold read of the h1 with it (`COLD-READ-p15d6.md`): every paragraph OK. Installed.

# Simple Practices (the guide's next h1)

Dedup first (`SP-DEDUP-REPORT.md`, nine practices, G1 to G9): what each practice still adds, what the article already says (left out), and three facts in the guide's own "I" that aren't in the article (left out, listed in `PARKED.md`). The h1 goes after The Inner Guide Comes Later, with each practice as an h2.

## Borrow Hindsight

- P1 (sp1-p1-d) and P2 (sp1-p2-e) read Human alone, in the h2 and in the h1 (rounds k to m; links in `tools/PREDICTIONS.md`).
- Grounding (`GROUNDING-sp1.md`): MAIN POINT OK, two MUST flags: [8] the guide's fallback is missing (if you can't get into the wiser self's head, the smallest honest thing, a no or a pause, without faking the feeling), since the article says it only of other practices; [9] the other person's wiser future self needs the guide's next line (it changes nothing about what you go by now). Both are things the dedup had marked as said elsewhere; the grounding's reason (a reader with someone who keeps hurting them would wait for the better version) is why they go back in here.
- Round o: refused by the gate before Pangram (two drafts FAILed the linter: a packed sentence, a list of three).
- Round q (e3, e7, e8, each with both fixes in one paragraph): e7 alone Human (0.31), e3 and e8 alone AI; in the h2 all three AI (0.82 to 0.98, high). The fixes made one paragraph of five moves.
- Round r: split as in the guide (its grounding: "fits one short addition per paragraph if [9] becomes its own paragraph"): P2 = the first three sentences and [8]; P3 = the other person's wiser future self and [9].

## Remember When You Already Did It

- Round m: sp2-e Human alone (0.026), in the h2 (0.049) and in the h1 (0.028, high); a, c and d AI.
- Grounding (`GROUNDING-sp2.md`): MAIN POINT OK; [5] CHANGED: "how worn out you are today" narrows the guide's "exhaustion or present limits", so a reader who no longer has the help they had then could still treat the old win as a bar. Fix: widen it to today's limits, including missing what helped.
- Round q: sp2-f ("when you might be more worn out or missing whatever helped you then") alone Human (0.14), in the h2 Human (0.16); sp2-h Human (0.40; 0.31). Next: the cold read (E175: a reworded clause gets a cold read, not a new grounding).

## A Heart-to-Child Loop

- Round n: P1 sp3-p1-c Human alone (0.001), in the h2 (0.001) and in the h1 (0.021, high).
- Round q: P2 sp3-p2-d Human alone (0.27) and in the h2 (0.13, medium); a2 and e AI alone.
- Grounding of P1 and P2 (`GROUNDING-sp3.md`): MAIN POINT OK; on P2's loop sentence, CHANGED ("nobody's doing all the rescuing" keeps the rescue frame and hands your little one part of the job) and MISFIRES, a MUST ("send some back up" reads as a step, against the vow's "You don't have to love me back"). Fix: the love coming back is welcome and not owed; if none comes, keep sending yours.

## Rounds r and s (the rest of Simple Practices, every practice at once)

Round r had 43 checks in one batch (seven groups), round s 52 (eleven groups); every result and link is in `tools/PREDICTIONS.md` (rows t65r, t65s), scored with `tools/humanization/pangram_score.py`.

- Borrow Hindsight, split as in the guide (round r): P3 read Human alone in three versions (0.012 to 0.12), but every P2 with the [8] fix read AI, and the h2 read AI with each (0.64 to 0.99). Round s, the fixes as a P3 after the unchanged P2 (e): P3 AI alone and the h2 AI (0.95, 0.996). Round t has one more try (the food image turned around: "make the food yourself"); if it fails, Borrow Hindsight is parked with P1 and P2 as they read Human and the two fixes written out for Joel.
- A Heart-to-Child Loop P2 with its grounding's fixes (round s): d2 alone Human (0.41) and the h2 Human (0.041, medium; https://www.pangram.com/history/2f59d723-4500-47f4-b003-808c3a553b35). The practice is ready: P1 = sp3-p1-c, P2 = sp3-p2-d2. Cold read of the first three practices running (`COLD-READ-sp-1.md`).
- The story phrase: P1 e and f Human alone (0.01, 0.008) and in the h2 (0.075, 0.054); P2 b, b2 and b3 Human alone (0.017 to 0.027), but the h2 with P1 and P2 read AI every time (0.71 to 0.90).
- Journal With Each Hand: eight versions in two rounds, all AI alone (0.56 to 0.99).
- Just Like Me: P1 two versions AI (0.78, 0.92); P2 three versions AI (0.80 to 0.997).
- One Intention: round r all AI (0.77 to 1.0); round s P2 h Human (0.44), the rest AI.
- Use Childhood Photographs (round s, alone): P2 a and b Human (0.022, 0.196); P1, P3, P4 and P5 AI (P3 mixed: an AI window of 36 to 38 words).
- Close the Session: six versions AI (0.99 to 1.0).

What changed for round t (E183): one representative draft of each practice went to the grounding before its screen (`GROUNDING-sp4.md` to `GROUNDING-sp9.md`), and round t's drafts carry the fixes: Journal (the wrong hand writes whatever is really there, nothing made up; its writing already looks like a child's), the story phrase (no defendant; the trial ends, not the accountability or the repair; telling it colder won't help; the turn to what the person in the story needs now), One Intention (any one hook; seeing it only in the review counts), Just Like Me (the wish asks for no contact; contact is its own decision, never made while flooded), the photo practice (the looking turns to what your little one needs now; a photo proves nothing about the story it seems to tell; putting it away gets its own paragraph; stop at the first pull, overwhelm included), Close the Session (going back to your life is part of the healing; rest as an example; nothing has to be settled first). The drafts also try his own moves from the article (maybes, an idiom, a quoted thought, "(hehe)"-style asides, one 😅 from his list) after the instruction-shaped drafts read AI.
- PGQ-016 (memory support isn't reflective journaling), queued for Journal With Each Hand and missed by the practice dedup (it isn't in the guide's text), gets a P2 of its own.

## Rounds t to v, and the first install

- Two tabs: from round t a batch runs in two Pangram tabs at once (the seed tab forward, a second tab with window.__reverse = true), meeting in the middle through localStorage; round u's version stopped one check short (both tabs left the middle one), so each tab now claims a check before it takes it.
- Borrow Hindsight: P2 j ("make the food yourself", the [8] fix) read Human alone (0.29) and in the h2 (0.40); P3 i read Human alone (0.001) and in the h2 (0.43), but the cold read of the first three practices (`COLD-READ-sp-1.md`) found "the other person" had nothing to point to. Two fixes ("If someone else is part of this", "And if there's another person in the picture") read Human alone and AI in the h2; "whoever else is involved" (i4) read Human alone (0.001), in the h2 (0.365, high) and in the h1 (0.099, high).
- Installed: # Simple Practices with Borrow Hindsight (P1 d, P2 j, P3 i4), Remember When You Already Did It (f) and A Heart-to-Child Loop (P1 c, P2 d2). The installed h1 is round v's checked text, character for character (Human Written 0.099, high, https://www.pangram.com/history/aa97d3db-6dc0-4fda-bfdb-4f93b26d9a61). A cold read of it is running (`COLD-READ-sp-2.md`).
- Parked (`PARKED.md`, with my best faithful drafts and every try): Journal With Each Hand, Close the Session, One Intention P1, the story phrase's P2, Just Like Me's P2, the photo practice's P1 and P4b. Their P1s that read Human alone and in their h2 (the story phrase, Just Like Me) wait with them.
- When Love Still Feels Missing (grounded first, `GROUNDING-lm1.md` to `lm4.md`): How Much Happiness P1 (lm4-p1-a) read Human alone (0.34) and with its heading (0.28); P2 (lm4-p2-a2, with the grounding's "profound") and Notice the Part P2 (lm2-p2-c) read Human alone; everything else read AI in two rounds (u, v).

## Rounds w to y (the later sections, my own drafts)

Groundings first (`GROUNDING-ks01.md`, `sh01`, `fg01`, `le01`, `ba01`), their MUST fixes in every draft (E183). Three rounds, about 100 checks; every result and link in `tools/PREDICTIONS.md` (rows t65w to t65y), scored with `pangram_score.py`. Eight read Human:

- If You Want to Kill Yourself: P3 a (the self you want to kill, 0.002), P4 c (the Buddhist view, 0.39), P5 b (momentum and redirections, 0.086) and P6 d (the change you still can't make, 0.022) alone; P1 e (the crisis steps) read Human in its section (0.37) and AI alone (0.82).
- When One Life Has Ended: P1 c (the gap and the bardo) alone (0.16) and with its heading (0.16).
- When Love Still Feels Missing: How Much Happiness P5 c alone (0.002).
- Never Human in three rounds: How to Forgive Without Forgetting (seventeen versions of four paragraphs), Borrowed Adulthood in Relationship (six), When the Practice Feels Real but Stays Shallow (seven), the crisis steps alone and the adult-in-the-room paragraph (six), and the rest of When One Life Has Ended (nine).
- The sixteen checks left "(pending)" since rounds a to x were found in the History by their first 300 characters (the list gives that much of each text) and scored; two were the same text as an earlier check, which Pangram reads once.

## Round z (fresh writers, E177)

My own drafts had read Human about one time in twelve since round w, against about one in four earlier in the turn, so every paragraph still failing went to fresh writer agents (`writers/`, prompts built by `writers/writers_jobs.py` from `reviewer/writer_draft.txt` with each passage's points and its grounding's MUST fixes; the guide's first-person life facts left out, E159). Twenty jobs, the Simple Practices and When Love Still Feels Missing paragraphs still parked, the later sections, and three not tried yet (Speak Toward What You Are Building without the framework's name, and the closing paragraph). Two writers on the same prompt came back nearly word for word alike, so the third writer of each job runs on a different model.

Round z (65 checks; rows t65z in `tools/PREDICTIONS.md`): 19 read Human, against about one in twelve of my own drafts in rounds w to y. By group:

- When Love Still Feels Missing did best. Notice the Part That Came Here: writer 2's two paragraphs read Human alone (0.42, 0.23) and in the h2 (0.16, high); writer 1's P2 alone (0.059) and its h2 (0.11, high). Somatic Heart Opening: both writers Human alone (0.093, 0.27) and in the h2 (0.32, 0.39). The h1's own opening: P1 Human for both writers (0.49, 0.45) and writer 1's P3 (0.055), every P2 AI, and the h1 opening AI with each. How Much Happiness: both writers' P3 Human (0.39, 0.15), both P4 AI.
- The closing paragraph (You Are Worthy of Love. Always.) read Human alone (0.019); the photo practice's P4b (writer 2) Human alone (0.068); Journal With Each Hand's P2 (writer 1, the memory aid) Human alone (0.32); One Intention's P2 (writer 2) Human alone (0.35).
- Every other Simple Practices paragraph read AI (0.62 to 1.0), and so did every h2 with them; the crisis steps and the adult-in-the-room paragraph (writer 1 and mine, 0.87 to 0.99); When One Life Has Ended; Borrowed Adulthood (0.57 to 0.63); the shallow-practice paragraph alone (AI Detected 0.57, an AI window of 89 words) though its section read Human (0.46).
- Two Sonnet writers stopped at their output limit on the four-paragraph jobs (How to Forgive, When One Life Has Ended), and a third on the crisis paragraphs.

Round z2 (35 checks, rows t65z2): 4 Human. The closing paragraph's h1 read Human with both versions (writer 1: 0.21; writer 3: 0.13, its paragraph alone 0.42), so You Are Worthy of Love. Always. is ready. My own crisis-steps paragraph (ks12 w8, which opens on the reader's own situation, "Maybe you're reading this with a plan, or the means, close by") read Human alone (0.20), the first in seven versions. Everything else AI: the adult-in-the-room paragraph again, two more versions of the h1's P2 (0.59, 0.89), How Much Happiness P4, the shallow-practice paragraph (writer 3 and mine), the photo opener (writer 3), Journal With Each Hand with my P1 and writer 1's P2 (0.80), How to Forgive (four paragraphs, writer 1, each 0.96 to 1.0), Borrowed Adulthood (writer 3), Speak Toward What You Are Building (six paragraphs, 0.67 to 1.0), and Close the Session (writer 3).

Round z3 (20 checks, rows t65z3): When Love Still Feels Missing's opening is done: writer 1's P2 for the middle paragraph read Human alone (0.17), and the opening with it read Human (0.25, high; with writer 2's P1, 0.39, high). The NDE paragraph of If You Want to Kill Yourself read Human alone in both of my versions (0.014, 0.13). Still AI: the adult-in-the-room paragraph (three more of mine), How Much Happiness P4 (writer 1), the photo opener (two of mine, and the practice with each P1), One Intention P1 (writer 1, and the h2 with each P2). The suicide section without its P2 read AI Detected (0.30, an AI window of 76 words). The cold reads of the love section (`COLD-READ-lm-1.md`) and the closing (`COLD-READ-wl-1.md`) found every paragraph OK.

Round z4 (10 checks, rows t65z4): the love h1 as it would go in (the opening, Notice the Part, Somatic Heart Opening) read Mostly Human Written (0.37) with one AI window of 45 words, the last two sentences of Somatic Heart Opening, which end the h1. Writer 3's version of the opening's P2 read Human alone (0.15) and in the opening (0.18). Two more adult-in-the-room paragraphs read AI (0.999); with eleven versions in five rounds, all AI, it's parked. The suicide section with its NDE paragraph and without P2 read AI Detected (0.51; the AI window covers the Buddhist view, the NDE paragraph and the start of the momentum paragraph). How Much Happiness P3 and P4 (writer 3) AI. Round z5 tries two new endings for Somatic Heart Opening (one points back to "turn the song off for tonight" in the article's opening) and writer 3's, each in the h1.

Rounds z5 to z7: Somatic Heart Opening with a new ending of mine (z5, lm3v w8) read Human alone (0.077), in its h2 (0.21) and in the h1, which read Human Written with no AI window (0.26, high, 519 words, https://www.pangram.com/history/0e708b03-204d-4126-935c-626a4c0db1e3). The second cold read of the h1 with it (`COLD-READ-lm-2.md`) found every paragraph OK. Installed: # When Love Still Feels Missing, its opening (writer 1's P1 and P3, the lm1p2 writer's P2), Notice the Part That Came Here (writer 2) and Somatic Heart Opening (lm3v w8); the installed h1 is the checked text character for character. Placeholders mark the parked Simple Practices before it and How Much Happiness after it.
- When the Practice Feels Real but Stays Shallow: writer 3's first half had read Human and its second half AI, and my w8 the other way round, so z7 joined the halves that read Human. Both joins read Human alone (w6 0.044, w7 0.47) and with the heading (0.073, 0.27). A cold read of w6 is running (`COLD-READ-sh-1.md`).
- Round z8 does the same for Borrowed Adulthood (writer 1's P2 read Human for its first 45 words, the routines and the three questions AI).
