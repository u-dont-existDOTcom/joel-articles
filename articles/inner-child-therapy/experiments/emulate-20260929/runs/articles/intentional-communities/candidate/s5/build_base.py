"""Section 5 ("The Medicine Part, Without Pretending It Isn't There"), 2026-10-03: the published text split into
blocks, and the Emulate inputs for runs of paragraphs (the section 4 lesson: a run sent as one unit reads as one
voice). As published the section read 97% AI (runs/pangram.jsonl, intentional-communities-baseline-05, 1,388 words):
AI from the heading to P10's first sentence ("Depth can increase alienation."), Human for P10's next two sentences
(Joel's ayahuasca at 26 and the monasteries, 39 words), AI from "That helped produce a God complex" to the end."""
import json, pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, '/home/claude/work'); import mdplain
IC = HERE.parent.parent
src = (IC / 'sections/006-original.md').read_text(encoding='utf-8').strip()
blocks = [b.strip() for b in src.split('\n\n') if b.strip()]
names = ['H1'] + ['P%d' % i for i in range(1, 9)] + ['H2a'] + ['P%d' % i for i in range(9, 18)] + ['H2b'] + \
        ['P%d' % i for i in range(18, 29)] + ['H2c', 'IMG9'] + ['P%d' % i for i in range(29, 34)]
assert len(blocks) == len(names), (len(blocks), len(names))
O = dict(zip(names, blocks))
for k in ('H2a', 'H2b', 'H2c'): assert O[k].startswith('## '), k
assert O['IMG9'].startswith('[image 9]')
json.dump(O, open(HERE / 'original-blocks.json', 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
plain = lambda md: mdplain.plain(md).strip()
EMU = {'e1': ['P1', 'P2'], 'e2': ['P3', 'P4', 'P5'], 'e3': ['P6', 'P7', 'P8'], 'e4': ['P9', 'P10', 'P11'],
       'e5': ['P12', 'P13', 'P14'], 'e6': ['P15', 'P16', 'P17'], 'e7': ['P18', 'P19', 'P20'], 'e8': ['P21', 'P22', 'P23'],
       'e9': ['P24', 'P25', 'P26'], 'e10': ['P27', 'P28'], 'e11': ['P29', 'P30', 'P31'], 'e12': ['P32', 'P33']}
json.dump(EMU, open(HERE / 'emu-in' / 'units.json', 'w'), indent=1)
d = {}
for k, parts in EMU.items():
    t = plain('\n\n'.join(O[p] for p in parts)); d[k] = t + '\n'
    (HERE / 'emu-in' / (k + '.txt')).write_text(t + '\n', encoding='utf-8')
json.dump(d, open(HERE / 'emu-in' / 'inputs.json', 'w', encoding='utf-8'), ensure_ascii=False)
print({k: len(v.split()) for k, v in d.items()})
