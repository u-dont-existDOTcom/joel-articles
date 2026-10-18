"""emu-at, emu-au, emu-av (2026-10-18, after 459g): new samples of "Altered states" (HG36), the one open section whose
problem is Pangram's and not a question for Joel. Its end keeps an AI window in every version: Joel's B10-B12 as published
(455g), B10-B11 from new samples over the installed B9 and B12 (456g, 457g, 459g: the AI window moved to B8-B12 or B10-B12,
though each paragraph read Human alone in 459g's HG36-ea). So these samples rewrite whole stretches in one run, so that
no window mixes runs:
  HG36-sw1  B8-B12 (the "Stabilize before you interpret" subsection, its heading with it)
  HG36-aw1  B0-B12 (the whole section; 431g's first Emulate screen of the whole section read Human)
emu-at and emu-au from my meaning-fixed text (rf-p/HG36.fixed.json; 459g's best-kept meaning came from it), emu-av from the
published text.
Run from fix-20261018/: python3 make_emu_at.py
"""
import json, pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE.parent / 'tools'))
import make_emu_ac as E  # noqa: E402
import assemble as A  # noqa: E402

F36 = HERE / 'rf-p' / 'HG36.fixed.json'
kb = A.kb()['HG36']


def pub(blocks, name):
    text = '\n\n'.join(kb[b][1] for b in blocks)
    heads = [b for b in blocks if kb[b][0].lstrip().startswith('#')]
    return (name, text, {'key': 'HG36', 'sent': list(blocks), 'flagged': [b for b in blocks if b not in heads], 'headings': heads,
                         'words': len(text.split()), 'input': 'published text', 'from': 'source/published-20260928.md B%d-B%d' % (blocks[0], blocks[-1])})


fixed = [('HG36-sw1',) + E.window('HG36', F36, range(8, 13)), ('HG36-aw1',) + E.window('HG36', F36, range(0, 13))]
published = [pub(range(8, 13), 'HG36-sw1'), pub(range(0, 13), 'HG36-aw1')]
for r in fixed + published:
    print(r[0], r[2]['input'], r[2]['sent'], r[2]['headings'], r[2]['words'])
E.write('emu-at', fixed, [])
E.write('emu-au', fixed, [])
E.write('emu-av', published, [])
