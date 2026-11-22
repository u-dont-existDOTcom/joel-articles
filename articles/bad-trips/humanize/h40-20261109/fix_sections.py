#!/usr/bin/env python3
"""fix_sections.py - what belongs in each section: the moves that keep the meaning and lose nothing, made without a card.

His rule after the contents (2026-11-09 17:22 UTC, HELPER-NOW): "make sure the ToC is optimized then we can make sure the
stuff in each section is what belongs there". Three fresh readers read the guide section by section for that
(section-read/READER-1..3.md); RESULTS.md has every proposal's fate. These five only move whole paragraphs, word for word,
to the section they belong in, so they go in without a card (gate bad-trips-2026-11-07a; his 2026-11-07 12:08 UTC "you're
asking me to approve things that are clearly good"):

1. The bridge into tripsitting ("Once the body is stable and those tools have done what they can ...") with its picture
   and divider: round 30's contents moved Some Remedies Require More Caution to the top of the remedies, and the bridge
   went with it, so it said "those tools" before any of them. It goes back to the end of the remedies, before
   Tripsitting Yourself or Others, where his post had it.
2. Active Seizure: "Call medics for a convulsive seizure lasting about five minutes ..." comes up after the rescue
   medicine, so first aid, rescue medicine and when to call medics come first, ahead of the six paragraphs on what else
   may help.
3. Zeolite: how he takes it ("Most sober people don't feel much from zeolite. ... I put a spoonful into water ...")
   comes before how he prepares it, so someone in trouble reads how to use it first.
4. The Movement evidence note goes to Stillness or Movement?: the movement lines it was written for (the post's Body and
   Ordinary world items) were cut from the menu in the deduplication because Stillness or Movement? says them.
5. After the Storm: "No "another ceremony will fix this" reflex." and the three paragraphs after it are for everyone after
   a hard trip, so they join the opening paragraph; What Kind of Aftermath Is This? keeps the kinds of lingering
   symptoms, and Bring in mental-health support when: now follows them directly.

  python3 fix_sections.py
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1]
BJ, MD = ART / 'GUIDE-SO-FAR-blocks.json', ART / 'GUIDE-SO-FAR.md'
blocks = json.loads(BJ.read_text(encoding='utf-8'))
before = '\n\n'.join(b['md'] for b in blocks) + '\n'
assert before == MD.read_text(encoding='utf-8'), 'the blocks and the guide disagree'
words = sorted(before.split())


def ids():
    return [b['id'] for b in blocks]


def move(group, to_before):
    """Take the blocks GROUP (consecutive, in order) out and put them just before block TO_BEFORE."""
    k = ids().index(group[0])
    assert ids()[k:k + len(group)] == group, (group, ids()[k:k + len(group)])
    taken = blocks[k:k + len(group)]
    del blocks[k:k + len(group)]
    j = ids().index(to_before)
    blocks[j:j] = taken


def text(bid):
    return blocks[ids().index(bid)]['md']


assert text('B224').startswith('Once the body is stable and those tools have done what they can')
assert text('B223') == text('B226') == '---' and text('B225').startswith('![](')
assert ids()[ids().index('B222') + 1] == 'B223' and ids()[ids().index('B216') + 1] == 'B227'
move(['B224', 'B225', 'B226'], 'B227')            # 1: ... niacin, ---, the bridge, its picture, ---, Tripsitting

assert text('B112').startswith('Call medics for a convulsive seizure')
move(['B112'], 'N-WARN')                          # 2: first aid, rescue medicine, call medics, then the rest

assert text('B158').startswith('Most sober people don\'t feel much from zeolite.')
move(['B158'], 'B155')                            # 3: how he takes it, then how he prepares it

assert text('B313').startswith('**Movement evidence note:**')
move(['B313'], 'B252')                            # 4: after parallel processing, in Stillness or Movement?

assert text('B427') == '**No "another ceremony will fix this" reflex.**'
assert ids()[ids().index('B427'):ids().index('B427') + 5] == ['B427', 'B428', 'B429', 'B430', 'B96']
move(['B427', 'B428', 'B429', 'B430'], 'B421')    # 5: after the opening paragraph, before its picture

after = '\n\n'.join(b['md'] for b in blocks) + '\n'
assert sorted(after.split()) == words, 'a move changed the words'
MD.write_text(after, encoding='utf-8')
BJ.write_text(json.dumps(blocks, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
for a, z in (('B215', 'B228'), ('B110', 'N-WARN'), ('B154', 'B155'), ('B251', 'B294'), ('B420', 'B424')):
    i, j = ids().index(a), ids().index(z)
    print(' '.join(ids()[i:j + 1]))
