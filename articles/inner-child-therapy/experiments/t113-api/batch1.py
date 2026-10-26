#!/usr/bin/env python3
"""NOT RUN in turn 113: Joel said the drafts can wait for the big edits ("no point checking the drafts at this point, we are
about to make major edits"), so the check runs on what he approves after GPT's review. Before running it, rebuild its
inputs from the version he approves and write new predictions for that version; numbers written here are from an earlier round.

Turn 113, API batch 1, prediction first: Borrow Love's third paragraph with his 109 A ("the blind spot behind it even has
a name"), alone, as the review sheet offers it. His own version passed in his check ("this version passes", 2026-10-25
21:40 UTC); the five words are mine and passed the owner-delivery gate (experiments/t113-gate/solomon/). The rest of the
turn's proposals are many paragraphs, so they go through the free Substack check in context (E200), not here.

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
BATCH = 't113-api-1'
P = M.Texts(M.candidate_md())
texts = {'t113_solomon': P.para('Or put somebody you care about')}
names = {'t113_solomon': "Borrow Love P3 with his 109 A (the name on the gap), alone"}
assert 'the blind spot behind it even has a name' in texts['t113_solomon']
preds = {'t113_solomon': ('t111-borrowlove', 0.55, 'try 3 of the lineage (try 1 the approved cut alone, AI; try 2 the line back, Human; his own version passed in his check): his version with five words of mine that name the gap; a small concrete change inside his own sentence, so I expect Human')}
(HERE / 'TEXTS-1.json').write_text(json.dumps(texts, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
for n, x in texts.items():
    (HERE / 'texts' / (n + '.txt')).write_text(x, encoding='utf-8')
(HERE / 'NAMES.json').write_text(json.dumps(names, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
if '--dry' in sys.argv:
    print(texts['t113_solomon'])
    sys.exit(0)
for n, (lin, chance, diag) in preds.items():
    call = 'Human' if chance >= 0.5 else 'AI'
    cmd = [sys.executable, str(ROOT / 'tools/humanization/pangram_ledger.py'), 'predict', str(LEDGER), '--lineage', lin, '--scope', 'paragraph',
           '--text', str(HERE / 'texts' / (n + '.txt')), '--call', call, '--chance', str(chance), '--tells', 'none named',
           '--human-tells', 'his own sentence and his king', '--diagnosis', diag, '--decides', 'whether the 109 A wording keeps the paragraph Human alone', '--key', n,
           '--batch', BATCH]
    out = subprocess.run(cmd, capture_output=True, text=True)
    if out.returncode:
        sys.exit(out.stdout + out.stderr)
    print(out.stdout.strip().split('\n')[-1])
