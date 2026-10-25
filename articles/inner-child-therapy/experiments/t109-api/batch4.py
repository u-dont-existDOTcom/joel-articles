#!/usr/bin/env python3
"""Turn 109, API batch 4: the third try at Hear the Guard First's P1 and P3 (experiments/t109-installs/reshape_t109c.py),
predictions first. Try 2's P1 read 28% AI as bare instructions; the reason line, which try 1's Human P1 had, follows the
question now, and the reply line stays in P3, where try 2 showed it belongs."""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.argv = [sys.argv[0]]
import make_texts as M  # noqa: E402

ROOT = HERE.parents[3]
LEDGER = ROOT / 'articles/inner-child-therapy/tools/pangram-ledger.jsonl'
BATCH = 't109-api-4'
texts, names, preds = {}, {}, {}


def add(name, text, desc, lineage, scope, chance, diagnosis, tells='none named', human='his words'):
    texts[name], names[name] = text, desc
    preds[name] = (lineage, scope, chance, diagnosis, tells, human)


add('t109_guard_p1c', M.para('Whichever protective part showed up'), 'Hear the Guard First P1, the plain path with its reason (third try), alone',
    't109-guard-plain', 'paragraph', 0.6,
    'try 3: try 1\'s P1 with this reason read Human, try 2\'s without it read 28% AI; the reason now follows the question it explains',
    human='his reason line; his "Peek-a-boo!"')
add('t109_guard_p3c', M.para('That part might say this will just be one more performance'), 'Hear the Guard First P3, his reply after the remembering, without the reason (third try), alone',
    't109-guard-performance', 'paragraph', 0.55,
    'try 3: the reply line is what turned try 1\'s 99.8% AI into try 2\'s Human, and it stays; only the reason line after it moved to P1',
    human='his reply line; his "Even if you didn\'t win an Emmy last year"')

(HERE / 'TEXTS-4.json').write_text(json.dumps(texts, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
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
