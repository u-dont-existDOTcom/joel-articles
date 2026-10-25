#!/usr/bin/env python3
"""Turn 109, API batch 5: the fourth try at Hear the Guard First (experiments/t109-installs/reshape_t109d.py), predictions
first. Its P2 is try 2's P3 word for word (Human alone, t109_guard_p3b), so only the new P1 is checked: the plain path with
the harder-voice case back in it, as his own P1 had it."""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.argv = [sys.argv[0]]
import make_texts as M  # noqa: E402

ROOT = HERE.parents[3]
LEDGER = ROOT / 'articles/inner-child-therapy/tools/pangram-ledger.jsonl'
BATCH = 't109-api-5'
texts, names, preds = {}, {}, {}


def add(name, text, desc, lineage, scope, chance, diagnosis, tells='none named', human='his words'):
    texts[name], names[name] = text, desc
    preds[name] = (lineage, scope, chance, diagnosis, tells, human)


add('t109_guard_p1d', M.para('Whichever protective part showed up'), 'Hear the Guard First P1, the plain path with the harder-voice case back in it (fourth try), alone',
    't109-guard-plain', 'paragraph', 0.6,
    'try 4: the plain path read Human only when it held more than instructions (tries 1 and 3, with his reason line); his own P1 held the harder-voice case and read Human, and now this one does',
    human='his "Peek-a-boo!"; "I\'d still keep it the same."')

(HERE / 'TEXTS-5.json').write_text(json.dumps(texts, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
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
