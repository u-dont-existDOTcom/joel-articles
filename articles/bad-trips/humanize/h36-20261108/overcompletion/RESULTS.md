# Overcompletion: the whole guide read for what it explains twice (2026-11-08, turn 27)

Gate E328, the next step after the repeats pass (`../../h34-20261108/`, `../../h35-20261108/`). Five fresh Sonnet
readers, one part of the guide each (`PART-1.md` to `PART-5.md`, blocks with their ids), blind to whose words they read,
were given `BRIEF.md`: his definition ("overcompletion is when you already have it explained and then you explain it
again"), the example he cut in his hypnosis guide, his rulings on what isn't overcompletion, and two rules for this
guide (a call-for-help threshold said again where the reader acts on it stays; a dose, timing or source is never the
thing cut). They found 39 candidates, 8 of them clear to them (`PART-1.json` to `PART-5.json`). `check_candidates.py`
ran each through the fidelity keys (R25), the keep-as-is ledger and the owner edits (`CHECKED.json`), and each was then
read by hand against its block and its neighbours.

Nine went in (`cut_overcompletion.py`): each says again only what the sentence, heading or item before it says, and
loses no point, key, kept line or owner edit. 12,306 to 12,173 words. Fidelity R25 PASS, keep-as-is 0 problems, owner
edits 63 pass. The rest stay, each for the reason in the table. No card this time: the one cut with a downside that a
card could have asked about (No Rash Actions' "experience-content" lines) failed its needed read, and the other ("The
difference is enormous.") is too small to spend a card on.

| block | kind (reader's strength) | the words | decision |
|---|---|---|---|
| B95 | says-again (clear) | "Calling medics does not require waiting passively, and using a fast field remedy does not require giving up..." | cut (`cut_overcompletion.py`) |
| B278 | says-again (borderline) | "Use local emergency services for immediate danger or a medical emergency." | stays: it holds a fidelity-key warning, and it is a call-for-help line where the reader acts on it |
| B77 | says-again (borderline) | "The emergency room is not magic, and for a physiologically stable psychedelic or practice-induced crisis it..." | stays: it gives the emergency room's limits with their reason (the benzodiazepines), in its own section |
| B104 | says-again (borderline) | "; their neurological status is still unknown" | stays: "their neurological status is still unknown" says not passing the screen means unknown, not failed |
| B120 | sums-up (borderline) | "Kidney impairment is a strong reason not to take MDMA--not a reason to sit there with worsening jaw tension..." | stays: "not a reason to sit there with worsening jaw tension" is what to do |
| B128 | sums-up (borderline) | "It is decision support, not first aid." | stays: "decision support, not first aid" tells the reader not to wait on the call |
| B87 | sums-up (borderline) | "The body is part of the spiritual field." | stays: "The body is part of the spiritual field" is a claim no other line makes |
| B161 | says-again (clear) | "When the goal is to reduce drug absorption or stop a toxic gut situation, charcoal may be relevant. When I ..." | stays: it holds a fidelity-key warning, and it is the rule for choosing charcoal or zeolite |
| B165 | preview-recap (clear) | "The tools in this section are for somebody who still wants the trip to continue." | cut (`cut_overcompletion.py`) |
| B176 | sums-up (borderline) | "That helped convince me the effect wasn't limited to my body." | stays: it is what the story showed him (borderline to the reader) |
| B188 | says-again (borderline) | "I don't understand the mechanism. I only know that it has repeatedly felt like a powerful natural remedy fo..." | stays: it holds a fidelity-key warning |
| B190 | says-again (borderline) | "Aged ozonated-charcoal water is different from zeolite and from swallowing charcoal." | stays: it tells the waters apart (borderline to the reader) |
| B197 | sums-up (clear) | "The mistake showed me that DMSO and aged ozonated-charcoal water address different kinds of overload." | cut (`cut_overcompletion.py`) |
| B201 | says-again (borderline) | "Sometimes DMSO works better; sometimes the water does." | stays: with B197's moral cut, it is where the guide says the two work differently |
| B218 | preview-recap (clear) | "Useful substances can still be poor rescue tools when somebody is already destabilized." | cut (`cut_overcompletion.py`) |
| B220 | sums-up (borderline) | "That may be therapeutic in the right context, but it is not a casual rescue tool." | stays: it is the caution itself |
| B221 | sums-up (borderline) | "The later benefit did not make the crisis recommendable." | stays: it is the caution itself (don't do it, whatever came after) |
| B224 | preview-recap (borderline) | "That finishes the rescue-chemistry side of the guide." | cut (`cut_overcompletion.py`) |
| B284a | preview-recap (borderline) | "As the person helping, you want to play the role of the calm, caring anchor to the safe present moment, not..." | stays: his anchor line (his round-24 version; the owner edits refuse it) |
| B290 | says-again (borderline) | "Redirect within the person's value-world toward peace and protection, increase" | stays: "increase containment" and "non-coercively" are said nowhere else |
| B295 | preview-recap (borderline) | "Choose one or two options rather than all of them." | cut (`cut_overcompletion.py`) |
| B300 | says-again (borderline) | "It does not issue commands or interpret the trip." | stays: it holds a fidelity-key warning |
| B304 | sums-up (borderline) | "Music should remain an option, rather than become another authority in the room." | cut (`cut_overcompletion.py`) |
| B314 | caveat-again (borderline) | "Never strain or turn breathing into another achievement." | stays: it holds a fidelity-key warning |
| B320 | says-again (clear) | "Because you saw it, it might feel like you have to act on it, and because it felt cosmic, obeying it might ..." | stays: a needed read of the line left after the cut found "experience-content, rather than fact-content" unclear without the two sentences that explain it (NEEDED-READ.md) |
| B337 | sums-up (clear) | "That is tripsitting, shadow work, and the path becoming practical." | cut (`cut_overcompletion.py`) |
| B328 | says-again (borderline) | "If it is true, it survives sleep." | stays: the survives-sleep test is said nowhere else; borderline to the reader |
| B321 | sums-up (borderline) | "Anything requiring violated consent or harm belongs in the notebook until you can review it with a clear he..." | stays: what to do with a harmful revelation (the notebook), borderline to the reader |
| B354 | says-again (borderline) | "And as the commenters on the first thread note, very few people would go thru that dozens of times hoping f..." | stays: his own aside on the Reddit threads (borderline to the reader) |
| B355 | says-again (borderline) | "Because they are unprepared to make the best of the experience, and unprepared to integrate it after, it's ..." | stays: his own picture of the swimming pool and his conclusion (borderline to the reader) |
| B355 | sums-up (borderline) | "So I think these approaches complement each other greatly." | stays: his own picture of the swimming pool and his conclusion (borderline to the reader) |
| B366b | says-again (borderline) | "The work is already done." | stays: his Give the Session, which reads Human High; its story makes the line make sense |
| B381 | sums-up (clear) | "The difference is enormous." | stays: a four-word line in his own story of Bee, borderline, and maybe his |
| B401 | says-again (borderline) | "A demon can fight your hatred, feed on your fear, argue with your pride or seduce your grandiosity, but the..." | cut (`cut_overcompletion.py`) |
| B399 | every-case (borderline) | "Panic fights panic, hatred fights hatred, pride fights pride, and suddenly a small war is running inside co..." | stays: the one concrete picture of fighting fear with fear (borderline to the reader) |
| B388 | says-again (borderline) | "Let it bubble up gently." | stays: the gentle side of "Never force gratitude", in a few words (borderline) |
| B409 | sums-up (borderline) | "You don't have to decide tonight." | stays: it holds a fidelity-key warning |
| B428 | sums-up (borderline) | "Deep practice can wait until the floor is back." | stays: "deep practice can wait until the floor is back" says when to go back to practice |
| B400 | sums-up (borderline) | "Practice being the space rather than the storm." | stays: it is the aim of the training the sentence before gives (borderline) |
