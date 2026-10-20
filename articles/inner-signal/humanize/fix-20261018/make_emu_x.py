"""emu-x (2026-10-18): third refix samples of the AI windows 449g left in HG17 (411 words) and HG31 (837 and 32 words),
from my meaning-fixed text again (tools/refix_runs.py window_runs over the refix units of emu-t and emu-v).
Run from fix-20261018/: python3 make_emu_x.py"""
import json, pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'tools'))
import refix_runs as R  # noqa: E402
g444 = json.loads((HERE / 'b444' / 'GATE.json').read_text(encoding='utf-8'))
f449 = json.loads((HERE / 'b449' / 'flags.json').read_text(encoding='utf-8'))
cases = []
for key in ('HG17', 'HG31'):
    fixed = str(HERE / g444[key + '-fix']['reviews'])
    u = R.units_fixed(fixed, [HERE / 'emu-t', HERE / 'emu-v'])
    tmp = HERE / 'rf-e' / ('%s.units.v.json' % key)
    tmp.write_text(json.dumps(u, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    pub = R.hit_published(tmp, f449[key + '-refix2']['flagged_blocks'])
    cases.append((fixed, R.fixed_draft_blocks(fixed, pub)))
    print(key, len(cases[-1][1]), 'fixed blocks')
R.window_runs(HERE / 'emu-x', cases)
