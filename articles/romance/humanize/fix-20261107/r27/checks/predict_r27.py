#!/usr/bin/env python3
"""r27's predictions, written before the checks (2026-11-08); each text was linted first (gate bad-trips-2026-11-07h):
the lint's flags fall on the live post's words and his own, which stay (his "my one poly college friend" counts one)."""
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[5]
LEDGER = ROOT / 'articles' / 'romance' / 'humanize' / 'pangram-ledger.jsonl'
REL = 'articles/romance/humanize/fix-20261107/r27/checks/'
DET = "pangram 4.1, the web app (Joel's account, GUI credits)"
P = {
    'r27-jeal': dict(
        lineage='romance-low-jeal', scope='section', call='Human', chance=0.6,
        tells='none of mine left: 366 to 370 are his T2 answer, with "than" put in, "too" taken out and one apostrophe '
              'straightened',
        human='his Magic 8 Ball story (357 to 361), "It sure would beat beating around the bush", "my one poly college '
              'friend who boasted about having 4 girlfriends", "come out of the closet" as poly',
        diag='Every version of mine read Human alone and AI together (#119, #131, #133, #134). His five read one Human High '
             'window by themselves (his check 8f1e5924, 302 words), the way his S2 did before it read Human in its '
             'section (#117), so I call Human; the open question is whether 357 to 365 around it keep a Low window.',
        extra=['--receipt', REL + 'RECEIPT-r27-jeal.json',
               '--unchanged', '357 to 365 as the live post has them; 366 to 370 as his T2 answer has them '
                              '(review/teach-20261107/ANSWERS-T2.json), but for three slips fixed (texts.py EDITS)',
               '--narrowed', 'his 366 to 370 by themselves: Human High (https://www.pangram.com/history/'
                             '8f1e5924-1921-4136-8815-d09f45d295e5)',
               '--after-fix', 'his version of 366 to 370 in place of the live 366 to 370']),
    'r27-jeal-b': dict(
        lineage='romance-low-jeal', scope='section', call='Human', chance=0.6,
        tells='none of mine but the five words added: "they can put it to work."',
        human='as r27-jeal: the Magic 8 Ball story, "beat beating around the bush", the college friend with 4 girlfriends',
        diag='#135 read Human, High, with one Medium window on the live 361. The sense read found 366\'s comparison '
             'with nothing to attach to; five words give it one, splitting the sentence before "I agree". A short '
             'plain sentence beside his should keep the section High.',
        extra=['--receipt', REL + 'RECEIPT-r27-jeal-b.json',
               '--unchanged', '357 to 365 as the live post has them; 366 to 370 as #135 checked them but for 366\'s '
                              'five added words',
               '--after-fix', '"they can put it to work." added to 366 after "even better than simply suppressing it" '
                              '(the sense read, whole/sense-r27)']),
    'r27-ideal': dict(
        lineage='romance-low-ideal', scope='section', call='Human', chance=0.55,
        tells='mine in 145, 147, 148 and 151, each reworked his way: two short sentences joined with "since", a hedge '
              '("can go", "can find") said as what happens, "Sure." as a sentence and "still matter to me" said plainly',
        human='"a real love slave", "save a hoe", "lost in the sauce", "I’m Lord Krishna", "she hasn’t found all of me"',
        diag='#132 read Human with five Low windows, each on a sentence of mine: 145\'s two short sentences, 147\'s caveat '
             'sentence, 148\'s two hedged sentences, 151\'s "Sure." and its last two. His fixes (join, point first, plain '
             'word, no hedge) took S2 and Jealousy to High; I expect them to lift these, with a Medium or two left.',
        extra=['--receipt', REL + 'RECEIPT-r27-ideal.json',
               '--after-fix', '145, 147, 148 and 151 reworked (texts.py IDEAL_EDITS) after #132\'s five Low windows',
               '--first-fix', 'join: 145\'s two sentences with "since", 147\'s two, 151\'s answer and its reason; payoff: '
                              '145 names what it points at; plain: "still care about them", "means", no hedges',
               '--humanized', '145 (the live post\'s), 147, 148 and 151 (r21 to r24)']),
    'r27-ideal-b': dict(
        lineage='romance-low-ideal', scope='section', call='Human', chance=0.5,
        tells='mine in 145, 148 and 151, reworked after #138',
        human='"a knight in shining armor", "you’re perfect" to "you’re a fraud", "gonna", "sometimes too"',
        diag='#138 read 14%% AI: AI Low on 148\'s first two sentences and 151\'s last, Human Low on 145 and 148\'s last. '
             'What was left was mine in neat mirrored shapes and abstract claims, the S2 pattern; his versions fixed that with '
             'particular things, quoted speech and a slack casual ending, so each changed sentence now says who does what.',
        extra=['--receipt', REL + 'RECEIPT-r27-ideal-b.json',
               '--after-fix', '145, 148 and 151 reworked after #138 (texts.py IDEAL_B)',
               '--narrowed', 'the section read Mixed in #138; 145, 148 and 151 are checked alone in this batch',
               '--first-fix', 'payoff: 145 says who needs what; plain: quoted speech in 148, "gonna" in 151; join: 148\'s '
                              'flip and its reason; slack ending: 151',
               '--humanized', '145 (the live post\'s), 148 and 151 (r21 to r24)']),
    'r27-p145': dict(
        lineage='romance-low-ideal-p145', scope='paragraph', call='Human', chance=0.5,
        tells='mine in 145, 148 and 151, reworked after #138',
        human='"a knight in shining armor", "you’re perfect" to "you’re a fraud", "gonna", "sometimes too"',
        diag='#138 read 14%% AI: AI Low on 148\'s first two sentences and 151\'s last, Human Low on 145 and 148\'s last. '
             'What was left was mine in neat mirrored shapes and abstract claims, the S2 pattern; his versions fixed that with '
             'particular things, quoted speech and a slack casual ending, so each changed sentence now says who does what.',
        extra=['--receipt', REL + 'RECEIPT-r27-p145.json',
               '--after-fix', '145, 148 and 151 reworked after #138 (texts.py IDEAL_B)',
               '--narrowed', 'the section read Mixed in #138; 145, 148 and 151 are checked alone in this batch',
               '--first-fix', 'payoff: 145 says who needs what; plain: quoted speech in 148, "gonna" in 151; join: 148\'s '
                              'flip and its reason; slack ending: 151',
               '--humanized', '145 (the live post\'s), 148 and 151 (r21 to r24)']),
    'r27-p148': dict(
        lineage='romance-low-ideal-p148', scope='paragraph', call='Human', chance=0.5,
        tells='mine in 145, 148 and 151, reworked after #138',
        human='"a knight in shining armor", "you’re perfect" to "you’re a fraud", "gonna", "sometimes too"',
        diag='#138 read 14%% AI: AI Low on 148\'s first two sentences and 151\'s last, Human Low on 145 and 148\'s last. '
             'What was left was mine in neat mirrored shapes and abstract claims, the S2 pattern; his versions fixed that with '
             'particular things, quoted speech and a slack casual ending, so each changed sentence now says who does what.',
        extra=['--receipt', REL + 'RECEIPT-r27-p148.json',
               '--after-fix', '145, 148 and 151 reworked after #138 (texts.py IDEAL_B)',
               '--narrowed', 'the section read Mixed in #138; 145, 148 and 151 are checked alone in this batch',
               '--first-fix', 'payoff: 145 says who needs what; plain: quoted speech in 148, "gonna" in 151; join: 148\'s '
                              'flip and its reason; slack ending: 151',
               '--humanized', '145 (the live post\'s), 148 and 151 (r21 to r24)']),
    'r27-p151': dict(
        lineage='romance-low-ideal-p151', scope='paragraph', call='Human', chance=0.5,
        tells='mine in 145, 148 and 151, reworked after #138',
        human='"a knight in shining armor", "you’re perfect" to "you’re a fraud", "gonna", "sometimes too"',
        diag='#138 read 14%% AI: AI Low on 148\'s first two sentences and 151\'s last, Human Low on 145 and 148\'s last. '
             'What was left was mine in neat mirrored shapes and abstract claims, the S2 pattern; his versions fixed that with '
             'particular things, quoted speech and a slack casual ending, so each changed sentence now says who does what.',
        extra=['--receipt', REL + 'RECEIPT-r27-p151.json',
               '--after-fix', '145, 148 and 151 reworked after #138 (texts.py IDEAL_B)',
               '--narrowed', 'the section read Mixed in #138; 145, 148 and 151 are checked alone in this batch',
               '--first-fix', 'payoff: 145 says who needs what; plain: quoted speech in 148, "gonna" in 151; join: 148\'s '
                              'flip and its reason; slack ending: 151',
               '--humanized', '145 (the live post\'s), 148 and 151 (r21 to r24)']),
    'r27-ideal-c': dict(
        lineage='romance-low-ideal', scope='section', call='Human', chance=0.6,
        tells='151\'s last sentence, mine, said again',
        human='as #139: "a knight in shining armor", "you’re perfect" to "you’re a fraud", "gonna"',
        diag='#139 read one Human High window; the compare read found 151\'s ending turned his boundary into a demand. '
             'Said as his boundary first, with the reason trailing and no mirrored "on her mind ... on mine", the casual '
             'register that lifted #139 stays.',
        extra=['--receipt', REL + 'RECEIPT-r27-ideal-c.json',
               '--after-fix', '151\'s last sentence after the compare read (compare-r27 F1.4)',
               '--first-fix', 'payoff: 151\'s boundary said first ("I’m not gonna act like they never cross my mind"), its '
                              'reason after; join: none, it is one sentence; plain: "cross my mind" for "pretend ... on '
                              'mine"',
               '--humanized', 'his register kept from #139 ("gonna"), a slack trailing reason ("not when I’m listening to '
                              'everything on hers"), the mirrored shape taken apart']),
    'r27-spir': dict(
        lineage='romance-sec-spiritual-sex', scope='section', call='Human', chance=0.75,
        tells='none: the change takes out a word said twice and a hyphen',
        human='his S17 (Kim Anami, the jade egg, Brad and Pam Keene), Malia and Mouhamed, "should have picked Grok"',
        diag='#118 read one Human High window with "the example couple I really liked as an example"; his correction '
             'takes out one "example" and the noun "pelvic floor" loses its hyphen. A word fewer in one sentence '
             'shouldn\'t move a 742-word High window.',
        extra=['--receipt', REL + 'RECEIPT-r27-spir.json',
               '--unchanged', 'the section as #118 checked it, but for the two words in texts.py EDITS',
               '--after-fix', '"the example couple ... as an example" made "the couple ... as an example" (his '
                              'correction) and "pelvic-floor" made "pelvic floor"']),
}
for key, p in P.items():
    if sys.argv[1:] and key not in sys.argv[1:]:
        continue
    cmd = [sys.executable, str(ROOT / 'tools' / 'humanization' / 'pangram_ledger.py'), 'predict', str(LEDGER),
           '--lineage', p['lineage'], '--scope', p['scope'], '--text', REL + 'CHECK-%s.txt' % key, '--call', p['call'],
           '--chance', str(p['chance']), '--tells', p['tells'], '--human-tells', p['human'], '--diagnosis', p['diag'],
           '--decides', 'whether the %s reads Human with no Low window' % p['scope'], '--key', key, '--batch', 'romance-r27',
           '--detector', DET] + p['extra']
    r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    print(key, r.returncode, (r.stdout + r.stderr).strip()[:1500])
