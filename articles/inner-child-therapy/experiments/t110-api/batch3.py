#!/usr/bin/env python3
"""Turn 110, API batch 3, predictions first: Hear the Guard First's candidate after the cold read's two fixes ("call it all
off"; "a protective job"; experiments/t110-review/COLD-READ.md), each changed paragraph of 50 words or more alone, then the
section, its second and last section try.

  python3 batch3.py [--dry]"""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import make_texts as M  # noqa: E402

ROOT = HERE.parents[3]
LEDGER = ROOT / 'articles/inner-child-therapy/tools/pangram-ledger.jsonl'
BATCH = 't110-api-3'
C = M.Texts(M.candidate_md())
texts, names, preds = {}, {}, {}


def add(name, text, desc, lineage, scope, chance, diagnosis, decides, tells='none named', human='his words'):
    texts[name], names[name] = text, desc
    preds[name] = (lineage, scope, chance, diagnosis, decides, tells, human)


add('t110_guard_moveout_b', C.para("That part doesn't have to move out"),
    'Hear the Guard First, the move-out paragraph split in two and with "call it all off", alone',
    't109-guard-moveout', 'paragraph', 0.8,
    'try 3: t110_guard_moveout (Human, one High window) with one word added, "all", so "it" can\'t be read as the guard; '
    'a one-word change inside a High window',
    'whether the cold read\'s fix goes into S1',
    human='"way longer than the grown-up you"; the blinds tilted open a crack; "If it says no, I\'d listen."')
add('t110_guard_blame', C.para('Blaming yourself can be doing a protective job'),
    'Hear the Guard First, the self-blame paragraph with "a protective job" for "a job like that", alone',
    't110-guard-blame', 'paragraph', 0.6,
    'try 1: the turn-90 paragraph with "a job like that" made "a protective job", as GPT asked; its other four sentences '
    'are as they read inside the section (t110_sec_guard, one Low window on its last sentence)',
    'whether the cold read\'s fix goes into S1',
    tells='a short paragraph of judgments', human='"word for word"; "I\'d stop the cruelty either way."')
add('t110_sec_guard_b', C.h2('Hear the Guard First'),
    'Hear the Guard First as the agreed candidate (S1) with the cold read\'s two fixes',
    't110-sec-guard', 'section', 0.65,
    'try 2 of 2: t110_sec_guard read Human (15 windows, none AI); the only changes are "all" and "protective job", both in '
    'paragraphs checked alone just before this',
    'whether S1 goes on the review page with the two fixes',
    human='his reason line; "Peek-a-boo!"; the roommate')

(HERE / 'TEXTS-3.json').write_text(json.dumps(texts, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
for n, x in texts.items():
    (HERE / 'texts' / (n + '.txt')).write_text(x, encoding='utf-8')
allnames = json.loads((HERE / 'NAMES.json').read_text(encoding='utf-8'))
allnames.update(names)
(HERE / 'NAMES.json').write_text(json.dumps(allnames, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
for n, x in texts.items():
    print('%-22s %4d words | %s' % (n, len(x.split()), x[:90].replace('\n', ' / ')))
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
