#!/usr/bin/env python3
"""Turn 109, the third try at Hear the Guard First's P1 (experiments/t109-api/API-CHECKS.md). Try 1's P1 had his reply line
and its reason and read Human, while P3 without the reply read 99.8% AI; try 2 put both back in P3 (Human), and P1 without
them read 28% AI, bare instructions. The reason, "It puts you into the role of the Nurturer, which alleviates the instinct
to argue back.", goes with the question in P1 now (asking what it's afraid of is the Nurturer's move), and the reply line
"Tell me what you remember, I'm listening." stays after the remembering it answers. Every sentence is word for word and
used once.

  python3 reshape_t109c.py [--show]"""
import sys
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import reshape_t109 as R  # noqa: E402

SECTIONS = {
    'guard': {
        'head': '### Hear the Guard First', 'end': '\n### When to Change the Strategy',
        # as try 2 left it: P1 (4 sentences), P2 (3), P3 (7), P4 (7), P5 (4), P6 (6), P7 (5)
        'counts': [4, 3, 7, 7, 4, 6, 5],
        'shape': [[(1, 1), (1, 2), (3, 5), (1, 3), (1, 4)],
                  [(2, 1), (2, 2), (2, 3)],
                  [(3, 1), (3, 2), (3, 3), (3, 4), (3, 6), (3, 7)],
                  [(4, k) for k in range(1, 8)],
                  [(5, k) for k in range(1, 5)],
                  [(6, k) for k in range(1, 7)],
                  [(7, k) for k in range(1, 6)]],
        'note': ('the third try (reshape_t109c.py): P1 without his reply and its reason read 28% AI; the reason now follows the question '
                 'in P1, and his reply line stays in P3 after the remembering it answers. Every sentence is word for word and used once.'),
    },
}


def main():
    s = R.ART.read_text(encoding='utf-8')
    R.SECTIONS.clear()
    R.SECTIONS.update(SECTIONS)
    s, old, new = R.reshape(s, 'guard')
    for p in new[:3]:
        print('%4d | %s' % (len(p.split()), p))
    if '--show' not in sys.argv:
        R.ART.write_text(s, encoding='utf-8')
        print('installed')


if __name__ == '__main__':
    main()
