"""Section 15 draft v8 (2026-10-17): v7 with the fix of trace r7 T2 (review-r7/trace-T2.md): H3-P2's "because they're
expected to carry everybody" dropped the published "may" ("the person earning cash may still be expected to carry
everybody"), so a reader took the expectation as certain. H1-P4 keeps the two variants of v7 (g, m) for batch 330g.
Writes v8.md and v8-variants.json. Run from this folder: python3 make_v8.py [CHOICE]"""
import json, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
choice = sys.argv[1] if len(sys.argv) > 1 else 'g'
v7 = json.loads((HERE / 'v7-variants.json').read_text(encoding='utf-8'))
t = (HERE / 'v7.md').read_text(encoding='utf-8')
P4 = v7['H1-P4'][v7['chosen']]
assert t.count(P4) == 1
t = t.replace(P4, v7['H1-P4'][choice])
OLD = "because they're expected to carry everybody."
assert t.count(OLD) == 1
t = t.replace(OLD, "because they may be expected to carry everybody.")
(HERE / 'v8.md').write_text(t, encoding='utf-8')
(HERE / 'v8-variants.json').write_text(json.dumps({'H1-P4': v7['H1-P4'], 'chosen': choice}, ensure_ascii=False, indent=1)
                                       + '\n', encoding='utf-8')
print('wrote v8.md with H1-P4', choice)
