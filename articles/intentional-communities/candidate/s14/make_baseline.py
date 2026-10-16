"""Section 14's baseline (2026-10-16, Joel 18:22 UTC: "continue into next section now"): the published text of "Dissolution
and Exit" as it stands in HUMANIZED-SO-FAR.md, read by Pangram as a whole and in groups of at least 50 words (a short
paragraph goes with its neighbor, the heading with the paragraph under it). Batch 300g. Run from candidate/:
python3 s14/make_baseline.py

Every text is Joel's published wording, so each record is an owner record; the whole section is a measurement of the
published text, not an install (its repeats were read by the whole-article runs of 2026-10-14, fix-20261014b/gate/REPEATS.md).
"""
import json, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parent
sys.path.insert(0, str(C / 'fix-20261014'))
from ptext import blocks, section  # noqa: E402

H = '# Dissolution and Exit'
art = (C / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
B = [t for _, t in blocks(art, H)]
assert B[0] == 'Dissolution and Exit' and len(B) == 8, B
# 0 heading, 1 P1 founders, 2 P2 what happens, 3 P3 living will, 4 P4 dissolution terms, 5 P5 consolation, 6 P6 my father,
# 7 P7 even after
GROUPS = {'A': (0, 2), 'B': (3, 4), 'C': (5, 5), 'D': (5, 7)}  # P6 and P7 together are 47 words, so they go with P5
drafts, gate = {}, {}
for g, (a, b) in GROUPS.items():
    t = '\n\n'.join(B[a:b + 1])
    k = 'S14-' + g
    drafts[k] = t
    gate[k] = {'kind': 'owner', 'joel': 'the published text of section 14, Dissolution and Exit', 'blocks': [a, b],
               'words': len(t.split())}
    assert len(t.split()) >= 50, (k, len(t.split()))
drafts['S14v0'] = section(art, H)
gate['S14v0'] = {'kind': 'section', 'parts': ['installed'], 'repeats': 0,
                 'repeats_note': 'a measurement of the published section; fix-20261014b/gate/REPEATS.md read the whole article',
                 'words': len(drafts['S14v0'].split())}
out = HERE / 'b300'
(out / 'drafts.json').write_text(json.dumps(drafts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(out / 'GATE.json').write_text(json.dumps(gate, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
for k, v in gate.items():
    print(k, v['words'], drafts[k][:70].replace('\n', ' / '))
