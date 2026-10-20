"""emu-u (2026-10-18): the refix windows that still read AI in 445g, each from my meaning-fixed text again
(tools/refix_runs.py window_runs): HG18 (a third sample; 445g: two windows, 47 and 114 words), HG24 (445g: two
windows, 87 and 54 words), and HG06's third paragraph with the line after it (445g: AI with its neighbour; its
quotation, B5, is kept out as before). Run from fix-20261018/: python3 make_emu_u.py"""
import json, pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'tools'))
import refix_runs as R  # noqa: E402
import assemble as A  # noqa: E402
g434 = json.loads((HERE / 'b434' / 'GATE.json').read_text(encoding='utf-8'))
g441 = json.loads((HERE / 'b441' / 'GATE.json').read_text(encoding='utf-8'))
f445 = json.loads((HERE / 'b445' / 'flags.json').read_text(encoding='utf-8'))
cases = []
for key, g, dirs, name in (('HG18', g434, ['emu-r', 'emu-s'], 'HG18-refix2'), ('HG24', g441, ['emu-s'], 'HG24-refix')):
    fixed = str(HERE / g[key + '-fix']['reviews'])
    u = R.units_fixed(fixed, [HERE / d for d in dirs])
    tmp = HERE / 'rf-c' / ('%s.units.json' % key)
    tmp.parent.mkdir(exist_ok=True)
    tmp.write_text(json.dumps(u, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    pub = R.hit_published(tmp, f445[name]['flagged_blocks'])
    cases.append((fixed, R.fixed_draft_blocks(fixed, pub)))
cases.append((str(HERE / g434['HG06-fix']['reviews']), [3, 4]))
for f, bl in cases:
    print(pathlib.Path(f).name, bl)
R.window_runs(HERE / 'emu-u', cases, keep=dict(A.KEEP, HG06={5}))
