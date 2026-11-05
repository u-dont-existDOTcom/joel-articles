#!/usr/bin/env python3
"""r15 = r12 (the text in his post) + his batch-9 answers (2026-11-05 18:43 UTC, ../../experiments/t14-answers/) + every
term introduced once, at its first use (his rule, same message: "make sure every term is introduced once at first ...
you don't need to ask me when making those obvious changes") + the obvious repeats cut. Each change is (block, old, new,
kind, why); old must occur once in its block. Writes r15.md and CHANGES.json. No API calls."""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[4]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402

R12 = (HERE.parent / 'r12' / 'r12.md').read_text(encoding='utf-8')
R14 = HERE.parent / 'r14'
P20_HIS = ("L-Glutamine ([watch Dr. Rhonda vid](https://m.youtube.com/watch?v=5DVUEKrekYw&ra=m)) is the main fuel for your "
           "enterocytes, and for your immune cells when they're activated. It doesn't have to go through the complicated "
           "digestive steps other nutrients do. Inside the mitochondria, it gets converted into alpha-ketoglutarate, or "
           "α-KG, which then goes into the citric acid cycle, which is how the mitochondria make their energy. So that's why "
           "consuming pure glutamine gives energy to those cells faster than eating food, on top of what they get from their "
           "meals. They then use their extra energy to repair the gut lining by pulling the tight junctions together, and "
           "that keeps LPS from getting through. Glutamine also provides nitrogen to help build new cells.")
P21_NEW = ("Take 5g a day as a baseline, to keep your enterocytes fed. Take it away from meals, so it doesn't have to compete "
           "with the amino acids in your food to get absorbed. If you train hard or long, like CrossFit or intense cardio, "
           "your gut lining takes damage. While you train, your body sends blood away from your gut to your working muscles, "
           "so your enterocytes get less oxygen and fuel. Glutamine taken two hours before training helps with that. In a "
           "study of men running for an hour in the heat, their gut lining leaked less, even at the lowest dose tested, about "
           "15g for a 70kg man. If your immune system is dealing with an acute exposure to toxins or pathogens, or your whole "
           "system is under a lot of stress, raise it to 10-30g a day, adding 1g a day in case you're sensitive to it. Up to "
           "14g a day is known to be safe for the long run, but the studies of higher doses were too short to say, so come "
           "back down once it's over. If you have an active inflammatory bowel disease (IBD), like Crohn's or colitis, don't "
           "count on it. In the two small trials in active Crohn's, it didn't help.")
P22_NEW = ("CAUTION: a lot of cancers feed on glutamine too, to fuel their growth. So if you have an active cancer, check with "
           "your oncologist before you take the 5g, and especially before you go up to the 10-30g. Your enterocytes take in a "
           "lot of the glutamine you swallow as soon as it reaches them, but not all of it, and the rest gets into your "
           "blood, where a cancer can get to it. They can only take in so much at a time, so the bigger the dose, the more of "
           "it gets into your blood.")

C = []


def ch(start, old, new, kind, why):
    C.append({'start': start, 'old': old, 'new': new, 'kind': kind, 'why': why})


# his batch-9 answers
ch('L-Glutamine (watch', None, P20_HIS, 'his',
   'F9-1, his own version (revise): "converted into" for "turned straight into", and the two sentences joined; with F9-2\'s '
   'clause, approved')
ch('Take 5g a day as a baseline.', None, P21_NEW, 'card',
   'F9-3 approved, with "incorporate your research to make this more accurate and useful"; F9-5 his answers: away from '
   'meals, an acute exposure to toxins or pathogens, raise it by a gram a day. The research changes are card F10-1')
ch('CAUTION: cancer cells that multiply', None, P22_NEW, 'payoff',
   'F9-4 approved; its instruction moved up to follow the warning, the issue he always fixes (payoff too late)')
# terms, at first use
ch('Previously, I made some posts', "on the AMD article on DMSO for gut health.",
   "on A Midwestern Doctor's article on the solvent DMSO for gut health.", 'term', 'AMD and DMSO, said where they first appear')
ch('Keep in mind that gut health', 'can cement the stress coming from those other vectors.',
   'can cement the stress coming from those other vectors. And by stress I mean every kind, physical or mental, from an '
   'injury to toxins and pathogens.', 'term',
   'his F9-5 answer: "stress refers to everything ... we can explain that once at first where we mention stress"')
ch('This is likely caused by diverticulosis', 'herniated pockets to form', 'herniated pockets (called diverticula) to form',
   'term', 'diverticula, named where the pockets first appear')
ch('This is likely caused by diverticulosis', 'Butyrate is the fuel for the colon cells.',
   'Butyrate, a fatty acid your gut bacteria make, is the fuel for the colon cells.', 'term', 'butyrate, at its first use')
ch('This is likely caused by diverticulosis', 'I would also suggest diosmin for',
   'I would also suggest diosmin, a compound from citrus fruits, for', 'term', 'diosmin')
ch("However, while we don't know if Pooyan", 'some bread with A1 dairy.',
   'some bread with A1 dairy, the regular cow\'s milk that has the A1 type of casein protein.', 'term', 'A1 dairy')
ch('CAUTION: If you have severe diverticulosis', 'Make sure you get cleared by a gastroenterologist first.',
   'Make sure you get cleared first by a gastroenterologist, a doctor who specializes in the gut.', 'term',
   'gastroenterologist, at its first use')
ch('Poor diet now (Phase 2)', '(especially visceral fat)', '(especially the visceral fat around your organs)', 'term',
   'visceral fat')
ch('Parasites, H. pylori, mold, metals', 'Parasites, H. pylori, mold, metals',
   'Parasites, the stomach bacteria H. pylori, mold, metals', 'term', 'H. pylori, at its first use')
ch('Parasites, H. pylori, mold, metals', "it's easily treated with berberine.",
   "it's easily treated with berberine, an extract from plants like barberry.", 'term', 'berberine, at its first use')
ch('Plant foods (Phases 2 and 5)', 'they cannot handle fiber, oxalates, and phytates in plants.',
   'they cannot handle the fiber in plants, or the oxalates and phytates, compounds in many plants that bind minerals.',
   'term', 'oxalates and phytates')
ch('Leaky gut (Phase 5)', "such as Crohn's Disease or IBS,", "such as Crohn's Disease or irritable bowel syndrome (IBS),",
   'term', 'IBS, at its first use')
# Try 2 of the leaky-gut items (stretch C, 2026-11-05): try 1 explained zonulin, colostrum and BPC-157 in sentences after
# their first use, and split "signal ... to open" with the tight-junctions note; those read Human Medium, AI-Generated
# Medium and Human Low. His usual fix (gate E368): each term explained where it is first used (his join for zonulin), and
# the point of each sentence first.
ch('Leaky gut (Phase 5)', "It's associated with increased zonulin levels clinically. Zonulin is the molecule released to "
   "signal your intestinal tight junctions to open.",
   "It's associated clinically with increased levels of zonulin, the molecule released to open your intestinal tight "
   "junctions, the seals between the cells of your gut lining.", 'term',
   'zonulin and tight junctions, each explained at its first use: his two sentences joined, so zonulin is explained where '
   'it is named, and what it does (open them) comes before what tight junctions are')
ch('Liposomal first-milking colostrum', 'Liposomal first-milking colostrum (esp.',
   'Liposomal first-milking colostrum, the first milk a cow makes after giving birth, wrapped in tiny fat bubbles that '
   'help you absorb it (esp.', 'term', 'colostrum and liposomal, at their first use')
ch('Liposomal first-milking colostrum', 'with bifidobacterium, or', 'with bifidobacterium, a common probiotic, or', 'term',
   'bifidobacterium')
ch('Liposomal first-milking colostrum', 'to mop up mycotoxins in the gut.',
   'to mop up mycotoxins, the toxins molds make, in the gut.', 'term', 'mycotoxins, at their first use')
ch('A good BPC-157 supplement,', 'A [good BPC-157 supplement,](http://barrier.co) like this one from Barrier, can also help.',
   'BPC-157 is a lab-made short protein based on one in stomach juice, and a [good BPC-157 supplement,](http://barrier.co) '
   'like this one from Barrier, can also help.', 'term', 'BPC-157, at its first use')
ch('Beta-glucans, in yeast extract.', 'Beta-glucans, in yeast extract.', 'Beta-glucans, a kind of fiber found in yeast extract.',
   'term', 'beta-glucans')
ch('Resistant starch to feed', ') to feed the good bacteria in your gut.',
   ') to feed the good bacteria in your gut, since your body can\'t digest it.', 'term',
   'resistant starch: his point first, then why it reaches the bacteria')
ch('Ozonated zeolite (or', '(http://zeolitelabs.com/proof)): I find', '(http://zeolitelabs.com/proof)), a volcanic mineral '
   'full of tiny pores: I find', 'term', 'zeolite')
ch('The colonocytes lining your large intestine are fueled',
   'The colonocytes lining your large intestine are fueled by short-chain fatty acids (SCFAs) like butyrate, while your '
   'small intestine runs on glutamine.', 'Your colonocytes are fueled by short-chain fatty acids (SCFAs) like butyrate.',
   'repeat', 'colonocytes were introduced in the fuels paragraph, and the glutamine point is said twice above it')
ch('IBS (Phase 4)', 'A [functional medicine](http://ifm.org) gastroenterologist might help.',
   'A gastroenterologist who practices [functional medicine](http://ifm.org), which looks for the root causes of illness, '
   'might help.', 'term', 'functional medicine')
ch('NOTE: this gut gem', '(apart from my H2O2 swap in Phase 3)', '(apart from my swap to H2O2, hydrogen peroxide, in Phase 3)',
   'term', 'H2O2, at its first use')
ch("Now let's have a look at your bile function", 'or phosphatidylcholine, before',
   'or phosphatidylcholine, a fatty nutrient found in egg yolks and soy, before', 'term', 'phosphatidylcholine')
# Phase 2 (stretch H) read AI Detected 65% alone, and its opening AI-Generated High in his post (#142): his usual fix,
# the point first (what this phase does, then whose it is, as Phases 1, 3 and 5 open) and "no harsh chemicals"
# uncompressed; FODMAP explained by what both diets do, joined to his "Either way" so it doesn't split his "go A or B".
ch('This is Dr. Michael Ruscio', 'This is Dr. Michael Ruscio (Healthy Gut, Healthy You) and Dr. Mark Pimentel (The '
   'Microbiome Connection): calm the inflammation down and starve the overgrowths, no harsh chemicals.',
   "Once the mechanics work, calm the inflammation down and starve the overgrowths, without any harsh chemicals. This one's "
   "from Dr. Michael Ruscio (Healthy Gut, Healthy You) and Dr. Mark Pimentel (The Microbiome Connection).", 'window',
   'his opening read AI: the point first, then the sources, as Phases 1, 3 and 5 open (card)')
ch('Diet-wise, go Paleo-Low FODMAP', 'Either way you stop feeding the bacteria in your small intestine.',
   'Either way you stop feeding the bacteria in your small intestine, since both cut out the carbs they ferment most '
   'easily.', 'term', 'FODMAP, by what both diets do, joined to his "Either way"')
ch("If diet didn't clear your symptoms", 'you likely have an active overgrowth (SIBO/SIFO).',
   'you likely have an active overgrowth of bacteria or fungi in your small intestine (SIBO or SIFO).', 'term', 'SIFO')
ch('H2O2 actually works better', 'according to me and orthomolecular drs.',
   'according to me and orthomolecular drs, who treat illness with high doses of nutrients.', 'term', 'orthomolecular')
ch('So check your organs (Brown).', 'Is it Exocrine Pancreatic Insufficiency?',
   "Is it Exocrine Pancreatic Insufficiency, where your pancreas doesn't make enough digestive enzymes?", 'term',
   'exocrine pancreatic insufficiency')
ch('My notes: see "Leaky gut" above for colostrum', 'BPC-157, ozonated zeolite and the fuels, and',
   'BPC-157 and ozonated zeolite, and', 'repeat', 'the fuels are pointed to in step 4, just above')
ch('You\'ll also find "gut cleanse" stacks',
   "berberine for H. pylori, the stomach bacteria that's usually behind heartburn you only get on an empty stomach: take",
   'berberine for H. pylori: take', 'repeat', 'H. pylori is introduced, and its heartburn sign given, under Parasites')
ch('Some severe symptoms warrant', 'not red like from lower GI)', 'not red like from the lower digestive tract)', 'term',
   'GI, said in plain words like the upper tract before it')

bl = sr.blocks(R12)
text = R12
lines = R12.split('\n')
out = []
MD_START = {'L-Glutamine (watch': 'L-Glutamine ([watch', 'Take 5g a day as a baseline.': 'Take 5g a day as a baseline.',
            'CAUTION: cancer cells that multiply': 'CAUTION: cancer cells that multiply'}
for c in C:
    i = [x['i'] for x in bl if x['text'].startswith(c['start'])]
    assert len(i) == 1, (c['start'], i)
    old = c['old']
    if old is None:   # the whole paragraph: its Markdown line, without the bullet
        ln = [l for l in lines if l.lstrip().startswith('- ' + MD_START[c['start']])]
        assert len(ln) == 1, c['start']
        old = ln[0].lstrip()[2:]
    assert text.count(old) == 1, ('not once in the article', old[:70])
    text = text.replace(old, c['new'])
    out.append(dict(c, block=i[0], old=old))
(HERE / 'r15.md').write_text(text, encoding='utf-8')
(HERE / 'CHANGES.json').write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding='utf-8')
print(len(out), 'changes;', len(text.split()), 'words')
