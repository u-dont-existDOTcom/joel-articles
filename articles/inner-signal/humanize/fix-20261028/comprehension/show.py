"""Print a part's findings with the whole paragraph each one is in, for checking them by hand.

  python3 articles/inner-signal/humanize/fix-20261028/comprehension/show.py PART [--sev N]
"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import collect as c  # noqa: E402

D = json.loads((HERE / 'FINDINGS.json').read_text(encoding='utf-8'))
part = int(sys.argv[1])
sev = int(sys.argv[sys.argv.index('--sev') + 1]) if '--sev' in sys.argv else 0
for r in D['findings']:
    if r['chunk'] != part or r['severity'] < sev:
        continue
    flags = []
    if r['his_words']:
        flags.append('HIS WORDS')
    if r['same_as_published']:
        flags.append('SAME AS PUBLISHED')
    if r['now_found'] < 1:
        flags.append('now found %.2f' % r['now_found'])
    print('=' * 100)
    print('%s  sev %d  %s  %s  %s  %s' % (r['id'], r['severity'], r['kind'], '; '.join(r['where']),
                                          (r['origin'] or {}).get('date', '?'), ' '.join(flags)))
    print('NOW:', r['now'])
    print('PUB:', r['published'])
    print('WHY:', r['why'])
    for i in r['now_blocks'][:2]:
        print('  [P%s] %s' % (c.NOW[i]['pn'], c.NOW[i]['text']))
