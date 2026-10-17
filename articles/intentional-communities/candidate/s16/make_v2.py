"""Section 16 draft v2 (2026-10-17): v1 with a break in each of the ten paragraphs where round r2's march found none in one
reading or both (review-r2/MARCH-labels-a.txt, -b.txt: H1-P1, H1-P2, H2-P3, H2-P4, H2-P6, H3-P2, H3-P3, H3-P5, H3-P6,
H3-P7). Each break is a short reaction, question or aside that claims nothing new about the world, the kind Joel kept in
section 14 (his 37 a), and no two share a shape (round r12's lesson in section 13: breaks that repeat turn into a tic).
Writes v2.md and v2-fixes.json. Run from this folder: python3 make_v2.py"""
import json, pathlib

HERE = pathlib.Path(__file__).resolve().parent
t = (HERE / 'v1.md').read_text(encoding='utf-8')
FIX = [
 ('H1-P1', "they do the steps in the wrong order. They get the land first,",
  "they do the steps in the wrong order. Sound familiar? They get the land first,",
  'a question before the list (at the end it was one of eleven short landings in nineteen paragraphs, the linter\'s B7/B13 FAIL)'),
 ('H1-P2', "decide ownership and exit, and only then think about land.",
  "decide ownership and exit, and only then think about land. I know, it wouldn't make much of a movie!",
  'a reaction to the published "less cinematic"'),
 ('H2-P3', "[Peer counseling](", "And [peer counseling](", 'see the next fix'),
 ('H2-P3', "And reparenting, somatic work, jealousy, conflict repair, etc. don't have to wait for a deed!",
  "Reparenting, somatic work, jealousy, conflict repair and the rest don't have to wait for a deed either!",
  'two sentences in a row no longer open on "And", and "and the rest" for "etc.", which the linter reads as a sentence end '
  '(a short landing, B7/B13)'),
 ('H2-P3', "And [peer counseling](https://ibogaqueen.substack.com/p/hearthwork-an-integrated-peer-counseling) only needs two "
           "people and enough privacy to talk.",
  "And [peer counseling](https://ibogaqueen.substack.com/p/hearthwork-an-integrated-peer-counseling)? It only needs two "
  "people and enough privacy to talk.",
  'the published sentence as a question and its answer'),
 ('H2-P4', "may never own land, and it can still make a difference",
  "may never own land. So what? It can still make a difference",
  'a question after "may never own land" (at the end, "That counts for a lot." was a short landing too, B7/B13)'),
 ('H2-P6', "If three households can commit", "Trust me on this one. If three households can commit",
  'the writer stepping in before the claim (at the end it was a short landing, and the subsection failed the linter\'s B7/B13)'),
 ('H3-P2', "Start working on the inner pl/ork, whether it's following the free [reparenting guide]",
  "Start working on the inner pl/ork. With what? Maybe the free [reparenting guide]",
  'a question and its answer (round r3\'s march found no break in "And practice before you have an audience, okay?")'),
 ('H3-P2', "(https://ibogaqueen.substack.com/p/hearthwork-an-integrated-peer-counseling) or another serious practice you already "
           "trust.",
  "(https://ibogaqueen.substack.com/p/hearthwork-an-integrated-peer-counseling), or another serious practice you already "
  "trust.", 'see the fix before'),
 ('H3-P3', "before you start talking about a shared future.",
  "before you start talking about a shared future. One disagreement is plenty to start with!",
  'a joke on the published "handle one disagreement"'),
 ('H3-P5', "Just check their current visitor requirements first.",
  "Just check their current visitor requirements first. Nobody likes surprise guests, right?",
  'a tag question giving the plain reason for the published instruction'),
 ('H3-P6', "You'll find out stuff no manifesto can tell you:",
  "What do you get out of a visit? Stuff no manifesto can tell you:",
  'the published sentence as a question and its answer'),
 ('H3-P7', "before you spend serious time or money looking for land.",
  "before you spend serious time or money looking for land. The land will still be there!",
  'a reaction: the published "before" says nothing is lost by waiting'),
]
log = []
for pid, old, new, why in FIX:
    assert t.count(old) == 1, (pid, old[:50])
    t = t.replace(old, new)
    log.append({'id': pid, 'old': old, 'new': new, 'why': why + ' (march r2: no break in one reading or both)'})
(HERE / 'v2.md').write_text(t, encoding='utf-8')
(HERE / 'v2-fixes.json').write_text(json.dumps(log, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('wrote v2.md')
