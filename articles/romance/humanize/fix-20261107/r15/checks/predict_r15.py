#!/usr/bin/env python3
"""r15's predictions, written before the checks."""
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[5]
LEDGER = ROOT / 'articles' / 'romance' / 'humanize' / 'pangram-ledger.jsonl'
REL = 'articles/romance/humanize/fix-20261107/r15/checks/'
DET = 'pangram 4.1, the web app (Joel\'s account, GUI credits)'
P = {
    'r15-sit': dict(lineage='romance-low-sit', scope='section', call='Human', chance=0.55,
                    tells='"the fun without the responsibility", a definition',
                    human='"basically the point", "Doomscrolling entertains you too.", "BFFs", "drainingly superficial"',
                    diag='#59 read 31% AI. Narrowed: paragraph 33 with his list joined to the void sentence read Human High '
                         'by itself (#64); paragraph 34 read Low three times (#65, #72, #85), the last with the tell panel’s '
                         'agreed tells fixed and only its end Low. This try puts them back with his 35 and 36; better is no '
                         'AI window and no Low outside paragraph 34.',
                    first='payoff: his order kept; join: 33’s list joined to the void sentence, 34’s claims as in #85; '
                          'plain: his words',
                    hum='the paragraphs as they read by themselves, his story after them',
                    extra=['--narrowed', 'romance-low-sit-p33 (#64, Human High) and romance-low-sit-p34 (#65, #72, #85, '
                                         'Human Low each time; the tell panel’s agreed tells fixed in #85)']),
    'r15-slow': dict(lineage='romance-low-slow', scope='section', call='Human', chance=0.65,
                     tells='a balanced can/can’t pair', human='"Let’s just be friends!", "the bodies just don’t connect"',
                     diag='#74 read 34% AI on his five-part list once its first paragraph was joined. Narrowed (#76): the '
                          'list said a pair at a time read Human High with paragraph 182. This try puts it back with the '
                          'joined first paragraph (High in #74) and his last two paragraphs.',
                     first='payoff: what going slowly shows first; join: his first paragraph with but, the list a pair at a '
                           'time; plain: his words',
                     hum='his list said a pair at a time and his first paragraph joined',
                     extra=['--narrowed', 'romance-low-slow-p181 (#76, Human High, with 182)']),
    'r15-disc': dict(lineage='romance-low-disc', scope='section', call='Human', chance=0.5,
                     tells='a list of three things to put first', human='"it can’t see what it can’t see", "My breathing gets shallow"',
                     diag='#75 read Human with four Low windows by itself, three on sentences the whole post read at Medium '
                          'or High. Narrowed (#77 to #80): 220 with its recommendation said directly, 221 with its mind-and-'
                          'body pair joined, 223 and 224 each read Human High or Medium. This try puts them back together.',
                     first='payoff: his recommendation and what happens in his body said first; join: the pairs and short '
                           'sentences joined as in #77 to #80; plain: "I recommend" for "That’s why I recommend"',
                     hum='the paragraphs as they read by themselves',
                     extra=['--narrowed', 'romance-low-disc-p220 (#77), romance-low-disc-p221 (#78), romance-low-disc-p223 '
                                          '(#79), romance-low-disc-p224 (#80), each Human High or Medium']),
    'r15-jeal367': dict(lineage='romance-low-jeal-p367', scope='pair', call='Human', chance=0.5,
                        tells='a triad of adjectives, a general mechanism', human='"including the low-stakes ones"',
                        diag='In #83 "If only the serious attractions ..." read AI Medium and 368 Human Low, with 367’s first '
                             'sentence Low. This try says 367’s problem first and its answer after with so (his reason-then-'
                             'act pattern, as the dam’s did in #70), and makes people the ones who promise in 368.',
                        first='payoff: the problem first, then what he would rather do; join: 367’s two sentences with so; '
                              'plain: "People promise ..." for "... is promised"',
                        hum='his reason said before his answer, and people as the ones who promise', extra=[]),
    'r15-jeal369': dict(lineage='romance-low-jeal-p369', scope='pair', call='Human', chance=0.5,
                        tells='"a way to ..., or a way to ...", a closing verdict',
                        human='"I learned most of this by screwing it up"',
                        diag='In #83 369 read AI Medium and AI High (its closing joined to the sentence before with and) and '
                             '370’s short first sentence Low. This try drops the staged "That’s not to say", says the closing '
                             'reason before its conclusion with so, and joins 370’s short sentence.',
                        first='payoff: "Polyamory isn’t automatically better" first, and the damage before the verdict; join: '
                              'the closing pair with so, 370’s sentences with and and so; plain: his words',
                        hum='his point said first and his reason before his verdict', extra=[]),
    'r15-deeper': dict(lineage='romance-low-deeper', scope='section', call='Human', chance=0.6,
                       tells='a general contrast ("is different from")', human='"in the forest than with any other man in a '
                       'mansion", Bee’s shoes, "You’re either going up, or going down."',
                       diag='One Human Low window here in the live post: 73’s "Helping carry somebody through temporary '
                            'incapacity is different from becoming the permanent support system ...". This try joins it to '
                            '"I agree" with a colon, the verdict he gives it, and puts S4 (#4) and S5 (#5) in as they read.',
                       first='payoff: his verdict first, then what it rests on; join: the general contrast joined to "I '
                             'agree" with a colon; plain: his words',
                       hum='his general sentence joined to the verdict it explains', extra=[]),
    'r15-ideal': dict(lineage='romance-low-ideal', scope='section', call='Human', chance=0.55,
                      tells='"That’s why it’s so easy to get confused", a run of short quoted lines',
                      human='"save a hoe", "lost in the sauce", "I’m Lord Krishna.", "Sure."',
                      diag='Two Human Low windows here in the live post, both in 148: "When the BPD splitting happens, '
                           'private hatred can replace worship." and "Then come public accusations ...". This try joins them '
                           'with "and then", and puts S8 in as it read in #18.',
                      first='payoff: what splitting does first, then what comes after; join: the two splitting sentences '
                            'with "and then"; plain: his words',
                      hum='his two short splitting sentences joined', extra=[]),
}
for key, p in P.items():
    if sys.argv[1:] and key not in sys.argv[1:]:
        continue
    cmd = [sys.executable, str(ROOT / 'tools' / 'humanization' / 'pangram_ledger.py'), 'predict', str(LEDGER),
           '--lineage', p['lineage'], '--scope', p['scope'], '--text', REL + 'CHECK-%s.txt' % key, '--call', p['call'],
           '--chance', str(p['chance']), '--tells', p['tells'], '--human-tells', p['human'], '--diagnosis', p['diag'],
           '--decides', 'whether the %s reads Human with no Low window' % p['scope'], '--key', key, '--batch', 'romance-r15',
           '--detector', DET, '--receipt', REL + 'RECEIPT-%s.json' % key, '--first-fix', p['first'], '--humanized', p['hum']] \
          + p['extra']
    r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    print(key, r.returncode, (r.stdout + r.stderr).strip()[:700])
