"""apply_h80.py - turn 72's checked Beach Morning Glory into the guide, from the repo root:

  python3 articles/bad-trips/humanize/h80-20261127/apply_h80.py

Each paragraph read Human High in every window by itself or with a neighbour (apply_gate.py, which this runs first):
- B171, which plant and what it is for, with B172 joined in (block B172 deleted): try 2, Human High 56 (ecce6d40), and
  Human High 92 with B174 (bb2893ad);
- B174, handling the leaf, moved up before the amounts: Human High 92 with B171 (bb2893ad);
- B173, how much does what, with B175's whole leaf moved to its start (block B175 deleted): Human High 67 (6bc70ed9);
- B176, the woman, try 3: Human High 86 with B178 (2dfaa7bb);
- B178, the MDMA limit, its list cut to the link: Human High 86 with B176 (2dfaa7bb). The list's line held no caution
  (FIDELITY-KEYS-R61.json, not_cautions W054, his CHARCOAL-WORDS "a"), and its link's words are now the section's name, so
  SECTION-LINKS.json's entry for B178 changes with it.
"""
import importlib.util
import json
import pathlib
import sys

REPO = pathlib.Path(__file__).resolve().parents[4]
ART = REPO / 'articles' / 'bad-trips'
HERE = ART / 'humanize' / 'h80-20261127'
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
import apply_gate  # noqa: E402

spec = importlib.util.spec_from_file_location('build_h80', HERE / 'build_h80.py')
b = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b)
NEW = {'B171': b.P1_FINAL, 'B174': b.P3_FINAL, 'B173': b.BMG['P2'], 'B176': b.P4_FINAL, 'B178': b.BMG['P5']}
ORDER = ['B171', 'B174', 'B173', 'B176', 'B178']
GONE = ['B172', 'B175']

apply_gate.require(ART / 'humanize' / 'pangram-ledger.jsonl', [NEW[k] for k in ORDER])
blocks = json.loads((ART / 'GUIDE-SO-FAR-blocks.json').read_text(encoding='utf-8'))
by = {x['id']: x for x in blocks}
first = min(i for i, x in enumerate(blocks) if x['id'] in ORDER + GONE)
rest = [x for x in blocks if x['id'] not in ORDER + GONE]
for k in ORDER:
    by[k]['md'] = NEW[k]
out = rest[:first] + [by[k] for k in ORDER] + rest[first:]
assert len(out) == len(blocks) - len(GONE)
(ART / 'GUIDE-SO-FAR.md').write_text('\n\n'.join(x['md'] for x in out) + '\n', encoding='utf-8')
(ART / 'GUIDE-SO-FAR-blocks.json').write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')

c = ART / 'SECTION-LINKS.json'
cat = json.loads(c.read_text(encoding='utf-8'))
hit = [x for x in cat['links'] if x['block'] == 'B178' and x['href'] == '#§mdma-magnesium-alarm']
assert len(hit) == 1
hit[0]['text'] = 'MDMA: Magnesium Alarm'
c.write_text(json.dumps(cat, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('applied: ' + ', '.join(ORDER) + ' (in that order); deleted: ' + ', '.join(GONE))
