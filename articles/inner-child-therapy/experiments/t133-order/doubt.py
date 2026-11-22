#!/usr/bin/env python3
"""Turn 136: can the readers' own doubt show where to ask the author, before anything is compared with his order?

Joel, 2026-11-20 23:22 UTC: "you need to ask the author for their view before the models miss... because what are they
even missing? in general you're not comparing against something already done. so the question is, can you know when the
models are unsure, then ask the right questions?"

  python3 doubt.py       # DOUBT.md

Uses only what exists before the author is asked: run 3's blind sort (no view of his in its frame) and run 2's cards.
Each signal flags some sections; the table says how many questions that would be and how many of the sections he moved
(or changed the level of) were among them, beside what the same number of sections picked at random would catch."""
import collections
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import assemble as A  # noqa: E402


def load(prefix):
    out = {}
    for L in 'ABCD':
        for c in json.load(open(HERE / 'out' / ('%s-%s.json' % (prefix, L))))['cards']:
            out[c['id']] = c
    return out


def main():
    c2, c3 = load('CARDS2'), load('CARDS3')
    B, H = A.score_order.parse(A.score_order.BASE), A.score_order.parse(A.score_order.HIS)
    units = [u for u in A.IDS if u in B['par']]
    moved = {u for u in A.IDS if u in H['par'] and H['par'].get(u) != B['par'].get(u)}
    target = moved | {u for u in A.IDS if u in H['lev'] and u in B['lev'] and H['lev'][u] != B['lev'][u]}
    signals = [
        ('the blind sort is unsure (medium or low)', [u for u in units if c3[u]['sits_under_confidence'] != 'high']),
        ('the blind sort would move it', [u for u in units if c3[u]['sits_under'] not in (B['par'][u], None, 'none')]),
        ('two readings disagree on where it goes (run 2, run 3)', [u for u in units if c2[u]['sits_under'] != c3[u]['sits_under']]),
        ('two readings disagree on whose role it is', [u for u in units if c2[u]['role'] != c3[u]['role']]),
    ]
    L = ['# Turn 136: does the readers\' doubt show where to ask?', '',
         'Made by [doubt.py](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/articles/inner-child-therapy/experiments/t133-order/doubt.py). Only what exists before he is asked: the blind sort without his view (run 3) and run 2.', '',
         '| Signal | Questions it would mean (of %d) | His 20 moves among them | Chance, for that many | Moves or level changes (of %d) |' % (len(units), len(target)),
         '|---|---|---|---|---|']
    for name, flagged in signals:
        f = set(flagged)
        L.append('| %s | %d | %d | %.1f | %d |' % (name, len(f), len(f & moved), len(f) * len(moved) / len(units), len(f & target)))
    L += ['', '**What it shows.** The readers were unsure about 14 of the 20 sections he moved, more than chance, but also about '
          '65 he left alone: 79 questions. Two readers disagreeing picked his moves no better than chance. And their doubt '
          'came without his answer: they were unsure about shame and forgiveness, yet still filed them under Healing Old '
          'Patterns. Doubt section by section is a weak pointer; the questions that moved the result were about the framework '
          '(his answers to questions 114 and 115), and those can be asked before any sort.', '']
    L += undefined_parts_section(B, H, units, moved, len(set(signals[0][1])))
    (HERE / 'DOUBT.md').write_text('\n'.join(L) + '\n')
    print('\n'.join(L))


def undefined_parts_section(B, H, units, moved, n_unsure):
    """What the guide itself shows before any sort: the parts and roles it never defines in its own words (lesson
    inner-child-2026-11-20r; his question 115 answer, 2026-11-20 23:22 UTC: "is that really hard for ai to understand
    the diff?")."""
    sys.path.insert(0, str(HERE.parents[3] / 'tools' / 'humanization'))
    import undefined_parts as U  # noqa: E402
    secs = [{'id': 'N%03d' % int(s['n']), 'level': int(s['level']), 'heading': s['heading'], 'own': s['body']}
            for s in json.load(open(A.ORDER / 'NOV4-SECTIONS.json'))[1:]]
    found = U.undefined(secs, min_words=1)
    names = {f['heading'] for f in found}
    und = {s['id'] for s in secs if s['heading'] in names}
    parts = [s for s in secs if s['level'] == 1]
    frame = json.load(open(HERE / 'out' / 'FRAME-2.json'))
    nurturer = next(r['work'] for r in frame['roles'] if r['id'] == 'N028')
    patterns = next(p['job'] for p in frame['parts'] if p['id'] == 'N067')
    under = [u for u in units if B['par'].get(u) in und]
    moved_under = [u for u in moved if B['par'].get(u) in und]
    spiritual = ['N035', 'N038', 'N040', 'N043', 'N044']
    repair = ['N068', 'N069', 'N071']
    assert all(B['par'][u] == 'N028' and u in moved for u in spiritual), 'the five spiritual sections'
    assert all(B['par'][u] == 'N067' and u in moved for u in repair), 'distrust, shame, forgiveness'
    q = lambda ids: ', '.join('"%s"' % A.CURRENT.get(u, A.HEADING[u]) for u in ids)  # noqa: E731
    return [
        '## A pointer that needs no sort: what the guide doesn\'t define', '',
        'Made with [undefined_parts.py](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/tools/humanization/undefined_parts.py) on the 4 November text. %d of its headings have sections under '
        'them and no text of their own: %d of its %d parts, one of its three roles (the Nurturer), and four groups inside the '
        'parts: %s.' % (
            len(found), sum(1 for p in parts if p['id'] in und), len(parts),
            ', '.join('"%s"' % f['heading'] for f in found if f['level'] > 1 and f['heading'] != 'The Nurturer')), '',
        'A model asked what such a part is for can only read it off what sits under it now. The frame for runs 2 to 4 '
        '(FRAME-2) was written with the instruction not to do that, and still said:', '',
        '- the Nurturer: "%s"' % nurturer,
        '- Discovering and Healing Old Patterns: "%s"' % patterns, '',
        'Those two lines give the old place to 8 of the 20 sections he moved: the five spiritual sections he put under the '
        'Guide (%s) and the three on distrust, shame and forgiveness (%s). His answer to question 114 overrode the second '
        'for shame and forgiveness (run 4); no run put a spiritual section under the Guide. In turn 132, with no frame and '
        'a rule that only said a spiritual practice goes under "the role that holds the spiritual side", GPT put three of '
        'the five there (its first outline with the rules).' % (q(spiritual), q(repair)), '',
        '**As a pointer to sections it is no better than chance:** %d of his %d moved sections sat directly under a '
        'heading with no text of its own, and so did %d of all %d (%.1f expected). Its use is the questions: one for each '
        'part or role the guide doesn\'t define ("what is it for, and what looks as if it belongs but doesn\'t?"), %d here '
        'against %d from the readers\' doubt, and one answer can move a group at once, as his answer to question 114 '
        'moved shame and forgiveness together.' % (
            len(moved_under), len(moved), len(under), len(units), len(under) * len(moved) / len(units), len(found), n_unsure), '']


if __name__ == '__main__':
    main()
