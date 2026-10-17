"""Section 16 draft v22 (2026-10-17): v21 ok, whose whole section reads Human over 676 words, then AI over H3-P6 to H3-P8 (130
words), then Human over the last 87 (375g, 0.37, https://www.pangram.com/history/fdf15fe2-946f-4575-8bad-970b3bc54a57). The
window starts at H3-P6 ("By visiting some communities, ...", v19's shape d) as it did in 369g. Shapes, one letter each (P6 P7 P8):
- P6: d = v21's; g = round i's call C ("When you do that, you'll get a much better idea of ...", v19's shape g; "When you visit"
  here, since after H3-P5's last sentence "that" would be checking their requirements), its last sentence
  with the writer's own voice so both march readings find the break ("Honestly, no manifesto is going to tell you any of that!";
  without "Honestly" one reading found none, review-r36);
- P7: k = v21's ("... The land can wait!"); m = the published sentence and a reaction ("I know, the land is the exciting part!",
  the cinematic land purchase of H1-P2);
- P8: k = v21's; e = v18's (round i's call A and round h's call A for the first half: "There is no application form you need to
  fill out. I'm not selling a retreat. The manuals are free.").
Writes v22.md and v22-variants.json. Run from this folder: python3 make_v22.py CODE (for example: gke)"""
import json, pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
code = sys.argv[1] if len(sys.argv) > 1 else 'dke'
assert len(code) == 3 and code[0] in 'dg' and code[1] in 'km' and code[2] in 'ke', code
subprocess.run([sys.executable, str(HERE / 'make_v21.py'), 'ok'], check=True, capture_output=True)
t = (HERE / 'v21.md').read_text(encoding='utf-8')
V19 = json.loads((HERE / 'v19-variants.json').read_text(encoding='utf-8'))
V18 = json.loads((HERE / 'v18-variants.json').read_text(encoding='utf-8'))
P6_OLD = V19['H3-P6']['d']
P6_NEW = V19['H3-P6']['g'].replace('No manifesto is going to tell you any of that!',
                                    'Honestly, no manifesto is going to tell you any of that!').replace('When you do that, ',
                                                                                                         'When you visit, ')
assert P6_NEW.startswith('When you visit, ') and 'Honestly, no manifesto' in P6_NEW
P7_OLD = 'Do those three things before you spend serious time or money looking for land. The land can wait!'
P7_NEW = 'Do those three things before you spend serious time or money looking for land. I know, the land is the exciting part!'
P8_OLD, P8_NEW = V18['P8']
for old in (P6_OLD, P7_OLD, P8_OLD):
    assert t.count(old) == 1, old
if code[0] == 'g':
    t = t.replace(P6_OLD, P6_NEW)
if code[1] == 'm':
    t = t.replace(P7_OLD, P7_NEW)
if code[2] == 'e':
    t = t.replace(P8_OLD, P8_NEW)
(HERE / 'v22.md').write_text(t, encoding='utf-8')
(HERE / 'v22-variants.json').write_text(json.dumps({'P6': [P6_OLD, P6_NEW], 'P7': [P7_OLD, P7_NEW], 'P8': [P8_OLD, P8_NEW],
                                                    'code': code}, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('wrote v22.md in shape', code)
