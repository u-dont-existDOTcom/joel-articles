#!/usr/bin/env python3
"""Mechanical checks on each writer's units against the r01 units: fidelity keys (numbers, terms, warnings), links kept,
the approved "My notes" line word for word, straight quotes only. Writes CHECKS.json. No API calls.

Usage: python3 check_candidates.py writer_A.json [writer_B.json ...]
"""
import json, pathlib, re, subprocess, sys, tempfile

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[4]
FK = REPO / 'tools' / 'humanization' / 'fidelity_keys.py'
units = json.loads((HERE / 'UNITS-r01.json').read_text(encoding='utf-8'))
LINK = re.compile(r'\]\(([^)]+)\)')


def fidelity(before, after):
    with tempfile.TemporaryDirectory() as d:
        d = pathlib.Path(d)
        (d / 'b.md').write_text(before, encoding='utf-8')
        (d / 'a.md').write_text(after, encoding='utf-8')
        subprocess.run([sys.executable, str(FK), 'extract', str(d / 'b.md'), str(d / 'k.json')], capture_output=True, check=True)
        r = subprocess.run([sys.executable, str(FK), 'check', str(d / 'k.json'), str(d / 'a.md')], capture_output=True, text=True)
        lines = [l for l in r.stdout.splitlines() if l.strip() and not l.startswith('verdict')]
        return [l for l in lines if not l.startswith('numbers_new')]


out = {}
for wf in sys.argv[1:]:
    w = json.loads((HERE / wf).read_text(encoding='utf-8'))
    res = {}
    for k, before in units.items():
        after = w[k]['text']
        probs = fidelity(before, after)
        for url in LINK.findall(before):
            if url not in after:
                probs.append('link lost: ' + url)
        notes = [l for l in before.split('\n\n') if 'My notes:' in l]
        for n in notes:
            body = n.split('My notes:', 1)[1].strip()
            if body not in after:
                probs.append('My notes line changed')
        if re.search('[‘’“”]', after):
            probs.append('curly quote')
        res[k] = {'words_before': len(before.split()), 'words_after': len(after.split()), 'problems': probs}
    out[wf] = res
(HERE / 'CHECKS.json').write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding='utf-8')
for wf, res in out.items():
    for k, r in res.items():
        print(wf, k, r['words_before'], '->', r['words_after'], '|', '; '.join(r['problems'])[:300] or 'ok')
