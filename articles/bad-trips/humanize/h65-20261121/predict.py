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




# Turn 58 (h65c): single steps of the second try, cut out of its pairs to find which read AI (1-2 read Human Written,
# 8ad45936, his last line Human Medium; 3-4, 5-6 and 7-8 AI High in one window each).
BATCH3 = 'h65c'
D3 = ('the second try\'s pairs: steps 1-2 Human High 109 and Human Medium 14 over his own last line (8ad45936); 3-4 AI High '
      '122 (5d3a5e91), 5-6 AI High 121 (fc3db895), 7-8 AI High 118 (b6d8abee), each one window over everything, so they '
      'don\'t say which step reads AI. This check is one step by itself, as it stands in the second try. ')
P3 = {
    'g3a-ss1-1': ('step 1 by itself', 'Human', 0.6, ['Stop all suspected serotonergic substances'], ['even DXM cough syrup'],
                  D3 + 'Step 1 was in the Human High window of its pair. Better: Human High alone, so it can go in'),
    'g3d-ss4-1': ('step 4 by itself', 'AI', 0.3, ['Put a fan on them, with cool damp cloths on their skin.'],
                  ["If you think of giving a fever reducer"], D3 + 'Better: a Human window, to start the next try from'),
    'g3e-ss5-1': ('step 5 by itself', 'AI', 0.35, ['Keep the room calm and keep them still:'],
                  ["They're already overstimulated, so keep crowds and arguments away."], D3 + 'Better: a Human window'),
    'g3h-ss8-1': ('step 8 by itself', 'AI', 0.4, ['Leave out DMSO too, which this guide uses for other emergencies'],
                  ["While you wait, don't reach for niacin to end the trip"], D3 + 'Better: a Human window'),
}


def run3(key):
    name, call, chance, tells, human, diag = P3[key]
    a = ['python3', 'tools/humanization/pangram_ledger.py', 'predict', L, '--lineage',
         LINEAGE.replace('steps: B136,', '%s: B136,' % name).replace('Syndrome steps', 'Syndrome'), '--scope', 'paragraph',
         '--text', REL + 'TEST-%s.txt' % key, '--key', key, '--batch', BATCH3, '--call', call, '--chance', str(chance),
         '--detector', DET, '--decides', DECIDES, '--diagnosis', diag, '--receipt', REL + 'TEST-%s.receipt.json' % key,
         '--humanized', HUMANIZED2, '--first-fix', FIRST_FIX2]
    for t in tells:
        a += ['--tells', t]
    for t in human:
        a += ['--human-tells', t]
    r = subprocess.run(a, cwd=REPO, capture_output=True, text=True)
    out = (r.stdout + r.stderr).strip()
    print(key, '|', out[:1500] if r.returncode else out.splitlines()[-1][:220])
    return r.returncode




# Turn 58 (h65d): the third try at steps 5 and 6, in his first person.
BIG4 = ('every second-person try of mine read AI, step 1 by itself included (49c25418, AI High 65), while his own first-'
        'person step 2 read Human High by itself (cc5e6563) and carried its pair to Human (8ad45936): no Human window of '
        'mine to start a small change from, so this try changes the register to his "I\'d" and "I wouldn\'t" where a step '
        'says what to do')


def run4(key='g4c-ss56-4'):
    a = ['python3', 'tools/humanization/pangram_ledger.py', 'predict', L, '--lineage',
         LINEAGE.replace('steps: B136,', 'steps 5 and 6: B136,'), '--scope', 'paragraph', '--text', REL + 'TEST-%s.txt' % key,
         '--key', key, '--batch', 'h65d', '--call', 'Human', '--chance', '0.55', '--detector', DET, '--decides', DECIDES,
         '--diagnosis', ('steps 5 and 6 read AI High 133 (25df9e03) and 121 (fc3db895), and step 5 by itself AI High 69 '
                         '(d85068d3); his first-person step 2 is the only text in these steps that reads Human. This try '
                         'puts steps 5 and 6 in his first person, with the three reads\' marks fixed and then the tell '
                         'panel\'s five agreed sentences (panel-g4c/PANEL.md); read again, the panel agreed on six of seven '
                         '(panel-g4c-2/PANEL.md), now on the steps\' own conditions and terms, which every wording of them '
                         'has. Better: a Human window'),
         '--receipt', REL + 'TEST-%s.receipt.json' % key, '--big-change', BIG4,
         '--humanized', ('steps 5 and 6 in his first person ("I\'d keep crowds and arguments away", "I wouldn\'t force '
                         'anything on them"), the register of his step 2; "fully alert" said; holding still said as talking '
                         'them into it, not holding them down; the fluids\' other case opened with "But if"'),
         '--first-fix', ('payoff: what he would do first in each sentence, the reason after it; join: "so", "also", '
                         '"anyway", "But if", "The same goes"; plain: "fully alert" said as following what you say and '
                         'swallowing easily, "help them keep still" said as talking them into it without holding them down'),
         '--panel', REL + 'panel-g4c/PANEL.md',
         '--tells', "They're already overstimulated, so I'd clear out the crowd and stop any arguing.",
         '--human-tells', "I'd stay with them and talk them into keeping still anyway"]
    r = subprocess.run(a, cwd=REPO, capture_output=True, text=True)
    out = (r.stdout + r.stderr).strip()
    print(key, '|', out[:1500] if r.returncode else out.splitlines()[-1][:220])
    return r.returncode


if __name__ == '__main__':
    ks = sys.argv[1:] or list(P)
    sys.exit(max([(run4(k) if k == 'g4c-ss56-4' else run3(k) if k in P3 else run2(k) if k in P2 else run(k)) for k in ks] or [0]))
