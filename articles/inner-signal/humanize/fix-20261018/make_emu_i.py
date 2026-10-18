"""Fourth Emulate samples (emu-i, 2026-10-18), after 437g (3 of 8 Human with whole-window runs: HG04, HG16, HG24). The
five left: HG17, HG37 and HG31 get their 437g window again as one run; HG29+30, whose prompt scripts (B29-B38) read AI in
every sample so far (431g, 436g, 437g), goes whole; HG38+39, whose Appendix J opening (B3) read AI in every sample, goes
from Appendix I to the second induction family (B0-B8), so Emulate sees more of it.
Run from humanize/: python3 fix-20261018/make_emu_i.py"""
import json, pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parent
sys.path.insert(0, str(H / 'tools'))
import assemble as A  # noqa: E402
import emu_runs as E  # noqa: E402

kb = A.kb()
D = lambda *xs: [HERE / x for x in xs]
fl437 = json.load(open(HERE / 'b437' / 'flags.json', encoding='utf-8'))
flags = {}
for key, dirs in (('HG17', D('emu-a', 'emu-e', 'emu-g', 'emu-h')), ('HG37', D('emu-a', 'emu-c', 'emu-g', 'emu-h'))):
    pubs, runs = A.published_flags(key, dirs, fl437[key + '-emuH']['flagged_blocks'])
    flags[key] = {'flagged_blocks': pubs, 'from_screen': '437g ' + key + '-emuH'}
SK = {'emu-g/HG31-r1-s4', 'emu-g/HG31-r1-s5', 'emu-g/HG31-r1-s7', 'emu-g/HG31-r1-s8'}
pubs, runs = A.published_flags('HG31', D('emu-e', 'emu-f', 'emu-g', 'emu-h'), fl437['HG31-emuH']['flagged_blocks'], SK)
flags['HG31'] = {'flagged_blocks': pubs, 'from_screen': '437g HG31-emuH'}
flags['HG29+30'] = {'flagged_blocks': [i for i, b in enumerate(kb['HG29+30']) if not b[2]], 'from_screen': 'whole section'}
flags['HG38+39'] = {'flagged_blocks': [i for i in range(0, 9) if not kb['HG38+39'][i][2]], 'from_screen': 'B0-B8 (437g: B3)'}
out = HERE / 'emu-i'
out.mkdir(exist_ok=True)
(out / 'flags-published.json').write_text(json.dumps(flags, indent=1) + '\n', encoding='utf-8')
subprocess.run([sys.executable, str(H / 'tools' / 'emu_runs.py'), 'make', str(out / 'flags-published.json'), str(out)], check=True)
