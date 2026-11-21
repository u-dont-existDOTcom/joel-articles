#!/usr/bin/env python3
"""Turn 139: where readers would look for each section, against where it now sits in his guide.

Joel, 2026-11-21 13:07 UTC: "in that approach you should recommend how to improve the guide so the real readers will
also know where they would look for the sections". Five blind card sorts filed every section of the 4 November text
under the heading a reader thought it belongs to (runs 3, 4, 5, 5b and 6 in ../t133-order/, each with a different
frame). Where most of them would look under a different part or role than the one it sits in now, a real reader may
look there too: that place needs a pointer, or its part a line saying what it holds.

His guide now is his outline of 20 November (../t132-toc-links/order/HIS-OUTLINE.json) with the moves he approved on
2026-11-21 at 13:07 UTC (question 117, A): Healing Old Patterns goes; Re-do Trauma Memories (h3) and Discipline Done
Right? (h4) follow Borrow a Guide to Build It in the Guide; Answer the Disciplinarian (h3) follows The Parent You
Inherited under the Protector.

  python3 where_readers_look.py      # READERS-LOOK.json"""
import collections
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
EXP = HERE.parent
sys.path.insert(0, str(EXP / 't133-order'))
import assemble as A  # noqa: E402

RUNS = [('run 3', 'CARDS3'), ('run 4', 'CARDS4'), ('run 5', 'CARDS5'), ('run 5b', 'CARDS5B'), ('run 6', 'CARDS6')]
MOVES_117 = {'drop': ['N067'], 'after': [(['N073', 'N074'], 'N047', {'N073': 3, 'N074': 4}),
                                          (['N075'], 'N026', {'N075': 3})]}


def current_outline():
    """His outline with question 117's moves: [{'key', 'id' (or None), 'level', 'name', 'S'}] in order."""
    picks = {h['id']: h['heading'] for h in json.load(open(EXP / 't132-toc-links' / 'HIS-PICKS-RESOLVED.json'))}
    out = []
    merged = {}
    for e in json.load(open(EXP / 't132-toc-links' / 'order' / 'HIS-OUTLINE.json'))['outline']:
        if 'merge_into' in e:
            merged[e['id']] = e['merge_into']
            continue
        if e.get('drop') or e.get('id') in MOVES_117['drop']:
            continue
        name = picks.get(e.get('S')) or e.get('new') or A.HEADING.get(e.get('id'), '')
        out.append({'key': e.get('id') or e.get('S'), 'id': e.get('id'), 'level': e['level'], 'name': name, 'S': e.get('S')})
    for ids, after, levels in MOVES_117['after']:
        block = [x for x in out if x['id'] in ids]
        out = [x for x in out if x['id'] not in ids]
        j = next(k for k, x in enumerate(out) if x['id'] == after)
        # after the whole subtree of `after`
        k = j + 1
        while k < len(out) and out[k]['level'] > out[j]['level']:
            k += 1
        for x in block:
            x['level'] = levels[x['id']]
        out[k:k] = block
    return out, merged


def areas(outline):
    """Each entry's part (h1) and, under it, its h2 (a role, or a section group), by name."""
    h1 = h2 = None
    area = {}
    for x in outline:
        if x['level'] == 1:
            h1, h2 = x['name'], None
        elif x['level'] == 2:
            h2 = x['name']
        area[x['key']] = (h1, x['name'] if x['level'] == 2 else (h2 if x['level'] > 2 else None))
    return area


def main():
    outline, merged = current_outline()
    area = areas(outline)
    where = {x['id']: x for x in outline if x['id']}
    for m, into in merged.items():
        where[m] = where[into]
        area[m] = area[into]
    cards = {}
    for label, prefix in RUNS:
        for L in 'ABCD':
            for c in json.load(open(EXP / 't133-order' / 'out' / ('%s-%s.json' % (prefix, L))))['cards']:
                cards.setdefault(c['id'], []).append((label, c.get('sits_under')))
    rows = []
    for u in A.IDS:
        if u not in where or where[u]['level'] == 1:
            continue
        mine = area[u]
        looks = []
        for label, t in cards.get(u, []):
            if t not in area:
                looks.append((label, None))
                continue
            ta = area[t]
            same = ta[0] == mine[0] and (ta[1] is None or ta[1] == mine[1])
            looks.append((label, None if same else ta))
        elsewhere = [ta for _, ta in looks if ta]
        if len(elsewhere) >= 3:
            top, n = collections.Counter(elsewhere).most_common(1)[0]
            rows.append({'id': u, 'S': where[u]['S'] if u not in merged else None, 'section': where[u]['name'] if u not in merged else A.HEADING[u],
                         'merged_into': where[merged[u]]['name'] if u in merged else None,
                         'sits_in': {'part': mine[0], 'under': mine[1]},
                         'readers_look': {'part': top[0], 'under': top[1], 'readings': n},
                         'elsewhere_readings': len(elsewhere), 'of': len(looks),
                         'by_run': [{'run': lab, 'looks': (None if ta is None else {'part': ta[0], 'under': ta[1]})} for lab, ta in looks]})
    doc = {'about': __doc__.split('\n\n')[1].replace('\n', ' '),
           'outline_now': [{'key': x['key'], 'level': x['level'], 'name': x['name']} for x in outline],
           'sections_readers_look_elsewhere': rows}
    (HERE / 'READERS-LOOK.json').write_text(json.dumps(doc, indent=1, ensure_ascii=False) + '\n')
    print('%d sections: most readings would look under another part or role' % len(rows))
    for r in rows:
        print('- %s (sits in %s / %s): %d of %d elsewhere, most under %s / %s (%d)' % (
            r['section'], r['sits_in']['part'], r['sits_in']['under'], r['elsewhere_readings'], r['of'],
            r['readers_look']['part'], r['readers_look']['under'], r['readers_look']['readings']))


if __name__ == '__main__':
    main()
