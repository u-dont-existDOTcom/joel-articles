#!/usr/bin/env python3
"""r19's predictions, written before the checks; each text was linted first (gate bad-trips-2026-11-07h)."""
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[5]
LEDGER = ROOT / 'articles' / 'romance' / 'humanize' / 'pangram-ledger.jsonl'
REL = 'articles/romance/humanize/fix-20261107/r19/checks/'
DET = 'pangram 4.1, the web app (Joel\'s account, GUI credits)'
P = {
    'r19-nitty201': dict(lineage='romance-low-nitty-p201', scope='paragraph', call='Human', chance=0.55,
                         tells='a list of what he is expected to do ("mind-read, check in constantly, notice every '
                               'emotional shift")',
                         human='"10% autistic", "all that expert “management”", "a bit of an introvert"',
                         diag='The section read AI (#108, 33%) on one window, 201’s closing sentence, unchanged from the '
                              'live post: four parallel items of what he is expected to do, then a "without ...ing" tail '
                              '(E186). This try gives the items different shapes (the silence in brackets under the '
                              'shift’s verb, E125’s fix from his Borrowed Adulthood paragraph) and says the tail as the '
                              'last item, what he must never do.',
                         first='payoff: unchanged, his order; join: the silence under the shift’s verb, in brackets; '
                               'plain: "and never use all that expert management to manipulate anyone" for "without '
                               'manipulating based on all that expert management"',
                         hum='his list given different shapes, his tail said as what he must never do', extra=[]),
    'r19-nitty201b': dict(lineage='romance-low-nitty-p201', scope='paragraph', call='Human', chance=0.5,
                          tells='"without manipulating based on all that expert “management.”" (his tail, kept)',
                          human='"10% autistic", "mind-read, silences included", "a bit of an introvert"',
                          diag='#111 read the closing sentence Human Low (up from AI Low in #108) with the list given '
                               'different shapes and the tail made its last item; it still read as a list of what he is '
                               'expected to do. This try cuts the list to two items: noticing every emotional shift is '
                               'what mind-reading means there (E125: drop the item that matters least), and the silence '
                               'goes in with the mind-reading ("silences included"); his tail is back as he wrote it, so '
                               'only the list changes.',
                          first='payoff: unchanged, his order; join: the silence into the mind-reading ("silences '
                                'included"); plain: his words, the overlapping item cut',
                          hum='his list cut to what it needs, his tail as he wrote it', extra=[]),
    'r19-nitty': dict(lineage='romance-low-nitty', scope='section', call='Human', chance=0.6,
                      tells='"which is a lot of emotional weight for a bed"',
                      human='"10% autistic", "mind-read, silences included", "I can make my bed whenever I want"',
                      diag='The first try (#108) read 33% AI on one window, 201’s closing list; the bed paragraph read '
                           'High with S9’s line said inside it. Narrowed: 201 by itself read Human Low with the list '
                           're-shaped (#111) and Human High with it cut to two items (#112). This last try puts that 201 '
                           'back with the bed paragraph as #108 read it.',
                      first='payoff: unchanged, his order; join: S9’s line inside the bed paragraph, the silence inside '
                            'the mind-reading; plain: his words, the overlapping item cut',
                      hum='the paragraphs as they read High', extra=['--narrowed', 'romance-low-nitty-p201 (#111 Human '
                                                                     'Low, #112 Human High)']),
    'r19-nitty2': dict(lineage='romance-low-nitty', scope='section', call='Human', chance=0.55,
                       tells='"which is a lot of emotional weight for a bed"',
                       human='"(no manipulating with all that expert “management,” though)", "10% autistic", "mind-read, '
                             'silences included"',
                       diag='The last try (#113) read Human with one Low window, 201’s closing sentence (33 words), which '
                            'read High by itself (#112). In the section it is the closing line, and it ends on his '
                            '"without manipulating based on ..." tail (E186). This check after the fix (his answer 28a) '
                            'says the tail as an aside in brackets.',
                       first='payoff: unchanged, his order; join: the tail into an aside in brackets; plain: "no '
                             'manipulating with all that expert management, though" for "without manipulating based on '
                             'all that expert management"',
                       hum='his tail said as an aside',
                       extra=['--after-fix', '201’s closing tail said as an aside, for the Low window on it in #113']),
}
for key, p in P.items():
    if sys.argv[1:] and key not in sys.argv[1:]:
        continue
    cmd = [sys.executable, str(ROOT / 'tools' / 'humanization' / 'pangram_ledger.py'), 'predict', str(LEDGER),
           '--lineage', p['lineage'], '--scope', p['scope'], '--text', REL + 'CHECK-%s.txt' % key, '--call', p['call'],
           '--chance', str(p['chance']), '--tells', p['tells'], '--human-tells', p['human'], '--diagnosis', p['diag'],
           '--decides', 'whether the %s reads Human with no Low window' % p['scope'], '--key', key, '--batch', 'romance-r19',
           '--detector', DET, '--receipt', REL + 'RECEIPT-%s.json' % key, '--first-fix', p['first'], '--humanized', p['hum']] \
          + p['extra']
    r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    print(key, r.returncode, (r.stdout + r.stderr).strip()[:700])
