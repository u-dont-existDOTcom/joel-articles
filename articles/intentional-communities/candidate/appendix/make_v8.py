"""The appendix, draft v8 (2026-10-17): v7 (Orlov o1, research paragraph r5: alone Human, 339g 0.16; the whole appendix 100%
Human, 0.20; trace OK, review-r12x) with Doucleff's entry in two more shapes. Trace T3's fix of review-r7 (the published three topics, "about kids
taking part in family life, autonomy, and spreading out the work of caring for them.") read AI with Liedloff's entry (339g,
E11-12, 0.52; with v6's wording, which the trace found made two of the topics results of the first, the pair read Human,
331g, 0.06). Both keep the three topics as three things the book is about, without another question (Liedloff, Christian
and Ludwig's entries around it are questions already):
- d1: two sentences ("... about kids taking part in family life. It's also about autonomy, and spreading out the work of
  caring for them.");
- d3: one, with "about" for each topic.
r5, not r6: r6 (v7x) read Human as well (0.18), but its trace found "So you can check it yourself" could point at the stuff he
couldn't verify, just named (review-r12, SHIFT); in r5 the same words follow the report's whole list, and its trace found
them EQUIVALENT (review-r12x), so r5 needs no change and no new screen.
v8 is v7 with d1, v8x v7 with d3. Writes v8.md, v8x.md and v8-variants.json. Run from this folder: python3 make_v8.py"""
import json, pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
subprocess.run([sys.executable, str(HERE / 'make_v7.py')], check=True, capture_output=True)
t = (HERE / 'v7.md').read_text(encoding='utf-8')
OLD = "is a practical, accessible book about kids taking part in family life, autonomy, and spreading out the work of caring for them."
V = {
 'd1': ("is a practical, accessible book about kids taking part in family life. It's also about autonomy, and spreading out the "
        "work of caring for them."),
 'd3': ("is a practical, accessible book about kids taking part in family life, about autonomy, and about spreading out the work "
        "of caring for them."),
}
assert t.count(OLD) == 1
(HERE / 'v8.md').write_text(t.replace(OLD, V['d1']), encoding='utf-8')
(HERE / 'v8x.md').write_text(t.replace(OLD, V['d3']), encoding='utf-8')
(HERE / 'v8-variants.json').write_text(json.dumps({'old': OLD, 'variants': V, 'v8': 'd1', 'v8x': 'd3', 'research': 'r5'},
                                                  ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('wrote v8.md (d1) and v8x.md (d3)')
