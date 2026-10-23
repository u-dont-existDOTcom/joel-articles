#!/usr/bin/env python3
"""Turn 101: Joel's answers of 2026-10-23 14:05 UTC (experiments/t101-answers/JOEL-20261023-1405.md).

- 91.1 B: Borrow One Competency at a Time in the turn-100 test's order (experiments/t100-readers-edit/), with the
  near-repeat cut: old P6's first sentence ("Most of us wouldn't open up to somebody who'd only just stopped being mean,
  or let them take care of us.") is out; its second sentence ("That takes warmth, and if there isn't any yet, borrow
  some.") now ends old P5, since its "That" points at P5's last words ("for them to trust you"). Each paragraph keeps the
  notes above it.
- 91.2 A: the heading "Instead of Blame" (h3) in Love Doesn't Have to Wait for Trust, before "Your little one might not
  be the only one getting accused." and the notes above that paragraph.
- 93.1: his words for the first sentence of the "Of course" paragraph, "Of course, that’s not to say you should not try
  to suffer less, or get away from abusers" (the period added).
- 93.2: his two sentences on the endless loop added onto the prosperity paragraph, as he pasted them ("we can add that
  onto the para about prosperity philosophy"); its first three sentences keep the characters they had.
"""
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1] / 'HUMANIZED-ARTICLE-SO-FAR.md'
SRC = 'experiments/t101-answers/JOEL-20261023-1405.md'
P6_FIRST = "Most of us wouldn't open up to somebody who'd only just stopped being mean, or let them take care of us. "
P6_SECOND = "That takes warmth, and if there isn't any yet, borrow some. "
OLD_OF_COURSE = 'Of course, that’s not to say you should not try to suffer less. The point'
NEW_OF_COURSE = 'Of course, that’s not to say you should not try to suffer less, or get away from abusers. The point'
PROSPERITY_END = 'I’m ultimately reaching for something much deeper.'
ADDED = " Because getting what you want is an endless loop, and it doesn't lead to being content with less. When you can see that less is more, at a deeper level, that's where the real gratitude flourishes."


def note(what):
    return '<!-- Turn 101 (his answers of 2026-10-23 14:05 UTC, ' + SRC + '): ' + what + ' -->'


def units(lines):
    """A section's body as units: (the comment lines right above a paragraph, the paragraph), in order."""
    out, pending = [], []
    for l in lines:
        if not l.strip():
            continue
        if l.startswith('<!--'):
            pending.append(l)
        else:
            out.append((pending, l))
            pending = []
    return out, pending


def main():
    lines = ART.read_text(encoding='utf-8').split('\n')
    a = lines.index('## Borrow One Competency at a Time')
    b = lines.index('## Borrow Hindsight')
    body, tail = units(lines[a + 1:b])
    assert len(body) == 9, len(body)
    P = {n + 1: u for n, u in enumerate(body)}
    assert P[1][1].startswith('A complete ideal parent') and P[2][1].startswith("If you weren't loved well")
    assert P[5][1].startswith("If the love still isn't coming") and P[6][1].startswith(P6_FIRST + P6_SECOND)
    assert P[7][1].startswith('For protecting') and P[8][1].startswith('The Guide can be you too') and P[9][1].startswith('The thank-you')
    warm = 'For warmth, think' + P[6][1][len(P6_FIRST + P6_SECOND) + len('Think'):]
    assert warm.startswith('For warmth, think of someone you remember fondly.')
    p5 = P[5][1] + ' ' + P6_SECOND.strip()
    order = [
        P[1],
        ([note('91.1 B: the main invitation first, then one borrowing for each job; this is old P6 without its first two sentences, with "For warmth," (the turn-100 test, experiments/t100-readers-edit/BORROW-ONE-COMPETENCY-TEST.md).')], warm),
        P[7], P[8],
        (['### If the Love Isn\'t Coming Yet', note('91.1 B: the troubleshooting under its own heading, in the order it had (old P2 to P5, then P9).')], None),
        P[2], P[3], P[4],
        (P[5][0] + [note('91.1 B: old P6\'s first sentence is cut as a near-repeat of this paragraph\'s last; its second ("That takes warmth, and if there isn\'t any yet, borrow some.") ends this paragraph now.')], p5),
        P[9],
    ]
    new = ['## Borrow One Competency at a Time', '']
    for pre, para in order:
        for c in pre:
            new += [c, '']
        if para is not None:
            new += [para, '']
    for c in tail:
        new += [c, '']
    lines[a:b] = new

    i = next(k for k, l in enumerate(lines) if l.startswith('Your little one might not be the only one getting accused.'))
    j = i
    while lines[j - 1].strip() == '' and lines[j - 2].startswith('<!--'):
        j -= 2
    lines[j:j] = ['### Instead of Blame', '', note('91.2 A: the second half of this section, from blaming an age of you to what you can give your little one now, under its own heading.'), '']

    k = [n for n, l in enumerate(lines) if l.startswith(OLD_OF_COURSE)]
    assert len(k) == 1
    lines[k[0]] = lines[k[0]].replace(OLD_OF_COURSE, NEW_OF_COURSE, 1)
    lines[k[0]:k[0]] = [note('93.1, his words for this paragraph\'s first sentence: "right, change the next sentence in next para to: \\"Of course, that’s not to say you should not try to suffer less, or get away from abusers\\"" (the period added).'), '']

    k = [n for n, l in enumerate(lines) if l.startswith('And I’m certainly not preaching “prosperity philosophy,”')]
    assert len(k) == 1 and lines[k[0]].endswith(PROSPERITY_END)
    lines[k[0]] += ADDED
    lines[k[0]:k[0]] = [note('93.2, his two sentences added onto this paragraph, as he pasted them: "my bad, i was editing the version i had before that. we can add that onto the para about prosperity philosophy".'), '']
    ART.write_text('\n'.join(lines), encoding='utf-8')
    print('installed: 91.1 B, 91.2 A, 93.1, 93.2')


if __name__ == '__main__':
    main()
