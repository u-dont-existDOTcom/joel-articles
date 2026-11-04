# Writer brief: Healing the Gut, batch 2 (the fuels under Leaky gut, and the ready-made stacks)

You are rewriting three stretches of Joel Rosenblum's post "Healing the Gut Naturally" so they read as Joel's own writing. All three read AI on Pangram 4.1 (High confidence): Gemini wrote them, in Gemini's voice, and Joel kept them. Your job is the voice, not the content.

## Read first, in full

1. `../../b1-protocol/briefs/ARTICLE-r01.md`: the whole post as it now stands. The causes list at the top is Joel's own writing and reads Human at High confidence; the other items under "Leaky gut" (colostrum, zinc carnosine, BPC-157, zeolite...) are the voice to match: short items, plain, a bit loose, his asides ("altho", "Note: I think..."), first person where he has a view.
2. `../../b1-protocol/briefs/JOEL-FIXES-CATALOGUE-20260928.md`: Joel's own before/after fixes. Your main teacher. For each unit, find the two or three fixes closest to it and work the way he did.
3. `../../b1-protocol/briefs/GATE-OWNER-RULINGS.md` and `../../b1-protocol/briefs/HUMANIZATION-TELL-INVENTORY.md`: his rulings and the tells.

## What batch 1 taught (the protocol phases, checked today)

Versions that passed: plain sentences that just say the step; a question to the reader where the original had a check ("Are you sensitive to everything?"); the Source/Logic/Protocol labels gone; Joel's own lines left alone.
Versions that read AI: a question the text answers itself ("Why so strict? Because..."); attribution asides around each step ("like Pimentel says", "We're back to Dr. Davis for this one"); a staged run of short rule sentences ("Start with the diet."); the same check, consequence, fix cadence repeated step after step.

## The units (`../UNITS-r01-b2.json`)

- **LGF**: the last item under "Leaky gut" in the causes list, a nested list on the mitochondrial fuels (glutamine, butyrate/SCFAs, TCA intermediates). It stays where it is, as part of Joel's Leaky gut list (he ruled the fuels are critical for leaky gut; Phase 5 points back to them). Keep it a list item (with sub-items if you want), indented as it is: it starts with "  - " at the same level as the colostrum and zinc carnosine items.
- **ST1**: the heading "## Optional Ready-Made Gut Stacks", the paragraph on why there is no universal stack, and the three categories to look for.
- **ST2**: the three paragraphs that follow: the kits, the "gut cleanse" stacks, and start low / see a clinician.

## Joel's answer to fold into ST2 (his words, 2026-11-03)

About the kits ("The best general commercial stack I have seen so far is..."): "actually i mean gemini gave me these suggestions but so far they are the best kits i've seen... tho haven't used them myself. peoiple can check the reviews."

So ST2 must say, in his voice: these kits were Gemini's suggestions; so far they're the best kits he's seen; he hasn't used them himself; people can check the reviews. Don't say anything more about them than that (no "I've heard good things", no star ratings, no "many people report").

The parenthesis at the end of the cleanse-stacks paragraph, "(My own advice is different for H. pylori, where berberine works well: see Parasites, above.)", is a note Joel approved today. Keep what it says (it may be reworded lightly, or kept as it is).

## Must keep, in every unit

- Every compound, product, brand, number, dose, condition and warning: 5g daily baseline; 10-30g; CrossFit or intense cardio; acute immune exposure, high systemic stress, active IBD (Crohn's/Colitis); the cancer caveat (active colon or liver malignancy; the liver sees it first via portal vein delivery); enterocytes (small intestine) and colonocytes (large intestine); LPS and endotoxins; alpha-ketoglutarate (α-KG) and the citric acid cycle; short-chain fatty acids (SCFAs) and butyrate; raw resistant starch fermentation; home-brewed SIBO yogurt; malate and citrate, organic malic acid, tart cherries, green apples; Microbiome Labs Total Gut Restoration, Dr. Ruscio's Leaky Gut Support Kit, Designs for Health GI Revive and why each is named; oregano oil, wormwood, black walnut, berberine; overgrowth, parasites, H. pylori; the whole list of people who should see a clinician (severe pain, GI bleeding, fever, dehydration, rapid weight loss, active IBD flares, cancer, immune suppression, pregnancy, complex medical conditions); start low with prebiotics, resistant starch, butyrate-support products and probiotics.
- The link "watch Dr. Rhonda vid" (same URL, same or equivalent words).
- Each claim's strength. Gemini's intensifiers can become plain words when the claim stays as strong ("the absolute premier energy substrate" can be "the main fuel"; "massive amounts" can be "a lot"); a word that carries the claim stays ("directly", "rapid", "prevents", "locks down" can be plainer but not weaker: "may help" for "prevents" is a FAIL).
- The order of the treatment reasoning in ST1 (fix digestion mechanics first, reset diet and motility, only then antimicrobial or anti-parasite protocols if symptoms persist) and the three categories.
- Straight apostrophes and quote marks only.

## Must not

- Add facts, experiences, people, opinions or claims that aren't in the unit or in Joel's answer above. Don't say Joel tried something.
- Add jokes, emoji, slang or deliberate errors to look human. Don't fake his humor.
- Turn a claim into a vaguer one, merge two so one is lost, or change a "may" into a "will" or the reverse.
- Use "kitchen" details, "isn't proof of / doesn't prove", or the clipped "X. Not really Y." cadence.
- Use em dashes.

## Form

Markdown limited to: paragraphs, "- " bullets (indented "  - " and "    - " for LGF's nesting), "1. " numbered items, **bold**, *italic*, [link text](url), and the ST1 heading line "## ...". The heading's words may change if you think it reads AI; say so in your notes.

## Output

Write a JSON object to the output path you are given: `{"LGF": {"text": "...", "notes": "at most 30 words: what you changed and which catalogue fixes you used"}, "ST1": {...}, "ST2": {...}}`. Validate that it parses and has all three keys.
