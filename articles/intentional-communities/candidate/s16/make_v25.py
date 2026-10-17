"""Section 16 draft v25 (2026-10-17): v24 ams (the whole section 100% Human, 387g; every H3 paragraph Human alone or in its pair,
388g; `paragraphs_alone.py` PASS) with the fixes of meaning round r42 (`review-r42/DISPOSITIONS-r42.md`), each the trace's own
fix (a SHIFT or ADDED finding) or the published words (a LOST finding):
- H3-P3 (T1, two SHIFTs): "This is not quite the same thing as forming a commune. Call it a practice group." made the group nearly
  a commune: "Call it a practice group, not a commune."; "Practice the skills you need to practice, like listening and switching
  roles." made the two skills examples of an open set: "Practice listening and switching roles.";
- H3-P5 (T2, LOST): "Check their requirements first." lost the published "current visitor": "Check their current visitor
  requirements first.";
- H3-P6 (T3, ADDED): "you'll start looking at studio apartments for rent right after the first communal shower you take" added
  the timing: "make you start looking at studio apartments";
- H3-P7 (T3, ADDED): "I know, the land is the exciting part!" added a claim: "I know!";
- H3-P8 (T4, LOST): "taking care of each other" lost the published "real": "taking real care of each other".
Writes v25.md and v25-variants.json. Run from this folder: python3 make_v25.py [ONLY] (ONLY: a comma list of P3,P5,P6,P7,P8 to
apply only those fixes, for the one-fix-at-a-time checks)"""
import json, pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
only = sys.argv[1].split(',') if len(sys.argv) > 1 else ['P3', 'P5', 'P6', 'P7', 'P8']
subprocess.run([sys.executable, str(HERE / 'make_v24.py'), 'ams'], check=True, capture_output=True)
t = (HERE / 'v24.md').read_text(encoding='utf-8')
FIX = {
 'P3': [("This is not quite the same thing as forming a commune. Call it a practice group.",
         "Call it a practice group, not a commune."),
        ("Practice the skills you need to practice, like listening and switching roles.",
         "Practice listening and switching roles.")],
 'P5': [("Check their requirements first.", "Check their current visitor requirements first.")],
 'P6': [("or you'll start looking at studio apartments for rent right after the first communal shower you take!",
         "or make you start looking at studio apartments!")],
 'P7': [("I know, the land is the exciting part!", "I know!")],
 'P8': [("taking care of each other", "taking real care of each other")],
}
for k in only:
    for old, new in FIX[k]:
        assert t.count(old) == 1, old
        t = t.replace(old, new)
(HERE / 'v25.md').write_text(t, encoding='utf-8')
(HERE / 'v25-variants.json').write_text(json.dumps({'fixes': FIX, 'applied': only}, ensure_ascii=False, indent=1) + '\n',
                                        encoding='utf-8')
print('wrote v25.md with', only)
