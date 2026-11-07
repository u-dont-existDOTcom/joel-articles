#!/usr/bin/env python3
"""r26's prediction, written before the checks; each text was linted first (gate bad-trips-2026-11-07h)."""
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[5]
LEDGER = ROOT / 'articles' / 'romance' / 'humanize' / 'pangram-ledger.jsonl'
REL = 'articles/romance/humanize/fix-20261107/r26/checks/'
DET = 'pangram 4.1, the web app (Joel\'s account, GUI credits)'
P = {
    'r26-jeal': dict(
        lineage='romance-low-jeal', scope='section', call='Human', chance=0.5,
        tells='"Lots of couples promise forever and nobody else" (a broad claim), "without necessarily doing the work on '
              'themselves"',
        human='the Magic 8 Ball and switch story, the quoted line to a partner, "like saying “she’s cute” about a woman at '
              'the next table", "just renames it polyamory", "I learned most of this by screwing it up."',
        diag='#133 read 26%% AI though each paragraph read Human alone. A fresh sense read of the live 367 to 369 found '
             'the links between them missing (no alternative to "I would rather", a missing step, a jump to polyamory, a '
             'rebuttal of a claim nobody made, "admit" contradicting "dishonest"). That would explain why each passes '
             'alone and the three fail together. This try puts each link in words; nothing else changed.',
        extra=['--receipt', REL + 'RECEIPT-r26-jeal.json',
               '--after-fix', '367 to 369 with their links put in words after the sense read (SENSE-T2.md): 367 tied to '
                              '366 and its missing step said, 368’s pretending said for 369’s too, 369’s second case made '
                              'the dishonest one',
               '--first-fix', 'payoff: each paragraph opens on its tie to the one before; join: 368’s claim with its '
               'consequence (so a lot of them end up pretending); plain: "renames it", "say so up front", "an affair"',
               '--humanized', 'his link move (E355) on 367 to 369, after his S2 fixes']),
}
for key, p in P.items():
    if sys.argv[1:] and key not in sys.argv[1:]:
        continue
    cmd = [sys.executable, str(ROOT / 'tools' / 'humanization' / 'pangram_ledger.py'), 'predict', str(LEDGER),
           '--lineage', p['lineage'], '--scope', p['scope'], '--text', REL + 'CHECK-%s.txt' % key, '--call', p['call'],
           '--chance', str(p['chance']), '--tells', p['tells'], '--human-tells', p['human'], '--diagnosis', p['diag'].replace('%%', '%'),
           '--decides', 'whether the %s reads Human with no Low window' % p['scope'], '--key', key, '--batch', 'romance-r26',
           '--detector', DET] + p['extra']
    r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    print(key, r.returncode, (r.stdout + r.stderr).strip()[:900])
