#!/usr/bin/env python3
"""Turn 114: his answers from the turn-113 review sheet (experiments/t114-answers/ANSWERS-20261026-0052.json, exported
2026-10-26 00:52 UTC from the sheet built 00:40:38 UTC), put in word for word.

- All eleven change cards approved: each section as the sheet showed it (experiments/t113-shape/proposals.py, SECTIONS):
  its case headings (####), the first words a heading now says dropped, its splits, the one move in Start With Whatever
  Showed Up, and his 109 A in Borrow Love. Every heading with new words is the text the owner-delivery gate admitted
  (experiments/t113-gate/<NAME>/FOR-JOEL.txt).
- Q-me answered "you": "makes me more grounded, truthful, and free" becomes "makes you more grounded, truthful, and free".

Each old paragraph is replaced in place by what it became, so every turn note stays where it was, above the paragraph it
describes; one turn-114 note goes above each section's first changed paragraph. The check: with the notes taken out, the
article is PROPOSAL-ARTICLE.md with his "you", and every gated heading is its FOR-JOEL.txt text. Applied once.

  python3 apply_t114.py [--show]"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
EXP = HERE.parent
ART = EXP.parent / 'HUMANIZED-ARTICLE-SO-FAR.md'
sys.path.insert(0, str(EXP / 't113-shape'))
import proposals as P  # noqa: E402

A = json.loads((EXP / 't114-answers' / 'ANSWERS-20261026-0052.json').read_text(encoding='utf-8'))
ITEMS = {x['id']: x for x in A['items']}
NAMES = {tuple(k.split('|', 1)): v for k, v in json.loads((EXP / 't113-gate' / 'NAMES.json').read_text(encoding='utf-8')).items()}
WHEN = ('Turn 114 (his answers of 2026-10-26 00:52 UTC from the turn-113 review sheet, '
        'experiments/t114-answers/ANSWERS-20261026-0052.json)')
WHAT = {
    'H-guard': 'four case headings, his "If it\'s been calling all this stupid" and three the owner-delivery gate admitted',
    'H-start': 'six case headings (his "If you do get an answer", "If it tells you to do something" and his stop rule\'s whole '
               'condition, and three the gate admitted), the answer paragraph split before "If it tells you to do something", and '
               '"How you picture all that is up to you ..." moved up three sentences, to stay with the forms an answer can take',
    'H-change': 'five case headings (his "How many tries would I give it?" and his condition "If you keep following the reparenting '
                'steps correctly without getting the expected results", and three the gate admitted), and the last paragraph split '
                'before that condition',
    'H-escape': 'seven case headings (his "What you mix" and six the gate admitted), the paranoia paragraph split before "If you '
                'can’t clearly understand what happened yourself", the spaced-out paragraph split before "And don\'t suddenly stop a '
                'medication", whose "And" goes, and "Your own drug history matters too." and "Say you keep coming back from trips '
                'confused or spaced out." out, since headings take their place',
    'H-fake': 'three case headings, each the paragraph\'s own first sentence or clause, which then leaves it',
    'H-therapist': 'four case headings, his "Inner Child Reparenting therapists", "Before choosing a therapist" and "AI therapy", and '
                   '"If you want a licensed therapist", which the gate admitted',
    'H-hooks': 'four case headings, his "If a relationship keeps making you feel less safe", "If they\'ve actually hurt or threatened '
               'you" and "If you really did hurt them", and "Can they change?", which the gate admitted; the danger line split into its '
               'own paragraph, and "Also easier said than done" without its "Also"',
    'H-borrow': 'three case headings, his "For warmth" and "For protecting" and "For guiding", which the gate admitted',
    'R-helping': 'its first paragraph split in four, every sentence kept',
    'R-forgive': 'its last paragraph split before "So a boundary can still be right."',
    'W-solomon': 'his 109 A: "and the blind spot behind it even has a name", which the gate admitted, the rest of his sentence as it was',
}
NOTE = '<!-- %s: %s approved, %s. -->'


def plain(t):
    return re.sub(r'\s+', ' ', P.plain(t)).strip()


def install(blocks, sec):
    """Replace each old paragraph of SEC's section in place by what it became; return the index of the first changed block."""
    i, j, paras = P.section_slice(blocks, sec['line'])
    old = [blocks[k] for k in paras]
    work = list(blocks)
    _, items, new_words, probs = P.apply_section(work, sec)
    assert not probs, probs
    for w in new_words:      # every gated word on the sheet is its admitted text
        key = (sec['id'], w['new']) if w['kind'] == 'heading' else None
        if key:
            name = NAMES[key]
            assert (EXP / 't113-gate' / name / 'FOR-JOEL.txt').read_text(encoding='utf-8') == w['new'], name
    olds = [plain(o) for o in old]
    groups, pending = {k: [] for k in range(len(old))}, []
    for kind, md in items:
        if kind != 'p':
            pending.append('#' * int(kind[1]) + ' ' + md)
            continue
        t = plain(md)
        k = next((n for n, o in enumerate(olds) if t == o or o.endswith(t[1:]) or t[1:] in o), None)
        if k is None and sec['id'] == 'W-solomon':
            k = next(n for n, o in enumerate(olds) if o[:60] == t[:60])
        if k is None:        # the paragraph the moved sentence joined: its first sentence's own
            first = re.split(r'(?<=[.!?])\s+', t)[0]
            k = next(n for n, o in enumerate(olds) if first[1:] in o)
        groups[k] += pending + [md]
        pending = []
    assert not pending and all(groups.values()), sec['id']
    first = None
    for k, b in zip(range(len(old)), paras):
        new = '\n\n'.join(groups[k])
        if new != blocks[b]:
            blocks[b] = new
            first = b if first is None else first
    return first


md = ART.read_text(encoding='utf-8')
assert 'Turn 114 (his answers of 2026-10-26 00:52 UTC' not in md, 'already applied'
blocks = [b.strip('\n') for b in re.split(r'\n\s*\n', md.strip('\n'))]
notes_at = []
for sec in P.SECTIONS:
    assert ITEMS[sec['id']]['status'] == 'approved', sec['id']
    b = install(blocks, sec)
    assert b is not None, sec['id']
    notes_at.append((b, NOTE % (WHEN, sec['id'], WHAT[sec['id']])))
# Q-me: "you"
assert ITEMS['Q-me']['status'] == 'answered' and ITEMS['Q-me']['comment'].strip() == 'you'
q = [n for n, b in enumerate(blocks) if b.startswith('If you still feel like a kid inside')]
assert len(q) == 1 and blocks[q[0]].count('makes me more grounded, truthful, and free.') == 1
blocks[q[0]] = blocks[q[0]].replace('makes me more grounded, truthful, and free.', 'makes you more grounded, truthful, and free.')
notes_at.append((q[0], '<!-- %s: Q-me answered "you": "makes you more grounded, truthful, and free" for "makes me" (two fresh '
                       'reviewers in turn 110 had tripped on the switch from "you"). -->' % WHEN))
for b, note in sorted(notes_at, reverse=True):
    blocks.insert(b, note)
out = '\n\n'.join(blocks) + '\n'

# the check: without notes, the article is PROPOSAL-ARTICLE.md with his "you"
def bare(t):
    t = re.sub(r'<!--.*?-->', '', t, flags=re.S)
    return [b.strip() for b in re.split(r'\n\s*\n', t) if b.strip()]


prop = [x.replace('makes me more grounded, truthful, and free.', 'makes you more grounded, truthful, and free.')
        if x.startswith('If you still feel like a kid inside') else x
        for x in bare((EXP / 't113-shape' / 'PROPOSAL-ARTICLE.md').read_text(encoding='utf-8'))]
assert bare(out) == prop, 'the installed article is not the proposal with his "you"'
assert out.count('makes you more grounded, truthful, and free.') == 1

if '--show' in sys.argv:
    print(len(md), '->', len(out))
else:
    ART.write_text(out, encoding='utf-8')
    print('installed: %d sections and Q-me; %d -> %d characters' % (len(P.SECTIONS), len(md), len(out)))
