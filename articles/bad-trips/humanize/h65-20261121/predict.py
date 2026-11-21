#!/usr/bin/env python3
"""predict.py - turn 57's predictions (pangram_ledger.py predict) for the first try at the serotonin steps (B136), written
before each check: the whole list and its four pairs of steps, each a text of its own.

  python3 predict.py [KEY...]
"""
import pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[3]
L = 'articles/bad-trips/humanize/pangram-ledger.jsonl'
REL = 'articles/bad-trips/humanize/h65-20261121/'
DET = "Pangram web app (his account), in the desktop app's browser pane"
BATCH = 'h65a'
LINEAGE = ('bad-trips Suspected Serotonin Syndrome steps: B136, "Do this immediately when serotonin toxicity is reasonably '
           'suspected:" (h62 c1-ss-steps-1, as it stood)')
BEFORE = ('c1-ss-steps-1 (2d3e8386), the eight steps as they stood with his C1 answer a, read AI Generated, AI High 326 over '
          'the whole list, its first check by itself; its three reads (../h62-20261120/reads/) marked the drug list run '
          'together, the "not the treatment" and "do not solve" lines, the unexplained akathisia and rhabdomyolysis, the '
          'two lists of four in the fluids line, the ten things to write down in one run, and the hospital, DMSO and '
          'magnesium lines with nothing saying how they follow. ')
HUMANIZED = ('my sentences rewritten the his-fixes ways after a second set of three reads of my first draft: the drug list '
             'in three groups, each built differently and ending on cough syrup; each term explained where it is first '
             'used; the pronouns named; each step\'s reasons said with "since", "because", "so"; the lists split into '
             'clauses; the hospital line cut (the reader does nothing with it); his step 2 and his C1 opening as he has '
             'them')
FIRST_FIX = ('payoff: each step opens on what to do and each reason follows it; join: the short lines joined to the step they '
             'belong to (the ER lead with a colon, the fluids line with "and then"), and each sentence says how it follows '
             '("either", "counts too", "Then", "though", "That means", "It also", "instead"); plain: "serotonergic", '
             'akathisia and rhabdomyolysis said in plain words where first used, "an appropriate oral rehydration drink" '
             'named as oral rehydration salts, "this branch" said as "these steps"')
DECIDES = ('whether these steps go into the guide: each pair of steps has to read Human High in every window by itself '
           '(apply_gate.py), his step 2 aside; a pair that doesn\'t gets its next try from its windows, one change a check '
           'from a near miss (lesson 19b), up to ten tries while the latest is the best so far (20g)')

P = {
    'g1-ss-steps-2': dict(scope='section', call='AI', chance=0.35, lineage=LINEAGE,
        tells=['Stop every suspected serotonergic substance, meaning anything that raises serotonin.',
               "Gather what the ER will need: bring their pill bottles and packages, and write down exactly what they took."],
        human_tells=["Don't put them in a cool bath, though, if they're confused, seizing or very weak, since they could slip under the water."],
        diagnosis=BEFORE + 'This try is the whole list in my words beside his. Better: fewer AI windows than the one over '
                  'everything; the windows say which steps the next try works on'),
    'g1a-ss12-2': dict(scope='paragraph', call='AI', chance=0.45, lineage=LINEAGE.replace('steps: B136,', 'steps 1 and 2: B136,'),
        tells=["No more MDMA or stimulant redoses either, and none of the supplements 5-HTP, St John's wort or SAM-e."],
        human_tells=["If they're on an antidepressant (an SSRI, SNRI or MAOI), give them no more of it"],
        diagnosis=BEFORE + 'Steps 1 and 2 by themselves: my step 1 (the drug list in three groups) with his step 2, which '
                  'read Human High 58 alone. Better: step 1 Human; if it reads AI, the windows say which group'),
    'g1b-ss34-2': dict(scope='paragraph', call='AI', chance=0.4, lineage=LINEAGE.replace('steps: B136,', 'steps 3 and 4: B136,'),
        tells=["Then cool their skin with a fan and damp cloths, and put ice packs wrapped in cloth at their neck, armpits or groin."],
        human_tells=["If you're thinking of a fever reducer, it won't help here"],
        diagnosis=BEFORE + 'Steps 3 and 4 by themselves: the call with poison control named, and the cooling split into '
                  'its ways with the bath and the fever reducer said how they follow. Better: no AI window'),
    'g1c-ss56-2': dict(scope='paragraph', call='AI', chance=0.4, lineage=LINEAGE.replace('steps: B136,', 'steps 5 and 6: B136,'),
        tells=['That means no crowds or arguments around them, and no pacing or exercise to "burn it off."'],
        human_tells=['help them stay put anyway, because every bit of muscle work adds heat'],
        diagnosis=BEFORE + 'Steps 5 and 6 by themselves: keeping still with its reasons, akathisia and rhabdomyolysis '
                  'explained, and the fluids line with why not to give anything. Better: no AI window'),
    'g1d-ss78-2': dict(scope='paragraph', call='AI', chance=0.45, lineage=LINEAGE.replace('steps: B136,', 'steps 7 and 8: B136,'),
        tells=["For each substance, note the dose and when they took it, which dose was the last, and any dose they recently raised, then list any supplements or recreational drugs."],
        human_tells=["Niacin may be this guide's trip killer, but it is unsafe with serotonin syndrome"],
        diagnosis=BEFORE + 'Steps 7 and 8 by themselves: what to write down in two parts, and niacin, DMSO and magnesium '
                  'said as what to leave out and what to use instead. Better: no AI window'),
}


def run(key):
    p = P[key]
    a = ['python3', 'tools/humanization/pangram_ledger.py', 'predict', L, '--lineage', p['lineage'], '--scope', p['scope'],
         '--text', REL + 'TEST-%s.txt' % key, '--key', key, '--batch', BATCH, '--call', p['call'], '--chance',
         str(p['chance']), '--detector', DET, '--decides', DECIDES, '--diagnosis', p['diagnosis'], '--receipt',
         REL + 'TEST-%s.receipt.json' % key, '--humanized', HUMANIZED, '--first-fix', FIRST_FIX]
    for t in p.get('tells', []):
        a += ['--tells', t]
    for t in p.get('human_tells', []):
        a += ['--human-tells', t]
    r = subprocess.run(a, cwd=REPO, capture_output=True, text=True)
    out = (r.stdout + r.stderr).strip()
    print(key, '|', out[:1500] if r.returncode else out.splitlines()[-1][:220])
    return r.returncode




# The second try (h65b): the steps in the form of his Active Seizure list, written and read in turn 57; predicted and
# checked when the desktop app's browser pane is back (it went offline after the first try's checks).
BATCH2 = 'h65b'
BIG = ('the first try read AI in every window of every pair (AI High over each, AI Medium over two short stretches): no '
       'window was Human, so there is no near miss to change a word or two from (lesson 19b), and the same sentence-by-'
       'sentence rewriting would fail the same way; this try changes the form instead, to his Active Seizure list\'s, '
       'which read Human High 243 in place: a lead line and short items, one point each')
HUMANIZED2 = ('the steps that list things written as his Active Seizure list is: a lead line ending in a colon, then short '
              'items, one point each, built differently; the reasons kept only where the reader needs them; the fever '
              'reducers named; DMSO said as this guide\'s remedy for other emergencies; his step 2 and his C1 opening as he '
              'has them')
FIRST_FIX2 = ('payoff: each lead line says what to do, each item one thing to do or not; join: "so", "as well, once help is '
              'on the way", "The same goes", "too", "instead"; plain: the antidepressant line answers what to do when the '
              'kind is unknown, the fever reducers are named, "isn\'t one of these steps" said as what DMSO is and why not')
P2 = {k.replace('g1', 'g2').replace('-2', '-3'): dict(v, chance=min(v['chance'] + 0.05, 0.5),
      diagnosis=('the first try (h65a) read AI in every window: the whole AI High 535 (896a47c9), steps 1-2 AI High 133 '
                 '(3c421039), 3-4 AI Medium 10 and AI High 134 (494e52a9), 5-6 AI High 133 (25df9e03), 7-8 AI High 63 and '
                 'AI Medium 62 (59de60fe). The sentences each followed his fixes and still read AI as a list of explained '
                 'instructions; his Active Seizure list, short items under a lead line, read Human High. This try takes its '
                 'form. Better: a Human window in any pair'),
      tells=[], human_tells=[]) for k, v in P.items()}
P2['g2-ss-steps-3'].update(tells=['Stop all suspected serotonergic substances, meaning anything that raises serotonin, like:'],
                           human_tells=["even DXM cough syrup"])
P2['g2a-ss12-3'].update(tells=['tramadol for pain, or the antibiotic linezolid'], human_tells=["even DXM cough syrup"])
P2['g2b-ss34-3'].update(tells=['Put a fan on them, with cool damp cloths on their skin.'],
                        human_tells=["If you think of giving a fever reducer like acetaminophen or ibuprofen, it won't work"])
P2['g2c-ss56-3'].update(tells=['Give fluids only if they\'re fully alert and not vomiting, and then only small sips of an electrolyte drink.'],
                        human_tells=["They're already overstimulated, so keep crowds and arguments away."])
P2['g2d-ss78-3'].update(tells=['exactly what they took, how much of each, and when'],
                        human_tells=["While you wait, don't reach for niacin to end the trip"])


def run2(key):
    p = P2[key]
    a = ['python3', 'tools/humanization/pangram_ledger.py', 'predict', L, '--lineage', p['lineage'], '--scope', p['scope'],
         '--text', REL + 'TEST-%s.txt' % key, '--key', key, '--batch', BATCH2, '--call', p['call'], '--chance',
         str(p['chance']), '--detector', DET, '--decides', DECIDES, '--diagnosis', p['diagnosis'], '--receipt',
         REL + 'TEST-%s.receipt.json' % key, '--humanized', HUMANIZED2, '--first-fix', FIRST_FIX2, '--big-change', BIG]
    for t in p.get('tells', []):
        a += ['--tells', t]
    for t in p.get('human_tells', []):
        a += ['--human-tells', t]
    r = subprocess.run(a, cwd=REPO, capture_output=True, text=True)
    out = (r.stdout + r.stderr).strip()
    print(key, '|', out[:1500] if r.returncode else out.splitlines()[-1][:220])
    return r.returncode


if __name__ == '__main__':
    ks = sys.argv[1:] or list(P)
    sys.exit(max([(run2(k) if k in P2 else run(k)) for k in ks] or [0]))
