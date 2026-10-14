"""Batch 130g: P17's two fixes one at a time inside the P15-P17 triple (with P16b, which passed there beside c6-P17), P18c with
"tell it badly", P25b's first-sentence fixes one at a time on v12, P3 with the lived-through unit placed elsewhere, beside P2b."""
import json, pathlib
HERE = pathlib.Path(__file__).resolve().parent
C = json.load(open(HERE.parent / 'cand-current.json', encoding='utf-8'))
V0 = {}
for f in ('v127-parts.json', 'v128-parts.json', 'v129-parts.json'): V0.update(json.load(open(HERE / f, encoding='utf-8')))
V = {}
c6P17 = C['P17']
V['f-P17j'] = c6P17.replace("But isolating a kid with secrets isn't allowed.", "But secrets meant to isolate a kid aren't allowed.")
V['f-P17k'] = c6P17.replace("A surprise isn't a secret, because at the end of a certain date it has to be told.", "A surprise has an end date.")
V['f-P18j'] = V0['f-P18c'].replace('may tell it wrong and still need protection.', 'may tell it badly and still need protection.')
v12 = C['P25b']
V['f-P25b5'] = v12.replace('They also need', 'Kids also need', 1)
V['f-P25b6'] = V['f-P25b5'].replace('at least one plausible next step outside the community (school, an apprenticeship, work, family, another community)',
                                    'at least one plausible next step (school, an apprenticeship, work, family, or another community)')
V['f-P25b8'] = v12.replace('a good set of transferable skills', 'transferable skills').replace('good relationships with people', 'relationships with people')
c4P3 = C['P3']
V['f-P3i'] = c4P3.replace('but the kids might have something else to say.', 'but the kids who lived it might have something else to say.')
V['f-P3k'] = c4P3.replace("All of this will ultimately be reviewed by the kids, once they're grown,", 'All of this will ultimately be reviewed by the kids who grew up with it,')
for k, v in V.items(): assert v not in (c6P17, v12, c4P3, V0['f-P18c']), k
parts = dict(V)
for k in ('f-P2b', 'f-P16b', 'f-P26'): parts[k] = V0[k]
parts['c-P15'] = C['P15']
items = [['130g-P15P16bP17j', ['c-P15', 'f-P16b', 'f-P17j']], ['130g-P15P16bP17k', ['c-P15', 'f-P16b', 'f-P17k']],
         ['130g-P17j', ['f-P17j']], ['130g-P17k', ['f-P17k']], ['130g-P18j', ['f-P18j']],
         ['130g-P25b5', ['f-P25b5']], ['130g-P25b6', ['f-P25b6']], ['130g-P25b8', ['f-P25b8']],
         ['130g-P25b5P26', ['f-P25b5', 'f-P26']], ['130g-P25b6P26', ['f-P25b6', 'f-P26']],
         ['130g-P2bP3i', ['f-P2b', 'f-P3i']], ['130g-P2bP3k', ['f-P2b', 'f-P3k']]]
json.dump({'batch': '130g', 'parts': parts, 'items': items}, open(HERE / 'v130.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(V, open(HERE / 'v130-parts.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
for k, v in V.items(): print(k, '|', v)
