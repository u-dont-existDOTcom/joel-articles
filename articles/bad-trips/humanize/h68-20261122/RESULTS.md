# Turn 60 (2026-11-22): his round-49 steps in, the medical part read for sense, round 50

His round-49 answers ([his export](../../review/r49/ANSWERS-R49-20261122-1721.json)) gave his own steps 1, 3, 4 and 7,
step 8 his way, his answers to the readers' questions, the bold, and his score of quiz 1. Two things he asked for run
through this folder: "i hope we don't have other nonsensical stuff in this guide" and "make sure we are not repeating
the same stuff over and over". The lessons are in [the lesson file](../../../../docs/lessons/2026-11-22-1721-bad-trips.md).

## What went into the guide

| step | whose | Pangram |
|---|---|---|
| 1, 3, 4, 7 | his, as he sent them (7 with the CDC linked on his "according to the CDC") | his own checks, listed with what each tested in [HIS-CHECKS-R49.md](../../review/r49/HIS-CHECKS-R49.md); step 7 as it went in: [Human Written, Human High](https://www.pangram.com/history/6e5ea946-e81a-403e-b44a-690eb999ca04) |
| 8 | his version, then his answers (c), (d), (e) in it ([apply_r49_answers.py](../../review/r49/apply_r49_answers.py)) | his: [Human High](https://www.pangram.com/history/0aaabffe-775f-40d0-8dfc-18d9d128dc81); with the answers: [Human Written, Human High](https://www.pangram.com/history/a3c02dd9-5907-4ead-a975-1deb4f58e039) |
| 2 | his, with his answer (a) (where to get it at night) as its last sentence | [Human Written, Human High](https://www.pangram.com/history/9e72f856-d889-487a-9fbe-179b6a87a271) |

The texts are [TEST-a3-ss2.txt](TEST-a3-ss2.txt), [TEST-a3-ss8.txt](TEST-a3-ss8.txt), [TEST-r49-ss7.txt](TEST-r49-ss7.txt)
and [TEST-r49-ss8his.txt](TEST-r49-ss8his.txt), with their sense receipts beside them; batch h68a in the ledger.

Of his answers, three things are not in the guide, each said in the turn's report:
- (c) "Niacinamide would be safer": step 8 says not to give niacin, and nothing tells the reader to give niacinamide, so
  the line would be a remedy with no step and no source in hand.
- (e) raising the Syrian rue oil's dose slowly: step 8 keeps "leave it out for now", and card SS-ASKED-2 (d) asks him
  which way it goes.
- (d) the study he linked on topical magnesium and kidney disease (PubMed 37486715) was not opened: the fetch waited on
  an approval nobody answered, so its claim is not in the step.

## The medical part, read for sense

Step 7 had "take readings every so often" of temperature, pulse or blood pressure, carried from the guide as it was; his
mark: "you can't even take BP readings reliably when someone is having a seizure ... i hope we don't have other
nonsensical stuff in this guide". So four fresh readers (one per part, each seeing only its part,
[make_advice_reads.py](make_advice_reads.py)) read the call list and who to contact, My Brain Feels Damaged and Active
Seizure, MDMA with chest pain and swallowing, and Serotonin Syndrome, as the friend who is there, asking of every line:
is it already true of anyone on the drug (ANYWAY), can I tell (CAN'T TELL), does it come from somewhere else (FROM), is
it right (RIGHT), could I take it wrong (MISREAD). Their prompts and answers: [advice/](advice/prompt-serotonin.txt)
(`prompt-*.txt`, `read-*.txt`).

They flagged 122 lines. Each one's fate, with whose words it is and why, is in [advice/FATES.md](advice/FATES.md)
([advice_fates.py](advice_fates.py)):

| fate | lines | what it means |
|---|---|---|
| his remedy or experience | 48 | DMSO, humic acid, the sniffer, CBD, magnesium by the gram, charcoal: said in his first person, with the studies linked where the guide makes a claim |
| decided before | 37 | he ruled on it in an earlier round, named in the table (the first seizure he cut in round 38; chest pain and the AHA in rounds 3 and 37; his brain checks in round 38) |
| left | 14 | the usual first-aid wording, or a line that says what it should |
| one part only | 5 | the reader missed what the guide has elsewhere (the call list above, a link) |
| checked today | 4 | Fireside's hours (Pacific time, which the guide says; the reader's copy was cut at "p.m."), Crisis Text Line's partners, ICEERS's five sessions, the monthly online group |
| his round-49 answers | 5 | his words this round |
| to him, round 50 | 9 | below |

What goes to him, each with what I found:
- **ADVICE-CALL** (a) "Severe insomnia" in Call Medics For, moved there from his reach-out paragraph in round 35; a night
  without sleep is usual after MDMA. (b) "if they start acting delusional", which fits most bad trips. (c) Naloxone,
  which the guide never names: fentanyl in pills sold as MDMA ([Harm Reduction Journal, 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10698886/)),
  naloxone over the counter and safe ([CDC](https://www.cdc.gov/stop-overdose/naloxone-faq/)), wearing off in 30 to 90
  minutes ([Jed Foundation](https://jedfoundation.org/resource/naloxone-101-how-to-use-it-to-save-lives-from-opioid-overdose/)).
- **ADVICE-ORAL** "Slow breathing is normal with iboga": ibogaine slows the heart ([2022 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC9292417/);
  [review](https://pubmed.ncbi.nlm.nih.gov/26807959/)); nothing found on breathing.
- **SS-DRINK** step 6: potassium can run high when muscle breaks down ([StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK448168/);
  [review](https://pubmed.ncbi.nlm.nih.gov/19046720/)); Epsom salt is the laxative kind his MDMA section steers away from.
- **SS-ASKED-2** (a) "the seizure" before any seizure; (b) the dose ([Maryland Poison Center](https://www.mdpoison.com/media/SOP/mdpoisoncom/healthcareprofessionals/antidote-facts/Cyproheptadine%20Antidote%20Facts.pdf):
  12 mg, then 2 mg every two hours, 32 mg a day at most); (c) DMSO's reason in step 8; (d) the oil's "almost none" with
  "could harm"; (e) flexing the feet, which is how clonus is set off ([CCJM](https://www.ccjm.org/content/83/11/810)).

Not asked again, because he decided it: a first seizure as a reason to call (the CDC lists it; he cut it from his seizure
list in round 38); mild chest pain treated at home with "if unsure" calling (round 3 raised the AHA's "call 911"; his
version, round 37); the magnesium by the gram (his answer (d) this round).

## Repeats

[repeat_scan.py](repeat_scan.py) read every sentence of the guide against every other (612 sentences): four pairs say
nearly the same thing ([REPEATS.json](REPEATS.json)). "train before you need it" and "This feeling is allowed to move
through" are each in two places he chose (round 31); hand on heart is the Grounding Menu pointing to its section; the
shungite water's "after ozonation had ended" comes twice two paragraphs apart, and goes to him (card REPEATS). The
medical part repeats less than it points: step 6 now points to MDMA: Magnesium Alarm for the signs, and step 7 to
Active Seizure for the first aid.

## My new lines: quiz 2, not checked on purpose

Version one ([TEST-a4-ss-v1.txt](TEST-a4-ss-v1.txt), [TEST-a4-nalox-v1.txt](TEST-a4-nalox-v1.txt)) went to three fresh
readers each (needed, against his fixes, fit: [reads/](reads/need-a4-ss.txt)). What they marked and what changed in
version two ([TEST-a4-ss.txt](TEST-a4-ss.txt), [TEST-a4-nalox.txt](TEST-a4-nalox.txt)):
- the dose packed five numbers into one sentence, and the ambulance comes long before a repeat: the first dose only,
  and tell the medics;
- step 6's last line ("If theirs is low instead, ... the ER will find that and fix it") gave the reader nothing to do:
  cut; the potassium don't said no reason anyone would add it: "And while you might think to add potassium too, since it
  can run low after MDMA";
- step 7's "And if they have a seizure" tied to nothing, "it" could be two things, and it said neither what to watch
  nor what to do: "while you wait", the first aid in Active Seizure, and what to tell the medics;
- naloxone came before the reason, never said what it does, and "It wears off" could be the drug: the reason first,
  "which naloxone reverses", "naloxone can wear off", and what to do then.

Still open in version two, and in my reading of it: no amount for the magnesium flakes, and the readers' wish to have the
electrolyte signs named in step 6, which he asked to point to instead. Quiz 2 on round 50 has my reading of each
sentence for him to score before Pangram sees them ([QUIZ-SCORES.md](../../review/QUIZ-SCORES.md)).
