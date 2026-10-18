"""emu-aw, emu-ax, emu-ay (2026-10-18, after 462g): the fast path for "Come all the way back" (HG18), the return steps.
Every version so far read AI or lost steps; 459g's HG18-ma (two medium windows of my fixed text) read 100% Human whole and
in every paragraph but lost four safety statements. HG36 went from AI to installed with one run of the whole section from
the published text (461g, 462g), and HG18's own first whole-section run from the published text read Human (431g). So:
  HG18-aw1  B0-B6, the whole section in one run
emu-aw and emu-ax from the published text, emu-ay from my meaning-fixed text (rev-b/HG18.fixed.json). For question 4: a
version that keeps every step and reads Human is an option for Joel, not an install, until he answers.
Run from fix-20261018/: python3 make_emu_aw.py
"""
import pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE.parent / 'tools'))
import make_emu_ac as E  # noqa: E402
import assemble as A  # noqa: E402

kb = A.kb()['HG18']


def pub(blocks, name):
    text = '\n\n'.join(kb[b][1] for b in blocks)
    heads = [b for b in blocks if kb[b][0].lstrip().startswith('#')]
    return (name, text, {'key': 'HG18', 'sent': list(blocks), 'flagged': [b for b in blocks if b not in heads], 'headings': heads,
                         'words': len(text.split()), 'input': 'published text', 'from': 'source/published-20260928.md B%d-B%d' % (blocks[0], blocks[-1])})


published = [pub(range(0, 7), 'HG18-aw1')]
fixed = [('HG18-aw1',) + E.window('HG18', HERE / 'rev-b' / 'HG18.fixed.json', range(0, 7))]
for r in published + fixed:
    print(r[0], r[2]['input'], r[2]['sent'], r[2]['headings'], r[2]['words'])
E.write('emu-aw', published, [])
E.write('emu-ax', published, [])
E.write('emu-ay', fixed, [])
