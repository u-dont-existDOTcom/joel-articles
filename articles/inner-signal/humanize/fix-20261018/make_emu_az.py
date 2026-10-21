"""emu-az, emu-ba, emu-bb (2026-10-21, after Joel's answers of 17:56 UTC): the fast path for the induction section (HG17),
which holds the listening script. Joel, question 4: "i am fine with all the humanized replacements as long as we don't lose
anything". Every Human version so far lost steps (451g HG17-refix3: 11 to 26 of the script's; 459g HG17-mb: 19 to 31
points), and the pieces that kept them read AI where the runs met. The return steps (HG18) and Appendix G (HG36) went
from AI to installed with one run of the whole section from the published text (463g, 461g), so:
  HG17-az1  B0-B75, the whole section in one run (2,012 words), three samples
Each sample then gets a second reader against the published text; the one that keeps the most gets every lost point put
back inside its own sentences (the community lesson, docs/HUMANIZATION-GATE.md: put the meaning back into Emulate's
sentence, not the published one), the gate's reviews, and its reading in the next whole-guide recheck through Substack.
Run from fix-20261018/: python3 make_emu_az.py
"""
import pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE.parent / 'tools'))
import make_emu_ac as E  # noqa: E402
import assemble as A  # noqa: E402

kb = A.kb()['HG17']


def pub(blocks, name):
    text = '\n\n'.join(kb[b][1] for b in blocks)
    heads = [b for b in blocks if kb[b][0].lstrip().startswith('#')]
    return (name, text, {'key': 'HG17', 'sent': list(blocks), 'flagged': [b for b in blocks if b not in heads], 'headings': heads,
                         'words': len(text.split()), 'input': 'published text', 'from': 'source/published-20260928.md B%d-B%d' % (blocks[0], blocks[-1])})


published = [pub(range(0, len(kb)), 'HG17-az1')]
for r in published:
    print(r[0], r[2]['input'], len(r[2]['sent']), 'blocks', r[2]['headings'], r[2]['words'], 'words')
for folder in ('emu-az', 'emu-ba', 'emu-bb'):
    E.write(folder, published, [])
