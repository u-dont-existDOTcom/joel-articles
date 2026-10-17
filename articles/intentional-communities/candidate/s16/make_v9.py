"""Section 16 draft v9 (2026-10-17): v8 with H1 in shape e (its H1-P1 with v5's H1-P2 read Human, 340g, 0.46) and two more
shapes of H1-P3 and one of H3-P6, after batch 340g.
- H1-P3: both of v8's shapes read AI with H1-P2 (340g, 0.63 to 0.86). The published-order paragraph of v5 and v6 ("Likewise,
  the economic side should go in stages. ..."), with trace r4's fixes, read Human alone (328g, 0.27) and with v5's H1-P2
  (328g, 0.34); only its end read AI inside H1, with other openings (333g, 337g). Two shapes:
  L: that paragraph as it was (its screens and its trace stand);
  q: the same with the outside money as a question, the way v8 asked it ("And cutting back on outside money, or getting rid
     of it? That should come from what the group has shown it can do."), the parenthetical kept.
- H3-P6: v8's "Which labor system drives you nuts!" (trace r13 T3's SHIFT fixed by dropping "Or") read AI with H3-P7 (340g,
  0.34; with "Or", 333g, Human 0.27), and inside H3 with the end of H3-P5 (73 words). Shape a is the trace's own fix, "And which
  labor system drives you nuts!"; shape w keeps v8's.
Writes v9.md and v9-variants.json. Run from this folder: python3 make_v9.py [L|q] [a|w]"""
import json, pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
p3 = sys.argv[1] if len(sys.argv) > 1 else 'L'
p6 = sys.argv[2] if len(sys.argv) > 2 else 'a'
subprocess.run([sys.executable, str(HERE / 'make_v8.py'), 'e', 'y'], check=True, capture_output=True)
t = (HERE / 'v8.md').read_text(encoding='utf-8')
P3_V8 = json.loads((HERE / 'v8-variants.json').read_text(encoding='utf-8'))['H1-P3']['y']
L = ("Likewise, the economic side should go in stages. You shouldn't try to fly straight to the economic destination! Only after "
     "the group has proven it can reliably provide for everybody, and fairly decide who gets what from the common, should it "
     "move to a common purse. And cutting back on outside money, or getting rid of it, should come from what the group has "
     "shown it can do. (\"Money is impure!\" is a weird thing to say while somebody else is quietly paying the tax bill.)")
V3 = {'L': L,
      'q': L.replace("And cutting back on outside money, or getting rid of it, should come from what the group has shown it can do.",
                     "And cutting back on outside money, or getting rid of it? That should come from what the group has shown it "
                     "can do.")}
assert V3['q'] != L
P6_W = "Which labor system drives you nuts!"
V6 = {'a': "And which labor system drives you nuts!", 'w': P6_W}
assert t.count(P3_V8) == 1 and t.count(P6_W) == 1
t = t.replace(P3_V8, V3[p3]).replace(P6_W, V6[p6])
(HERE / 'v9.md').write_text(t, encoding='utf-8')
(HERE / 'v9-variants.json').write_text(json.dumps({'H1-P3': V3, 'H3-P6': V6, 'P3': p3, 'P6': p6}, ensure_ascii=False, indent=1)
                                       + '\n', encoding='utf-8')
print('wrote v9.md with H1-P3', p3, 'and H3-P6', p6)
