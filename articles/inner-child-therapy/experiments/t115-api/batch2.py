#!/usr/bin/env python3
"""Turn 115, API batch 2, prediction first: Love Doesn't Have to Wait for Trust with F03's second try (experiments/t115-pass/
fixes.py), after try 1's check (t115_lovewait) read P7's "You don't have to accept every conclusion ..., but do listen ..."
Human, Low. The second and last try for that section in this lineage (pangram_ledger.py counts it).

  python3 batch2.py [--dry]"""
import json
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
LEDGER = ROOT / 'articles/inner-child-therapy/tools/pangram-ledger.jsonl'
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
from paragraphs_alone import reader_blocks, plain  # noqa: E402
from substack_check_text import smart  # noqa: E402

CAND = (HERE.parent / 't115-pass' / 'CANDIDATE-ARTICLE.md').read_text(encoding='utf-8')
seq = reader_blocks(re.sub(r'<!--.*?-->', '', CAND, flags=re.S))


def line(kind, b):
    t = plain(re.sub(r'^#+\s*', '', b) if kind == 'h' else b)
    return smart(t).replace('‍', '').replace('️', '')


HEAD = "Love Doesn't Have to Wait for Trust ❤️"
i = [n for n, (k, b) in enumerate(seq) if k == 'h' and re.sub(r'^#+\s*', '', b) == HEAD][0]
out = [line(*seq[i])]
for k, b in seq[i + 1:]:
    if k == 'h':
        break
    out.append(line(k, b))
name = 't115_lovewait_r2'
texts = {name: '\n'.join(out)}
assert 'Your little one might say it’s you. Listen for the concrete complaint' in texts[name]
(HERE / 'TEXTS-2.json').write_text(json.dumps(texts, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
(HERE / 'texts' / (name + '.txt')).write_text(texts[name], encoding='utf-8')
names = json.loads((HERE / 'NAMES.json').read_text(encoding='utf-8'))
names['names'][name] = HEAD + ', with F03 (second try)'
names['fixes'][name] = ['F03']
(HERE / 'NAMES.json').write_text(json.dumps(names, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
print(name, len(texts[name].split()), 'words')
if '--dry' in sys.argv:
    sys.exit(0)
cmd = [sys.executable, str(ROOT / 'tools/humanization/pangram_ledger.py'), 'predict', str(LEDGER), '--lineage', 'ic-t115-lovewait',
       '--scope', 'section', '--text', str(HERE / 'texts' / (name + '.txt')), '--call', 'Human', '--chance', '0.55',
       '--tells', 'none named after the change', '--human-tells', 'his bedtime story; the Mr. Rogers scene',
       '--diagnosis', 'try 2 for P7: try 1 left its permission sentence ("You don\'t have to accept every conclusion they reach about '
       'you, but do listen ...") Human, Low (27 words); the "You don\'t have to X, but do Y" packaging is the tell, so its permission '
       'clause is cut too (the Mr. Rogers scene shows it: "He doesn\'t collapse under that or fight it"). Target: no Low or AI window on P7',
       '--decides', 'whether F03 goes to him as a fix that reads Human, high in its block', '--key', name, '--batch', 't115-api-2']
r = subprocess.run(cmd, capture_output=True, text=True)
if r.returncode:
    sys.exit(r.stdout + r.stderr)
print(r.stdout.strip().split('\n')[-1])
