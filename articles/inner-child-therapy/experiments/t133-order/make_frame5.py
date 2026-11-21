#!/usr/bin/env python3
"""Run 5's frame (PLAN.md, "Run 5"): the guide's own words for its parts and roles, and Joel's framework answers.

No model writes any of it: a model asked what a part with no text of its own is for describes what sits under it now,
which is how the frame for runs 2 to 4 kept 8 of his 20 moves in their old place (lesson inner-child-2026-11-20r).

  python3 make_frame5.py      # out/FRAME-5.json
  python3 make_frame5.py --b  # out/FRAME-5B.json: run 5b, with his line on where divine love leads (PLAN.md, "Run 5b")"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
NOV4 = json.load(open(HERE.parent / 't132-toc-links' / 'order' / 'NOV4-SECTIONS.json'))[1:]
BY = {'N%03d' % int(s['n']): s for s in NOV4}
ROLES = ['N021', 'N028', 'N045']
ANSWERS = HERE.parent / 't133-answers'


def text(i):
    return BY[i]['body'].strip()


def verbatim(path, start, end):
    """The words of his saved message from start to end, inclusive, exactly as he wrote them."""
    t = open(path, encoding='utf-8').read()
    a = t.index(start)
    b = t.index(end, a) + len(end)
    return t[a:b]


def main():
    q114 = json.load(open(HERE / 'out' / 'FRAME-3.json'))['joel_view']
    q115 = verbatim(ANSWERS / 'JOEL-20261120-2322.md', 'the nurturer doesn', "it's infinite, it's unspeakable...")
    q116 = verbatim(ANSWERS / 'JOEL-20261121-0147.md', 'yes all 3 roles', "fit cleanly into just one role")
    parts = [{'id': 'N%03d' % int(s['n']), 'heading': s['heading'], 'own_text': s['body'].strip()}
             for s in NOV4 if int(s['level']) == 1]
    parts[0]['own_text'] = '(the opening, in "overview" above)'
    frame = {
        'about': "The guide's own words for what each part and role is for (its text as of 4 November, verbatim, "
                 'empty where a part or role has no text of its own), then the author\'s answers about how he sorts '
                 'things. Nothing here describes a part by the sections now under it.',
        'overview': {'opening': text('N001'), 'five_stages': text('N003')},
        'parts': parts,
        'roles': [{'id': i, 'name': BY[i]['heading'], 'own_text': text(i)} for i in ROLES],
        'joel_view': [
            {'source': q114['source'], 'text': q114['text']},
            {'source': 'Joel, 2026-11-20 23:22 UTC, on divine love and the Nurturer (verbatim)', 'text': q115},
            {'source': 'Joel, 2026-11-20 23:22 UTC, agreeing to this rule', 'text': 'A problem goes where the reader meets it.'},
            {'source': 'Joel, 2026-11-21 01:47 UTC, on what the part "Discovering and Healing Old Patterns" is for (verbatim)',
             'text': q116},
        ],
    }
    if '--b' in sys.argv:
        frame['joel_view'].append({
            'source': 'Joel, in his guide after his reorganization: the text under the heading "Divine Love: Bigger '
                      'Door", verbatim, without its last clause, which says where a section sits',
            'text': 'This is what the Inner Guide can bring you to'})
    assert re.search('spiritual source', json.dumps(frame)) is None
    out = 'FRAME-5B.json' if '--b' in sys.argv else 'FRAME-5.json'
    (HERE / 'out' / out).write_text(json.dumps(frame, indent=1, ensure_ascii=False) + '\n')
    print('parts %d (with no text of their own: %s); roles: %s' % (
        len(parts), ', '.join(p['heading'] for p in parts if not p['own_text']),
        ', '.join('%s %d words' % (r['name'], len(r['own_text'].split())) for r in frame['roles'])))


if __name__ == '__main__':
    main()
