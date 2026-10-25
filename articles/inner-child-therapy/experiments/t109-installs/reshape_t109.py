#!/usr/bin/env python3
"""Turn 109, 104 A ("yes this makes it much more of a readable guide, good"), the next sections in the densest-first order of
experiments/t108-shape/DENSITY.md: the plain path first, as if nothing goes wrong, then one situation a paragraph, every
sentence kept word for word and used once (each shape below is checked against the old sentences), only their order and
the paragraph breaks changed.

- Start With Whatever Showed Up (5.1 turns a paragraph, its seven paragraphs before Two Common Guarding Patterns): the
  first paragraph is the whole path now, noticing what showed up, asking it, his line to say and waiting; then who it
  might be, the fears and stray thoughts, his "If nothing comes" and his "Or if you do get an answer" side by side, and the
  anxiety and hesitation paragraphs as they were.
- Before You Tell the Hardest Stuff (6.0, both paragraphs his own text of his 2026-10-19 upload): what to do first, his "I'd
  assume" and his danger lines; then the reasons, one a paragraph: what a phone or a server keeps, who has to report, his
  question to ask them and why he wouldn't bother, and his dream narrative.

The densest sections I left as they are (When to Change the Strategy and Not Every Hero Wears A Cape are his own recent
rewrites; If You Want to Kill Yourself already starts with the steps; What to Make of a Passing Feeling, Notice the Part
That Came Here and The Belief Behind the Guards already take one case a paragraph, or their order carries the argument) are
named on the review page with why.

  python3 reshape_t109.py           installs both, printing each new paragraph's words
  python3 reshape_t109.py --show    prints the new paragraphs without writing"""
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1] / 'HUMANIZED-ARTICLE-SO-FAR.md'
WHEN = 'Turn 109 (his answers of 2026-10-25 14:20 UTC, experiments/t109-answers/JOEL-20261025-1420.md)'
SPLIT = re.compile(r'(?<=[.!?"”)])\s+(?=[A-Z"“(])')

SECTIONS = {
    'start-with': {
        'head': '## Start With Whatever Showed Up', 'end': '\n### Two Common Guarding Patterns Blocking Reparenting',
        'counts': [6, 5, 3, 8, 7, 4, 1],  # his quoted line is three sentences to the splitter
        'shape': [[(1, 1), (1, 2), (1, 3), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5)],
                  [(1, 4), (1, 5), (1, 6), (3, 1), (3, 2), (3, 3)],
                  [(2, k) for k in range(1, 6)],
                  [(4, 6), (4, 7), (4, 8)],
                  [(5, k) for k in range(1, 8)],
                  [(6, k) for k in range(1, 5)],
                  [(7, 1)]],
        'note': ('104 A: the section\'s own paragraphs in the plain-path-first shape (experiments/t109-installs/reshape_t109.py), '
                 'every sentence word for word and used once: the path first (what showed up, ask it, his line to say, wait), '
                 'then who it might be, the fears and stray thoughts, his "If nothing comes" and his "Or if you do get an answer" '
                 'side by side, and the anxiety and hesitation paragraphs as they were. The notes above are the paragraphs\' '
                 'history from before the move.'),
    },
    'hardest': {
        'head': '#### Before You Tell the Hardest Stuff', 'end': '\n## Other Folks Also Have Hooks',
        'counts': [9, 7],  # "Mr. Boopaloopa" is two to the splitter
        'shape': [[(1, 1), (1, 2), (2, 4), (2, 6), (2, 7)],
                  [(1, 3), (1, 4), (1, 5), (1, 6)],
                  [(1, 7), (1, 8), (1, 9)],
                  [(2, 1), (2, 2), (2, 3)],
                  [(2, 5)]],
        'note': ('104 A: his two paragraphs in the plain-path-first shape (experiments/t109-installs/reshape_t109.py), every '
                 'sentence his, word for word and used once: what to do first (his "I\'d assume" and his danger lines), then the '
                 'reasons one a paragraph, what a phone or a server keeps, who has to report, his question and why he wouldn\'t '
                 'bother, and his dream narrative. The notes above are the paragraphs\' history from before the move.'),
    },
}


def sentences(p):
    return [x for x in SPLIT.split(p) if x]


def reshape(s, key):
    spec = SECTIONS[key]
    i = s.index('\n' + spec['head'] + '\n') + 1
    j = s.index(spec['end'], i)
    sec = s[i:j]
    reader = re.sub(r'<!--.*?-->', '', sec, flags=re.S)
    paras = [p.strip() for p in reader.split('\n\n')[1:] if p.strip()]
    S = [sentences(p) for p in paras]
    assert [len(x) for x in S] == spec['counts'], (key, [len(x) for x in S])
    used = sorted(x for xs in spec['shape'] for x in xs)
    assert used == sorted((p + 1, k + 1) for p in range(len(S)) for k in range(len(S[p]))), key
    new = [' '.join(S[p - 1][k - 1] for p, k in xs) for xs in spec['shape']]
    assert sorted(sum((sentences(p) for p in new), [])) == sorted(sum(S, [])), key
    for p in paras:
        assert sec.count(p) == 1, (key, p[:60])
    notes = re.findall(r'<!--.*?-->', sec, flags=re.S)
    body = (spec['head'] + '\n\n' + ''.join(n + '\n\n' for n in notes) + '<!-- ' + WHEN + ': ' + spec['note'] + ' -->\n\n'
            + '\n\n'.join(new) + '\n')
    return s[:i] + body + s[j:], paras, new


def main():
    s = ART.read_text(encoding='utf-8')
    out = {}
    for key in SECTIONS:
        s, old, new = reshape(s, key)
        out[key] = (old, new)
        print('==', key)
        for p in new:
            print('%4d | %s' % (len(p.split()), p))
    if '--show' not in sys.argv:
        ART.write_text(s, encoding='utf-8')
        print('installed')
    return out


if __name__ == '__main__':
    main()
