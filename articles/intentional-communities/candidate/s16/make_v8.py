"""Section 16 draft v8 (2026-10-17): v7 with two fixes.
- H1-P3: v7's new paragraph (the impure-money contrast inside the last sentence) had no break in the march (review-r12
  reading a, "S S S"; the published-order versions' break was the separate "("Money is impure!" is a weird thing to say
  ...)", B in both readings of review-r5, and that sentence's run read AI inside H1, 337g). Two shapes, both with the outside
  money as a question ("And cutting back on outside money, or getting rid of it?"), the way H1-P1 asks about the emotional
  preparation, and opening on "And" (v7's "The money side" made the third paragraph of the section to open on "The", lint
  B13):
  y: the rest of v7's last sentence after the question ("That should come from ..., rather than from deciding that "money is
     impure!" (which sounds weird ...)");
  v: the published contrast as its own sentence ("Not from deciding that "money is impure!" while somebody else is quietly
     paying the tax bill.").
- H2-P5: trace T1 of review-r13 (SHIFT): "Share tools and childcare, or transport and food prep." made pairs out of the
  published list of five things, any of which will do; its fix, "Share tools, childcare, transport or food prep." ("Or a
  sauna!" stays).
Writes v8.md and v8-variants.json. Run from this folder: python3 make_v8.py [n|e] [y|v]"""
import json, pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
h1 = sys.argv[1] if len(sys.argv) > 1 else 'n'
p3 = sys.argv[2] if len(sys.argv) > 2 else 'y'
subprocess.run([sys.executable, str(HERE / 'make_v7.py'), h1], check=True, capture_output=True)
t = (HERE / 'v7.md').read_text(encoding='utf-8')
P3_V7 = ("The money side should go in stages too: don't try to fly straight to the economic destination! Only once the group can "
         "reliably provide for everybody, and fairly decide who gets what from the common, should it move to a common purse. And "
         "cutting back on outside money, or getting rid of it, should come from what the group has shown it can do, rather than "
         "from deciding that \"money is impure!\" (which sounds weird while somebody else is quietly paying the tax bill).")
HEAD = ("And the money side should go in stages too: don't try to fly straight to the economic destination! Only once the group can "
        "reliably provide for everybody, and fairly decide who gets what from the common, should it move to a common purse. And "
        "cutting back on outside money, or getting rid of it? ")
V = {
 'y': HEAD + ("That should come from what the group has shown it can do, rather than from deciding that \"money is impure!\" "
              "(which sounds weird while somebody else is quietly paying the tax bill)."),
 'v': HEAD + ("That should come from what the group has shown it can do. Not from deciding that \"money is impure!\" while "
              "somebody else is quietly paying the tax bill."),
}
P5_OLD = "Share tools and childcare, or transport and food prep."
P5_NEW = "Share tools, childcare, transport or food prep."
assert t.count(P3_V7) == 1 and t.count(P5_OLD) == 1
t = t.replace(P3_V7, V[p3]).replace(P5_OLD, P5_NEW)
(HERE / 'v8.md').write_text(t, encoding='utf-8')
(HERE / 'v8-variants.json').write_text(json.dumps({'H1-P3': V, 'H2-P5': {'old': P5_OLD, 'new': P5_NEW}, 'H1': h1, 'P3': p3},
                                                  ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('wrote v8.md with H1', h1, 'and H1-P3', p3)
