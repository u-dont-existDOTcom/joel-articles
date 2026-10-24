#!/usr/bin/env python3
"""Turn 106, API batch 2: three checks of the text as it was before two of his cuts, to see whether a cut caused what batch 1
showed. Timing Is Individual read 51% AI with its windows on P2 once "Timing is different for everyone, but" was cut
from P1 (he had added that line in turn 67 as "a marching order break"); My Journey's bypassing paragraph read AI alone
once "It doesn't mean you're stupid or crazy." was cut, though the section shows no AI window."""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.argv = [sys.argv[0]]
import make_texts as M  # noqa: E402

ROOT = HERE.parents[3]
LEDGER = ROOT / 'articles/inner-child-therapy/tools/pangram-ledger.jsonl'
texts, names, preds = {}, {}, {}
t = M.h2('Timing Is Individual')
a, b = 'Most of us need enough Nurturer and Protector first.', M.smart('Timing is different for everyone, but most of us need enough Nurturer and Protector first.')
assert t.count(a) == 1
texts['t106_timing_before'] = t.replace(a, b)
names['t106_timing_before'] = 'Timing Is Individual as it was before H32, with his "Timing is different for everyone, but"'
preds['t106_timing_before'] = ('t106-sec-timing', 'section', 'Human', 0.6, 'his line was the march break he added in turn 67 to pass; with it cut, the windows moved onto P2, so with it back P2 should read Human again')
p = M.para('I think most people who chase spiritual freedom')
extra = ' ' + M.smart("It doesn't mean you're stupid or crazy.")
texts['t106_h3_journey_before'] = p + extra
names['t106_h3_journey_before'] = 'My Journey\'s bypassing paragraph as it was before H3, alone'
preds['t106_h3_journey_before'] = ('t106-h3-journey', 'paragraph', 'AI', 0.4, 'the AI window covers the whole paragraph, from its first sentence, which the cut left alone, so I expect it read AI alone before too')
s = M.h2('My Journey')
q = M.smart("I did it too.")
assert s.count(q) == 1
texts['t106_sec_journey_before'] = s.replace(q, q + extra)
names['t106_sec_journey_before'] = 'My Journey\'s h1 part as it was before H3'
preds['t106_sec_journey_before'] = ('t106-sec-journey', 'section', 'Human', 0.5, 'the section after the cut read 0.26% AI with no AI window; before it, the same or a little lower')
(HERE / 'TEXTS-2.json').write_text(json.dumps(texts, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
for n, x in texts.items():
    (HERE / 'texts' / (n + '.txt')).write_text(x, encoding='utf-8')
allnames = json.loads((HERE / 'NAMES.json').read_text(encoding='utf-8'))
allnames.update(names)
(HERE / 'NAMES.json').write_text(json.dumps(allnames, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
for n, (lin, scope, call, chance, diag) in preds.items():
    cmd = [sys.executable, str(ROOT / 'tools/humanization/pangram_ledger.py'), 'predict', str(LEDGER), '--lineage', lin, '--scope', scope,
           '--text', str(HERE / 'texts' / (n + '.txt')), '--call', call, '--chance', str(chance), '--tells', 'none named',
           '--human-tells', 'his words', '--diagnosis', diag, '--decides', 'whether his cut caused it', '--key', n, '--batch', 't106-api-2']
    out = subprocess.run(cmd, capture_output=True, text=True)
    if out.returncode:
        sys.exit(out.stdout + out.stderr)
    print(out.stdout.strip().split('\n')[-1])
