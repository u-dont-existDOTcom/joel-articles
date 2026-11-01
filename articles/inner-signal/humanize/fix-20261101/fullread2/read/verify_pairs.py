"""VERIFY-PAIRS.md: every paragraph the second full read's fixes changed, before and after (APPLIED-FULLREAD2.json),
for the lead session's read of the fixes (E294).

  python3 articles/inner-signal/humanize/fix-20261101/fullread2/read/verify_pairs.py
"""
import json
import pathlib

D = pathlib.Path(__file__).resolve().parent.parent


def main():
    rec = json.loads((D / 'APPLIED-FULLREAD2.json').read_text(encoding='utf-8'))
    out = ['# The second full read: every changed paragraph, before and after (for the read of the fixes)', '']
    for k, c in enumerate(rec['changed'], 1):
        out.append('## C%d (%s; now paragraphs %s)' % (k, c['op'], c['after_blocks']))
        out.append('')
        out += ['BEFORE: ' + b for b in c['before']]
        out += ['AFTER:  ' + a for a in c['after']]
        out.append('')
    (D / 'VERIFY-PAIRS.md').write_text('\n'.join(out), encoding='utf-8')
    print(len(rec['changed']), 'changes')


if __name__ == '__main__':
    main()
