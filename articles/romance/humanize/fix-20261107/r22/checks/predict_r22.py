#!/usr/bin/env python3
"""r22's predictions, written before the checks; each text was linted first (gate bad-trips-2026-11-07h)."""
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[5]
LEDGER = ROOT / 'articles' / 'romance' / 'humanize' / 'pangram-ledger.jsonl'
REL = 'articles/romance/humanize/fix-20261107/r22/checks/'
DET = 'pangram 4.1, the web app (Joel\'s account, GUI credits)'
P = {
    'r22-jeal366': dict(
        lineage='romance-low-jeal-p366', scope='stretch', call='Human', chance=0.5,
        tells='"Plenty of couples vow to be together forever with nobody else, and far fewer actually live that way." (a '
              'finished principle), "the inner work"',
        human='"say “she’s cute” about a woman at the next table", "who gets to stay the night", "say “I can’t help '
              'myself” out loud", "than an affair would have", "I learned most of this by screwing it up."',
        diag='r21 (#119) read 95%% AI from idiom stacking (a whole sit-down talk, one and only, pull it off, keep it in '
             'their pants, fake it), worse than the live words; his 366 went AI Low beside it. This try puts a '
             'particular scene or thing where each idiom was, brings back his plain words (pretending, negotiate, '
             'ethical), and gives the last line its reason with since, as his S2 did. If it still reads AI, the stretch '
             'goes to the section only after a cause I can name.',
        extra=['--receipt', REL + 'RECEIPT-r22-jeal366.json',
               '--big-change', 'the named cause of #119 (idiom stacking) is in every sentence of 367 to 369, so taking '
               'each idiom out changes most of their words; 366 and 370 are unchanged',
               '--first-fix', 'payoff: what he would rather, said as a scene, first; join: 369’s opener with its '
               'reason by a colon, the last line with since; plain: his words back (pretending, negotiate, ethical), '
               'idioms out',
               '--humanized', 'romance-2026-11-07a and c on 367 to 369, minus r21’s idioms']),
    'r22-ideal147': dict(
        lineage='romance-low-ideal-p147', scope='pair', call='Human', chance=0.55,
        tells='"She rewrites our whole history until every flaw of mine looks like evidence" (a summary verb)',
        human='"first in private and then in front of everybody", "I’m already running", his punchline',
        diag='r21 (#121) read 33.6%% AI: 148 AI Low as a general sequence (kicks in, then come the public accusations, '
             'rewrites our whole history); his quote cut at its full stop gave Medium and Low windows, and his '
             'punchline read Low after the AI window. The tell panel (two fresh readers) agreed on 147’s disclaimer, '
             'my rewriting sentence and the punchline’s mirror. This try: the flip said with verbs (worshipping me to '
             'hating me, first in private and then in front of everybody), a callback to his "I can’t find any flaw" '
             'for the rewriting, the punchline’s mirror loosened, the disclaimer reworded, his quote as one sentence. '
             'A second panel still names the closing reversal, which is his point.',
        extra=['--receipt', REL + 'RECEIPT-r22-ideal147.json',
               '--panel', 'articles/romance/humanize/fix-20261107/r22/panel-ideal147/PANEL.md',
               '--big-change', 'the tell panel agreed on three of 148’s four sentences and on 147’s disclaimer; fixing '
               'each changes most of 148’s words; 147 keeps all but its disclaimer’s wording and its quote’s full stop',
               '--first-fix', 'payoff: she goes from worshipping to hating, said first; join: private and public in one '
               'sentence, his quote as one sentence (a comma for its full stop); plain: verbs for "worship" and '
               '"hatred", his "When the BPD splitting happens" back',
               '--humanized', 'romance-2026-11-07a on 148, the panel’s agreed sentences fixed']),
    'r22-jeal367': dict(
        lineage='romance-low-jeal-p367b', scope='paragraph', call='Human', chance=0.6,
        tells='"If only the serious crushes get mentioned, every mention turns into a confession" (a tidy consequence)',
        human='"say “she’s cute” about a woman at the next table", "some guy", "without it turning into a fight"',
        diag='Narrowing r21’s stretch (#119, 95%% AI from idiom stacking): 367 by itself, the stock idioms out and a '
             'particular scene in.',
        extra=['--receipt', REL + 'RECEIPT-r22-jeal367.json',
               '--big-change', 'a new lineage for the narrowed paragraph; it differs from r21’s 367 by the named cause',
               '--first-fix', 'payoff: what he would rather, as a scene, first; join: the consequence with so; plain: '
               '"crushes", "a fight" for r21’s idioms',
               '--humanized', 'romance-2026-11-07a on 367, minus r21’s idioms']),
    'r22-jeal368': dict(
        lineage='romance-low-jeal-p368', scope='pair', call='Human', chance=0.55,
        tells='"Plenty of couples vow to be together forever with nobody else, and far fewer actually live that way." (a '
              'finished principle)',
        human='"who gets to stay the night", "say “I can’t help myself” out loud", "than an affair would have"',
        diag='Narrowing r21’s stretch (#119): 368 with 369, the paragraph that answers it (368 is under 50 words).',
        extra=['--receipt', REL + 'RECEIPT-r22-jeal368.json',
               '--first-fix', 'payoff: the promise and how few keep it, first; join: 369’s opener with its reason by a '
               'colon; plain: "vow", "negotiate", "an affair"',
               '--humanized', 'romance-2026-11-07a and c on 368 and 369, minus r21’s idioms']),
    'r22-jeal369': dict(
        lineage='romance-low-jeal-p369b', scope='paragraph', call='Human', chance=0.6,
        tells='"the inner work that would make the arrangement ethical"',
        human='"say “I can’t help myself” out loud", "since pretending sometimes does more damage than an affair would '
              'have"',
        diag='Narrowing r21’s stretch (#119): 369 by itself, with its reason given by since, as his S2 gave one.',
        extra=['--receipt', REL + 'RECEIPT-r22-jeal369.json',
               '--first-fix', 'payoff: polyamory can be dishonest too, first; join: the opener and its reasons by a '
               'colon, the last line with since; plain: "pretending", "ethical", "an affair"',
               '--humanized', 'romance-2026-11-07a and c on 369, minus r21’s idioms']),
    'r22-romance': dict(
        lineage='romance-low-romance', scope='section', call='Human', chance=0.7,
        tells='"Unfortunately, I’ve seen a lot of the latter." (a short close), the manufactured-crisis line',
        human='"Bee once called me her “wife.”", "play the damsel", "She’s choosing the ride.", "a party where you were '
              'invited or a war you got drafted into"',
        diag='Try 1 (#98) read 36.8%% AI on 285 to 287’s lists and parallels. r21’s 285 to 287 read Human by themselves '
             'with every window High or Medium (#120), with 284 and 288 around them. This puts them in #98’s text, '
             'nothing else changed.',
        extra=['--receipt', REL + 'RECEIPT-r22-romance.json',
               '--big-change', 'the change is r21’s 285 to 287, tested by themselves with their neighbours (#120, every '
               'window High or Medium); nothing else in #98’s text changes',
               '--narrowed', 'romance-low-romance-p284#120 (Human, every window High or Medium)',
               '--first-fix', 'payoff: r21’s (each sentence says what she does or feels first); join: r21’s; plain: '
               'r21’s ("play the damsel", "a handful", "lying back while he pleases her")',
               '--humanized', 'r21’s 285 to 287 in the section']),
}
for key, p in P.items():
    if sys.argv[1:] and key not in sys.argv[1:]:
        continue
    cmd = [sys.executable, str(ROOT / 'tools' / 'humanization' / 'pangram_ledger.py'), 'predict', str(LEDGER),
           '--lineage', p['lineage'], '--scope', p['scope'], '--text', REL + 'CHECK-%s.txt' % key, '--call', p['call'],
           '--chance', str(p['chance']), '--tells', p['tells'], '--human-tells', p['human'], '--diagnosis', p['diag'].replace('%%', '%'),
           '--decides', 'whether the %s reads Human with no Low window' % p['scope'], '--key', key, '--batch', 'romance-r22',
           '--detector', DET] + p['extra']
    r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    print(key, r.returncode, (r.stdout + r.stderr).strip()[:900])
