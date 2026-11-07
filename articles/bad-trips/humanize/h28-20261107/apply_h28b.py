#!/usr/bin/env python3
"""apply_h28b.py - the second batch of his round-22 move, put into the guide (2026-11-07, about 14:35 UTC).

Each of these paragraphs read Human in its own windows after the Human base, where the guide's words read AI. None of
the changes alters what the paragraph says, so none gets a card (gate bad-trips-2026-11-07a):
- B316, No Rash Actions' urgency line: Human, its window Low (3ea94994). The guide's words read 38%.
- B320, the experience-content paragraph: its own windows Human Low, Medium and Low (948da7dc). The test's one AI
  window was the base's first. The guide's words read 41% and 50%.
- B361, Why Bad Trips Tend to Happen's lesson line: Human, its window High (4109c05e).
- B382 and B383, Sorrow's deepest utility: Human Low (5f70db5e). The guide's words read 83% with the Send love list. The
  list after them still reads AI Low and stays on the later list.

  python3 apply_h28b.py      write the guide (GUIDE-SO-FAR.md and its blocks) and print what changed
"""
import importlib.util
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1]
BJ = ART / 'GUIDE-SO-FAR-blocks.json'
MD = ART / 'GUIDE-SO-FAR.md'
spec = importlib.util.spec_from_file_location('build_tests', HERE / 'build_tests.py')
T = importlib.util.module_from_spec(spec)
spec.loader.exec_module(T)

BLOCKS = json.loads(BJ.read_text(encoding='utf-8'))
before = MD.read_text(encoding='utf-8')
assert '\n\n'.join(b['md'] for b in BLOCKS) + '\n' == before, 'the blocks and the guide disagree'
UNIT = {b['id']: b for b in BLOCKS}
OLD = {
    'B316': 'An intense altered state can make everything feel final, cosmic, and urgent. Urgency does not make action safe.',
    'B320': ('Treat trip content first as **experience-content**, rather than fact-content. "I saw it" does not create a duty '
             'to act. "It felt cosmic" does not make obedience wise.'),
    'B361': ('Every hard experience is not a profound lesson. Sometimes the lesson is just to lower the dose or stop the '
             'practice, get some sleep and something to eat, pick safer people, and admit that the room is bad.'),
    'B382': ('The mistake people often make in love states is simply enjoying the love – or sending heart emojis to everybody. '
             'That is nice, but it is not the deepest utility.'),
    'B383': 'The deepest utility is sending love to the places where love is missing.',
}
for bid, old in OLD.items():
    assert UNIT[bid]['md'] == old, (bid, UNIT[bid]['md'])
    UNIT[bid]['md'] = T.NEW[bid]
after = '\n\n'.join(b['md'] for b in BLOCKS) + '\n'
MD.write_text(after, encoding='utf-8')
BJ.write_text(json.dumps(BLOCKS, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('%d words -> %d (%+d); changed %s' % (len(before.split()), len(after.split()),
                                            len(after.split()) - len(before.split()), ', '.join(OLD)))
