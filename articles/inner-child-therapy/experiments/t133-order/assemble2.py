#!/usr/bin/env python3
"""Turn 133, run 2 (PLAN.md, "Run 2"; written before its cards existed): the outline from the function-only frame's
cards, two ways, scored the same as run 1.

  python3 assemble2.py       # out/OUTLINE2-*.json and RESULTS-2.md

(a) run 1's rule (assemble.py) with FRAME-2.json and the run 2 cards;
(b) "sits under": a section whose card names, with high confidence, a section it sits directly under that isn't its 4
    November parent moves there (with the sections under it), unless that would put it inside itself."""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import assemble as A  # noqa: E402


def sits_under(cards, levels=('high',)):
    base = A.base_parents()
    par, moved = dict(base), {}
    for i in A.IDS:
        c = cards.get(i, {})
        t = c.get('sits_under')
        if c.get('sits_under_confidence') not in levels or t not in A.LEVEL or t == par[i] or t == i:
            continue
        if i in A.ancestors(t, par):
            continue
        par[i], moved[i] = t, 'sits under'
    kids, roots = {}, []
    for i in A.IDS:
        (roots if par[i] is None else kids.setdefault(par[i], [])).append(i)
    out = []

    def walk(i, lev):
        out.append({'id': i, 'level': min(lev, 5)})
        for k in sorted(kids.get(i, []), key=A.POS.get):
            walk(k, lev + 1)
    for r in sorted(roots, key=A.POS.get):
        walk(r, 1)
    assert len(out) == len(A.IDS)
    return {'outline': out}, moved


def main():
    frame = json.load(open(HERE / 'out' / 'FRAME-2.json'))
    cards = {}
    for L in 'ABCD':
        for c in json.load(open(HERE / 'out' / ('CARDS2-%s.json' % L)))['cards']:
            cards[c['id']] = c
    runs = [('(a) role, then part (high), function-only frame', 'role-part', A.assemble(frame, cards)),
            ('(a) role moves only (high)', 'role-only', A.assemble(frame, cards, use_part=False)),
            ('(b) sits under (high)', 'sits-under', sits_under(cards)),
            ('(b) sits under (high or medium)', 'sits-under-medium', sits_under(cards, ('high', 'medium')))]
    base = A.score_order.score(A.score_order.BASE)
    L = ['# Turn 133, run 2: a function-only frame, and "sits under"', '',
         'Made by `assemble2.py` (method and predictions: PLAN.md, "Run 2", written before the run).', '',
         '| Outline | His moves (of 20) | Other moves | His level changes (of 15) | Other level changes | Tau | In his place (of 148) | Sections moved |',
         '|---|---|---|---|---|---|---|---|',
         '| 4 November order, unchanged | 0 | 0 | 0 | 0 | %.3f | %d | 0 |' % (base['tau_vs_his'], base['same_place']),
         '| Turn 132 best on his moves: GPT with the rules, run 1 | 9 | 16 | 5 | 15 | 0.814 | 67 | |']
    detail = {}
    for label, name, (outline, moved) in runs:
        p = HERE / 'out' / ('OUTLINE2-%s.json' % name)
        p.write_text(json.dumps(outline, indent=1) + '\n')
        s = A.score_order.score(outline)
        detail[name] = (s, moved)
        L.append('| %s | %d | %d | %d | %d | %.3f | %d | %d |' % (label, s['reparented_same'], s['reparented_extra'],
                 s['levels_same'], s['levels_extra'], s['tau_vs_his'], s['same_place'], len(moved)))
    for name in ('role-part', 'sits-under'):
        s, moved = detail[name]
        L += ['', '## %s, move by move' % name, '']
        for i, why in sorted(moved.items(), key=lambda kv: A.POS[kv[0]]):
            c = cards[i]
            dest = {'role': c.get('role'), 'part': c.get('part')}.get(why, c.get('sits_under'))
            L.append('- %s "%s" -> under %s "%s" (%s)' % (i, A.HEADING[i], dest, A.HEADING.get(dest, '?'),
                                                         'his move' if i in s['got'] else 'not his'))
        L.append('')
        L.append('His moves it missed: %s.' % ', '.join('%s %s' % (u, A.HEADING[u]) for u in his_moves() if u not in s['got']))
    (HERE / 'RESULTS-2.md').write_text('\n'.join(L) + '\n')
    print('\n'.join(L))


def his_moves():
    B, H = A.score_order.parse(A.score_order.BASE), A.score_order.parse(A.score_order.HIS)
    return [u for u in A.IDS if u in H['par'] and H['par'].get(u) != B['par'].get(u)]


if __name__ == '__main__':
    main()
