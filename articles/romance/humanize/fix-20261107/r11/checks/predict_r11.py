#!/usr/bin/env python3
"""r11's predictions, written before the checks."""
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[5]
LEDGER = ROOT / 'articles' / 'romance' / 'humanize' / 'pangram-ledger.jsonl'
REL = 'articles/romance/humanize/fix-20261107/r11/checks/'
DET = 'pangram 4.1, the web app (Joel\'s account, GUI credits)'
P = {
    'r11-dam': dict(lineage='romance-low-dam', scope='section', call='Human', chance=0.7,
                    tells='the want list after So', human='"Based on what?", "a damn shame", his run of questions',
                    diag='Try 1 (#51) read 23% AI: the want list fastened to its reason with because-otherwise read AI Medium '
                         'and the common-law sentence Human Low. Narrowed (#52, #53): with his reason said first as its own '
                         'sentence and the list after it with So, paragraph 176 read Human High by itself, as did 175 with its '
                         'Sometimes join. This try puts both back with his last two paragraphs; better is no AI and no Low window.',
                    first='payoff: 176’s reason said before its list; join: 175’s Sometimes sentences with and and so; plain: his '
                          'words throughout',
                    hum='his paragraphs as they read Human High by themselves, with his last two',
                    extra=['--narrowed', 'romance-low-dam-p175 (#52, Human High) and romance-low-dam-p176 (#53, Human High), '
                                         'each checked by itself']),
    'r11-s22b': dict(lineage='romance-s22-p438', scope='paragraph', call='AI', chance=0.4,
                     tells='a general claim about seeing, advice to the reader in the imperative',
                     human='"a cartoon villain", "bonded", "including the conflicts they were carrying inside themselves"',
                     diag='The both-sides sentence ("Look at ..., but also try to understand ..., including ..., so/rather than '
                          '...") read AI High wherever it sat: the live post (S22), the section (#50) and by itself (#55), and '
                          'the opener read AI Medium alone (#55). It covers every side in one balanced advice sentence. This try '
                          'says it in the shape of his own advice in paragraph 440, which read Human High in #50: one short '
                          'instruction per act, the last joined with ", and don’t ...".',
                     first='payoff: what you can see once you are out comes first; join: the last act joined with ", and '
                           'don’t" as he joins his; plain: "a cartoon villain" for "one-dimensionalizing them"',
                     hum='the advice said in the shape of his own advice two paragraphs on', extra=[]),
    'r11-sit': dict(lineage='romance-low-sit', scope='section', call='Human', chance=0.55,
                    tells='"the existential void", an X-without-the-Y line',
                    human='"basically the point", "Doomscrolling entertains you too", "BFFs", "drainingly superficial"',
                    diag='His extension read three Human Low windows here (LOW-WINDOWS.json): the void sentence with its dash '
                         'aside, the undefined pair with its staged "What they don’t escape is ...", and his two short '
                         'sentences closing the H. story. The fixes: the dash made a comma, the pair joined with but and the '
                         'staged sentence said plainly with either, and the two short sentences joined.',
                    first='payoff: his order kept, nothing staged before its point; join: the undefined pair with but, his '
                          'two short H. sentences with a comma; plain: "They don’t escape ... either" for "What they don’t '
                          'escape is"',
                    hum='his short sentences joined and the staged sentence said plainly, the dash a comma', extra=[]),
    'r11-clar': dict(lineage='romance-low-clar', scope='section', call='Human', chance=0.5,
                     tells='two balanced if-sentences, a dash pair around the chemicals',
                     human='"the modern degen dating scene", "etc.", "freaked out"',
                     diag='Two Human Low windows here: his short "It comes from reading I’ve done as well." after "isn’t just '
                          'from my own experience", and the oxytocin paragraph’s two if-sentences, where the point (more '
                          'attached and more freaked out at once) came last. The fixes: the two short sentences made one, and '
                          'the point moved up into the paragraph’s first sentence, the if-sentences after it.',
                     first='payoff: the oxytocin paragraph’s point in its first sentence; join: "isn’t just from my own '
                           'experience. It comes from reading" made one sentence; plain: his words, the dash pair kept',
                     hum='his short sentences joined and the paragraph’s point said first', extra=[]),
    'r11-flaws': dict(lineage='romance-low-flaws', scope='section', call='Human', chance=0.6,
                      tells='a run of short "I’m" sentences',
                      human='"astrology predicts I will by 2030 😃", "FAWNING", "No, I really didn’t."',
                      diag='Two short Human Low windows open his list: "My own list isn’t especially flattering." and '
                           '"I’m impulsive." The fix joins them with a colon and joins "I’m impulsive" to the next item, the '
                           'way he joins his own short sentences.',
                      first='payoff: the list still opens the section; join: the opener and "I’m impulsive" joined to the '
                            'next item; plain: his words',
                      hum='his short opening sentences joined the way he joins his own', extra=[]),
}
for key, p in P.items():
    if sys.argv[1:] and key not in sys.argv[1:]:
        continue
    cmd = [sys.executable, str(ROOT / 'tools' / 'humanization' / 'pangram_ledger.py'), 'predict', str(LEDGER),
           '--lineage', p['lineage'], '--scope', p['scope'], '--text', REL + 'CHECK-%s.txt' % key, '--call', p['call'],
           '--chance', str(p['chance']), '--tells', p['tells'], '--human-tells', p['human'], '--diagnosis', p['diag'],
           '--decides', 'whether the %s reads Human with no Low window' % p['scope'], '--key', key, '--batch', 'romance-r11',
           '--detector', DET, '--receipt', REL + 'RECEIPT-%s.json' % key, '--first-fix', p['first'], '--humanized', p['hum']] \
          + p['extra']
    r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    print(key, r.returncode, (r.stdout + r.stderr).strip()[:600])
