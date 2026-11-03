#!/usr/bin/env python3
"""Turn 115: check and deliver each reworded paragraph of the pass (tools/humanization/owner_delivery_gate.py) once its three
reviews are in, and write GATE-OUTCOMES.json: each item's reviewers' verdicts and whether the gate admitted it, with the
cuts' reviews (CUTS-REVIEW-<role>.json). Adapted from experiments/t113-gate/run_gate.py.

  python3 run_gate.py"""
import hashlib
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
GATE = ROOT / 'tools' / 'humanization' / 'owner_delivery_gate.py'
NAMES = ['F02', 'F04', 'F05', 'F06', 'F10']
ROLES = ('preservation', 'cold_read_1', 'cold_read_2')
res = {'gated': {}, 'cuts': {}}


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


for n in NAMES:
    d = HERE / n
    files = ['--draft', str(d / 'DRAFT.txt'), '--context', str(d / 'CONTEXT.txt'), '--source', str(d / 'SOURCE.txt'),
             '--manifest', str(d / 'ADMISSION.json')]
    verdicts = {}
    for role in ROLES:
        p = d / ('REVIEW-%s.json' % role)
        verdicts[role] = json.loads(p.read_text(encoding='utf-8')).get('verdict') if p.exists() else 'missing'
    proof = d / 'FOR-JOEL.proof.json'
    if proof.exists() and (d / 'FOR-JOEL.txt').exists():
        pr = json.loads(proof.read_text(encoding='utf-8'))
        same = (pr['manifest_sha256'] == sha(d / 'ADMISSION.json') and pr['candidate_sha256'] == sha(d / 'DRAFT.txt')
                and pr['context_sha256'] == sha(d / 'CONTEXT.txt') and (d / 'FOR-JOEL.txt').read_bytes() == (d / 'DRAFT.txt').read_bytes())
        res['gated'][n] = {'reviews': verdicts, 'admitted': same,
                           'gate': ('DELIVERED earlier (%s); the proof matches the files' % pr['verified_at_utc']) if same else 'STALE'}
        print('%-5s %s %s' % (n, 'ADMITTED (earlier)' if same else 'STALE', verdicts))
        continue
    out = subprocess.run([sys.executable, str(GATE), 'deliver'] + files + ['--out', str(d / 'FOR-JOEL.txt'),
                          '--proof', str(d / 'FOR-JOEL.proof.json')], capture_output=True, text=True)
    res['gated'][n] = {'reviews': verdicts, 'admitted': out.returncode == 0,
                       'gate': (out.stdout.strip() or out.stderr.strip())[-1500:].replace(str(HERE) + '/', '')}
    print('%-5s %s %s' % (n, 'ADMITTED' if out.returncode == 0 else 'BLOCKED', verdicts))
    if out.returncode:
        print('   ', out.stderr.strip()[-900:])
for role in ROLES:
    p = HERE / ('CUTS-REVIEW-%s.json' % role)
    if not p.exists():
        continue
    r = json.loads(p.read_text(encoding='utf-8'))
    for k, v in r['cuts'].items():
        res['cuts'].setdefault(k, {})[role] = v['verdict']
for k, v in res['cuts'].items():
    v['passed'] = all(v.get(role) == 'PASS' for role in ROLES)
print('cuts:', {k: ('PASS' if v['passed'] else v) for k, v in res['cuts'].items()})
(HERE / 'GATE-OUTCOMES.json').write_text(json.dumps(res, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
