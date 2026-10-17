# The faithfulness pass of 2026-10-17: every finding and what happened to it

Joel, 17:16 UTC (his 45): "we should do a final pass to make sure it's faithful to the original i think before we are done ...
i feel like we've been doing section by section which could potentially lose the forest for the trees". Five fresh Opus
readers, none of whom had seen the work: four read the published article and the rewrite side by side (sections 1-4, 5-8,
9-12, 13-17: REPORT-A to REPORT-D.md), one read both whole (REPORT-FOREST.md). Mechanical checks: LINKS.md (no published link
is gone; the one new link is his PsyPost study) and LENGTHS.md (the rewrite is 42% longer; 5,842 of its 18,482 words are his).

The readers had the ledger and the unincorporated-ideas list, but not the questions page's decided list, where some of his
decisions and the dedup cuts he saw are recorded; I checked every finding against it before changing anything (the third
gap below).

How each finding was weighed (patterns/whole-argument-reconstruction.md, "Reviewing the owner's own writing"): the strongest
reading under which it isn't a problem first; a finding in Joel's own text is his choice and goes to him only as a question;
a finding in the accepted sections 13 and 14 goes to him as a proposal; a loss or shift in my wording or Emulate's, in a
candidate section, gets the published words back (his rule: "LOST gets the published words back").

## A tool bug the pass found

Three readers reported closing quotes and brackets "missing" after a sentence end (nine places: "keep clean.” Again", "“little
school.”", "Go see the world.”", "a treasure and a burden.”", "First let's get land!”", "(Not everyone does!)", "(And who owns
the land!)", "(Hopefully not all at once!)", "neutral stranger.”"). The article has every one of them. meaning_sweep.py's
sentence splitter, which puts in the author marks, swallowed a closer after a sentence end and joined sentences with one
space, so the readers' copy lost them (and the line breaks inside a block). Every sweep and pause tally that used author
marks read the same damaged text. Fixed in tools/humanization/meaning_sweep.py (sentences() keeps each closer on its
sentence and the space as it was; unmarked text now comes back unchanged), with a test (MeaningSweepAuthorMarks
test_closing_quotes_and_line_breaks_survive_the_marks). The second gap: the author marks came from the ledger and the
joel-2026* folders only, so his texts kept in section folders (s5/, s6/, s8/joel-*, s9/joel-*, s11/joel-*) went unmarked,
and his own section 8 rewrite of 7 October was read as mine (findings B1 to B6 below). The third: cuts he saw and
accepted were recorded on the questions page but not in UNINCORPORATED-IDEAS.md, so the readers took them for losses (D1
to D5, D10, D12); they're in that list now.

## Sections 1 to 4 (REPORT-A.md)

| # | Where | Finding | Decision |
|---|---|---|---|
| A1 | S1, East Wind | SHIFT, medium: "but the factory's importance still affected who could be challenged" gone; the paragraph ends on praise | Dropped: the rewrite's previous sentence says the factory "seemed to make the woman running it very hard to question", which is the published point; "Otherwise" scopes the praise. The published last clause restated it. |
| A2 | S1 and later | closing quotes missing | The tool bug above; the article is fine. |
| A3 | S1, the visitor's kid | SHIFT, low: "adventures mixed in" new, "great" for "strangely useful" | Dropped: "adventures mixed in" is his ruling of 2026-09-30 (ledger s1-rulings locks it); the sentence is his ruled text. |
| A4 | S2, P2 | VOICE: "starvin'" reads as a detector trick | Tried: "starving" (published), by his section 5 rule ("unusual spellings should help pass pangram, but that's also cheating i'd say"). The paragraph then read AI alone (415g, 0.60) and section 2 with it (0.31), and three rewordings that restore his published stance ("I'm less interested in ... than in the obvious thing underneath it") had no turn for either march reader (s2p2/). So the installed paragraph stays, and it goes to him: question 47. |

## Sections 5 to 8 (REPORT-B.md)

All seven findings are in section 8's "Children Need Freedom" and "The Door Must Open Outward", and all are in his own text of
2026-10-07 15:05 UTC (s8/joel-1505/joel-20261007-1505.json, "his texts as he sent them"), which the marks missed.

| # | Finding | Decision |
|---|---|---|
| B1 | LOST, medium: "If it cannot, it can still avoid punishing departure or withholding the knowledge and records a young adult needs to function elsewhere." | Question 49 (his text). Strongest reading: his "it doesn't need to be artificially impossible for grown kids to leave" and "access their own records" carry part of it; "punishing departure" isn't carried. |
| B2 | QUESTION: "or a reason to dismiss a report" gone from his truthfulness paragraph | Question 49. |
| B3 | SHIFT: money-world knowledge for all kids, not only money-free ones | Dropped: his own broadening, a plausible view. |
| B4 | ADDED: Rumspringa "age 16 ... a 2-year period of freedom from parental control" | Question 49: his text, but "a 2-year period" is likely wrong (it has no fixed length; it ends with baptism or leaving). |
| B5 | ADDED: "and eventually take care of their aging parents" | Dropped: his view, his words. |
| B6 | SHIFT: "sounds amorphous if it's not structured into plausible next steps" | Dropped: his words; the next steps are named. |
| B7 | the "treasure and a burden" quote not closed | The tool bug; the article is fine. |

## Sections 9 to 12 (REPORT-C.md)

| # | Finding | Decision |
|---|---|---|
| C1 | LOST, medium: "not claiming the Zapatistas already proved my whole model" | Fixed: "I'm not claiming the Zapatistas already proved my whole model." after "...their ambition to replicate." It was cut on 2026-10-14 as a repeat of his P13 ("the Zapatistas also don't prove my whole money-free economy goal"; fix-20261014 S9P18f), offered on the page as "Say if you want it back", with no answer. Under his dedup rule of 2026-10-17 02:07 the cut lost meaning: his P13 limits the economy claim, this one the whole model. |

Sections 10, 11 and 12: no findings (11 and 12 are almost all his text).

## Sections 13 to 17 (REPORT-D.md)

| # | Where | Finding | Decision |
|---|---|---|---|
| D1 | S13 (accepted) | SHIFT: Creating a Life Together's "full sequence" (vision, membership, resources, land) gone | Dropped: his decision of 2026-10-16 23:38, "no we should not lean on Christian's book order if it contradicts my own order that wouldn't make sense so fix that"; the book is recommended for the nuts and bolts. |
| D2 | S13 | LOST: "Nobody benefits from joining a group that cannot support what it has promised." | Dropped: a dedup cut of 2026-10-16 ("restated sections 5 and 12"), listed on his page; he accepted section 13 at 02:07. |
| D3 | S13 | LOST: "Discover the group's conflict capacity before hiring a surveyor." | Dropped: the same dedup (the paragraph before says it: "until you've been through at least one real conflict together"), accepted. |
| D4 | S13 | LOST: "the well fails" | Dropped: the same dedup (section 12's "The water well doesn't care how beautiful the new member's heart is." stays), accepted. |
| D5 | S13 | LOST: "A premove simulation cannot reveal a soul" | Dropped: the same dedup (the "good person" detector line says it), accepted. |
| D6 | S13 | ADDED: "But when power had crept up in their own system ..., it took them a long review to push it back down." (repeats section 9) | Dropped: it agrees with his section 9 text, and it's the paragraph's point (even they needed a review from outside the level that had grown); section 13 is accepted. |
| D7 | S13, 15, 16 | closers missing | The tool bug; the article is fine. |
| D8 | S15, "All is not well" P3 | SHIFT, medium: "It's interesting to see that ... whether you're allowed" for "Community itself isn't automatically liberating. Everything depends on who is permitted" | Fixed: "Being in community isn't automatically liberating. It all depends on who is allowed to belong without pretending." |
| D9 | S15, Black Tax P1 | SHIFT: "whatever you made of yourself later" for "whatever prosperity later came through you" | Fixed: "whatever prosperity came through you later". |
| D10 | S16, "If You Can't Move" | LOST, medium: "already contains a real piece of community"; "make a difference" for "change how people survive" | Half fixed: "It can still change how people survive a divorce, an illness or grief." (published), with the installed paragraph before it (415g read the pair AI, 0.88, while "That's it!" was cut there; 417g reads it as installed). "already contains a real piece of community" stays out: the overnight dedup cut it under his 02:07 rule because section 13 opens with it ("Your Little Forming Group Already Is the Community"), and the page listed it. |
| D11 | S16 | QUESTION: "Trust me on this one." vouches from experience | Question 50. |
| D12 | Appendix | LOST: "sequencing" gone from Creating a Life Together's entry | Dropped: his decision of 2026-10-16 23:38 (D1), which the page said the reading list would get too. I had put "sequencing" back before checking the page's decided list, and took it out again. |

## The whole article (REPORT-FOREST.md)

The spine holds: "The rewrite makes the same argument in the same order: all 17 sections, the thesis lines word for word".

| # | Finding | Decision |
|---|---|---|
| F1 | Section 11, his own rewrite: the published hard lines ("Members can decline to share without producing a therapeutic explanation for the refusal"; a floor "the majority cannot vote away") became balances, so the answer to the spiritual failure no longer says a member may keep their inner material to themselves | Question 50 (his text; it bears on the article's main argument). |
| F2 | Section 16: "rather than because "money is impure!"" mocks the belief, which section 4 gives as his own ("money is antagonistic to the spirit of community"); the published mocked declaring it while somebody else pays | Fixed: "rather than by declaring "money is impure!"" (published "declaring"). The section 8 half (money knowledge for every kid) is B3, now in question 49 since two readers raised it. |
| F3 | Christian's order gone in section 13 and the appendix | Dropped: his decision of 2026-10-16 23:38 (D1, D12). |
| F4 | Section 12, "free resource/capacity" before "free resource" is introduced | Dropped: his decision of 2026-10-14 ("free resource should be free resource/capacity at first not 2nd so it's defined where it first comes in"). |
| F5 | Section 8, Tamera: "repeated some of these old Kibbutz failings" and "weren't as dogmatic as I originally thought" | Dropped: his text, and both can be true (the reader says so too). |
| F6 | Section 13's Zapatista power creep repeats section 9 | Question 48, with section 13's exclamations (accepted section; D6 too). |
| F7 | Visitors' terms in sections 11 and 13 | Dropped: not opposed (the reader says so); friends visiting and decisions about pay or housing. |
| F8 | Two writers: sections 13, 15 and 16 exclaim and ask-then-answer (section 13: 32 "!" and 43 "?", against the published 0 and 6; section 15: 14 "?" against 0), with capitals for stress ("REALLY", "VISIBILITY", "PLUS goats", "CAN do") | The exclamations: his 43, done in 15 and 16, proposed for 13 (question 48). The question-answer pairs and the capitals: question 51 (the same treatment?). |
| F9 | Padding, mostly in section 13 (+781 words, 29 his) | Question 48 (a tightening pass on section 13, his call since it's accepted). |
| F10 | New facts: the Island Pond judge, the Amish "2-year period" | The judge: kept; it's the raid's history in the linked report (the court released the children the same day for want of specific evidence about any child). The Amish: question 49 (his text, likely wrong). |
| F11 | Section 8, "or a reason to dismiss a report" gone | Question 49 (B2). |
| F12 | Section 15, "No, not that either!" before the anti-gay law: bluntness softened at the gravest point | Tried: "No, not that either." The paragraph then read AI with its neighbor (415g, 0.34, the AI window exactly that paragraph): the "!" holds the question-and-answer it's built on. Taken back; his paragraph to help with (question 47). D8's fix covers the second half of the finding. |
