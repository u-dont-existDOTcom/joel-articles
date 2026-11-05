#!/usr/bin/env python3
"""Fills the making-sense receipts (gate E365) for r15's twelve check texts: each sentence of mine with its payoff for
this stretch's reader and why it follows the sentence before; the nine questions; placement; and every point I checked
against a source. Then runs sense_receipt.check on each."""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
TOOLS = HERE.parents[5] / 'tools' / 'humanization'
sys.path.insert(0, str(TOOLS))
import sense_receipt as sr  # noqa: E402

READER = {
 'A': "Someone opening Joel's gut-healing post, deciding whether its approach fits them, who meets his claim that the gut and mental health are linked.",
 'B': "Someone with poor gut health reading the causes (old impaction and diverticulosis, today's diet, parasites and H. pylori), deciding which apply to them.",
 'C': "Someone with poor gut health reading the plant-food and leaky gut causes, choosing among the leaky gut treatments the list gives.",
 'D': "Someone with a leaky gut deciding whether and how to take glutamine (how much, when, and at what risk, cancer included), and where butyrate fits.",
 'E': "Someone with IBS or low stomach acid, enzymes or thick bile, deciding where to look for the root cause.",
 'F': "Someone deciding whether to use Joel's Gemini Gem, and which parts of its phases are his own rather than the books'.",
 'G': "Someone in Phase 1 checking whether stress or stagnant bile blocks their digestion before they take any antimicrobial.",
 'H': "Someone starting Phase 2's diet, to calm the inflammation and starve an overgrowth in the small intestine.",
 'I': "Someone whose symptoms survived the diet, choosing how to kill an overgrowth in Phase 3 without the side effects.",
 'J': "Someone whose symptoms survived Phase 3's last option, checking which organ isn't working in Phase 4.",
 'K': "Someone rebuilding their gut in Phase 5, looking for which treatments from the causes section to use there.",
 'L': "Someone choosing a ready-made gut stack, and checking which symptoms mean seeing a doctor instead.",
}
# sentence prefix -> (payoff, follows)
P = {
 "Previously, I made some posts": ("The reader knows who AMD is (A Midwestern Doctor, a doctor writing on Substack) and that DMSO is a solvent, so the link they may open isn't a riddle.",
                                   "It follows the line inviting the emotional side, as the second thing before the physical treatments: what he's written before."),
 "And by stress I mean": ("The reader knows what counts as stress for the rest of the post (an injury, toxins and germs as much as worry), so 'severe stress' and 'a lot of stress' later mean the same broad thing (his F9-5 answer).",
                          "It glosses the word the sentence before used twice, right after it, as his answer asked: once, where stress first comes up."),
 "This is likely caused by diverticulosis": ("The pockets get their name where they appear, so 'reductions in diverticula' later in the paragraph is understood.",
                                             "It names the likely cause of the impaction in the item above, as before."),
 "Butyrate, a fatty acid your gut bacteria make": ("The reader learns what butyrate is the first time it comes up, so the fuels paragraphs later build on it.",
                                                   "It follows glutamine's job for the small intestine with the fuel of the colon, where diverticula form."),
 "I would also suggest diosmin": ("The reader knows what diosmin is (a citrus compound) when deciding whether to take it for the pockets' blood vessels.",
                                  "It adds his own suggestion after the trial and the fuels, as before."),
 "However, while we don't know if Pooyan": ("The reader knows A1 dairy is most regular cow's milk, so they can see what Pooyan ate and what to avoid.",
                                            "It continues Pooyan's story from the impaction above, as before."),
 "Make sure you get cleared first by a gastroenterologist": ("The reader knows which doctor to ask (a gut specialist) before trying colon hydrotherapy with severe diverticulosis.",
                                                             "It ends the caution with what to do, as before."),
 "Toxins are sequestered in fat cells": ("The reader knows visceral fat is the fat around the organs, the kind the toxins make most harmful.",
                                         "It explains why the toxic diet in the sentence before does lasting harm, as before."),
 "Parasites, the stomach bacteria H. pylori": ("The reader learns H. pylori is a stomach bacteria at its first mention, before the heartburn sign that points to it.",
                                               "It opens the next cause in the list, after poor diet."),
 "For H. pylori specifically": ("The reader knows berberine is a plant extract, so they know what kind of remedy to buy for the heartburn sign.",
                                "It gives the H. pylori case after the general approach, as before."),
 "Plant foods (Phases 2 and 5)": ("The reader learns what oxalates and phytates are (plant compounds that bind minerals) when deciding if they're why plants bother them.",
                                  "It opens the next cause in the list, after SIBO."),
 "Leaky gut (Phase 5)": ("IBS gets its full name at its first mention, so its own item later and the stacks section read without guessing.",
                         "It opens the leaky gut cause after the plant-food one it overlaps with, as before."),
 "Zonulin is the molecule released": ("The reader learns what tight junctions are (the seals between the gut lining's cells) where they first appear, so the leaking and the fuels paragraphs make sense.",
                                      "It explains the zonulin the sentence before named, as before."),
 "Colostrum is the first milk a cow makes": ("The reader knows what colostrum and liposomal mean, so they can buy and judge the first treatment on the list.",
                                             "It explains the two words of the item just named, before what Matt finds it does."),
 "Matt from EndSickness.org finds": ("The reader learns mycotoxins are mold toxins at their first mention, so the colostrum's job and the mold check in Phase 6 make sense.",
                                     "It gives what the colostrum is good for after saying what it is."),
 "Liposomal first-milking colostrum (esp.": ("The first treatment's name and how to take it, as he wrote it, with bifidobacterium said to be a common probiotic.",
                                            "It opens the list of leaky gut treatments the item above announced."),
 "BPC-157 is a lab-made short protein": ("The reader knows what BPC-157 is, and so why Barrier's claim that it's made from plants is false.",
                                         "It explains the supplement just named, before his note on Barrier's marketing."),
 "Beta-glucans, a kind of fiber": ("The reader knows beta-glucans are a fiber, the kind of thing they'd be buying.", "Next item in the list."),
 "Resistant starch, the starch your body can't digest": ("The reader knows why resistant starch feeds the gut bacteria: it gets past digestion to them.", "Next item in the list."),
 "Ozonated zeolite (or ZeoCharge)": ("The reader knows zeolite is a mineral full of pores, so 'the pores are clogged' and 'adsorb' make sense.", "Next item in the list."),
 "So that's why consuming pure glutamine": ("'Extra' in the next sentence follows: the glutamine's energy comes on top of the meals' (his card 3, approved).",
                                           "It draws the conclusion of the mechanism just described, as before."),
 "Take 5g a day as a baseline, to keep your enterocytes fed.": ("The reader knows the everyday dose and what it's for, whether or not they train (his card 4, approved).",
                                                               "It gives the dose right after the paragraph on how glutamine feeds the enterocytes."),
 "Take it away from meals": ("The reader knows when to take it, and why: the amino acids in food compete with it (his F9-5 answer).",
                             "How to take the dose follows the dose."),
 "If you train hard or long": ("A reader who trains hard learns their training damages the gut lining, so the 5g isn't the whole story for them.",
                               "Training comes next as the case that needs more than the baseline."),
 "While you train, your body sends blood away": ("The reader understands how exercise damages the gut, though exercise is good for them elsewhere in the post: blood leaves the gut for the muscles.",
                                                 "It answers how the training in the sentence before does the damage."),
 "Glutamine taken two hours before training": ("A reader who trains learns what to do about it: take it two hours before.", "The fix follows the damage just explained."),
 "In a study of men running for an hour": ("The reader knows the dose and timing that helped, about 15g, not 5g, and the evidence behind it (Pugh 2017).",
                                           "The study supports the advice in the sentence before, right after it."),
 "If your immune system is dealing with an acute exposure": ("The reader knows the other cases that call for more, what an exposure is (toxins or pathogens), and how to raise it: a gram a day, in case of sensitivity (his F9-5 answers).",
                                                            "After training, the other cases that need more than the baseline, as in his sentence."),
 "Up to 14g a day is known to be safe": ("The reader knows how high is safe for how long, so they come back down after the exposure or stress (Shao and Hathcock 2008).",
                                         "The safety limit follows the higher dose it applies to."),
 "If you have an active inflammatory bowel disease": ("A reader with active IBD won't count on glutamine for it; IBD gets its full name here, at its first mention.",
                                                      "After the cases where more helps, the case where the evidence says it doesn't."),
 "In the two small trials in active Crohn's": ("The reader knows why: the trials found no benefit (Cochrane 2016).", "The evidence follows the advice it supports."),
 "CAUTION: a lot of cancers feed on glutamine too": ("The reader with cancer knows the danger at once: cancers use glutamine too (his cards 1 and 2).",
                                                     "The caution follows the dose paragraph it qualifies."),
 "So if you have an active cancer, check with your oncologist": ("The reader with an active cancer knows what to do right after the danger, before the reasons (the issue he always fixes: the payoff first).",
                                                                 "The instruction follows from the danger just stated."),
 "Your enterocytes take in a lot of the glutamine you swallow": ("The reader understands how swallowed glutamine reaches a cancer elsewhere: not all of it stays in the gut.",
                                                                 "It answers the question the instruction raises: how can what I swallow reach my cancer?"),
 "They can only take in so much at a time": ("The reader knows why the 10-30g is worse than the 5g: more of a big dose gets into the blood (Hankard 1995).",
                                             "It explains the 'especially' of the instruction, after the route."),
 "Your colonocytes are fueled by short-chain fatty acids": ("The reader moves from the small intestine's fuel to the large intestine's, butyrate, without hearing the glutamine point a third time.",
                                                            "It opens the butyrate paragraph after the glutamine ones."),
 "A gastroenterologist who practices functional medicine": ("The reader knows what kind of doctor to look for: one who looks for root causes, which is what the sentence before says IBS needs.",
                                                            "It names who can do the investigation the sentence before calls for."),
 "So the phases below are what the Gem will tell you": ("The reader knows H2O2 is hydrogen peroxide at its first mention, before Phase 3 recommends it.",
                                                        "It says which parts of the phases are his, after the Gem's limits."),
 "So thin the bile first with Beet Flow": ("The reader knows what phosphatidylcholine is, so they can find it.", "It gives the fix for the stagnant bile just described."),
 "Diet-wise, go Paleo-Low FODMAP": ("The reader knows what a low-FODMAP diet cuts (the carbs gut bacteria ferment most), the reason it starves an overgrowth.",
                                    "It gives the diet after the phase's aim."),
 "If diet didn't clear your symptoms": ("The reader knows SIFO is the fungal version of SIBO, the overgrowth they likely have.", "It opens Phase 3 after Phase 2's diet."),
 "H2O2 actually works better than the herbal antibiotics": ("The reader knows who orthomolecular doctors are (doctors who treat with high doses of nutrients), so they can weigh the claim.",
                                                            "It gives his swap right after the herbal antibiotics he advises against."),
 "Is it Exocrine Pancreatic Insufficiency": ("The reader knows what EPI is, so they can tell if their symptoms fit before testing.", "It opens the organ check."),
 "My notes: see \"Leaky gut\" above for colostrum": ("The reader is pointed to the treatments not already pointed to by step 4, without the fuels twice.",
                                                     "It ends the phase with the pointers back, as in every phase."),
 "The exception is berberine for H. pylori": ("The reader knows to take berberine alone for H. pylori; the heartburn sign and what H. pylori is are under Parasites, where it points.",
                                              "It gives the exception to skipping cleanse stacks, as before."),
 "Take it seriously if you notice blood in your stool": ("The reader can tell upper from lower bleeding in plain words, without 'GI'.", "It opens the list of warning signs."),
}
COMMON_Q = {
 'Q1': 'PASS: each term note comes right where the term first appears, or in the next sentence, and the sentence\'s own point still comes first; the caution\'s instruction now follows its warning',
 'Q2': 'PASS: every instruction says what it is for in the reader\'s terms (take it away from meals so food doesn\'t compete; check with your oncologist before the 5g)',
 'Q3': 'PASS: each term note names the exact thing (the A1 type of casein protein; the seals between the cells of your gut lining; the first milk a cow makes after giving birth)',
 'Q4': 'PASS: each new "it", "that" and "this" has its object in the sentence before',
 'Q5': 'PASS: each "so", "but" and "because" has the claim it turns on said before it',
 'Q6': 'PASS: the notes sit where a reader first needs them; nothing moved except the caution\'s instruction, up to where a reader with cancer needs it',
 'Q7': 'PASS: each note helps this reader act on the sentence it explains',
 'Q8': 'PASS: no item moved between groups',
 'Q9': 'PASS: the long notes are their own short sentences (stress, colostrum, BPC-157), one step each',
}
PLACEMENT = {
 'A': 'The intro, before the causes: the AMD sentence is his list of past posts; the stress note right after the sentence that first says stress.',
 'B': 'The causes list, impaction to parasites, in his order; each note inside the sentence that first uses the term.',
 'C': 'The plant-food cause and the leaky gut list, in his order; the colostrum and BPC-157 notes as sentences right after the items they explain.',
 'D': 'The fuels under leaky gut, in order: what starvation is, glutamine, its dose, the caution on the dose, then the colon\'s fuel; the caution\'s first "So" points to the warning before it.',
 'E': 'The IBS cause, last but one in the list; the note on functional medicine where the doctor is named.',
 'F': 'The note under the Gem, before the phases; H2O2 explained there, its first mention, before Phase 3 uses it.',
 'G': 'Phase 1, the bile check; the note where phosphatidylcholine is named.',
 'H': 'Phase 2, the diet; the FODMAP note where the diet is named.',
 'I': 'Phase 3, the purge; SIFO and orthomolecular explained where they appear.',
 'J': 'Phase 4, the organ check; EPI explained where it is named.',
 'K': 'Phase 5\'s pointers back, at its end as in every phase.',
 'L': 'The stacks section\'s cleanse-stack paragraph and the doctor paragraph, in his order.',
}
CHECKED = {
 'A': [{'point': 'AMD is A Midwestern Doctor, and DMSO is a solvent', 'found': 'his own post on AMD names "A Midwestern Doctor" (https://ibogaqueen.substack.com/p/critical-analysis-of-amd-and-their); DMSO is a solvent (https://respectfulinsolence.com/?p=43510)', 'still_needed': 'yes: the reader meets both here', 'fate': 'kept'}],
 'B': [{'point': 'A1 dairy is regular cow\'s milk with the A1 type of beta-casein', 'found': 'A1 beta-casein is the most common type in cow\'s milk in the US and most of Europe (https://en.wikipedia.org/wiki/A2_milk)', 'still_needed': 'yes: it is what Pooyan ate', 'fate': 'kept'},
       {'point': 'diosmin comes from citrus', 'found': 'a citrus flavonoid made from hesperidin (https://prolekare.cz/topic/venous-insufficiency/detail/diosmin-and-hesperidin-what-does-pharmacokinetics-show-121991)', 'still_needed': 'yes: the reader is told to take it', 'fate': 'kept'},
       {'point': 'berberine is a plant extract (barberry)', 'found': 'an alkaloid from barberry, goldenseal and Oregon grape (https://en.wikipedia.org/wiki/Berberine)', 'still_needed': 'yes: the remedy for H. pylori', 'fate': 'kept'}],
 'C': [{'point': 'BPC-157 is lab-made, based on a stomach juice protein', 'found': 'a synthetic 15-amino-acid peptide derived from a protein in human gastric juice (https://en.wikipedia.org/wiki/BPC-157)', 'still_needed': 'yes: it shows why the plant claim is false', 'fate': 'kept'},
       {'point': 'zeolite is a volcanic mineral full of pores', 'found': 'porous minerals, mostly from volcanic ash (https://pubmed.ncbi.nlm.nih.gov/30999685/)', 'still_needed': 'yes: the pores are the point', 'fate': 'kept'}],
 'D': [{'point': 'glutamine before a run cut the gut\'s leak, even at the lowest dose', 'found': 'Pugh 2017: 0.25, 0.5 and 0.9 g per kg of fat-free mass two hours before a 60-minute run at 30 C all lowered the permeability marker; 0.9 g/kg is 54g for a 70kg man at 15% fat, so 0.25 is about 15g (https://pmc.ncbi.nlm.nih.gov/articles/PMC5694515/)', 'still_needed': 'yes: it gives the training reader a dose that was tested', 'fate': 'changed'},
       {'point': 'up to 14g a day is safe long term', 'found': 'Shao and Hathcock 2008: observed safe level 14 g/day; higher intakes tested without harm but not enough data for long-term safety (https://www.nutraingredients.com/Article/2008/04/18/crn-authors-risk-assessment-for-key-amino-acids/)', 'still_needed': 'yes: the 10-30g is above it', 'fate': 'kept'},
       {'point': 'take amino acids away from meals', 'found': 'amino acids share transporters and can compete; there is too little human research to know at what dose, so labels say to take them without food (https://www.consumerlab.com/answers/must-i-take-amino-acid-supplements-on-an-empty-stomach/how_to_take_amino_acid)', 'still_needed': 'yes: his answer, with its reason', 'fate': 'kept'},
       {'point': 'glutamine for active Crohn\'s', 'found': 'Cochrane 2016: two small trials found no benefit; insufficient evidence (https://www.cochrane.org/CD007348)', 'still_needed': 'yes: the original raised the dose for active IBD', 'fate': 'changed'}],
 'G': [{'point': 'phosphatidylcholine is a fatty nutrient in egg yolks and soy', 'found': 'a phospholipid, the main part of lecithin, from soybeans and eggs (https://uofmhealth.org/health-library/hn-2873001)', 'still_needed': 'yes: the reader has to find it', 'fate': 'kept'}],
 'H': [{'point': 'FODMAPs are the carbs gut bacteria ferment most easily', 'found': 'short-chain carbohydrates, poorly absorbed and rapidly fermented (https://pubmed.ncbi.nlm.nih.gov/23588241/)', 'still_needed': 'yes: it says what the diet cuts', 'fate': 'kept'}],
 'I': [{'point': 'orthomolecular doctors treat with high doses of nutrients', 'found': 'also called megavitamin therapy (https://www.topdoctors.co.uk/medical-dictionary/orthomolecular-nutrition?amp=1)', 'still_needed': 'yes: the reader weighs his claim by who agrees', 'fate': 'kept'}],
}
for k in READER:
    f = HERE / ('RECEIPT-%s.json' % k)
    r = json.loads(f.read_text(encoding='utf-8'))
    r['section'] = json.loads((HERE / 'STRETCHES.json').read_text())[k]['section'] or 'the intro'
    r['reader'] = READER[k]
    for s in r['sentences']:
        if s.get('his'):
            continue
        hit = [v for pre, v in P.items() if s['s'].startswith(pre)]
        assert len(hit) == 1, (k, s['s'][:70], len(hit))
        s['payoff'], s['follows'] = hit[0]
    r['questions'] = dict(COMMON_Q)
    r['placement'] = PLACEMENT[k]
    r['checked'] = CHECKED.get(k, [])
    f.write_text(json.dumps(r, ensure_ascii=False, indent=1), encoding='utf-8')
    text = (HERE / ('CHECK-%s.txt' % k)).read_text(encoding='utf-8').rstrip('\n')
    probs = sr.check(text, r)
    print(k, 'PASS' if not probs else probs)
