#!/usr/bin/env python3
"""Turn 111: his answers from the turn-110 review sheet (experiments/t111-answers/ANSWERS-20261025-2008.json, exported
2026-10-25 20:08 UTC), put in word for word.

- S1 approved: Hear the Guard First in the agreed order (experiments/t110-installs/reshape_t110.py, its admitted sentences).
- S3 revised: the agreed order, with his "So I'd ask this person" for "So I'd ask them" (the cold read's note on the card).
- C3 to C9, C11, C12 approved: the nine cuts, exactly as the sheet showed them.
- C10 rejected, with his note: the blessing line stays, his sentence follows it, and his cut of "Say they're the one who
  always remembers your appointments." from the next paragraph.
- P2 and P5 approved: the wording shown on the sheet.
- P6 revised: Just Like Me's second paragraph is his sentence, with the tonglen link kept; and his cut of "Some of them make
  it worse trying to get away from it. Just like you, sometimes. 😅" from the first.
- Q1 answered with his sentence, "Once a truce is made, we can begin to let down our defenses.", in place of "What people
  most often say helped is letting their defenses down."; Q2 and Q3 answered with their basis, no text change.

Each change gets a note above its paragraph, and the check fails unless every old text is in the article exactly once.

  python3 apply_t111.py [--show]"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1] / 'HUMANIZED-ARTICLE-SO-FAR.md'
sys.path.insert(0, str(HERE.parent / 't110-installs'))
import reshape_t110 as RS  # noqa: E402

A = json.loads((HERE.parent / 't111-answers' / 'ANSWERS-20261025-2008.json').read_text(encoding='utf-8'))
ITEMS = {x['id']: x for x in A['items']}
REV = json.loads((HERE.parent / 't110-review' / 'REVIEW.json').read_text(encoding='utf-8'))
SUG = {x['id']: x for x in REV['suggestions']}
WHEN = 'Turn 111 (his answers of 2026-10-25 20:08 UTC from the turn-110 review sheet, experiments/t111-answers/ANSWERS-20261025-2008.json)'
s = ART.read_text(encoding='utf-8')


def once(old, new, note=None):
    """Replace OLD with NEW in the article, OLD there exactly once; NOTE goes above the paragraph that holds it."""
    global s
    assert s.count(old) == 1, (s.count(old), old[:80])
    i = s.index(old)
    s = s[:i] + new + s[i + len(old):]
    if note:
        p = s.rfind('\n\n', 0, i) + 2
        s = s[:p] + '<!-- %s: %s -->\n\n' % (WHEN, note) + s[p:]


def change(before, after):
    """The changed piece of a sheet edit, (old, new), with the least context around it that is in the article's Markdown
    exactly once (a link's Markdown can sit right beside a cut, so the context grows a character at a time from none)."""
    a = 0
    while a < min(len(before), len(after)) and before[a] == after[a]:
        a += 1
    z = 0
    while z < min(len(before), len(after)) - a and before[len(before) - 1 - z] == after[len(after) - 1 - z]:
        z += 1
    hi_b, hi_a = len(before) - z, len(after) - z
    for k in range(0, 60):
        for lo, hi in ((max(0, a - k), k), (a, k), (max(0, a - k), 0)):
            old = before[lo:hi_b] + before[hi_b:hi_b + hi]
            new = after[lo:hi_a] + before[hi_b:hi_b + hi]
            if old and s.count(old) == 1:
                return old, new
    raise SystemExit('no unique piece for %r' % before[a:hi_b][:80])


# S1 and S3: the agreed order (its admitted sentences), then his word change in S3
assert ITEMS['S1']['status'] == 'approved' and ITEMS['S3']['status'] == 'revise'
s = RS.install(s, 'guard', WHEN + ': S1 approved, the order GPT\'s review and mine agreed on (experiments/t110-review/AGREED.md, '
               'reshape_t110.py): his question, then the exchange in one paragraph in his own order from before turn 109, then one '
               'case a paragraph, with the three sentences the owner-delivery gate admitted (experiments/t110-gate/GATE.md). Hear '
               'the Guard First read Human as a section in exactly this text (t110_sec_guard_b).')
s = RS.install(s, 'hardest', WHEN + ': S3 in his version: the agreed order (his danger lines back after the dream line they limit), '
               'with his "So I\'d ask this person" for "So I\'d ask them". The agreed order read Human as a section (t110_sec_hardest).')
once('So I’d ask them, before handing over any tricky specifics', 'So I’d ask this person, before handing over any tricky specifics')

# the nine approved cuts, and P2 and P5, exactly as the sheet showed them
for sid in ('C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C11', 'C12', 'P2', 'P5'):
    assert ITEMS[sid]['status'] == 'approved', sid
    e = SUG[sid]['edits'][0]
    old, new = change(e['before'], e['after'])
    what = ('%s approved: the cut the sheet showed (%s)' % (sid, SUG[sid]['what']) if sid.startswith('C')
            else '%s approved: the wording the sheet showed (%s)' % (sid, SUG[sid]['what']))
    once(old, new, what)

# C10: rejected, with his note
c10 = ITEMS['C10']
assert c10['status'] == 'rejected'
once("Having someone like that while you're struggling can be an enormous blessing.",
     "Having someone like that while you're struggling can be an enormous blessing. If it's more distributed, with various people "
     "you can count on for small parts, that can be more sustainable, even if it doesn't feel as monumental.",
     'C10 rejected, his note: "i\'m trying to instill gratitude and also show that not everyone has this blessing in their life... '
     'altho i should probably also not assume that someone does. let\'s add after that ..." The blessing line stays, and his sentence follows it.')
once("Say they're the one who always remembers your appointments. Over time, reparenting",
     'Over time, reparenting',
     'His cut, with C10: "i\'m surprised you didn\'t notice the next sentence after this is redundant. cut "Say they\'re the one who '
     'always remembers your appointments.""')

# P6: his sentence for Just Like Me's second paragraph, and his cut in the first
assert ITEMS['P6']['status'] == 'revise'
his = ITEMS['P6']['your_version'].strip()
assert his.startswith("This is sort of a gentler version of Tibetan Buddhism's tonglen practice")
his_md = his.replace("Tibetan Buddhism's tonglen practice", "Tibetan Buddhism's [tonglen](https://www.lionsroar.com/how-to-practice-tonglen-meditation/) practice")
once("If you've tried Pema Chödrön's [tonglen](https://www.lionsroar.com/how-to-practice-tonglen-meditation/), this is a gentler cousin, "
     "and normal breathing is fine. Whoever hurt you might come to mind, too. I'd leave out forgiving them and picturing their childhood.",
     his_md,
     'P6 revised: the paragraph is his sentence, with the tonglen link it had since turn 71. His note: "also not sure why it was '
     'decided to leave out forgiving" (the guide had "This is not a demand to forgive an abuser, imagine their childhood, or open '
     'contact while you are flooded"; turn 71 made it "Forgiving them isn\'t part of it", and turn 93\'s tell fix "I\'d leave out", '
     'experiments/t111-answers/TRACES.md).')
once(" Some of them make it worse trying to get away from it. Just like you, sometimes. 😅 Wish all of you",
     ' Wish all of you',
     'His cut, with P6: "cut this, idk how this got put in, but it sticks out strangely: "Some of them make it worse trying to get '
     'away from it. Just like you, sometimes. 😅"" (my turn-65 draft of the guide\'s script line, experiments/t111-answers/TRACES.md).')

# Q1: his sentence
assert 'truce' in ITEMS['Q1']['comment']
once('What people most often say helped is letting their defenses down.',
     'Once a truce is made, we can begin to let down our defenses.',
     'Q1, his answer: "change to "Once a truce is made, we can begin to let down our defenses.""')

if '--show' in sys.argv:
    print(len(s))
else:
    ART.write_text(s, encoding='utf-8')
    print('installed')
