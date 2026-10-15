# Round r8 on v10: what each finding got (2026-10-15)

Reports: `trace-T1.md`, `trace-T3.md`, `trace-T4.md`, `SENSE-a.md`, `SENSE-b.md`, `MARCH-labels-a.txt`, `MARCH-labels-b.txt`, `STANCE-pub.md`, `STANCE-sofar.md`. Trace T2 (H3-P1, H3-P3, H4-P6+7) ran past the agent's 64,000-token output limit and left no report; round r9 ran those pairs again, one or two per run. Same rule as round r6 (`../review-r6/DISPOSITIONS-r6.md`). The fixes were made in `../make_v11.py` before round r9; this record was written at the end of the turn, after round r9.

## Kept, with the reason

- **H1-P2, "the real relational pl/ork" (trace T1, added: "pl/ork is unreadable"; fix "the real work of").** The article's own term: section 4 is "The Four Parts That Have to Pl/ork Together", and "Relational pl/ork" is its second part. The tracer reads section 13's pairs without section 4; both cold reads, which read the whole article, passed the paragraph, and this round's stance check against the article so far measured the sentence against section 4's relational pl/ork.
- **H2-P3, "Yes, it keeps getting longer." (trace T1: an aside, "no fix").**
- **H4-P2, "Do they get the basic idea of why this community is here? Are they at least starting to do the relevant practices?" (stance check against the article so far: the bar for newcomers is arriving largely pre-healed).** The published questions set the same floor in the same place ("Do they understand why this community exists? Have they begun the relevant practices?"). The pre-healed floor is about what a newcomer brings (sections 3 and 12), and neither version of this paragraph restates it. One reviewer; the paragraph read Human alone and after The Farm paragraph (290g).
- **H5-P3, the research aside (both cold reads: "why is this here?").** The published sentence, which the link to the research explains. With round r7's reader a, three cold reads had stopped at it; round r9's reader b made four, and it went to Joel as question 32 (`../../OWNER-QUESTIONS.md`).
- **The published contradiction, "already a community" against "still a circle of promising strangers" (published-essay stance check: the rewrite "still has it, in a milder form").** No change this round: v9's bridge ("even if it's still an untested one") stays, and round r9's published-essay stance check found the rewrite no longer has it. Reported to Joel with the other published passages the reviewers kept stopping at.

## Fixed in v11

- H1-P2: "giving each of you time," for "allowing each of you to take the time you need," (stance check against the article so far: section 4's relational pl/ork gives everyone equal time; the published "Give each person time").
- H4-P8: "(Hanging out doesn't count, I'm afraid!)" (march: no break in reading a).
- H5-P1: "A safe community can't promise to keep everyone. Yes, really." (trace T3: "Even" made safety a concession; march: no break in reading b, so the published claim said again as a reaction is the break); "keeps violating essential boundaries," (trace T3: the published "repeatedly violates").
- H5-P3: "an autonomous regional institution" back in the published list; "The Zapatistas are an important correction here: autonomous institutions can review local power without becoming the state, and when power crept up in theirs, they pushed it back down." (traces T4 of r6 and r8: "opening my eyes" made a personal claim; the published-essay stance check: "regional" narrowed the lesson; both cold reads: section 9 tells how power "had crept up and consolidated itself at higher levels" and was pushed back down, so the clause is section 9's account).

## Clean after r8, to Pangram (batch 291g)

v10's values paragraphs (H2-P1 with H2-P2, H2-P3 alone and with H2-P3b, H2-P4 alone and with H2-P3b before it), H5-P2 and H5-P4. The values paragraphs all read Human. H5-P2 and H5-P4 read AI, went to a fresh Emulate round from v11 (round f, `../emu-f/`), and came back as v12 (`../make_v12.py`).
