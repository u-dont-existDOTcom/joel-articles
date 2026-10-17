"""Section 16 draft v24 (2026-10-17): v23 j dmk, whose whole section reads Mostly Human (383g, 0.27): Human 731, AI 57, Human 115
(https://www.pangram.com/history/b06bf401-7474-4d57-a8f9-e8e50eaa0447). The one window is H3-P6's last sentence ("No manifesto
is going to tell you any of that."), H3-P7 ("Do those three things before you spend serious time or money looking for land. I
know, the land is the exciting part!") and H3-P8's first sentence ("I'm not trying to sell you a retreat or get you to fill out
an application or anything, the manuals I mentioned are free."). One change at a time on it, then together. Shapes, one letter
each (P6's end, P7, P8's first sentence):
- P6: k = v23's; a = the manifesto as a reaction ("And no manifesto is going to tell you any of that!");
- P7: m = v23's; k = v21's ("... The land can wait!");
- P8: k = v23's (one sentence with a comma); s = two sentences ("... or anything. The manuals I mentioned are free.").
Writes v24.md and v24-variants.json. Run from this folder: python3 make_v24.py CODE (for example: kks)"""
import json, pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
code = sys.argv[1] if len(sys.argv) > 1 else 'kks'
assert len(code) == 3 and code[0] in 'ka' and code[1] in 'mk' and code[2] in 'ks', code
subprocess.run([sys.executable, str(HERE / 'make_v23.py'), 'j', 'dmk'], check=True, capture_output=True)
t = (HERE / 'v23.md').read_text(encoding='utf-8')
P6_OLD, P6_NEW = 'No manifesto is going to tell you any of that.', 'And no manifesto is going to tell you any of that!'
P7_OLD = 'Do those three things before you spend serious time or money looking for land. I know, the land is the exciting part!'
P7_NEW = 'Do those three things before you spend serious time or money looking for land. The land can wait!'
P8_OLD = ("I'm not trying to sell you a retreat or get you to fill out an application or anything, the manuals I mentioned are "
          "free.")
P8_NEW = ("I'm not trying to sell you a retreat or get you to fill out an application or anything. The manuals I mentioned are "
          "free.")
for old in (P6_OLD, P7_OLD, P8_OLD):
    assert t.count(old) == 1, old
if code[0] == 'a':
    t = t.replace(P6_OLD, P6_NEW)
if code[1] == 'k':
    t = t.replace(P7_OLD, P7_NEW)
if code[2] == 's':
    t = t.replace(P8_OLD, P8_NEW)
(HERE / 'v24.md').write_text(t, encoding='utf-8')
(HERE / 'v24-variants.json').write_text(json.dumps({'P6': [P6_OLD, P6_NEW], 'P7': [P7_OLD, P7_NEW], 'P8': [P8_OLD, P8_NEW],
                                                    'code': code}, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('wrote v24.md in shape', code)
