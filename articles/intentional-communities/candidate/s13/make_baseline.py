"""Section 13's baseline: the published text, as it stands in HUMANIZED-SO-FAR.md (one line fixed on 2026-10-12),
read by Pangram as a whole and in groups of at least 50 words (a short paragraph goes with its neighbors, a heading
with the paragraph under it). Run from candidate/: python3 s13/make_baseline.py

Every text is Joel's published wording, so each record is an owner record. The whole section's record carries the
repeats run of 2026-10-14 21:19 (fix-20261014b/gate/REPEATS.md), which read section 13 too; this is a measurement
of the published text, not an install.
"""
import json, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parent
sys.path.insert(0, str(C / 'fix-20261014'))
from ptext import blocks, section  # noqa: E402

art = (C / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
B = [t for _, t in blocks(art, '# Your Little Forming Group Already Is the Community')]
GROUPS = {'A': (0, 3), 'B': (4, 6), 'C': (7, 9), 'D': (10, 11), 'E': (12, 13), 'F': (14, 17), 'G': (18, 18),
          'H': (19, 20), 'I': (21, 24), 'J': (25, 26), 'K': (27, 28), 'L': (29, 30), 'M': (31, 32), 'N': (33, 34),
          'O': (35, 35), 'P': (36, 36), 'Q': (36, 37)}
drafts, gate = {}, {}
for g, (a, b) in GROUPS.items():
    t = '\n\n'.join(B[a:b + 1])
    k = 'S13-' + g
    drafts[k] = t
    gate[k] = {'kind': 'owner', 'joel': 'the published text (section 13 is the published text except one line he fixed on 2026-10-12)',
               'blocks': [a, b], 'words': len(t.split())}
    assert len(t.split()) >= 50, (k, len(t.split()))
drafts['S13v0'] = section(art, '# Your Little Forming Group Already Is the Community')
gate['S13v0'] = {'kind': 'section', 'parts': ['installed'], 'repeats': 0,
                 'repeats_note': 'a measurement of the published section; fix-20261014b/gate/REPEATS.md read it on 2026-10-14',
                 'words': len(drafts['S13v0'].split())}
(HERE / 'drafts.json').write_text(json.dumps(drafts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(HERE / 'GATE.json').write_text(json.dumps(gate, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
for k, v in gate.items():
    print(k, v['words'], drafts[k][:70].replace('\n', ' / '))
