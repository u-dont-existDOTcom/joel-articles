#!/usr/bin/env python3
"""r28's predictions, written before the checks (2026-11-08); each text linted first (gate bad-trips-2026-11-07h)."""
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[5]
LEDGER = ROOT / 'articles' / 'romance' / 'humanize' / 'pangram-ledger.jsonl'
REL = 'articles/romance/humanize/fix-20261107/r28/checks/'
DET = "pangram 4.1, the web app (Joel's account, GUI credits)"
WHOLE = 'his whole-article check of 16:47 UTC (r27/checks/RESULTS-whole-r27.json)'
P = {
    'r28-labels': ('romance-low-labels', 'AI Low on 38 ("Here’s the funny thing ... which matters a lot")',
                   'payoff: the scene first ("call someone your boyfriend or girlfriend for years"); join: one sentence; '
                   'plain: "one foot out the door", "matters a lot" cut', '38'),
    'r28-deeper': ('romance-low-deeper', 'Low on 72\'s last sentence ("I get why ... wanted my knee to be fine")',
                   'payoff: "I get it" first; join: none, one sentence; plain: "brushing me off" for "felt dismissive"',
                   '72'),
    'r28-bundling': ('romance-s6', 'Low on 103\'s first two sentences (the 30 to 40 percent)',
                     'payoff: the failure first; join: the two sentences with a colon; plain: "late-1700s", "didn’t keep '
                     '... from having sex" for "keep courtship nonsexual"', '103'),
    'r28-ptsd': ('romance-low-ptsd', 'Low on 157\'s opener ("That dynamic alone isn’t necessarily the main problem")',
                 'payoff: what happened first; join: none; plain: "that part can be fine" for the negated "isn’t '
                 'necessarily the main problem"', '157'),
    'r28-dam': ('romance-low-dam', 'Low on 175\'s last sentence', 'payoff: "about her" names what he learned; join: '
                'none; plain: "less likely to question it" for "harder for me to question"', '175'),
    'r28-slow': ('romance-low-slow', 'Low on 181\'s two list sentences', 'payoff: each sentence names a thing; join: the '
                 'list taken apart into two of two; plain: "smell turns you off", "every day ... once a month", "click"',
                 '181'),
    'r28-slow-b': ('romance-low-slow', 'Low on 181; then #149 read AI Medium on my list sentences and Low on the opener',
                   'payoff: the opener and its examples in one sentence; join: the three sentences into one; plain: two '
                   'particular items (his cut to two, #112), the needed read\'s cut of the third sentence, a slack ending '
                   'tied to the opener', '181'),
    'r28-pillars': ('romance-pillars-330-336', 'Low on 331\'s opener and on 334\'s "There isn’t one perfect arrangement."',
                    'payoff: "Here’s how this looks for me" with what happens; join: 334\'s last two sentences with '
                    '"so"; plain: "run to our own friends" for "turn to our separate circles of friends"', '331, 334'),
}
for key, (lineage, low, first, paras) in P.items():
    if sys.argv[1:] and key not in sys.argv[1:]:
        continue
    cmd = [sys.executable, str(ROOT / 'tools' / 'humanization' / 'pangram_ledger.py'), 'predict', str(LEDGER),
           '--lineage', lineage, '--scope', 'stretch' if key == 'r28-pillars' else 'section',
           '--text', REL + 'CHECK-%s.txt' % key, '--call', 'Human', '--chance', '0.55',
           '--tells', 'mine in ' + paras + ', reworked after ' + WHOLE,
           '--human-tells', 'the live post\'s stories and jokes around it',
           '--diagnosis', WHOLE + ' read ' + low + '; its section check had read Human with no Low, so the whole read '
           'split its windows differently. Said his way (point first, particular words, joined), it should read High in '
           'any split.',
           '--decides', 'whether the window his whole check read AI or Low reads Human at Medium or High',
           '--key', key, '--batch', 'romance-r28', '--detector', DET,
           '--receipt', REL + 'RECEIPT-%s.json' % key,
           '--after-fix', paras + ' reworked after ' + WHOLE,
           '--first-fix', first,
           '--humanized', 'his moves (romance-2026-11-08b, c): particular things for abstract ones, a casual register, '
                          'no announcing opener']
    r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    print(key, r.returncode, (r.stdout + r.stderr).strip()[:700])
