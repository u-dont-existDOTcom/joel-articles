"""The 5-HTP stop signs (his post's block 92) and the hard interaction rule (block 93), drafted with the point first
(E357) and his other moves (fix-20261103/examples/WHAT-HIS-VERSIONS-DO.md), held to the fidelity check, each by itself and
both together, in the article as it stands; and to the linter.

  python3 articles/neuro-de-armoring/humanize/fix-20261104/next5/check_next5.py
"""
import json
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
F = HERE.parent
H = F.parent
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import fidelity_keys as fk  # noqa: E402

FIRST = {'092': 'Side effects / stop signs: Nausea, stomach discomfort'}   # 093 went in (apply_b093.py)
DRAFTS = {k: HERE / 'blocks' / ('%s.md' % k) for k in FIRST}


def main():
    md = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
    keys = json.loads((H / 'FIDELITY-KEYS.json').read_text(encoding='utf-8'))
    raw = re.split(r'\n\s*\n', md.rstrip('\n'))
    where = {}
    for k, start in FIRST.items():
        hits = [i for i, b in enumerate(raw) if b.startswith(start)]
        assert len(hits) == 1, (k, hits)
        where[k] = hits[0]
    out = {'about': __doc__.split('\n')[0], 'each': {}, 'lint': {}}
    together = list(raw)
    for k, p in DRAFTS.items():
        t = p.read_text(encoding='utf-8').strip()
        one = list(raw)
        one[where[k]] = t
        together[where[k]] = t
        r = fk.check(keys, '\n\n'.join(one) + '\n')
        out['each'][k] = {'block': where[k], 'draft': str(p.relative_to(H)), 'pass': r['pass'],
                          'lost': {x: r[x] for x in ('numbers_lost', 'numbers_new', 'terms_lost', 'warnings_lost') if r[x]}}
        lint = subprocess.run([sys.executable, str(ROOT / 'tools' / 'humanization' / 'tells_lint.py'), str(p), '--quiet'],
                              capture_output=True, text=True)
        out['lint'][k] = {'exit': lint.returncode, 'out': lint.stdout.strip().splitlines()[-12:]}
    r = fk.check(keys, '\n\n'.join(together) + '\n')
    out['together'] = {'pass': r['pass'], 'lost': {x: r[x] for x in ('numbers_lost', 'numbers_new', 'terms_lost', 'warnings_lost') if r[x]}}
    print(json.dumps(out, ensure_ascii=False, indent=1))
    (HERE / 'CHECK-NEXT5.json').write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    sys.exit(0 if r['pass'] and all(v['pass'] for v in out['each'].values()) else 1)


if __name__ == '__main__':
    main()
