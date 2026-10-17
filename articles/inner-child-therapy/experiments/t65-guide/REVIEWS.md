# Turn 65: the 12-hour run

Joel, 2026-10-17 02:11 UTC (`experiments/t65-answers/JOEL-20261017-0211.md`): "work continuously for 12 hours doing as much as you can. if you find that you are stumbling on a paragraph too much, just leave it for later and go to an easier one, then at the end we will see what you needed help with for the whole article". Also 31, A (his P5 stays), and #186's conflicts (fixed: main's #183 and this lane had both added tests at the end of the same file; both kept).

## How the run works

- Order: The Inner Guide Comes Later, groups 12 to 16 (dedup: `experiments/t56-guide/DEDUP-REPORT.md`); then the guide's next sections in order, each with a dedup first (`reviewer.py dedup`), easier ones first.
- Each paragraph the E181 way: a target from the dedup; four drafts with the moves that have read Human, linted and fixed; one `pangram_round.py` round (each draft alone, beside the paragraph before, in its section); one grounding (Opus) and one cold read (Sonnet) on the best draft that reads Human alone; installed only when it reads Human alone (E180); pushed with the state's next step.
- Parking: a paragraph with no draft that reads Human alone after three rounds is parked in `PARKED.md` (its faithful draft, every try with its result and link, the tells I see), and the run goes on to the next. Parked paragraphs are the list of what needs Joel at the end.
- While a paragraph's reviews run, the next paragraph is drafted and screened.
