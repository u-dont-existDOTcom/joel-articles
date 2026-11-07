#!/usr/bin/env python3
"""r18's predictions, written before the checks; each text was linted first (gate bad-trips-2026-11-07h)."""
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[5]
LEDGER = ROOT / 'articles' / 'romance' / 'humanize' / 'pangram-ledger.jsonl'
REL = 'articles/romance/humanize/fix-20261107/r18/checks/'
DET = 'pangram 4.1, the web app (Joel\'s account, GUI credits)'
P = {
    'r18-choosing': dict(lineage='romance-low-choosing', scope='section', call='Human', chance=0.5,
                         tells='a run of questions, "There’s nothing inherently wrong with that arrangement"',
                         human='"two lovey bunnies", "low-key pretending", "And the biggie", "make a card game out of '
                               'this"',
                         diag='The first try (#103) read Human with three Low windows, all on S20’s questions, each read '
                              'as a window of its own: "Then the questions change for me." (6 words), "Are we promising '
                              'actions, or low-key pretending to promise permanent feelings?" (12) and "If our lives '
                              'change, can we honestly sit down and rethink the agreement?" (13). This try joins the '
                              'opener to the first question with a colon, leaves the either/or question a little '
                              'unbalanced in brackets (bad-trips-2026-11-07g), and joins the rethink question to the '
                              'split-up one, so the run has fewer, longer questions.',
                         first='payoff: unchanged, his order; join: the opener to its first question with a colon, the '
                               'rethink question to the split-up one with and; plain: his words, the kids put in brackets',
                         hum='his questions joined, one left a little unbalanced', extra=[]),
    'r18-convo': dict(lineage='romance-low-convo', scope='section', call='Human', chance=0.55,
                      tells='a run of questions ("What addictions ...? How dependable are we? What are we probably going '
                            'to ask forgiveness for ...?")',
                      human='"That would be a pretty weird date.", "falling for the same stuff", "okay, what does that '
                            'mean"',
                      diag='S7 read Human by itself (#34) with one Low window, its last question "Did you stop talking to '
                           'your partner for days, and did they feel abandoned?" (14 words); the section has never been '
                           'checked whole. This first check puts S7 in as #34 read, its closing question joined to the '
                           'one before with a colon and his "okay" kept from the live post.',
                      first='payoff: unchanged, his order; join: the closing question to the one before with a colon; '
                            'plain: his "okay" kept',
                      hum='his closing questions joined, with his "okay"', extra=[]),
    'r18-nitty': dict(lineage='romance-low-nitty', scope='section', call='Human', chance=0.55,
                      tells='a list of four ("mind-read, notice every emotional shift, check in constantly, and '
                            'understand what a silence means")',
                      human='"10% autistic", "all that expert “management.”", "I can make my bed whenever I want"',
                      diag='S9 read Human by itself (#10) with one Low window, its closing summary line as a paragraph '
                           'of its own ("So a bed ends up carrying way more emotional weight than any bed should.", 14 '
                           'words); the live post’s "A tiny thing can end up carrying ..." read AI Low. This first check '
                           'of the section says that point once, at the end of the bed paragraph, as what the bed '
                           'carries ("which is a lot of emotional weight for a bed").',
                      first='payoff: the bed’s weight said in the sentence it follows from; join: the summary line into '
                            'the bed paragraph’s last sentence with which; plain: "a lot of emotional weight for a bed" '
                            'for "way more emotional weight than it should"',
                      hum='his summary line said once, inside the example it sums up', extra=[]),
    'r18-vows': dict(lineage='romance-sec-vows', scope='section', call='Human', chance=0.5,
                     tells='"We also find something like my warning", "the passage warns that God will be angry"',
                     human='"tell the priest", "like a snowball", "feelings aren’t contractual"',
                     diag='The section read 8.9% AI (#46) with one AI High window, S21’s closing: "To me, the extra '
                          'promise itself starts to look suspicious: if your yes is trustworthy, why does it need another '
                          'layer?" (21 words). Four tries of S21 as a pair read AI (#28, #33, #43, #49), his verses '
                          'included, and the tell panel (r05/panel-s21) agreed on the closing’s syllogism, its "to me" '
                          'softener and its neat question. This try drops the closing as a sentence of its own and says '
                          'it first, in the verse sentence: the verses "make the wedding vow itself look even more '
                          'suspicious (to me, anyway)", the hedge left in brackets and the verse itself giving the '
                          'reason.',
                     first='payoff: what the verses do to the wedding vow said before the verse; join: the closing into '
                           'the verse sentence, before its colon; plain: "even more suspicious" for "stranger still", the '
                           'question cut since the verse says it',
                     hum='his conclusion said first with his hedge in brackets, and the neat question cut',
                     extra=['--narrowed', 'romance-s21 (#49, 350 with 351 as a pair, read after #46: AI on the verse '
                                          'sentence with its closing joined, which the section had read as its one AI '
                                          'window; 351 alone is under the web app’s 50 words)']),
    'r18-loss': dict(lineage='romance-low-loss', scope='section', call='Human', chance=0.6,
                     tells='"Relationships are a process of growth in many dimensions.", "The dominant culture '
                           'hermetically seals two people together"',
                     human='"(Just kidding, click here!)", "the Rosenblum sex talk", "first, second, third, fourth, and '
                           'fifth marriages!"',
                     diag='The last part’s check (#47) read this section as one Human High window except 443’s "Loss '
                          'taught me things love alone never would." (Human Low, 8 words), a short line between his '
                          'opening and the Rumi line it goes with. This first check of the section joins it to the Rumi '
                          'line with "or".',
                     first='payoff: unchanged, his order; join: 443’s short line to the Rumi line with or; plain: his '
                           'words',
                     hum='his short line joined to the line it goes with', extra=[]),
}
for key, p in P.items():
    if sys.argv[1:] and key not in sys.argv[1:]:
        continue
    cmd = [sys.executable, str(ROOT / 'tools' / 'humanization' / 'pangram_ledger.py'), 'predict', str(LEDGER),
           '--lineage', p['lineage'], '--scope', p['scope'], '--text', REL + 'CHECK-%s.txt' % key, '--call', p['call'],
           '--chance', str(p['chance']), '--tells', p['tells'], '--human-tells', p['human'], '--diagnosis', p['diag'],
           '--decides', 'whether the %s reads Human with no Low window' % p['scope'], '--key', key, '--batch', 'romance-r18',
           '--detector', DET, '--receipt', REL + 'RECEIPT-%s.json' % key, '--first-fix', p['first'], '--humanized', p['hum']] \
          + p['extra']
    r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    print(key, r.returncode, (r.stdout + r.stderr).strip()[:700])
