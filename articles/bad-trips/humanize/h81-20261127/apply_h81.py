"""apply_h81.py - turn 73's checked step into the guide, from the repo root:

  python3 articles/bad-trips/humanize/h81-20261127/apply_h81.py

B174, the handling paragraph, with all of his round-62 LEAF-JUICE answer in (the juice relaxes him; it works through the
skin almost as well as eating the leaf; the armpits, for example, to give it on purpose): try 5 of its lineage, Human High
122 in one window with B171 before it (6026d11b). apply_gate.py runs first.

B173 stays as it is: with his NIBBLE-SIZE amounts in, its nibble sentence read Medium 16 in a window of its own in every
step (ddea8d92, 10d2a2a5, 5772af1d; Low 37 joined to the sentence before, b771d740), and its lineage has used its six
tries, so it goes to him as round 63's TEACH-B173 with his amounts in it.
"""
import importlib.util
import json
import pathlib
import sys

REPO = pathlib.Path(__file__).resolve().parents[4]
ART = REPO / 'articles' / 'bad-trips'
HERE = ART / 'humanize' / 'h81-20261127'
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
import apply_gate  # noqa: E402

spec = importlib.util.spec_from_file_location('build_h81', HERE / 'build_h81.py')
b = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b)
NEW = {'B174': b.B174_S3}

apply_gate.require(ART / 'humanize' / 'pangram-ledger.jsonl', list(NEW.values()))
blocks = json.loads((ART / 'GUIDE-SO-FAR-blocks.json').read_text(encoding='utf-8'))
by = {x['id']: x for x in blocks}
for k, v in NEW.items():
    assert by[k]['md'] == b.T0[k], k + ' changed since the turn began'
    by[k]['md'] = v
(ART / 'GUIDE-SO-FAR.md').write_text('\n\n'.join(x['md'] for x in blocks) + '\n', encoding='utf-8')
(ART / 'GUIDE-SO-FAR-blocks.json').write_text(json.dumps(blocks, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('applied: ' + ', '.join(NEW))
