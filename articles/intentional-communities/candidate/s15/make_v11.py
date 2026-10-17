"""Section 15 draft v11 (2026-10-17): v10 with three last shapes of H1-P4 after seven that keep the published "often" read AI
alone (330g, 332g) and the one that reads Human (round d's c, "so much is taken care of by", 0.54) was a SHIFT for trace r7
T1. Two keep g's first sentence (the published "often" and "go through", trace r8 T1: OK) and change the two sentences that
every shape so far has shared; the third keeps c's texture with the published words:
- h1: "Land, childcare, housing, food, obligations, you name it!" for "Whether it's land, ..., etc, etc.";
- h4: "That goes for land, childcare, housing, food, obligations, etc, etc." for the same;
- c2: "so much often passes through" (c's "so much", the published "often pass through").
If none reads Human alone, the choice is Joel's (questions page). Writes v11.md and v11-variants.json.
Run from this folder: python3 make_v11.py [CHOICE]"""
import json, pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
choice = sys.argv[1] if len(sys.argv) > 1 else 'h1'
subprocess.run([sys.executable, str(HERE / 'make_v9.py'), 'g'], check=True, capture_output=True)
t = (HERE / 'v9.md').read_text(encoding='utf-8')
G1 = ("In the villages and families I've spent time around, things often go through the extended family and the local memory, "
      "alongside the formal systems.")
LIST = "Whether it's land, childcare, housing, food, obligations, etc, etc."
END = "Who needs a workshop called \"Rebuilding Intergenerational Belonging\" when some aunt has already given three people a task?"
G = G1 + ' ' + LIST + ' ' + END
assert t.count(G) == 1
V = {
 'h1': G1 + " Land, childcare, housing, food, obligations, you name it! " + END,
 'h4': G1 + " That goes for land, childcare, housing, food, obligations, etc, etc. " + END,
 'c2': ("In the villages and families I've spent time around, so much often passes through the extended family and the local "
        "memory, alongside the formal systems. ") + LIST + ' ' + END,
}
t = t.replace(G, V[choice])
(HERE / 'v11.md').write_text(t, encoding='utf-8')
(HERE / 'v11-variants.json').write_text(json.dumps({'H1-P4': V, 'chosen': choice}, ensure_ascii=False, indent=1) + '\n',
                                        encoding='utf-8')
print('wrote v11.md with H1-P4', choice)
