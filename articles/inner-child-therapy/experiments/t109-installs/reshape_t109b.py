#!/usr/bin/env python3
"""Turn 109, the second try at two reshaped paragraphs that read AI alone in API batch t109-api-1 and -2
(experiments/t109-api/API-CHECKS.md), every sentence still word for word and used once.

- Hear the Guard First P3 (the performance paragraph) read 99.8% AI alone (t109_guard_p3). The diagnosis: the reshape had
  pulled his reply, "Tell me what you remember, I'm listening." with its reason, up into P1, away from "Maybe you've fooled
  yourself before, and that part remembers.", which it answers. That left P3 a chain of worries with no reply in it
  (says, stings because, maybe, if, even if), and left "what you remember" in P1 with nothing remembered before it. Now
  his reply and its reason are back right after the remembering, in his own order (his P2 of turn 26, sentences 1 to 4,
  7 and 8), and P1 is the plain path without them: the Nurturer voice, the question to ask, and his "Usually your little
  one only comes forward after that part feels heard. Peek-a-boo!".
- Start With Whatever Showed Up P1 (the plain path) read 99.8% AI alone (t109_start_p1). The diagnosis: the reshape had
  joined his P1's first three sentences to his P4's line and its wait, an unbroken run of instructions (ask, tell, or
  however, wait), and moved his "Maybe it just has something to say ... or a bit of each." out from between them. Now his
  P1 is whole again, as it read Human, his line to say and its wait are the next paragraph, then his "If nothing comes"
  (which read Human alone, t109_start_p4) and his "Or if you do get an answer"; the paragraphs about fears and stray thoughts, about naming
  parts (whose "though" still follows the fears), about anxiety and about a part's no follow, each as it was.

  python3 reshape_t109b.py [--show]"""
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import reshape_t109 as R  # noqa: E402

WHEN = R.WHEN
SECTIONS = {
    'guard': {
        'head': '### Hear the Guard First', 'end': '\n### When to Change the Strategy',
        # the section as reshape 1 left it: P1 (6 sentences), P2 (3), P3 (5), P4 (7), P5 (4), P6 (6), P7 (5)
        'counts': [6, 3, 5, 7, 4, 6, 5],
        'shape': [[(1, 1), (1, 2), (1, 5), (1, 6)],
                  [(2, 1), (2, 2), (2, 3)],
                  [(3, 1), (3, 2), (3, 3), (1, 3), (1, 4), (3, 4), (3, 5)],
                  [(4, k) for k in range(1, 8)],
                  [(5, k) for k in range(1, 5)],
                  [(6, k) for k in range(1, 7)],
                  [(7, k) for k in range(1, 6)]],
        'note': ('the second try (reshape_t109b.py): P3 read 99.8% AI alone once his reply "Tell me what you remember, I\'m listening." '
                 'and its reason had moved up to P1, away from "and that part remembers", which it answers; they are back after it '
                 'in his own order, and P1 is the plain path without them. Every sentence is word for word and used once.'),
    },
    'start-with': {
        'head': '## Start With Whatever Showed Up', 'end': '\n### Two Common Guarding Patterns Blocking Reparenting',
        # as reshape 1 left it: P1 (8, his quoted line counts as three), P2 (6), P3 (5), P4 (3), P5 (7), P6 (4), P7 (1)
        'counts': [8, 6, 5, 3, 7, 4, 1],
        'shape': [[(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3)],
                  [(1, 4), (1, 5), (1, 6), (1, 7), (1, 8)],
                  [(4, 1), (4, 2), (4, 3)],
                  [(5, k) for k in range(1, 8)],
                  [(3, k) for k in range(1, 6)],
                  [(2, 4), (2, 5), (2, 6)],
                  [(6, k) for k in range(1, 5)],
                  [(7, 1)]],
        'note': ('the second try (reshape_t109b.py): the new P1 read 99.8% AI alone, an unbroken run of instructions once his "Maybe it '
                 'just has something to say ... or a bit of each." had moved out of it; his P1 is whole again, then his line to say '
                 'and its wait, his "If nothing comes", his "Or if you do get an answer", and the paragraphs on fears and stray thoughts, on '
                 'naming parts, on anxiety and on a part\'s no, each as it was. Every sentence is word for word and used once.'),
    },
}


def main():
    s = R.ART.read_text(encoding='utf-8')
    R.SECTIONS.clear()
    R.SECTIONS.update(SECTIONS)
    for key in SECTIONS:
        s, old, new = R.reshape(s, key)
        print('==', key)
        for p in new:
            print('%4d | %s' % (len(p.split()), p))
    if '--show' not in sys.argv:
        R.ART.write_text(s, encoding='utf-8')
        print('installed')


if __name__ == '__main__':
    main()
