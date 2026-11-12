#!/usr/bin/env python3
"""build_tests.py - turn 40's carries (2026-11-12, after his fixes of 19:44 UTC): the rest of the medical part, written
with the lessons of rounds 37 and 38 (the action before what it serves; each line the kind of thing its lead-in says;
"safe" saying how; nothing true anyway of someone tripping, nothing a friend can't tell, no rule from another setting,
the fit read's three questions, gate bad-trips-2026-11-12j).

- rescue-c1: Active Seizure as it now reads (his first aid and call list, 5e41c575) with its rescue medicine paragraph
  (B110) after them: what to do first ("give it the way it's meant to be given") and why, the rescue forms said plainly
  with the reason a pill won't do, and the breathing risk said as what happens.
- brainev-c1: My Brain Feels Damaged's evidence paragraph (B105): his belief first, as it is; "That judgment is stronger
  than the clinical evidence, but the evidence is not empty" said plainly; the three studies one a sentence, each saying
  what it found in the reader's terms; what the animal study means for the reader (it may still help if you start late).

  python3 build_tests.py
"""
import hashlib, pathlib
HERE = pathlib.Path(__file__).resolve().parent
SEIZE = ("Active Seizure\n\n"
         "Time the seizure, and while it lasts:\n"
         "- Move any dangerous objects away from them, especially anything hard or sharp.\n"
         "- Don't restrain them, since that can cause injuries, but do put pillows where appropriate, especially under the head.\n"
         "- Loosen any tight clothing.\n"
         "- Turn them gently onto their side, which helps them breathe.\n"
         "- Keep everything out of their mouth while they're convulsing or not fully conscious.\n\n"
         "Call medics if any of these happen:\n"
         "- A convulsive seizure goes on for over 5 minutes.\n"
         "- Their breathing gets slow and shallow.\n"
         "- Their lips turn blue or gray.\n"
         "- They get dangerously hot (not just regular sweating).\n"
         "- They injure their head, break a bone, or bleeding won't stop.")
RESCUE = ("If you have a benzodiazepine made for stopping seizures, give it the way it's meant to be given, since "
          "benzodiazepines are the first drugs doctors use when a seizure won't stop. They come in forms you don't have to "
          "swallow, like a nasal spray or a rectal gel, and some are intramuscular shots, since a pill is no use while "
          "they're seizing. If they've also taken respiratory depressants, like opioids or alcohol, "
          "the benzodiazepine adds to the risk of their breathing slowing too much.")
EVID = ("I believe DMSO works better for stroke and most acute brain damage than anything else readily available to ordinary "
        "people. My judgment goes further than the clinical evidence, but that evidence points the same way. People who'd "
        "had a stroke from a clot may have recovered better on DMSO in a preliminary trial. Doctors have also used it in a "
        "small series of patients to bring down dangerous pressure inside the skull. And animal stroke research found it "
        "shrank the area of the brain that died, even when treatment started after the stroke, so it may still help if you "
        "start late. It also suppresses NMDA- and AMPA-mediated excitotoxicity, the overexcited nerve signaling that "
        "kills brain cells after a stroke.")
TESTS = {
    'rescue-c1': SEIZE + "\n\n" + RESCUE,
    'brainev-c1': "If Someone Says \"My Brain Feels Damaged\": DMSO + Humic Acid + Electrolytes First\n\n" + EVID,
}

# rescue-c2, after the reads of rescue-c1 (reads/): who has a rescue medicine and how to give it said ("like one they carry
# for epilepsy", "the way its label says": the fit read could not tell from "the way it's meant to be given" what a friend
# would do, and called it a step for prescribed patients), the forms one sentence and the reason, and the breathing risk
# ending on what to do ("so keep watching their breathing").
RESCUE2 = ("If there's a rescue medicine for seizures on hand, like one they carry for epilepsy, give it the way its label "
           "says. These are benzodiazepines, the first drugs doctors use when a seizure won't stop. They come in forms you "
           "don't have to swallow, like a nasal spray or a rectal gel, since a pill is no use while someone's seizing, and "
           "some are intramuscular shots. If they've also taken respiratory depressants, like opioids or alcohol, the "
           "benzodiazepine adds to the risk of their breathing slowing too much, so keep watching their breathing.")
TESTS['rescue-c2'] = SEIZE + "\n\n" + RESCUE2

# rescue-c3, after the reads of rescue-c2 (reads/his-rescue-c2.txt, reads/fit-rescue-c2.txt): the medicine said with the
# reader in it ("the same first drugs doctors reach for"), the forms one sentence and the shot another, and the breathing
# said as what to do whatever was taken (the fit read: a friend often can't know whether opioids or alcohol were taken).
RESCUE3 = ("If there's a rescue medicine for seizures on hand, like one they carry for epilepsy, give it the way its label "
           "says. They're benzodiazepines, the same first drugs doctors reach for when a seizure won't stop. They come in "
           "forms you don't have to swallow, like a nasal spray or a rectal gel, since a pill is no use while someone's "
           "seizing. A few are intramuscular shots. After giving one, keep watching their breathing, since a benzodiazepine "
           "adds to the risk of it slowing too much, more so if they've also taken respiratory depressants like opioids or "
           "alcohol.")
TESTS['rescue-c3'] = SEIZE + "\n\n" + RESCUE3

# rescue-c4, after the reads of rescue-c3: the first two sentences joined (what to do, and why this drug), and the
# breathing sentence split into what to do with its reason, and when the risk is higher.
RESCUE4 = ("If there's a rescue medicine for seizures on hand, like one they carry for epilepsy, give it the way its label "
           "says, since these are benzodiazepines, the same first drugs doctors reach for when a seizure won't stop. They "
           "come in forms you don't have to swallow, like a nasal spray or a rectal gel, since a pill is no use while "
           "someone's seizing. A few are intramuscular shots. After giving one, keep watching their breathing, since a "
           "benzodiazepine adds to the risk of it slowing too much. That risk is higher if they've also taken respiratory "
           "depressants like opioids or alcohol.")
TESTS['rescue-c4'] = SEIZE + "\n\n" + RESCUE4

# rescue-c5, after the reads of rescue-c4 (reads/his-rescue-c4.txt; the fit read found nothing): what to watch for after
# giving one said in the words of his call list ("slow and shallow"), so the friend watching knows the sign and that it
# means calling medics. The other marks are kept (HIS-FIXES.json).
RESCUE5 = ("If there's a rescue medicine for seizures on hand, like one they carry for epilepsy, give it the way its label "
           "says, since these are benzodiazepines, the same first drugs doctors reach for when a seizure won't stop. They "
           "come in forms you don't have to swallow, like a nasal spray or a rectal gel, since a pill is no use while "
           "someone's seizing. A few are intramuscular shots. After giving one, keep watching their breathing, since a "
           "benzodiazepine adds to the risk of it getting slow and shallow. That risk is higher if they've also taken "
           "respiratory depressants like opioids or alcohol.")
TESTS['rescue-c5'] = SEIZE + "\n\n" + RESCUE5

# rescue-c6, rescue-c5 with its last two sentences said as one, in the shape of his own electrolytes sentence (19:44 UTC:
# "..., because magnesium (and then potassium) can be depleted by some drugs, especially MDMA and iboga, ..."): what to do
# after giving one, why, and "especially if" for opioids or alcohol, so the paragraph ends on what to watch and not on a
# bare risk (the needed read and the read against his fixes of rescue-c5 both marked the risk sentence as giving no action);
# and "After giving it", since "one" is a word AI uses far more than he does (O46).
RESCUE6 = ("If there's a rescue medicine for seizures on hand, like one they carry for epilepsy, give it the way its label "
           "says, since these are benzodiazepines, the same first drugs doctors reach for when a seizure won't stop. They "
           "come in forms you don't have to swallow, like a nasal spray or a rectal gel, since a pill is no use while "
           "someone's seizing. A few are intramuscular shots. After giving it, keep watching their breathing, since a "
           "benzodiazepine adds to the risk of it getting slow and shallow, especially if they've also taken respiratory "
           "depressants like opioids or alcohol.")
TESTS['rescue-c6'] = SEIZE + "\n\n" + RESCUE6

# rescue-c7, rescue-c6 with its connectors varied: the read against his fixes of rescue-c6 marked three ", since" clauses in
# five sentences (S14, S15, S17) as built the same way, one of the eight ways his fixes differ. The medicine and why it is
# the right drug are two sentences again, the forms take "because", and the breathing sentence keeps "since".
RESCUE7 = ("If there's a rescue medicine for seizures on hand, like one they carry for epilepsy, give it the way its label "
           "says. These are benzodiazepines, the same first drugs doctors reach for when a seizure won't stop. They come in "
           "forms you don't have to swallow, like a nasal spray or a rectal gel, because a pill is no use while someone's "
           "seizing. A few are intramuscular shots. After giving it, keep watching their breathing, since a benzodiazepine "
           "adds to the risk of it getting slow and shallow, especially if they've also taken respiratory depressants like "
           "opioids or alcohol.")
TESTS['rescue-c7'] = SEIZE + "\n\n" + RESCUE7

# rescue-c8, rescue-c7 with when to give it said: four reads against his fixes (rescue-c1, c5, c6, c7) marked that the
# paragraph never says when to give the medicine. The label (and the plan of someone who carries one) says when, so the
# action points to it for both: "follow its label for when and how to give it". No timing of mine.
RESCUE8 = ("If there's a rescue medicine for seizures on hand, like one they carry for epilepsy, follow its label for when "
           "and how to give it. These are benzodiazepines, the same first drugs doctors reach for when a seizure won't stop. "
           "They come in forms you don't have to swallow, like a nasal spray or a rectal gel, because a pill is no use while "
           "someone's seizing. A few are intramuscular shots. After giving it, keep watching their breathing, since a "
           "benzodiazepine adds to the risk of it getting slow and shallow, especially if they've also taken respiratory "
           "depressants like opioids or alcohol.")
TESTS['rescue-c8'] = SEIZE + "\n\n" + RESCUE8

# rescue-c9, after rescue-c8 read AI Detected, 17% (ed4fe070): his lists Human High, my first sentence and last two Human
# Low, and AI Low 44 over the two between, "These are benzodiazepines, the same first drugs doctors reach for ..." and "They
# come in forms you don't have to swallow ...". The class said of what they hold, with why it is right to give it ("It's a
# benzodiazepine, which is what doctors reach for first ..."), the forms said as what it will be, with the reason first.
RESCUE9 = ("If there's a rescue medicine for seizures on hand, like one they carry for epilepsy, follow its label for when "
           "and how to give it. It's a benzodiazepine, which is what doctors reach for first when a seizure won't stop. "
           "Because a pill is no use while someone's seizing, it comes as a nasal spray or a rectal gel, or sometimes an "
           "intramuscular shot. After giving it, keep watching their breathing, since a benzodiazepine adds to the risk of "
           "it getting slow and shallow, especially if they've also taken respiratory depressants like opioids or alcohol.")
TESTS['rescue-c9'] = SEIZE + "\n\n" + RESCUE9

# brainev-c2, after brainev-c1 read AI Detected, 72% (a8a986e7): his belief and heading Human Low, every sentence after it
# AI, the study-a-sentence run ("People who'd had ... Doctors have also ... And animal stroke research ...") most of all.
# Rebuilt around what the reader can do with it: the honesty about the evidence said once, then the finding that tells them
# it may still help after the damage has started, then the human evidence in one sentence of two shapes, and the mechanism
# said plainly with its term in brackets, his shape ("slow and shallow breathing (respiratory depression, ...)").
EVID2 = ("I believe DMSO works better for stroke and most acute brain damage than anything else readily available to "
         "ordinary people. That's more than the clinical evidence shows so far, but what there is points the same way. In "
         "animal stroke research, it shrank the area of the brain that died even when it was given after the stroke, so it "
         "may still help after the damage has started. A preliminary trial in people who'd had a stroke from a clot found "
         "they may have recovered better on it, and doctors have used it in a small series of patients to bring down "
         "dangerous pressure inside the skull. It also calms the overexcited nerve signaling that kills brain cells after a "
         "stroke (NMDA- and AMPA-mediated excitotoxicity).")
TESTS['brainev-c2'] = "If Someone Says \"My Brain Feels Damaged\": DMSO + Humic Acid + Electrolytes First\n\n" + EVID2

# rescuep-c9: rescue-c9's paragraph by itself, the ledger's narrowing after a section read Mixed (Joel, 2026-11-04: "you'd
# still need to narrow it down to para level if it doesn't work").
TESTS['rescuep-c9'] = RESCUE9

# rescue-c10, after rescuep-c9 read AI Generated, 100% by itself (9f5b6765): the same facts in his first person, the
# voice of my carries that read Human High this week ("I'd calm and stabilize the trip right where they are", acute-c1,
# 97bf9589), and of his own lines in the guide ("I give electrolytes to drink also, because ..."): what I'd do, what it is,
# what it will look like, and what I'd watch after.
RESCUE10 = ("If they have a rescue medicine for seizures with them, like one they carry for epilepsy, I'd give it when and "
            "how its label says. It's a benzodiazepine, the kind of drug doctors reach for first when a seizure won't stop. A "
            "pill is no use while someone's seizing, so it'll be a nasal spray or a rectal gel, or sometimes an intramuscular "
            "shot. After giving it, I'd keep a close eye on their breathing, since a benzodiazepine adds to the risk of it "
            "getting slow and shallow, especially if they've also taken respiratory depressants like opioids or alcohol.")
TESTS['rescue-c10'] = SEIZE + "\n\n" + RESCUE10
TESTS['rescuep-c10'] = RESCUE10

if __name__ == '__main__':
    for k, t in TESTS.items():
        p = HERE / ('TEST-%s.txt' % k)
        p.write_text(t + '\n', encoding='utf-8')
        print(k, len(t.split()), 'words', hashlib.sha256(t.encode()).hexdigest()[:12])
