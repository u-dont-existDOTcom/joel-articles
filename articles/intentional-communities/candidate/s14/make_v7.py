"""Section 14 draft v7 (2026-10-17): v6 with P2 rebuilt. Batch 313g read v6's P2 alone AI (0.78, medium) where v5's P2 had read
Human alone (305g-x): taking the repeated food-housing-care question out left eight questions in a row, four of them opening
"Who takes responsibility", and a run of questions is a tell the linter knows (O29; the lesson of 307g to 309g: "runs of
questions ... trigger AI windows"). v7 keeps every published item and the dedup, in four questions and one run-on sentence
ending "etc." (Emulate's shape), with the paragraph's break, "That's a lot of loose ends!". Writes v7.md and v7-fixes.json.
Run from this folder: python3 make_v7.py"""
import json, pathlib

HERE = pathlib.Path(__file__).resolve().parent
OLD = ('If the community dissolves, what happens to the land and any outside debts? What about its buildings, equipment, common '
       'stores or funds? What happens to each member’s agreed rights? More immediately, who is responsible for ensuring that '
       'everyone has a place to live and food to eat? Who takes responsibility for making sure people get their medications and '
       'the other care they need? Who keeps childcare going, and makes sure the kids’ schooling carries on? Who takes '
       'responsibility for bridging any outside cash or benefits people depend on, if relevant? Who takes responsibility for '
       'transportation, for the records, for family contact, for the animals, for making sure land obligations are met, and for '
       'any unresolved claims? That’s a lot of loose ends!')
NEW = ('If the community dissolves, what happens to the land and any outside debts? What about its buildings, equipment, common '
       'stores or funds, and each member’s agreed rights? More immediately, who makes sure everyone still has a place to live '
       'and food to eat, and gets their medications and the other care they need? Who keeps childcare going, and the kids’ '
       'schooling? And somebody has to take responsibility for bridging any outside cash or benefits people depend on, if '
       'relevant. Also for transportation, and for the records and family contact. Then there’s the animals and land '
       'obligations, and any unresolved claims. That’s a lot of loose ends!')
t = (HERE / 'v6.md').read_text(encoding='utf-8')
assert t.count(OLD) == 1
t = t.replace(OLD, NEW)
OLD5 = 'The communal economy had changed dramatically, but the bonds hadn’t vanished.'
NEW5 = 'The Farm’s communal economy had changed dramatically, but the bonds hadn’t vanished.'
assert t.count(OLD5) == 1
t = t.replace(OLD5, NEW5)
(HERE / 'v7.md').write_text(t, encoding='utf-8')
(HERE / 'v7-fixes.json').write_text(json.dumps([{'id': 'P2', 'old': OLD, 'new': NEW, 'why': (
    'batch 313g: v6\'s P2 read AI alone (0.78); eight questions in a row, four opening "Who takes responsibility" (O29). '
    'Every published item kept, the dedup kept, four questions and one run-on sentence')},
    {'id': 'P5', 'old': OLD5, 'new': NEW5, 'why': 'pause tally: "The communal economy had changed dramatically" (r5 b, r6 a): '
     'whose economy; The Farm\'s, named two sentences before'}], ensure_ascii=False, indent=1) + '\n',
    encoding='utf-8')
print('wrote v7.md')
