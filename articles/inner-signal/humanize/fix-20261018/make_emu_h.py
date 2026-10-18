"""Third Emulate samples (emu-h, 2026-10-18), after 436g: second samples of the short pieces inside the AI windows fixed
none of the seven sections (0 of 7 Human). This round sends each AI window's published blocks as one run with its
headings (the method of emu-a: whole stretches, not 40-to-180-word pieces), so Emulate rewrites the window in one
context: HG04 whole (its one window covered everything in 436g), HG16, HG29+30, HG17, HG37, HG38+39 and HG31 from
436g's windows, and HG24 from 435g's (the troubleshooting section's short scripts, from "You dissociate" to the end).
Run from humanize/: python3 fix-20261018/make_emu_h.py"""
import json, pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parent
sys.path.insert(0, str(H / 'tools'))
import assemble as A  # noqa: E402

D = lambda *xs: [HERE / x for x in xs]
SKIP31 = {'emu-g/HG31-r1-s4', 'emu-g/HG31-r1-s5', 'emu-g/HG31-r1-s7', 'emu-g/HG31-r1-s8'}
CASES = {  # key: (batch, screen name, dirs, skip)
 'HG04': ('b436', 'HG04-emuG', D('emu-a', 'emu-g'), ()),
 'HG16': ('b436', 'HG16-emuG', D('emu-a', 'emu-g'), ()),
 'HG29+30': ('b436', 'HG29+30-emuG', D('emu-a', 'emu-g'), ()),
 'HG17': ('b436', 'HG17-emuG', D('emu-a', 'emu-e', 'emu-g'), ()),
 'HG37': ('b436', 'HG37-emuG', D('emu-a', 'emu-c', 'emu-g'), ()),
 'HG38+39': ('b436', 'HG38+39-emuG', D('emu-a', 'emu-c', 'emu-g'), ()),
 'HG31': ('b436', 'HG31-emuG', D('emu-e', 'emu-f', 'emu-g'), SKIP31),
 'HG24': ('b435', 'HG24-emuF', D('emu-c', 'emu-f'), ()),
}
flags = {}
for key, (b, name, dirs, skip) in CASES.items():
    fl = json.load(open(HERE / b / 'flags.json' if (HERE / b / 'flags.json').exists() else '/dev/null', encoding='utf-8')) if (HERE / b / 'flags.json').exists() else None
    if fl is None:
        r = subprocess.run([sys.executable, str(H / 'tools' / 'flagged.py'), str(HERE / b / 'drafts.json'), str(HERE / b / ('%s-results.json' % b)),
                            '--out', str(HERE / b / 'flags.json')], capture_output=True, text=True)
        fl = json.load(open(HERE / b / 'flags.json', encoding='utf-8'))
    pubs, runs = A.published_flags(key, dirs, fl[name]['flagged_blocks'], skip)
    flags[key] = {'flagged_blocks': pubs, 'from_screen': '%s %s' % (b, name), 'runs_in_window': runs}
    print('%-8s %s: published blocks %s' % (key, name, pubs))
out = HERE / 'emu-h'
out.mkdir(exist_ok=True)
(out / 'flags-published.json').write_text(json.dumps(flags, indent=1) + '\n', encoding='utf-8')
subprocess.run([sys.executable, str(H / 'tools' / 'emu_runs.py'), 'make', str(out / 'flags-published.json'), str(out)], check=True)
