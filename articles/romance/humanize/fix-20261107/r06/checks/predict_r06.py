#!/usr/bin/env python3
"""r06's predictions, written before the checks (pangram_ledger.py predict): four sections with the best tries in place,
and the post's last part, which his extension never read, as it stands."""
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[5]
LEDGER = ROOT / 'articles' / 'romance' / 'humanize' / 'pangram-ledger.jsonl'
REL = 'articles/romance/humanize/fix-20261107/r06/checks/'
DET = 'pangram 4.1, the web app (Joel\'s account, GUI credits)'
WHY = ('the two-paragraph checks of this spot read his own sentences AI as well, Human in the live post, so they could not '
       'tell my change from the context; the section is the unit the live post has around it')
P = {
    'r06-secA': dict(lineage='romance-sec-bypass', scope='section', call='AI', chance=0.45,
                     tells='S2’s perks and West sentences (AI Low in #38)',
                     human='his ayahuasca story, Bhante Gunaratana, the abbot, "Robes do nothing", "Venerable Somebody"',
                     diag='S2’s fifth try (#38) read 27% AI, only its perks and West sentences AI Low, and in every pair '
                          'check his own first paragraph read only Human Low or AI. ' + WHY + '.',
                     first='payoff: as #38, the West case said as where the food falls away; join: as #38, "And even where ..." '
                           'ties the West case to the first; plain: "a roof", "hold down a job", "gets to be Venerable Somebody"',
                     hum='S2 as its fifth try has it (his moves: the point first, the mirrored pair broken, his closing '
                         'pair kept), now inside his section'),
    'r06-secB': dict(lineage='romance-sec-whole-world', scope='section', call='AI', chance=0.4,
                     tells='S10, his words in a new order (AI Medium in #41)',
                     human='his paradise and heroin lines, his questions about friends, Toft, "Don’t just disappear into '
                           'each other"',
                     diag='S10’s fourth try (#41), his own words with the problem first, read AI Medium; my rebuilds read '
                          'worse, and his girlfriend sentence before it read Human Low in every pair check. ' + WHY + '.',
                     first='payoff: the problem first, then his answer; join: his outburst and what it sounds like in one '
                           'sentence; plain: his words',
                     hum='S10 in his own words, reordered so the problem leads, now inside his section'),
    'r06-secC': dict(lineage='romance-sec-spiritual-sex', scope='section', call='AI', chance=0.35,
                     tells='S17’s students’ list (AI High in every try)',
                     human='the suttas as he cites them, the Keenes, Malia and Mouhamed, "she should have picked Grok"',
                     diag='S17’s tries read AI at 100% in two-paragraph checks, his own jade-egg sentence included (Human '
                          'in the live post); the best of them (#36) read AI Low, High, Low. ' + WHY + '.',
                     first='payoff: what she says comes first (#36); join: "goes even further:"; plain: "can heal you and '
                           'wake you up spiritually"',
                     hum='S17 as its second try has it, now inside his section with the suttas before and the Keenes and '
                         'twin flames after'),
    'r06-secD': dict(lineage='romance-sec-vows', scope='section', call='Human', chance=0.5,
                     tells='a closing rhetorical question after a colon',
                     human='his vows paragraph, his Ecclesiastes and Matthew sentences, "feelings aren’t contractual"',
                     diag='S21’s three rebuilds (#28, #33, #43) read AI Medium to High, worse than the live post’s two AI '
                          'Low sentences, and pulled his verses to AI. This try keeps his two sentences and only joins them, '
                          'so the question reads as the reason for the suspicion. ' + WHY + '.',
                     first='payoff: the suspicion first, its reason after the colon; join: his two sentences joined by a '
                           'colon; plain: his words',
                     hum='his own two closing sentences joined into one, so the second is read as the reason for the first'),
    'r06-secD2': dict(lineage='romance-sec-vows', scope='section', call='Human', chance=0.5,
                      tells='a which-clause at the end of a long sentence',
                      human='his vows paragraph, his Ecclesiastes and Matthew sentences, "feelings aren’t contractual"',
                      diag='Try 1 (#46) read every window Human except the closing sentence, his own two sentences joined '
                           'by a colon, AI High; in the live post the same two sentences read AI Low each. Both are a '
                           'closing summary after the verse: the suspicion, then the verse again as a question.',
                      first='payoff: the conclusion rides on the verse that leads to it; join: "which makes" joins it to '
                            'his Matthew sentence; plain: his words, the repeated question cut',
                      hum='the closing summary is gone as a sentence of its own: the conclusion is the end of his verse '
                          'sentence, and the question that repeated the verse is cut'),
}
for key, p in P.items():
    if sys.argv[1:] and key not in sys.argv[1:]:
        continue
    cmd = [sys.executable, str(ROOT / 'tools' / 'humanization' / 'pangram_ledger.py'), 'predict', str(LEDGER),
           '--lineage', p['lineage'], '--scope', p['scope'], '--text', REL + 'CHECK-%s.txt' % key, '--call', p['call'],
           '--chance', str(p['chance']), '--tells', p['tells'], '--human-tells', p['human'], '--diagnosis', p['diag'],
           '--decides', 'whether the section reads Human with the spot’s best try in it', '--key', key,
           '--batch', 'romance-r06', '--detector', DET, '--receipt', REL + 'RECEIPT-%s.json' % key,
           '--first-fix', p['first'], '--humanized', p['hum']]
    r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    print(key, r.returncode, (r.stdout + r.stderr).strip()[:600])
if not sys.argv[1:] or 'r06-tail' in sys.argv[1:]:
    cmd = [sys.executable, str(ROOT / 'tools' / 'humanization' / 'pangram_ledger.py'), 'predict', str(LEDGER),
           '--lineage', 'romance-tail', '--scope', 'stretch', '--text', REL + 'CHECK-r06-tail.txt', '--call', 'AI',
           '--chance', '0.2', '--tells', 'none named: his text as it stands', '--human-tells', 'his Bee, Key, Ann and Bear '
           'stories, his dad, Rumi, Somé, "You’re not a yo-yo"', '--diagnosis', 'His extension read only the first 99,999 '
           'characters of the live post (live-check/META.json); the post is 116,586, so its last 2,871 words, from "It’s '
           'not always possible in that moment to change a defensive posture" to the end, were never checked. The rest of '
           'the post had 21 AI spots in about 18,400 words.', '--decides', 'where the unchecked last part of the post '
           'reads AI or Low', '--key', 'r06-tail', '--batch', 'romance-r06', '--detector', DET, '--unchanged',
           'the live post’s last part as it stands, paragraphs 403 to 457 without their headings, which his extension '
           'did not read']
    r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    print('r06-tail', r.returncode, (r.stdout + r.stderr).strip()[:600])
