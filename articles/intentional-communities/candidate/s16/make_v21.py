"""Section 16 draft v21 (2026-10-17): v20 kmb, the first draft whose whole section has one window left (368g, AI 0.40: Human 644,
AI 155, Human 87, https://www.pangram.com/history/8dfa2f1b-26f1-4684-a2b2-1df79cb15113). H3-P3's skills in two pairs cleared the
H3-P3 window, and with H3-P10's three items split, the windows in H2 and over H3-P10's end with H3-P11 went too (369g to 373g:
each change alone left them). The one window starts at H3-P5's list of communities ("Twin Oaks, East Wind, Acorn and other
intentional communities are used to having people visit them, and so are many ecovillages.") and runs to H3-P8's end, in both
H3-P5 shapes (368g, 373g); the subsection alone reads Human (368g, 0.24). Shapes, one letter each (P5 P7):
- P5: m = v20's; n = round i's call B ("Twin Oaks will welcome visitors, as will East Wind, Acorn, and many other intentional
  communities and ecovillages."); o = round i's call A ("Twin Oaks is one. East Wind is another, ..."), with the other
  intentional communities and the ecovillages' visitors put back;
- P7: k = v20's ("Do those three things before you spend serious time or money looking for land. The land can wait!"); e = round
  i's call A ("Don't invest serious time or money in looking for land until you've done these three things.") and a break after
  it ("The land isn't going anywhere!").
Writes v21.md and v21-variants.json. Run from this folder: python3 make_v21.py CODE (for example: ne)"""
import json, pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
code = sys.argv[1] if len(sys.argv) > 1 else 'ne'
assert len(code) == 2 and code[0] in 'mno' and code[1] in 'ke', code
subprocess.run([sys.executable, str(HERE / 'make_v20.py'), 'kmb'], check=True, capture_output=True)
t = (HERE / 'v20.md').read_text(encoding='utf-8')
TO = '[Twin Oaks](https://twinoaks.org/)'
EW = '[East Wind](http://eastwind.org/)'
AC = '[Acorn](https://www.ic.org/directory/acorn-community-farm/)'
IC = '[intentional communities](https://www.ic.org/)'
EV = '[ecovillages](https://ecovillage.org/)'
P5_OLD = ('%s, %s, %s and other %s are used to having people visit them, and so are many %s. Check their requirements first.'
          % (TO, EW, AC, IC, EV))
P5 = {
 'n': '%s will welcome visitors, as will %s, %s, and many other %s and %s. Check their requirements first.' % (TO, EW, AC, IC, EV),
 'o': ('%s is one. %s is another, and so is %s, and there are plenty of other %s. Lots of %s are open to visitors too. Check '
       'their requirements first.' % (TO, EW, AC, IC, EV)),
}
P7_OLD = 'Do those three things before you spend serious time or money looking for land. The land can wait!'
P7_NEW = ("Don't invest serious time or money in looking for land until you've done these three things. The land isn't going "
          "anywhere!")
for old in (P5_OLD, P7_OLD):
    assert t.count(old) == 1, old
if code[0] != 'm':
    t = t.replace(P5_OLD, P5[code[0]])
if code[1] == 'e':
    t = t.replace(P7_OLD, P7_NEW)
(HERE / 'v21.md').write_text(t, encoding='utf-8')
(HERE / 'v21-variants.json').write_text(json.dumps({'P5': [P5_OLD, P5], 'P7': [P7_OLD, P7_NEW], 'code': code}, ensure_ascii=False,
                                                   indent=1) + '\n', encoding='utf-8')
print('wrote v21.md in shape', code)
