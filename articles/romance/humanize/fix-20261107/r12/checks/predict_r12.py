#!/usr/bin/env python3
"""r12's predictions, written before the checks."""
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[5]
LEDGER = ROOT / 'articles' / 'romance' / 'humanize' / 'pangram-ledger.jsonl'
REL = 'articles/romance/humanize/fix-20261107/r12/checks/'
DET = 'pangram 4.1, the web app (Joel\'s account, GUI credits)'
P = {
    'r12-s22': dict(lineage='romance-s22', scope='section', call='AI', chance=0.35,
                    tells='advice to the reader in the imperative, the seeing sentence',
                    human='"Often times", "No, that isn’t true.", the Buddha’s cousin, Mr. Rogers, "You’re not a yo-yo."',
                    diag='#50 read 41% AI. Narrowed (#54, #55, #56): 437 with its triad joined to the truth by So read Human '
                         'High by itself, as did 439 with one instruction for the pair of don’ts; 438 read AI by itself (#55) '
                         'as in the section. This try puts the two that read Human back, with his "whom" and "heavily" back '
                         'in them, and 438 in the shape of his 440, which read Human High in #50.',
                    first='payoff: 438’s seeing first and 439’s easy story first; join: 437’s triad joined to its truth with '
                          'So, 438’s last act with ", and don’t"; plain: "a cartoon villain", "simplest" for "parsimonious"',
                    hum='the paragraphs as they read by themselves, his own words back in them',
                    extra=['--narrowed', 'romance-s22-p437 (#54, Human High), romance-s22-p438 (#55, AI; its next version, '
                                         '47 words, is under the web app’s 50-word minimum, so it goes in here), '
                                         'romance-s22-p439 (#56, Human High)']),
    'r12-dam': dict(lineage='romance-low-dam', scope='section', call='Human', chance=0.6,
                    tells='a reason sentence before a list of wants',
                    human='"Based on what?", "basically", "a damn shame", his run of questions',
                    diag='#57 read Human with one Low window (45 words) on the reason and the want list, which read Human '
                         'High by themselves (#53) and Low in the live post: the tidy triad of wants after its reason is the '
                         'weak part. This fix joins his two reasons for not moving in fast (the common-law marriage, the '
                         'entanglement) into one sentence and says the list as two wants.',
                    first='payoff: his reasons before his wants, as in #53; join: his two reasons in one sentence with and; '
                          'plain: his words, the list said as two wants',
                    hum='his two reasons joined and his wants said as two, in his words',
                    extra=['--after-fix', 'his two reasons for not moving in fast joined with and, and the want list said as '
                                          'two wants ("and I want us to pick actual dates"), for the one Human Low window '
                                          'in #57']),
    'r12-sit33': dict(lineage='romance-low-sit-p33', scope='paragraph', call='Human', chance=0.5,
                      tells='a list of four things you do together, a definition', human='"basically the point", '
                      '"happenstance", "maybe just enough"',
                      diag='In #59 the void sentence with a comma for its dash read AI Low, in one window with "It can go '
                           'either way."; in the live post, with the dash, it read Human Low. This try keeps his dash and '
                           'joins the sentence to his list before it with so, since the list is why it feels like a '
                           'relationship.',
                      first='payoff: his order kept, the list before what it does; join: his list and the void sentence '
                            'joined with so; plain: his words, his dash kept',
                      hum='his list joined to the sentence it explains, his dash kept', extra=[]),
    'r12-sit34': dict(lineage='romance-low-sit-p34', scope='paragraph', call='Human', chance=0.5,
                      tells='"the fun without the responsibility", a claim and its rebuttal',
                      human='"Doomscrolling entertains you too.", "partly because she’s the one risking pregnancy"',
                      diag='In #59 his two claims joined with but read AI High and the plain "They don’t escape ..., '
                           'either" AI Low; in the live post, three sentences with the staged "What they don’t escape is", '
                           'Human Low. This try says his claims to the reader, as his "If you’re quite numb ..." does (Human '
                           'High in #60), keeps them two sentences, and ties the void to the second with "though, and".',
                      first='payoff: the one keeping it undefined named first, as "you"; join: the void tied to the '
                            'responsibility sentence with "though, and"; plain: "you don’t escape" for the staged "What '
                            'they don’t escape is"',
                      hum='his claims said to the reader, as he speaks to the reader elsewhere', extra=[]),
    'r12-clar108': dict(lineage='romance-low-clar-p108', scope='paragraph', call='Human', chance=0.55,
                        tells='two balanced if-sentences', human='"freaked out", "a bit like coming home"',
                        diag='In #60, with the point moved up, the two if-sentences stood bare and read AI Low and AI '
                             'Medium; in the live post, ending on the point, they read Human Low as one window. This try '
                             'keeps his order, ending on the point, and joins the two into one sentence with ", but if".',
                        first='payoff: his pair ends on its point, as he wrote it; join: the two if-sentences joined with '
                              '", but if"; plain: his words',
                        hum='his two if-sentences joined, ending on his point', extra=[]),
    'r12-peek': dict(lineage='romance-low-peek', scope='section', call='Human', chance=0.55,
                     tells='a run of questions to ask, a list of places to take them',
                     human='"Can you guys be normal together", "an inconvenient PMS afternoon", "😆", "a little “wait” feeling"',
                     diag='One Human Low window here in the live post: his short closing "That may mean the game worked '
                          'without telling us whether the relationship will." This try joins it to the sentence before with '
                          '", but that", the high and what it may mean in one sentence.',
                     first='payoff: the high comes first, then what it may mean; join: his short closing sentence joined with '
                           '", but that"; plain: his words',
                     hum='his short closing sentence joined to the one it answers', extra=[]),
    'r12-tricky': dict(lineage='romance-low-tricky', scope='section', call='Human', chance=0.5,
                       tells='a summing-up clause, "It’s just important to realize"',
                       human='"but I love her", "while I tell mine mine", "I’ll come back to that."',
                       diag='Two Human Low windows here in the live post: the closing "The relationship can close off at '
                            'exactly the point ..." with "Sometimes withdrawing isn’t wrong." after it, and "We need people '
                            'who actually know both of us ...". This try joins each to what it belongs to: the closing as '
                            '", right when both people most need a view from outside it", the short "Sometimes withdrawing '
                            'isn’t wrong" to its example with a colon (as the flaws list’s colon read Human High in #61), and '
                            '"We need people" to the problem before it with so.',
                       first='payoff: each problem comes before its answer; join: the closing, "Sometimes withdrawing isn’t '
                             'wrong" and "We need people" each joined to what they belong to; plain: his words',
                       hum='his short sentences joined to what they belong to', extra=[]),
}
for key, p in P.items():
    if sys.argv[1:] and key not in sys.argv[1:]:
        continue
    cmd = [sys.executable, str(ROOT / 'tools' / 'humanization' / 'pangram_ledger.py'), 'predict', str(LEDGER),
           '--lineage', p['lineage'], '--scope', p['scope'], '--text', REL + 'CHECK-%s.txt' % key, '--call', p['call'],
           '--chance', str(p['chance']), '--tells', p['tells'], '--human-tells', p['human'], '--diagnosis', p['diag'],
           '--decides', 'whether the %s reads Human with no Low window' % p['scope'], '--key', key, '--batch', 'romance-r12',
           '--detector', DET, '--receipt', REL + 'RECEIPT-%s.json' % key, '--first-fix', p['first'], '--humanized', p['hum']] \
          + p['extra']
    r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    print(key, r.returncode, (r.stdout + r.stderr).strip()[:700])
