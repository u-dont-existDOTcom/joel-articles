"""Batch 134g: after 133g, one fix at a time where a combined fix read AI (P19, P25b), the P2-P3 pair with the published
semicolon, P3 in the active voice, P13 with "boss … around", P18's two passing fixes together, P22-P23 diagnostics, P23
with an agent, P25a without "just"."""
import json, pathlib
HERE = pathlib.Path(__file__).resolve().parent
V0 = {}
for f in ('v127-parts.json', 'v128-parts.json', 'v129-parts.json', 'v130-parts.json', 'v131-parts.json', 'v133-parts.json'):
    V0.update(json.load(open(HERE / f, encoding='utf-8')))
B = json.load(open(HERE.parent / 'cand-v21.json', encoding='utf-8'))
V = {}
V['h-P2o'] = V0['g-P2n'].replace("I'm not trying to design a village for everyone. Communities need", "I'm not trying to design a village for everyone; communities need")
V['h-P3l'] = ("The kids will ultimately review all of this once they're grown, and their review weighs more heavily than founders usually want "
              "it to. Adults can go on about their intentions forever, but the kids who lived through it might have something else to say.")
V['h-P13h'] = V0['g-P13g'].replace('quietly lord it over the younger ones there', 'quietly boss the younger ones around there')
V['h-P18n'] = V0['g-P18l'].replace('may tell it badly and still need protection.', 'may get mixed up telling it and still need protection.')
V['h-P19d'] = V0['f-P19b'].replace('Hear the child even when they accuse someone people love.', 'Hear the child even when the accused is someone people love.')
V['h-P19e'] = V0['f-P19b'].replace('Keep everyone safe first, right away,', "Keep whoever's at risk safe first, right away,")
V['h-P23o'] = V0['g-P23n'].replace('and disagree with the founders without being treated as traitors.', 'and disagree with the founders, without the community treating them as traitors.')
V['h-P25a3'] = V0['f-P25a'].replace("It's just not making it artificially impossible for people to leave.", "It's not making it artificially impossible for people to leave.")
V['h-P25a5'] = V0['f-P25a'].replace("It's just not making it artificially impossible for people to leave.", "It's making sure leaving isn't artificially impossible.")
V['h-P25b11'] = V0['f-P25b9'].replace('travel expenses', 'help with travel')
V['h-P25b12'] = V0['f-P25b9'].replace('or a little money,', 'or a small reserve,')
for k, v in V.items():
    assert v not in V0.values(), k
parts = dict(V)
for k in ('g-P2n', 'g-P14c', 'g-P22d', 'g-P23n', 'f-P22a', 'f-P23', 'f-P25b9', 'g-P26n'): parts[k] = V0[k]
parts['c-P3'] = B['P3']; parts['f-P3e'] = V0['f-P3e']
items = [['134g-P2oP3c4', ['h-P2o', 'c-P3']], ['134g-P2oP3e', ['h-P2o', 'f-P3e']], ['134g-P2nP3l', ['g-P2n', 'h-P3l']], ['134g-P2o', ['h-P2o']],
         ['134g-P13hP14c', ['h-P13h', 'g-P14c']], ['134g-P18n', ['h-P18n']], ['134g-P19d', ['h-P19d']], ['134g-P19e', ['h-P19e']],
         ['134g-P22dP23f (diagnostic)', ['g-P22d', 'f-P23']], ['134g-P22aP23n (diagnostic)', ['f-P22a', 'g-P23n']], ['134g-P22dP23o', ['g-P22d', 'h-P23o']],
         ['134g-P25a3', ['h-P25a3']], ['134g-P25a5', ['h-P25a5']], ['134g-P25b11', ['h-P25b11']], ['134g-P25b12', ['h-P25b12']],
         ['134g-P25b9P26n', ['f-P25b9', 'g-P26n']]]
json.dump({'batch': '134g', 'parts': parts, 'items': items}, open(HERE / 'v134.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(V, open(HERE / 'v134-parts.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
