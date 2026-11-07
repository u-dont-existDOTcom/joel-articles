#!/usr/bin/env python3
"""r23's predictions, written before the checks; each text was linted first (gate bad-trips-2026-11-07h)."""
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[5]
LEDGER = ROOT / 'articles' / 'romance' / 'humanize' / 'pangram-ledger.jsonl'
REL = 'articles/romance/humanize/fix-20261107/r23/checks/'
DET = 'pangram 4.1, the web app (Joel\'s account, GUI credits)'
P = {
    'r23-jeal367': dict(
        lineage='romance-low-jeal-p367b', scope='paragraph', call='Human', chance=0.6,
        tells='a long joined sentence', human='"say “she’s cute” about a woman at the next table", "some guy"',
        diag='r22’s 367 read Human: Medium on its first sentence, Low on its second (#124). This try joins the second to '
             'the first as its reason (because), as he joins a reason to its claim.',
        extra=['--receipt', REL + 'RECEIPT-r23-jeal367.json',
               '--big-change', 'only the Low second sentence changes, joined to the first as its reason; the first is '
               'r22’s word for word',
               '--first-fix', 'payoff: his preference first; join: the Low sentence as its reason with because; plain: '
               '"every crush you do mention" for "every mention"',
               '--humanized', 'romance-2026-11-07c (a reason joined to its claim)']),
    'r23-jeal368': dict(
        lineage='romance-low-jeal-p368', scope='pair', call='Human', chance=0.5,
        tells='"Lots of couples promise forever and nobody else." (a short claim)',
        human='"Look around at how many actually live that way.", "dates four at once and calls it polyamory", "keeps '
              'cheating until they finally announce they’re poly", "who gets to stay the night"',
        diag='r22 (#125) read 100%% AI: the essay shape, a claim with two abstract reasons joined by or and a verdict. '
             'This try tells each reason as what some people do (dates four at once and calls it polyamory; keeps '
             'cheating until they announce they’re poly), the way his S2 told the monks’ reasons, and turns 368’s '
             'finished claim into something the reader can look at.',
        extra=['--receipt', REL + 'RECEIPT-r23-jeal368.json',
               '--big-change', 'the named cause of #125 (the essay shape) is in 369’s every sentence and 368’s first; '
               'telling each reason as a person doing something changes most words',
               '--first-fix', 'payoff: what people do, first; join: the opener with its first example by like when; '
               'plain: "dates four at once", "keeps cheating", "an affair"',
               '--humanized', 'romance-2026-11-07a and d: the reasons told as people, as his S2 told the monks’']),
    'r23-jeal369': dict(
        lineage='romance-low-jeal-p369b', scope='paragraph', call='Human', chance=0.55,
        tells='"without necessarily doing the work on themselves that would make it ethical"',
        human='"dates four at once and calls it polyamory", "keeps cheating until they finally announce they’re poly"',
        diag='r22 (#126) read AI Medium alone, from the essay shape. This try tells each reason as what someone does.',
        extra=['--receipt', REL + 'RECEIPT-r23-jeal369.json',
               '--big-change', 'the named cause of #126 (the essay shape) is in every sentence; telling each reason as a '
               'person doing something changes most words',
               '--first-fix', 'payoff: polyamory can be dishonest, with its first example in the same sentence; join: '
               'like when; plain: "dates four at once", "keeps cheating"',
               '--humanized', 'romance-2026-11-07a and d on 369']),
    'r23-ideal': dict(
        lineage='romance-low-ideal', scope='section', call='Human', chance=0.65,
        tells='"Idealization can be pathological, but it can also come very close to real deep love" (a balanced opener)',
        human='"I’m not Superman out here trying to “save a hoe.”", "I’m Lord Krishna.", "I’m already running", "first in '
              'private and then in front of everybody"',
        diag='Try 1 (#92) read 9.6%% AI: AI Low on 147’s quote end and 148. r22’s 147 and 148 read Human, High and '
             'Medium, as a pair (#123). This puts them in #92’s text, nothing else changed.',
        extra=['--receipt', REL + 'RECEIPT-r23-ideal.json',
               '--narrowed', 'romance-low-ideal-p147#123 (Human, High and Medium)',
               '--first-fix', 'payoff: she goes from worshipping to hating, said first (r22); join: his quote as one '
               'sentence, private and public in one (r22); plain: verbs for "worship" and "hatred", "evidence" for '
               '"proof" (r22)',
               '--humanized', 'r22’s 147 and 148 in the section']),
}
for key, p in P.items():
    if sys.argv[1:] and key not in sys.argv[1:]:
        continue
    cmd = [sys.executable, str(ROOT / 'tools' / 'humanization' / 'pangram_ledger.py'), 'predict', str(LEDGER),
           '--lineage', p['lineage'], '--scope', p['scope'], '--text', REL + 'CHECK-%s.txt' % key, '--call', p['call'],
           '--chance', str(p['chance']), '--tells', p['tells'], '--human-tells', p['human'], '--diagnosis', p['diag'].replace('%%', '%'),
           '--decides', 'whether the %s reads Human with no Low window' % p['scope'], '--key', key, '--batch', 'romance-r23',
           '--detector', DET] + p['extra']
    r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    print(key, r.returncode, (r.stdout + r.stderr).strip()[:900])
