#!/usr/bin/env python3
"""Turn 140: the section catalog (../../SECTION-LINKS.json) follows the post after question 117's moves, published
2026-11-21 13:35 UTC, and is checked against the live post's headings read back then (live_headings.txt).

Healing Old Patterns (S075) is gone; Re-do Trauma Memories (S076, now h3) and Discipline Done Right? (S077, now h4)
follow You Did It Well Before (S047); Answer the Disciplinarian (S078, now h3) follows Reframe the Critic (S028). "Killing
the Old You" (S013k), whose level the catalog didn't have, is an h4 in the post. Anchors don't change: they come from the
heading text alone. His renames of S092, S102 and S105 went through section_links.py rename (no links to change).

  python3 apply_moves.py          # check only: the catalog against the live headings
  python3 apply_moves.py --write  # apply the moves, then check"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
CAT = HERE.parents[1] / 'SECTION-LINKS.json'


def move_after(hs, ids, after, levels):
    block = [h for h in hs if h['id'] in ids]
    rest = [h for h in hs if h['id'] not in ids]
    k = next(i for i, h in enumerate(rest) if h['id'] == after) + 1
    for h in block:
        h['level'] = levels[h['id']]
    return rest[:k] + block + rest[k:]


def follow_live(hs):
    """Put the headings in the live post's order and at its levels, matched by text (each text once, in order). This
    takes in his own moves the catalog didn't have: "Killing the Old You" under This Precious Human Life; What to Do
    With a Peak before Prepare for Altered States Now; Life's a trip also under it; Confused After Trips? before Who
    Counts as Trusted."""
    live = []
    for line in open(HERE / 'live_headings.txt', encoding='utf-8').read().splitlines():
        lvl, text = line.split('|', 1)
        if text:
            live.append((int(lvl), text))
    pool = {}
    for h in hs:
        pool.setdefault(h['text'], []).append(h)
    out = []
    for lvl, text in live:
        h = pool[text].pop(0)
        h['level'] = lvl
        out.append(h)
    assert not any(pool.values()), 'catalog headings not in the post: %s' % [v for v in pool.values() if v]
    return out


def apply(c):
    hs = [h for h in c['headings'] if h['id'] != 'S075']
    hs = move_after(hs, ['S076', 'S077'], 'S047', {'S076': 3, 'S077': 4})
    hs = move_after(hs, ['S078'], 'S028', {'S078': 3})
    for h in hs:
        if h['id'] == 'S013k':
            h['level'] = 4
            h['note'] = h.get('note', '') + '; an h4 in the post (read 2026-11-21 13:35 UTC)'
    c['headings'] = follow_live(hs)
    c['source'] += (' Turn 140, 2026-11-21: question 117\'s moves (S075 gone; S076 and S077 after S047 as h3 and h4; S078 '
                    'after S028 as h3), the level of S013k, and his renames of S092, S102 and S105, and his own moves since 20 November (Killing the Old You under This Precious Human Life; What to Do With a Peak '
                    'before Prepare for Altered States Now; Life\'s a trip also under it; Confused After Trips? before Who '
                    'Counts as Trusted), all checked against the live post\'s headings at 13:35 UTC (experiments/t140-moves/).')
    return c


def refresh_anchors(c):
    """Every anchor by section_links.slug, which now reads "&" as "and" and keeps an accented letter's plain letter."""
    sys.path.insert(0, str(HERE.parents[3] / 'tools' / 'humanization'))
    import section_links as sl  # noqa: E402
    changed = []
    for h in c['headings']:
        a = sl.slug(h['text'])
        if h['anchor'] != a:
            changed.append((h['id'], h['anchor'], a))
            h['anchor'] = a
    return changed


def check_anchors(c):
    """The catalog's anchors against the ones read from the rendered post (live_anchors.txt)."""
    seen = dict(l.split('\t') for l in open(HERE / 'live_anchors.txt', encoding='utf-8').read().splitlines() if l)
    return [(h['id'], h['anchor'], seen[h['text']]) for h in c['headings'] if h['text'] in seen and seen[h['text']] != h['anchor']]


def check(c):
    live = []
    for line in open(HERE / 'live_headings.txt', encoding='utf-8').read().splitlines():
        lvl, text = line.split('|', 1)
        if text:
            live.append((int(lvl), text))
    cat = [(h['level'], h['text']) for h in c['headings']]
    bad = [(i, a, b) for i, (a, b) in enumerate(zip(cat, live)) if a != b]
    return len(cat) == len(live) and not bad, len(cat), len(live), bad[:5]


def main():
    c = json.load(open(CAT, encoding='utf-8'))
    if '--write' in sys.argv:
        if any(h['id'] == 'S075' for h in c['headings']):
            c = apply(c)
        for i, old, new in refresh_anchors(c):
            print('anchor %s: %s -> %s' % (i, old, new))
        CAT.write_text(json.dumps(c, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    wrong = check_anchors(c)
    print('anchors against the rendered post: %s' % ('all the same' if not wrong else wrong))
    ok, n_cat, n_live, bad = check(c)
    ok = ok and not wrong
    print('catalog %d headings, live %d (empty headings left out): %s%s' % (n_cat, n_live, 'the same, in order and level' if ok else 'DIFFERENT', '' if ok else ' %s' % bad))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
