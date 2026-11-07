#!/usr/bin/env python3
"""r21's predictions, written before the checks; each text was linted first (gate bad-trips-2026-11-07h)."""
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[5]
LEDGER = ROOT / 'articles' / 'romance' / 'humanize' / 'pangram-ledger.jsonl'
REL = 'articles/romance/humanize/fix-20261107/r21/checks/'
DET = 'pangram 4.1, the web app (Joel\'s account, GUI credits)'
HIS_S2 = 'https://www.pangram.com/history/f562bf37-6d5a-464a-bac9-2fc34bb2d3fa'
HIS_S17 = 'https://www.pangram.com/history/0e2f8a68-6fe9-4804-9bff-114705fa542b'
P = {
    'r21-bypass': dict(
        lineage='romance-sec-bypass', scope='section', call='Human', chance=0.8,
        tells='"People can want several things at once." (a balanced close, which survived in his version)',
        human='"more perverted", "massive unearned respect", "Venerable Nobody ... become Nobody some day", his ayahuasca '
              'story',
        diag='Try 1 (#48) read 14.3%% AI: his first 370 words Human High, then my S2 try AI Low and Medium. His own S2 read '
             'Human High by itself in his account (%s, 131 words). With the live 53 to 59 before it, the section should '
             'read Human; the risk is the balanced close on its own at the end.' % HIS_S2,
        extra=['--unchanged', 'the live post’s 53 to 59 and his S2 exactly as he sent it on the marking page '
               '(TEACH-MONASTIC-PERKS, ANSWERS-T1.json)',
               '--narrowed', 'his S2 checked by itself in his account (%s, Human High)' % HIS_S2]),
    'r21-spir': dict(
        lineage='romance-sec-spiritual-sex', scope='section', call='Human', chance=0.7,
        tells='"a lasting universal-consciousness awakening", the quoted sutta verse',
        human='"checks rolling in, and creativity flowing out like nobody\'s business", "No partner required for the jade '
              'egg phase.", "Who isn’t a stream-enterer these days?", his twin-flame paragraphs',
        diag='Try 1 (#45) read 14.8%% AI: AI Low on 304’s two denials, AI High and Medium on S17’s lists, AI Low on 312’s '
             'opener. Since then 304 to 309 read Human High by themselves (#115), and so did 312 with 313 (#116); his own '
             'S17 read Human High by itself (%s, 173 words) where his earlier version with the noun lists read 100%% AI. '
             'All are in this try, with "your attention" for his "you\'re attention".' % HIS_S17,
        extra=['--receipt', REL + 'RECEIPT-r21-spir.json',
               '--narrowed', 'romance-sec-spiritual-sex-p304#115 and romance-sec-spiritual-sex-p312#116 (both Human '
               'High), and his S17 checked by itself in his account (%s, Human High)' % HIS_S17,
               '--first-fix', 'payoff: his S17 says Anami’s claim as what she says, first; join: his; plain: his lists '
               'said as things that happen ("checks rolling in"), my only change "you\'re" to "your"',
               '--humanized', 'his S17 in place of S17, r20’s 304 to 306 kept']),
    'r21-jeal366': dict(
        lineage='romance-low-jeal-p366', scope='stretch', call='Human', chance=0.55,
        tells='"If you can’t do monogamy, it’s still more honest to just say so than to fake it." (a verdict line), '
              '"without necessarily doing the work on themselves"',
        human='"can’t keep it in their pants", "a whole sit-down talk", "one and only forever ... pull it off", "I '
              'learned most of this by screwing it up."',
        diag='In the section (#94) 367 to 369 read AI Low and Medium although each read Human High alone (#89, #90): the '
             'same pattern as S2, which his version fixed by saying lists and abstract nouns as concrete, idiomatic '
             'things. This try says "foundational, permanent, exclusive romantic partnership" as "promise to be each '
             'other’s one and only forever", "an inability to connect deeply" and "a lack of self-control" as what '
             'people do, and the disclosure line as a sit-down talk people avoid. 366 and 370 go with it unchanged.',
        extra=['--receipt', REL + 'RECEIPT-r21-jeal366.json',
               '--first-fix', 'payoff: each sentence says what people do first; join: 369’s opener joined with its '
               'reason; plain: the adjective stack and the abstract nouns said as idioms (one and only, keep it in '
               'their pants, a sit-down talk)',
               '--humanized', 'romance-2026-11-07a on 367 to 369 (his S2 and S17 fixes)']),
    'r21-rom284': dict(
        lineage='romance-low-romance-p284', scope='stretch', call='Human', chance=0.55,
        tells='"Letting a man help her, or lead for a while, leaves a strong woman just as strong." (a principle), "And a '
              'man she takes care of stays a grown man."',
        human='"play the damsel ... pretending she can’t open a jar", "a handful", "She’s choosing the ride.", "Honey, '
              'how do you see this intuitively?", Toft’s fifty years',
        diag='The section (#98) read 36.8% AI: AI windows on 285’s list sentence, 286’s over-correction, 287’s "help, '
             'lead, or give her pleasure" (AI High) and the parallel "I might ask ... she might ask"; Human Low on 285’s '
             'surrender line, 286’s list of worries and "Anami talks a lot about women learning to receive." Each list '
             'is now particular things, built differently; the parallel is broken; the two High sentences are kept.',
        extra=['--receipt', REL + 'RECEIPT-r21-rom284.json',
               '--first-fix', 'payoff: each sentence says what she does or feels first; join: kept short where a list '
               'was packed; plain: "play the damsel", "a handful", "lying back while he pleases her" for the lists',
               '--humanized', 'romance-2026-11-07a on 285 to 287 (his S2 and S17 fixes)']),
    'r21-ideal147': dict(
        lineage='romance-low-ideal-p147', scope='pair', call='Human', chance=0.6,
        tells='"Then come the public accusations." (a short inverted line)',
        human='"I’m already running", "worshipped me can start hating me in private", his punchline about thinking I’m '
              'perfect',
        diag='Try 1 (#93) read 36.9% AI: my BPD gloss AI Medium and the list "public accusations, rewriting the whole '
             'past and treating every flaw as proof" AI Low. This try drops the gloss (BPD is used earlier in the '
             'article) and says the list in two sentences built differently; 147 and the punchline are kept.',
        extra=['--receipt', REL + 'RECEIPT-r21-ideal147.json',
               '--first-fix', 'payoff: what happens first ("a woman who worshipped me can start hating me in '
               'private"); join: the list split into two sentences built differently; plain: "a sign" for "proof"',
               '--humanized', 'romance-2026-11-07a on 148']),
}
for key, p in P.items():
    if sys.argv[1:] and key not in sys.argv[1:]:
        continue
    cmd = [sys.executable, str(ROOT / 'tools' / 'humanization' / 'pangram_ledger.py'), 'predict', str(LEDGER),
           '--lineage', p['lineage'], '--scope', p['scope'], '--text', REL + 'CHECK-%s.txt' % key, '--call', p['call'],
           '--chance', str(p['chance']), '--tells', p['tells'], '--human-tells', p['human'], '--diagnosis', p['diag'],
           '--decides', 'whether the %s reads Human with no Low window' % p['scope'], '--key', key, '--batch', 'romance-r21',
           '--detector', DET] + p['extra']
    r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    print(key, r.returncode, (r.stdout + r.stderr).strip()[:900])
