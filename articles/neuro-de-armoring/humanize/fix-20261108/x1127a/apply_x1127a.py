#!/usr/bin/env python3
"""Put his answers of 2026-11-27 15:45 UTC ("73 a  but i also can't recommend starting them 74 b") into the article, each
warning in only at Human High by itself (apply_gate.py).

  python3 articles/neuro-de-armoring/humanize/fix-20261108/x1127a/apply_x1127a.py --prec [--write]
  python3 articles/neuro-de-armoring/humanize/fix-20261108/x1127a/apply_x1127a.py --lma TRY LINK "HOW" [--write]

Each run appends to APPLIED-X1127A.json, with the article's hash before and after.
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
import texts_x1127a as T  # noqa: E402

REC = HERE / 'APPLIED-X1127A.json'
ABOUT = ('his answers "73 a  but i also can\'t recommend starting them 74 b" of 2026-11-27 15:45 UTC '
         '(fix-20261108/joel-20261127-1545-message.txt): 73a and his line in the herbs warning, 74b in his Precautions')


def run(key, old, new, whose, check, write):
    apply_gate.require(T.H / 'pangram-ledger.jsonl', [T.plain(new)])
    text = T.ARTICLE.read_text(encoding='utf-8')
    before = hashlib.sha256(text.encode()).hexdigest()
    assert text.count(old) == 1, key
    text = text.replace(old, new)
    after = hashlib.sha256(text.encode()).hexdigest()
    print(key, before[:8], '->', after[:8], check)
    if write:
        T.ARTICLE.write_text(text, encoding='utf-8')
        rec = json.loads(REC.read_text(encoding='utf-8')) if REC.exists() else {'about': ABOUT, 'runs': []}
        rec['runs'].append({'applied': [{'key': key, 'whose': whose, 'check': check, 'old': old, 'new': new}],
                            'before_sha256': before, 'after_sha256': after})
        REC.write_text(json.dumps(rec, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
        print('written', after[:8])


if __name__ == '__main__':
    write = '--write' in sys.argv
    if '--prec' in sys.argv:
        run('prec', T.OLD['prec'], T.NEW['prec'], 'his own Precautions paragraph, with his 74b ("on the same day as")',
            'my check, this turn: https://www.pangram.com/history/df64f39b-0778-436c-a650-efe5d3bfbda5 (Human Written, '
            'one window, High, 91 words)', write)
    elif '--lma' in sys.argv:
        i = sys.argv.index('--lma')
        k, link, how = sys.argv[i + 1:i + 4]
        run('lma', T.OLD['lma'], T.TRY[k], 'his card version, with his 73a and his line "i also can\'t recommend starting '
            'them" put in; the stop sign\'s words are mine (%s)' % k, 'my check, this turn: %s (%s)' % (link, how), write)


def sw22(write):
    """The humanizing pass in "Psychology is the Software; Biology is the Hardware.": the Anti-Breakthrough, from its near
    miss of last turn (#267), two one-change steps (sw_x1127a.STEP), the second Human High in one window."""
    import sw_x1127a as W
    run('sw22', W.T.OLD['sw22'], W.STEP['sw22-s2'], 'mine: my version of the post\'s Anti-Breakthrough (texts_x1126b.NEW'
        '[\'sw22\'], fixed for sense from the fresh reads x1126b/v1), "Dr." off and its last sentence joined',
        'my check, this turn: https://www.pangram.com/history/31905039-057d-4b64-9c9e-5dbde18dadef (Human Written, one '
        'window, High, 81 words; P-SW22 try 4); comparison read x1127a/read-1127b (one finding, severity 1, kept)', write)


if __name__ == '__main__' and '--sw22' in sys.argv:
    sw22('--write' in sys.argv)


def prec76(write):
    """His answer 76 of 2026-11-27 17:21 UTC (76a and his reason), in three one-piece steps from the 74b version (#291),
    each Human High in one window; the last, his reason in a sentence of its own, goes in."""
    run('prec', T.P74, T.PREC76['c'], 'his own Precautions paragraph, with his 74b and his 76: 76a\'s words and his reason '
        '("that can be dangerous with non-kratom opioids where overdose is more of a concern but even with kratom you can '
        'get side effects when more sensitive"), fitted as a sentence after the list',
        'my check, this turn: https://www.pangram.com/history/bcf604c0-bb07-46c7-9262-d5cec58ed6f9 (Human Written, one '
        'window, High, 124 words; W015-his try 8, after 76a by itself, '
        'https://www.pangram.com/history/2145221d-aedb-494a-bf47-03837fa81a43, and with the overdose half, '
        'https://www.pangram.com/history/84647620-42e8-4e40-a96d-ea971a1f011b, each High)', write)


if __name__ == '__main__' and '--prec76' in sys.argv:
    prec76('--write' in sys.argv)
