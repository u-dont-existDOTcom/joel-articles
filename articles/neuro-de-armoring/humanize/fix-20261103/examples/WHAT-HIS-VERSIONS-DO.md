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
