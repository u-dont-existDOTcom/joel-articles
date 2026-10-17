"""Section 14 draft v8 (2026-10-17): v7 with P2 back to v5's text. Taking the repeated food-housing-care question out of P2
made the paragraph read AI alone twice (313g, v6: 0.78; 315g, v7: 0.96), while v5's P2 reads Human alone (305g-x). The
question it keeps, "Who takes responsibility for bridging people's food, housing and care, and any outside cash or benefits,
if relevant?", asks who carries people through the handover, which P3's "assign a bridge or successor" leans on (round r5's
trace asked for "bridges" back for that reason). The rest of the dedup stays: the last paragraph's point in P5, the section
ending on the father paragraph, and "The Farm's communal economy". Writes v8.md. Run from this folder: python3 make_v8.py"""
import pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
blocks = lambda t: [b for b in re.split(r'\n\s*\n', t.strip())]
v5 = blocks((HERE / 'v5.md').read_text(encoding='utf-8'))
v7 = blocks((HERE / 'v7.md').read_text(encoding='utf-8'))
p2_5 = [b for b in v5 if b.startswith('If the community dissolves')][0]
p2_7 = [b for b in v7 if b.startswith('If the community dissolves')][0]
t = (HERE / 'v7.md').read_text(encoding='utf-8').replace(p2_7, p2_5)
assert t.count(p2_5) == 1
(HERE / 'v8.md').write_text(t, encoding='utf-8')
print('wrote v8.md')
