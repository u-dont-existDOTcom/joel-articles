#!/usr/bin/env python3
"""Turn 110: check and deliver each gated sentence (tools/humanization/owner_delivery_gate.py), once its three reviews are
in, and write GATE-OUTCOMES.json: each candidate's reviewers' verdicts and whether the gate admitted it.

  python3 run_gate.py"""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
GATE = ROOT / 'tools' / 'humanization' / 'owner_delivery_gate.py'
NAMES = ['S1-nurturer', 'S1-watch', 'S1-protective', 'P2', 'P5', 'P6']
res = {}
for n in NAMES:
    d = HERE / n
    files = ['--draft', str(d / 'DRAFT.txt'), '--context', str(d / 'CONTEXT.txt'), '--source', str(d / 'SOURCE.txt'),
             '--manifest', str(d / 'ADMISSION.json')]
    verdicts = {}
    for role in ('preservation', 'cold_read_1', 'cold_read_2'):
        p = d / ('REVIEW-%s.json' % role)
        verdicts[role] = json.loads(p.read_text(encoding='utf-8')).get('verdict') if p.exists() else 'missing'
    out = subprocess.run([sys.executable, str(GATE), 'deliver'] + files + ['--out', str(d / 'FOR-JOEL.txt'),
                          '--proof', str(d / 'FOR-JOEL.proof.json')], capture_output=True, text=True)
    res[n] = {'reviews': verdicts, 'admitted': out.returncode == 0,
              'gate': (out.stdout.strip() or out.stderr.strip())[-1500:].replace(str(HERE) + '/', '')}
    print('%-14s %s %s' % (n, 'ADMITTED' if out.returncode == 0 else 'BLOCKED', verdicts))
    if out.returncode:
        print('   ', out.stderr.strip()[-900:])
(HERE / 'GATE-OUTCOMES.json').write_text(json.dumps(res, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
