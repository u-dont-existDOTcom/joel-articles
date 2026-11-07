#!/usr/bin/env python3
"""apply_r23.py - his round-23 answers of 22:38 UTC put into the guide (../../review/r23/ANSWERS-R23-20261107-2238.json).

- B318, No Rash Actions' list: his own version, as he sent it (Pangram history e1537940, Human High alone; after the
  Human base its paragraph reads Human High, f14f541b). It drops "possessions" from W097's keys ("giving away your BMW"),
  and "make a grand purchase", the item he approved in round 21, became his "buying a new BMW" (FIDELITY-KEYS-R23.json).
- B422 and B423, Minimum Viable Integration (its heading and its four steps): cut as a repeat, as he pointed out ("i also
  feel like this has been said at least twice already"). Step 1 repeats After the Storm's first paragraph and No Rash
  Actions' lock; steps 3 and 4 repeat the questions and the fruit of insight after it; step 2's facts to write down are
  the questions' "what actually happened" and No Rash Actions' "Write it down". No fidelity key rests on it.

  python3 apply_r23.py      write the guide (GUIDE-SO-FAR.md and its blocks) and print what changed
"""
import importlib.util
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1]
BJ = ART / 'GUIDE-SO-FAR-blocks.json'
MD = ART / 'GUIDE-SO-FAR.md'
spec = importlib.util.spec_from_file_location('b', HERE / 'build_tests.py')
T = importlib.util.module_from_spec(spec)
spec.loader.exec_module(T)

BLOCKS = json.loads(BJ.read_text(encoding='utf-8'))
before = MD.read_text(encoding='utf-8')
assert '\n\n'.join(b['md'] for b in BLOCKS) + '\n' == before, 'the blocks and the guide disagree'
UNIT = {b['id']: b for b in BLOCKS}
OLD318 = ("Until you have slept and eaten, don't drive, travel, break up, quit your job, confess everything, confront anybody, "
          "accuse anybody, send the message, post the revelation, give away possessions, make a grand purchase, call your ex, "
          "call your parents to explain the universe, or decide that you are permanently enlightened or permanently damaged.")
assert UNIT['B318']['md'] == OLD318, UNIT['B318']['md']
UNIT['B318']['md'] = T.HIS_DT
assert UNIT['B422']['md'] == '### Minimum Viable Integration' and UNIT['B423']['md'].startswith('1. **First 24 hours:**')
BLOCKS = [b for b in BLOCKS if b['id'] not in ('B422', 'B423')]
after = '\n\n'.join(b['md'] for b in BLOCKS) + '\n'
MD.write_text(after, encoding='utf-8')
BJ.write_text(json.dumps(BLOCKS, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('%d words -> %d (%+d); B318 his version; B422, B423 cut' % (len(before.split()), len(after.split()),
                                                                   len(after.split()) - len(before.split())))
