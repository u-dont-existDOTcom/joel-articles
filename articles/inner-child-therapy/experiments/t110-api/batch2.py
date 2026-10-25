#!/usr/bin/env python3
"""Turn 110, API batch 2, predictions first: the two agreed candidates as sections (experiments/t110-installs/reshape_t110.py,
on Joel's review page, not installed), now that every changed paragraph of 50 words or more read Human alone (batch 1).

  python3 batch2.py [--dry]"""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import make_texts as M  # noqa: E402

ROOT = HERE.parents[3]
LEDGER = ROOT / 'articles/inner-child-therapy/tools/pangram-ledger.jsonl'
BATCH = 't110-api-2'
C = M.Texts(M.candidate_md())
texts, names, preds = {}, {}, {}


def add(name, text, desc, lineage, scope, chance, diagnosis, decides, tells='none named', human='his words'):
    texts[name], names[name] = text, desc
    preds[name] = (lineage, scope, chance, diagnosis, decides, tells, human)


add('t110_sec_guard', C.h2('Hear the Guard First'),
    'Hear the Guard First as the agreed candidate (S1): his instruction and question, the exchange in his order, the harder voice with the Nurturer voice named, the roommate, move-out, hopes, self-blame',
    't110-sec-guard', 'section', 0.65,
    'try 1: its two long changed paragraphs read Human alone (t110_guard_p2, t110_guard_moveout) and the rest is as it read before; '
    'the risk is the short opening of instructions and the three-sentence harder-voice paragraph, which read AI inside '
    'longer paragraphs of instructions in turn 109 (t109_guard_p1b, t109_guard_p1d)',
    'whether S1 goes on the review page as checked',
    tells='a short opening of instructions; the harder-voice paragraph', human='his reason line; "Peek-a-boo!"; the roommate')
add('t110_sec_hardest', C.h2('Before You Tell the Hardest Stuff'),
    'Before You Tell the Hardest Stuff as the agreed candidate (S3): the topic and his "I\'d assume" first, the danger lines after the dream line',
    't109-sec-hardest', 'section', 0.75,
    'try 2: turn 109\'s order read Human as a section (t109_sec_hardest); this moves only his two danger lines back after the '
    'dream line, and both changed paragraphs read Human alone (t110_hardest_p1, t110_hardest_p5)',
    'whether S3 goes on the review page as checked',
    human='all his words')

(HERE / 'TEXTS-2.json').write_text(json.dumps(texts, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
for n, x in texts.items():
    (HERE / 'texts' / (n + '.txt')).write_text(x, encoding='utf-8')
allnames = json.loads((HERE / 'NAMES.json').read_text(encoding='utf-8'))
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
