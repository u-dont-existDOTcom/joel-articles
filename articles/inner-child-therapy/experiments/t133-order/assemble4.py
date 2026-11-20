#!/usr/bin/env python3
"""Turn 133, run 4 (PLAN.md, "Run 4"; written before its cards existed): the blind card sort with his own view's outline, scored.

  python3 assemble4.py       # out/OUTLINE4-*.json and RESULTS-4.md"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import assemble as A  # noqa: E402
import assemble2 as A2  # noqa: E402


def main():
    cards = {}
    for L in 'ABCD':
        for c in json.load(open(HERE / 'out' / ('CARDS4-%s.json' % L)))['cards']:
            cards[c['id']] = c
    missing = [i for i in A.IDS if i not in cards]
    runs = [('his view, sits under (high)', 'high', A2.sits_under(cards)),
            ('his view, sits under (high or medium)', 'medium', A2.sits_under(cards, ('high', 'medium')))]
    base = A.score_order.score(A.score_order.BASE)
    L = ['# Turn 133, run 4: the blind card sort with his own view (question 114)', '',
         'Made by `assemble4.py` (method and predictions: PLAN.md, "Run 4", written before the run).', '',
         '| Outline | His moves (of 20) | Other moves | His level changes (of 15) | Other level changes | Tau | In his place (of 148) | Sections moved |',
         '|---|---|---|---|---|---|---|---|',
         '| 4 November order, unchanged | 0 | 0 | 0 | 0 | %.3f | %d | 0 |' % (base['tau_vs_his'], base['same_place']),
         '| Turn 132 best on his moves: GPT with the rules, run 1 | 9 | 16 | 5 | 15 | 0.814 | 67 | |']
    detail = {}
    for label, name, (outline, moved) in runs:
        (HERE / 'out' / ('OUTLINE4-%s.json' % name)).write_text(json.dumps(outline, indent=1) + '\n')
        s = A.score_order.score(outline)
        detail[name] = (s, moved)
        L.append('| %s | %d | %d | %d | %d | %.3f | %d | %d |' % (label, s['reparented_same'], s['reparented_extra'],
                 s['levels_same'], s['levels_extra'], s['tau_vs_his'], s['same_place'], len(moved)))
    L += ['', 'Cards missing: %s.' % (', '.join(missing) or 'none'), '', '## His 20 moves: where the blind sort filed each', '']
    B, H = A.score_order.parse(A.score_order.BASE), A.score_order.parse(A.score_order.HIS)
    for u in A2.his_moves():
        c = cards.get(u, {})
        t = c.get('sits_under')
        mark = 'his' if t == H['par'][u] else ('where it was' if t == B['par'][u] else 'elsewhere')
        L.append('- %s "%s": he put it under "%s"; the sort, under "%s" (%s, %s)' % (
            u, A.HEADING[u], A.HEADING.get(H['par'][u], H['par'][u]), A.HEADING.get(t, t), c.get('sits_under_confidence'), mark))
    s, moved = detail['high']
    L += ['', '## The high-confidence moves', '']
    for i in sorted(moved, key=A.POS.get):
        t = cards[i]['sits_under']
        L.append('- %s "%s" -> under "%s" (%s)' % (i, A.HEADING[i], A.HEADING.get(t, t), 'his move' if i in s['got'] else 'not his'))
    (HERE / 'RESULTS-4.md').write_text('\n'.join(L) + '\n')
    print('\n'.join(L))


if __name__ == '__main__':
    main()
