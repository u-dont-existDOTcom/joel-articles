"""Section 16 draft v6 (2026-10-17): v5 (H1-P1 a, H2-P3 a) with the paragraphs that still read AI in 333g reshaped.
- H1-P2: H1-P1 with H1-P2 read AI with each H1-P1 shape (v4, v5 a and b: 0.98, 0.88, 0.85), and the AI window takes in H1-P2's
  list sentence; H1-P2 with H1-P3 read Human (328g). H1-P2 numbers Joel's order inline, the way he numbers his own four parts
  in section 4 ("1) inner pl/ork (reparenting), 2) ..."); a numbered list read Human in the appendix (Orlov, 334g, 0.22).
- H2-P5: its first five sentences read AI with H2-P6 (0.52), though H2-P5 read Human alone (328g, 0.09). Round b's call B of b04
  ("Here's an idea for those of you who are in remote locations, or otherwise stuck ...: pick a part of the village ... that
  you can actually build"), with the published claims: build the portion available, a weekly meal with two households, a
  counseling exchange with one friend in person or by video, the shared tools, childcare, transport, food preparation and
  sauna, and the extras if you're hippie enough.
- H3-P4: its last two sentences read AI with H3-P3 and all of it with H3-P5. Call A of b05 ("Maybe among unprogrammed Quakers,
  people involved in restorative practices, ..."), the possible places as one run, and the people back from a long retreat
  as their own sentence.
- H3-P5: AI with H3-P4 and with H3-P6. It opens with a question now ("Have you ever visited an actual community? Go!"), the
  published "Visit actual communities." as the imperative after it.
Writes v6.md and v6-fixes.json. Run from this folder: python3 make_v6.py"""
import json, pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
subprocess.run([sys.executable, str(HERE / 'make_v5.py'), 'a', 'a'], check=True, capture_output=True)
t = (HERE / 'v5.md').read_text(encoding='utf-8')
FIX = [
 ('H1-P2', "The better order is less cinematic, more like this: practice together, process a real conflict, clarify your values, "
           "test membership, decide ownership and exit, and only then think about land.",
  "The better order is less cinematic: 1) practice together, 2) process a real conflict, 3) clarify your values, 4) test "
  "membership, 5) decide ownership and exit, and 6) only then think about land."),
 ('H2-P5', "Remote or constrained readers can build the portion available. Hold a weekly meal with two households. Arrange a "
           "counseling exchange with one friend in person or by video. Share tools and childcare, or transport and food "
           "preparation. Or a sauna! Add acro-yoga, dance improvisation, a mothers' circle, or a [cuddle "
           "puddle](http://cuddleparty.com/) if you're hippie enough.",
  "Here's an idea if you're remote, or stuck where you are: build the part of it you actually can. Have a weekly meal with "
  "two households. Set up a counseling exchange with one friend, in person or by video. Share tools and childcare, or "
  "transport and food prep. Or a sauna! And if you're hippie enough, add acro-yoga, dance improv, a mothers' circle or a "
  "[cuddle puddle](http://cuddleparty.com/)."),
 ('H3-P4', "Where can you find them? Maybe at an unprogrammed Quaker meeting, or a restorative-practice group. Open-hearted "
           "congregations, mature recovery groups and meditation groups are worth a try too. And look for the people who came "
           "back from a long retreat kinder, rather than more impressed with themselves!",
  "Where might you find them? Maybe among unprogrammed Quakers, restorative-practice groups, open-hearted congregations, "
  "mature recovery groups or meditation groups. Or people who came back from a long retreat kinder, rather than more "
  "impressed with themselves."),
 ('H3-P5', "Then go visit actual communities! [Twin Oaks](https://twinoaks.org/), [East Wind](http://eastwind.org/) and "
           "[Acorn](https://www.ic.org/directory/acorn-community-farm/) take visitors, and so do other [intentional "
           "communities](https://www.ic.org/) and a lot of [ecovillages](https://ecovillage.org/). Ever been to one? Just check "
           "their current visitor requirements first.",
  "Have you ever visited an actual community? Go! [Twin Oaks](https://twinoaks.org/), [East Wind](http://eastwind.org/), "
  "[Acorn](https://www.ic.org/directory/acorn-community-farm/) and other [intentional communities](https://www.ic.org/) take "
  "visitors, and so do a lot of [ecovillages](https://ecovillage.org/). Just check their current visitor requirements first."),
]
log = []
for pid, old, new in FIX:
    assert t.count(old) == 1, pid
    t = t.replace(old, new)
    log.append({'id': pid, 'old': old, 'new': new})
(HERE / 'v6.md').write_text(t, encoding='utf-8')
(HERE / 'v6-fixes.json').write_text(json.dumps(log, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('wrote v6.md,', len(log), 'changes')
