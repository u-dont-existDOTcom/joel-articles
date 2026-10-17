"""Section 16 draft v13 (2026-10-17): v11 (a, a) with the five paragraphs that batch 348g's runs of three put inside every run that
reads AI: H2-P3 and H2-P4 (runs H2-P2 to P4, 0.52, and H2-P3 to P5, 0.44), H3-P2, H3-P3 and H3-P4 (runs H3-P2 to P4, 0.74; P3 to
P5, 0.85; P4 to P6, 0.69; and H2-P6 to H3-P3, 0.56). Every other run of three reads Human (0.00 to 0.38). Two shapes:
- G, from Emulate round g (emu-g/out/: the subsections sent whole), the published meaning put back:
  H2-P3 from calls A and C ("Peer counseling takes two", "jealousy work"): "So your inner pl/ork can start now, right where you
  live. Peer counseling takes two people and a private place to sit and talk. That's it! ...";
  H2-P4 plain, the published claim with a reaction after it ("and that's not nothing!");
  H3-P2 from call B ("Get a copy of the free reparenting guide ... start practicing before you bring an audience into it!"),
  with the published "and" (B: "and/or") and "another serious practice you already trust" (A: "or whatever");
  H3-P3 from call B ("See if you can get through at least one disagreement (one is enough!), and keep your commitments to each
  other"), with "two or three" (B: "a couple"), the name ("Call it that, not a commune!"), "regularly", and the shared future
  after all four (B lost it);
  H3-P4 from call C ("Where would you find such people, you ask? Well, ..."), with the published places and the person back from
  a long retreat "kinder, rather than more impressed with themselves" (C: "seems kind").
- M: G with H2-P4 with the situations split ("So what? It can still make a difference when people are going through a divorce,
  an illness or grief. Parenting too, and plain old loneliness."). Marches (review-r23 and r24): G's H2-P4, H3-P2 and H3-P3 had no
  break in either reading at first ("and that's not nothing!", "Call it that, not a commune!" and "(one is enough!)" read as
  steps), and M's first H2-P3 neither; H3-P2 got "No, really!" and H3-P3 "One disagreement is enough, I promise!", with the
  shared future put first so it covers all four ("Before you start talking about a shared future, meet regularly: ...").
  H2-P3 ends "None of it has to wait until somebody has a deed in hand." (with "for a deed." half of H2's paragraphs ended on a
  short line, lint B7, a FAIL; marched again in review-r25).
Writes v13.md and v13-variants.json. Run from this folder: python3 make_v13.py [G|M]"""
import json, pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
shape = sys.argv[1] if len(sys.argv) > 1 else 'G'
subprocess.run([sys.executable, str(HERE / 'make_v11.py'), 'a', 'a'], check=True, capture_output=True)
t = (HERE / 'v11.md').read_text(encoding='utf-8')
V11 = json.loads((HERE / 'v11-variants.json').read_text(encoding='utf-8'))['new']
PC = '[Peer counseling](https://ibogaqueen.substack.com/p/hearthwork-an-integrated-peer-counseling)'
RG = '[reparenting guide](https://ibogaqueen.substack.com/p/inner-child-self-love-tips-and-guided)'
HM = '[Hearthwork manual](https://ibogaqueen.substack.com/p/hearthwork-an-integrated-peer-counseling)'
OLD = {
 'H2-P3': V11['H2-P3'], 'H2-P4': V11['H2-P4'],
 'H3-P2': ("Start working on the inner pl/ork. With what? The free %s and %s, or another serious practice you already trust. And "
           "practice before you have an audience!" % (RG, HM)),
 'H3-P3': ("Find two or three people to form a practice group with (call it that, not a commune). Meet regularly, and learn to "
           "listen, switch roles, handle one disagreement and keep your commitments before you start talking about a shared future. "
           "One disagreement is enough!"),
 'H3-P4': V11['H3-P4'],
}
G = {
 'H2-P3': ("So your inner pl/ork can start now, right where you live. %s takes two people and a private place to sit and talk. "
           "That's it! And reparenting, somatic work, jealousy work, conflict repair, etc etc? None of it has to wait until somebody has a "
           "deed in hand."
           % PC),
 'H2-P4': ("A group that practices together weekly for two years may never own land. It can still change how people get through "
           "divorce, illness, grief, parenting and plain old loneliness, and that's not nothing!"),
 'H3-P2': ("Start doing some inner pl/ork. No, really! Get a copy of the free %s and the %s, or go with another serious practice "
           "you already trust, and start practicing before you bring an audience into it." % (RG, HM)),
 'H3-P3': ("Get two or three people together to form a practice group. Call it that, not a commune! Before you start talking about "
           "a shared future, meet regularly: practice listening and switching roles, get through at least one disagreement "
           "together, and keep your commitments to each other. One disagreement is enough, I promise!"),
 'H3-P4': ("Where would you find such people, you ask? Well, are there any unprogrammed Quaker meetings nearby? Any "
           "restorative-practice groups, or open-hearted congregations? Maybe a mature recovery group, or a meditation group? Or "
           "do you know anyone who came back from a long retreat kinder, rather than more impressed with themselves?"),
}
M = dict(G)
M['H2-P4'] = ("A group that practices together weekly for two years may never own land. So what? It can still make a difference when "
              "people are going through a divorce, an illness or grief. Parenting too, and plain old loneliness.")
NEW = {'G': G, 'M': M}[shape]
for k, v in OLD.items():
    assert t.count(v) == 1, k
    t = t.replace(v, NEW[k])
(HERE / 'v13.md').write_text(t, encoding='utf-8')
(HERE / 'v13-variants.json').write_text(json.dumps({'old': OLD, 'G': G, 'M': M, 'shape': shape}, ensure_ascii=False, indent=1) + '\n',
                                        encoding='utf-8')
print('wrote v13.md in shape', shape)
