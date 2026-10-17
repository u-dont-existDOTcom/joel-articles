"""Section 16 draft v15 (2026-10-17): v14's H2 (every run of three and every pair Human, 349g and 350g; H2-P5 with trace r27
T2's fix) with H3-P2 to H3-P4 in three more shapes. Every shape of these three so far reads AI in some run of three over them:
v8 to v11's (348g, 0.69 to 0.85), v13's from Emulate round g (349g, 0.73 and 0.92, though its H3-P3 read Human in the run H3-P3
to P5, 0.04), and v14's short imperatives (350g, 0.91 to 0.99). The instruction list under "What to Do This Month" is the
shape that reads AI, so two shapes change H3-P2's opening and one keeps v8's:
- q: H3-P2 opens on a question ("So what do you actually do this month?"), then v13's H3-P3 and v11's H3-P4;
- y: H3-P2 and H3-P3 as the author's own first month ("If I were starting this month, I'd start with the inner pl/ork. ...";
  "Then I'd find two or three people for a practice group ..."), the instructions as what he would do, then v11's H3-P4;
- w: v8's H3-P2 ("Start working on the inner pl/ork. With what? ..."), v13's H3-P3 and v11's H3-P4.
Writes v15.md and v15-variants.json. Run from this folder: python3 make_v15.py [q|y|w]"""
import json, pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
shape = sys.argv[1] if len(sys.argv) > 1 else 'q'
subprocess.run([sys.executable, str(HERE / 'make_v14.py')], check=True, capture_output=True)
t = (HERE / 'v14.md').read_text(encoding='utf-8')
V14 = json.loads((HERE / 'v14-variants.json').read_text(encoding='utf-8'))['new']
V13 = json.loads((HERE / 'v13-variants.json').read_text(encoding='utf-8'))['M']
V11 = json.loads((HERE / 'v11-variants.json').read_text(encoding='utf-8'))['new']
V13O = json.loads((HERE / 'v13-variants.json').read_text(encoding='utf-8'))['old']
RG = '[reparenting guide](https://ibogaqueen.substack.com/p/inner-child-self-love-tips-and-guided)'
HM = '[Hearthwork manual](https://ibogaqueen.substack.com/p/hearthwork-an-integrated-peer-counseling)'
P2 = {
 'q': ("So what do you actually do this month? Start doing some inner pl/ork, with the free %s and %s or with another serious "
       "practice you already trust. And practice before you have an audience!" % (RG, HM)),
 'y': ("If I were starting this month, I'd start with the inner pl/ork. The free %s and %s are there for exactly that, or go with "
       "another serious practice you already trust. Just practice before you have an audience!" % (RG, HM)),
 'w': V13O['H3-P2'],
}
P3 = {
 'q': V13['H3-P3'],
 'y': ("Then I'd find two or three people for a practice group (I'd call it that, not a commune). We'd meet regularly, and learn "
       "to listen, switch roles, get through one disagreement and keep our commitments, all before anybody talked about a shared "
       "future. One disagreement is enough!"),
 'w': V13['H3-P3'],
}
P4 = V11['H3-P4']
for k in ('H3-P2', 'H3-P3', 'H3-P4'):
    assert t.count(V14[k]) == 1, k
t = t.replace(V14['H3-P2'], P2[shape]).replace(V14['H3-P3'], P3[shape]).replace(V14['H3-P4'], P4)
(HERE / 'v15.md').write_text(t, encoding='utf-8')
(HERE / 'v15-variants.json').write_text(json.dumps({'H3-P2': P2, 'H3-P3': P3, 'H3-P4': P4, 'shape': shape}, ensure_ascii=False, indent=1)
                                        + '\n', encoding='utf-8')
print('wrote v15.md in shape', shape)
