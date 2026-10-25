#!/usr/bin/env python3
"""Turn 109, API batch 2: the first checks of the two sections reshaped by experiments/t109-installs/reshape_t109.py
(104 A, the plain path first, every sentence word for word), each new paragraph of 50 words or more alone and then the
section, the predictions written to the ledger first. Paragraphs that kept their sentences and order (Start With's old P2,
P5, P6 and P7) aren't checked alone again."""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.argv = [sys.argv[0]]
import make_texts as M  # noqa: E402

ROOT = HERE.parents[3]
LEDGER = ROOT / 'articles/inner-child-therapy/tools/pangram-ledger.jsonl'
BATCH = 't109-api-2'
texts, names, preds = {}, {}, {}


def add(name, text, desc, lineage, scope, chance, diagnosis, tells='none named', human='his words'):
    texts[name], names[name] = text, desc
    preds[name] = (lineage, scope, chance, diagnosis, tells, human)


add('t109_start_p1', M.para('You might go looking for your little one'), 'Start With Whatever Showed Up P1, the plain path (his P1 start and his P4 line), alone',
    't109-start-plain', 'paragraph', 0.65,
    'all eight sentences are his (his P1 fix of turn 21 and his P4 of turn 23), now in one paragraph; his quoted line breaks up any march',
    human='his "pl/ork"; his quoted line to the part; "Or however you\'d actually say that."')
add('t109_start_p2', M.para('Maybe it just has something to say'), 'Start With Whatever Showed Up P2, who it might be, alone',
    't109-start-who', 'paragraph', 0.55,
    'his three sentences of who it could be, then writer b\'s three about not spending long naming parts (they read Human as his P3 before)',
    tells='"I wouldn\'t spend long deciding what to call each part, though."')
add('t109_start_p4', M.para('If nothing comes, that'), 'Start With Whatever Showed Up P4, if nothing comes, alone',
    't109-start-nothing', 'paragraph', 0.6,
    'his three sentences, the end of his old P4, now their own paragraph before his "Or if you do get an answer"')
# Start With Whatever Showed Up's section check waits: the point-of-view read flagged its hesitation paragraph's "I'd stop there and not test it", and my pick there changes the section, so it is checked once he has decided.
# add('t109_sec_start', M.h2('Start With Whatever Showed Up'), 'Start With Whatever Showed Up, its own seven paragraphs in the new shape',
#     't109-sec-start', 'section', 0.5,
#     'the same sentences read Human in round 6\'s half A; only the order and the breaks changed')
add('t109_hardest_p1', M.para('Then there’s the stuff that’s hardest to tell anyone'), 'Before You Tell the Hardest Stuff P1, what to do first, alone',
    't109-hardest-plain', 'paragraph', 0.6,
    'five of his sentences, his topic lines and his "I\'d assume" and danger lines, side by side now',
    human='his "I\'d assume"; his "whatever it costs you legally"')
add('t109_hardest_p3', M.para('And some of the people you’d tell'), 'Before You Tell the Hardest Stuff P3, who has to report, alone',
    't109-hardest-report', 'paragraph', 0.65,
    'his three sentences, the end of his old P1', human='his "even if they pretend to care"')
add('t109_sec_hardest', M.h2('Before You Tell the Hardest Stuff'), 'Before You Tell the Hardest Stuff, the whole section in its new shape',
    't109-sec-hardest', 'section', 0.55,
    'his own text throughout; round 6 read it Human in half B, with two Medium windows; only the order and breaks changed')

(HERE / 'TEXTS-2.json').write_text(json.dumps(texts, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
(HERE / 'texts').mkdir(exist_ok=True)
for n, x in texts.items():
    (HERE / 'texts' / (n + '.txt')).write_text(x, encoding='utf-8')
allnames = json.loads((HERE / 'NAMES.json').read_text(encoding='utf-8')) if (HERE / 'NAMES.json').exists() else {}
allnames.update(names)
(HERE / 'NAMES.json').write_text(json.dumps(allnames, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
if '--dry' in sys.argv or '--dry' in sys.orig_argv:
    for n, x in texts.items():
        print('%-18s %4d words | %s' % (n, len(x.split()), x[:90].replace('\n', ' / ')))
    sys.exit(0)
for n, (lin, scope, chance, diag, tells, human) in preds.items():
    cmd = [sys.executable, str(ROOT / 'tools/humanization/pangram_ledger.py'), 'predict', str(LEDGER), '--lineage', lin, '--scope', scope,
           '--text', str(HERE / 'texts' / (n + '.txt')), '--call', 'Human', '--chance', str(chance), '--tells', tells,
           '--human-tells', human, '--diagnosis', diag, '--decides', 'whether the turn-109 install stays as it is', '--key', n,
           '--batch', BATCH]
    out = subprocess.run(cmd, capture_output=True, text=True)
    if out.returncode:
        sys.exit(out.stdout + out.stderr)
    print(out.stdout.strip().split('\n')[-1])
