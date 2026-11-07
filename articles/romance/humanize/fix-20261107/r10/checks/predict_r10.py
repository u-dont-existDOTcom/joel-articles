#!/usr/bin/env python3
"""r10's predictions, written before the checks: the paragraphs of two sections by themselves (E343)."""
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[5]
LEDGER = ROOT / 'articles' / 'romance' / 'humanize' / 'pangram-ledger.jsonl'
REL = 'articles/romance/humanize/fix-20261107/r10/checks/'
DET = 'pangram 4.1, the web app (Joel\'s account, GUI credits)'
P = {
    'r10-dam175': dict(lineage='romance-low-dam-p175', call='Human', chance=0.6,
                       tells='a short question by itself', human='his "Based on what?", "the new certainty"',
                       diag='In the section (#51) this paragraph read Human High and Human Medium with its two Sometimes '
                            'sentences joined; his extension had read three Human Low windows here, the short pieces alone.',
                       first='payoff: unchanged; join: the two Sometimes sentences with "and", the last clause with "so"; plain: his words',
                       hum='his short sentences joined the way he joins his own'),
    'r10-dam176': dict(lineage='romance-low-dam-p176', call='Human', chance=0.5,
                       tells='a list of three wants after "So"', human='"a common-law marriage without discussing it", his want list',
                       diag='His want list and its Otherwise reason read Human Low twice in the live post; joined with "because '
                            'otherwise" they read AI Medium (#51). S10 read Human High in its section once his reason came '
                            'before his answer (#44).',
                       first='payoff: the risk comes first, then what he wants because of it; join: "So" ties the list to it; '
                             'plain: his words, the Otherwise frame dropped',
                       hum='his reason moved ahead of his list, the way S10 turned (the problem first, then his answer)'),
    'r10-s22a': dict(lineage='romance-s22-p437', call='AI', chance=0.45,
                     tells='a three-part "how much, to who, how publicly"', human='his first two sentences; "to who", "really"',
                     diag='In the section (#50) the noun list said with verbs read Human Medium, and the triad said one item at '
                          'a time read AI Medium; the live triad read AI Medium too.',
                     first='payoff: unchanged; join: "So" ties the triad to the truth before it; plain: "to who", "really"',
                     hum='the triad said the way he talks, with "and" between its parts and "really" before "depends"'),
    'r10-s22b': dict(lineage='romance-s22-p438', call='AI', chance=0.4,
                     tells='a joined advice sentence with a purpose clause', human='"a cartoon villain in your head"',
                     diag='In the section (#50) "Once you’re out, you can see ..." and the look-at sentence read AI High as one '
                          '52-word window; the live "A breakup can expose things ..." read AI High alone.',
                     first='payoff: what starts to show comes first; join: none; plain: "a cartoon villain in your head" for '
                           '"one-dimensionalizing them"',
                     hum='the seeing said as what starts to show, and the jargon at the end said the way he talks'),
    'r10-s22c': dict(lineage='romance-s22-p439', call='AI', chance=0.4,
                     tells='a single instruction then an and-joined helpers sentence', human='"Even the curiosity itself can be therapeutic"',
                     diag='In the section (#50) the denial said as a feeling read AI Medium and the advice joined to its reason '
                          'with "because" AI High; the live balanced pair of don\'ts read AI High.',
                     first='payoff: the easy story and why it tempts come first; join: the helpers joined with "and"; plain: '
                           '"simplest" for "parsimonious", one instruction for the pair of don\'ts',
                     hum='the pair of don\'ts said as one instruction, and the helpers said without a because-reason'),
}
for key, p in P.items():
    if sys.argv[1:] and key not in sys.argv[1:]:
        continue
    cmd = [sys.executable, str(ROOT / 'tools' / 'humanization' / 'pangram_ledger.py'), 'predict', str(LEDGER),
           '--lineage', p['lineage'], '--scope', 'paragraph', '--text', REL + 'CHECK-%s.txt' % key, '--call', p['call'],
           '--chance', str(p['chance']), '--tells', p['tells'], '--human-tells', p['human'], '--diagnosis', p['diag'],
           '--decides', 'whether the paragraph reads Human by itself', '--key', key, '--batch', 'romance-r10',
           '--detector', DET, '--receipt', REL + 'RECEIPT-%s.json' % key, '--first-fix', p['first'], '--humanized', p['hum']]
    r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    print(key, r.returncode, (r.stdout + r.stderr).strip()[:400])
