"""Batch 135g: P23 beside P24 (its other neighbor, which passes alone), P25b's reserve as "a small stash", P26 with "may" on the second
clause, P2b without "among the parents" beside the 102g P3; then the whole section with the best of 127g-135g so far."""
import json, pathlib
HERE = pathlib.Path(__file__).resolve().parent
V0 = {}
for f in ('v127-parts.json', 'v128-parts.json', 'v129-parts.json', 'v130-parts.json', 'v131-parts.json', 'v133-parts.json', 'v134-parts.json'):
    V0.update(json.load(open(HERE / f, encoding='utf-8')))
B = json.load(open(HERE.parent / 'cand-v21.json', encoding='utf-8'))
V = {}
V['i-P25b13'] = V0['h-P25b11'].replace('tools or a little money,', 'tools or a small stash,')
V['i-P26o'] = V0['f-P26'].replace('and others will start their own communities', 'and others may start their own communities')
V['i-P2r'] = V0['f-P2b'].replace("some common ground among the parents on children's health, enough that they can actually trust one another.",
                                  "some common ground on children's health, enough that parents can actually trust one another.")
for k, v in V.items(): assert v not in V0.values(), k
parts = dict(V)
for k in ('g-P23n', 'h-P23o', 'h-P25b11', 'f-P26', 'g-P26n'): parts[k] = V0[k]
parts['c-P24'] = B['P24']; parts['c-P3'] = B['P3']
items = [['135g-P23nP24', ['g-P23n', 'c-P24']], ['135g-P23oP24', ['h-P23o', 'c-P24']], ['135g-P25b13', ['i-P25b13']],
         ['135g-P25b11P26o', ['h-P25b11', 'i-P26o']], ['135g-P25b11P26', ['h-P25b11', 'f-P26']], ['135g-P2rP3c4', ['i-P2r', 'c-P3']], ['135g-P2r', ['i-P2r']]]
json.dump({'batch': '135g', 'parts': parts, 'items': items}, open(HERE / 'v135.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(V, open(HERE / 'v135-parts.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
