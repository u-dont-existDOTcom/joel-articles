"""Batch f1102b: the second try for the two stretches of batch f1102 whose fix still left a Human (Low) window
(RESULTS.md), each with a new diagnosis (the six-try rule; their stretch lineages' try 2 of 2).

- The two-hand practice: the Low window of f1102-119 took in the last two sentences of the paragraph before it as well
  as the breathing line ("Don't pretend to feel something you don't. Let it go back and forth between your heart and your
  inner child, like a real conversation. Keep breathing gently the whole way through."). Those two are ours (not in his
  published guide or his inner child guide), a warning closer and a simile closer, and the second repeats his own loop
  line two sentences up ("so it goes around like a loop"). F-118 cuts them and keeps the no-faking point in the warmth
  sentence; F-119 stays as checked.
- Indirect language and re-entry cues: f1102-762's new disclaimer sentence still read Human (Low) by itself. F-762b puts
  the Nimja line where Nimja is named, with his "by the way" (his first account: "either." became "by the way."), and says
  the other two caveats with a plain idiom ("not on the hook").

  python3 articles/inner-signal/humanize/fix-20261102/f1102/fixes_f1102b.py
"""
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import fixes_f1102 as fx  # noqa: E402

EDITS_B = [
    ('F-118', 118, 'ours',
     "If you can't find any warmth today, just leave your hands where they are and notice what's there. Don't pretend to "
     "feel something you don't. Let it go back and forth between your heart and your inner child, like a real conversation.",
     "If you can't find any warmth today, don't fake it, just leave your hands where they are and notice what's there.",
     'with F-119: two closers of ours cut (a warning and a simile that repeats his loop line); "don\'t fake it" keeps the '
     'no-pretending point inside the warmth sentence'),
    ('F-762b', 762, 'ours',
     "and [his tutorial on triggers](https://learn.nimja.com/techniques/triggers). The information on these techniques comes "
     "from these sources, but that doesn't mean they validate every NLP claim, or that every example suits trauma work "
     "(Nimja did not write or endorse this guide).",
     "and [his tutorial on triggers](https://learn.nimja.com/techniques/triggers) (he didn't write or endorse this guide, by "
     "the way). They're where these techniques come from, but they're not on the hook for every NLP claim I make, or for "
     "whether every example suits trauma work.",
     'second try: the Nimja line next to his name, and the two caveats said plainly; replaces F-762'),
]


def apply(md, take):
    """The guide with the f1102 edits named in take (ours) and F-118, F-762b when named."""
    a = [e for e in fx.EDITS if e[0] in take and e[2] == 'ours']
    raw = re.split(r'\n\s*\n', fx.apply(md, ()).rstrip('\n'))
    for eid, b, kind, old, new, why in a + [e for e in EDITS_B if e[0] in take]:
        assert raw[b].count(old) == 1, (eid, raw[b][:80])
        raw[b] = raw[b].replace(old, new)
    return '\n\n'.join(raw) + '\n'


if __name__ == '__main__':
    for e in EDITS_B:
        print('%s (block %d)\n  - %s\n  + %s\n' % (e[0], e[1], e[3], e[4]))
