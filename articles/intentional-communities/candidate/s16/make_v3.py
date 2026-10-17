"""Section 16 draft v3 (2026-10-17): v2 with the fixes of review round r4 (the meaning traces, the cold read and the stance
check of v2; review-r4/DISPOSITIONS-r4.md says what each finding got). Writes v3.md and v3-fixes.json.
Run from this folder: python3 make_v3.py"""
import json, pathlib

HERE = pathlib.Path(__file__).resolve().parent
t = (HERE / 'v2.md').read_text(encoding='utf-8')
FIX = [
 ('H1-P1', "One of the main problems I see with how people go about building community is that they do the steps in the wrong "
           "order.",
  "Most people building community do the steps in the wrong order.",
  'trace T1: the published "Most" (how common it is); "one of the main problems I see" ranked it and rested it on my view'),
 ('H1-P3', "Likewise, the economic side has to go in stages. You're probably not going to be able to fly straight to the "
           "economic destination!",
  "Likewise, the economic side should go in stages. You shouldn't try to fly straight to the economic destination!",
  'trace T2: the published "should" (Emulate\'s "has to" made it required), and the break advises as the published does '
  '(Emulate\'s "You\'re probably not going to be able to" predicted failure)'),
 ('H1-P3', "comes from what the group has shown it can do.", "should come from what the group has shown it can do.",
  'trace T2: the published "should emerge from demonstrated capacity"'),
 ('H2-P5', "Share tools and childcare. Or a sauna!",
  "Share tools and childcare, or transport and food preparation. Or a sauna!",
  'trace T4: transport and food preparation were lost; they come back as a second pair, so the paragraph still has one list '
  'of three (E125)'),
 ('H3-P2', "With what? Maybe the free [reparenting guide]", "With what? The free [reparenting guide]",
  'trace T5: "Maybe" made the published instruction a half-recommendation'),
 ('H3-P3', "(call it that, not a commune, at least for now)", "(call it that, not a commune)",
  'trace T6: "at least for now" said the commune label is only postponed, a new claim; section 13 calls such a group a '
  'community, and this says not to call it a commune, two different words, so nothing needs reconciling'),
 ('H3-P3', "One disagreement is plenty to start with!", "One disagreement is enough!",
  'trace T6: "plenty to start with" said one is a lot and more will follow; the published sets one as the bar'),
 ('H3-P5', "Just check their current visitor requirements first. Nobody likes surprise guests, right?",
  "Ever been to one? Just check their current visitor requirements first.",
  'trace T7: "Nobody likes surprise guests" gave a reason the published doesn\'t; the break is a question that claims nothing'),
 ('H3-P7', "So do those three things first, before you spend serious time or money looking for land. The land will still be "
           "there!",
  "What about the land? Do those three things first, before you spend serious time or money looking for it.",
  'trace T8: "The land will still be there!" said waiting costs nothing, a reason the published doesn\'t give; the break is a '
  'question'),
 ('H3-P8', "or anything, the manuals are free.", "or anything, the manuals I mentioned are free.",
  'the cold read: "the manuals" were six paragraphs back'),
]
log = []
for pid, old, new, why in FIX:
    assert t.count(old) == 1, (pid, old[:50])
    t = t.replace(old, new)
    log.append({'id': pid, 'old': old, 'new': new, 'why': why})
(HERE / 'v3.md').write_text(t, encoding='utf-8')
(HERE / 'v3-fixes.json').write_text(json.dumps(log, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('wrote v3.md', len(log), 'fixes')
