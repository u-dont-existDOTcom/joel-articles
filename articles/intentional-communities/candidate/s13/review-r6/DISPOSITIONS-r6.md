# Round r6 on v8: what each finding got (2026-10-15)

Reports: `trace-T1.md`, `trace-T3.md` to `trace-T6.md` (T2 stopped at its output limit and wrote nothing; its four pairs go to round r7), `SENSE-a.md`, `SENSE-b.md`, `MARCH-labels-a.txt`, `MARCH-labels-b.txt`, `STANCE-pub.md`, `STANCE-sofar.md`. The rule: fix what two reviewers raise, or what one raises when the fix loses nothing; the published sentence decides between traces that disagree (docs/HUMANIZATION-GATE.md, section 13's first rounds). Fixes are in `../make_v9.py`.

## Kept, with the reason

- **H1-P2, "relational pl/ork" (trace T1 of r5 and of r6: "unreadable", "play/work").** The article's own term: section 4 names the four parts, "2) relational pl/ork (peer counseling especially)", and pl/ork is play and work on purpose. Both traces read the pair without the article. The four cold reads of r5 and r6, which read the whole article first, passed the paragraph. A flag that holds only without the article's context gets this disposition, not a change (Joel's 30 b, 2026-10-15). Record: clean.
- **H1-P4, "capacity" (trace T1 of r6).** "Capacity" is a word Joel called an AI tell ("capacity is an AI tell", 2026-10-12; linter O40) unless it's tied to free resource. The budget's meaning, what the group can provide, is put in plain words in v9 ("budget for what the group can provide on the practical side"), which round r4's trace passed as the same claim.
- **H5-P3, "opening my eyes" (trace T5 of r6, a shift; trace T5 of r5 called the same words equivalent).** The published "The Zapatistas are an important correction here" follows "My research initially leaned too far that way": the correction is of that lean, which is what "opening my eyes" says. v9 drops "very" (the trace's "matter more"), a fix that loses nothing.
- **H5-P3, "or anything else" (trace T5 of r6, added).** The published list is "sometimes another community, ...": examples of a kind the sentence before defines (a competent layer not reviewing its own conduct). The hedge also keeps a list of six from running as a list (Joel's list fix, 2026-10-12). One reviewer; the fix would lose that.
- **H5-P4, "if necessary, a ruling" (trace T6, a shift).** Mediation doesn't replace adjudication where adjudication is needed; not every case needs a ruling. One reviewer; the hedge also breaks Emulate's "and ... and" run.
- **H2-P2, "When you go to visit a community" (cold read a).** The published order: the values heading moves from your own group to a community you might join, and v8's H2-P1 now opens on choosing a community. One reader; the paragraph read Human (288g) and doesn't change.
- **The Zapatistas against section 9 (stance check, so far: a contradiction in the published text).** Section 13 says autonomous institutions *can* review local power without becoming the state; section 9 tells how their higher levels drifted and how they moved authority back down, which the check itself says leaves "can" standing. One reviewer, on published words; read within the section's frame it holds.

## Fixed in v9

- **"Already a community" against "still a circle of promising strangers"** (both cold reads and the so-far stance check of r6, cold read b of r5): a published tension three reviewers raised in one round, so a fix I make and report (2026-10-13 rule). H1-P1 gets "even if it's still an untested one", which says in what sense the group already is a community before H1-P3's strangers line.
- H1-P4: "practical side" named as what the group can provide; "would stop everything" -> "could stop everything" (trace T1).
- H2-P3: the three LGBTQ+ questions about a member of the community again ("Could an LGBTQ+ member live openly there? Date and/or be in a relationship with whomever they choose? Would the community keep them fully protected?"); "taught to question" (traces T1 of r5 and r6); "Until a group has answered" (trace T1).
- H4-P2: "through a thoughtful exchange" (traces T3 of r5 and r6).
- H4-P5: what the founding agreements cover named ("A full member's rights and responsibilities"), not "These" (r5) or "Both" (r6) (trace T4 of both rounds).
- H5-P1: "it can be okay to eject them" and "just impossible to live with" (stance check, published essay; Joel's own "if that gets to the point of impossible to live with", 2026-10-11 23:12).
- H5-P2: "who has to step aside from the decisions" (traces T5 of r5 and r6: who is recused).
- H5-P4: the instruction back ("Also pick a mediator or ombud beforehand") before the question (trace T6: "Also" lost; cold read a: the question took the claim as made); "people", not "the parties", and nobody named twice as "they"; "mediation is for repairing relations"; "once consent is gone" (trace T6; round r4's trace had found "living together" narrow).

## The march (breaks)

Both readings had a break in 19 of v8's 27 paragraphs. Without one in a reading: H2-P2 (unchanged, read Human in 288g), H3-P1, H4-P2, H4-P3, H4-P5, H4-P7, H4-P8, H4-P9, H5-P4. The breaks both readings took in r5 and r6 were remarks in the writer's voice ("It's boring stuff, I know.", "That's a lot of deciding, I realize."), asides in parentheses ("(Hopefully not all at once!)", "(More on that one next.)"), reactions ("Being open to everybody felt so spiritual!", "that's cool!") and "Otherwise, what's it worth?". Opening questions, "right?", "Hanging out doesn't count!" and "(Hint: ...)" each went one way in one reading and the other way in the next. So v9's new breaks are of the first kinds, each saying again something its paragraph says.

## Clean after r6, to Pangram now (batch 289g)

H1-P2, H2-P1 (alone and with its heading), H3-P4, H3-P5 (with H3-P4, being under 50 words), H4-P4 and H4-P6: trace OK (or the disposition above), cold reads OK, both march readings with a break, stance checks clear, lint not FAIL, keys PASS.
