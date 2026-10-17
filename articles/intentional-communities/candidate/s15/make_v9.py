"""Section 15 draft v9 (2026-10-17): v8 with the fix of trace r8 T2 (review-r8/trace-T2.md): H3-P2's "it's really hard to
become independent or start a stable life" lost the published "any" and "long-term" ("They struggle to build any independence
or long-term stability"). Round r7's trace had read the same words as EQUIVALENT; a LOST stands (only Joel overrules one), so
the published words go back. H1-P4 keeps v8's variants. Writes v9.md and v9-variants.json.
Run from this folder: python3 make_v9.py [CHOICE]"""
import json, pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
choice = sys.argv[1] if len(sys.argv) > 1 else 'g'
subprocess.run([sys.executable, str(HERE / 'make_v8.py'), choice], check=True, capture_output=True)
t = (HERE / 'v8.md').read_text(encoding='utf-8')
OLD = "it's really hard to become independent or start a stable life,"
assert t.count(OLD) == 1
t = t.replace(OLD, "it's really hard to build any independence or long-term stability,")
(HERE / 'v9.md').write_text(t, encoding='utf-8')
v8 = json.loads((HERE / 'v8-variants.json').read_text(encoding='utf-8'))
(HERE / 'v9-variants.json').write_text(json.dumps(v8, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('wrote v9.md with H1-P4', choice)
