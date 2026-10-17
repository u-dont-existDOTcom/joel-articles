"""Section 16 draft v14 (2026-10-17): v13 shape M (H2 reads Human in every run of three and every pair, 349g) with H3-P2 to H3-P4
in another shape, since the runs over them still read AI (349g: the heading and H3-P2 to H3-P4, 0.92; H3-P4 to H3-P6, 0.73),
H3-P4 read AI alone (0.36), and H3-P3's colon list read AI in two runs ("Before you start talking about a shared future, meet
regularly: ...", 35 words). The shape is round g's call A for H3-P2 and H3-P3 (short sentences, "Seriously work at it", "Actually
disagree and work it out", "Yes, you have to work through at least one disagreement") with the published meaning back, and an
offer for H3-P4 ("Not sure where to find them? Try ..."), the places as possible places ("could work too"):
- H3-P2: the published "and" (both texts) and "another serious practice you already trust" (A: "or whatever"), the audience;
- H3-P3: "two or three" (A: "2-3"), the name ("call it a practice group, not a commune"; A: "until you've gotten to know each
  other", a condition the published doesn't make), "regularly" (A: "for a while"), switching roles, the commitments, one
  disagreement, and the shared future after all of them ("Talk about a shared future after all that.");
- H3-P4: the published places and the person back from a long retreat "kinder, rather than more impressed with themselves".
The march found no break in H3-P2 or H3-P3 in either reading at first (review-r26: "And seriously work at it before you have
an audience!" and "And yes, get through at least one disagreement together (one is enough!)." read as steps), so H3-P2 ends
"No rush on the audience part!" and H3-P3 asks "Just one? Yep, one is enough!" (review-r28).
H2-P5 takes trace T2 of review-r27's fix: "build the part of community you actually can" (marched in review-r29).
Writes v14.md and v14-variants.json. Run from this folder: python3 make_v14.py"""
import json, pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
subprocess.run([sys.executable, str(HERE / 'make_v13.py'), 'M'], check=True, capture_output=True)
t = (HERE / 'v13.md').read_text(encoding='utf-8')
V13 = json.loads((HERE / 'v13-variants.json').read_text(encoding='utf-8'))['M']
RG = '[reparenting guide](https://ibogaqueen.substack.com/p/inner-child-self-love-tips-and-guided)'
HM = '[Hearthwork manual](https://ibogaqueen.substack.com/p/hearthwork-an-integrated-peer-counseling)'
OLD = {p: V13[p] for p in ('H3-P2', 'H3-P3', 'H3-P4')}
NEW = {
 'H3-P2': ("Start doing some inner pl/ork. Read the free %s and %s, or go with another serious practice you already trust. And "
           "practice it seriously before you have an audience. No rush on the audience part!" % (RG, HM)),
 'H3-P3': ("Get together with two or three people and call it a practice group, not a commune. Meet regularly. Work on listening, "
           "and on switching roles. Keep the commitments you make to each other. And get through at least one disagreement "
           "together. Just one? Yep, one is enough! Talk about a shared future after all that."),
 'H3-P4': ("Not sure where to find them? Try an unprogrammed Quaker meeting, or a restorative-practice group. An open-hearted "
           "congregation could work too, or a mature recovery group, or a meditation group. Or look for someone who came back from "
           "a long retreat kinder, rather than more impressed with themselves!"),
}
# trace T2 of review-r27 (SHIFT): "build the part of it you actually can" has no noun for "it" in reach since the dedup cut
# "a real piece of community" from H2-P4, and a reader may take it as the list; its fix is the published thing, community
P5_OLD, P5_NEW = "build the part of it you actually can.", "build the part of community you actually can."
assert t.count(P5_OLD) == 1
t = t.replace(P5_OLD, P5_NEW)
for k, v in OLD.items():
    assert t.count(v) == 1, k
    t = t.replace(v, NEW[k])
(HERE / 'v14.md').write_text(t, encoding='utf-8')
(HERE / 'v14-variants.json').write_text(json.dumps({'old': OLD, 'new': NEW}, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('wrote v14.md')
