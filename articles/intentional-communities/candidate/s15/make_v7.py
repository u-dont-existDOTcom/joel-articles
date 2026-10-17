"""Section 15 draft v7 (2026-10-17): v6 (H1-P4 c, H3-P2 l) with the fixes of trace round r7 (review-r7/DISPOSITIONS-r7.md).
- H1-P4: "so much is taken care of by the extended family" made the family handle most of it, where the published says these
  things often pass through it. Two variants go to Pangram (330g): g, "things often go through" (the published words), and m,
  "a lot often goes through" (closer to Emulate's "so much"); CHOICE picks one.
- H2-P1: the published "either" (trace r7 T1: LOST): "No, not that either!"
Writes v7.md and v7-variants.json. Run from this folder: python3 make_v7.py [CHOICE]"""
import json, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
t = (HERE / 'v6.md').read_text(encoding='utf-8')
OLD4 = ("In the villages and families I've spent time around, so much is taken care of by the extended family and the local "
        "memory, alongside the formal systems.")
assert t.count(OLD4) == 1
V = {
 'g': "In the villages and families I've spent time around, things often go through the extended family and the local memory, "
      "alongside the formal systems.",
 'm': "In the villages and families I've spent time around, a lot often goes through the extended family and the local memory, "
      "alongside the formal systems.",
}
OLD1 = "kept its communal paradise? No! The warmth has hard limits here,"
assert t.count(OLD1) == 1
t = t.replace(OLD1, "kept its communal paradise? No, not that either! The warmth has hard limits here,")
choice = sys.argv[1] if len(sys.argv) > 1 else 'g'
P4 = [b for b in t.split('\n\n') if b.startswith(OLD4)][0]
VARS = {k: P4.replace(OLD4, v) for k, v in V.items()}
t = t.replace(P4, VARS[choice])
(HERE / 'v7.md').write_text(t, encoding='utf-8')
(HERE / 'v7-variants.json').write_text(json.dumps({'H1-P4': VARS, 'chosen': choice}, ensure_ascii=False, indent=1) + '\n',
                                       encoding='utf-8')
print('wrote v7.md with H1-P4', choice)
