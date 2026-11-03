"""STABILITY.md: how windows of words nobody changed read in the two whole-guide rechecks of 30 October (20:15 UTC,
../../recheck/read/RESULT-*.json; 21:40 UTC, RESULT-*.json here). Between the two, only the eleven paragraphs of
../TRIES.json changed. Each window of the first check with 5 words or more, found once in the second check's text and more
than 300 characters from any changed paragraph, is read again in the second (its worst window there). The evidence for gate
E304 and question 28.

  python3 articles/inner-signal/humanize/fix-20261030/tries/read/stability.py
"""
import collections
import json
import pathlib

from spots_tries import find, reading

HERE = pathlib.Path(__file__).resolve().parent
T = HERE.parent
LAST = T.parent / 'recheck' / 'read'
ORDER = ['AI High', 'AI Medium', 'AI Low', 'Human Low', 'Human Medium', 'Human High']


def main():
    tries = json.loads((T / 'TRIES.json').read_text(encoding='utf-8'))['tries']
    rows, moved = collections.defaultdict(collections.Counter), []
    for p in 'AB':
        now = json.loads((HERE / ('RESULT-%s.json' % p)).read_text(encoding='utf-8'))
        last = json.loads((LAST / ('RESULT-%s.json' % p)).read_text(encoding='utf-8'))
        changed = [loc for loc in (find(now['text'], t['after']) for t in tries) if loc]
        for w in last['windows']:
            seg = last['text'][w['start_index']:w['end_index']].strip()
            if len(seg.split()) < 5:
                continue
            loc = find(now['text'], seg)
            if not loc or any(loc[0] < b + 300 and loc[1] > a - 300 for a, b in changed):
                continue
            before = '%s %s' % ('AI' if w['label'].startswith('AI') else 'Human', w['confidence'])
            r = reading(now, *loc)[0]
            after = r.replace(' (', ' ').rstrip(')')
            rows[before][after] += 1
            if before.split()[0] != after.split()[0]:
                moved.append((p, before, after, seg[:140].replace('\n', ' / ')))
    lines = ['# Windows of words nobody changed, in the two rechecks of 30 October', '',
             'Each row is how a window read at 20:15 UTC; each column, how the same words read at 21:40 UTC (the worst window '
             'over them). Only windows of 5 words or more, more than 300 characters from the eleven paragraphs that changed '
             'in between. Made by `stability.py`.', '',
             '| at 20:15 | windows | ' + ' | '.join(ORDER) + ' |', '|---|---|' + '---|' * len(ORDER)]
    for b in ORDER:
        if rows[b]:
            lines.append('| %s | %d | %s |' % (b, sum(rows[b].values()), ' | '.join(str(rows[b][a]) for a in ORDER)))
    lines += ['', '## The ones that changed sides', '']
    lines += ['- part %s: %s at 20:15, %s at 21:40: %s' % m for m in moved]
    (HERE / 'STABILITY.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print('\n'.join(lines[4:4 + 2 + len([b for b in ORDER if rows[b]])]))


if __name__ == '__main__':
    main()
