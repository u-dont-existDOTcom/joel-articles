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
         'Made by `doubt.py`. Only what exists before he is asked: the blind sort without his view (run 3) and run 2.', '',
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
    (HERE / 'DOUBT.md').write_text('\n'.join(L) + '\n')
    print('\n'.join(L))


if __name__ == '__main__':
    main()
