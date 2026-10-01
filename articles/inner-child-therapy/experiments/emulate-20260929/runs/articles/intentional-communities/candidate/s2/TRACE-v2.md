# TRACE-v2: blind two-way preservation trace, "Communes Are Hot Again" section

Files opened: only those in `review-v2/trace/` (BRIEF.md, original-section.md, R-section.md, and the 17 R-C*.md files). The folder was listed once. No other file or folder was opened, nothing was searched, no web.

Quotation marks in this report are straightened. Where the original uses curly quotes or apostrophes, the rewrites use the same characters; the difflib check found no character-level differences of that kind.

## Completeness check (Python difflib, word level, on the files in that folder only)

- R-section.md is string-identical to the a-versions for C1a, C2, C3, C4a, C6, C7a, C8, C9a, C10a, C11a and C12 (C2, C3, C6, C8, C12 have a single version).
- The unchanged paragraph ("It's poppin' on Instagram", called C5 here) is string-identical in R-section.md and original-section.md. It has no R-file.
- The H1, the H3 "The Freeloader Problem", and the three image lines (image 4, 5, 6) are string-identical to the original and sit in the same order and positions.
- Paragraph order in R-section.md equals the original order.
- Every difflib hunk between each original paragraph and each rewrite file appears in a table below. Punctuation-only hunks: C1 (comma before "and treated"), C3 (period inside the closing quote becomes a comma outside it), C6 (comma before "the way"), C11 (Oxford comma before "and ownership" removed), C12 (comma in "me, too"), C9b (", and" joins two sentences). They are not marked unless they change meaning.

## File to original paragraph

| Rewrite file | Original paragraph (original-section.md line) | First words of the original |
|---|---|---|
| R-C1a, R-C1b | P1 (line 3) | "The longing that shaped my father's film..." |
| R-C2 | P2 (line 5) | "I'm less interested in declaring an official..." |
| R-C3 | P3 (line 7) | "Look at Google Trends for..." |
| R-C4a, R-C4b | P4 (line 11) | "I can't prove AI caused that turn..." |
| (no file) | P5 (line 13) | "It's poppin' on Instagram too!..." unchanged |
| R-C6 | P6 (line 15) | "Another large influencer later floated..." |
| R-C7a, R-C7b | P7 (line 19) | "Not everybody in the comments was trying to join..." |
| R-C8 | P8 (line 23) | "The commune comments became a miniature..." |
| R-C9a, R-C9b | P9 (line 25) | "Although that comment applies more to..." |
| R-C10a, R-C10b | P10 (line 27) | "Communal ownership therefore needs..." |
| R-C11a, R-C11b | P11 (line 29) | "The desire to return to a natural way..." |
| R-C12 | P12 (line 31) | "I'm not currently recruiting anyone..." |

## How the tables are marked

- Forward table: original units against the rewrite. SAME = identical wording. SAME-MEANING = reworded, a reader could swap the two without believing anything different. SHIFTED = scope, strength, hedge, voice, tense/mood, kind of claim or attribution changed, even slightly (the Note says exactly how and flags "minor" where the change is small). DROPPED = no counterpart in the rewrite.
- Reverse table (ADDED): wording in the rewrite with no counterpart unit in the original (claims, judgments, causes, people addressed, intensifiers, hedges, connectives that add a relation). Pure synonym swaps (began/started) and punctuation are not listed. A new wording that replaces a SHIFTED unit is listed too, with a cross-reference, because it carries something the original did not.
- The counts at the end are: SHIFTED = rows marked SHIFTED in the Forward table; DROPPED = rows marked DROPPED; ADDED = rows in the Reverse table.
- For the b files, units whose text is identical to the a file are marked as in the a file; only the differing units are re-argued.

---

# Per-file traces

## R-C1a (answers original P1)

**Forward**

| # | Original unit | Rewrite | Mark | Note |
|---|---|---|---|---|
| 1 | "The longing that shaped my father's film" | same | SAME | |
| 2 | "is suddenly everywhere again" | "is suddenly in the air again" | SHIFTED | Minor. "everywhere" claims ubiquity; "in the air" is figurative (ambient, felt, can suggest something impending). "suddenly ... again" kept. |
| 3 | "The U.S. Surgeon General's 2023 advisory" | "In 2023, the U.S. Surgeon General's advisory" | SAME-MEANING | Same body, same year. "2023" moves out of the link text and becomes a sentence-opening date for the reporting. |
| 4 | "reported that roughly half of American adults experience loneliness" | identical | SAME | "roughly half" and present-tense "experience" unchanged. |
| 5 | "and treated social connection as a public-health issue" | same words, comma before "and" | SAME | |
| 6 | "rather than a sentimental extra" | identical | SAME | |

**Reverse (ADDED)**

| # | Rewrite wording | Kind | Note |
|---|---|---|---|
| A1 | "in the air" | figurative idiom | Replaces "everywhere" (Forward 2). Not counted as ADDED content beyond that: no new fact. Listed because "in the air" can carry an "impending" sense the original lacked. |

Not counted: "In 2023," is relocated from the link text, not new.

**Sources**

| Item | Original | Rewrite | Result |
|---|---|---|---|
| Link | [U.S. Surgeon General's 2023 advisory](https://www.hhs.gov/sites/default/files/surgeon-general-social-connection-advisory.pdf) | [U.S. Surgeon General's advisory](same URL) | Same URL, same job (source for the loneliness figure and the framing). Link text loses "2023". |
| Quote marks | none | none | |
| Who said or did what | the advisory reported; the advisory treated | same | SAME |

**Sense**

| Word or phrase | Referent visible? | Note |
|---|---|---|
| "the longing" | No. First text after the H1; nothing says which longing. | Same in the original. |
| "my father's film" | No. Neither the father nor the film is named or described. | Same in the original. |
| "again" | Nothing visible says when it was in the air before. | Same in the original. |
| "advisory" | Named only by the link text and URL. | Same in the original. |
| Tense | No slip. | |

## R-C1b (answers original P1)

**Forward.** Units 1 to 5 are identical to R-C1a and carry the same marks (1 SAME, 2 SHIFTED, 3 SAME-MEANING, 4 SAME, 5 SAME).

| # | Original unit | Rewrite | Mark | Note |
|---|---|---|---|---|
| 6 | "rather than a sentimental extra" | absent; the sentence ends "as a public-health issue." | DROPPED | The advisory is still said to treat connection as a public-health issue. The contrast with a "sentimental extra" is gone. |

**Reverse (ADDED)**

| # | Rewrite wording | Kind | Note |
|---|---|---|---|
| A1 | "in the air" | figurative idiom | As in R-C1a. |

**Sources.** As R-C1a: same URL and job, link text loses "2023", no quote marks, same agent (the advisory) for "reported" and "treated".

**Sense.** As R-C1a. No additional items.

---

## R-C2 (answers original P2)

**Forward**

| # | Original unit | Rewrite | Mark | Note |
|---|---|---|---|---|
| 1 | "I'm less interested in declaring ... than in the obvious fact underneath it" (the author's own comparative interest, first person) | "Whether you want to call that loneliness an 'epidemic' or not, it's obvious that" | SHIFTED | First-person ranking (label matters less to me than the underlying fact) becomes a second-person concession that leaves the label to the reader. The author's own stance on the label is no longer stated. "declaring" becomes "call". |
| 2 | "official" ("an official 'epidemic'") | absent | DROPPED | The formal-designation sense is gone. |
| 3 | "epidemic" in scare quotes | "epidemic" in scare quotes | SAME | Marks kept. What it is applied to is in A2. |
| 4 | "the obvious fact" | "it's obvious that" | SAME-MEANING | "obvious" kept. "underneath it" (the fact lying beneath the label) is not stated. |
| 5 | "a lot of people can't tolerate isolated modern life anymore" | "a lot of people can't tolerate modern life in isolation anymore" | SAME-MEANING | "isolated modern life" becomes "modern life in isolation". "a lot of people", "can't tolerate", "anymore" unchanged. See Sense on "in isolation". |
| 6 | "They" (the many people who can't tolerate it) | "People" | SHIFTED | Anaphoric "They" becomes generic "People". The group that disagrees and agrees changes from those many people to people in general, or reads that way. |
| 7 | "may disagree about politics, food, God, sex, and whether shoes are oppressive" | "may disagree about politics, food, God, sex, or whether shoes are oppressive" | SAME-MEANING | All five topics kept; "and" becomes "or". |
| 8 | "but they agree that something ... is starving them" | "...is starvin' them" | SAME-MEANING | Spelling only. |
| 9 | "something about the current arrangement" | "something about the way things are now" | SHIFTED | Minor. "current arrangement" (a set-up of living) becomes "the way things are now" (looser, general circumstances). |

**Reverse (ADDED)**

| # | Rewrite wording | Kind | Note |
|---|---|---|---|
| A1 | "Whether you want ... or not" | second-person address; reader's choice | The reader ("you") is addressed and given the choice of label. Not in the original. |
| A2 | "that loneliness" | named object | Names loneliness as the thing that might be called an "epidemic". The original leaves the object implicit. |
| A3 | "starvin'" | dialect spelling | Register only, no claim. |

**Sources**

| Item | Original | Rewrite | Result |
|---|---|---|---|
| Links | none | none | |
| Quote marks | "epidemic" (scare quotes, no source named) | "epidemic" (scare quotes, no source named) | Same marks. In the original it is a word the author declines to "declare"; in the rewrite it is a label the reader may or may not "call" it. No speaker for the word in either. |
| Who said or did what | author states his own interest; "They" disagree and agree | reader ("you") chooses the label; "People" disagree and agree | Author's stance removed (Forward 1); group changed (Forward 6). |

**Sense**

| Word or phrase | Referent visible? | Note |
|---|---|---|
| "that loneliness" | Yes: "loneliness" in R-C1. | |
| "epidemic" | No source for the word in visible text. | Same in the original. |
| "modern life in isolation" | Yes, but a reader may reread: "in isolation" also means "considered separately". | |
| "People" (second sentence) | Ambiguous: the "a lot of people" of the previous sentence, or people in general. | Original used "They". |
| "the way things are now" | "things" has no referent; "now" is not anchored. | |
| Tense | No slip. | |

---

## R-C3 (answers original P3)

**Forward**

| # | Original unit | Rewrite | Mark | Note |
|---|---|---|---|---|
| 1 | "Look at Google Trends for" | "If you look at Google Trends for" | SAME-MEANING | Imperative becomes conditional. Both send the reader to the same two queries. |
| 2 | "ecovillage" and "intentional community" (two links) | same | SAME | Same terms, same link texts, same URLs. |
| 3 | "Interest had been drifting downward for years" | "interest drifted down for years" | SAME-MEANING | Past perfect progressive becomes simple past; "downward" becomes "down". "for years" and the order (decline, then upturn) kept. |
| 4 | "then bent upward sharply in the mid-2020s" | identical | SAME | |
| 5 | The author states the trend after telling the reader to look | "you can see that" | SHIFTED | Minor. The trend becomes something the reader will see in the Trends data (an evidential claim), not the author's own statement. |

**Reverse (ADDED)**

| # | Rewrite wording | Kind | Note |
|---|---|---|---|
| A1 | "you can see that" | evidential claim | Asserts the linked Trends pages visibly show this pattern. The original only says "Look at" and then states the trend. |

**Sources**

| Item | Original | Rewrite | Result |
|---|---|---|---|
| Links | [ecovillage](https://trends.google.com/explore?q=ecovillage&date=all&geo=Worldwide), [intentional community](https://trends.google.com/explore?q=intentional%20community&date=all&geo=Worldwide) | same two | Same URLs, same link texts, same job (the data behind the trend claim). |
| Quote marks | around the two search terms | around the two search terms | Same words and function (the query strings). Period inside the closing quote becomes a comma outside it. |
| Who said or did what | author tells reader to look, then states the trend | reader looks and "can see" the trend | See Forward 5. |

**Sense**

| Word or phrase | Referent visible? | Note |
|---|---|---|
| "interest" | Only by context: search interest in the two terms. | Same in the original. |
| Topic jump from R-C2 (loneliness) to search interest | No connective. | Same in the original. |
| Tense | "drifted ... bent" past, "you can see" present. No slip. | |

---

## R-C4a (answers original P4)

**Forward**

| # | Original unit | Rewrite | Mark | Note |
|---|---|---|---|---|
| 1 | "I can't prove AI caused that turn" | "I have no proof that AI caused this turn" | SAME-MEANING | Hedge kept. Nuance: "can't prove" (unable to demonstrate) becomes "have no proof" (none in hand). "that turn" becomes "this turn". The causal hypothesis (AI caused the turn) is the same. |
| 2 | "The timing is still hard to ignore." | ", but it's hard to ignore the timing." | SAME-MEANING | "still" becomes "but"; two sentences become one. |
| 3 | "Around the same period," | "That's around when" | SAME-MEANING | "around" kept. Both say AI's change coincided approximately with the turn. See Sense on "That". |
| 4 | "AI stopped being a tech-news curiosity" | same | SAME | |
| 5 | "and began reorganizing" | "and started reorganizing" | SAME-MEANING | |
| 6 | "people's jobs" | same | SAME | |
| 7 | "feeds" | same | SAME | |
| 8 | "relationships" | same | SAME | |
| 9 | "expectations of the future" | same | SAME | |
| 10 | "Suddenly 'maybe we should form a village' sounded less like a 1972 leftover and more like a backup plan." | identical | SAME | |

**Reverse (ADDED).** None.

**Sources**

| Item | Original | Rewrite | Result |
|---|---|---|---|
| Links | none | none | |
| Quote marks | "maybe we should form a village" | same | Same words, same marks. Unattributed in both: a thought or remark with no speaker. |
| Who said or did what | author cannot prove; AI stopped and began | author has no proof; AI stopped and started | SAME |

**Sense**

| Word or phrase | Referent visible? | Note |
|---|---|---|
| "this turn" | Yes: the upward bend in R-C3 (image 4 sits between). | |
| "That's around when" | "That" has two candidates: "this turn" and "the timing". Both point to the same period. | Mild reread. |
| "the timing" | Timing of what against what is only supplied by the next sentence. | Same in the original. |
| "AI" | Not introduced earlier in the section. | Same in the original. |
| Tense | Present ("have no proof", "it's") then past ("stopped", "started", "sounded"). No slip. | |

## R-C4b (answers original P4)

**Forward.** Units 1 to 4 and 10 are identical to R-C4a (1 SAME-MEANING, 2 SAME-MEANING, 3 SAME-MEANING, 4 SAME, 10 SAME).

| # | Original unit | Rewrite | Mark | Note |
|---|---|---|---|---|
| 5 | "and began reorganizing" | "and started changing" | SHIFTED | "reorganizing" (restructuring) becomes "changing" (generic). |
| 6 | "people's jobs" | absent | DROPPED | |
| 7 | "feeds" | absent | DROPPED | |
| 8 | "relationships" | absent | DROPPED | |
| 9 | "expectations of the future" | absent | DROPPED | Replaced by "the way people live" (A1). The link between "expectations of the future" and "backup plan" is no longer stated. |

**Reverse (ADDED)**

| # | Rewrite wording | Kind | Note |
|---|---|---|---|
| A1 | "the way people live" | catch-all scope | Names no domain. Covers all of life, so the claim about what AI changed is broader and vaguer than four named domains. |

**Sources.** As R-C4a.

**Sense.** As R-C4a. No additional items.

---

## R-C6 (answers original P6)

**Forward**

| # | Original unit | Rewrite | Mark | Note |
|---|---|---|---|---|
| 1 | "Another large influencer" | "Then another large influencer" | SAME | "another" and "large" kept. |
| 2 | "later" | "Then" | SAME-MEANING | Sequence after the first influencer's post kept. "later" (after an interval) becomes "Then" (next in sequence). See Sense. |
| 3 | "floated the commune idea" (link) | same | SAME | Same link text and URL. |
| 4 | "the comments began turning into a recruitment board" | "the comments started turning into a recruitment board" | SAME-MEANING | |
| 5 | "People were finding prospective members under a post" | "People were finding future members under a post" | SHIFTED | "prospective" (potential) becomes "future" (people who will be members). Strength of the claim about the commenters goes up. |
| 6 | "the way they might normally find" | "the way you'd normally find" | SHIFTED | The hedge "might" goes ("would normally" is a habitual generalization). The subject changes from third-person "they" (the people in the comments) to generic "you". |
| 7 | "a used sofa" | "a second-hand sofa" | SAME-MEANING | |
| 8 | "It was chaotic" | absent | DROPPED | Author's judgment of the episode. |
| 9 | "sincere" | absent | DROPPED | Author's claim that the people involved meant it. |
| 10 | "and revealing" | absent | DROPPED | Author's claim that the episode showed something. Rows 8 to 10 are one sentence: "It was chaotic, sincere, and revealing." |

**Reverse (ADDED)**

| # | Rewrite wording | Kind | Note |
|---|---|---|---|
| A1 | "you'd" | person addressed (generic "you") | The reader is cast as the person who finds a sofa. The original had "they". See Forward 6. |

**Sources**

| Item | Original | Rewrite | Result |
|---|---|---|---|
| Link | [floated the commune idea](https://instagram.com/p/DaLvZV2qIk2/) | same | Same URL, same job (the second influencer's post). |
| Quote marks | none | none | |
| Who said or did what | another influencer floated the idea; the comments turned; people found prospective members; "they" find a sofa | another influencer floated the idea; the comments turned; people found future members; "you" find a sofa | Actors the same except the sofa-finder (they becomes you) and the dropped assessment. |

**Sense**

| Word or phrase | Referent visible? | Note |
|---|---|---|
| "Then" | Follows the last sentence of R-C5: "Imagine opening your inbox after casually inviting a million followers to co-found a village." | Reread: "Then" can read as the next step of the imagined scenario rather than a later real event. The original had "Another ... later". |
| "another large influencer" | Yes: Chantress Seba in R-C5 ("a million followers"). | |
| "the comments" | The comments on this influencer's post; "a post" appears only in the next sentence. | Same in the original. |
| "a post" | Indefinite; context implies the post just linked. | Same in the original. |
| "future members" | Members of what is implicit (the commune). | |
| Tense | No slip. | |

---

## R-C7a (answers original P7)

**Forward**

| # | Original unit | Rewrite | Mark | Note |
|---|---|---|---|---|
| 1 | "Not everybody in the comments was trying to join." | identical | SAME | |
| 2 | "The oldest objection" | same | SAME | |
| 3 | "arrived" | "came up" | SAME-MEANING | |
| 4 | "almost immediately" | same | SAME | |
| 5 | "maybe most people don't want the responsibility anarchism requires" | "maybe most people don't want the responsibility that anarchism requires" | SAME | "that" inserted. "maybe" kept. |
| 6 | "and communal property becomes" | "and communal property ends up" | SAME-MEANING | "becomes" becomes "ends up" (adds an eventual-result sense). |
| 7 | "owned by everyone, cared for by nobody." (quoted) | identical | SAME | |

**Reverse (ADDED).** None.

**Sources**

| Item | Original | Rewrite | Result |
|---|---|---|---|
| Links | none | none | |
| Quote marks | "owned by everyone, cared for by nobody." | same | Same words and marks. No speaker named in either; image 5 follows. |
| Who said or did what | the objection arrived in the comments | the objection came up in the comments | SAME |

**Sense**

| Word or phrase | Referent visible? | Note |
|---|---|---|
| "the comments" | Yes: R-C6. | |
| "The oldest objection" | Objection to what is not stated (the commune idea, by implication). | Same in the original. |
| "anarchism" | First appearance. Nothing visible links the commune or village idea to anarchism. | Same in the original. |
| quoted phrase | No named speaker. | Same in the original. |
| Tense | "came up" past; "don't want", "ends up" present generic. No slip. | Same pattern as the original. |

## R-C7b (answers original P7)

**Forward**

| # | Original unit | Rewrite | Mark | Note |
|---|---|---|---|---|
| 1a | "Not everybody in the comments" (scope: the commenters) | "Not everyone commented" | SHIFTED | The location phrase folds into "commented". Reads as "not every commenter ..." or as "not everyone [at all] commented". |
| 1b | "was trying to join" | "with interest" | SHIFTED | An action or intent (trying to join) becomes an attitude (commenting with interest). A person can be interested and not trying to join. |
| 2 | "The oldest objection" | same | SAME | |
| 3 | "arrived" | "came up" | SAME-MEANING | |
| 4 | "almost immediately" | same | SAME | |
| 5 | the objection follows a colon | "the idea that" | SAME-MEANING | The objection is framed as "the idea that". Content unchanged (see A2). |
| 6 | "maybe" | "maybe" | SAME | |
| 7 | "most people don't want the responsibility" | same | SAME | |
| 8a | "anarchism" | "a working anarchism" | SHIFTED | Adds "working": presupposes a version of anarchism that functions. The responsibility becomes that of a functioning anarchism, not of anarchism as such. |
| 8b | "requires" | "would require of them" | SHIFTED | Present indicative (a general fact) becomes conditional "would" (hypothetical). Adds "of them". |
| 9 | "and communal property becomes" | "and that communal property ends up" | SAME-MEANING | "becomes" becomes "ends up", as in R-C7a. |
| 10 | "owned by everyone, cared for by nobody." (quoted) | identical | SAME | |

**Reverse (ADDED)**

| # | Rewrite wording | Kind | Note |
|---|---|---|---|
| A1 | "with interest" | attitude | Commenters are said to show interest. The original speaks of intent to join. See Forward 1b. |
| A2 | "the idea that" | framing | The objection is presented as "the idea that ...". |
| A3 | "working" | qualifier | See Forward 8a. |
| A4 | "of them" | person | The people on whom the responsibility would fall. Implied in the original, not stated. |

**Sources**

| Item | Original | Rewrite | Result |
|---|---|---|---|
| Links | none | none | |
| Quote marks | "owned by everyone, cared for by nobody." | same | Same words and marks; no speaker named in either. In the rewrite the quotation sits inside "the idea that ... and that communal property ends up ...". |
| Who said or did what | the objection arrived in the comments | the objection came up as "the idea that" | Commenters remain the implied source. |

**Sense**

| Word or phrase | Referent visible? | Note |
|---|---|---|
| "Not everyone commented with interest." | "everyone" has no stated domain. | Reread: "not everyone [at all] commented" against "not every commenter was interested". |
| "a working anarchism" | "working" reads as "functioning". First appearance of anarchism, with no visible link to the commune idea. | The link gap is the same in the original. |
| "of them" | Yes: "most people". | |
| Tense | "came up" past; "would require" conditional alongside present "don't want". No slip. | |

---

## R-C8 (answers original P8)

**Forward**

| # | Original unit | Rewrite | Mark | Note |
|---|---|---|---|---|
| 1 | "The commune comments" | "Those comments" | SHIFTED | The comments are named by topic (the comments on the commune posts). "Those" points back at the most recently described comments (the objection thread, image 5). The scope may narrow from all the commune comments to the objecting ones. |
| 2 | "became a miniature political-philosophy seminar" | "became a little seminar on political philosophy" | SAME-MEANING | |
| 3 | "as Instagram comments sometimes do" | "which you don't normally find on Instagram" | SHIFTED | The claim about Instagram flips. The original says Instagram comments sometimes do this (a wry remark on the platform). The rewrite says this is not normally found there (unusual for the platform). Frequency and expectation change, and so does the author's attitude to Instagram comments. |

**Reverse (ADDED)**

| # | Rewrite wording | Kind | Note |
|---|---|---|---|
| A1 | "you" | person addressed (generic "you") | Not in the original. |
| A2 | "don't normally find on Instagram" | claim of rarity | A claim about Instagram that the original does not make. See Forward 3. |

**Sources.** No links, no quote marks. Who does what: the original makes "Instagram comments" the agent ("sometimes do"); the rewrite makes "you" the finder and Instagram the place.

**Sense**

| Word or phrase | Referent visible? | Note |
|---|---|---|
| "Those comments" | Several candidates: the objecting comments in R-C7, the unlabeled screenshot (image 5), or all comments under the influencer posts. No single clear referent. | The original named them ("The commune comments"). |
| "which" | Most naturally "a little seminar on political philosophy"; a reader could take it as the whole event. | |
| Tense | "became" past; "don't normally find" present generic. No slip. | |

---

## R-C9a (answers original P9)

**Forward**

| # | Original unit | Rewrite | Mark | Note |
|---|---|---|---|---|
| 1 | "Although" | "While" | SAME-MEANING | Concessive. |
| 2 | "that comment" (a specific comment, presumably the one in image 5) | "this objection" | SHIFTED | The referent changes from one comment to the objection as an idea. The original separates "that comment" (one comment) from "that objection" (the idea). The rewrite has only the objection, so the concession now belongs to the objection itself. |
| 3 | "applies more to large socialism experiments than small communes" | "is more applicable to large-scale experiments in socialism than to small communes" | SAME-MEANING | "large socialism experiments" becomes "large-scale experiments in socialism". |
| 4 | "that objection deserves a serious answer" | "it deserves a serious answer anyway" | SAME-MEANING | "that objection" becomes "it". "anyway" is A1. |
| 5 | "Some people really would rather let somebody else take responsibility." | "since some people really would rather let somebody else take responsibility" | SAME | Claim words identical, "really" kept. The sentence becomes a "since" clause (A2). |
| 6 | "Shared ownership can blur responsibility until the same three people maintain everything while everybody else discusses freedom." | identical | SAME | |
| 7 | "Informal leaders then gain power partly because everyone keeps handing it to them." | identical | SAME | |

**Reverse (ADDED)**

| # | Rewrite wording | Kind | Note |
|---|---|---|---|
| A1 | "anyway" | intensifier | Adds emphasis to a concession "While" already makes. |
| A2 | "since" | cause | States that some people's preference is the reason the objection deserves a serious answer. In the original the second sentence stands alone and the relation is not stated. |

**Sources**

| Item | Original | Rewrite | Result |
|---|---|---|---|
| Links, quote marks | none | none | |
| Who said or did what | "that comment" (a commenter's, image 5) applies more to socialism experiments; "that objection" deserves an answer | "this objection" is more applicable to socialism experiments and deserves an answer | The pointer to a specific comment (the screenshot) is gone. The author's concession now concerns the objection. |

**Sense**

| Word or phrase | Referent visible? | Note |
|---|---|---|
| "this objection" | Yes: "The oldest objection" in R-C7a. R-C8 and image 5 sit between. | |
| "it" | Yes: the objection. | |
| "large-scale experiments in socialism" | No examples given. | Same in the original. |
| "the same three people" | "same" as whom is not visible (a hypothetical group). | Same in the original. |
| "it ... them" (handing it to them) | "it" = power; "them" = informal leaders. | Same in the original. |
| Tense | No slip. | |

## R-C9b (answers original P9)

**Forward.** Units 1 to 6 are identical to R-C9a with the same marks (1 SAME-MEANING, 2 SHIFTED, 3 SAME-MEANING, 4 SAME-MEANING, 5 SAME, 6 SAME).

| # | Original unit | Rewrite | Mark | Note |
|---|---|---|---|---|
| 7a | "then" ("Informal leaders then gain power") | absent | DROPPED | The sequence marker goes: the leaders' gain of power is no longer stated as a later step after the same three people do everything. It becomes a parallel clause joined by ", and". |
| 7b | "Informal leaders gain power partly because everyone keeps handing it to them." | "and informal leaders gain power partly because everyone keeps handing it to them" | SAME | Words identical apart from "then" and the join. "partly" kept. |

**Reverse (ADDED).** A1 "anyway" and A2 "since", as in R-C9a.

**Sources.** As R-C9a.

**Sense.** As R-C9a, plus: ", and informal leaders gain power" follows "while everybody else discusses freedom" and can be read as part of the "until ... while ..." clause. Reread risk.

---

## R-C10a (answers original P10)

**Forward**

| # | Original unit | Rewrite | Mark | Note |
|---|---|---|---|---|
| 1 | "therefore" | absent | DROPPED | The inference marker goes. The needs are no longer stated as following from the preceding argument. |
| 2 | "Communal ownership ... needs" | same | SAME | |
| 3 | "named stewardship" | same | SAME | |
| 4 | "visible duties" | same | SAME | |
| 5 | "consequences for chronic freeloading" | same | SAME | |
| 6 | "enough relational capacity to confront the problem before resentment becomes the real government" | "It also needs enough relational capacity to confront the problem before resentment becomes the real government." | SAME | Words identical. Becomes its own sentence with "It also needs". |
| 7 | "A community cannot run on the assumption that" | "A community can't run on the assumption that" | SAME-MEANING | |
| 8 | "removing bosses removes" | "getting rid of bosses gets rid of" | SAME-MEANING | |
| 9 | "passivity, selfishness, theft, or learned helplessness" | same | SAME | All four items kept. |

**Reverse (ADDED).** None.

**Sources.** No links, no quote marks. The actor is "A community" in both.

**Sense**

| Word or phrase | Referent visible? | Note |
|---|---|---|
| "It also needs" | "It" = "Communal ownership"; the nearest noun is "chronic freeloading". | Minor. |
| "the problem" | Yes: chronic freeloading in the previous sentence. | |
| "bosses" | No visible account of whose bosses. | Same in the original. |
| "the real government" | Metaphor, no gloss. | Same in the original. |
| Tense | No slip. | |

## R-C10b (answers original P10)

**Forward.** Units 1 to 6 and 9 are identical to R-C10a (1 DROPPED, 2 to 6 SAME, 9 SAME).

| # | Original unit | Rewrite | Mark | Note |
|---|---|---|---|---|
| 7 | "A community cannot run on the assumption that" | "It's naive to think that" | SHIFTED | A claim about what a community can and cannot run on becomes an evaluation of the person who holds the belief. The subject "A community" is gone. |
| 8 | "removing bosses removes" | "getting rid of bosses will get rid of" | SHIFTED | Generic present becomes future "will". |

**Reverse (ADDED)**

| # | Rewrite wording | Kind | Note |
|---|---|---|---|
| A1 | "naive" | judgment | Characterizes people who hold the assumption. Not in the original. |

**Sources.** No links, no quote marks. The actor changes: the original's subject is "A community"; the rewrite's is the unnamed thinker.

**Sense.** As R-C10a, plus: "It also needs ..." and "It's naive to think ..." are consecutive sentences with two different "It"s (communal ownership; expletive). Reread risk. "will get rid of" is future tense inside generic present discussion.

---

## R-C11a (answers original P11)

**Forward**

| # | Original unit | Rewrite | Mark | Note |
|---|---|---|---|---|
| 1 | "The desire to return to a natural way of living together" | "The desire to go back to a natural way of living together" | SAME-MEANING | "return to" becomes "go back to". |
| 2 | "has outrun the knowledge" | "has outrun the knowledge of how to actually do it" | SHIFTED | The original leaves "the knowledge" open; the later "don't know" items fill it with why communities failed, why conflicts return, how fast land stops mattering. The rewrite states it outright as practical know-how ("how to actually do it"). |
| 3 | "People know they're lonely and exhausted." | identical | SAME | |
| 4 | "They usually don't know why so many earlier communities failed" | identical | SAME | "usually" kept. |
| 5 | "why the same conflicts keep returning" | "why the same conflicts keep coming back" | SAME-MEANING | |
| 6 | "or how quickly beautiful land becomes irrelevant" | "or how quickly beautiful land stops mattering" | SAME-MEANING | "irrelevant" becomes "stops mattering". |
| 7 | "once money, children, jealousy, and ownership enter the picture" | "once money, children, jealousy and ownership come into it" | SAME-MEANING | All four items kept. "enter the picture" becomes "come into it". |

**Reverse (ADDED)**

| # | Rewrite wording | Kind | Note |
|---|---|---|---|
| A1 | "of how to ... do it" | claim about what is missing | Names the missing knowledge as know-how. See Forward 2. |
| A2 | "actually" | intensifier | Not in the original. |

**Sources.** No links, no quote marks. "People" and "They" are the actors in both.

**Sense**

| Word or phrase | Referent visible? | Note |
|---|---|---|
| "do it" | Yes: "go back to a natural way of living together". | |
| "come into it" | No explicit antecedent. Candidates: "beautiful land", the community, the situation. | Reread. The original had "enter the picture". |
| "natural way of living together" | "natural" is not glossed. | Same in the original. |
| "the same conflicts" | "same" as which is not visible. | Same in the original. |
| Tense | "has outrun" present perfect; "failed" past; "keep coming back" present. No slip. | |

## R-C11b (answers original P11)

**Forward.** Units 1 to 5 are identical to R-C11a (1 SAME-MEANING, 2 SHIFTED, 3 SAME, 4 SAME, 5 SAME-MEANING). In the rewrite, unit 5 ends the sentence ("or why the same conflicts keep coming back.").

| # | Original unit | Rewrite | Mark | Note |
|---|---|---|---|---|
| 6a | "usually" covering the third item ("They usually don't know ... or how quickly ...") | "And they don't see how quickly ..." (a separate sentence) | DROPPED | The hedge "usually" no longer reaches the third item. That item is stated flat. |
| 6b | "don't know" | "don't see" | SHIFTED | Minor. "not know" becomes "not see", i.e. not recognize or notice. |
| 7 | "how quickly beautiful land becomes irrelevant" | "how quickly beautiful land stops mattering" | SAME-MEANING | |
| 8 | "once money, children, jealousy, and ownership enter the picture" | "once money, children, jealousy and ownership come into the picture" | SAME-MEANING | |

**Reverse (ADDED).** A1 "of how to ... do it" and A2 "actually", as in R-C11a.

**Sources.** As R-C11a.

**Sense.** As R-C11a, except "come into the picture" has no unclear "it". "they" in "And they don't see" = "People", visible. Starting a sentence with "And" is not a referent problem.

---

## R-C12 (answers original P12)

**Forward**

| # | Original unit | Rewrite | Mark | Note |
|---|---|---|---|---|
| 1 | "I'm not currently recruiting anyone" | "I am not currently recruiting for a community" | SHIFTED | Minor. The denial's object changes from persons ("anyone") to a purpose ("for a community"). "currently" kept. |
| 2 | "or founding a community" | "or attempting to start one" | SHIFTED | Minor. "founding" (establishing) becomes "attempting to start" (any attempt). The denial now also covers attempts, so it is the broader claim. |
| 3 | "That makes this easier to write" | "which makes it easier for me to write an article like this" | SHIFTED | Minor. "this" (this article) becomes "an article like this" (articles of this kind). Adds "for me" (the writer, implied in the original). |
| 4 | "because I'm not trying to get you onto my land" | "since I'm not trying to get you onto my land" | SAME-MEANING | "you" kept. |
| 5 | "I do plan to buy land" | identical | SAME | |
| 6 | "and people may naturally end up living around me" | "and people may naturally end up living near me" | SAME-MEANING | "around" (surrounding) becomes "near" (close by). "may" and "naturally" kept. |
| 7 | "Every warning in this article applies to me too." | "all of the warnings in this article apply to me, too" | SAME-MEANING | |

**Reverse (ADDED)**

| # | Rewrite wording | Kind | Note |
|---|---|---|---|
| A1 | "But" | contrast connective | Frames the last sentence as a qualification against what precedes. The original states it without a contrast. |

**Sources.** No links, no quote marks. Actors are the author and "you" (the reader) in both. "my land" is the author's land in both.

**Sense**

| Word or phrase | Referent visible? | Note |
|---|---|---|
| "one" | Yes: "a community". | |
| "which" | The whole preceding statement. | |
| "an article like this" | "this" = the article being read. | |
| "the warnings in this article" | Only some are in this section (R-C9 to R-C11). | Same in the original. |
| "But" | The contrast target is not stated. It could be "I do plan to buy land..." or "easier for me to write". | Reread. |
| Tense | No slip. | |

---

# Cross-paragraph sense check (R-section.md, a versions in order)

| Where | Word or link | Visible referent? | Note |
|---|---|---|---|
| H3 "The Freeloader Problem" | "Freeloader" | The word first recurs in R-C10a ("chronic freeloading"). R-C7a, R-C8 and R-C9a, which sit under the heading, do not use it. | Same in the original. |
| R-C1a to R-C2 | "that loneliness" | Yes: "loneliness" in R-C1a. | |
| R-C3, image 4, R-C4a | "this turn" | Yes: the upward bend in R-C3. | |
| R-C4a to R-C5 (unchanged) | "It's poppin' on Instagram too!" | "It" = the village or commune idea in R-C4a's last sentence. | R-C4a's last sentence is verbatim the original. Same in the original. |
| R-C5 to R-C6 | "Then another large influencer" | R-C5 ends "Imagine opening your inbox ... co-found a village." | Reread: "Then" can continue the imagined scenario. The original used "Another ... later". |
| R-C6 to R-C7a | "the comments" | Yes: the comments on the second influencer's post. | |
| R-C7a, image 5, R-C8 | "Those comments" | No single referent (objecting comments, the screenshot, or all the comments). | The original named them ("The commune comments"). |
| R-C8 to R-C9a | "this objection" | Yes: "The oldest objection" in R-C7a. R-C8 and image 5 sit between. | |
| Image 5 | the screenshot | In the original, P9's "that comment" is the only text pointing at the comment shown. No sentence in R-section.md points at it. | |
| R-C7a, R-C10a | "anarchism", "bosses" | Nothing visible links the commune idea to anarchism or to bosses. | Same in the original. |
| R-C9a to R-C10a | "Communal ownership needs" | The needs are not marked as following from R-C9a ("therefore" dropped). | See R-C10a Forward 1. |
| R-C10a | "the problem" | Yes: chronic freeloading in the previous sentence. | |
| R-C11a to R-C12 | "I am not currently recruiting" | No cross-reference needed. | |
| All paragraphs | Tense | No tense slip found in any rewrite or across paragraphs. | |

---

# Counts

Counts are per file. The a and b alternatives answer the same paragraph, so they are not additive. For a b file the count includes marks inherited from the a file (R-C1b, R-C9b, R-C10b, R-C11b).

| File | SHIFTED | DROPPED | ADDED |
|---|---|---|---|
| R-C1a | 1 | 0 | 1 |
| R-C1b | 1 | 1 | 1 |
| R-C2 | 3 | 1 | 3 |
| R-C3 | 1 | 0 | 1 |
| R-C4a | 0 | 0 | 0 |
| R-C4b | 1 | 4 | 1 |
| R-C6 | 2 | 3 | 1 |
| R-C7a | 0 | 0 | 0 |
| R-C7b | 4 | 0 | 4 |
| R-C8 | 2 | 0 | 2 |
| R-C9a | 1 | 0 | 2 |
| R-C9b | 1 | 1 | 2 |
| R-C10a | 0 | 1 | 0 |
| R-C10b | 2 | 1 | 1 |
| R-C11a | 1 | 0 | 2 |
| R-C11b | 2 | 1 | 2 |
| R-C12 | 3 | 0 | 1 |

R-C5 (the "It's poppin' on Instagram" paragraph) is unchanged and has no rewrite file.

# Summary table: changes that alter what a reader would believe about a fact, a person, or the author's position

Counts appear on the first row of each file. R-C4a and R-C7a have no such change.

| File | S | D | A | Change |
|---|---|---|---|---|
| R-C1a | 1 | 0 | 1 | "suddenly everywhere" becomes "suddenly in the air": how widespread the longing is said to be goes from ubiquity to an ambient presence (minor). |
| R-C1b | 1 | 1 | 1 | Same "in the air" change. "rather than a sentimental extra" is dropped: the advisory is still said to call connection a public-health issue, but the view it is said to reject is gone. |
| R-C2 | 3 | 1 | 3 | The author's own stance ("I'm less interested in declaring an official 'epidemic' than in the obvious fact underneath it") becomes "Whether you want to call that loneliness an 'epidemic' or not": his priority and "official" are gone and the label is left to the reader. |
| R-C2 | | | | "They" becomes "People": the group said to agree that something is starving them widens from the many who can't tolerate isolated life to people in general, or reads that way. |
| R-C2 | | | | "the current arrangement" becomes "the way things are now": what is said to be starving people goes from a social set-up to circumstances in general (minor). |
| R-C3 | 1 | 0 | 1 | The trend becomes "you can see that ...": presented as visible in the linked Trends data, not as the author's statement. |
| R-C4a | 0 | 0 | 0 | none |
| R-C4b | 1 | 4 | 1 | Four named effects of AI (jobs, feeds, relationships, expectations of the future) become "changing the way people live": a specific claim becomes a broad one. |
| R-C6 | 2 | 3 | 1 | "prospective members" becomes "future members": people in the comments are described as ones who will join, not might. "might normally" becomes "would normally" (hedge gone). |
| R-C6 | | | | "It was chaotic, sincere, and revealing." is dropped: the author's judgment of the episode, including that the participants were sincere, is gone. |
| R-C7a | 0 | 0 | 0 | none |
| R-C7b | 4 | 0 | 4 | The commenters' objection is reported differently: "anarchism requires" becomes "a working anarchism would require of them" (a functioning anarchism, conditional). The non-joiners are described as not commenting "with interest" instead of not "trying to join". |
| R-C8 | 2 | 0 | 2 | The claim about Instagram flips: "as Instagram comments sometimes do" becomes "which you don't normally find on Instagram" (usual becomes unusual). "Those comments" may cover fewer comments than "The commune comments". |
| R-C9a | 1 | 0 | 2 | The concession ("applies more to large socialism experiments than small communes") now attaches to the objection itself, not to one comment (the one in image 5). "since" adds a stated reason the objection deserves an answer, which the original did not state. |
| R-C9b | 1 | 1 | 2 | Same as R-C9a. "then" is dropped: the leaders' gain of power is no longer a later step after the same three people do everything (minor). |
| R-C10a | 0 | 1 | 0 | "therefore" is dropped: the needs no longer follow from the argument before them. |
| R-C10b | 2 | 1 | 1 | Same "therefore" drop. "A community cannot run on the assumption that removing bosses removes ..." becomes "It's naive to think that getting rid of bosses will get rid of ...": a claim about what a community can't do becomes a judgment of people who believe it ("naive"), in the future tense. |
| R-C11a | 1 | 0 | 2 | The missing "knowledge" is now stated as "of how to actually do it" (practical know-how); the original left it open. |
| R-C11b | 2 | 1 | 2 | Same know-how change. The hedge "usually" no longer covers the third item, and "don't know" becomes "don't see": a flat claim about what people fail to see. |
| R-C12 | 3 | 0 | 1 | The author's disclosure is reworded: "recruiting anyone" becomes "recruiting for a community"; "founding a community" becomes "attempting to start one" (a broader denial); "this" becomes "an article like this"; "But" is added before "all of the warnings ... apply to me". |
