"""Variants of section 13 draft v30 (2026-10-16), to find which of round r19's fixes brought back the two AI windows of 310g
(the heading through H1-P3's first sentence; H2-P4 whole), when v29 had read 100% Human (309g). Each variant takes v30 and puts
back v29's text in one place: v30a, H1-P4 (T1-1's ", if you have any?" and T1-3's "gets exhausted" out); v30b, H2-P4 (T3-4's
"It'll be" back to "It may be"); v30d, H2-P3b without T3-3's "because" (two sentences again, as in v29, keeping T3-5's "the
experiment"); v30c, all three. Run from this folder: python3 make_v30v.py"""
import pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
IDS = [None, 'H1-P1', 'H1-P2', 'H1-P3', 'H1-P4', None, 'H2-P1', 'H2-P2', 'H2-P3', 'H2-P3b', 'H2-P4', None, 'H3-P1',
       'H3-P2', 'H3-P3', 'H3-P4', 'H3-P5', None, 'H4-P1', 'H4-P2', 'H4-P3', 'H4-P4', 'H4-P5', 'H4-P6', 'H4-P7', 'H4-P8',
       'H4-P9', None, 'H5-P1', 'H5-P2', 'H5-P3', 'H5-P4']
bl = lambda f: [x.strip() for x in re.split(r'\n\s*\n', (HERE / f).read_text(encoding='utf-8')) if x.strip()]
V29, V30 = bl('v29.md'), bl('v30.md')
i14, i23b, i24 = IDS.index('H1-P4'), IDS.index('H2-P3b'), IDS.index('H2-P4')
P3b = V30[i23b].replace('whether or not you are willing to experiment, because the people next to you',
                        'whether or not you are willing to experiment. The people next to you')
assert P3b != V30[i23b]
VAR = {'v30a': {i14: V29[i14]}, 'v30b': {i24: V29[i24]}, 'v30d': {i23b: P3b},
       'v30c': {i14: V29[i14], i24: V29[i24], i23b: P3b}}
for name, ch in VAR.items():
    out = [ch.get(i, b) for i, b in enumerate(V30)]
    (HERE / (name + '.md')).write_text('\n\n'.join(out) + '\n', encoding='utf-8')
print('written', ', '.join(VAR))
