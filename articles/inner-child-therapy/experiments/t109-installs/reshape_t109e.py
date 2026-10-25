#!/usr/bin/env python3
"""Turn 109: Hear the Guard First back to the second try's arrangement, my pick on the review page after four tries
(experiments/t109-api/API-CHECKS.md). Only one line, his "It puts you into the role of the Nurturer, which alleviates the
instinct to argue back.", carried a paragraph to Human alone: P1 read Human with it (tries 1 and 3) and 28% AI and 99% AI
without it (tries 2 and 4), and P3 read Human with it and his reply line (try 2), 46% AI with the reply alone (try 3) and
99.8% AI with neither (try 1). The second try keeps his reply and its reason together, the way he wrote them, with the
plain path short before them; its P1 waits on his answer on the review page (a line of his own, or another of the
arrangements). Every sentence is word for word and used once, and P1 and P3 are the texts checked as t109_guard_p1b and
t109_guard_p3b.

  python3 reshape_t109e.py [--show]"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parents[3] / 'tools' / 'humanization'))
import reshape_t109 as R  # noqa: E402
from substack_check_text import smart  # noqa: E402

SECTIONS = {
    'guard': {
        'head': '### Hear the Guard First', 'end': '\n### When to Change the Strategy',
        # as try 4 left it: P1 (7 sentences), P2 (7), P3 (7), P4 (4), P5 (6), P6 (5)
        'counts': [7, 7, 7, 4, 6, 5],
        'shape': [[(1, 1), (1, 5), (1, 6), (1, 7)],
                  [(1, 2), (1, 3), (1, 4)],
                  [(2, k) for k in range(1, 8)],
                  [(3, k) for k in range(1, 8)],
                  [(4, k) for k in range(1, 5)],
                  [(5, k) for k in range(1, 7)],
                  [(6, k) for k in range(1, 6)]],
        'note': ('back to the second try\'s arrangement (reshape_t109e.py), my pick after four tries: his reply and its reason together, '
                 'as he wrote them, and the plain path short before them; its P1 read 28% AI alone and waits on his answer on the '
                 'review page. Every sentence is word for word and used once.'),
    },
}


def main():
    s = R.ART.read_text(encoding='utf-8')
    R.SECTIONS.clear()
    R.SECTIONS.update(SECTIONS)
    s, old, new = R.reshape(s, 'guard')
    t = HERE.parent / 't109-api' / 'texts'
    assert smart(new[0]) == (t / 't109_guard_p1b.txt').read_text(encoding='utf-8'), 'P1 differs from the second try'
    assert smart(new[2]) == (t / 't109_guard_p3b.txt').read_text(encoding='utf-8'), 'P3 differs from the second try'
    for p in new[:3]:
        print('%4d | %s' % (len(p.split()), p[:100]))
    if '--show' not in sys.argv:
        R.ART.write_text(s, encoding='utf-8')
        print('installed')


if __name__ == '__main__':
    main()
