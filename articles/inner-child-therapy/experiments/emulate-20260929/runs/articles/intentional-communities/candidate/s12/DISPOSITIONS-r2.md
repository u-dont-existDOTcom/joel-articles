# Section 12, gate rounds r2 to r5 (v4 to v9)

Section 12 is "The Math of Absorption, and Who This Isn't For". The candidate that went to the gate first was v4: Emulate's passing shapes with the meaning put back, which read 100% Human as a section (243g). Each round's fixes went to Pangram one at a time, and the section was checked again after every change. The final candidate is **v9** (`section-v9.md`, `candidate-v9-keys.json`). Pangram's web app scored it 100% Human ("Human Written", 907 words, 259g), and every paragraph passes alone or in a run with a neighbor that passes alone (`PREDICTIONS-s12.md`, 245g to 260g).

Reviewers: traces (Sonnet), section cold reads (`reviewer.py sense-section`, Sonnet), the whole-essay stance check (`stance_check_prompt.py` with `positions.txt`, Opus), the linter (`tells_lint.py`). Reports are in `review-r2/` to `review-r5/`.

Paragraph names here are the published section's (P1 to P17, with the list as L1 to L4). On Joel's pages the chart counts as P5, so P5 to P16 here are P6 to P17 there, L1 to L4 are P18 to P21, and P17 is P22.

My rule for findings, because trace rounds disagreed on text that hadn't changed: I fix what two reviewers raise and what the stance check raises. A finding that only one trace raised, where other traces had called the same words EQUIVALENT, stays, with the reason given below.

## Linter

- v4: **FAIL**, twice. P1's "jealousy or God or death or childhood or money or sex or psychedelics or somebody wanting to leave" is Joel's O14 ban ("that looks like emulate trying to cheat, and it wasn't needed"). And five paragraphs opened with "You" (B13). P1 is now P1t6, a normal comma list with the sentence turned round ("Many perfectly intelligent grownups would rather sit around for six hours talking about solar panels than talk about jealousy, God, death, childhood, money, sex, psychedelics, or somebody wanting to leave, which is what I ask people to do in this article."). The list's lead-in is now "This community may not be a good fit for you right now if:". v5 then failed B13 on three "So" openers; P3 lost its "So" (see P3 below).
- **My slip:** I built four Pangram batches (240g to 244g) on Emulate's "or ... or" P1 without linting it. The gate already says to lint every candidate before Pangram. The lane's batch builder (`build_batch.py`) now lints every new part and refuses the batch on a FAIL.
- v9: REVIEW, no FAIL (`review-r4/LINT-v9.txt`). The REVIEW flags are kept. The lists of three carry the published items (P13's five chores, P15's steps, P17's three answers). "And even then, the power is dangerous" and "But it's not infinite" are published one-line points. "Actually" carries the published "real". "Ordinary" is the published word.

## Stance check (Opus, whole essay, Joel's positions since publication)

| round | finding | what I did |
|---|---|---|
| r2 | P1 "intelligent and well adjusted": the essay says these people hide behind a show of competence | gone with P1t6 ("perfectly intelligent grownups") |
| r2 | P3 "some very practical questions to ask might be": a test floated, not the test | "the practical questions to ask are" |
| r2 | L1 "It's good that some groups can provide that": reads as approving communities as crisis landing places | cut; L1 ends "(A founding group shouldn't pretend it can give you those.)" |
| r2 | L4 "build up your resources a bit": a small top-up, against arriving largely healed | "a bit" cut |
| r3 | L4 "your ability to bring in a resource for it": reads as a means test | "a need that far outstrips your free resource right now" (the section's own term) |
| r4 | P13 "Whether there are eight people ... or eighty": size-neutral, where the point is that eight people still carry all of it | "With only eight people in the community" |
| r4 | P14 "some skill to contribute": emotional skill would count | "some practical skills to contribute" |
| r2 to r5 | P15 "outside review" (published) against Joel's 2026-10-11 18:35 rule and his 2026-10-07 position | kept as published; question 17 to Joel |

r5 on v9: one finding, the published "outside review". "No other rewrite sentence changes a position."

## Traces

Fixed, because two or more reviewers raised them:
- L2 "all of the benefits of village life" for "the feeling of village life" (r2 and r3 traces): "the feeling".
- L4 "finding support where you are so you can build up your resources" (r2, r3, r4 traces): the "so you can" they all objected to is "and" now ("finding support where you are and building up your resources"). "Finding" stays: r5 calls the line EQUIVALENT.
- P17 lost "A humane membership process" (r2 and r4 traces): "(Any humane membership process should have ways of not flat-out rejecting people who fall into these categories, like saying "later," or "in another role," or "with more support.")". The published opening ("A humane membership process should") failed the list's run three times; "Any" passes.
- P13 and P14, with the stance check (above).

Fixed on one trace, because the fix passed and loses nothing: P5 "accompany" ("being there for each other"), P7's four parts of free resource ("attention, steadiness, skill and practical capacity"), P14's "So" (the consequence link).

Kept, one reviewer against others:
- P3 without "So" (r3 trace): the linter's B13 needed one "So" gone, and one cold reader (r2 S1) said P3's "So" had nothing to follow from in P1 and P2. P14 keeps its "So", which the r2 trace asked for. "Good enough" without "for community", and "how available is he or she to engage in self-examination": EQUIVALENT in r2 (the section is about who joins; "available to" reads as open to).
- P5 "there's a lot of peer counseling going on" (r3: activity for capacity; "a lot of" as added volume): r2 called it the same picture, members doing for each other what therapists do elsewhere. The model in the published text implies a lot of it.
- P11 "roles" without "practical" (r2): every section with the fix ("practical roles") failed on the window over P10a and P11 (four sections, 245g to 249g). The next paragraphs' chores make the roles concrete.
- P12 "the people they are taking in" for "the person who was promised support" (r2): taking someone in is the promise; every section with the fix ("the people they've promised to support") failed on that same window (nine sections, 245g to 249g).
- P13 "fix the cars" for "equipment repaired" (r3): r5 calls it "a narrower example ... not a different claim". With "equipment", the window over P13's last two sentences failed in seven sections (244g to 247g); E6B's "cars" took it away.
- L1 "a place to land" for "safety" (r5 only): r2 to r4 read it as a safe refuge.
- P17 "these categories" for "every limit", and "flat-out" (r5 only): r2 and r4 called it EQUIVALENT ("every limit" is the four conditions just listed).
- "etc." in L1 and L2 (r2, r3, r5; r4: "low risk, no fix"): the article uses "etc." in its own lists ("Membership, land, resources, governance, children, leaving, etc."). The items stay examples of the same kind of need and the same kind of responsibility.

## Cold reads (`reviewer.py sense-section`, Sonnet)

- P11's "the same need can often be spread across lots of relationships and roles": the chart just above shows five in crisis among eighty, not the two of the group of eight. Three of four readers stumbled on it (r2 S1 and S2, r3 S3). The words are published, and so is the chart, so this is question 18 to Joel.
- P3's "So" (r2 S1): gone, above.
- r3 S4: no breaks.

## Not changed, for Joel (information)

- The chart repeats two of the section's sentences before the text says them ("A community can absorb only as much need as its members have free resource to meet." and "The cruel paradox: small communities need new members most and can absorb them least.").
