#!/usr/bin/env python3
"""r13's predictions, written before the checks."""
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[5]
LEDGER = ROOT / 'articles' / 'romance' / 'humanize' / 'pangram-ledger.jsonl'
REL = 'articles/romance/humanize/fix-20261107/r13/checks/'
DET = 'pangram 4.1, the web app (Joel\'s account, GUI credits)'
P = {
    'r13-s22': dict(lineage='romance-s22', scope='section', call='Human', chance=0.6,
                    tells='advice to the reader in the imperative',
                    human='"Often times", "No, that isn’t true.", the Buddha’s cousin, Mr. Rogers, "You’re not a yo-yo."',
                    diag='#62 read Human with two Low windows: 438’s last sentence (my instruction with the villain at its '
                         'end) and his 9-word "Looking honestly at your part doesn’t erase theirs.", split off alone after '
                         'the Buddha sentence (Low in #50 too). This fix puts 438’s point first ("And don’t turn your ex into '
                         'a cartoon villain: try to understand ...") and joins his short sentence to the example it draws on '
                         'with a colon, as the colons in #61 and #68 read High.',
                    first='payoff: 438’s instruction first, then how; join: his short lesson joined to the Buddha sentence '
                          'with a colon; plain: his words',
                    hum='the point said first and his short sentence joined to its example',
                    extra=['--after-fix', '438’s last sentence with its point first, and his "Looking honestly at your part '
                                          'doesn’t erase theirs." joined to the Buddha sentence with a colon, for the two '
                                          'Human Low windows in #62']),
    'r13-dam': dict(lineage='romance-low-dam', scope='section', call='Human', chance=0.55,
                    tells='a want list', human='"Based on what?", "basically", "a damn shame", his run of questions',
                    diag='The want list read Low in every form after its reason (#57 as a triad, #63 as two wants) and in '
                         'the live post; by itself after the reason it read High (#53). This fix says the wants as part of '
                         'the paragraph’s point, what he does when sex comes quickly, and gives his two reasons after it, '
                         'the point first as his first fix asks.',
                    first='payoff: the wants said with the paragraph’s point, the reasons after; join: the wants joined to '
                          '"that’s a reason not to move in quickly too"; plain: his words',
                    hum='his wants said with his point and his reasons after, in his words',
                    extra=['--after-fix', '176 with its point first: what he does when sex comes quickly (not moving in fast, '
                                          'and the three wants), then his two reasons in one sentence, for the Low window '
                                          'on the want list in #63']),
    'r13-clar': dict(lineage='romance-low-clar', scope='section', call='Human', chance=0.7,
                     tells='a dash pair around the chemicals', human='"the modern degen dating scene", "etc.", "freaked out"',
                     diag='#60 read 15% AI: the bare if-pair after the point was moved up. Narrowed (#66): with the pair '
                          'joined and ending on its point as he wrote it, the oxytocin paragraph read Human High (79 words, '
                          'one window). This try puts it back with the first three paragraphs as they read High in #60.',
                     first='payoff: his pair ends on its point, as he wrote it; join: the pair joined with ", but if", and '
                           '107’s two sentences made one; plain: his words',
                     hum='his short sentences joined and his pair ending on its point',
                     extra=['--narrowed', 'romance-low-clar-p108 (#66, Human High), checked by itself']),
    'r13-sit34': dict(lineage='romance-low-sit-p34', scope='paragraph', call='AI', chance=0.4,
                      tells='"the fun without the responsibility", a claim and its rebuttal, "What they don’t escape is"',
                      human='"Doomscrolling entertains you too.", "partly because she’s the one risking pregnancy"',
                      diag='The you-frame (#65) read Human Low throughout, his unchanged first two sentences included, and '
                           'his two claims joined with but read AI High (#59). This try goes back to his three sentences as '
                           'the live post has them (Human Low in the extension) and joins only the short "It can go either '
                           'way." to the sentence it opens, to see how his own version reads by itself.',
                      first='payoff: who keeps it undefined comes first; join: "It can go either way" joined to the sentence '
                            'it opens with but; plain: his words as the live post has them',
                      hum='his short opening sentence joined to the one it opens, the rest his', extra=[]),
    'r13-ptsd': dict(lineage='romance-low-ptsd', scope='section', call='Human', chance=0.6,
                     tells='"That’s the reality shift I’m talking about", a list of three ways to go in',
                     human='"anti-PTSD", "like Ping Pong", "Best drug I ever had.", "witchcrafted"',
                     diag='One Human Low window here in the live post: his short "That dynamic alone isn’t necessarily the '
                          'main problem." This try joins it to the sentence that says why with a colon, as his flaws list’s '
                          'colon read High (#61).',
                     first='payoff: the claim first, then why; join: the short claim joined to its reason with a colon; '
                           'plain: his words',
                     hum='his short sentence joined to the one that says why', extra=[]),
    'r13-slow': dict(lineage='romance-low-slow', scope='section', call='Human', chance=0.5,
                     tells='a balanced can/can’t pair, a five-part list of what may not fit',
                     human='"Let’s just be friends!", "the bodies just don’t connect"',
                     diag='One Human Low window here (84 words in the live post): "It still can’t tell you how good the sex '
                          'will be ..." with his twenty-years sentence after it. This try joins the two halves of his first '
                          'paragraph with but, what going slowly can show and what it can’t, the way his "Often times the '
                          'breakup is hard, but the aftermath is worse." reads High (#62).',
                     first='payoff: what going slowly shows comes first, then what it can’t; join: his two sentences joined '
                           'with but; plain: his words',
                     hum='his two short halves joined with but, the way he joins his own', extra=[]),
    'r13-disc': dict(lineage='romance-low-disc', scope='section', call='Human', chance=0.6,
                     tells='"That’s why I recommend", a list of three things to put first',
                     human='"it can’t see what it can’t see", "the Buteyko method", "My breathing gets shallow."',
                     diag='One Human Low window here: his short "Other times it’s hard to tell." This try joins it to the '
                          'sentence it answers with and ("Sometimes she’s deliberately trying to do that, and other times '
                          'it’s hard to tell."), as the joined Sometimes sentences read High in the dam section (#52).',
                     first='payoff: unchanged, his order; join: his short Sometimes and Other times sentences joined with '
                           'and; plain: his words',
                     hum='his two short sentences joined with and', extra=[]),
}
for key, p in P.items():
    if sys.argv[1:] and key not in sys.argv[1:]:
        continue
    cmd = [sys.executable, str(ROOT / 'tools' / 'humanization' / 'pangram_ledger.py'), 'predict', str(LEDGER),
           '--lineage', p['lineage'], '--scope', p['scope'], '--text', REL + 'CHECK-%s.txt' % key, '--call', p['call'],
           '--chance', str(p['chance']), '--tells', p['tells'], '--human-tells', p['human'], '--diagnosis', p['diag'],
           '--decides', 'whether the %s reads Human with no Low window' % p['scope'], '--key', key, '--batch', 'romance-r13',
           '--detector', DET, '--receipt', REL + 'RECEIPT-%s.json' % key, '--first-fix', p['first'], '--humanized', p['hum']] \
          + p['extra']
    r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    print(key, r.returncode, (r.stdout + r.stderr).strip()[:700])
