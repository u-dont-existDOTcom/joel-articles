# Tells coverage: what the linter checks (2026-10-11)

Scope: every tell named in `AGENTS.md` (AGENTS), `SKILL.md` (SKILL), `docs/HUMANIZATION-GATE.md` (GATE), `tools/humanization/TELLS-FROM-PANGRAM-DATA-20261007.md` (PANG) and `tools/humanization/JOEL-FIXES-CATALOGUE-20260928.md` (CAT), tested against `tools/humanization/tells_lint.py`. Files and line numbers are as of commit `cf89ab2f`.

## Summary

- The five documents name **131 tells**. **82 are mechanical** (a regex, a word list or a count can find them) and 49 need a reader.
- The linter **checks 51** of the 82. Two of the 51, misspellings and odd hyphenation (O15), fire only when pyspellchecker is installed. This checkout's python3 doesn't have it, so a plain run skips them and prints a note.
- It **misses 31** (table 1). The largest group is first-person staging: SKILL's "I care about...", "I'd want to see..." and "that tells me...", three of AGENTS's four significance-staging forms, and the curly-apostrophe spelling of the fourth. O20 only looks for "I want" at the start of a sentence.
- Some checked tells are caught in one spelling only. B2, B5, E41 and E138 match a straight apostrophe and miss a curly one, O2 needs "Fine," with a comma, and the acronym flag only sees capitals.

## How it was measured

- Each mechanical tell got a paragraph of two or three plain sentences in `/tmp/tells-audit/<id>.txt`. It was run from the repo root with `python3 tools/humanization/tells_lint.py /tmp/tells-audit/<id>.txt`; W77 also needed `--source`, since D9 compares against a source. When the tell got NONE, a plainer second example (`<id>b.txt`) ran before NONE was recorded. A flag counts only when its line quotes the sentence that carries the tell, or the paragraph for the count rules. Outputs are in `<id>.out`.
- This checkout's python3 has spaCy, but not WordNet or pyspellchecker, so a plain run uses O6's word list and skips O15. Every test was run again with both installed, in a scratchpad venv (`<id>.full.out`). The rule IDs matched, except that O15 fired on W18 and W19. With the parse, O6 also flagged two first drafts for reasons that had nothing to do with their tells ("The plan actually worked", and a 😉 that made spaCy read "balance" as a subject), so those two examples were reworded.
- Some rules were left out as rules about meaning or facts rather than tells: the rulings on rewriting his words (GATE:19–25), logical relations (GATE:41–45), stance (GATE:32, :301), invented life facts (GATE:228, :288) and claims about sources (SKILL:79–88). Also left out: what PANG says didn't hold up (surface counts and the mid-sentence colon, PANG:49–51), the moves that help (PANG:38–45; CAT:81–117), and inventory codes the documents name without their words (T03, T08, T12, T14, T20, T28, C01–C04, defined in `docs/HUMANIZATION-TELL-INVENTORY.md`).
- Extra probes for the notes below are X1 to X13 in the same folder.

## Table 1: MISSED (mechanical, linter NONE)

| ID | Tell (exact words) | Where | Examples run (A; then B, the plainest form) |
|---|---|---|---|
| W07 | "Even" ("They're words I add to sound casual, and they don't help") | PANG:33, :36 | A: "We painted the barn red that spring, and we even fixed the leak over the hayloft." B: "It was even colder in the barn than in the house that first winter on the land." |
| W08 | "actually" (same finding) | PANG:33, :36 | A: "The barn was actually warmer than the house during the first winter on the land." B: "The new pump actually worked, and it ran all summer without a single repair." |
| W10 | "lol" ("\"lol\" is wry, so it's out") | GATE:386; CAT:221 | A: "The goat ate the treasurer's notes again lol, so the budget vote moved to the next meeting." B: "The goat ate the treasurer's notes again, lol." The acronym flag is case-sensitive: "LOL" is flagged (X6). |
| W12 | "Never a pointer (👇 👉 👆 👈 ☝️)" | GATE:386; CAT:221 | A: "The sign-up sheet for the harvest crew is on the board by the kitchen door 👉 and it closes at the end of the month." B: "The sign-up sheet is by the door 👇 for anyone who wants a turn on the harvest crew this year." |
| W13 | "😉" | GATE:386; CAT:219, :221 | A: "The treasurer says the accounts add up this year 😉 and nobody has looked at them since spring." B: "The books balance this year, says the treasurer 😉." |
| W14 | an emoji off the allowlist ("everything else counts as banned until Joel says yes") | GATE:386 | A: "The new solar panels went up on the barn roof last week 🚀 and the lights stayed on all night." B: "The solar panels went up last week 🔥." |
| W20 | "double spaces" ("Rough edges he leaves: typos, double spaces, missing periods. ... They aren't something for me to imitate.") | CAT:116 | A: two spaces between "…after the harvest." and "The treasurer read…". B: two spaces inside "The council met  in the barn…". |
| W21 | "missing periods" (same line) | CAT:116 | A: a paragraph whose last sentence has no period ("…to everyone who came that night"). B: "The council met in the barn after the harvest The treasurer read the numbers aloud to everyone who came that night." |
| W23 | `I care about...` | SKILL:215 | A: "I care about how the group splits the money when a member leaves the farm." B: "I care about the shared money." |
| W24 | `I'd want to see...` | SKILL:215 | A: "I'd want to see the budget before anyone signs the lease on the new barn." B: "I'd want to see the numbers first." |
| W25 | `that tells me...` | SKILL:215 | A: "The well ran dry twice last summer. That tells me the group needs a second water source before the next drought comes." B: "That tells me something about the wiring in the old shed by the pond." |
| W27 | `That’s where X matters to me` (curly apostrophe, the form AGENTS writes first) | AGENTS:81 | A: "That’s where the council matters to me, since it decides who gets to farm the lower field." B: "That’s where the money matters to me." B5 only matches the straight "That's where" (W26). |
| W28 | `This is one reason I want X` | AGENTS:81 | A: "This is one reason I want the council to post its minutes every month on the board." B: "This is one reason I want a smaller council." |
| W29 | `The version I want is X` | AGENTS:81 | A: "The version I want is a council that meets in the open and posts its minutes on the board." B: "The version I want is smaller." |
| W30 | `What matters to me is X` | AGENTS:81 | A: "What matters to me is a council that posts its minutes every month on the board." B: "What matters to me is the budget." |
| W31 | research notes as narration: `I thought X`, `I had heard Y`, `I checked it`, `I wasn't sure what the term was`, `the check I did here showed...`; "a diary of `I thought → I checked → I learned`" | AGENTS:65, :92 | A: "I had heard the mill closed in 1990. I checked it against the county records, and the real closing date was 1987, three years earlier." B: "I thought the bridge was older. I checked it, and the town built the bridge in 1952 after the spring flood." |
| W33 | "I see the need to" | GATE:141 | A: "I see the need to write the guest rules down before the first big dispute comes up." B: "I see the need to keep better records." |
| W34 | "It's also important to" | GATE:141 | A: "It's also important to keep every receipt from the hardware store in one folder." B: "It's also important to rest." |
| W35 | "One thing to notice about" | GATE:141 | A: "One thing to notice about the old ledger is how often the same three names come up." B: "One thing to notice about the barn is the roof." |
| W36 | "sure. But" | GATE:141 | A: "The new pump works, sure. But it costs twice as much as the old one did to run each month." B: "Sure. But the new pump costs twice as much to run as the old one did each month." O2 needs "Sure," with a comma, and the period splits the sentence before O2 looks. |
| W38 | "Nope.", "Aww, buddy." | GATE:395 | A: "The puppy begged for a second dinner at the table. Nope. Aww, buddy. The vet wants him to lose two pounds before his checkup in the spring." B: "We asked whether the shop was open. Nope. The owner had gone fishing with his brother for the whole weekend." |
| W39 | "'i wouldn't call that X'" | CAT:123 | A: "The shed has a roof and three walls. I wouldn't call that a barn." B: the same line as the paragraph's first sentence. |
| W40 | "with or without X is not quite guidance" | GATE:233; CAT:315 | A: "The breathing exercise works with or without music in the background." B: "Do the exercise with or without music." |
| W41 | a "but also" pair | GATE:145 | A: "The garden feeds the whole house, but also teaches the younger members some patience." B: "The pump is cheap but also slow, and it takes an hour to fill the tank by the barn." |
| W55 | "Not X. It's Y." and its cousins | CAT:27–29 | A: "It's not a hobby. It's a job that pays the rent on the farmhouse every month." B: "Not a hobby. It's a job, and it pays the rent on the farmhouse every month." B11 has this pattern, but it tests one sentence at a time, so the pattern can never match. The cousin "The point is not… The point is…" (CAT:28) only gets E41, for "the point is" (X5). |
| W58 | "It's one thing to X. It's another to Y" (Emulate's "one thing ... another thing") | CAT:278, :288 | A: "It's one thing to talk about a universal consciousness. It's another to struggle to escape one man's opinions about everything on the farm." B: "It's one thing to plan a garden. It's another to weed it every morning through the whole of July." |
| W62 | "question runs" | GATE:357 | A: "Who pays for the new roof? Who fixes the well when it runs dry? Who keeps the books after the treasurer moves back to the city?" B: "Who pays? Who fixes it? Who keeps the books after the treasurer moves back to the city next year?" |
| W63 | the parallel "who is … who is … or who is" list | CAT:421 | A: "The facilitator on the retreat circuit may be someone who is a sexual predator, who is financially dependent on people coming back, or who is simply wrong." B: "She could be someone who is kind, who is tired, or who is lost." E125 skips a list whose middle item starts with "who". |
| W80 | a phrase repeated in one paragraph ("gave P22 its fourth \"as adults\"") | GATE:107; CAT:554 | A: "The members sign the land trust as adults. They pay their share of the dues as adults. Later their children can join the trust as adults too, …" B: "The members make the choice as adults and keep it as adults. They can also leave as adults whenever they want to go." |
| W81 | two parallel "When…, don't…" lines | CAT:150 | A: "When the toddler cries at night, don't rush in right away. When she calms down, don't lecture her about it at breakfast." B: "When she cries, don't rush in. When she calms down, don't lecture her." |
| W82 | an "is a kind of love, … but it's not the whole thing" line | CAT:151 | A: "Keeping the promise is a kind of love, but it's not the whole thing." B: "It's a kind of love, but it's not the whole thing." |

## Table 2: CHECKED

| ID | Tell (exact words) | Where | Linter rule |
|---|---|---|---|
| W01 | "boring" ("Treat `boring`, `quietly`, and `ordinary` as AI-frequency-risk words"; "the boring problem") | AGENTS:82; GATE:130, :450; CAT:460, :469 | O12 |
| W02 | "quietly" ("using quietly all the time like that is a huge AI tell") | AGENTS:82; GATE:130, :450 | O12 |
| W03 | "ordinary" | AGENTS:82; GATE:409, :450; CAT:460 | O12 |
| W04 | "regular" | GATE:409, :450; CAT:460, :469 | O12 |
| W05 | "everyday" | GATE:409, :450 | O12 |
| W06 | "mundane" | GATE:450 | O12 |
| W09 | "never \"the kid\"" | GATE:324, :438 | E1 |
| W11 | "Chat acronyms (IMO, TBH and the like)" | GATE:403, :439 | the chat-acronym flag, which has no rule ID (capitals only) |
| W15 | `on Tuesday`, `last Tuesday`, `Tuesday afternoon`; "on a regular Tuesday is the worst" | SKILL:96; GATE:409, :427; CAT:460 | O11 (FAIL) |
| W16 | "day-of-week or clock-time details"; "a made-up number or clock time" | SKILL:96; GATE:409, :453 | O13 (tested with "7 pm") |
| W17 | "five percent is enough"; "how much is 5%?" | GATE:410, :453; CAT:461 | O13 |
| W18 | "unusual spellings" ("priveleged"); "Never add errors" | GATE:52, :57, :443; CAT:116, :519; SKILL:283 | O15, only with pyspellchecker; a plain run here skips it (NONE) |
| W19 | "an unusual spelling or hyphenation" ("re-incarnation", "pre-requisite") | GATE:57, :443; CAT:519 | O15, same condition |
| W22 | `I want...`, `I don't want...`; "\"I want\" or \"I don't want\" opening a stance" | SKILL:215; GATE:33, :131, :451; CAT:284 | O20 (only at the start of a sentence) |
| W26 | `That's where X matters to me` (straight apostrophe) | AGENTS:81 | B5, on the "That's where" opener |
| W32 | "my first guess", "I'd probably want to", "I'd be tempted to" | GATE:411, :456; CAT:459 | E138 (straight apostrophe only, X2) |
| W37 | "\"Fine,\" \"Good,\" \"Great,\" as a clause of their own" | GATE:401; CAT:129, :478 | O2 (FAIL; comma form only: "Fine. They're nice boots…" is CLEAR, X4) |
| W42 | "X with a nicer logo", "X with extra steps" | GATE:132, :452 | O21 |
| W43 | smuggling talk: "not smuggled into one sentence here" | GATE:413, :425 | O8 (FAIL), also O9 |
| W44 | "individual coach phrases" ("You might notice…") | GATE:437, :563 | E41 (one phrase in a 31-word paragraph also trips the E41 density FAIL) |
| W45 | an "if you do, you might" consequence | CAT:227; PANG:20 | E41, on "you might" |
| W46 | an action "it" ("did it", "do it", "tried it") | GATE:446; CAT:197 | R1 |
| W47 | "Key here is that…" | GATE:49, :426; CAT:420 | O10 (FAIL) |
| W48 | "\"doesn't get to decide\" and its family … when the subject isn't a person" | GATE:400, :428; CAT:128, :477 | O1 (FAIL) |
| W49 | an x-not-y heading ("The Medicine Part, Without Pretending It Isn't There") | GATE:47, :133, :426; CAT:419 | H1 (FAIL) |
| W50 | "a negation in a heading" | GATE:432 | H1 (REVIEW) |
| W51 | a pointer word ("This", "It", "The other") opening the first paragraph under a heading | GATE:432 | O10 (REVIEW) |
| W52 | "A \"not Y\" tail on a finished claim"; Emulate's "not the other way around" | GATE:414, :433; CAT:256 | O9 |
| W53 | "Not x, but still y." ("It isn't proof, but it still counts") | GATE:405, :454; PANG:52; CAT:482 | O18, also B2 and B1. PANG:52 still calls it O14, which is now the "and … and … and" rule. |
| W54 | "may have X and still Y"; "may be X and still Y" | GATE:95, :405; CAT:532 | O17, also B1 |
| W56 | "isn't X, it's Y" | GATE:357 | B2 (straight apostrophes only, X1) |
| W57 | "always trying to do an x not y statement" (tested in a sentence: "not X but Y") | GATE:47, :405; CAT:419 | B2 |
| W59 | a balanced "X enough to A and Y enough to B" pair | GATE:448; CAT:256, :265 | O7 |
| W60 | an objection in "an \"even if\" clause" | GATE:395; CAT:294 | B1 |
| W61 | a closing line that sums up: "These are all questions that a community should consider in advance." | GATE:59, :444; CAT:520 | O16 |
| W64 | "lists of 3 in general are an ai pattern"; "triads" | GATE:357, :408, :441; CAT:45, :355 | E125 (REVIEW) |
| W65 | "P! failed b ecause it has 2 lists of 3" | GATE:94, :430; CAT:75, :532 | E125 (FAIL) |
| W66 | "a bulleted or numbered list" ("lists in general are overused by AI") | GATE:404, :455; CAT:480 | O19 |
| W67 | Emulate's "and … and … and" | GATE:57, :429, :442; CAT:521 | O14 (FAIL), also B4/E15 |
| W68 | "packed or list sentences" | GATE:347, :440 | B4/E15 |
| W69 | "contrast constructions" | GATE:434 | B2 (tested with "rather than") |
| W70 | "short knock-downs" | GATE:445 | B3 |
| W71 | "short paragraph-final lines" | GATE:449 | B7 |
| W72 | "half or more of the paragraphs ending on a short line" | GATE:422 | B7, and HARD B7/B13 |
| W73 | "three or more paragraphs with the same opener" | GATE:119, :424 | HARD B13 |
| W74 | "two or more paragraphs that are strings of instructions" | GATE:423 | E23, and HARD E23 |
| W75 | "coach phrases above 2 per 100 of my words" | GATE:421 | E41, and HARD E41 |
| W76 | "second person above 6 per 100" | GATE:457 | E36/E41 |
| W77 | "the draft follows the source's order (D9)" | GATE:458 | D9 (needs `--source`) |
| W78 | "Abstract concepts or feelings as agents" ("the anger goes there"; "goodwill doesn't answer those questions") | GATE:103, :406, :447; CAT:275, :541 | O6, as a candidate (the word list caught it here, and the parse does too) |
| W79 | "his Claude tics"; "Joel's tics" | GATE:399, :420 | B11 (FAIL). Tested with "load-bearing" from `reviewer/owner_bans.txt:8`, since the five documents don't list the words. |

## Table 3: JUDGMENT

| ID | Tell (exact words) | Where | Why it needs a reader |
|---|---|---|---|
| J01 | "and close syntactic variants" of significance staging; "and close variants" of `I care about...` etc.; "oddly arrogant or performatively intimate" | AGENTS:81; SKILL:215–216 | The variants are open-ended, and his own wish as the subject is allowed. |
| J02 | editor-facing rationale (`this is important because it connects with my other articles`); "explaining to the editor/model why the material matters" | AGENTS:53, :57, :91 | Whom a sentence addresses is a reading. |
| J03 | unanchored `this`, `that`, `it`, `here`, `earlier`, `what I mean`; "an undefined referent"; "A12 referents"; "Both kinds"; "for an actual case" | AGENTS:52, :57; GATE:97, :324; CAT:457, :533 | It needs the text before it. R1 and O10 catch two narrow forms. |
| J04 | pointers sections back ("like before", "the goodwill prayer from before", "it's the food bank all over again") | GATE:230; CAT:316, :324 | The distance to the referent needs the article. |
| J05 | a term the prose "refers back to" before it's introduced; "E8 and E33 premises and terms not yet introduced" | AGENTS:55; GATE:324 | It needs the article so far. |
| J06 | "least qualification necessary"; "skeptical aftercare explaining non-implications"; "prosecutorial language" | SKILL:67, :69, :71 | It depends on what a reader would infer. |
| J07 | "aftercare that merely explains why a point was made, repeats an already available inference, labels a demonstrated dynamic, or fills conceptual space"; "unnecessary recap/interpretive aftercare" | SKILL:104, :165 | It's a function, not a form. |
| J08 | "concrete image followed by explanatory aftercare"; "an image or an example made up to explain" | SKILL:201; PANG:26–31 | Whether the image was needed is a reading. |
| J09 | overcompletion: "you already have it explained and then you explain it again"; "functional redundancy"; "Over-explaining listicles" | GATE:98, :412; SKILL:165; CAT:308, :548 | It needs what was already said, and the sentence's job (GATE:106). |
| J10 | "an exhaustive list"; covering "every case": "the rule, its exception, the exception's own exception, and a safety carve-out" | GATE:59; PANG:61 | Exhaustive relative to the source. PANG:62 calls it a guess. |
| J11 | a last line that sums up: "ensuring the thought is fully complete and summed up perfectly"; "bringing it all together in the most defensible way possible"; "an ending that restates the thesis or reframes it"; "a last sentence that concluded the paragraph" | CAT:23, :123; GATE:352, :359, :563 | O16 catches one fixed form (W61). Summing up in general is a reading. |
| J12 | a closing gloss: "a second point added after the paragraph had already made its own" ("a caveat", "a consequence", "a moral", "an aphorism", "a tender beat"); a last sentence opening "So", "That way", "It just", "Then again", or That, This, It, So or Which | PANG:17–23, :50 | PANG:50: 6 failing against 7 passing, so "A reader has to judge it". |
| J13 | "matched pair ending on punchline gives it away"; "a punchy closer"; "a poignant last line" | CAT:25; GATE:395 | Tone. |
| J14 | "Wry humor" ("wry in a strange way which i can't pin down"; "lol ... it's more wry") | GATE:402; CAT:37, :221 | Tone, and Joel can't pin it down. |
| J15 | a quip AI colonized: "just with longer meetings and fewer robes"; "the 1972 line is witty altho it's kind of an obvious ai quip"; "a quip per beat"; "semi quip" | GATE:38, :516; CAT:240, :255, :307 | "whether a line is a quip at all stays a reader's call" (GATE:132). O21 has only two stock forms. |
| J16 | "Too many made-up scenes"; "a textbook dinner vignette" | GATE:407, :548; CAT:130 | Knowing what's made up needs the source. |
| J17 | "synthetic didactic prop selection"; "the generic image for a specific, silly one" | SKILL:201; GATE:50; CAT:423 | A judgment of quality. |
| J18 | "fabricated scheduling, scenery, or incidental specificity"; "fake specificity"; "E36 details that fit every reader" | SKILL:98, :283; GATE:324 | It needs the source. Weekdays and clock times are mechanical (W15, W16). |
| J19 | "fake-spontaneity markers"; "filler/hesitation is earned or stage-managed"; "asides shaped like his"; "a goofy exclamation"; "speech markers laid over AI shapes" | SKILL:201, :207, :220; GATE:141, :395 | Earned or staged is a reading. The fixed "Nope." and "Aww, buddy." are W38. |
| J20 | T02 "instruction-manual cadence": "one-function-per-sentence marching"; "the next sentence lands like code without a hitch"; "a definition sentence for each job" | SKILL:171, :217; GATE:318, :322, :395, :541; CAT:121, :376 | It's a property of the sequence. E23's imperative count is a proxy (W74). |
| J21 | T09 "equal efficiency": "Optimal efficiency"; "suspiciously efficient equality"; "equal weight"; "five even items" | SKILL:207, :218; GATE:322, :565; CAT:424 | GATE:565 says it "isn't mechanical". |
| J22 | T13 "nothing noticed"; "organization needs to be not reducible to code" | GATE:297, :322, :565; CAT:125 | GATE:565 says it "isn't mechanical". |
| J23 | "one source function per scene beat"; "a scene that just skins the source's order still fails" | SKILL:201, :205; GATE:179 | It needs the source map. |
| J24 | "Abrupt complication" | SKILL:219 | Whether the turn has a visible reason is a reading. |
| J25 | "generic therapeutic abstraction"; "abstractions became happenings" | SKILL:201; CAT:240 | An open class of words. |
| J26 | "tighter, more exact, more formal or more hedged" wording | GATE:143 | Only relative to a looser wording. |
| J27 | "stacked hedges"; "the hedging self-talk (\"rein in my enthusiasm\")"; "The hedge \"and it might be right\" went" | GATE:114, :563; CAT:199 | GATE:563 says it "isn't mechanical". |
| J28 | "a therapist's sequence", "a reassuring close" | GATE:563 | The same line says they aren't mechanical. |
| J29 | "a tidy taxonomy"; "Taxonomy inside a list item" | GATE:565; CAT:46 | GATE:565 says it "isn't mechanical". |
| J30 | "Telegraphic fragments" | CAT:56 | "Bare items that were already fine stay bare" (CAT:72). |
| J31 | "Reassurance and commentary about the text itself" | CAT:30 | It's a function. |
| J32 | "Mechanism talk and over-precise sourcing" | CAT:38 | It depends on what the reader needs. |
| J33 | "The bridge sentence that announces the next move"; "generic bridges"; "lines that announce a paragraph (B5)" | CAT:41; SKILL:165; GATE:436 | It's a function. B5 flags a few openers only. |
| J34 | "finished principles (B1)" | GATE:435 | It's a function. B1 flags proxies ("even if", "still counts", a "Most…" opener). |
| J35 | "The moral stated as an antithesis" | CAT:49 | It's a function. |
| J36 | "false symmetry/completeness" ("Both approaches fail for symmetric reasons") | SKILL:165; CAT:279 | A reading. |
| J37 | "pre-completed reasoning" | SKILL:165 | A reading. |
| J38 | "a thesis stated before the first part"; "a topic-sentence opener"; "a thesis opener"; "a claim opener" | GATE:353, :524, :527; CAT:149 | A reading. |
| J39 | "a summary or synthesis stage" | GATE:354 | A shape of the whole section. |
| J40 | "stakes escalated" | GATE:355 | A reading. |
| J41 | "the editorial-explainer voice" | GATE:356 | A register. |
| J42 | insight that's set up "too much rather than throw it in where it naturally arises" | CAT:124 | A reading. |
| J43 | "the 3 part conditional syntax" | CAT:123 | The documents don't say what the form is, so no pattern or test can be written from them. |
| J44 | "questions the text answers itself" | GATE:141; CAT:566, :582 | Whether the next line answers the question is a reading. |
| J45 | advice turned into an observation ("it sounds like it's making an observation ... but it is supposed to advise") | GATE:49; CAT:422 | It needs the sentence's intended job. |
| J46 | an emoji that "only labels a thing or an activity" (🐶 🎶 💆 🔥); "gratuitous emojis" | GATE:386; CAT:221 | A reading. The allowlist itself is mechanical (W14). |
| J47 | "catchphrases, unusual punctuation, slang, or corpus tics" added to improve similarity | SKILL:283 | Not defined in the documents; it depends on his corpus. |
| J48 | "a list of conditions", when every fix adds a clause | GATE:395 | A property of the sequence. |
| J49 | a practice paragraph that ends "on a prediction of how the reader will sound" or "on a technique" | CAT:188, :194 | A reading. |

## Reverse: linter words and patterns the five documents never name as tells

- **B11 (FAIL):** "doing some work", "tells on itself", "metaboli[sz]", "digest", "clean" and "does its work". "load-bearing" appears only as an ordinary word (SKILL:63, :207). The documents say only "his Claude tics" (GATE:399) and "Joel's tics" (GATE:420), and the words live in `reviewer/owner_bans.txt:8`. Any "clean" fails a draft: "The kitchen was clean by the time the guests arrived…" gets B11 FAIL (X7).
- **B2:** "rather than", "instead of", "doesn't mean … means", "It's tempting", "not the same as", "is still a long way from" and "the difference between". The documents only say "contrast constructions (B2)".
- **B1:** "and still/yet" outside O17's modal form, "even though", "enough to … but/not", "not necessarily", "anyway.", "only gets you", and sentences opening Most, Nobody, Everyone, Everybody, People, Kids, Children, No one, Plenty of or Anybody who. The documents name "finished principles (B1)", "even if" and "still counts".
- **E41:** "you'll want/need/probably", "at some point", "that's fine/okay/ok/normal/all right", "it helps", "start by/with", "the next step", "don't be surprised", "it's tempting", "you don't have/need to", "keep in mind", "remember that/to", "give yourself", "it's okay to", "the goal is", "the point is", "in other words" and "go easy". The documents name "you can" and "you might" (GATE:313, :563). One of these runs against the documents: Joel's own break, "If nothing comes, that's fine for now" (GATE:395; CAT:368), gets E41 and the coach-density FAIL when linted alone (X9).
- **B5:** the openers "Or maybe", "For x,", "Here's", "The next step", "Now,", "First,", "Second,", "Finally," and "So the next", plus any short "X is …." sentence.
- **O2:** "Okay", "OK" and "Fair enough".
- **O16:** "This is why", "That's why", "In short", "In the end", "Ultimately", "Taken together", "In sum", "To sum up" and "All of these". The documents give only "These are all questions that…".
- **O10:** "Here's the thing/deal/key" and "key thing here".
- **E138:** "my first thought/instinct/reaction" and "my instinct would be".
- **O20:** "I wish", "I would like" and "I'd like". The "'d like" branch can't match, because the pattern wants a space after "I": "I'd like a smaller council that meets in the open." is CLEAR (X13).
- **O21:** better, fancier, shinier, prettier or new with logo, name, label, branding, font, website or mission statement.
- **O1:** "gets to choose/pick/vote/call/run/set", "the last/final word/say" and "gets a say/veto".
- **O13:** "o'clock", "by dinner/noon/bedtime/lunchtime" and "afternoon/evening of".
- **Chat acronyms** beyond IMO and TBH: IMHO, FWIW, IIRC, AFAIK, NGL, IRL, ICYMI, TL;DR, BTW, OMG, LOL, SMH and YMMV. The gate's "and the like" covers them.

## Notes

- **Curly apostrophes:** B2, B5, E41 and E138 spell their patterns with ' only. Each curly version came back CLEAR where the straight version was flagged: "That’s where…" (W27 against W26), "The fence isn’t a wall, it’s a promise…" (X1 against W56), "I’d be tempted to…" (X2 against X3), and "You’ll want to store…" (X10 against X11). AGENTS:81 writes the curly form, and his own paragraphs keep his characters (GATE:31).
- **Punctuation:** O2 needs a comma after the word. "Fine. They're nice boots…" (X4) and "Sure. But…" (W36) are both CLEAR.
