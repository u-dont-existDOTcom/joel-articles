#!/usr/bin/env python3
"""r25's prediction, written before the checks; each text was linted first (gate bad-trips-2026-11-07h)."""
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[5]
LEDGER = ROOT / 'articles' / 'romance' / 'humanize' / 'pangram-ledger.jsonl'
REL = 'articles/romance/humanize/fix-20261107/r25/checks/'
DET = 'pangram 4.1, the web app (Joel\'s account, GUI credits)'
P = {
    'r25-jeal': dict(
        lineage='romance-low-jeal', scope='section', call='AI', chance=0.4,
        tells='366 to 369 read AI as a stretch (#131) although each read Human alone',
        human='the Magic 8 Ball and switch story (357 to 361), the quoted line to a partner (364), "dates four at once and '
              'calls it polyamory", "I learned most of this by screwing it up."',
        diag='S2’s pattern: each new paragraph read Human by itself, the stretch read 94.8%% AI (#131). Inside the whole '
             'section, with his story before it, the argument may read differently, but #83 and #94 read AI there too, so '
             'I call AI.',
        extra=['--receipt', REL + 'RECEIPT-r25-jeal.json',
               '--after-fix', 'r22’s 367 and r23’s 368 and 369 in place of the live 367 to 369 (since #94: each '
                              'paragraph narrowed and read Human alone, #124, #127, #128)',
               '--first-fix', 'payoff: what he would rather and what people do, first (r22, r23); join: 369’s opener '
               'with its first example (r23); plain: "crushes", "dates four at once", "an affair" (r22, r23)',
               '--humanized', 'r22’s 367 and r23’s 368 and 369 in the section']),
}
for key, p in P.items():
    if sys.argv[1:] and key not in sys.argv[1:]:
        continue
    cmd = [sys.executable, str(ROOT / 'tools' / 'humanization' / 'pangram_ledger.py'), 'predict', str(LEDGER),
           '--lineage', p['lineage'], '--scope', p['scope'], '--text', REL + 'CHECK-%s.txt' % key, '--call', p['call'],
           '--chance', str(p['chance']), '--tells', p['tells'], '--human-tells', p['human'], '--diagnosis', p['diag'].replace('%%', '%'),
           '--decides', 'whether the %s reads Human with no Low window' % p['scope'], '--key', key, '--batch', 'romance-r25',
           '--detector', DET] + p['extra']
    r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    print(key, r.returncode, (r.stdout + r.stderr).strip()[:900])
