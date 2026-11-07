#!/usr/bin/env python3
"""r14's predictions, written before the checks."""
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[5]
LEDGER = ROOT / 'articles' / 'romance' / 'humanize' / 'pangram-ledger.jsonl'
REL = 'articles/romance/humanize/fix-20261107/r14/checks/'
DET = 'pangram 4.1, the web app (Joel\'s account, GUI credits)'
PANEL = 'articles/romance/humanize/fix-20261107/r14/panel-sit34/PANEL.md'
P = {
    'r14-sit34': dict(lineage='romance-low-sit-p34', scope='paragraph', call='Human', chance=0.55,
                      tells='"the fun without the responsibility", the hedge opener',
                      human='"Doomscrolling entertains you too.", "partly because she’s the one risking pregnancy"',
                      diag='The tell panel agreed on four of its five sentences: the hedge opener, the fun-without-'
                           'responsibility antithesis, the "doesn’t make the responsibility disappear" formula that restates '
                           'it, and the staged "What they don’t escape is the existential void ..."; both readers said the '
                           'whole is a chain of even general claims with nothing concrete. This try says what stays '
                           'concretely (people still get pregnant and attached, his own pair from paragraph 41) and the void '
                           'plainly, joined to it; the opener read Medium (#72) and his fun line stays.',
                      first='payoff: what stays (pregnancy, attachment) said first in its sentence; join: the void sentence '
                            'joined to it; plain: "ends up with" for the staged "What they don’t escape is"',
                      hum='the panel’s agreed tells fixed with his own concrete pair from paragraph 41',
                      extra=['--panel', PANEL, '--big-change', 'the small fixes are spent: saying it to the reader (#65), his own '
                                   'version with one join (#72) and his claims joined with but (#59) all read '
                                   'below High, and the panel’s agreed tells sit in the two sentences this try '
                                   'rewrites (the formula and the staged void); the other three are kept, and '
                                   'the share is high because the paragraph has 66 words']),
    'r14-slow181': dict(lineage='romance-low-slow-p181', scope='pair', call='Human', chance=0.5,
                        tells='a list of things that may not fit', human='"Let’s just be friends!", "the bodies just don’t connect"',
                        diag='In #74 his twenty-years sentence, a five-part list in one breath, read AI Low with the sentence '
                             'after it; in the live post it read Human Low with the sentence before it. This try says the '
                             'list a pair at a time, in three sentences, as the bad trips lesson has it (a list said one item '
                             'at a time, with verbs), checked with paragraph 182 since the list’s paragraph alone is under 50 '
                             'words.',
                        first='payoff: the polarity, the first thing that may not fit, comes first; join: the list’s items '
                              'said two by two; plain: his words, with "can" and "Maybe" to carry them',
                        hum='his list said a pair at a time', extra=[]),
    'r14-disc220': dict(lineage='romance-low-disc-p220', scope='pair', call='Human', chance=0.55,
                        tells='a recommendation tied to its reason', human='"hopefully does not", "whatever I do when I still '
                        'don’t understand it"',
                        diag='In #75 "That’s why I recommend peer counseling outside the couple." read Low by itself (10 '
                             'words) and the pain sentence after it Low (39 words, with the next paragraph’s first sentence), '
                             'where the extension read them Human at Medium or High in the whole post. "That’s why I '
                             'recommend" stages the recommendation (the significance-staging rule in AGENTS.md); this try '
                             'says it directly and joins it to its reason with a colon.',
                        first='payoff: his recommendation said directly, its reason after; join: the recommendation and its '
                              'reason with a colon; plain: "I recommend" for "That’s why I recommend"',
                        hum='his recommendation said directly and joined to its reason', extra=[]),
    'r14-disc221': dict(lineage='romance-low-disc-p221', scope='paragraph', call='Human', chance=0.55,
                        tells='a mind-and-body pair', human='"My breathing gets shallow", "dragged down, fragile, and sensitive"',
                        diag='In #75 "I also have to deal with what happens in my body." and "My mind may understand ..." '
                             'read Low (39 and 24 words) and the body sentences Medium. This try joins his opening to the '
                             'mind-and-body pair with a colon and the pair with "but ... still", and his two short closing '
                             'sentences with and.',
                        first='payoff: what happens in his body comes first; join: the mind-and-body pair with "but ... '
                              'still", the short closing sentences with and; plain: his words',
                        hum='his short sentences joined and his pair said as one sentence', extra=[]),
    'r14-disc223': dict(lineage='romance-low-disc-p223', scope='paragraph', call='Human', chance=0.6,
                        tells='a pointer to another guide', human='"automatic erratic breathwork", "the Buteyko method"',
                        diag='In #75 its last two sentences read Low inside an 84-word window with paragraph 224. This checks '
                             'the paragraph by itself, with its Sometimes join as r13 had it, to see whether the Low belongs '
                             'to it or to 224.',
                        first='payoff: unchanged, his order; join: his Sometimes and Other times sentences with and; plain: '
                              'his words',
                        hum='his two short sentences joined with and', extra=[]),
    'r14-disc224': dict(lineage='romance-low-disc-p224', scope='paragraph', call='Human', chance=0.55,
                        tells='a list of three things to put first, "a road into spiritual bypassing"',
                        human='"or have not gotten to that stage yet"',
                        diag='In #75 paragraph 224 read Low inside an 84-word window with 223’s end. This try joins its short '
                             '"Meditation is also helpful." to the sentence it opens with but, and its two reasons for the '
                             'order with and.',
                        first='payoff: where meditation fits comes first; join: the short opener with but, the two reasons '
                              'with and; plain: his words',
                        hum='his short opener and his two reasons joined', extra=[]),
    'r14-muses': dict(lineage='romance-low-muses', scope='section', call='Human', chance=0.55,
                      tells='"I’m referring more to feminine vs masculine archetypes", a list of what she brings',
                      human='"Woops...", "teleport me outside the galaxy", "mute her with the TV remote", "tho"',
                      diag='One Human Low window here in the live post: its opening "In ordinary life, I sometimes think of '
                           'the woman as the engine and myself as the steering wheel." This try joins it to the sentence that '
                           'says what the engine gives him ("and I get motivation from her").',
                      first='payoff: the picture first, then what it gives him; join: the opening and "I get motivation from '
                            'her" with and; plain: his words',
                      hum='his opening joined to the sentence that explains it', extra=[]),
    'r14-queen': dict(lineage='romance-low-queen', scope='section', call='Human', chance=0.5,
                      tells='"establishes the biological validity", a dash aside',
                      human='"(ahem..)", "peanut gallery critics and lazy fact-checkers", "It seems more like foreplay."',
                      diag='One Human Low window here: "That laboratory evidence establishes the biological validity and '
                           'uniqueness of the phenomenon.", a formal sentence after his own. This try joins it to the sentence '
                           'before with and, in plain words ("shows it’s a real and distinct thing in the body"); Kim '
                           'Anami’s claims stay as the live post words them.',
                      first='payoff: the studies first, then what they show; join: the evidence sentence joined to the one '
                            'before with and; plain: "shows it’s a real and distinct thing in the body" for "establishes '
                            'the biological validity and uniqueness of the phenomenon"',
                      hum='the formal sentence said plainly and joined to his', extra=[]),
    'r14-jeal': dict(lineage='romance-low-jeal', scope='section', call='Human', chance=0.55,
                     tells='"A foundational, permanent, exclusive romantic partnership", a balanced verdict on polyamory',
                     human='"The inner Magic 8 Ball came back YES", "about 99% of the time", "I learned most of this by '
                     'screwing it up."',
                     diag='One Human Low window here: his closing "Sometimes the pretending does more damage than an outside '
                          'connection would have." This try joins it to the sentence it finishes with and.',
                     first='payoff: unchanged, his order; join: the closing sentence joined to the one before with and; '
                           'plain: his words',
                     hum='his short closing sentence joined to the one it finishes', extra=[]),
    'r14-labels': dict(lineage='romance-low-labels', scope='section', call='Human', chance=0.5,
                       tells='"Here’s the funny thing many people don’t understand:", "not a label"',
                       human='"No, I’m miserable, dude.", "Get a cat or a puppy.", "come on."',
                       diag='One Human Low window here (52 words in the live post, from the end of the H. story): "Here’s the '
                            'funny thing many people don’t understand: labels don’t create commitment. They can still '
                            'expose ..." and "True commitment grows out of relational depth, not a label." This try joins '
                            'his two label sentences with but, and his commitment sentence to its example with a colon.',
                       first='payoff: what labels do and don’t do comes first; join: the two label sentences with but, the '
                             'commitment sentence to its example with a colon; plain: his words',
                       hum='his short sentences joined to what they belong with', extra=[]),
}
for key, p in P.items():
    if sys.argv[1:] and key not in sys.argv[1:]:
        continue
    cmd = [sys.executable, str(ROOT / 'tools' / 'humanization' / 'pangram_ledger.py'), 'predict', str(LEDGER),
           '--lineage', p['lineage'], '--scope', p['scope'], '--text', REL + 'CHECK-%s.txt' % key, '--call', p['call'],
           '--chance', str(p['chance']), '--tells', p['tells'], '--human-tells', p['human'], '--diagnosis', p['diag'],
           '--decides', 'whether the %s reads Human with no Low window' % p['scope'], '--key', key, '--batch', 'romance-r14',
           '--detector', DET, '--receipt', REL + 'RECEIPT-%s.json' % key, '--first-fix', p['first'], '--humanized', p['hum']] \
          + p['extra']
    r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    print(key, r.returncode, (r.stdout + r.stderr).strip()[:700])
