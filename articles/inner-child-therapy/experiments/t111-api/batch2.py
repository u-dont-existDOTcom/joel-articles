#!/usr/bin/env python3
"""Turn 111, API batch 2, predictions first: the two paragraphs that read AI alone after his approved cuts (t111_c4_borrowlove,
t111_c8_belonging), as they were before the cut, alone, to tell whether the cut did it. In round 6, the whole article, both
read Human in context (experiments/t109-windows/WINDOWS.json has only Medium windows on them).

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
BATCH = 't111-api-2'
B = M.Texts(pathlib.Path('/tmp/claude-0/-home-claude/d17e637c-ae79-5296-a30e-05fa0a73af9d/scratchpad/article-before-t111.md').read_text(encoding='utf-8'))
texts, names, preds = {}, {}, {}
texts['t111_c4_before'] = B.para('Or put somebody you care about')
names['t111_c4_before'] = 'Borrow Love P3 as it was before his approved cut (C4), alone'
preds['t111_c4_before'] = ('t111-borrowlove', 0.5, 'try 2: the same paragraph with the life\'s-journey line back; if it reads Human, that line was what carried it alone and the cut did it; if AI, the paragraph read AI alone anyway and Human only in context (round 6)')
texts['t111_c8_before'] = B.para('Part of building who you are')
names['t111_c8_before'] = 'Untangling the Belonging Bargains P1 as it was before his approved cut (C8), alone'
preds['t111_c8_before'] = ('t111-belonging', 0.3, 'try 2: the same paragraph with ", which is ordinary" back; a tag that small rarely carries a 141-word paragraph, so I expect AI: the paragraph reads AI alone anyway (a run of instructions) and Human only in context (round 6)')
assert texts['t111_c4_before'] != M.Texts(M.ART.read_text(encoding='utf-8')).para('Or put somebody you care about')
(HERE / 'TEXTS-2.json').write_text(json.dumps(texts, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
for n, x in texts.items():
    (HERE / 'texts' / (n + '.txt')).write_text(x, encoding='utf-8')
allnames = json.loads((HERE / 'NAMES.json').read_text(encoding='utf-8'))
allnames.update(names)
(HERE / 'NAMES.json').write_text(json.dumps(allnames, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
if '--dry' in sys.argv:
    sys.exit(0)
for n, (lin, chance, diag) in preds.items():
    call = 'Human' if chance >= 0.5 else 'AI'
    cmd = [sys.executable, str(ROOT / 'tools/humanization/pangram_ledger.py'), 'predict', str(LEDGER), '--lineage', lin, '--scope', 'paragraph',
           '--text', str(HERE / 'texts' / (n + '.txt')), '--call', call, '--chance', str(chance), '--tells', 'a run of instructions',
           '--human-tells', 'none named', '--diagnosis', diag, '--decides', 'whether his approved cut caused the AI result alone', '--key', n,
           '--batch', BATCH]
    out = subprocess.run(cmd, capture_output=True, text=True)
    if out.returncode:
        sys.exit(out.stdout + out.stderr)
    print(out.stdout.strip().split('\n')[-1])
