#!/usr/bin/env python3
"""apply_his_r22.py - his round-22 versions of 15:38 UTC put into the guide (both teaching cards answered "revise" with his
own version; ../../review/r22/ANSWERS-R22-20261107-1538.json).

- B331, the not-broken paragraph: his final version (Pangram history 96a465a6, Human High alone). It replaces the version
  of 14:25 (his first, typos fixed). Four typos are fixed: "I might feel" to "It might feel", "no that" to "or that", a
  double space, and "Be kind about to yourself" to "Be kind to yourself". After the Human base it reads Human, High with
  its last sentence Medium (3b397872).
- B420, After the Storm's first paragraph: his version, the one he prefers ("altho i like the version where i'm betting
  better, sounds more human"; Pangram history ff7e9099, Human High alone), with a double space fixed. After the Human base
  it reads Human; its first sentence shares a Low window with the base's reminder (7b027e98). He cut "Don't rush to turn a
  hard experience into content" ("what does "content" mean? ... and it's redundant"), so W122's "rush" and "hard" go
  (FIDELITY-KEYS-R22.json records it).

  python3 apply_his_r22.py      write the guide (GUIDE-SO-FAR.md and its blocks) and print what changed
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
spec2 = importlib.util.spec_from_file_location('b28', HERE.parent / 'h28-20261107/build_tests.py')
T28 = importlib.util.module_from_spec(spec2)
spec2.loader.exec_module(T28)

BLOCKS = json.loads(BJ.read_text(encoding='utf-8'))
before = MD.read_text(encoding='utf-8')
assert '\n\n'.join(b['md'] for b in BLOCKS) + '\n' == before, 'the blocks and the guide disagree'
UNIT = {b['id']: b for b in BLOCKS}
OLD = {
    'B331': T28.HIS_FIXED,
    'B420': ("Don't rush to turn a hard experience into content. Sleep. Eat simple food. Drink water. Walk. Journal. Pray and "
             "meditate gently. Talk with one grounded person, rather than twenty chaotic people. Don't make huge decisions, "
             "diagnose yourself from one intense night, or assume every vision was literal and every fear was false. Let the "
             "system settle."),
}
NEW = {'B331': T.HIS_NB, 'B420': T.HIS_AS}
for bid, old in OLD.items():
    assert UNIT[bid]['md'] == old, (bid, UNIT[bid]['md'])
    UNIT[bid]['md'] = NEW[bid]
after = '\n\n'.join(b['md'] for b in BLOCKS) + '\n'
MD.write_text(after, encoding='utf-8')
BJ.write_text(json.dumps(BLOCKS, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('%d words -> %d (%+d); changed %s' % (len(before.split()), len(after.split()),
                                            len(after.split()) - len(before.split()), ', '.join(OLD)))
