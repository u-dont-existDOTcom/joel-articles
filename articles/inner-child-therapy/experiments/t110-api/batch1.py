#!/usr/bin/env python3
"""Turn 110, API batch 1, predictions first: the paragraphs of 50 words or more that the two agreed candidates change
(experiments/t110-installs/reshape_t110.py, on Joel's review page, not installed), each alone, and Start With Whatever
Showed Up as a section, its check held in turn 109 until the point-of-view decisions, which both reviews now leave as it
is. The candidates' sections come in batch 2, once these are in.

  python3 batch1.py [--dry]"""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import make_texts as M  # noqa: E402

ROOT = HERE.parents[3]
LEDGER = ROOT / 'articles/inner-child-therapy/tools/pangram-ledger.jsonl'
BATCH = 't110-api-1'
C = M.Texts(M.candidate_md())
I = M.Texts(M.ART.read_text(encoding='utf-8'))
texts, names, preds = {}, {}, {}


def add(name, text, desc, lineage, scope, chance, diagnosis, decides, tells='none named', human='his words'):
    texts[name], names[name] = text, desc
    preds[name] = (lineage, scope, chance, diagnosis, decides, tells, human)


add('t110_guard_p2', C.para('It might say this will just be one more performance'),
    'Hear the Guard First P2 of the agreed candidate (S1): the exchange in his own order from before turn 109, alone',
    't109-guard-performance', 'paragraph', 0.75,
    'try 4: his own order from before turn 109 (his "It might say", the sting, the remembering, his reply and his reason, '
    'his little one and "Peek-a-boo!", then pushing past and the Emmy); every try with his reason line read Human (t109_guard_p1, '
    'p1c, p3b) and every try without it read 28% to 99.8% AI, and this one has it',
    'whether S1 goes on the review page as checked',
    human='his reason line; "Peek-a-boo!"; the Emmy line')
add('t110_guard_moveout', C.para("That part doesn't have to move out"),
    'Hear the Guard First, the move-out paragraph with its long sentence split in two (GPT\'s readability fix), alone',
    't109-guard-moveout', 'paragraph', 0.8,
    'try 2: the same words as t109_guard_p4 (Human alone), with ", and I think" made ". I think", the readability fix both '
    'reviews agree on; a full stop between his permission to watch and its reason should not change how it reads',
    'whether S1 goes on the review page as checked',
    human='"way longer than the grown-up you"; the blinds tilted open a crack; "If it says no, I\'d listen."')
add('t110_hardest_p1', C.para('Then there’s the stuff that’s hardest to tell anyone'),
    'Before You Tell the Hardest Stuff P1 of the agreed candidate (S3): the topic and his "I\'d assume", alone',
    't109-hardest-plain', 'paragraph', 0.6,
    'try 2: his three sentences without the danger lines, which go back after the dream line they limit (GPT\'s S3 advice); '
    'with them it read Human (t109_hardest_p1), and the three are his own words, his "of course that\'s exactly what you need '
    'help with" and his "I\'d assume"',
    'whether S3 goes on the review page as checked',
    human='"and of course that\'s exactly what you need help with"; "I\'d assume"')
add('t110_hardest_p5', C.para('You can always rephrase things as a dream narrative'),
    'Before You Tell the Hardest Stuff P5 of the agreed candidate (S3): his dream line with his two danger lines after it, alone',
    't110-hardest-dream', 'paragraph', 0.75,
    'try 1: his dream line and the two danger lines after it, as he wrote them on 2026-10-19; the danger lines read Human '
    'inside t109_hardest_p1, and his TalkSpace aside is his own',
    'whether S3 goes on the review page as checked',
    human='his TalkSpace aside; "whatever it costs you legally"')
add('t110_sec_start', I.h2('Start With Whatever Showed Up'),
    'Start With Whatever Showed Up, the whole section as turn 109 installed it (the second try)',
    't110-sec-start', 'section', 0.6,
    'try 1: his P1 whole (the first try\'s P1 without his "Maybe it just has something to say" read 99.8% AI), and its '
    'other paragraphs as they were, two of them Human alone (t109_start_p2, t109_start_p4)',
    'whether the second try stays as it is',
    human='his P1; his "If nothing comes"; his "Or if you do get an answer"')

(HERE / 'TEXTS-1.json').write_text(json.dumps(texts, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
(HERE / 'texts').mkdir(exist_ok=True)
for n, x in texts.items():
    (HERE / 'texts' / (n + '.txt')).write_text(x, encoding='utf-8')
allnames = json.loads((HERE / 'NAMES.json').read_text(encoding='utf-8')) if (HERE / 'NAMES.json').exists() else {}
allnames.update(names)
(HERE / 'NAMES.json').write_text(json.dumps(allnames, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
for n, x in texts.items():
    print('%-20s %4d words | %s' % (n, len(x.split()), x[:90].replace('\n', ' / ')))
if '--dry' in sys.argv:
    sys.exit(0)
for n, (lin, scope, chance, diag, decides, tells, human) in preds.items():
    cmd = [sys.executable, str(ROOT / 'tools/humanization/pangram_ledger.py'), 'predict', str(LEDGER), '--lineage', lin, '--scope', scope,
           '--text', str(HERE / 'texts' / (n + '.txt')), '--call', 'Human', '--chance', str(chance), '--tells', tells,
           '--human-tells', human, '--diagnosis', diag, '--decides', decides, '--key', n, '--batch', BATCH]
    out = subprocess.run(cmd, capture_output=True, text=True)
    if out.returncode:
        sys.exit(out.stdout + out.stderr)
    print(out.stdout.strip().split('\n')[-1])
