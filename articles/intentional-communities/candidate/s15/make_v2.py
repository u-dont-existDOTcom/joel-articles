"""Section 15 draft v2 (2026-10-17): v1 with a break in each paragraph where both march readings of round r1 found none
(review-r1/MARCH-labels-a.txt, -b.txt: H1-P2, H2-P1, H2-P3, H2-P4, H2-P7, H3-P2, H3-P4 to H3-P8). Each break is a short
reaction, question or aside that claims nothing new about the world, the kind Joel kept in section 14 (his 37 a). Writes
v2.md and v2-fixes.json. Run from this folder: python3 make_v2.py"""
import json, pathlib

HERE = pathlib.Path(__file__).resolve().parent
t = (HERE / 'v1.md').read_text(encoding='utf-8')
FIX = [
 ('H1-P2', "Five times a day the prayers pour out into the streets, and I find them so soothing.",
  "Five times a day the prayers pour out into the streets. I find them so soothing!", 'the break: his reaction on its own'),
 ('H2-P1', "Not that Sénégal is some communal paradise that survived! The warmth has hard limits, and for LGBTQ+ people who cross them, it can be brutal.",
  "Does that make Sénégal some communal paradise that survived? No! The warmth has hard limits, and for LGBTQ+ people who cross them, it can be brutal.",
  'the break: a question and his answer (round r2\'s march found none in "I wish I didn\'t have to say this", the first try)'),
 ('H2-P3', "It can also be cruel to people who break its categories. Community isn't automatically freeing, then.",
  "It can also be cruel to people who break its categories. Both at once, which is hard to take in. Community isn't automatically freeing, then.",
  'the break: stopping to take in the two halves'),
 ('H2-P4', "People avoid confrontation so much that everybody knows who stole the sheep, and nobody wants to make a stink by saying it out loud.",
  "People avoid confrontation so much it's almost funny. Who stole the sheep? Everybody knows. And nobody wants to make a stink by saying it out loud.",
  'the break: the question and its answer, and a reaction'),
 ('H1-P4', "Nobody has to announce a workshop called \"Rebuilding Intergenerational Belonging.\" An aunt has already given three people a task.",
  "Nobody has to announce a workshop called \"Rebuilding Intergenerational Belonging,\" because an aunt has already given three people a task.",
  'the linter fails the first subsection on landings (B7/B13: three of five paragraphs ended on a short line); the joke in one sentence'),
 ('H2-P6', "Everybody raises sheep here, including me, and they are extremely cute.",
  "Everybody here raises sheep (me too), and they are extremely cute.",
  'the linter fails the paragraph on two lists of three (E125, Joel 2026-10-03: "P! failed b ecause it has 2 lists of 3"); '
  'this one is only a sentence shaped like a list, so the shape goes and the music-to-people list, the published point, stays'),
 ('H2-P7', "the wider world (and some of the men take the dangerous sea route to Europe).",
  "the wider world (and some of the men take the dangerous sea route to Europe). Can you blame them?",
  'the break: a question'),
 ('H3-P2', "They can hardly build any independence or long-term stability.",
  "They can hardly build any independence or long-term stability. How are they supposed to get ahead?",
  'the break: a question in the earner\'s place'),
 ('H3-P4', "There's another schedule, another status system and social world, other loyalties, and often new habits of consumption.",
  "There's another schedule, another status system and social world, other loyalties, and often new habits of consumption. That's a lot to bring home from a job!",
  'the break: a reaction to the list'),
 ('H3-P5', "But now it's something the community can name and negotiate.",
  "But now it's something the community can name and negotiate. I like that.",
  'the break: his opinion, stepping back'),
 ('H3-P6', "and watch parts of it fall apart.",
  "and watch parts of it fall apart. Kind of the opposite problem, isn't it?",
  'the break: a tag question'),
 ('H3-P7', "But they're people, not exhibits!",
  "But they're people, not exhibits! Would you want tourists staring at your family?",
  'the break: a question'),
 ('H3-P8', "and they won't let me pay rent!",
  "and they won't let me pay rent! I know, I'm lucky.",
  'the break: an aside'),
]
log = []
for pid, old, new, why in FIX:
    assert t.count(old) == 1, pid
    t = t.replace(old, new)
    log.append({'id': pid, 'old': old, 'new': new, 'why': why + ('' if pid in ('H2-P6', 'H1-P4') else ' (march r1: no break in either reading)')})
(HERE / 'v2.md').write_text(t, encoding='utf-8')
(HERE / 'v2-fixes.json').write_text(json.dumps(log, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('wrote v2.md')
