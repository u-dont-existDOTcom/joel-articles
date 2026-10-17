"""Section 16 draft v27 (2026-10-17): v25 (all five fixes of meaning round r42) with H3-P6's showers sentence in shapes that keep the
published meaning without the timing trace r42 T3 flagged. Its own fix ("or make you start looking at studio apartments!") reads
AI inside the whole section in every v25 and v26 shape (389g to 402g, best 0.32, one 61-word window from the showers sentence:
https://www.pangram.com/history/112d2d5b-83c3-439a-a38a-74a631b7fe13); v24's longer joke read Human there (387g), and only its
timing ("right after the first communal shower you take") was the addition. Shapes, one letter each (showers, P6's end, P7):
- showers: s = v24's sentence without the timing ("or you'll start looking at studio apartments for rent!"); t = "or if they'll
  have you looking at studio apartments for rent!";
- P6's end: k = v25's ("And no manifesto is going to tell you any of that!"); n = without "And";
- P7: k = v25's ("I know!"); i = "I know, I know!".
Writes v27.md and v27-variants.json. Run from this folder: python3 make_v27.py CODE (for example: skk)"""
import json, pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
code = sys.argv[1] if len(sys.argv) > 1 else 'skk'
assert len(code) == 3 and code[0] in 'st' and code[1] in 'kn' and code[2] in 'ki', code
subprocess.run([sys.executable, str(HERE / 'make_v25.py')], check=True, capture_output=True)
t = (HERE / 'v25.md').read_text(encoding='utf-8')
SH_OLD = "or make you start looking at studio apartments!"
SH = {'s': "or you'll start looking at studio apartments for rent!", 't': "or if they'll have you looking at studio apartments for rent!"}
END = ("And no manifesto is going to tell you any of that!", "No manifesto is going to tell you any of that!")
P7 = ("looking for land. I know!", "looking for land. I know, I know!")
for old in (SH_OLD, END[0], P7[0]):
    assert t.count(old) == 1, old
t = t.replace(SH_OLD, SH[code[0]])
if code[1] == 'n':
    t = t.replace(*END)
if code[2] == 'i':
    t = t.replace(*P7)
(HERE / 'v27.md').write_text(t, encoding='utf-8')
(HERE / 'v27-variants.json').write_text(json.dumps({'showers': [SH_OLD, SH], 'end': END, 'P7': P7, 'code': code}, ensure_ascii=False,
                                                   indent=1) + '\n', encoding='utf-8')
print('wrote v27.md in shape', code)
