#!/usr/bin/env python3
"""Turn 109, the fourth try at Hear the Guard First (experiments/t109-api/API-CHECKS.md). Three tries showed that each of
P1 and P3 read Human alone only while it held his reason line, "It puts you into the role of the Nurturer, which alleviates
the instinct to argue back.": try 1 (the reply and the reason in P1) P1 Human, P3 99.8% AI; try 2 (both in P3) P3 Human,
P1 28% AI; try 3 (the reason in P1, the reply in P3) P1 Human, P3 46% AI. The plain path had been stripped to
instructions. So P1 takes back the harder-voice case, as his own P1 had it (the Nurturer voice, why not a harder one,
borrowing it), with the question and his two lines about the little one, and P3 is try 2's P3 word for word (it read
Human alone, t109_guard_p3b). Every sentence is word for word and used once.

  python3 reshape_t109d.py [--show]"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import reshape_t109 as R  # noqa: E402

SECTIONS = {
    'guard': {
        'head': '### Hear the Guard First', 'end': '\n### When to Change the Strategy',
        # as try 3 left it: P1 (5 sentences), P2 (3), P3 (6), P4 (7), P5 (4), P6 (6), P7 (5)
        'counts': [5, 3, 6, 7, 4, 6, 5],
        'shape': [[(1, 1), (2, 1), (2, 2), (2, 3), (1, 2), (1, 4), (1, 5)],
                  [(3, 1), (3, 2), (3, 3), (3, 4), (1, 3), (3, 5), (3, 6)],
                  [(4, k) for k in range(1, 8)],
                  [(5, k) for k in range(1, 5)],
                  [(6, k) for k in range(1, 7)],
                  [(7, k) for k in range(1, 6)]],
        'note': ('the fourth try (reshape_t109d.py): P1 takes back the harder-voice case, as his own P1 had it, so the plain path is the '
                 'Nurturer voice, why not a harder one, borrowing it, the question and his two lines about the little one; P2 is the '
                 'performance paragraph as it read Human alone in the second try. Every sentence is word for word and used once.'),
    },
}


def main():
    s = R.ART.read_text(encoding='utf-8')
    R.SECTIONS.clear()
    R.SECTIONS.update(SECTIONS)
    s, old, new = R.reshape(s, 'guard')
    sys.path.insert(0, str(HERE.parents[3] / 'tools' / 'humanization'))
    from substack_check_text import smart  # noqa: E402
    b = (HERE.parent / 't109-api' / 'texts' / 't109_guard_p3b.txt').read_text(encoding='utf-8')
    assert smart(new[1]) == b, 'P2 is not try 2\'s P3 word for word'
    for p in new[:2]:
        print('%4d | %s' % (len(p.split()), p))
    if '--show' not in sys.argv:
        R.ART.write_text(s, encoding='utf-8')
        print('installed')


if __name__ == '__main__':
    main()
