#!/usr/bin/env python3
"""predict.py - turn 55's predictions (pangram_ledger.py predict), written before each check.

  python3 predict.py [KEY...]
"""
import pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[3]
L = 'articles/bad-trips/humanize/pangram-ledger.jsonl'
REL = 'articles/bad-trips/humanize/h63-20261120/'
DET = "Pangram web app (his account), in the desktop app's browser pane"
BATCH = 'h63a'

P = {
    'd3-ozone-2': dict(
        lineage='bad-trips Aged Ozonated-Charcoal Water ozone story: B197, by itself as the guide has it (h62)',
        scope='paragraph', call='AI', chance=0.4,
        tells=['It intensified the experience and became mentally alarming.'],
        human_tells=["so if one doesn't help, try the other"],
        diagnosis=('the near miss c3-ozone-1 (4cf06939) read Human Medium 17, Human Low 21, Human Low 6 and AI Low 15 over '
                   'its last line, "The mistake suggested that DMSO and aged ozonated-charcoal water address different '
                   'kinds of overload.", which all three fresh reads marked: a summing-up the reader can do nothing with. '
                   'This try changes only that line (17% of the near miss\'s words, lesson 19b): it ends on what to do, '
                   'joined with "so", and "address" is said as "work on". Better: the last window Human; the two Human Low '
                   'windows over the story\'s middle are the next tries if they stay Low'),
        decides=('whether the ozone story reads Human High in every window by itself: if so it goes into the guide in place '
                 'of B197 (apply_gate.py); if not, the windows say which line the next small try changes'),
        flag=('--receipt', REL + 'TEST-d3-ozone-2.receipt.json'),
        humanized=('the last sentence ends on what the reader does with the point, joined to it with "so"; "address" said '
                   'as the plain "work on"; one change from the near miss (4cf06939), 17% of its words'),
        first_fix=('payoff: the last sentence now ends on what the reader does with it ("so if one doesn\'t help, try the '
                   'other"), the use the three reads found missing; join: the use joined to the point it follows from, '
                   'with "so"; plain: "address" said as "work on"')),
}


P['e3-ozone-3'] = dict(P['d3-ozone-2'], call='Human', chance=0.75,
    tells=['The mistake suggested that DMSO and the water work on different kinds of overload'],
    diagnosis=('d3 (7794e2d9) read Human Written: Human High 44 over the first four sentences, Human Medium 25 over the last '
               'line. This try changes only that line\'s "aged ozonated-charcoal water" to "the water", since the line '
               'before has just named it (3% of d3\'s words). Better: the last window High'),
    humanized=('the long name the line before has just used said as "the water", the way a person refers back; one change '
               'from the near miss (7794e2d9), 3% of its words'),
    first_fix=('payoff: the last line already ends on what the reader does ("so if one doesn\'t help, try the other"); '
               'join: none, the line was joined with "so" in d3; plain: "aged ozonated-charcoal water" said as "the water" '
               'right after the line that names it'),
    flag=('--receipt', REL + 'TEST-e3-ozone-3.receipt.json'))


P['f3-ozone-4'] = dict(P['d3-ozone-2'], call='Human', chance=0.8,
    tells=['The mistake suggested that DMSO and aged ozonated-charcoal water work on different kinds of overload'],
    human_tells=["so if DMSO doesn't help, try the water, and the other way around"],
    diagnosis=('d3 (7794e2d9), the best: Human High 44 over the first four sentences, Human Medium 25 over the last line; '
               'e3\'s "the water" for the long name made that line Human Low (71fcaf75), so the long name stays. This try '
               'names the remedies in the advice: "if DMSO doesn\'t help, try the water, and the other way around" (10% '
               'of d3\'s words). Better: the last window High'),
    humanized=('the advice at the end names which to try first and the way back ("if DMSO doesn\'t help, try the water, '
               'and the other way around"), the concrete words a person uses; one change from the near miss (7794e2d9)'),
    first_fix=('payoff: the last line already ends on what the reader does, now with the remedies named; join: none, the '
               'line was joined with "so" in d3; plain: "one" and "the other" said as "DMSO" and "the water"'),
    flag=('--receipt', REL + 'TEST-f3-ozone-4.receipt.json'))


def run(key):
    p = P[key]
    a = ['python3', 'tools/humanization/pangram_ledger.py', 'predict', L, '--lineage', p['lineage'], '--scope', p['scope'],
         '--text', REL + 'TEST-%s.txt' % key, '--key', key, '--batch', BATCH, '--call', p['call'], '--chance',
         str(p['chance']), '--detector', DET, '--decides', p['decides'], '--diagnosis', p['diagnosis'], p['flag'][0],
         p['flag'][1]]
    for t in p.get('tells', []):
        a += ['--tells', t]
    for t in p.get('human_tells', []):
        a += ['--human-tells', t]
    if p.get('humanized'):
        a += ['--humanized', p['humanized']]
    if p.get('first_fix'):
        a += ['--first-fix', p['first_fix']]
    r = subprocess.run(a, cwd=REPO, capture_output=True, text=True)
    out = (r.stdout + r.stderr).strip()
    print(key, '|', out[:1500] if r.returncode else out.splitlines()[-1][:220])
    return r.returncode


if __name__ == '__main__':
    sys.exit(max([run(k) for k in (sys.argv[1:] or list(P))] or [0]))
