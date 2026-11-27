"""apply_h82.py - turn 74's checked texts into the guide, in the section's new order, from the repo root:

  python3 articles/bad-trips/humanize/h82-20261127/apply_h82.py         his answers in (done first)
  python3 articles/bad-trips/humanize/h82-20261127/apply_h82.py fix     the two fixes after the section's second check

- B171, where people still find it and a name to look for (his round-63 comment on TEACH-B173): try 3, Human High 69 in
  one window by itself (0e0bd36d).
- B173, his TEACH-B173 version whole (his check, Human High 84 in one window, 09e42ca2) with "(the dried juice)" from his
  comment where the extract paste is first named: Human High 87 in one window by itself (bf3ae1f3). It now comes before
  B174, so the skin route's amounts can point back to it (the fit read couldn't tell which of two doses ended a trip).
- B174, his SKIN-AMOUNT answer: "sensitive skin" back in (Human High 122, 385cddfb), then the amounts as the same as by
  mouth, or a few drops of fresh juice: Human High 143 in one window with B171 (3da1f8d2).
apply_gate.py runs first, on every text of mine here (B173 is his version with three words of mine, so it goes through
the gate too).
"""
import importlib.util
import json
import pathlib
import sys

REPO = pathlib.Path(__file__).resolve().parents[4]
ART = REPO / 'articles' / 'bad-trips'
HERE = ART / 'humanize' / 'h82-20261127'
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
import apply_gate  # noqa: E402

spec = importlib.util.spec_from_file_location('build_h82', HERE / 'build_h82.py')
b = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b)
NEW = {'B171': b.B171_V, 'B173': b.B173_D1, 'B174': b.B174_S7}
if sys.argv[1:] == ['fix']:
    # after the section's second check (3a2d2b12): B173 with "Eating a whole leaf" (Human High 88 by itself, 9bae6cd1) and
    # B176 with its last line's payoff first (Human High 87 with B178, 79f9e21f)
    T1 = {x['id']: x['md'] for x in json.loads((ART / 'GUIDE-SO-FAR-blocks.json').read_text(encoding='utf-8'))}
    assert T1['B173'] == b.B173_D1 and T1['B176'] == b.T0['B176'], 'run apply_h82.py first'
    NEW = {'B173': b.B173_F1, 'B176': b.B176_F1}
    b.T0 = dict(b.T0, B173=b.B173_D1)

apply_gate.require(ART / 'humanize' / 'pangram-ledger.jsonl', list(NEW.values()))
blocks = json.loads((ART / 'GUIDE-SO-FAR-blocks.json').read_text(encoding='utf-8'))
by = {x['id']: x for x in blocks}
for k, v in NEW.items():
    assert by[k]['md'] == b.T0[k], k + ' changed since the turn began'
    by[k]['md'] = v
first = min(i for i, x in enumerate(blocks) if x['id'] in b.ORDER)
rest = [x for x in blocks if x['id'] not in b.ORDER]
out = rest[:first] + [by[k] for k in b.ORDER] + rest[first:]
assert len(out) == len(blocks)
(ART / 'GUIDE-SO-FAR.md').write_text('\n\n'.join(x['md'] for x in out) + '\n', encoding='utf-8')
(ART / 'GUIDE-SO-FAR-blocks.json').write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('applied: ' + ', '.join(NEW) + '; order: ' + ', '.join(b.ORDER))
