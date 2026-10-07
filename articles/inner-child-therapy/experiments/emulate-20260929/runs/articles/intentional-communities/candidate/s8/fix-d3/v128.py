"""Batch 128g: P3 after 127g (P2a with P3a or P3d read AI; P2a alone Human), and P10e (P10c's "deserves direct study"
with P10a's "expands a kid's circle"). Writes v128.json; the remaining 127g items ride in the same install."""
import json, pathlib
HERE = pathlib.Path(__file__).resolve().parent
C = json.load(open(HERE.parent / 'cand-current.json', encoding='utf-8'))
V127 = json.load(open(HERE / 'v127-parts.json', encoding='utf-8'))
spec127 = json.load(open(HERE / 'v127.json', encoding='utf-8'))
V = {}
c4P3 = C['P3']  # "…Adults can go on about their intentions forever, but the kids might have something else to say."
assert 'go on about' in c4P3
# e: only "who lived through it" added (the dropped unit); "go on about" kept
V['f-P3e'] = c4P3.replace('but the kids might have something else to say.', 'but the kids who lived through it might have something else to say.')
# f: only "talk about" for "go on about"
V['f-P3f'] = c4P3.replace('Adults can go on about their intentions forever', 'Adults can talk about their intentions forever')
# g: "who grew up in it" for the lived-through unit
V['f-P3g'] = c4P3.replace('but the kids might have something else to say.', 'but the kids who grew up in it might have something else to say.')
# h: "who actually lived through it"
V['f-P3h'] = c4P3.replace('but the kids might have something else to say.', 'but the kids who actually lived through it might have something else to say.')
V['f-P10e'] = ("What's going on at Tamera's Children's Place deserves direct study instead of caricature. My own bias is still toward a "
               "system that expands a kid's circle, without the parent-child bond being made ideologically inconvenient.")
for k in V: assert V[k] != c4P3 or k == 'x', k
parts = dict(V); parts['c-P3'] = c4P3; parts['f-P2a'] = V127['f-P2a']; parts['f-P9a'] = V127['f-P9a']
rest = spec127['items'][13:]
need = sorted({k for _, ks in rest for k in ks})
for k in need: parts[k] = spec127['parts'][k]
items = rest + [['128g-P2aP3e', ['f-P2a', 'f-P3e']], ['128g-P2aP3f', ['f-P2a', 'f-P3f']], ['128g-P2aP3g', ['f-P2a', 'f-P3g']],
                ['128g-P2aP3h', ['f-P2a', 'f-P3h']], ['128g-P2aP3c4 (diagnostic)', ['f-P2a', 'c-P3']], ['128g-P9aP10e', ['f-P9a', 'f-P10e']]]
json.dump({'batch': '128g', 'parts': parts, 'items': items}, open(HERE / 'v128.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(V, open(HERE / 'v128-parts.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
for k, v in V.items(): print(k, '|', v)
