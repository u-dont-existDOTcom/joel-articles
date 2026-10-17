"""Section 15 draft v10 (2026-10-17): v9 with H1-P4 rebuilt from Emulate round e (emu-e/out/) after both of v8's shapes with
the published "often" back read AI alone (330g: g 0.94, m 0.91). Round d's c ("so much is taken care of by", 0.54 Human) is
the only shape that read Human, and trace r7 T1 found it said the family handles most of it. Three shapes, each keeping the
published "often" (things often pass through the family and the local memory, alongside the formal systems):
- q: "a lot of the time things go through ...": the published "often" as "a lot of the time" (calls A and B of e01 and e02 all
  say "a lot of things" or "most things"; "a lot of the time" keeps it frequency, not quantity);
- u: "you'd be surprised how often things go through ...": e02 A's "how a lot of things are handled through ...", with
  the published "often";
- v: the list first, as a fragment after the place, then "A lot of the time, all that goes through ...": e01 A's list before
  its claim.
Writes v10.md and v10-variants.json. Run from this folder: python3 make_v10.py [CHOICE]"""
import json, pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
choice = sys.argv[1] if len(sys.argv) > 1 else 'q'
subprocess.run([sys.executable, str(HERE / 'make_v9.py'), 'g'], check=True, capture_output=True)
t = (HERE / 'v9.md').read_text(encoding='utf-8')
G = ("In the villages and families I've spent time around, things often go through the extended family and the local memory, "
     "alongside the formal systems. Whether it's land, childcare, housing, food, obligations, etc, etc. Who needs a workshop "
     "called \"Rebuilding Intergenerational Belonging\" when some aunt has already given three people a task?")
assert t.count(G) == 1
END = "Who needs a workshop called \"Rebuilding Intergenerational Belonging\" when some aunt has already given three people a task?"
V = {
 'q': "In the villages and families I've spent time around, a lot of the time things go through the extended family and the "
      "local memory, alongside the formal systems. Whether it's land, childcare, housing, food, obligations, etc, etc. " + END,
 'u': "In the villages and families I've spent time around, you'd be surprised how often things go through the extended family "
      "and the local memory, alongside the formal systems. Whether it's land, childcare, housing, food, obligations, etc, etc. "
      + END,
 'v': "In the villages and families I've spent time around? Land, childcare, housing, food, obligations, etc, etc. A lot of the "
      "time, all that goes through the extended family and the local memory, alongside the formal systems. " + END,
}
t = t.replace(G, V[choice])
(HERE / 'v10.md').write_text(t, encoding='utf-8')
(HERE / 'v10-variants.json').write_text(json.dumps({'H1-P4': V, 'chosen': choice}, ensure_ascii=False, indent=1) + '\n',
                                        encoding='utf-8')
print('wrote v10.md with H1-P4', choice)
