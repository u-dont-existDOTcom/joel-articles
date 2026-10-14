"""Section 4 ("The Four Parts That Have to Pl/ork Together"), 2026-10-02: the published text split into blocks,
and the Emulate inputs (40 words at least, plain text, no headings) for the paragraphs Pangram flagged.

As published the section read 87% AI (runs/pangram.jsonl, intentional-communities-baseline-04, 1,105 words):
AI from the heading to "fewer robes" (310 words); Human 83 (P8 to P11's "The adult reparents."); AI 35 (P11's last
sentence and P12); Human 70 (P13, P14); AI 607 (P15 to the end). No per-paragraph baseline checks: the section's
spans already say which paragraphs are flagged, and the credits go to the candidate checks."""
import json, pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, '/home/claude/work'); import mdplain
IC = HERE.parent.parent
src = (IC / 'sections/005-original.md').read_text(encoding='utf-8').strip()
blocks = [b.strip() for b in src.split('\n\n') if b.strip()]
assert len(blocks) == 39, len(blocks)
names = ['H1', 'IMG7', 'P1', 'P2', 'P3', 'H2', 'P4', 'P5', 'P6', 'P7', 'H3a', 'P8', 'P9', 'P10', 'IMG8', 'P11', 'P12',
         'P13', 'H3b', 'P14', 'P15', 'P16', 'P17', 'P18', 'P19', 'H3c', 'P20', 'P21', 'H3d', 'P22', 'P23', 'P24', 'P25',
         'P26', 'P27', 'P28', 'P29', 'P30', 'P31']
O = dict(zip(names, blocks))
json.dump(O, open(HERE / 'original-blocks.json', 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
plain = lambda md: mdplain.plain(md).strip()
wc = {k: len(plain(v).split()) for k, v in O.items() if not k.startswith('IMG')}
print(wc)
EMU = {'e1': ['P1', 'P2'], 'e2': ['P3', 'P4'], 'e3': ['P5', 'P6', 'P7'], 'e4': ['P11', 'P12'], 'e5': ['P15', 'P16'],
       'e6': ['P17', 'P18', 'P19'], 'e7': ['P20', 'P21'], 'e8': ['P22', 'P23', 'P24'], 'e9': ['P25'], 'e10': ['P26'],
       'e11': ['P27', 'P28'], 'e12': ['P29', 'P30', 'P31']}
(HERE / 'emu-in').mkdir(exist_ok=True)
json.dump(EMU, open(HERE / 'emu-in' / 'units.json', 'w'), indent=1)
for k, parts in EMU.items():
    t = plain('\n\n'.join(O[p] for p in parts)); (HERE / 'emu-in' / (k + '.txt')).write_text(t + '\n', encoding='utf-8'); print(k, len(t.split()))
