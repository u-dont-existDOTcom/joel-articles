# What his three versions do (Neuro De-Armoring Cards, 3 November)

His answers file: `ANSWERS-20261103-1748.json` (2026-11-03 17:48 UTC). Each card was a paragraph of his post that read AI in
the baseline and again in my round-1 rewrite. Below, for each kind of text, his post's sentence, what he wrote, and what
changed, then the rules round 2 takes from it. His versions are in the article (`apply_answers_x1103.py`); he tested X-26
and X-84 himself ("passes"), and X-15 by itself read [Human Written, 0.3% AI](https://www.pangram.com/history/0bc718b1-278a-40ce-a7dd-6af7d45268d5)
(`../x15/RESULTS.md`): its first sentence Human (High), the two short label sentences after it Human (Low).

Neither the label nor the metaphor was the tell. He kept the house, the solvent, the concrete and the software (X-26), and
he added a label of his own, "Precautions/Side Effects:" (X-15). My round 1 had cut metaphors and taken labels off, and still
read AI. What he changed is how each sentence is built.

## The science (X-26, Psychology is the Software)

| his post | his version | what changed |
|---|---|---|
| Neurological De-Armoring is underpinning (not redecorating). | Neurological De-Armoring is about fixing the underpinnings, not redecorating. | The coined label (a noun with its contrast in brackets) is said as a plain claim: "is about fixing X, not Y". |
| This protocol acts as a metabolic solvent—an HDAC inhibitor—that softens the neural concrete of the brainstem by modulating Glutamate and introducing Ketones (BHB). We are digging underneath the house to pour a new foundation so that, eventually, the psychological “software” updates upstairs will actually install. | It's a protocol that serves as a metabolic solvent, via HDAC inhibition, that softens the "concrete" in the brainstem by using Glutamate modulation and supplementing Ketones (BHB) to allow us to dig under the house, and pour a new foundation, so we can eventually update the psychological software upstairs. | Two sentences become one long one, joined loosely: "that serves as", "via", "that softens", "by using ... and supplementing", "to allow us to", ", and pour", "so we can eventually". The em dashes go. The scare quotes move to the metaphor word ("concrete"). Verbs become a noun and a supplement word ("Glutamate modulation", "supplementing Ketones"). "We are digging" becomes "us" inside the purpose: the metaphor is what the protocol lets us do. |

My round 1 kept "That's why I call ... underpinning" and a colon reveal ("The work happens under the house: ..."); both read
AI.

**Rules for the science paragraphs**: say the claim plainly ("X is about ...", "It's a ..."); carry the mechanism, the
means and the purpose in one long sentence joined the way he joins them ("that", "via", "by using", "to allow us to", "so
we can"), commas where they fall, not tidy; keep his metaphors and scare-quote the metaphor word; no em dashes, no colon
reveals, no "That's why".

## A dose with its instructions (X-84, the uridine trial)

| his post | his version | what changed |
|---|---|---|
| Trial: UMP 150–300 mg in the morning with food for 3–7 days. | Do a trial with 150-300mg Uridine, in the morning with food. It shouldn't take more than 3 to 7 days to get an idea of whether or not it's beneficial. | The label and the spec become an instruction with a verb ("Do a trial with ..."). The number of days gets its own sentence, saying what it is for, hedged the way people talk ("It shouldn't take more than", "to get an idea of whether or not"). |
| Keep omega-3s in place, especially DHA/EPA. | Keep your Omega-3's up, especially DHA and EPA. | "your", and a casual verb ("keep ... up"); the slash becomes "and"; his capitals and apostrophe. |
| Make sure there is enough choline from eggs, phosphatidylcholine, CDP-choline, or another tolerated choline source. | Make sure you have sufficient Choline - from eggs, Phosphatidylcholine, CDP-choline, etc, whichever works best for you. | "you have"; a formal word in a casual sentence ("sufficient"); a spaced hyphen; the list ends "etc, whichever works best for you" instead of naming a category. |
| Do not start UMP on the same day you start 5-HTP, agmatine, D-serine, keto, iboga, shrooms, LSD, ketamine, or any other major variable. You are trying to see whether UMP itself changes the signal. | Don't start the uridine at the same time as starting some other major variable (like 5-HTP, Agmatine, D-serine, Keto diet, Iboga, Shrooms, LSD, Ketamine, etc), since the point is to see whether uridine itself changes the signal. | The category comes first ("some other major variable") and the list goes in brackets as examples ("like ... etc"). The reason is joined on ("since the point is"). "Don't", "the uridine", "at the same time as starting". |

My round 1 had "To trial it:" and the spec, the list kept as a list, and "since you're trying to see"; it read AI.

**Rules for the dose-and-instruction paragraphs**: no "Label: spec"; each dose inside an instruction with a verb ("Do a
trial with", "Take", "Try"); what a number of days or a dose is for in a sentence of its own, said the way people talk; "you"
and "your"; a list of things to avoid or choose goes after its category, in brackets, as examples ("like ... etc"); end a
list of options with "whichever works best for you" only where the post already leaves the choice open (as its "another
tolerated choline source" did), never as a catch-all the post doesn't have (J64); join the reason with "since the point is"
or "so".

## Warnings (X-15, agmatine's interactions)

| his post | his version | what changed |
|---|---|---|
| Do not combine agmatine casually with opioids, kratom, clonidine/guanfacine, blood-pressure medication, nitrates, PDE-5 inhibitors, MAOIs, or complex psychiatric medication stacks without clinician review. | Precautions/Side Effects: Do not use concurrently with opioids and/or kratom (will reduce tolerance), clonidine and/or guanfacine, blood pressure lowering medications, nitrates, PDE-5 inhibitors, MAOIs, or other complex “psych” stacks without having a physician competent to consider the likelihoods of problematic interactions. | The register of a supplement label ("Precautions/Side Effects:", "Do not use concurrently with"). "and/or" for the slash; a reason in brackets, in label shorthand ("(will reduce tolerance)", a fact the post states in the paragraph before: agmatine affects "opioid reward/tolerance"); "“psych” stacks"; the clinician review said as a long, particular clause ("without having a physician competent to consider the likelihoods of problematic interactions"). This sentence read Human (High). |
| Avoid it during pregnancy or breastfeeding, and be especially cautious with bipolar disorder, psychosis history, unstable panic, low blood pressure, kidney/liver disease, or active substance relapse risk. | Not recommended for use in pregnancy or breast-feeding. Use with extreme caution in those with bipolar disorder, prior psychotic episode, unstable panic disorder, lower end blood pressure, kidney or liver issues, or those with a currently-high likelihood of relapsing in addictions. | One sentence becomes two label sentences ("Not recommended for use in", "Use with extreme caution in those with"); each condition a little more particular ("prior psychotic episode", "lower end blood pressure", "currently-high likelihood of relapsing in addictions"). These read Human (Low): the stock label phrases are human, but less surely than his own clause. |

My round 1 had "So without clinician review, do not combine ..." and "be especially cautious with it if you have"; it read
100% AI.

**Rules for the warnings**: the register of a supplement label, with his own particular clauses in it (the reason a
combination is a problem, when the article gives it, said in brackets in a few words; who should check it, said as he says
it); "and/or" for a slash between two drugs; the post's own words for things where it has them (its "psych meds"); each
condition as particular as the article lets it be; not every sentence a stock phrase (those read Human only at Low).

## Across the three

- Every dose, compound and warning came out again (the fidelity check holds them; his wording is recorded in
  `../../FIDELITY-KEYS.json`, "owner_wording"). He didn't drop anything; he said each one his way.
- What he added is his to add. "(will reduce tolerance)" rests on the paragraph before it; "It shouldn't take more than 3
  to 7 days to get an idea" says what the post's "for 3–7 days" is for. Round 2 adds nothing the article doesn't already say
  (C03): a reason in brackets only when the article gives the reason somewhere.
- His habits stay in his own sentences and aren't copied into mine: capitals on compound names (Uridine, Choline,
  Agmatine), "Omega-3's", "etc" with no full stop, " - ". Adding his tics to other paragraphs to read like him is the thing
  SKILL.md forbids ("Never add errors, fake specificity, memories, catchphrases, unusual punctuation, slang, or corpus tics
  to improve similarity"; tells J47 and W18). What round 2 takes from him is how each sentence is built: the verb that
  carries a dose, the sentence that says what a number is for, the list after its category, the long joined science
  sentence, the label register with a particular clause in it. Contractions are ordinary English, not his tic.

## What round 2 showed (gate E336)

These rules carried the science in my hand: the Role-Self part of Psychology is the Software went from 100% AI to 19.8% AI
in two tries. They didn't carry the warnings or the uridine section, which read 100% AI every way I tried, even one
paragraph at a time in his label register ([round 2's results](../r2his/RESULTS-ROUND2.md)). What made his warnings and
his trial paragraph Human is his own wording, not the build, so those kinds go to him as stretches to edit.

## His fourth version: "Who this is for" (4 November, gate E343)

His message of 2026-11-04 10:01 UTC took my round-2 version of the uridine section's first paragraph ("fixed it, just
clarified and uncompressed"); his version by itself reads [Human Written, 0.0% AI](https://www.pangram.com/history/9225442f-06b8-4a7a-ab8e-d8a03f720290) (High).
What he did, the gut lane's E338 in this article:
- **The plain meaning first, the term after it in brackets**: "where everything feels gray and there's no desire for
  anything (anhedonia)"; and the plain word before a code: "dopamine receptor D2/D3".
- **One observation a sentence, with the causes said**: "These folks also find that dreams and psychedelic visuals are
  weak, so they need unusually high doses to feel anything, and as a result they tend to compulsively reach for ...".
- **A hedge for the reader instead of a rule**: "It could be helpful, though, for folks that show ...".
- **A plain clinical verb**: "People with DAWS, after tapering off dopamine agonist drugs, present with symptoms of ...".
- **My closer cut**: "That's a pretty specific phenotype, and I'm not saying everyone needs dopamine."

In my hand the same moves took the evidence paragraph from 62.2% to 0.0% AI (AI Assisted) in four tries, but not Scott's
story (100% AI in all four): `../../fix-20261104/checks/`, and the two cards that ask him.

## His fifth version: Scott's paragraph, joined with ", but" (4 November, gate E352)

The card's version (Codex's rewrite) read Human Written with its last three sentences at Low confidence; both of my tries
at those sentences read worse (84.6% and 100% AI). His answer on Neuro De-Armoring Cards, 4 November (2) (2026-11-04
13:53 UTC; `../../fix-20261104/cards/ANSWERS-20261104-1352.json`): "the only change i needed to flip the low conf human all
to high conf was to merge the sentences with a ", but" ... again it's the way it flows". His version by itself read
[Human Written, 0.0% AI](https://www.pangram.com/history/6716a87f-8df3-4107-ab4c-5df53a83ef6d), every window High.

| the card's version | his version | what changed |
|---|---|---|
| You can't tell from this whether UMP rebuilt his D3 receptors overnight. It does suggest that in the right person, ... | You can't prove from this whether UMP rebuilt his D3 receptors overnight, but it does suggest that in the right person, ... | The negation and its contrast are one sentence, joined with ", but": "Ai says stuff like "It doesn't X. [But is implied] Blah blah blah ..."". "prove" for "tell", his post's word ("That does not prove ..."). |
| Scott was having vivid dreams again too, with real childhood memories coming back in them. | Scott was having vivid dreams again too, with real childhood memories surfacing. | "surfacing" for "coming back in them". |

His caution with it: "there's also the Not X, but Y. pattern with AI, so we shouldn't overuse that either, but sometimes
it is the most clear and natural way to phrase it." What I take from it: where a draft says what isn't so and then, in a
new sentence, what is ("X doesn't Y. It does Z."), join the two with ", but" (`tells_lint.py` O64 now fails the split
form); the joined "not X, but Y" is used where it is the clearest way to say it, not as a habit. My two tries had kept
the two sentences and changed their words, which is why they couldn't work.

## His versions six to eleven: the uridine stop signs and caution, and the 5-HTP section (4 November, gates E357, E358)

His answers on Neuro De-Armoring Cards, 4 November (3) (`../../fix-20261104/cards/ANSWERS-20261104-1809.json`, 18:09 UTC),
after two tries of mine and Codex's rewrite read AI by themselves in each of four paragraphs, and two weak windows whose
one-sentence fixes moved the rest. Each of his read Human Written by itself (his checks, and the lane's for Y-86 and the
full stop of Y-91: `../../fix-20261104/cards/apply_cards_x1104d.py`).

| card | what he changed | his words on it |
|---|---|---|
| Y-85, the uridine stop signs | "the studies" became "the studies I've seen"; the choline guess said as what it means ("places a higher demand on choline than what people may normally get from diet alone"); the last line cut | "\"i've seen\" fixed a part of the AI issue, because \"the studies\" is referencing which studies?"; "you were overcompleting, repeating yourself on the last line" |
| Y-86, the psychedelic caution | the post's "treat that as a safety signal" replaced by what the section means: vivid dreams and sensitivity are what UMP is for, so the old high dose may hit harder | "idk where this safety warning came from, doesn't make much sense at all" |
| Y-88, the 5-HTP "Who this is for" | the exclusions turned round: the advice first ("I'd avoid casually experimenting with 5-HTP if ..."), then who and why, in two sentences | "give the reader payoff sooner so they understand why they should read" |
| Y-89, the 5-HTP tool | the whole paragraph in the reader's order: what 5-HTP is, what you'd feel, the hype, the review, the risk and why | "a lot of work to reverse the order of how it was written"; then "i'd cut this whole paragraph or merge anything important from it into the last one" (merged into Y-88) |
| Y-90, Scott's doses | "matters" and "more isn't better" cut; the link between slow-COMT and P5P sensitivity said ("making him sensitive") | "Ai is always saying stuff \"MATTERS\""; "you had 2 statements just floating there, what were they for?" |
| Y-91, the 5-HTP trial | "50mg" without the space; "just" before the lower dose; "like Scott did"; the tense made one ("felt like it \"almost worked\""); "the other suggested regimen changes" | "don't think i've seen humans put spaces there"; "i got it all high conf by addding \"like scott did\"" |

**Rules from these six** (my drafts, from now on):
- The point first. A sentence that opens on a long condition ("If you're already X, Y or Z, ...") makes the reader hold it
  before they know why; say the advice, then who it's for and why (E357, the gut lane's E347; `tells_lint.py` O65).
- Say what a word like "matters" stands for (O66), and say the link between two facts placed side by side ("making him
  sensitive"), or the reader can't tell what they're for.
- No last line that says again what the paragraph has said (the stop line after the stop signs; "more isn't better").
- A source the reader can place ("the studies I've seen"), and a warning only where it makes sense in its section.
- His spelling of doses ("50mg"; O67), and the case named where an option comes from it ("like Scott did").
- A warning's words may change when its meaning stays (E358); the fidelity check holds its warning word, compounds and
  numbers.
