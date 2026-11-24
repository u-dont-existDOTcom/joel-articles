#!/usr/bin/env python3
"""An obvious correction found while reading Scenario A's Step 2 for question 62: "you cerebral cortex" is "your".

  python3 articles/neuro-de-armoring/humanize/fix-20261108/x1124a/fix_typo_x1124a.py [--write]
"""
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ARTICLE = HERE.parents[1] / 'HUMANIZED-SO-FAR.md'
OLD, NEW = 'Once your heart rate is within normal range, you cerebral cortex', \
           'Once your heart rate is within normal range, your cerebral cortex'


def main(write):
    text = ARTICLE.read_text(encoding='utf-8')
    if NEW in text:
        print('already in')
        return
    assert text.count(OLD) == 1
    out = text.replace(OLD, NEW, 1)
    p = HERE / 'APPLIED-X1124A.json'
    rec = json.loads(p.read_text(encoding='utf-8'))
    rec.setdefault('obvious', []).append({'old': OLD, 'new': NEW, 'where': "Scenario A, Step 2", 'by': 'fix_typo_x1124a.py'})
    rec['after_sha256'] = hashlib.sha256(out.encode('utf-8')).hexdigest()
    print('after', rec['after_sha256'][:8])
    if write:
        ARTICLE.write_text(out, encoding='utf-8')
        p.write_text(json.dumps(rec, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main('--write' in sys.argv)
