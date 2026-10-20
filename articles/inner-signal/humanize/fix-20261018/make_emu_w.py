"""emu-w (2026-10-18): the stretches the triage sent back for a new sample (more than a quarter of their words would need
fixing): HG35 B17 (rf-a/HG35.triage.json) and HG06 B6 (rf-b/HG06.triage.json), each from my meaning-fixed text
(tools/refix_runs.py window_runs). Run from fix-20261018/: python3 make_emu_w.py"""
import json, pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'tools'))
import refix_runs as R  # noqa: E402
import assemble as A  # noqa: E402
g434 = json.loads((HERE / 'b434' / 'GATE.json').read_text(encoding='utf-8'))
cases = []
for key, blocks in (('HG35', {17}), ('HG06', {6})):
    fixed = str(HERE / g434[key + '-fix']['reviews'])
    cases.append((fixed, R.fixed_draft_blocks(fixed, blocks)))
    print(key, cases[-1][1])
R.window_runs(HERE / 'emu-w', cases, keep=dict(A.KEEP, HG06={5}))
