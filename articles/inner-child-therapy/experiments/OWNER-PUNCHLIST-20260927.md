# Joel's punch list, 2026-09-27 04:19 UTC: fixes to installed sections

Status: **DONE. ALL NINE ITEMS ARE IN THE ARTICLE. THE ASK AND HOOK FIXES PASS ALONE AND IN THEIR SECTIONS. ALSO LOOK OUTWARD PASSES AS A SECTION; ITS P1 WAS NEVER HUMAN ALONE (REWRITE PROPOSED; OPEN-OWNER-FLAGS.md).**

Where to pick up: the last heading of this file. Process: `tools/HUMANIZATION-GATE.md`; lessons E59–E80.

## Joel's items (his words, trimmed)

1. Pema isn't introduced in Don't Give: "I guess we could change it to: 'Even Pema Chodron, who inspired parts of this guide, comes from ...'"
2. "then the 'if you're actually in danger' seems to come out of nowhere? cut that + the sentence after."
3. "the 4 paragraphs after 'borrow adulthood, do not surrender it' are supposed to be right before 'don't give the inner adult away' and remove the first 5 word sentence 'my own case was weird'"
4. "change 'Everybody gets thoughts like that sometimes' to 'Everybody gets scary thoughts they'd rather not have sometimes'"
5. "where did 'ask' get introduced? what is that talking about?" ("i know i told you this before but you didn't fix it")
6. "What is the 'hook' you jump into talking about in Catch the Hook?"
7. "change 'new age wisdom' to 'new-age wizdumb'"
8. "...and that somehow elevated the boundary crossing to 'They're evil.'"
9. "the first paragraph in Also Look Outward makes no sense. after 'irritating.' the next sentence is referring to what? and next and next... ?"

## Applied as Joel wrote them (owner text): items 1, 2, 3, 4, 7, 8

- Item 3 moved one more line than the four paragraphs: "The image below maps out the details as best as I can fit:". The last moved paragraph says "The three adult jobs from the map…", and the map line is what it points to, so they stay together, at the end of My Journey before the h3.
- How item 3 happened: it's the working source's order. `SOURCE-WORKING-20260925C.html` has "My own version was strange…" and the rest after "Borrow adulthood. Do not surrender it.", inside Don't Give. The humanized section kept that order, and no sense read of My Journey caught that his own story had ended up after Don't Give's conclusion.

## Item 5: the orphaned "ask" (flagged before)

Joel flagged it on 2026-09-24. `DANGEROUS-ADULT-BOUNDARY-SCOPE-EXTENSION-20260924.md` registered it as PU-ADJ-ASK-01 ("This setup must appear before the accepted humanized paragraph refers metalinguistically to quoted 'ask'"; "minimal insertion preferred"). Candidates G to I carried a fix and none was installed. It was never tracked after that, so it was lost (E80).

Minimal insertion: the prompt is named where the paragraph first refers to it.

> If you don't hear a little kid talking in your head, don't invent one. Actually, this is one place where the usual inner-child prompt to "ask your little one what they need" can get confusing, because "ask" sounds like you're supposed to ask a question and then wait for a second voice to answer. Maybe that's what happens for some people, but you might not be some people.

68 words, sha256 1efad0bee5704accf266db146bb27640465a5804ff86d4bb39cdd8db92ada359.

## Item 6: the undefined hook

"The hook" is used from the first sentence, and "shenpa" is only named in the fourth. The fix moves Pema's sentence to the front and adds her own gloss. The source for the gloss is Pema Chödrön, "How We Get Hooked and How We Get Unhooked" (Lion's Roar, https://www.lionsroar.com/how-we-get-hooked-shenpa-and-how-we-get-unhooked/): "The Tibetan word for this is shenpa. It is usually translated 'attachment,' but a more descriptive translation might be 'hooked.'" That page is linked on "hooked" in the article. Pema is now introduced earlier, in Don't Give (item 1).

> Pema Chödrön calls the tightening and urge you get before the story has finished forming "shenpa," and she says "hooked" is a more descriptive translation than the usual "attachment." You might notice the hook before you have any clue what part of you is doing the hooking. Or you might notice it embarrassingly late. The jaw and stomach are already tight, and/or half the text is written, and then suddenly it dawns you: you're supposed to be observing yourself. 😀 Maybe forget the parts detective work for a minute. You can figure that out later.

95 words, sha256 67e047370fcbd8373414080928dbf268c232c318a92509d625339eea98fe5942.

## Item 9: Also Look Outward P1

The paragraph came from the GPT lane (Episode 008 candidate H), accepted on its Pangram result on 2026-09-18 ("oh wow ok perfect") without a sense read. "They can still disagree with you. Their boundary can still make you mad. Now the first fight has company." are the source's "Someone disagreeing with you, needing time, or setting their own boundary does not make them emotionally immature", with the verdict lost, so they point at nothing. "Now the first fight has company" doesn't map to anything. The fix replaces the three with the point they were meant to make, tied to the first sentence (a fight didn't show who they are, and neither does a disagreement or a boundary).

> Have you ever had a fight where you were absolutely sure you'd finally seen who somebody was, and then they came back later and had a basically normal conversation with you? Irritating. Disagreeing with you doesn't tell you who they are either, and neither does a boundary that makes you mad. What matters more is when the subject changes but somehow you keep ending up in the same role: taking care of their reaction while your own experience disappears. Lindsay Gibson writes about those repeated relational patterns in her work on emotional immaturity.

93 words, sha256 a6ccec1586f012ffdfd41cd937be3afdcecb8b78b0485f4bc7aef07cb1a7985f. The article keeps the Gibson link.

## Gate for the three fixes

**Linter**, with the unchanged accepted sentences passed as `--owner` so only the changed sentence is measured:
- ask: CLEAR.
- hook: CLEAR. Without `--owner` it hard-fails on coach density (3.1 per 100), but all three coach phrases are in the accepted sentences.
- outward: REVIEW; second person on a 19-word sentence is a note.

**Sense read.**
- Ask: the usual prompt is to ask your little one what they need; "ask" suggests a question and a second voice answering; that may not be you.
- Hook: Pema's word for the tightening and urge is shenpa, better said as getting hooked; you may notice the hook early or late.
- Outward: one fight didn't show who they are, and neither does a disagreement or a boundary that makes you mad; the repeated role across subjects is what matters.
- All three now say what they refer to.

**Inventory, on the changed sentences (the rest was accepted as it stands).**
- **Ask:** C02 was PRESENT (the orphaned "ask") and is now ABSENT. T26: "ask" three times in one sentence, but the sentence is about the word. Every other row is ABSENT.
- **Hook:** C02 is fixed. C04 ABSENT (sourced and linked). T19 ABSENT: the first sentence names the thing the section is about rather than announcing it. T25 ABSENT. The other rows are ABSENT.
- **Outward:** C02 is fixed. T12 UNCERTAIN → KEEP: "doesn't… either, and neither does…" is a pair, but it's the source's own two cases. T16 ABSENT. T17 ABSENT. The other rows are ABSENT.

**Stance ledger.** Pema is the teacher who "inspired parts of this guide" (Joel's item 1). The hook is still named before the parts work ("forget the parts detective work"). Outward keeps "Keep that assessment specific and revisable".

**Checks planned (Pangram 4.0, Joel's account):** each fixed paragraph alone, then its section.
- ask P1: 68 words.
- hook P1: 95 words.
- outward P1: 93 words.
- sections: 219, 245, 276 words (sha256 d13aa9c43d68543a…, 0f0b69175b2112cc…, 3bb8fec6ed3d847d…).

## Results (Pangram 4.0, Joel's account, 2026-09-27, the turn that started 04:21)

- ask P1 alone: Human Written, 100% Human, 73 words scanned (short text).
- `You Don't Need an Inner Monologue` with the fix: 100% Human, 231 words scanned.
- hook P1 alone: 100% Human, 96 words scanned (short text).
- `Catch the Hook` with the fix and Joel's items 7 and 8: 100% Human, 255 words scanned.
- outward P1 alone, with the fix: **AI Generated, 100% AI**, 95 words scanned; the whole paragraph flagged.
- Diagnostic: the **original** outward P1 alone (sha256 e802901b6bfec92192cf31752f3a6306f2accd71869c993b7882d14d13ad0fb1, 93 words): also **100% AI**, 94 words scanned. This one wasn't hash-verified in the page before the click. The flagged span's start and the count match the original. So the paragraph was never Human on its own. It passed on 2026-09-18 only as part of its section, and my sentence isn't what makes it AI.

**Second wording for the fix sentence, before the section check.** Rereading the section, P4 ends "That doesn't tell you the whole conflict was yours, and it doesn't prove they're manipulating you." My sentence ("doesn't tell you who they are either, and neither does…") repeats that shape and phrase three paragraphs earlier (T26, and a matched pair twice in one section). The new wording ties to the first sentence's "seen who somebody was" instead:

> People disagree, and sometimes their boundaries make us mad, and none of that shows who somebody really is.

Section, sha256 526e93c56991d7704c8d1637165e9a14ee9440f0e4f0b4a419635d53e4803bdf, 275 words. Check planned: the section. P1 alone isn't rechecked, since the original failed alone too. Rewriting the whole paragraph so it passes alone is a separate job, and it goes to Joel as a proposal.

**Result (the section with the second wording):** Human Written, 100% Human, 284 words scanned. Installed.
