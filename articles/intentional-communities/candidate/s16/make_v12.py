"""Section 16 draft v12 (2026-10-17): v11 (a, a) with the two windows that read AI inside the whole section (345g: H2-P3 to the start
of H2-P5, 116 to 127 words in every shape; the end of H3-P5 to H3-P8, 141 words) rebuilt from Emulate round f (emu-f/out/, three
calls on each window whole in v11's meaning), the published meaning put back inside the calls' sentences.
- H2-P3 from call A ("can actually start right now", "a place to sit down and talk", "can all start before you own a single
  square inch of dirt"), with "your inner pl/ork" whole (A: "a lot of your", a part), "right where you live", the privacy (A
  lost it) and the deed ("No deed required!").
- H2-P4 from call B (the outcome as questions: "What if after two years of practicing together, the group isn't able to get a
  piece of land? ... Would that be a waste of time?"), with "every week", "still doesn't own land" for the published "may never
  own land", and the published situations as the answer (B: "Could you still have a positive impact on ... etc.?").
- H2-P5 stays v10's: round f's shape from call B ("Maybe you're remote, or stuck where you are. In that case, ...", "Trade
  counseling hours with one friend") had no break in one of the march's readings (review-r21); v10's had one in both (r16).
- H3-P5 from call A ("If you haven't, you ought to!"), with the visitor requirements as an instruction (A: "they may need to
  tighten up", C: "but that's okay", claims the published doesn't make).
- H3-P6 from calls A to C ("What will you learn? So much!", "drives you bananas", "showering with folks"), with "no manifesto"
  (all three lost it), the kind of privacy (B: "your need for privacy"), the four lessons joined by "and" (trace r13 T3), and the
  studio apartments priced, not rented or bought.
- H3-P7 from call A ("Do these three things before you invest a lot of time or money in looking for land!"), "spend" for the
  published; the exclamation had no break in either reading (review-r21), so "I know, I know!" after it (a reaction that claims
  nothing).
- H3-P8 from call A ("I'm not even asking you to come to a retreat or fill out an application"), with the published observation
  as it was ("I've just noticed that community tends to gather wherever ..."; A: "Community is like flowers, it grows where
  people cultivate ...", a different claim).
Writes v12.md and v12-variants.json. Run from this folder: python3 make_v12.py"""
import json, pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
subprocess.run([sys.executable, str(HERE / 'make_v11.py'), 'a', 'a'], check=True, capture_output=True)
t = (HERE / 'v11.md').read_text(encoding='utf-8')
V11 = json.loads((HERE / 'v11-variants.json').read_text(encoding='utf-8'))['new']
PC = '[Peer counseling](https://ibogaqueen.substack.com/p/hearthwork-an-integrated-peer-counseling)'
L5 = ('[Twin Oaks](https://twinoaks.org/), [East Wind](http://eastwind.org/), [Acorn](https://www.ic.org/directory/acorn-community-'
      'farm/) and other [intentional communities](https://www.ic.org/)')
EV = '[ecovillages](https://ecovillage.org/)'
CP = '[cuddle puddle](http://cuddleparty.com/)'
P5_OLD = ("Here's an idea if you're remote, or stuck where you are: build the part of it you actually can. Have a weekly meal with two "
          "households. Set up a counseling exchange with one friend, in person or by video. Share tools or childcare. Transport or "
          "food prep work too. Or a sauna! And if you're hippie enough, add acro-yoga, dance improv, a mothers' circle or a %s." % CP)
P7_OLD = "What about the land? Do those three things first, before you spend serious time or money looking for it."
P8_OLD = ("I'm not trying to sell you a retreat or get you to fill out an application or anything, the manuals I mentioned are free. "
          "I've just noticed that community tends to gather wherever people find real care, play, usefulness and room to become "
          "more honest.")
OLD = {'H2-P3': V11['H2-P3'], 'H2-P4': V11['H2-P4'], 'H2-P5': P5_OLD, 'H3-P5': V11['H3-P5'], 'H3-P6': V11['H3-P6'],
       'H3-P7': P7_OLD, 'H3-P8': P8_OLD}
NEW = {
 'H2-P3': ("Your inner pl/ork can actually start right now, right where you live. %s just requires 2 people and a private place to "
           "sit down and talk. Reparenting work, somatic work, working on jealousy, working on conflict repair, etc etc, can all "
           "start before you own a single square inch of dirt. No deed required!" % PC),
 'H2-P4': ("What if, after two years of practicing together every week, the group still doesn't own land? Would that be a waste of "
           "time? Nope. It can still change how people get through divorce, illness, grief, parenting and plain old loneliness."),
 'H2-P5': ("Maybe you're remote, or stuck where you are. In that case, build the part of it you actually can. Have a weekly meal "
           "with two households. Trade counseling hours with one friend, in person or by video. Share tools or childcare. "
           "Transport or food prep work too. Or a sauna! And if you're hippie enough, add acro-yoga, dance improv, a mothers' "
           "circle or a %s." % CP),
 'H3-P5': ("Have you ever been to an actual community? If you haven't, you ought to! %s take visitors, and so do a lot of %s (just "
           "check their current visitor requirements before you go)." % (L5, EV)),
 'H3-P6': ("What will you learn? So much, and none of it is in any manifesto! How much togetherness you actually like, for one, and "
           "what kind of privacy you need. And which labor system drives you bananas! And whether showering with folks feels "
           "liberating, or makes you want to start pricing studio apartments."),
 'H3-P7': "Do those three things before you spend a lot of time or money looking for land. I know, I know!",
 'H3-P8': ("I'm not selling anything here, by the way. I'm not even asking you to come to a retreat or fill out an application, and "
           "the manuals I mentioned are free. I've just noticed that community tends to gather wherever people find real care, "
           "play, usefulness and room to become more honest."),
}
for k in ('H2-P5',):
    del OLD[k], NEW[k]
for k, v in OLD.items():
    assert t.count(v) == 1, k
    t = t.replace(v, NEW[k])
(HERE / 'v12.md').write_text(t, encoding='utf-8')
(HERE / 'v12-variants.json').write_text(json.dumps({'old': OLD, 'new': NEW}, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('wrote v12.md')
