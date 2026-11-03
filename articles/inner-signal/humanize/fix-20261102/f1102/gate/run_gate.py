"""Check and deliver G-92 and G-480 (tools/humanization/owner_delivery_gate.py) once their three reviews are in, and write
GATE.md: each draft's reviewers' verdicts and whether the gate admitted it. A draft any reviewer failed is not delivered,
and its card stays off his page (../build_page_f1102.py shows only an admitted one).

  python3 articles/inner-signal/humanize/fix-20261102/f1102/gate/run_gate.py
"""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[5]
GATE = ROOT / 'tools' / 'humanization' / 'owner_delivery_gate.py'
ROLES = ('preservation', 'cold_read_1', 'cold_read_2')


def main():
    inputs = json.loads((HERE / 'GATE-INPUTS.json').read_text(encoding='utf-8'))
    rows, out = [], {}
    for name in inputs:
        f = HERE / name
        args = ['--draft', str(f / 'DRAFT.txt'), '--context', str(f / 'CONTEXT.txt'), '--source', str(f / 'SOURCE.txt'),
                '--manifest', str(f / 'ADMISSION.json')]
        v = {}
        for r in ROLES:
            p = f / ('REVIEW-%s.json' % r)
            v[r] = json.loads(p.read_text(encoding='utf-8')).get('verdict') if p.exists() else 'missing'
        if all(x != 'missing' for x in v.values()):
            # the receipt moves from PENDING once all three reviews are saved (the gate's rule); the check still reads each review
            a = json.loads((f / 'ADMISSION.json').read_text(encoding='utf-8'))
            if a.get('status') == 'PENDING':
                a['status'] = 'READY_FOR_CHECK'
                (f / 'ADMISSION.json').write_text(json.dumps(a, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        chk = subprocess.run([sys.executable, str(GATE), 'check'] + args, capture_output=True, text=True)
        ok = chk.returncode == 0
        if ok and not (f / 'FOR-JOEL.txt').exists():
            d = subprocess.run([sys.executable, str(GATE), 'deliver'] + args + ['--out', str(f / 'FOR-JOEL.txt'),
                                '--proof', str(f / 'FOR-JOEL.proof.json')], capture_output=True, text=True)
            ok = d.returncode == 0
            if not ok:
                print(name, 'deliver:', d.stdout[-400:], d.stderr[-400:])
        out[name] = {'reviews': v, 'admitted': ok and (f / 'FOR-JOEL.txt').exists(),
                     'check': ' '.join((chk.stdout + chk.stderr).split())[:300]}
        draft = (f / 'DRAFT.txt').read_text(encoding='utf-8').replace('|', '\\|')
        rows.append('| %s | %s | %s | %s | %s | %s |' % (name, draft, v['preservation'], v['cold_read_1'], v['cold_read_2'],
                                                         'yes' if out[name]['admitted'] else 'no'))
        print(name, v, 'admitted' if out[name]['admitted'] else 'not admitted', out[name]['check'])
    md = ['# The owner-delivery gate for batch f1102\'s card suggestions (2 November)', '',
          'Model-written words in Joel\'s byline pass `tools/humanization/owner_delivery_gate.py deliver` before his page shows '
          'them (`docs/HUMANIZATION-OWNER-DELIVERY-GATE.md`): the linter, the writer\'s ledger (`make_gate.py`), and three '
          'reviewers, each a fresh Claude Sonnet subagent with only its brief and these files (preservation, cold reader 1, '
          'cold reader 2), launched 2026-11-02 by session_01Mxpoi6tFT3FgKmBvtGjRtS.', '',
          '| NAME | the new words | preservation | cold reader 1 | cold reader 2 | delivered |',
          '| --- | --- | --- | --- | --- | --- |'] + rows
    for name in inputs:
        for r in ROLES:
            p = HERE / name / ('REVIEW-%s.json' % r)
            if p.exists():
                j = json.loads(p.read_text(encoding='utf-8'))
                if j.get('verdict') != 'PASS':
                    md += ['', '%s, %s: %s' % (name, r, '; '.join(j.get('unresolved') or []) or j.get('evidence', '')[:400])]
    (HERE / 'GATE.md').write_text('\n'.join(md) + '\n', encoding='utf-8')
    (HERE / 'GATE-OUTCOMES.json').write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
