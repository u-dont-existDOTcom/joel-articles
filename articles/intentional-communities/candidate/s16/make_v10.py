"""Section 16 draft v10 (2026-10-17): v9 (H3-P6 shape a) with H1 rebuilt from Emulate round d (emu-d/out/, four calls on H1
whole in v8's meaning), the published meaning put back inside its sentences.
- H1-P1 from call D: the wrong order in the mistaken plan's own voice, as quotes ("First let's get land!" "Then let's write down
  a vision document!" ...), with the published "Most" (D: "I often feel like people ..."), the ownership that follows the money
  (D: "let whoever is putting in the money own the community"), the emotional preparation put off "until later, when everyone
  has more time" (D: "Most often what I see is ...", an observation the published doesn't make).
- H1-P2 from call D ("the order should be more like: ...", "(Unfortunately that would make for a pretty bad movie.)"), with
  Joel's order as his steps (D: "decide who should/might be in the community" for "test membership", "maybe think about land"
  for "then consider land") and "less cinematic", or from call B (one run of "and"s: "and processing conflicts, and sorting
  out your values, and ..."), with the same steps.
- H1-P3 from call D ("Don't try and fly right to "economic utopia" in one step", "based on what you CAN do"), with the
  published stages (D: "a couple of steps"), "reliably" (D lost it), "demonstrated" ("what the group has shown it CAN do"), and
  the tax bill, which D lost ("that sounds kind of weird when you say it out loud").
Shapes: dd (P1 D, P2 D, P3 D), db (P1 D, P2 B, P3 D), ed (v8's H1-P1 e, P2 D, P3 D).
Writes v10.md and v10-variants.json. Run from this folder: python3 make_v10.py [dd|db|ed]"""
import json, pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
shape = sys.argv[1] if len(sys.argv) > 1 else 'dd'
subprocess.run([sys.executable, str(HERE / 'make_v9.py'), 'L', 'a'], check=True, capture_output=True)
t = (HERE / 'v9.md').read_text(encoding='utf-8')
V9 = json.loads((HERE / 'v9-variants.json').read_text(encoding='utf-8'))
P1_E = ("Most people building community do it in the wrong order. Get the land first! Put the vision in a document! Let whoever "
        "had the money end up owning it! And the emotional preparation? That can wait until later, when everyone has more time.")
P2_V5 = ("The better order is less cinematic, more like this: practice together, process a real conflict, clarify your values, "
         "test membership, decide ownership and exit, and only then think about land. I know, it wouldn't make much of a movie!")
P3_L = V9['H1-P3']['L']
for x in (P1_E, P2_V5, P3_L):
    assert t.count(x) == 1, x[:40]
P = {
 'P1D': ("Most people try and do community in the wrong order. \"First let's get land!\" \"Then let's write down a vision "
         "document!\" \"And whoever's putting in the money can own the place!\" And the emotional side of things? That doesn't get "
         "done until \"later on, when everyone has more time\"."),
 'P2D': ("The order should be more like this: practice together, process a real conflict, clarify values, test membership, work "
         "out ownership and exit, and only then think about land. Less cinematic, I know! (It would make for a pretty bad "
         "movie.)"),
 'P2B': ("It would be better to get together to practice first, and process a real conflict, and get clear on your values, and "
         "test membership, and decide ownership and exit, and then, after all that, think about land. Less cinematic, I know! "
         "(It would make for a pretty bad movie.)"),
 'P3D': ("Same with money: do it in stages. Don't try and fly right to the economic destination in one go! Wait until the group "
         "can reliably provide for everyone, and fairly decide who gets what from the common, before it goes to a common purse. "
         "And work on reducing (or eliminating) outside money based on what the group has shown it CAN do, rather than because "
         "\"money is impure!\" (That sounds kind of weird when somebody else is quietly paying the tax bill.)"),
}
SHAPES = {'dd': ('P1D', 'P2D', 'P3D'), 'db': ('P1D', 'P2B', 'P3D'), 'ed': (None, 'P2D', 'P3D')}
p1, p2, p3 = SHAPES[shape]
if p1:
    t = t.replace(P1_E, P[p1])
t = t.replace(P2_V5, P[p2]).replace(P3_L, P[p3])
(HERE / 'v10.md').write_text(t, encoding='utf-8')
(HERE / 'v10-variants.json').write_text(json.dumps({'paragraphs': P, 'shapes': SHAPES, 'chosen': shape}, ensure_ascii=False,
                                                   indent=1) + '\n', encoding='utf-8')
print('wrote v10.md with H1', shape)
