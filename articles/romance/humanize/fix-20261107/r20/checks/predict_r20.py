#!/usr/bin/env python3
"""r20's predictions, written before the checks; each text was linted first (gate bad-trips-2026-11-07h)."""
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[5]
LEDGER = ROOT / 'articles' / 'romance' / 'humanize' / 'pangram-ledger.jsonl'
REL = 'articles/romance/humanize/fix-20261107/r20/checks/'
DET = 'pangram 4.1, the web app (Joel\'s account, GUI credits)'
P = {
    'r20-spir304': dict(lineage='romance-sec-spiritual-sex-p304', scope='stretch', call='Human', chance=0.55,
                        tells='"Marriage, sex, and household life are not automatically on the opposite side" (his), a '
                              'quoted sutta line',
                        human='"Who isn’t a stream-enterer these days?", "510 lay stream-enterers", "almost comic"',
                        diag='The section with S17’s best try read 14.8% AI (#45): AI Low on 304’s two denials ("don’t '
                             'teach ...", "But they also don’t show ..."), and Human Low on 305’s closing gloss with 306’s '
                             'short opener. This try says 304 as one sentence with its second half as what is so (the '
                             'linter’s X1), names the stages of awakening in the sentence that lists them (E369), and '
                             'joins 306’s opener with a colon.',
                        first='payoff: what the texts show (lay people awakened) said as what is so; join: 304’s two '
                              'sentences with but, 305’s gloss as an appositive, 306’s opener with a colon; plain: "have '
                              'nothing on tantric sex" for "don’t teach tantric sex"',
                        hum='his denials said as what the texts do show, his short lines joined', extra=[]),
    'r20-spir312': dict(lineage='romance-sec-spiritual-sex-p312', scope='pair', call='Human', chance=0.6,
                        tells='"a lasting universal-consciousness awakening"',
                        human='"as my friend Cody says", "Yin/Yang", "Twin Flames (TFs)"',
                        diag='In #45, 312’s opener "Brad and Pam Keene are the example I really like." read AI Low (10 '
                             'words) by itself and the story after it Human Low (34). This try says the paragraph’s point '
                             'first ("whose marriage itself became part of the path") and joins the story with and; 313 '
                             'goes with it unchanged, since 312 alone is under the web app’s 50 words.',
                        first='payoff: the marriage as part of the path said first; join: the story’s two sentences with '
                              'and; plain: his words',
                        hum='his point said first, his story joined', extra=[]),
}
for key, p in P.items():
    if sys.argv[1:] and key not in sys.argv[1:]:
        continue
    cmd = [sys.executable, str(ROOT / 'tools' / 'humanization' / 'pangram_ledger.py'), 'predict', str(LEDGER),
           '--lineage', p['lineage'], '--scope', p['scope'], '--text', REL + 'CHECK-%s.txt' % key, '--call', p['call'],
           '--chance', str(p['chance']), '--tells', p['tells'], '--human-tells', p['human'], '--diagnosis', p['diag'],
           '--decides', 'whether the %s reads Human with no Low window' % p['scope'], '--key', key, '--batch', 'romance-r20',
           '--detector', DET, '--receipt', REL + 'RECEIPT-%s.json' % key, '--first-fix', p['first'], '--humanized', p['hum']] \
          + p['extra']
    r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    print(key, r.returncode, (r.stdout + r.stderr).strip()[:700])
