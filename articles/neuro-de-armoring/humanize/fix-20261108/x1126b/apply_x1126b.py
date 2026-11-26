#!/usr/bin/env python3
"""Put his message of 2026-11-26 15:26 UTC into the article: the 5-HTP section's interaction paragraph ('ss', his answer
fitted, not yet humanized) and its "Who this is for" ('who', mine, in only at Human High by itself).

  python3 articles/neuro-de-armoring/humanize/fix-20261108/x1126b/apply_x1126b.py [--write]
"""
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import apply_gate  # noqa: E402
import texts_x1126b as T  # noqa: E402

CHECKS = {'who': 'my check, this turn: https://www.pangram.com/history/bc4243cd-e73e-40bb-944e-16cacf727350 (Human Written, '
                 'one window, High, 197 words)',
          'ss': 'his answer fitted; not yet humanized (LEFT.md: never checked as it stands), so no check'}


def main(write):
    apply_gate.require(T.H / 'pangram-ledger.jsonl', [T.plain(T.NEW[k]) for k in T.MINE])
    text = T.ARTICLE.read_text(encoding='utf-8')
    before = hashlib.sha256(text.encode()).hexdigest()
    applied = []
    for k in T.MINE + T.OWNER_EDITS:
        assert text.count(T.OLD[k]) == 1, k
        text = text.replace(T.OLD[k], T.NEW[k])
        applied.append({'key': k, 'whose': 'mine' if k in T.MINE else 'his answer, fitted', 'check': CHECKS[k],
                        'old': T.OLD[k], 'new': T.NEW[k]})
    print('\n'.join('%s: %s' % (a['key'], a['check']) for a in applied))
    if write:
        T.ARTICLE.write_text(text, encoding='utf-8')
        rec = {'about': 'his message of 2026-11-26 15:26 UTC (fix-20261108/joel-20261126-1526-message.txt): 70a and 71 '
                        'need no change; mushrooms are up to the reader', 'runs': [{
                            'applied': applied, 'before_sha256': before,
                            'after_sha256': hashlib.sha256(text.encode()).hexdigest()}]}
        (HERE / 'APPLIED-X1126B.json').write_text(json.dumps(rec, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
        print('written', rec['runs'][0]['after_sha256'][:8])


if __name__ == '__main__':
    main('--write' in sys.argv)
