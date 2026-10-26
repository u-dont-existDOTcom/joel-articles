#!/usr/bin/env python3
"""Turn 113: check and deliver each gated heading and sentence (tools/humanization/owner_delivery_gate.py), once its three reviews are
in, and write GATE-OUTCOMES.json: each candidate's reviewers' verdicts and whether the gate admitted it.

  python3 run_gate.py"""
import hashlib
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
GATE = ROOT / 'tools' / 'humanization' / 'owner_delivery_gate.py'
NAMES = sorted(json.loads((HERE / 'NAMES.json').read_text(encoding='utf-8')).values())
# a round-3 FAIL is run too, for the record of the gate refusing it (it is not on the sheet: GATE.md)
NAMES += ['start-stop-r3']
res = {}


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


for n in NAMES:
    d = HERE / n
    files = ['--draft', str(d / 'DRAFT.txt'), '--context', str(d / 'CONTEXT.txt'), '--source', str(d / 'SOURCE.txt'),
             '--manifest', str(d / 'ADMISSION.json')]
    verdicts = {}
    for role in ('preservation', 'cold_read_1', 'cold_read_2'):
        p = d / ('REVIEW-%s.json' % role)
        verdicts[role] = json.loads(p.read_text(encoding='utf-8')).get('verdict') if p.exists() else 'missing'
    proof = d / 'FOR-JOEL.proof.json'
    if proof.exists() and (d / 'FOR-JOEL.txt').exists():
        # the gate never replaces a delivery; an earlier one stands when its proof still matches the files
        pr = json.loads(proof.read_text(encoding='utf-8'))
        same = (pr['manifest_sha256'] == sha(d / 'ADMISSION.json') and pr['candidate_sha256'] == sha(d / 'DRAFT.txt')
                and pr['context_sha256'] == sha(d / 'CONTEXT.txt') and (d / 'FOR-JOEL.txt').read_bytes() == (d / 'DRAFT.txt').read_bytes())
        res[n] = {'reviews': verdicts, 'admitted': same,
                  'gate': ('DELIVERED earlier (%s); the proof matches the manifest, draft and context as they are' % pr['verified_at_utc'])
                  if same else 'STALE: the delivery proof no longer matches the files'}
        print('%-18s %s %s' % (n, 'ADMITTED (earlier)' if same else 'STALE', verdicts))
        continue
    out = subprocess.run([sys.executable, str(GATE), 'deliver'] + files + ['--out', str(d / 'FOR-JOEL.txt'),
                          '--proof', str(d / 'FOR-JOEL.proof.json')], capture_output=True, text=True)
    res[n] = {'reviews': verdicts, 'admitted': out.returncode == 0,
              'gate': (out.stdout.strip() or out.stderr.strip())[-1500:].replace(str(HERE) + '/', '')}
    print('%-18s %s %s' % (n, 'ADMITTED' if out.returncode == 0 else 'BLOCKED', verdicts))
    if out.returncode:
        print('   ', out.stderr.strip()[-900:])
(HERE / 'GATE-OUTCOMES.json').write_text(json.dumps(res, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
