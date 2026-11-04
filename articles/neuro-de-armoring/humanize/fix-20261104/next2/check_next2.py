"""The next paragraphs' drafts held to the fidelity check, each by itself and all together, in the article as it stands.

Try 2 (blocks/): 085, 086, 088 and 089, after their first tries read 100% AI (../checks/x1104j) and the tell panel on each
(../panel/b0XX-n1/PANEL.md, E346). 090 and 091 are still their first tries (../next1/blocks/), never sent: the API's
credits ran out (HTTP 402) before them.

  python3 articles/neuro-de-armoring/humanize/fix-20261104/next2/check_next2.py
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

FIRST = {'085': 'Side effects / stop signs:', '086': 'Psychedelic caution:', '088': 'Who this is for: This is for the low-serotonin',
         '089': 'The tool:5-HTP', '090': "Scott's version: 100 mg 5-HTP", '091': 'Trial: Start lower if you are sensitive'}
DRAFTS = {k: (HERE / 'blocks' / ('%s.md' % k)) for k in ('085', '086', '088', '089')}
DRAFTS.update({k: (F / 'next1' / 'blocks' / ('%s.md' % k)) for k in ('090', '091')})


def main():
    md = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
    keys = json.loads((H / 'FIDELITY-KEYS.json').read_text(encoding='utf-8'))
    raw = re.split(r'\n\s*\n', md.rstrip('\n'))
    where = {}
    for k, start in FIRST.items():
        hits = [i for i, b in enumerate(raw) if b.startswith(start)]
        if k == '085':
            hits = [i for i in hits if 'choline headache' in raw[i]]
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
    (HERE / 'CHECK-NEXT2.json').write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    sys.exit(0 if r['pass'] and all(v['pass'] for v in out['each'].values()) else 1)


if __name__ == '__main__':
    main()
