#!/usr/bin/env python3
"""fid_try.py - each draft put into a copy of the guide where it would go, then fidelity_keys.py check (R41 keys).

  python3 fid_try.py KEY [KEY...]
"""
import json, pathlib, subprocess, sys, tempfile
HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1]; REPO = ART.parents[1]
B = json.loads((ART / 'GUIDE-SO-FAR-blocks.json').read_text())
ids = [b['id'] for b in B]
KIDNEY = '[acute kidney injury](https://pubmed.ncbi.nlm.nih.gov/27917269/)'

def guide_with(key):
    md = (HERE / ('MD-%s.md' % key)).read_text().strip()
    G = [dict(b) for b in B]
    if key.startswith('cyp'):
        i = ids.index('B136'); items = G[i]['md'].split('\n')
        assert items[1].startswith('2. ')
        items[1] = md; G[i]['md'] = '\n'.join(items)
    elif key.startswith('mdma'):
        G[ids.index('B119')]['md'] = md
        j = ids.index('B120'); assert G[j]['md'].count('and acute kidney injury.') == 1
        G[j]['md'] = G[j]['md'].replace('and acute kidney injury.', 'and %s.' % KIDNEY)
    elif key.startswith('b106'):
        G[ids.index('B106')]['md'] = md
    return '\n\n'.join(b['md'] for b in G) + '\n'

if __name__ == '__main__':
    for k in sys.argv[1:]:
        with tempfile.NamedTemporaryFile('w', suffix='.md', delete=False) as f:
            f.write(guide_with(k))
        r = subprocess.run([sys.executable, 'tools/humanization/fidelity_keys.py', 'check',
                            'articles/bad-trips/humanize/h01/FIDELITY-KEYS-R41.json', f.name, '--json'],
                           cwd=REPO, capture_output=True, text=True)
        d = json.loads(r.stdout)
        print(k, 'PASS' if d['pass'] else 'FAIL', {x: d[x] for x in ('numbers_lost', 'numbers_new', 'terms_lost') if d[x]},
              [(u['id'], u['missing']) for u in d['warnings_lost']])
