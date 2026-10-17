"""Section 16 draft v26 (2026-10-17): v25 (all five fixes of meaning round r42) with the junction where every v25 window sits, H3-P5's
last sentence to H3-P7 (389g to 394g), in a few shapes that say the same thing. Shapes, one letter each (P5 P6 P7):
- P5: k = v25's ("Check their current visitor requirements first."); j = "Just check their current visitor requirements first.";
- P6: k = v25's; n = its last sentence without "And" ("No manifesto is going to tell you any of that!"); h = its showers sentence
  as "or have you looking at studio apartments!" (the published "make you start pricing" in another spoken shape);
- P7: k = v25's ("I know!"); i = "I know, I know!".
Writes v26.md and v26-variants.json. Run from this folder: python3 make_v26.py CODE (for example: knk)"""
import json, pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
code = sys.argv[1] if len(sys.argv) > 1 else 'knk'
assert len(code) == 3 and code[0] in 'kj' and code[1] in 'knh' and code[2] in 'ki', code
subprocess.run([sys.executable, str(HERE / 'make_v25.py')], check=True, capture_output=True)
t = (HERE / 'v25.md').read_text(encoding='utf-8')
CH = {
 'P5j': ("Check their current visitor requirements first.", "Just check their current visitor requirements first."),
 'P6n': ("And no manifesto is going to tell you any of that!", "No manifesto is going to tell you any of that!"),
 'P6h': ("or make you start looking at studio apartments!", "or have you looking at studio apartments!"),
 'P7i': ("looking for land. I know!", "looking for land. I know, I know!"),
}
use = [k for k, on in (('P5j', code[0] == 'j'), ('P6n', code[1] == 'n'), ('P6h', code[1] == 'h'), ('P7i', code[2] == 'i')) if on]
for k in use:
    old, new = CH[k]
    assert t.count(old) == 1, old
    t = t.replace(old, new)
(HERE / 'v26.md').write_text(t, encoding='utf-8')
(HERE / 'v26-variants.json').write_text(json.dumps({'changes': CH, 'code': code, 'applied': use}, ensure_ascii=False, indent=1) + '\n',
                                        encoding='utf-8')
print('wrote v26.md in shape', code)
