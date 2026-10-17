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
- Round h, under "## Timing Is Individual": p15-a Human alone and with the heading but AI in the h1; p15-c and p15-d the other way round. Round i, after P13 without the heading: p15-d Human alone (0.30), beside P13 (0.34, medium) and in the h1 (0.099, high). Its grounding and a cold read of the whole h1 (with P12's fix) are running.
