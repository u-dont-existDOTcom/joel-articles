#!/usr/bin/env python3
"""Turn 108: a worked example for Joel's question of 2026-10-25 12:39 UTC ("i'm having a hard time thinking of how it
could be as engaging as my natural writing without losing the important complexities"). Hear the Guard First, as it is,
beside the same sentences in a different shape: the plain path first, then one situation per paragraph, each opening with
the situation (labelled on the page). Every sentence is kept word for word and used once (checked below); only their order
and the paragraph breaks change. Writes DEMO.md. Not checked in Pangram: it's a shape for him to judge first."""
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1] / 'HUMANIZED-ARTICLE-SO-FAR.md'
md = re.sub(r'<!--.*?-->', '', ART.read_text(encoding='utf-8'), flags=re.S)
i = md.index('### Hear the Guard First')
j = md.index('\n### ', i + 10)
now = [p.strip() for p in md[i:j].split('\n\n')[1:] if p.strip()]
assert len(now) == 5


def sents(p):
    return [s for s in re.split(r'(?<=[.!?"”)])\s+(?=[A-Z"“(])', p) if s]


S = [sents(p) for p in now]
# Whose paragraphs these are (the article's notes): P1, P4 and P5 mine; P2 and P3 his, word for word.
WHO = ['mine', 'his', 'his', 'mine', 'mine']
# The new shape: (what the paragraph is for, [(paragraph, sentence) ...]), 1-based.
SHAPE = [
    ('The plain path, as if nothing goes wrong', [(1, 1), (1, 5), (2, 3), (2, 4), (2, 5), (2, 6)]),
    ('If the Nurturer voice feels wrong for it, or isn\'t there yet', [(1, 2), (1, 3), (1, 4)]),
    ('If it says this is one more performance', [(1, 6), (2, 1), (2, 2), (2, 7), (2, 8)]),
    ('If it won\'t step back', [(4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6)]),
    ('If it\'s been calling all this stupid', [(4, 7), (4, 8), (4, 9), (4, 10), (4, 11)]),
    ('The long game', [(3, k) for k in range(1, len(S[2]) + 1)]),
    ('When the guard is your own self-blame', [(5, k) for k in range(1, len(S[4]) + 1)]),
]
used = [x for _, xs in SHAPE for x in xs]
every = [(p + 1, k + 1) for p in range(5) for k in range(len(S[p]))]
assert sorted(used) == sorted(every), (sorted(set(every) - set(used)), sorted(set(used) - set(every)))
new = [' '.join(S[p - 1][k - 1] for p, k in xs) for _, xs in SHAPE]

out = ['# Hear the Guard First, in a simpler shape (a worked example, turn 108)', '',
       'Joel, 2026-10-25 12:39 UTC: "if i had written this whole guide myself i\'m quite sure it would not look as detailed and '
       'hedgy and coursey as it does -- it would be much simpler, but i\'m having a hard time thinking of how it could be as '
       'engaging as my natural writing without losing the important complexities."', '',
       'The same sentences, word for word, in a different order and with different paragraph breaks: the plain path first, as '
       'if nothing goes wrong, and then one situation per paragraph, the way your When to Change the Strategy gives each '
       'situation its own paragraph. Nothing is added or cut. P2 and P3 of the section are yours; P1, P4 and P5 are mine. The '
       'labels in italics are only for this page. If it went in, a few words would change so each paragraph names its '
       'situation in its first sentence ("That part might say" for "It might say", say), and those would be yours to OK. It '
       'isn\'t checked in Pangram yet, since the shape is yours to judge first.', '',
       '## The new shape', '']
for (what, xs), p in zip(SHAPE, new):
    src = ', '.join('P%d.%d' % x for x in xs)
    out += ['*%s* (%s)' % (what, src), '', p, '']
out += ['## As it is now', '']
for k, (p, who) in enumerate(zip(now, WHO), 1):
    out += ['*P%d (%s)*' % (k, who), '', p, '']
out += ['P*n*.*m* is paragraph *n*\'s sentence *m* in the section as it is now. Made by [make_demo.py]'
        '(https://github.com/u-dont-existDOTcom/joel-articles/blob/handoff/claude-dangerous-adult-20260924-1631/articles/'
        'inner-child-therapy/experiments/t108-shape/make_demo.py), which checks that every sentence is used once.']
(HERE / 'DEMO.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
print('\n\n'.join(new))
print('\nparagraph words now:', [len(p.split()) for p in now], ' new:', [len(p.split()) for p in new])
