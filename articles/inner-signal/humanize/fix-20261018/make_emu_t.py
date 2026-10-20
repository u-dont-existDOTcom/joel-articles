"""emu-t (2026-10-18): refix runs for 444g's five fixed sections, which all read AI with my fixes in (HG16, HG17, HG31,
HG37, HG38+39): each window that read AI, from my meaning-fixed text (tools/refix_runs.py window_runs), as emu-r did
for 434g (17 of 21 then read 100% Human in 443g). Run from fix-20261018/: python3 make_emu_t.py"""
import json, pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'tools'))
import refix_runs as R  # noqa: E402
g = json.loads((HERE / 'b444' / 'GATE.json').read_text(encoding='utf-8'))
fl = json.loads((HERE / 'b444' / 'flags.json').read_text(encoding='utf-8'))
cases = [(str(HERE / g[k]['reviews']), fl[k]['flagged_blocks']) for k in sorted(fl) if fl[k].get('flagged_blocks')]
R.window_runs(HERE / 'emu-t', cases)
