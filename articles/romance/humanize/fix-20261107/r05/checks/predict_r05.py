#!/usr/bin/env python3
"""r05's predictions, written before the checks (pangram_ledger.py predict, one per text in texts.py)."""
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[5]
LEDGER = ROOT / 'articles' / 'romance' / 'humanize' / 'pangram-ledger.jsonl'
REL = 'articles/romance/humanize/fix-20261107/r05/checks/'
DET = 'pangram 4.1, the web app (Joel\'s account, GUI credits)'
PANEL = 'articles/romance/humanize/fix-20261107/r03/panel-s2/PANEL.md'
BACK = ('the r02 try rewrote his sentences into new set pieces and read worse than the live post; this try goes back to '
        'the live post\'s words and changes only the sentences in its windows, so most of r02\'s words go')
PB = 'articles/romance/humanize/fix-20261107/'
P = {
    'r05-s2f': dict(lineage='romance-s2', scope='pair', call='AI', chance=0.45,
                    tells='"like in the West" as an aside; three things in the poor-country sentence',
                    human='his "Venerable Somebody", "Why wouldn’t it?", his closing pair; "a guy who was a nobody", "gets to '
                          'be"',
                    diag='Try 4 (#29) read AI Medium on the poor-country and West sentences together (52 words), better than '
                         'AI Medium plus AI High before, with his closing pair AI Low. The two sentences still mirror each '
                         'other ("In a poor country, it’s ... In the West it’s ..."), the pair the first explanation named.',
                    first='payoff: the West case says why it is the second case, the food falling away; join: "And even '
                          'where ..." ties it to the first; plain: "gets to be Venerable Somebody"',
                    hum='the mirrored pair broken: the West case is now where the first reason falls away, not a second '
                        '"In X, it’s"',
                    panel=PB + 'r03/panel-s2/PANEL.md'),
    'r05-s7': dict(lineage='romance-s7', scope='pair', call='Human', chance=0.6,
                   tells='a run of questions',
                   human='his questions; "or just go quiet for an evening", in the either-or of his "or do you keep falling '
                         'for the same stuff"',
                   diag='Try 3 (#34) read Human, with my joined question in a Low window: "Did you stop talking to your '
                        'partner for days, and did they feel abandoned?" (14 words), two questions stuck together with '
                        '"and".',
                   first='payoff: the question shows the range "shut down" can mean; join: the abandoned question stands '
                         'as he wrote it; plain: "go quiet for an evening"',
                   hum='the question asks either-or, the way his judgment question does, and his abandoned question is back '
                       'by itself',
                   panel=PB + 'r04/panel-s7/PANEL.md'),
    'r05-s9': dict(lineage='romance-s9', scope='pair', call='Human', chance=0.6,
                   tells='a closing line that sums up',
                   human='his whole bed paragraph, unchanged; "of all things"',
                   diag='Try 1 (#10) read Human, with my closing line in a Low window: "So a bed ends up carrying way more '
                        'emotional weight than any bed should." (14 words), a tidy summing-up with a repeated "bed".',
                   first='payoff: the line still says what the example shows; join: none; plain: "of all things" marks the '
                         'surprise in his voice, "than it should" drops the second "bed"',
                   hum='the summing-up made into his surprised aside, without the repeated noun'),
    'r05-s10': dict(lineage='romance-s10', scope='pair', call='Human', chance=0.5,
                    tells='"So I’d rather ..." as a takeaway line',
                    human='Toft’s sentence and his reply; his own words for the problem and the answer',
                    diag='Tries 2 and 3 (#19, #35) rebuilt his sentence and read AI Medium to High, worse than the live '
                         'post’s AI Low, even with the panel’s two wordings fixed. His words read better than my rebuilds. '
                         'This try keeps his words and changes only their order: the problem first, then his answer.',
                    first='payoff: the problem leads, so the answer is read as his answer to it; join: the outburst and '
                          'what it sounds like stay in one sentence; plain: his words, "from early on"',
                    hum='his comparison frame ("I’d rather X than wait until Y") turned into the problem, then his answer, '
                        'in his words',
                    big='my two rebuilds read worse than his own words, so this try goes back to his words in a new order, '
                        'which changes most of try 3’s words',
                    panel=PB + 'r04/panel-s10/PANEL.md'),
    'r05-s17': dict(lineage='romance-s17', scope='pair', call='AI', chance=0.45,
                    tells='a list of four in the students’ sentence',
                    human='"a ton of stories"; "even their money"; his jade-egg sentence, unchanged',
                    diag='Tries 1 and 2 (#24, #36) read AI, his jade-egg sentence included. The tell panel (r05/panel-s17) '
                         'agreed on "goes even further" as a stock escalation that adds nothing, on the paired benefits, and '
                         'on the students’ list ending in a catch-all ("the rest of their lives"); it called the voice a '
                         'neutral summarizer.',
                    first='payoff: what she goes further than is said, the suttas just before; join: her view follows a '
                          'colon; plain: "it changed their health, their work, their creativity, even their money"',
                    hum='the escalation says what it goes beyond; the catch-all gone, and the list ends on the surprising '
                        'item with "even"',
                    big='the panel agreed on the wording of both my sentences, so both change; his jade-egg sentence is '
                        'unchanged',
                    panel=PB + 'r05/panel-s17/PANEL.md'),
    'r05-s21': dict(lineage='romance-s21', scope='pair', call='Human', chance=0.5,
                    tells='a closing rhetorical question',
                    human='his Ecclesiastes paragraph and his verses, unchanged; "why swear on top of it"',
                    diag='Tries 1 and 2 (#28, #33) read AI Medium and High on my closing sentences, worse than the live '
                         'post’s two AI Low windows. The tell panel (r05/panel-s21) agreed on my conclusion sentence (a '
                         'syllogism’s conclusion with a "to me" softener) and on his closing question ("another layer", an '
                         'abstract metaphor).',
                    first='payoff: the conclusion says plainly what the verses do to the vow; join: none; plain: "why swear '
                          'on top of it" for "why does it need another layer", the verses’ own word for an oath',
                    hum='the softener gone ("Taken seriously" instead of "to me"); the abstract layer made the oath the '
                        'verses are about',
                    big='both my closing sentences are rebuilt because the panel agreed on both; his paragraph and his '
                        'verses are unchanged',
                    panel=PB + 'r05/panel-s21/PANEL.md'),
}
for key, p in P.items():
    if sys.argv[1:] and key not in sys.argv[1:]:
        continue
    cmd = [sys.executable, str(ROOT / 'tools' / 'humanization' / 'pangram_ledger.py'), 'predict', str(LEDGER),
           '--lineage', p['lineage'], '--scope', p['scope'], '--text', REL + 'CHECK-%s.txt' % key, '--call', p['call'],
           '--chance', str(p['chance']), '--tells', p['tells'], '--human-tells', p['human'], '--diagnosis', p['diag'],
           '--decides', 'whether the %s window reads Human' % p['lineage'].split('-')[1].upper(), '--key', key,
           '--batch', 'romance-r05', '--detector', DET, '--receipt', REL + 'RECEIPT-%s.json' % key,
           '--first-fix', p['first'], '--humanized', p['hum']]
    if p.get('big'):
        cmd += ['--big-change', p['big']]
    if p.get('panel'):
        cmd += ['--panel', PANEL if p['panel'] is True else p['panel']]
    r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    print(key, r.returncode, (r.stdout + r.stderr).strip()[:600])
