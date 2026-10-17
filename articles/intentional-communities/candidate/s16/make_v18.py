"""Section 16 draft v18 (2026-10-17): v17 h q, the first draft whose runs, its stretch over the subsection break, H3-P5 to the end
and H3-P7 to the end all read Human (359g, 0.01 to 0.12), with the one stretch that read AI in the subsection alone in both v17
shapes changed (359g, 361g: "Many ecovillages are too. Check their current visitor requirements first." to H3-P8's end, 136
words, https://www.pangram.com/history/0e194f00-c9d9-4911-bbc0-c34f3ba24476). The window starts on my restoration at H3-P5's end
(Emulate: "Check their requirements.") and holds H3-P6, where I rebuilt Emulate's run-on list around a published phrase ("things
no manifesto can tell you, like ..."). Shapes, one letter each (P5 P6 P8), then the H3-P3 shape (h or b, as in v17):
- P5: k = v17's; e = Emulate's end, "Check their requirements first." ("visit" carries the visitors, and "first" stays);
- P6: r = v17's; b = Emulate's run-on list kept whole (round h, call B), with the published items in it (how much togetherness
  you enjoy, what kind of privacy you need, the labor system that irritates you, showers liberating or the studio apartment),
  and the manifesto as its own reaction after it ("You're not going to find any of that in a manifesto!"; the shorter "No
  manifesto can tell you that!" made half of H3's paragraphs end on a short line, a lint FAIL);
- P8: k = v17's; e = round i's call A's first and third sentences and round h's call A's second ("There is no application form
  you need to fill out. I'm not selling a retreat. The manuals are free."; round i's "no retreat you need to buy" lost the
  published "sell", key U39), then v17's second sentence.
Writes v18.md and v18-variants.json. Run from this folder: python3 make_v18.py CODE P3 (for example: ebk h)"""
import json, pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
code = sys.argv[1] if len(sys.argv) > 1 else 'ebk'
p3 = sys.argv[2] if len(sys.argv) > 2 else 'h'
assert len(code) == 3 and code[0] in 'ke' and code[1] in 'rb' and code[2] in 'ke', code
subprocess.run([sys.executable, str(HERE / 'make_v17.py'), p3, 'q'], check=True, capture_output=True)
t = (HERE / 'v17.md').read_text(encoding='utf-8')
V16 = json.loads((HERE / 'v16-variants.json').read_text(encoding='utf-8'))
P5_OLD = 'Many [ecovillages](https://ecovillage.org/) are too. Check their current visitor requirements first.'
P5_NEW = 'Many [ecovillages](https://ecovillage.org/) are too. Check their requirements first.'
P6_OLD = V16['shapes']['H3-P6']['h']
P6_NEW = ("By visiting some communities, you'll get a better idea of how much togetherness you enjoy, what kind of privacy you need, "
          "what kind of labor system irritates you, whether communal showers feel liberating, or if you'll immediately begin "
          "looking at studio apartments for rent after the first communal shower you take. You're not going to find any of that in a "
          "manifesto!")
P8_OLD = ("I'm not trying to sell you a retreat or get you to fill out an application or anything, the manuals I mentioned are free. "
          "I've just noticed")
P8_NEW = ("There is no application form you need to fill out. I'm not selling a retreat. The manuals are free. I've just noticed")
for old in (P5_OLD, P6_OLD, P8_OLD):
    assert t.count(old) == 1, old
if code[0] == 'e':
    t = t.replace(P5_OLD, P5_NEW)
if code[1] == 'b':
    t = t.replace(P6_OLD, P6_NEW)
if code[2] == 'e':
    t = t.replace(P8_OLD, P8_NEW)
(HERE / 'v18.md').write_text(t, encoding='utf-8')
(HERE / 'v18-variants.json').write_text(json.dumps({'P5': [P5_OLD, P5_NEW], 'P6': [P6_OLD, P6_NEW], 'P8': [P8_OLD, P8_NEW],
                                                    'code': code, 'P3': p3}, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('wrote v18.md in shape', code, p3)
