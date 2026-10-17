"""Section 16 draft v5 (2026-10-17): v4 with the paragraphs that read AI in 328g rebuilt from Emulate round b (emu-b/out/,
two calls on each paragraph with its fixed meaning) and the published meaning put back inside Emulate's sentences.
- H1-P1 (AI with H1-P2, 0.98): a, call A of b02 ("They get the land first, then ..., and say they'll do the emotional work stuff
  later when they have more time"), with the published "wrong order" (A: "backwards") and the emotional preparation as a
  question and its answer; b, call B of b01's sequence ("they get the land first, put the vision into a document next, ...")
  split into sentences.
- H2-P3 (AI with H2-P2 and with H2-P4): a, call B of b03 ("Reparenting, somatic work, jealousy, conflict, etc etc ...") with the
  published "can begin" and "do not wait for a deed" as a question; b, the same with "No deed required!" as its break.
- H2-P6 (H2-P5 with it read Mixed): "keep showing up" (the published "reliably showing up"; b04's calls: "commit to doing this
  stuff"), "Trust me on this one." kept as its break.
- H3-P4, H3-P5, H3-P6 (the AI window of H3): call B of b05 ("Maybe at ...", "Lots of ecovillages take visitors, too", "You might
  get a very good idea of ..."), each list split into sentences the way Joel fixes lists (2026-10-07: split them into
  sentences), with the published claims back: the places as possible ones, the visit as a step ("Then go visit"), and what a
  visit teaches that no manifesto can. H3-P6 keeps v4's question "What do you get out of a visit?" as its break: without it,
  the first march reading of review-r8 found none.
- The linter's B7/B13 (half of a subsection's paragraphs landing on a line of nine words or fewer) failed H1 and H2 with
  the first endings: H1-P1's last sentence is "That gets put off until later, when everyone has more time." and H2-P3's has the
  published sense's "either" ("None of that has to wait for a deed either!").
- H2-P3 b ("No deed required!") had no break in the first reading of review-r8 either; a is the one screened.
Writes v5.md and v5-variants.json. Run from this folder: python3 make_v5.py [H1-P1 choice] [H2-P3 choice]"""
import json, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
c1 = sys.argv[1] if len(sys.argv) > 1 else 'a'
c3 = sys.argv[2] if len(sys.argv) > 2 else 'a'
t = (HERE / 'v4.md').read_text(encoding='utf-8')
PC = 'https://ibogaqueen.substack.com/p/hearthwork-an-integrated-peer-counseling'
OLD = {
 'H1-P1': "Most people building community do the steps in the wrong order. Sound familiar? They get the land first, put the vision "
          "in a document, let ownership pile up with whoever had the money, and put off the emotional preparation until "
          "everyone has more time.",
 'H2-P3': "But there's no reason you can't start the inner pl/ork where you live. And [peer counseling](%s)? It only needs two "
          "people and enough privacy to talk. Reparenting, somatic work, jealousy, conflict repair and the rest don't have to "
          "wait for a deed either!" % PC,
 'H2-P6': "Trust me on this one. If three households can commit to showing up for each other like this for six months, you'll "
          "learn more than you would from another year of daydreaming about the ideal village.",
 'H3-P4': "Where do you find them? Maybe try unprogrammed Quaker meetings, restorative practice groups, open-hearted "
          "congregations, mature recovery groups, meditation groups, or people who came back from a long retreat kinder rather "
          "than more impressed with themselves.",
 'H3-P5': "Then go visit actual communities, like [Twin Oaks](https://twinoaks.org/), [East Wind](http://eastwind.org/), "
          "[Acorn](https://www.ic.org/directory/acorn-community-farm/) or other [intentional communities](https://www.ic.org/) "
          "(a lot of [ecovillages](https://ecovillage.org/) take visitors too). Ever been to one? Just check their current "
          "visitor requirements first.",
 'H3-P6': "What do you get out of a visit? Stuff no manifesto can tell you: how much togetherness you actually enjoy, what kind "
          "of privacy you need, which labor system drives you nuts, and whether communal showers feel liberating or send you "
          "off pricing studio apartments.",
}
VAR = {
 'H1-P1': {
  'a': "Most people building community go about it in the wrong order. They get the land first, then write the vision down in a "
       "document, then let whoever had the money end up owning it. And the emotional preparation? That gets put off until later, "
       "when everyone has more time.",
  'b': "Most people building community take the steps in the wrong order. Sound familiar? First they get the land. Then the "
       "vision goes in a document, and the ownership piles up with whoever had the money. The emotional preparation? That gets "
       "put off until later, when everyone has more time.",
 },
 'H2-P3': {
  'a': "The inner pl/ork can start right where you live, though. [Peer counseling](%s) only needs two people and enough privacy to "
       "talk. And reparenting, somatic work, jealousy, conflict repair, etc etc? None of that has to wait for a deed either!" % PC,
  'b': "The inner pl/ork can start right where you live. [Peer counseling](%s) only needs two people and enough privacy to "
       "talk. And reparenting, somatic work, jealousy, conflict repair, etc etc can happen pretty much anywhere. No deed "
       "required!" % PC,
 },
}
NEW = {
 'H2-P6': "Trust me on this one. If three households keep showing up for each other like this for six months, you'll learn more "
          "than you would from another year of daydreaming about the ideal village.",
 'H3-P4': "Where can you find them? Maybe at an unprogrammed Quaker meeting, or a restorative-practice group. Open-hearted "
          "congregations, mature recovery groups and meditation groups are worth a try too. And look for the people who came "
          "back from a long retreat kinder, rather than more impressed with themselves!",
 'H3-P5': "Then go visit actual communities! [Twin Oaks](https://twinoaks.org/), [East Wind](http://eastwind.org/) and "
          "[Acorn](https://www.ic.org/directory/acorn-community-farm/) take visitors, and so do other [intentional "
          "communities](https://www.ic.org/) and a lot of [ecovillages](https://ecovillage.org/). Ever been to one? Just check "
          "their current visitor requirements first.",
 'H3-P6': "What do you get out of a visit? Things no manifesto can tell you. How much togetherness you actually enjoy, for "
          "one, and what kind of privacy you need. Or which labor system drives you nuts! And whether communal showers feel "
          "liberating or send you off pricing studio apartments.",
}
for pid, old in OLD.items():
    assert t.count(old) == 1, pid
new = dict(NEW, **{'H1-P1': VAR['H1-P1'][c1], 'H2-P3': VAR['H2-P3'][c3]})
for pid, old in OLD.items():
    t = t.replace(old, new[pid])
(HERE / 'v5.md').write_text(t, encoding='utf-8')
(HERE / 'v5-variants.json').write_text(json.dumps({'variants': VAR, 'new': NEW, 'old': OLD, 'chosen': {'H1-P1': c1, 'H2-P3': c3}},
                                                  ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('wrote v5.md with H1-P1', c1, 'and H2-P3', c3)
