"""Section 16 draft v16 (2026-10-17): v15 q (H3-P2 opens on a question, and the runs H3-P2 to P4 and H3-P3 to P5 read Human,
351g, 0.03 and 0.06) with the two places that still read AI there changed:
- H3-P3's colon sentence ("Before you start talking about a shared future, meet regularly: practice listening and switching
  roles, get through at least one disagreement together, and keep your commitments to each other.") read AI alone in the run
  from H2-P6 (351g, 35 words) and in the whole section. In v16 the four steps are one sentence joined by "and", in the
  published order, and the shared future comes after all of them in its own sentence ("Hold off on talking about a shared future
  until you've done all of that.").
- From H3-P4's end to the section's end the whole section read AI (351g, 250 words), and the run H3-P4 to H3-P6 read AI with
  every H3-P4 tried (348g to 350g). Five of v15's seven paragraphs from H3-P2 to H3-P7 open on a question, because in the march
  the questions were the breaks (review-r20). So v16 tries the tail with fewer questions, each paragraph keeping a break of
  another kind:
  k: by hand (H3-P4 "As for where to find these people, I'd try ... You never know!"; H3-P5 "Go visit some actual communities
     too. Really, go! ..."; H3-P6 "You'll learn things on a visit that no manifesto can teach you, like ... And then there are
     the communal showers. Will they feel liberating, or send you off pricing studio apartments?"; H3-P7 "... The land can
     wait!");
  h: Emulate round h (emu-h/out/h02-emuB.txt, sent the published text) with the published meaning put back: the retreat
     person "kinder, rather than more impressed with themselves" (Emulate: "come back nice"), the named communities with their
     links, the current visitor requirements, "no manifesto", the four things a visit teaches (Emulate: togetherness OR
     privacy, the labor system "you want to be part of"), and "serious time or money" before land;
  e: v15's shape of that paragraph.
Writes v16.md and v16-variants.json. Run from this folder: python3 make_v16.py CODE, CODE = the shapes of H3-P4 to H3-P7, one
letter each (for example kkkk, ekkk, hhhh, eekk, eeee)."""
import json, pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
code = sys.argv[1] if len(sys.argv) > 1 else 'kkkk'
assert len(code) == 4 and set(code) <= set('ekh'), code
subprocess.run([sys.executable, str(HERE / 'make_v15.py'), 'q'], check=True, capture_output=True)
t = (HERE / 'v15.md').read_text(encoding='utf-8')
V15 = json.loads((HERE / 'v15-variants.json').read_text(encoding='utf-8'))
TO = '[Twin Oaks](https://twinoaks.org/)'
EW = '[East Wind](http://eastwind.org/)'
AC = '[Acorn](https://www.ic.org/directory/acorn-community-farm/)'
IC = '[intentional communities](https://www.ic.org/)'
EV = '[ecovillages](https://ecovillage.org/)'
OLD = {
 'H3-P3': V15['H3-P3']['q'],
 'H3-P4': V15['H3-P4'],
 'H3-P5': ("Have you ever been to an actual community? If not, you should go! %s, %s, %s and other %s take visitors, and so do a lot "
           "of %s (just check their current visitor requirements before you go)." % (TO, EW, AC, IC, EV)),
 'H3-P6': ("What will you learn from a visit? Things no manifesto can tell you. How much togetherness you actually enjoy, for one, "
           "and what kind of privacy you need. And which labor system drives you bananas! And whether communal showers feel "
           "liberating, or send you off pricing studio apartments."),
 'H3-P7': "What about the land? Do those three things first, before you spend serious time or money looking for it.",
}
P3 = ("Get two or three people together to form a practice group. Call it that, not a commune! Meet regularly, and practice "
      "listening and switching roles, and get through at least one disagreement together, and keep your commitments to each "
      "other. One disagreement is enough, I promise! Hold off on talking about a shared future until you've done all of that.")
SHAPES = {
 'H3-P4': {
  'k': ("As for where to find these people, I'd try an unprogrammed Quaker meeting, or a restorative-practice group. An "
        "open-hearted congregation is another option, or a mature recovery group, or a meditation group. Or someone you know who "
        "came back from a long retreat kinder, rather than more impressed with themselves. You never know!"),
  'h': ("Where do you find these people? Try an unprogrammed Quaker meeting, a restorative-practice group, an open-hearted "
        "congregation, a mature recovery group, a meditation group, or find some people who have gone on long retreats and come "
        "back kinder, rather than more impressed with themselves."),
 },
 'H3-P5': {
  'k': ("Go visit some actual communities too. Really, go! %s, %s and %s all take visitors. So do other %s, and a lot of %s. "
        "Check their current visitor requirements first, though." % (TO, EW, AC, IC, EV)),
  'h': ("Go visit some real communities. Really, go! %s, %s, %s and other %s are used to having people visit them. Many %s are "
        "too. Check their current visitor requirements first." % (TO, EW, AC, IC, EV)),
 },
 'H3-P6': {
  'k': ("You'll learn things on a visit that no manifesto can teach you, like how much togetherness you actually enjoy, what "
        "kind of privacy you need, and which labor system drives you bananas. And then there are the communal showers. Will they "
        "feel liberating, or send you off pricing studio apartments?"),
  'h': ("By visiting some communities, you'll get a better idea of things no manifesto can tell you, like how much togetherness "
        "you enjoy, what kind of privacy you need, and what kind of labor system irritates you. And whether communal showers "
        "feel liberating, or you'll start looking at studio apartments for rent right after the first communal shower you take!"),
 },
 'H3-P7': {
  'k': "Do those three things before you spend serious time or money looking for land. The land can wait!",
  'h': ("Do these three things before you spend serious time or money looking for land, if that's what you're thinking of "
        "doing."),
 },
}
NEW = {'H3-P3': P3}
for n, p in enumerate(('H3-P4', 'H3-P5', 'H3-P6', 'H3-P7')):
    NEW[p] = OLD[p] if code[n] == 'e' else SHAPES[p][code[n]]
for k, v in OLD.items():
    assert t.count(v) == 1, k
    t = t.replace(v, NEW[k])
(HERE / 'v16.md').write_text(t, encoding='utf-8')
(HERE / 'v16-variants.json').write_text(json.dumps({'old': OLD, 'H3-P3': P3, 'shapes': SHAPES, 'code': code, 'new': NEW},
                                                   ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('wrote v16.md in shape', code)
