#!/usr/bin/env python3
"""r16's predictions, written before the checks; each text was linted first (gate bad-trips-2026-11-07h)."""
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[5]
LEDGER = ROOT / 'articles' / 'romance' / 'humanize' / 'pangram-ledger.jsonl'
REL = 'articles/romance/humanize/fix-20261107/r16/checks/'
DET = 'pangram 4.1, the web app (Joel\'s account, GUI credits)'
PANEL = 'articles/romance/humanize/fix-20261107/r14/panel-sit34/PANEL.md'
P = {
    'r16-ideal147': dict(lineage='romance-low-ideal-p147', scope='pair', call='Human', chance=0.5,
                         tells='"proof that the person was fake all along", a quoted "You’re perfect"',
                         human='"I’m already running", "I use it almost diagnostically in my own life"',
                         diag='In #92 my join of 148’s splitting sentences read AI Low (32 words) and his "“I can’t find any '
                              'flaw,” I’m already running." AI Low (10 words); in the live post 148’s two sentences read Human '
                              'Low. This try gives 148 back his two sentences, with "splitting" said in plain words where it is '
                              'first used (his fix 2), and 147 as the live post has it.',
                         first='payoff: what splitting is, said where it first appears; join: none, his two sentences kept; '
                               'plain: "flips from seeing you as all good to seeing you as all bad" for the bare "splitting"',
                         hum='his two sentences back, with the term explained where it is first used', extra=[]),
    'r16-jeal': dict(lineage='romance-low-jeal', scope='section', call='Human', chance=0.55,
                     tells='a balanced verdict on polyamory, "A foundational, permanent, exclusive"',
                     human='"The inner Magic 8 Ball came back YES", "about 99% of the time", "I learned most of this by '
                     'screwing it up"',
                     diag='#83 read 16% AI on 367 to 370, his unchanged sentences among them. Narrowed (#89, #90): 367 with '
                          'its problem said first and 368 with people as the ones who promise read Human High, and so did 369 '
                          'with its point first and its closing reason before its verdict, with 370’s short sentence joined. '
                          'This try puts both pairs back with the first ten paragraphs.',
                     first='payoff: 367’s problem and 369’s point said first; join: 367’s two sentences with so, 369’s closing '
                           'pair with so, 370’s sentences with and and so; plain: "People promise ..." for "... is promised"',
                     hum='the pairs as they read High by themselves',
                     extra=['--narrowed', 'romance-low-jeal-p367 (#89, Human High) and romance-low-jeal-p369 (#90, Human '
                                          'High)']),
    'r16-sit34': dict(lineage='romance-low-sit-p34', scope='paragraph', call='Human', chance=0.5,
                      tells='"the fun without (most of) the responsibility", "the existential void"',
                      human='"Doomscrolling entertains you too.", "partly because she’s the one risking pregnancy"',
                      diag='Five readings below High (#59, #65, #72, #85, #86). The bad trips lessons f and g (his own tries '
                           'of 2026-11-07): a claim left a little unbalanced read Human where the balanced one read AI ("true '
                           '(or false)"). This try leaves the fun line unbalanced ("without (most of) the responsibility") '
                           'and says the pregnancy sentence shorter and apart from the void, after the linter read the joined '
                           'one as a list of three.',
                      first='payoff: what stays (pregnancy, attachment) said in its own short sentence; join: none, the long '
                            'sentence split; plain: "whatever they call it" for "whether or not anybody named the relationship"',
                      hum='the fun line left a little unbalanced, the way his own fix was',
                      extra=['--panel', PANEL]),
    'r16-slow': dict(lineage='romance-low-slow', scope='section', call='Human', chance=0.55,
                     tells='a balanced can/can’t pair', human='"Let’s just be friends!", "the bodies just don’t connect"',
                     diag='#87 read Human with one Low window (47 words) on the list’s last two pairs and 182’s first sentence. '
                          'This fix joins 182’s two sentences with but, what may get better and when it doesn’t, so the '
                          'list’s window can’t end on a sentence by itself.',
                     first='payoff: unchanged, his order; join: 182’s two sentences with but; plain: his words',
                     hum='his two short sentences joined with but',
                     extra=['--after-fix', '182’s two sentences joined with but, for the Low window in #87 on the list and '
                                           '182’s first sentence']),
    'r16-deeper': dict(lineage='romance-low-deeper', scope='section', call='Human', chance=0.55,
                       tells='a general contrast ("is different from")', human='"in the forest than with any other man in a '
                       'mansion", Bee’s shoes, "You’re either going up, or going down."',
                       diag='#91 read Human with two Low windows: S5’s two closing sentences (34 words) and 73’s colon join (33 '
                            'words). This try joins S5’s closing pair with but, and gives 73 back his sentences, its general '
                            'contrast tied to his own knee from the paragraph before.',
                       first='payoff: his verdict "I agree" first, then what it rests on; join: S5’s closing pair with but; '
                             'plain: "a temporary incapacity, like my knee" for the bare "temporary incapacity"',
                       hum='his contrast tied to his own story, and S5’s closing pair joined', extra=[]),
    'r16-romance': dict(lineage='romance-low-romance', scope='section', call='Human', chance=0.5,
                        tells='"doesn’t make a strong woman helpless", a list of what she may worry about',
                        human='"Bee once called me her “wife.”", "a war you got drafted into", "Unfortunately, I’ve seen a lot of '
                        'the latter."',
                        diag='Three Human Low windows here in the live post: 285’s "She should not have to perform softness '
                             '...", 286’s "Then she can over-correct ..." and 287’s "A man receiving care doesn’t make him a '
                             'child either." This try joins 285’s short opener to it with a colon, says 286’s second half with '
                             'receiving care as its subject, and says 287’s line as what is so ("a man who receives care is '
                             'still a grown man", the linter’s X1), joined to the sentence before; S15 is in as it read (#31).',
                        first='payoff: what is true for her too comes first; join: 285’s opener with a colon, 287’s two lines '
                              'with and; plain: "is still a grown man" for "doesn’t make him a child"',
                        hum='his short lines joined and his denial said as what is so', extra=[]),
    'r16-fantasy': dict(lineage='romance-low-fantasy', scope='section', call='Human', chance=0.55,
                        tells='"enable extreme masculine-feminine polarity", a contrast with "rather than"',
                        human='"turn the polarity dial all the way to the right", "an extraordinary act of trust"',
                        diag='Two Human Low windows here in the live post, both in 294: "They are private until the person '
                             'decides to share them." and "When somebody does share one, ...". This try joins them with and; '
                             'S16 is in as it read (#23).',
                        first='payoff: unchanged, his order; join: 294’s two short sentences with and; plain: his words',
                        hum='his two short sentences joined with and', extra=[]),
}
for key, p in P.items():
    if sys.argv[1:] and key not in sys.argv[1:]:
        continue
    cmd = [sys.executable, str(ROOT / 'tools' / 'humanization' / 'pangram_ledger.py'), 'predict', str(LEDGER),
           '--lineage', p['lineage'], '--scope', p['scope'], '--text', REL + 'CHECK-%s.txt' % key, '--call', p['call'],
           '--chance', str(p['chance']), '--tells', p['tells'], '--human-tells', p['human'], '--diagnosis', p['diag'],
           '--decides', 'whether the %s reads Human with no Low window' % p['scope'], '--key', key, '--batch', 'romance-r16',
           '--detector', DET, '--receipt', REL + 'RECEIPT-%s.json' % key, '--first-fix', p['first'], '--humanized', p['hum']] \
          + p['extra']
    r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    print(key, r.returncode, (r.stdout + r.stderr).strip()[:700])
