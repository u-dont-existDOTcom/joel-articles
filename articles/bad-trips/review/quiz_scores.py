#!/usr/bin/env python3
"""quiz_scores.py - the reading quizzes he suggested on 2026-11-21 15:57 UTC ("i still don't think you are able to read
youur own writing correctly to see what looks ai, that's what i'm trying to teach you. we should do some quizes for you
without pangram first maybe"; lesson bad-trips-2026-11-21f), counted from QUIZZES.json into QUIZ-SCORES.md.

Each quiz is a passage of mine that no Pangram check has seen, with my reading of it written before he sees it: for each
sentence, "reads right" or "not sure" with why. His answer scores each reading right or wrong and names what I missed
(QUIZZES.json "his": {sentence number: "right" | "wrong"}, "missed": [sentence numbers he marks that I read as right],
"his_words": what he wrote). The Pangram check of the passage comes after his answer and is counted beside his score
("pangram": {sentence number: "Human High" | ...}), so whether my reading is getting closer to his is a number here, not
my impression.

  python3 articles/bad-trips/review/quiz_scores.py          writes QUIZ-SCORES.md beside it
"""
import json, pathlib

HERE = pathlib.Path(__file__).resolve().parent
Q = json.loads((HERE / 'QUIZZES.json').read_text(encoding='utf-8'))


def score(q):
    his = q.get('his') or {}
    if not his:
        return None
    right = sum(1 for v in his.values() if v == 'right')
    wrong = sum(1 for v in his.values() if v == 'wrong')
    return right, wrong, len(q.get('missed') or [])


lines = ['# Reading quizzes: my reading of my own sentences, scored by Joel before any Pangram check', '',
         'His suggestion, 2026-11-21 15:57 UTC: "i still don\'t think you are able to read youur own writing correctly '
         'to see what looks ai, that\'s what i\'m trying to teach you. we should do some quizes for you without pangram '
         'first maybe" ([the lesson](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/docs/lessons/2026-11-21-1557-bad-trips.md)). '
         'Counted by `quiz_scores.py` from [QUIZZES.json](QUIZZES.json); his answers come from the marking page.', '',
         '| quiz | round | passage | sentences | my "not sure" | his score: right / wrong | he found that I missed | Pangram after |',
         '|---|---|---|---|---|---|---|---|']
for q in Q['quizzes']:
    s = score(q)
    mine_no = sum(1 for r in q['reading'] if r['mine'] != 'reads right')
    pg = q.get('pangram') or {}
    lines.append('| %s | %s | %s | %d | %d | %s | %s | %s |' % (
        q['id'], q['round'], q['passage'], len(q['reading']), mine_no,
        '%d / %d' % s[:2] if s else 'waiting for his answer', str(s[2]) if s else '-',
        ', '.join('%s: %s' % kv for kv in sorted(pg.items())) if pg else 'not checked yet'))
lines.append('')
for q in Q['quizzes']:
    if not q.get('his'):
        continue
    sure = [r for r in q['reading'] if r['mine'] != 'reads right']
    said_right = [r for r in q['reading'] if r['mine'] == 'reads right']
    ok = lambda rs: sum(1 for r in rs if q['his'].get(str(r['n'])) == 'right')
    lines.append('%s: my "not sure" was right %d times of %d, my "reads right" %d of %d.' % (
        q['id'], ok(sure), len(sure), ok(said_right), len(said_right)))
lines.append('')
for q in Q['quizzes']:
    lines += ['## %s: %s' % (q['id'], q['passage']), '']
    for r in q['reading']:
        mark = (q.get('his') or {}).get(str(r['n']), '')
        note = (q.get('his_notes') or {}).get(str(r['n']), '')
        lines.append('- S%d, my reading **%s**%s: "%s" %s%s' % (r['n'], r['mine'], (', his score **%s**' % mark) if mark else '',
                                                             r['s'], r['why'], ('. His note: %s' % note) if note else ''))
    if q.get('his_words'):
        lines += ['', 'His words: "%s"' % q['his_words']]
    lines.append('')
(HERE / 'QUIZ-SCORES.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
print('wrote QUIZ-SCORES.md:', len(Q['quizzes']), 'quiz(zes)')
