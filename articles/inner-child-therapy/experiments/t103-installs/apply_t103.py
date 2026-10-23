#!/usr/bin/env python3
"""Turn 103: Joel's answers of 2026-10-23 21:52 UTC (experiments/t103-answers/JOEL-20261023-2152.md).

- 96.1 B: his own Untangling paragraph, word for word, in place of "Differentiation is slow, ..." (it passes, his check).
- 97 (all A) and 98 (all A): the 26 cuts of experiments/t102-safety/CUTS.json, each old text replaced exactly once in
  its paragraph, as SAFETY-CUTS.md showed them.
- 99 A: The Inner Guide's three h2 headings (experiments/t102-readers-edit/THE-INNER-GUIDE.md), each above the notes of
  the paragraph it opens, so every paragraph keeps its notes; no word changes.
Each changed paragraph gets a note above it. The script asserts every old text occurs once, so it can't run twice.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1] / 'HUMANIZED-ARTICLE-SO-FAR.md'
SRC = 'experiments/t103-answers/JOEL-20261023-2152.md'
CUTS = json.loads((HERE.parent / 't102-safety' / 'CUTS.json').read_text(encoding='utf-8'))
HIS_961 = ("Differentiation is slow, and it goes on your whole life. Sometimes you need to take a break from a family, group or "
           "relationship, even if they aren't doing anything to you. Simply being around them may pull you into that programmed "
           "space where listening to what you really want becomes harder. Some people come back later on different terms, and "
           "sometimes the break has to be long-term because the pattern of losing yourself with them is deeply entrenched. As you "
           "differentiate, you learn to tell which of those apply.")
HEADINGS = [("Maybe you've let a small child win at Go Fish", '## Between Spoiling and Clamping Down'),
            ("The Guide doesn't need to know everything for sure", '## A Healthy Mind Is Not a Perfect Mind'),
            ("The Guide also points beyond itself", '## A Belonging Deeper Than Any Group')]


def note(what):
    return '<!-- Turn 103 (his answers of 2026-10-23 21:52 UTC, ' + SRC + '): ' + what + ' -->'


def para_index(lines, start):
    hits = [k for k, l in enumerate(lines) if l.startswith(start)]
    assert len(hits) == 1, (start, hits)
    return hits[0]


def notes_top(lines, k):
    """The first line of the run of comment lines (and blank lines between them) right above line k."""
    j = k
    while j > 0:
        i = j - 1
        while i >= 0 and not lines[i].strip():
            i -= 1
        if i >= 0 and lines[i].startswith('<!--') and lines[i].rstrip().endswith('-->'):
            j = i
        else:
            break
    return j


def main():
    lines = ART.read_text(encoding='utf-8').split('\n')
    # 96.1 B
    k = para_index(lines, 'Differentiation is slow, and it goes on your whole life.')
    lines[k] = HIS_961
    lines[k:k] = [note('96.1 B: his own paragraph, word for word, in place of mine ("i fixed it, passes"); it carries the guide\'s line 543, a break taken on purpose.'), '']
    # 97 and 98
    for g in CUTS['groups']:
        for it in g['items']:
            k = para_index(lines, it['start'])
            for old, new in it['edits']:
                assert lines[k].count(old) == 1, (it['id'], old)
                lines[k] = lines[k].replace(old, new, 1)
            what = '%s A (%s): cut %s' % (it['id'], 'his "97. i agree cut all"' if it['id'].startswith('97') else 'his "98. agree cut all"',
                                         '; '.join('"%s"' % o.strip() for o, n in it['edits']))
            if any(n for o, n in it['edits']):
                what += ' (with "%s" for it)' % '; '.join(n for o, n in it['edits'] if n)
            what += '. The original is in experiments/t102-safety/SAFETY-CUTS.md.'
            lines[k:k] = [note(what), '']
    # 99 A
    for start, head in HEADINGS:
        k = para_index(lines, start)
        top = notes_top(lines, k)
        lines[top:top] = [head, '', note('99 A: a new heading, no word changes (experiments/t102-readers-edit/THE-INNER-GUIDE.md).'), '']
    ART.write_text('\n'.join(lines), encoding='utf-8')
    print('applied: 96.1, %d cuts, %d headings' % (sum(len(g['items']) for g in CUTS['groups']), len(HEADINGS)))


if __name__ == '__main__':
    main()
