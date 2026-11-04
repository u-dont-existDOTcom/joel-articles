# Writer brief: Healing the Gut, the protocol section (batch 1)

You are rewriting the protocol section of Joel Rosenblum's post "Healing the Gut Naturally" so it reads as Joel's own writing. Each phase currently reads 100% AI on Pangram 4.1: it is Gemini's summary of nine gut-health books, in Gemini's template voice. Joel has approved the structure; your job is the voice.

## Read first, in full

1. `ARTICLE-r01.md`: the whole post as it now stands. The first part (the causes) is Joel's own writing and reads Human at High confidence. That is the voice to match: plain, direct, a bit loose, his asides, his "tho", his first person where he has a view.
2. `JOEL-FIXES-CATALOGUE-20260928.md`: Joel's own before/after fixes. Your main teacher. For each unit, find the two or three fixes closest to it and work the way he did (what he does to lists, what he cuts, what he adds, how he turns specs into questions to the reader).
3. `GATE-OWNER-RULINGS.md` and `HUMANIZATION-TELL-INVENTORY.md`: his rulings and the tells.

## The units

`UNITS-r01.json`: PI (the one-line intro to the protocol) and P1 to P6 (each phase: its heading, Source, Logic, Protocol steps and a "My notes" line).

## Must keep, in every unit

- The phase heading line exactly as it is (number and name; you may drop the nickname in parentheses only if you think it reads AI, and say so).
- Which book or author each step comes from (Ruscio, Pimentel, Hale, Rosenberg, Davis, Brown, Nathan, Hopper, Bulsiewicz), and the book titles.
- Every step, test, compound, product, dose, number, timing and warning, exactly: 4-5 hours, 36 hours, 30+ plants, 4 weeks, 2-3 weeks, 4+ hours, Stool Elastase, SeHCAT, Beet Flow, Phosphatidylcholine, Candibactin AR/BR, FC Cidal/Dysbiocide, H2O2, berberine, secnidazole, paromomycin, Zholy3O, S. boulardii, C. diff, L. reuteri, L. gasseri, DNRS, cholestyramine and the rest. Every link stays on the same words or on words that mean the same thing.
- The order of the steps, and each phase's trigger (when you move to it).
- Joel's own sentences inside the units word for word in meaning (Phase 3's H2O2 and Pooyan lines, "tho", "according to me and orthomolecular drs").
- The "My notes" line of each phase: Joel approved its wording today. Keep it as it is.
- Straight apostrophes and quote marks only.

## Must not

- Add facts, experiences, people, opinions or claims that aren't in the unit. Don't say Joel tried something he didn't say he tried.
- Add jokes, emoji, slang or deliberate errors to look human. Joel's humor is real when he has it; don't fake it.
- Turn a step into a vaguer one, merge two steps so one is lost, or change a "may" into a "will" or the reverse.
- Use "kitchen" details, "isn't proof of / doesn't prove", or the clipped "X. Not really Y." cadence.

## Form

You may change the form inside a phase: the "Source: / The Logic: / The Protocol:" scaffolding can become a sentence or two, a list can stay a list, become sentences or become questions to the reader, as Joel does in his catalogue. Keep it as easy to follow as a recipe; a reader has to be able to do the steps.

Write in Markdown limited to: paragraphs, "- " bullets, "  1. " numbered sub-items (two-space indent), **bold**, *italic*, [link text](url).

## Output

Write a JSON object to the output path you are given: `{"PI": {"text": "...", "notes": "at most 30 words: what you changed and which catalogue fixes you used"}, "P1": {...}, ... "P6": {...}}`. `text` is the unit's full new Markdown, heading line included (except PI, which has no heading). Validate that it parses and has all seven keys.
