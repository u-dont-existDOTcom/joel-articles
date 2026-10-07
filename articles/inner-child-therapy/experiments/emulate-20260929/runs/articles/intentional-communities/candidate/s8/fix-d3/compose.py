"""The candidate after the d3 gate's fixes: CHOICE maps each block to the variant that passed (see PREDICTIONS-s8.md, 127g-130g).
Writes cand-v21.json (plain blocks in order) and fix-d3/whole-131g.json (the whole section as the web app gets it, P28 whole
and with the cut that is Joel's question 3)."""
import json, pathlib
HERE = pathlib.Path(__file__).resolve().parent
S8 = HERE.parent
C = json.load(open(S8 / 'cand-current.json', encoding='utf-8'))
V = {}
for f in ('v127-parts.json', 'v128-parts.json', 'v129-parts.json', 'v130-parts.json'):
    V.update(json.load(open(HERE / f, encoding='utf-8')))
CHOICE = {'P2': 'f-P2b', 'P5': 'f-P5', 'P7': 'f-P7', 'P8': 'f-P8b', 'P9': 'f-P9a', 'P10': 'f-P10a', 'P11': 'f-P11', 'P12': 'f-P12',
          'P13': 'f-P13d', 'P14': 'f-P14a', 'P16': 'f-P16b', 'P17': 'f-P17j', 'P18': 'f-P18j', 'P19': 'f-P19b', 'P20': 'f-P20b',
          'P21': 'f-P21b', 'P22': 'f-P22a', 'P23': 'f-P23', 'P25a': 'f-P25a', 'P25b': 'f-P25b5', 'P26': 'f-P26', 'P27': 'f-P27a', 'P28': 'f-P28a'}
KEEP = ['H0', 'P1', 'CAP1', 'P3', 'P4', 'P6', 'H1', 'H2', 'CAP2', 'P15', 'H3', 'P24', 'H4']  # unchanged from the current candidate
B = {}
for k in C:
    B[k] = V[CHOICE[k]] if k in CHOICE else C[k]
    assert k in CHOICE or k in KEEP, k
json.dump(B, open(S8 / 'cand-v21.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
whole = '\n\n'.join(B[k] for k in B)
cut = dict(B); cut['P28'] = V['f-P28a-s2']
whole_cut = '\n\n'.join(cut[k] for k in cut)
json.dump({'S8-v21-P28whole': whole, 'S8-v21-P28cut': whole_cut}, open(HERE / 'whole-131g.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('words: whole', len(whole.split()), '| cut', len(whole_cut.split()))
print('changed vs current:', ' '.join(k for k in B if B[k] != C[k]))
