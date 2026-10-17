"""Section 16 draft v20 (2026-10-17): v19 d h, whose subsection reads Human as a whole (366g, 0.25), with the sentences that start
the whole section's windows changed (366g, https://www.pangram.com/history/bbe84457-a051-4b76-8f10-78779fdee942). In every H3-P3
shape so far the window inside the whole section starts at the sentence that holds the four skills as one list (v15's colon
list, v16's "and ... and ...", round h's "Practice the skills you need to practice: listening, ...", round i's "Just get
together regularly, and learn to listen, switch roles, handle one disagreement and keep your commitments."; 351g to 367g).
Shapes, one letter each (P3 P5 P10):
- P3: h = v19's (round h's colon list); k = the four skills in two pairs, each in Emulate's own words around them ("Practice the
  skills you need to practice, like listening and switching roles. Get through at least one disagreement too, and keep your
  commitments.");
- P5: e = v19's ("... are used to having people visit them. Many ecovillages are too. Check their requirements first."); m = the
  ecovillages in the same sentence ("..., and so are many ecovillages.");
- P10: k = v19's ("Passing it on doesn't need one institution, one founder or one official version."); b = the three split two
  and one ("Passing it on doesn't need one institution or one founder. And there doesn't have to be one official version of it,
  either."), since the last window (H3-P10's last sentence with H3-P11, 39 words) starts there (a shorter last sentence made
  half of H3's paragraphs end on a short line).
Writes v20.md and v20-variants.json. Run from this folder: python3 make_v20.py CODE (for example: kmb)"""
import json, pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
code = sys.argv[1] if len(sys.argv) > 1 else 'kmb'
assert len(code) == 3 and code[0] in 'hk' and code[1] in 'em' and code[2] in 'kb', code
subprocess.run([sys.executable, str(HERE / 'make_v19.py'), 'd', 'h'], check=True, capture_output=True)
t = (HERE / 'v19.md').read_text(encoding='utf-8')
EV = '[ecovillages](https://ecovillage.org/)'
P3_OLD = ("Practice the skills you need to practice: listening, switching roles, handling one disagreement, keeping your commitments, "
          "etc.")
P3_NEW = ("Practice the skills you need to practice, like listening and switching roles. Get through at least one disagreement too, "
          "and keep your commitments.")
P5_OLD = 'are used to having people visit them. Many %s are too. Check their requirements first.' % EV
P5_NEW = 'are used to having people visit them, and so are many %s. Check their requirements first.' % EV
P10_OLD = "Passing it on doesn't need one institution, one founder or one official version."
P10_NEW = ("Passing it on doesn't need one institution or one founder. And there doesn't have to be one official version of it, "
           "either.")
for old in (P3_OLD, P5_OLD, P10_OLD):
    assert t.count(old) == 1, old
if code[0] == 'k':
    t = t.replace(P3_OLD, P3_NEW)
if code[1] == 'm':
    t = t.replace(P5_OLD, P5_NEW)
if code[2] == 'b':
    t = t.replace(P10_OLD, P10_NEW)
(HERE / 'v20.md').write_text(t, encoding='utf-8')
(HERE / 'v20-variants.json').write_text(json.dumps({'P3': [P3_OLD, P3_NEW], 'P5': [P5_OLD, P5_NEW], 'P10': [P10_OLD, P10_NEW],
                                                    'code': code}, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('wrote v20.md in shape', code)
