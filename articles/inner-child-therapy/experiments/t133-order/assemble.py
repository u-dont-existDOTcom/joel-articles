#!/usr/bin/env python3
"""Turn 133: put the cards together into an outline (PLAN.md, step 3; written before any card existed), and score it.

  python3 assemble.py        # out/OUTLINE-*.json and RESULTS.md

Start from the 4 November outline. A section whose card names a role with high confidence, when that role's heading isn't
already above it, moves under the role; otherwise a section whose card names another part with high confidence moves
under that part. A section moves with the sections under it. Parts, role headings and grouping headings stay. Inside each
parent the 4 November order holds; a child sits one level below its parent (level 5 at most)."""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ORDER = HERE.parent / 't132-toc-links' / 'order'
sys.path.insert(0, str(ORDER))
import score_order  # noqa: E402

SECTIONS = json.load(open(ORDER / 'NOV4-SECTIONS.json'))[1:]
IDS = ['N%03d' % s['n'] for s in SECTIONS]
LEVEL = {'N%03d' % s['n']: s['level'] for s in SECTIONS}
HEADING = {'N%03d' % s['n']: s['heading'] for s in SECTIONS}
POS = {i: k for k, i in enumerate(IDS)}


def _his_names():
    """His current heading for each unit, and the heading he really put it under, headings he added included.
    (score_order.py skips added headings when it finds a parent, so its parent for a unit under one of his new headings
    is the nearest older unit above: right for scoring, wrong to report as his move. Joel, 2026-11-20 23:22 UTC: "no they
    didn't go under between spoiling and clamping down. they went under borrow a guide to build it. what are you looking
    at?")"""
    picks = {h['id']: h['heading'] for h in json.load(open(ORDER.parent / 'HIS-PICKS-RESOLVED.json'))}
    outline = json.load(open(ORDER / 'HIS-OUTLINE.json'))['outline']
    current, real, merged, stack = {}, {}, {}, []
    for e in outline:
        if 'merge_into' in e:
            merged[e['id']] = e['merge_into']
            continue
        if e.get('drop'):
            continue
        name = picks.get(e.get('S')) or e.get('new') or HEADING.get(e.get('id'), '')
        while stack and stack[-1][0] >= e['level']:
            stack.pop()
        if 'id' in e:
            current[e['id']] = name
            real[e['id']] = stack[-1][1] if stack else None
        stack.append((e['level'], name))
    return current, real, merged


CURRENT, HIS_PARENT, MERGED = _his_names()


def his_place(u):
    """Where he really put unit u, in words: under a heading (his added ones included), or merged into another section
    (Being Your Own Advocate With Doctors went into "Physical Pain?"; turn 136's first named report said "under None")."""
    if u in MERGED:
        return 'he merged it into "%s"' % CURRENT.get(MERGED[u], HEADING.get(MERGED[u], MERGED[u]))
    return 'he put it under "%s"' % HIS_PARENT.get(u)


def base_parents():
    par, stack = {}, []
    for i in IDS:
        while stack and LEVEL[stack[-1]] >= LEVEL[i]:
            stack.pop()
        par[i] = stack[-1] if stack else None
        stack.append(i)
    return par


def ancestors(i, par):
    out = []
    while par.get(i):
        i = par[i]
        out.append(i)
    return out


def assemble(frame, cards, use_role=True, use_part=True, role_levels=('high',)):
    base = base_parents()
    parts = [p['id'] for p in frame['parts']]
    roles = [r['id'] for r in frame.get('roles', [])]
    fixed = set(parts) | set(roles)
    par, moved = dict(base), {}
    for i in IDS:
        c = cards.get(i)
        if not c or i in fixed or c.get('kind') == 'grouping':
            continue
        r = c.get('role')
        if (use_role and r in roles and c.get('role_confidence') in role_levels and r not in ancestors(i, par)
                and i not in ancestors(r, par) and r != i):
            par[i], moved[i] = r, 'role'
            continue
        p = c.get('part')
        top = (ancestors(i, base) or [i])[-1]
        if use_part and p in parts and p != top and c.get('part_confidence') == 'high' and p != i \
                and i not in ancestors(p, par):
            par[i], moved[i] = p, 'part'
    kids, roots = {}, []
    for i in IDS:
        (roots if par[i] is None else kids.setdefault(par[i], [])).append(i)
    out = []

    def walk(i, lev):
        out.append({'id': i, 'level': min(lev, 5)})
        for k in sorted(kids.get(i, []), key=POS.get):
            walk(k, lev + 1)
    for r in sorted(roots, key=POS.get):
        walk(r, 1)
    assert len(out) == len(IDS), 'a cycle or a lost section'
    return {'outline': out}, moved


def main():
    frame = json.load(open(HERE / 'out' / 'FRAME.json'))
    cards = {}
    for L in 'ABCD':
        for c in json.load(open(HERE / 'out' / ('CARDS-%s.json' % L)))['cards']:
            cards[c['id']] = c
    missing = [i for i in IDS if i not in cards]
    variants = [('primary: role, then part (high)', 'primary', dict()),
                ('role moves only (high)', 'role-only', dict(use_part=False)),
                ('part moves only (high)', 'part-only', dict(use_role=False)),
                ('role (high or medium), then part (high)', 'role-medium', dict(role_levels=('high', 'medium')))]
    rows, detail = [], {}
    for label, name, kw in variants:
        outline, moved = assemble(frame, cards, **kw)
        p = HERE / 'out' / ('OUTLINE-%s.json' % name)
        p.write_text(json.dumps(outline, indent=1) + '\n')
        ok = subprocess.run([sys.executable, str(HERE.parent / 't132-toc-links' / 'order-test' / 'validate.py'), str(p)],
                            capture_output=True, text=True).stdout.strip()
        s = score_order.score(outline)
        rows.append((label, s, len(moved), ok))
        detail[name] = (s, moved)
    base = score_order.score(score_order.BASE)
    L = ['# Turn 133: the contents built from small questions', '',
         'Made by `assemble.py` from the cards in `out/` (method and predictions: PLAN.md, written before the run).', '',
         '| Outline | His moves (of 20) | Other moves | His level changes (of 15) | Other level changes | Tau | In his place (of 148) | Sections moved |',
         '|---|---|---|---|---|---|---|---|',
         '| 4 November order, unchanged | 0 | 0 | 0 | 0 | %.3f | %d | 0 |' % (base['tau_vs_his'], base['same_place']),
         '| Turn 132 best on his moves: GPT with the rules, run 1 | 9 | 16 | 5 | 15 | 0.814 | 67 | |',
         '| Turn 132 best tau: Fable, no rules, run 2 | 2 | 8 | 0 | 11 | 0.930 | 90 | |']
    for label, s, n, ok in rows:
        L.append('| %s | %d | %d | %d | %d | %.3f | %d | %d |' % (label, s['reparented_same'], s['reparented_extra'],
                 s['levels_same'], s['levels_extra'], s['tau_vs_his'], s['same_place'], n))
    s, moved = detail['primary']
    L += ['', 'Cards missing: %s.' % (', '.join(missing) or 'none'), '',
          '## The primary outline, move by move', '',
          'His moves it made: %s.' % (', '.join('%s %s' % (i, HEADING[i]) for i in s['got']) or 'none'), '',
          'Moves it made that he did not: %s.' % (', '.join('%s %s' % (i, HEADING[i]) for i in s['extra']) or 'none'), '']
    for i, why in sorted(moved.items(), key=lambda kv: POS[kv[0]]):
        c = cards[i]
        dest = c['role'] if why == 'role' else c['part']
        L.append('- %s "%s" -> under %s "%s" (%s; %s)' % (i, HEADING[i], dest, HEADING.get(dest, '?'), why,
                                                          'his move' if i in s['got'] else 'not his'))
    (HERE / 'RESULTS.md').write_text('\n'.join(L) + '\n')
    print('\n'.join(L))


if __name__ == '__main__':
    main()
