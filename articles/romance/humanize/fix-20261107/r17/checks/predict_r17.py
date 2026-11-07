#!/usr/bin/env python3
"""r17's predictions, written before the checks; each text was linted first (gate bad-trips-2026-11-07h)."""
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[5]
LEDGER = ROOT / 'articles' / 'romance' / 'humanize' / 'pangram-ledger.jsonl'
REL = 'articles/romance/humanize/fix-20261107/r17/checks/'
DET = 'pangram 4.1, the web app (Joel\'s account, GUI credits)'
P = {
    'r17-sit': dict(lineage='romance-low-sit', scope='section', call='Human', chance=0.5,
                    tells='"the fun without (most of) the responsibility", "the existential void another superficial fix '
                          'creates"',
                    human='"Doomscrolling entertains you too.", "We were (and still are) BFFs", "drainingly superficial"',
                    diag='Two section tries read below High (#59, #86: 15% AI, two AI Low windows in 34). By itself, 34 then '
                         'read Human with no Low (#95) and 33 Human High (#64). This check after the fix (his answer 28a) '
                         'puts #95’s 34 back with 33 as #64 read, and says 36’s closing line (Low in the live post and in '
                         '#86) once, in its opening sentence, where "much deeper" already said it wasn’t superficial.',
                    first='payoff: 36’s point (deeper, and painfully uneven) said in its first sentence; join: 36’s closing '
                          'line into its opener with and; plain: his words',
                    hum='34 as it read Human by itself, and 36’s repeated closing line cut into its opener',
                    extra=['--after-fix', '34 as it read Human with no Low by itself (#95), for the two AI Low windows in '
                                          '34 in #86, and 36’s closing line said in its opener']),
    'r17-babies': dict(lineage='romance-low-babies', scope='section', call='Human', chance=0.55,
                       tells='a list of four roles ("therapist, guru, doctor, or dad"), "It can be affectionate, erotic, '
                             'comforting, or playful."',
                       human='"Wow, I must have been really confused back then!", "Can you be my guru?", "then I’ve made '
                             'her Mom"',
                       diag='One Human Low window here in the live post, 238’s "But enough moments become a pattern." (6 '
                            'words), and two spots fixed by themselves: S11 (233 and 234, Human High in #37) and S12 (240 '
                            'and 241, Human High in #13). This first check of the whole section puts both spots in as '
                            'they read and joins 238’s short closing to the sentence before with but.',
                       first='payoff: unchanged, his order; join: 238’s two sentences with but; plain: his words',
                       hum='his short closing joined with but, and the spots as they read', extra=[]),
    'r17-levels': dict(lineage='romance-low-levels', scope='section', call='Human', chance=0.5,
                       tells='"So I do believe in mutual coaching and complementarity.", a list of four ("maturity, '
                             'emotional stability, self-love, and self-awareness")',
                       human='"According to myself", "more moolah", "everyone should simply do as they please"',
                       diag='Two Human Low windows here in the live post, both in 250: its first sentence (29 words, the '
                            'advice after its condition, with "lest") and its last (27 words, two balanced clauses before '
                            'the point). S13 (248 and 249) read Human High by itself (#14). This try says 250’s advice '
                            'first with "or" for "lest", puts the closing’s point first with its aside in brackets, and '
                            'puts S13 in as it read.',
                       first='payoff: 250’s advice and its closing point said first; join: none; plain: "or the romance '
                             'could collapse" for "lest the romance collapse", "a partner" for "one person"',
                       hum='his advice said first, and his closing aside left a little unbalanced in brackets', extra=[]),
    'r17-choosing': dict(lineage='romance-low-choosing', scope='section', call='Human', chance=0.5,
                         tells='"There’s nothing inherently wrong with that arrangement", a list of six ("sex, '
                               'exclusivity, living together, money, children, caregiving")',
                         human='"two lovey bunnies", "low-key pretending", "And the biggie", "make a card game out of '
                               'this"',
                         diag='Two Human Low windows here in the live post: 342’s "The problem is when we’re using the '
                              'same words for two different futures." (14 words) and 344’s "Two people really are in love '
                              'and want to build something together." (12 words). S20 (345 and 346) read Human High by '
                              'itself (#27). This try joins each short sentence to the one it belongs with (342’s with but, '
                              '344’s with and), says "without naming every part" as what happens and "without pretending" '
                              'as a condition (the linter’s E186), and puts S20 in as it read.',
                         first='payoff: unchanged, his order; join: 342’s two sentences with but, 344’s with and; plain: '
                               '"with some parts left unnamed" for "without naming every part", "as long as nobody '
                               'pretends" for "without pretending"',
                         hum='his short sentences joined to what they belong with', extra=[]),
    'r17-artificial': dict(lineage='romance-low-artificial', scope='section', call='Human', chance=0.6,
                           tells='"This is the time for agape to shine", "which was its own kind of damage"',
                           human='"Well, yeah.", "(LOL)..", "old Romeo & Juliette might get wandering eye syndrome", "as '
                                 'my dad explained a thousand times whenever we had a visitor"',
                           diag='One Human Low window here, in the live post and in the last part’s check (#47): 410’s '
                                '"Some things were less mysterious." (5 words). This try joins it to what it says with a '
                                'colon; the rest is the live post’s.',
                           first='payoff: what was less mysterious said in the same sentence; join: 410’s opener with a '
                                 'colon; plain: his words',
                           hum='his short opener joined to what it says', extra=[]),
    'r17-gaslight': dict(lineage='romance-low-gaslight', scope='section', call='Human', chance=0.5,
                         tells='"good friends should hear both sides before validating either", "that’s no reason to '
                               'pretend"',
                         human='"you might wanna find some new friends", "I’ve never told anyone this, but you guys need '
                               'to split up", "Ann"',
                         diag='Three Human Low windows here in the last part’s check (#47): 433’s "Both people should have '
                              'a chance to speak, and good friends shouldn’t automatically validate either side." (17 '
                              'words), and 435’s "You may need to arrange other care." (7) and "That doesn’t mean you '
                              'have to pretend the romance still has a future." (14). This try says 433’s guideline as '
                              'what good friends do (the linter’s X1), and joins 435’s pair with but, said as "that’s no '
                              'reason to" (the linter read "you don’t have to" as a coach phrase, E41).',
                         first='payoff: what good friends do said plainly; join: 435’s two sentences with but; plain: '
                               '"should hear both sides before validating either" for "shouldn’t automatically validate '
                               'either side"',
                         hum='his denial said as what friends do, and his short pair joined', extra=[]),
}
for key, p in P.items():
    if sys.argv[1:] and key not in sys.argv[1:]:
        continue
    cmd = [sys.executable, str(ROOT / 'tools' / 'humanization' / 'pangram_ledger.py'), 'predict', str(LEDGER),
           '--lineage', p['lineage'], '--scope', p['scope'], '--text', REL + 'CHECK-%s.txt' % key, '--call', p['call'],
           '--chance', str(p['chance']), '--tells', p['tells'], '--human-tells', p['human'], '--diagnosis', p['diag'],
           '--decides', 'whether the %s reads Human with no Low window' % p['scope'], '--key', key, '--batch', 'romance-r17',
           '--detector', DET, '--receipt', REL + 'RECEIPT-%s.json' % key, '--first-fix', p['first'], '--humanized', p['hum']] \
          + p['extra']
    r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    print(key, r.returncode, (r.stdout + r.stderr).strip()[:700])
