"""emu-s (2026-10-18): the next refix runs. Each from my meaning-fixed text (tools/refix_runs.py window_runs):
the windows of 443g's refix screens that still read AI (HG18, HG23, HG36: a second sample, from the fixed text again),
the windows of 441g's fixed sections that read AI (HG24, HG29+30), and the paragraphs of 442g's paragraph checks that read
AI alone (HG04 P1-P2, HG06 P3-P6; their sections read Human whole). HG02+03's one window is Joel's own table-of-contents
note, kept as he wrote it (a question for him). A quotation of someone else (HG06 B5) is never sent. Run from fix-20261018/: python3 make_emu_s.py"""
import json, pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'tools'))
import refix_runs as R  # noqa: E402
g434 = json.loads((HERE / 'b434' / 'GATE.json').read_text(encoding='utf-8'))
g441 = json.loads((HERE / 'b441' / 'GATE.json').read_text(encoding='utf-8'))
f443 = json.loads((HERE / 'b443' / 'flags.json').read_text(encoding='utf-8'))
f441 = json.loads((HERE / 'b441' / 'flags.json').read_text(encoding='utf-8'))
cases = []
for key in ('HG18', 'HG23', 'HG36'):
    fixed = str(HERE / g434[key + '-fix']['reviews'])
    units = R.units_fixed(fixed, [HERE / 'emu-r'])
    tmp = HERE / 'rf-a' / ('%s.units.json' % key)
    tmp.write_text(json.dumps(units, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    pub = R.hit_published(tmp, f443[key + '-refix']['flagged_blocks'])
    cases.append((fixed, R.fixed_draft_blocks(fixed, pub)))
for key in ('HG24', 'HG29+30'):
    fixed = str(HERE / g441[key + '-fix']['reviews'])
    cases.append((fixed, f441[key + '-fix']['flagged_blocks']))
cases.append((str(HERE / g441['HG04-fix']['reviews']), [1, 2]))       # 442g: P1 (with P2) and P2 alone read AI
cases.append((str(HERE / g434['HG06-fix']['reviews']), [3, 4, 5, 6])) # 442g: P3 to P6 read AI alone or in their pairs
for f, bl in cases:
    print(pathlib.Path(f).name, bl)
import assemble as A  # noqa: E402
# HG06 B5 is a quotation (the Silva Mind Control line): it stays word for word, so it isn't sent
R.window_runs(HERE / 'emu-s', cases, keep=dict(A.KEEP, HG06={5}))
