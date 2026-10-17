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
