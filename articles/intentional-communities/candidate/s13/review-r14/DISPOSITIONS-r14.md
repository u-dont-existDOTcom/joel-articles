# Round r14 on v21: what each finding got (2026-10-15)

Reports: `trace-T1.md` (H2-P3, H3-P5), `trace-T2.md` (H4-P5, H5-P3), `SENSE-a.md`, `SENSE-b.md`, `MARCH-labels-a.txt`, `MARCH-labels-b.txt`, `STANCE-pub.md`, `STANCE-sofar.md`. Same rule as round r6 (`../review-r6/DISPOSITIONS-r6.md`); every flag that touches a linked sentence went through `tools/humanization/link_flags.py` with this file. No fixes this round.

## Kept, with the reason

- **H3-P5, "(It's in the reading list at the end, too.)" (trace T1, added: "a new fact about the article ... not checkable from this file"; fix: delete it, or "The book is also in the reading list at the end.").** A second tracer, and like the first it can't see the appendix, which lists the book (published, with its link); round r12's repeats check, which reads the whole article, named that entry. The tracer's own reading settles "It": "only the book fits". The sentence before links to the same book, and the pointer tells a reader who wants it where else the article sends them. The two-reviewers rule counts reviewers who could see what the words rely on. Cold read a paused at "the full sequence" and left it out: the sentence links to the book whose sequence it is.
- **H5-P3, the Zapatista clause (trace T2, added).** A fifth tracer, none shown section 9; both stance checks of this round name it as backed by the Zapatista section. As in rounds r9 to r13.
- **H5-P3, "that way" in Joel's sentence (both cold reads paused there and left it out).** Reader a: "the last one means toward treating 'outside' as the nation-state. P26's 'My research' is a link, so I did not ask why that sentence is there." The link goes to his research report, the one that leaned that way: the rule added at his 32 b, at work in both readers this round.
- **H2-P2 (no break in either march reading).** Done, as before.

## Clean, to Pangram (batch 297g)

Every paragraph v21 changed: H2-P3 ("Both of them!" a break in both readings), H3-P5 with H3-P4 (H3-P5 is under 50 words), H4-P5 (the hint with 😜 a break in both readings, "Write down your answers"), H5-P3 ("Just not whoever's being reviewed!" a break in both readings). Both cold reads OK for all 27 paragraphs (reader a: "P26's 'My research' is a link, so I did not ask why that sentence is there"), nothing in either stance check, keys PASS, lint REVIEW.
