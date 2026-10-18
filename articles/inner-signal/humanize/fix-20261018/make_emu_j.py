"""Fifth Emulate samples (emu-j, 2026-10-18), after 438g (HG29+30 Human from its whole run; four left, each with small
windows now): HG17 B0-B3 (117 words, Medium), HG37 B17 (40 words), HG38+39 B3-B6 (160 words), HG31's three (B18-B19,
B42-B45, B89-B104). Each window as one run of its published blocks.
Run from humanize/: python3 fix-20261018/make_emu_j.py"""
import json, pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parent
sys.path.insert(0, str(H / 'tools'))
import assemble as A  # noqa: E402

D = lambda *xs: [HERE / x for x in xs]
fl = json.load(open(HERE / 'b438' / 'flags.json', encoding='utf-8'))
SK = {'emu-g/HG31-r1-s4', 'emu-g/HG31-r1-s5', 'emu-g/HG31-r1-s7', 'emu-g/HG31-r1-s8'}
flags = {}
for key, dirs, skip in (('HG17', D('emu-a', 'emu-e', 'emu-g', 'emu-h', 'emu-i'), ()), ('HG37', D('emu-a', 'emu-c', 'emu-g', 'emu-h', 'emu-i'), ()),
                        ('HG38+39', D('emu-a', 'emu-c', 'emu-g', 'emu-h', 'emu-i'), ()), ('HG31', D('emu-e', 'emu-f', 'emu-g', 'emu-h', 'emu-i'), SK)):
    pubs, runs = A.published_flags(key, dirs, fl[key + '-emuI']['flagged_blocks'], skip)
    flags[key] = {'flagged_blocks': pubs, 'from_screen': '438g %s-emuI' % key}
out = HERE / 'emu-j'
out.mkdir(exist_ok=True)
(out / 'flags-published.json').write_text(json.dumps(flags, indent=1) + '\n', encoding='utf-8')
subprocess.run([sys.executable, str(H / 'tools' / 'emu_runs.py'), 'make', str(out / 'flags-published.json'), str(out)], check=True)
