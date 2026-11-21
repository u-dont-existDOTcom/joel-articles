# The serotonin steps (B136), turn 57

His message, 2026-11-21 13:04 UTC: "done. learn lessons. why would you put 2 serotonin syndrome headings in a row /
continue". After the headings work, the next unit below High in the queue: the eight steps under "Do this immediately
when serotonin toxicity is reasonably suspected:", which read AI High 326 over the whole list as they stood
([2d3e8386](https://www.pangram.com/history/2d3e8386-31e3-45f8-8968-f875710a2470), turn 54).

His step 2 (cyproheptadine, his round-41 version, Human High 58 by itself) and the opening of step 3 he chose in C1
("Call emergency help and arrange transport." with "Don't drive yourself.") stay as he has them in every try.

## The first try: each sentence his fixes' way

Three fresh reads of the steps as they stood ([need](../h62-20261120/reads/need-c1-ss-steps-1.txt),
[his fixes](../h62-20261120/reads/his-c1-ss-steps-1.txt), [fit](../h62-20261120/reads/fit-c1-ss-steps-1.txt)), then my
draft and three fresh reads of it ([need](reads/need-g1-ss-steps-2.txt), [his fixes](reads/his-g1-ss-steps-2.txt),
[fit](reads/fit-g1-ss-steps-2.txt)), every sentence of mine they marked changed before the check
([the steps as they would read in the guide](STEPS-g1.md)): the drug list in three groups ending on cough syrup;
"serotonergic", akathisia and rhabdomyolysis said in plain words where first used (the last two checked against MedGen
and MedlinePlus); poison control named instead of "it"; the bath and the fever reducer said as how they follow from the
cooling; what to write down for the ER split in two; niacin said as the guide's trip killer, which is why it comes up.
The hospital line ("Hospitals may use benzodiazepines, ...") is cut: the needed read found the reader does nothing with
it, and the call and transport steps already send them there.

| Text | Result | Windows | Link |
|---|---|---|---|
| The whole list | AI Generated, 100% | AI High 535 | [896a47c9](https://www.pangram.com/history/896a47c9-cbc6-4fa3-a130-a9677f69b6cc) |
| Steps 1 and 2 | AI Generated, 100% | AI High 133 | [3c421039](https://www.pangram.com/history/3c421039-6f53-4798-8085-e604427ec49b) |
| Steps 3 and 4 | AI Generated, 100% | AI Medium 10 ("Call emergency help and arrange transport."), AI High 134 | [494e52a9](https://www.pangram.com/history/494e52a9-0bb8-4cbd-9857-eace260d10f0) |
| Steps 5 and 6 | AI Generated, 100% | AI High 133 | [25df9e03](https://www.pangram.com/history/25df9e03-eb53-458f-a136-c238e6650e3a) |
| Steps 7 and 8 | AI Generated, 100% | AI High 63, AI Medium 62 (step 8) | [59de60fe](https://www.pangram.com/history/59de60fe-6ada-4e33-bb70-8027ff7c59e2) |

All five predicted AI, all right. Nothing goes in. His step 2, Human High by itself, read AI inside steps 1 and 2: the
pull is the list as a whole, explained instructions one after another, not one sentence.

## The second try: his Active Seizure list's form

The same sentence-by-sentence way would fail the same way, and no window was Human to start a small change from (lesson
19b). His Active Seizure list read Human High 243 in place: "Time the seizure, and while it lasts:" and short items, one
point each, each built differently. The second try takes that form where a step lists things
([as it would read in the guide](STEPS-g2.md)): a lead line ending in a colon, then the items. Read by three fresh
readers ([need](reads/need-g2-ss-steps-3.txt), [his fixes](reads/his-g2-ss-steps-3.txt), [fit](reads/fit-g2-ss-steps-3.txt))
and changed where they marked it: the antidepressant line says to hold it back even when the kind is unknown (the lead
line's "suspected"), the fever reducers are named, DMSO is said as this guide's remedy for other emergencies, the fan and
the ice packs are two items. Its receipts pass and its fidelity check passes.

**Not checked yet:** the desktop app's browser pane went offline after the first try's checks (its tools left this
session), and the checks run only there (his Pangram account; tabs in his own browser get lost, so not there). The
predictions are written in [predict.py](predict.py) (`python3 predict.py g2a-ss12-3 g2b-ss34-3 g2c-ss56-3 g2d-ss78-3`,
right before the checks), with the texts to type beside it. The whole list waits until the pairs read Human: its
lineage has one of its two section checks left.

## Also found

The fidelity check failed on the first try for a reason outside it: a warning his round-33 card STILL-CUT cut with its
whole paragraph ("Stop if the task increases agitation, speed, or risk.") had only "speed" recorded as cut, and the rest
of its words had been matched to the serotonin steps by chance ever since. [FIDELITY-KEYS-R47.json](../h01/FIDELITY-KEYS-R47.json)
records the rest of that card's cut (W077, W078); every check from now uses it. The first try also dropped the key term
"MDMA-related" ("when MDMA has their jaw clenched"); the second try keeps it.
