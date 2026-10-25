#!/usr/bin/env python3
"""Turn 109, API batch 3: the second tries (experiments/t109-installs/reshape_t109b.py) at the two reshaped paragraphs
that read AI alone in batches 1 and 2, predictions first. Hear the Guard First P3 has his reply back after the remembering
it answers, and P1 is the plain path without it (51 words, so it is checked alone too). Start With Whatever Showed Up's
second try leaves no new paragraph of 50 words or more unchecked (his P1 is whole again; his "If nothing comes" read Human
alone in batch 2), so it waits for its section check."""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.argv = [sys.argv[0]]
import make_texts as M  # noqa: E402

ROOT = HERE.parents[3]
LEDGER = ROOT / 'articles/inner-child-therapy/tools/pangram-ledger.jsonl'
BATCH = 't109-api-3'
texts, names, preds = {}, {}, {}


def add(name, text, desc, lineage, scope, chance, diagnosis, tells='none named', human='his words'):
    texts[name], names[name] = text, desc
    preds[name] = (lineage, scope, chance, diagnosis, tells, human)


add('t109_guard_p1b', M.para('Whichever protective part showed up'), 'Hear the Guard First P1, the plain path without his reply line (second try), alone',
    't109-guard-plain', 'paragraph', 0.55,
    'try 2 of the plain path: the reply line and its reason went back to P3, so P1 is two instructions and his two lines about the little one coming forward',
    tells='two instructions in a row', human='his "Peek-a-boo!"')
add('t109_guard_p3b', M.para('That part might say this will just be one more performance'), 'Hear the Guard First P3, the performance paragraph with his reply back (second try), alone',
    't109-guard-performance', 'paragraph', 0.6,
    'try 2: P3 read 99.8% AI as a chain of worries with no reply in it; his reply "Tell me what you remember, I\'m listening." and its reason are back after "that part remembers", in his own order, which read Human as his P2',
    human='his reply line; his "Even if you didn\'t win an Emmy last year"')

(HERE / 'TEXTS-3.json').write_text(json.dumps(texts, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
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
