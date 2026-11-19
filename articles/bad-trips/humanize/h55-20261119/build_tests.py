#!/usr/bin/env python3
"""build_tests.py - turn 45 (2026-11-19, his round-40 export of 00:52 UTC): what his Chest Pain version teaches, carried to
the other evidence passages of mine (CURRENT-STATE's next step).

Lesson bad-trips-2026-11-19a (docs/lessons/2026-11-19-0052-bad-trips.md): say first whether what follows bears on the
reader's case, and put the limit that decides it in the first sentence, never in a clause hung on a finding. His words: "i
flipped it high conf human by moving the payoff earlier about whether they are about to read something relevant or not".
With it the linter's O75 (a past perfect where the simple past does) and O76 (one abbreviation in three sentences in a row).

- cyp-c1, cyp-c2: Suspected Serotonin Syndrome's step 2 (B136, item 2), cyproheptadine. The sources (PubMed): Graudins et
  al. 1998 (9696181): five patients given 4-8 mg by mouth, three with no signs left within 2 h, the other two after a repeat
  dose, "it is unknown whether cyproheptadine modifies patient outcome"; King & Rotella 2025 (39791184): twelve reports from
  2003 on, every one very low evidence, "a lack of evidence to support the efficacy of cyproheptadine". The limit that
  decides how much the reader can lean on it (only case reports) said first, the review's verdict with it, then the series;
  c1 has the receptors with the series, c2 with the step.
- mdma-c1, mdma-c2: MDMA's paragraph after his second wife's story (B119). Atila et al. 2024 (39546312): four placebo-
  controlled trials, 96 healthy volunteers given one 100 or 125 mg dose, low sodium in 30 (31%), none of the 15 whose
  drinking was limited. What bears on the reader first: even one normal dose; and what it means for them, small sips (the
  guide's own advice at "Water? (in small sips)"). The kidney review (Bora et al. 2016, 27917269) goes on B120's "acute
  kidney injury", the next paragraph's same claim, so the paragraph doesn't say kidney injury twice. c1 keeps the
  original's order; c2 puts the trial next to the sign it explains.
- b106-now, b106-c1: My Brain Feels Damaged's DMSO-and-bleeding paragraph (B106): his three bleed lines (K4) and my two
  before them, which his round-38 version left in place, never checked by themselves: b106-now as it stands; b106-c1 opens
  on his lines, the limit that decides whether DMSO is for this reader at all (a possible bleed), and ends on mine with its
  payoff (they can feel better while a clot or bleed is still there, so the checks go on). b106-c1 says W008 ("The larger
  adjacent risk ...") in other words, which the fidelity keys hold to "adjacent": a card for him if it is the one that reads
  High.

  python3 build_tests.py
"""
import hashlib, pathlib
HERE = pathlib.Path(__file__).resolve().parent

CYP_STEP = "If the person is fully alert and able to swallow, I would give cyproheptadine early."
SERIES = ("When doctors gave it by mouth to five patients, three had no signs left within two hours, and the other two after "
          "a second dose.")
SERIES_MD = SERIES.replace('gave it by mouth to five patients',
                           '[gave it by mouth to five patients](https://pubmed.ncbi.nlm.nih.gov/9696181/)')
REVIEW = '[a recent review](https://pubmed.ncbi.nlm.nih.gov/39791184/)'
# c1: the receptors with the limit (after the linter: "It blocks serotonin receptors, and when doctors ..." packed, B4)
CYP1_S2 = ("It blocks serotonin receptors, but so far the evidence for it has only been case reports, and a recent review "
           "found them too weak to say whether it changes the outcome.")
CYP1 = ' '.join([CYP_STEP, CYP1_S2, SERIES, "I wouldn't wait to see whether it works before doing the other steps."])
# c2: his Chest Pain shape: the receptors with the step, then "So far, ..." first
CYP2_S1 = ("If the person is fully alert and able to swallow, I would give cyproheptadine early, since it blocks serotonin "
           "receptors.")
CYP2_S2 = ("So far, the evidence for it has only been case reports, and a recent review found them too weak to show that it "
           "works.")
CYP2 = ' '.join([CYP2_S1, CYP2_S2, SERIES, "I wouldn't wait for it to work before doing the other steps."])
CYP1_MD = ' '.join(["2. **" + CYP_STEP + "**", CYP1_S2.replace('a recent review', REVIEW), SERIES_MD,
                    "I wouldn't wait to see whether it works before doing the other steps."])
CYP2_MD = ' '.join(["2. **" + CYP_STEP[:-1] + "**, since it blocks serotonin receptors.", CYP2_S2.replace('a recent review', REVIEW),
                    SERIES_MD, "I wouldn't wait for it to work before doing the other steps."])

# MDMA: the linter's lists of three taken apart (E125), "one" gone (O46), the trial split from its payoff
JAW = "When their jaw tenses, that's also the time to stop taking MDMA and get them to slow down and cool off."
TRIAL = "When healthy volunteers took it once in clinical trials, about a third ended up with low sodium (hyponatremia)."
TRIAL_MD = TRIAL.replace('When healthy volunteers took it once in clinical trials',
                         '[When healthy volunteers took it once in clinical trials](https://pubmed.ncbi.nlm.nih.gov/39546312/)')
CALL = ("A seizure or a collapse raises the stakes, so call medics, since overheating and MDMA toxicity can cause those "
        "too.")
MDMA1 = ' '.join([
    JAW,
    "Keep watching them: a headache that keeps getting worse can mean their sodium is getting too low, and so can confusion "
    "or vomiting.",
    "Weakness or palpitations can mean their potassium is dropping.",
    CALL,
    "Even a single normal dose can drop sodium.",
    TRIAL,
    "None of the volunteers whose drinking was limited did, so keep water to small sips."])
TRIAL_L = TRIAL[0].lower() + TRIAL[1:]
TRIAL_L_MD = '[' + TRIAL_MD[1].lower() + TRIAL_MD[2:]
# c2: the trial beside the sign it explains, and the headache's signs split (E125: "if every item is needed, split it")
MDMA2 = ' '.join([
    JAW,
    "Watch for a headache that keeps getting worse.",
    "If they also get confused or start vomiting, their sodium may be getting too low, and even a single normal dose can do "
    "that: " + TRIAL_L,
    "None of the ones whose drinking was limited did, so keep water to small sips.",
    "Weakness or palpitations can mean low potassium instead.",
    CALL])

HIS_BLEED = ("If someone is worried about a bleed, I'd probably skip DMSO, but it depends on how severe their issue is. It's "
             "not a powerful blood thinner like heparin, unless maybe injected; it's basically a dietary blood thinner. I've "
             "never had any issues with bleeding too much from consuming DMSO, and never heard of it either, but if bleeding "
             "is already a medical issue I'd want to think about that more.")
MINE_NOW = ("DMSO cannot identify whether the problem is a clot, a hemorrhage, low oxygen, an electrolyte crisis, or something "
            "else. The larger adjacent risk is losing a treatment window or missing a bleed because the symptoms improved "
            "enough to feel reassuring.")
B106_NOW = MINE_NOW + ' ' + HIS_BLEED      # the paragraph as it stands (B106), never checked by itself
B106_1 = HIS_BLEED + ' ' + ("They can feel better on DMSO while a clot or a bleed is still there. So if any of the checks "
                            "above fail, call medics anyway, while a hospital can still treat it.")

TESTS = {'cyp-c1': CYP1, 'cyp-c2': CYP2, 'mdma-c1': MDMA1, 'mdma-c2': MDMA2, 'b106-now': B106_NOW, 'b106-c1': B106_1}
MD = {'cyp-c1': CYP1_MD, 'cyp-c2': CYP2_MD,
      'mdma-c1': MDMA1.replace(TRIAL, TRIAL_MD),
      'mdma-c2': MDMA2.replace(TRIAL_L, TRIAL_L_MD),
      'b106-now': B106_NOW, 'b106-c1': B106_1}

# ---- after the three reads of h55a's first drafts (reads/), batch h55a's texts --------------------------------------------
# cyp-c3: the five-patient series cut (the needed read: "Five hospital cases give the reader no dose to give and no action";
# the fit read: "sounds like proof the drug works, even though S2 says the evidence is weak"; the read against his fixes of
# c1: way 7), its study linked on "case reports", which rest on it; c2's wording, which that read marked nowhere.
CYP3 = ' '.join([CYP2_S1, CYP2_S2, "I wouldn't wait to see whether it does before doing the other steps."])
CYP3_MD = ' '.join(["2. **" + CYP_STEP[:-1] + "**, since it blocks serotonin receptors.",
                    CYP2_S2.replace('case reports', '[case reports](https://pubmed.ncbi.nlm.nih.gov/9696181/)')
                           .replace('a recent review', REVIEW),
                    "I wouldn't wait to see whether it does before doing the other steps."])
# mdma-c3, c4: who stops said ("don't let them take any more MDMA"), no "also" pointing outside the paragraph; the trial's
# number cut (the needed read) and its payoff said as what to do, sip an electrolyte drink when thirsty (the guide's own
# electrolytes, B103 and step 6), so it can't read as "restrict water" (the fit read); each sign said as it gets worse, with
# what to do (the read against his fixes: way 7; the fit read: ANYWAY, these come with MDMA anyway); the seizure line
# opening on the friend (way 5). c3 says the signs as statements, c4 as his triage questions (way 1's example). After the
# read of mdma-c2 against his fixes (reads/his-mdma-c2.txt): what decides whether the trial bears on them (drinking a lot
# of plain water) before the finding (way 9, lesson 19a); weakness said as what they'd notice; the seizure line ending on
# calling medics, its other causes before it.
JAW3 = "Once their jaw tenses, that's their last dose of MDMA, so get them to slow down and cool off."
SIP = ("If they drink a lot of plain water, even a single normal dose raises the risk of their sodium dropping too low, so "
       "have them sip an electrolyte drink when they're thirsty instead.")
SIP_MD = SIP.replace('even a single normal dose', '[even a single normal dose](https://pubmed.ncbi.nlm.nih.gov/39546312/)')
SEIZE = ("A seizure or collapse can also come from overheating or MDMA toxicity, so if either happens, call medics right "
         "away.")
MDMA3 = ' '.join([
    JAW3, SIP,
    "If a headache keeps getting worse, the vomiting keeps coming back, or they're getting more and more confused, their "
    "sodium may already be low, so call medics.",
    "Do the same if their muscles keep getting weaker or their palpitations keep getting stronger, which can mean low "
    "potassium, like my second wife had.",
    SEIZE])
SIP4 = ("If they've been drinking a lot of plain water, even a single normal dose raises that risk, so have them sip an "
        "electrolyte drink when they're thirsty instead.")
MDMA4 = ' '.join([
    JAW3,
    "Is a headache getting worse and worse, does the vomiting keep coming back, or are they more and more confused?",
    "Their sodium may be getting too low, so call medics.",
    SIP4,
    "Are their muscles getting weaker, or their palpitations getting stronger?",
    "That can mean low potassium, like my second wife had, and they need medics for that too.",
    SEIZE])
# b106-c2: the read against his fixes marked S5's "while ... still", built like S4's (way 2): S5 ends on the action and the
# original's treatment window
B106_2 = HIS_BLEED + ' ' + ("They can feel better on DMSO with a clot or a bleed still there. So if any of the checks above "
                            "fail, call medics right away, before the window for treating a stroke closes.")
TESTS.update({'cyp-c3': CYP3, 'mdma-c3': MDMA3, 'mdma-c4': MDMA4, 'b106-c2': B106_2})
MD.update({'cyp-c3': CYP3_MD, 'mdma-c3': MDMA3.replace(SIP, SIP_MD),
           'mdma-c4': MDMA4.replace(SIP4, SIP4.replace('even a single normal dose',
                                                       '[even a single normal dose](https://pubmed.ncbi.nlm.nih.gov/39546312/)')),
           'b106-c2': B106_2})

# ---- after h55a (RESULTS-h55a.json) ----------------------------------------------------------------------------------------
# cyp-c3 read AI Detected 79%: the step Human Low, then "So far, the evidence ... too weak to show that it works. I wouldn't
# wait ..." AI Medium: a bare limit with nothing in it a reader can see. His round-40 version kept the study's concrete
# finding after the limit ("When they gave it to rats for three days before a heart attack, those rats lost ... than the
# rats who didn't get DMSO"). cyp-c4: the limit first, said as why case reports can't show it works (no one to compare
# against: the fit read's "With no comparison group, I can't tell the drug apart from the signs fading on their own"),
# then the series with the payoff the read against his fixes asked for ("turn it into what to expect ... so don't count on
# it working fast").
# After its reads (reads/, the text they read kept as read-text-cyp-c4.txt): "early" said as the moment (the read against
# his fixes: way 4); the second dose said as "took longer" (the fit read: "no dose and no time gap for the second dose";
# the needed read of c1: "invites repeat dosing"); the summing-up cut and the line ending on what to do (way 6).
CYP4_S1 = ("If the person is fully alert and able to swallow, I would give cyproheptadine right away, since it blocks serotonin "
           "receptors.")
CYP4_S2 = ("So far, the evidence for it has only been case reports, where nobody could compare it against people who didn't "
           "get it.")
CYP4_S3 = ("When doctors gave it to five patients, three had no signs left within two hours, and the other two took longer, so "
           "keep going with the other steps while you see whether it works.")
CYP4 = ' '.join([CYP4_S1, CYP4_S2, CYP4_S3])
CYP4_MD = ' '.join([
    "2. **If the person is fully alert and able to swallow, I would give cyproheptadine right away**, since it blocks "
    "serotonin receptors.",
    CYP4_S2.replace('case reports', '[case reports](https://pubmed.ncbi.nlm.nih.gov/39791184/)'),
    CYP4_S3.replace('gave it to five patients', '[gave it to five patients](https://pubmed.ncbi.nlm.nih.gov/9696181/)')])
# mdma-c3 read AI Detected 87%: the first line Human Low, the water line AI Medium, and the three sign sentences AI High
# together, each built the same way ("If ... keeps getting worse ..., so call medics." "Do the same if ... keep getting
# ..."). mdma-c4: the water line as what he'd do ("I'd have them sip"), with what decides the risk before the finding; each
# sign sentence built its own way (how it tends to show up; the palpitations glossed as what they'd notice; "And if"
# ending on the call).
# After its reads (reads/, the text they read kept as read-text-mdma-c4b.txt): low sodium named where the headache comes
# (the fit read: "that" has nothing to point to); weakness and palpitations said as they get worse, "skips beats" (the
# fit read: a pounding heart and tired muscles come with MDMA anyway), "instead" and the squeezed "like my second wife's"
# out (the read against his fixes, ways 1 and 3; her story is the paragraph before), each line built its own way (way 2),
# the seizure line straight to the call (way 7), with the toxicity his paragraph before names ("I treat serious MDMA
# toxicity as a broader electrolyte emergency").
MDMA4B = ' '.join([
    JAW3,
    "If they're drinking a lot of plain water, even a single normal dose raises the risk of their sodium dropping too low, "
    "so I'd have them sip an electrolyte drink when they're thirsty.",
    "A headache that gets worse and worse is how low sodium tends to show up, often with throwing up or confusion, and it's "
    "time to call medics.",
    "The same goes for muscles getting weaker and weaker, or palpitations where the heart skips beats, which can mean their "
    "potassium is low.",
    "And a seizure or collapse means the MDMA toxicity has become an emergency, so get medics there right away."])
TESTS.update({'cyp-c4': CYP4, 'mdma-c4b': MDMA4B})
MD.update({'cyp-c4': CYP4_MD,
           'mdma-c4b': MDMA4B.replace('even a single normal dose', '[even a single normal dose](https://pubmed.ncbi.nlm.nih.gov/39546312/)')})

# ---- after h55c (RESULTS-h55c.json): c4 of each read AI Generated, 100%, one AI High window over all of it, worse than
# c3 (79%, 87%). c3 and c4 changed order and builds in my plain instructing voice; in b106-now (h55a) his bleed lines read
# Human High beside my two sentences' AI High, in his first person with his hedges and asides ("I'd probably skip DMSO,
# but it depends ...", "unless maybe injected; it's basically a dietary blood thinner"). c5 of each: his first person
# ("I'd"), the drug said as what it is (cyproheptadine, a term a reader wouldn't know, unexplained since the original),
# asides in brackets, the limit still first (lesson 19a). No experience of his is claimed that he hasn't told.
# After its reads (reads/, the text they read kept as read-text-cyp-c5.txt): the drug glossed inside the sentence that
# first names it (the rule of gates E368 and E369), its "which is why it can help here" cut (the needed read; the read
# against his fixes, way 8); "three of them" with no "took a bit longer" (the fit read: "leaves the impression that all five
# did well"; the read against his fixes: "doesn't say how long"); the last line opening on what keeps going (cooling) and
# what the reader sees (moderate or severe signs), as the read against his fixes asked (way 5).
CYP5 = ' '.join([
    "If the person is fully alert and able to swallow, I'd give them cyproheptadine right away, an old allergy medicine that "
    "also blocks serotonin receptors.",
    "The evidence for it is only case reports so far (nobody has compared it against people who didn't get it), but in a "
    "small series of five ER patients, three of them had no symptoms left within two hours.",
    "Keep cooling them down either way, and get help now if their signs are moderate or severe, before you know whether it "
    "works."])
CYP5_MD = ("2. **If the person is fully alert and able to swallow, I'd give them cyproheptadine right away.** " + CYP5.split(' ', 17)[-1]
           if False else None)
# After its reads (reads/, the text they read kept as read-text-mdma-c5.txt): why the jaw tension means the last dose said
# (the fit read: jaw tension comes with MDMA anyway; "more only adds to the toxicity", the toxicity his paragraph before
# names); the water line split, the fix its own clause (the read against his fixes, ways 1 and 4); the signs gathered
# and built two ways, each past what MDMA does anyway ("so weak they can barely stand", "feeling irregular"; the fit read),
# and one call to medics for all of them (way 2: "say call medics once"); her story left to the paragraph before (the
# needed read: "the reader can lose that clause").
MDMA5 = ' '.join([
    "Once their jaw tenses, I'd make that their last dose of MDMA, since more only adds to the toxicity, and get them to "
    "slow down and cool off.",
    "I'd also watch how much plain water they drink.",
    "If they're downing bottle after bottle, even a single normal dose raises the risk of their sodium dropping too low, so "
    "give them an electrolyte drink to sip when they're thirsty instead.",
    "Low sodium tends to show up as a headache that keeps getting worse, often with throwing up or confusion, and low "
    "potassium can leave their muscles so weak they can barely stand, or their heartbeat feeling irregular (palpitations).",
    "Call medics for any of these, and get them there right away for a seizure or collapse."])
TESTS.update({'cyp-c5': CYP5, 'mdma-c5': MDMA5})
MD.update({
    'cyp-c5': CYP5.replace("If the person is fully alert and able to swallow, I'd give them cyproheptadine right away,",
                           "2. **If the person is fully alert and able to swallow, I'd give them cyproheptadine right away**,")
                  .replace("only case reports so far", "only [case reports](https://pubmed.ncbi.nlm.nih.gov/39791184/) so far")
                  .replace("a small series of five ER patients", "[a small series of five ER patients](https://pubmed.ncbi.nlm.nih.gov/9696181/)"),
    'mdma-c5': MDMA5.replace('even a single normal dose', '[even a single normal dose](https://pubmed.ncbi.nlm.nih.gov/39546312/)')})

if __name__ == '__main__':
    for k, t in TESTS.items():
        (HERE / ('TEST-%s.txt' % k)).write_text(t + '\n', encoding='utf-8')
        (HERE / ('MD-%s.md' % k)).write_text(MD[k] + '\n', encoding='utf-8')
        print(k, len(t.split()), 'words', hashlib.sha256(t.encode()).hexdigest()[:12])
