#!/usr/bin/env python3
"""apply_h28.py - round 22's first answer and what it taught, put into the guide (2026-11-07, about 14:25 UTC).

- B331, the not-broken paragraph: Joel's own version from round 22's card (TEACH-NOT-BROKEN, answered 13:51 to 14:02 UTC
  with two Pangram links; the one that passed is his history 68752b7e). Two typos are fixed ("I might feel" to "It might
  feel", "no that" to "or that") and a double space. After the Human base it read Human with its window at High (16f4706a).
  As he sent it, it also read Human, but with its last sentence at Low (93b7eab3). No card: his typos fixed with no
  downside, a kind of change he has approved every time (approval_record.py).
- B401, "unhookable", and B430, the fruit of insight: his move carried ("it might look/feel like X, but Y"). Each read
  Human after the Human base: B401 at High and Medium (5a5cb640), B430 at High (1a9cd0ed). Each keeps what the paragraph
  says, so no card (gate bad-trips-2026-11-07a).

  python3 apply_h28.py      write the guide (GUIDE-SO-FAR.md and its blocks) and print what changed
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
    'B331': ('A bad trip does not prove that you are broken, punished, unspiritual, impure, or permanently damaged. It means '
             'the nervous system, meaning-making system, body, environment, memories, dose, or relationships became '
             'overwhelmed. The response is care rather than blame.'),
    'B401': ('This is not passivity. It is becoming unhookable. A demon can fight hatred, feed on fear, argue with pride, and '
             'seduce grandiosity. Love gives it nothing to grab.'),
    'B430': ("The fruit of insight isn't how cosmic the story sounds. It's whether suffering goes down and love gets more "
             "available."),
}
NEW = {'B331': T.HIS_FIXED, 'B401': T.NEW['B401'], 'B430': T.NEW['B430']}
for bid, old in OLD.items():
    assert UNIT[bid]['md'] == old, (bid, UNIT[bid]['md'])
    UNIT[bid]['md'] = NEW[bid]
after = '\n\n'.join(b['md'] for b in BLOCKS) + '\n'
MD.write_text(after, encoding='utf-8')
BJ.write_text(json.dumps(BLOCKS, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('%d words -> %d (%+d); changed %s' % (len(before.split()), len(after.split()),
                                            len(after.split()) - len(before.split()), ', '.join(OLD)))
