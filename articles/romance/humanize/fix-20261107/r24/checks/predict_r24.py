#!/usr/bin/env python3
"""r24's predictions, written before the checks; each text was linted first (gate bad-trips-2026-11-07h)."""
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[5]
LEDGER = ROOT / 'articles' / 'romance' / 'humanize' / 'pangram-ledger.jsonl'
REL = 'articles/romance/humanize/fix-20261107/r24/checks/'
DET = 'pangram 4.1, the web app (Joel\'s account, GUI credits)'
P = {
    'r24-jeal366': dict(
        lineage='romance-low-jeal-p366', scope='stretch', call='Human', chance=0.55,
        tells='"Lots of couples promise forever and nobody else." (a short claim)',
        human='"say “she’s cute” about a woman at the next table", "Look around at how many actually live that way.", '
              '"dates four at once and calls it polyamory", "I learned most of this by screwing it up."',
        diag='r21’s stretch (#119) read 95%% AI from idiom stacking. Narrowed: r22’s 367 read Human (Medium, Low; #124); '
             'r23’s 368 with 369 read Human (Medium, High, Medium; #127) and 369 alone Human, High (#128), after the '
             'reasons were told as what people do. This puts those three between the live 366 and 370.',
        extra=['--receipt', REL + 'RECEIPT-r24-jeal366.json',
               '--narrowed', 'romance-low-jeal-p367b#124, romance-low-jeal-p368#127 and romance-low-jeal-p369b#128 (all '
               'Human)',
               '--big-change', 'the change is the three narrowed paragraphs, each checked by itself; 366 and 370 are '
               'unchanged',
               '--first-fix', 'payoff: what he would rather and what people do, first (r22, r23); join: 369’s opener '
               'with its first example (r23); plain: "crushes", "dates four at once", "an affair" (r22, r23)',
               '--humanized', 'r22’s 367 and r23’s 368 and 369 in the stretch']),
    'r24-ideal': dict(
        lineage='romance-low-ideal', scope='section', call='Human', chance=0.6,
        tells='"It shouldn’t have to happen that way, though." (read Human Low), 147’s disclaimer (read Human Low)',
        human='"I’m not Superman out here trying to “save a hoe.”", "I’m Lord Krishna.", "I’m already running"',
        diag='r23 (#130) read 4.9%% AI: the AI windows were 151’s last two short sentences, untouched live text; 147 and '
             '148 read Human. This joins 151’s two short sentences with but and keeps the rest.',
        extra=['--receipt', REL + 'RECEIPT-r24-ideal.json',
               '--after-fix', '151’s "Maybe I do talk about them too much sometimes. But they still matter to me." joined '
               'with but, and "that isn’t on mine" made "they aren’t on mine"; nothing else changed since #130',
               '--first-fix', 'payoff: his answer first, as it was; join: 151’s two short sentences with but; plain: '
               '"they aren’t" for the "that" the join would misdirect',
               '--humanized', 'his join move (SKILL.md fix 3) on 151: its two short sentences joined with but, the pronoun made plain']),
}
for key, p in P.items():
    if sys.argv[1:] and key not in sys.argv[1:]:
        continue
    cmd = [sys.executable, str(ROOT / 'tools' / 'humanization' / 'pangram_ledger.py'), 'predict', str(LEDGER),
           '--lineage', p['lineage'], '--scope', p['scope'], '--text', REL + 'CHECK-%s.txt' % key, '--call', p['call'],
           '--chance', str(p['chance']), '--tells', p['tells'], '--human-tells', p['human'], '--diagnosis', p['diag'].replace('%%', '%'),
           '--decides', 'whether the %s reads Human with no Low window' % p['scope'], '--key', key, '--batch', 'romance-r24',
           '--detector', DET] + p['extra']
    r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    print(key, r.returncode, (r.stdout + r.stderr).strip()[:900])
